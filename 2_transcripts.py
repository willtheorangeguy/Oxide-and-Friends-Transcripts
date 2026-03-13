"""
This script scrapes transcripts from transistor.fm for the Oxide and Friends
podcast episodes.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# Feed and URL constants
RSS_URL = "https://feeds.transistor.fm/oxide-and-friends"
TRANSCRIPT_URL = "https://share.transistor.fm/s/{token}/transcript"

# Log file name
LOG_FILENAME = "transcribed.log"

# Polite delay
REQUEST_DELAY = 1.5

# HTTP headers to mimic a real browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


# RSS fetching and parsing
def fetch_rss(url: str) -> list[dict]:
    """Download the RSS feed and return a list of episode dicts."""
    print(f"Fetching RSS feed: {url}")
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    # Parse the XML feed
    root = ET.fromstring(response.content)
    episodes = []

    # Each episode is an <item> with <title>, <link>, and <pubDate>
    for item in root.findall(".//item"):
        title_el   = item.find("title")
        link_el    = item.find("link")
        pubdate_el = item.find("pubDate")

        # Skip if any of the required elements are missing
        if title_el is None or link_el is None or pubdate_el is None:
            continue

        title      = (title_el.text   or "").strip()
        link       = (link_el.text    or "").strip()
        pubdate_str = (pubdate_el.text or "").strip()

        # Extract the 8-char share token from the URL
        m = re.search(r"/s/([0-9a-f]+)(?:/|$)", link)
        if not m:
            continue
        token = m.group(1)

        # Parse publication year
        try:
            pub_date = datetime.strptime(pubdate_str[:25].rstrip(), "%a, %d %b %Y %H:%M:%S")
            year = str(pub_date.year)
        except ValueError:
            try:
                # Some dates omit the day-of-week
                pub_date = datetime.strptime(pubdate_str[:16].rstrip(), "%d %b %Y %H:%M")
                year = str(pub_date.year)
            except ValueError:
                print(f"Cannot parse date '{pubdate_str}' for '{title}' – skipping")
                continue

        # Append episode info to the list
        episodes.append(
            {
                "title":  title,
                "link":   link,
                "token":  token,
                "year":   year,
            }
        )

    print(f"Found {len(episodes)} episodes in feed.")
    return episodes

# Characters that yt-dlp (and Windows) forbid in filenames
_ILLEGAL_CHARS_RE = re.compile(r'[\\/:*?"<>|]')

# Sanitize a podcast title
def sanitize_title(title: str) -> str:
    """Turn a podcast title into a filename-safe string that matches yt-dlp's
    Windows sanitisation."""
    sanitized = _ILLEGAL_CHARS_RE.sub("_", title)
    sanitized = sanitized.strip(". ")
    return sanitized


def find_existing_base(folder: str, title: str) -> str | None:
    """Look inside *folder* for an existing .mp3 whose stem fuzzy-matches *title*.
    Returns the bare stem (no extension) if found, otherwise None."""
    if not os.path.isdir(folder):
        return None

    clean_title = sanitize_title(title).lower()
    # Also strip any bracketed ID that yt-dlp can append
    clean_title_no_id = re.sub(r"\s*\[[^\]]+\]\s*$", "", clean_title).strip()

    # Look for .mp3 files in the folder and try to match them to the title
    for fname in os.listdir(folder):
        if not fname.lower().endswith(".mp3"):
            continue
        stem = os.path.splitext(fname)[0]
        # Strip yt-dlp's appended ID from the on-disk name too
        stem_clean = re.sub(r"\s*\[[^\]]+\]\s*$", "", stem).strip().lower()

        # Exact match or close match
        if stem_clean == clean_title_no_id or stem.lower() == clean_title.lower():
            return os.path.splitext(fname)[0]   # return original-case stem
    
    return None

# Transcript fetching and scraping
def fetch_transcript(token: str) -> str | None:
    """Fetch the transistor.fm transcript page for *token* and return a formatted
    string where each line looks like:
        [Speaker Name] [MM:SS] Utterance text goes here.
    Returns None if no transcript found or on error."""
    # Get transcript page HTML
    url = TRANSCRIPT_URL.format(token=token)

    # We use a long timeout and catch exceptions to avoid crashing the whole script
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
    except requests.RequestException as exc:
        print(f"Request failed for {url}: {exc}")
        return None

    # Handle HTTP errors gracefully
    if resp.status_code == 404:
        print(f"No transcript available (404) for token {token}")
        return None
    # Treat 403 Forbidden as "no transcript"
    if not resp.ok:
        print(f"HTTP {resp.status_code} for {url}")
        return None

    # Initialize BeautifulSoup to parse the HTML
    soup = BeautifulSoup(resp.text, "html.parser")

    # Strategy 1: look for a dedicated transcript container
    # Transistor renders each utterance inside an element that contains both
    # a speaker label and its body text.  Common class names / structures:
    utterances = _parse_utterances_structured(soup)

    # Strategy 2: fallback – extract raw text and use regex
    if not utterances:
        utterances = _parse_utterances_text(soup)

    if not utterances:
        print(f"⚠ Could not parse transcript for token {token}")
        return None

    # Format lines identically to how 2_transcriber.py stores Whisper output,
    # except we include the speaker name (which Whisper cannot provide):
    #   [Speaker Name] [MM:SS] Utterance text.
    lines = []
    for u in utterances:
        speaker = u.get("speaker", "Unknown")
        ts      = u.get("time", "")
        text    = u.get("text", "").strip()
        if text:
            lines.append(f"[{speaker}] [{ts}] {text}")

    return "\n".join(lines)

# Parsing strategies for the transcript page
def _parse_utterances_structured(soup: BeautifulSoup) -> list[dict]:
    """Parse utterances from the Transistor.fm transcript page HTML structure."""
    utterances = []

    # Find the transcript section
    section = soup.find(
        "section",
        class_=lambda c: c and "episode-transcript" in c,
    )
    if section is None:
        return utterances

    # We expect a repeating pattern of <cite>Speaker Name</cite>, 
    # <time><a>MM:SS</a></time>, and <p>Utterance text</p>.
    current_speaker: str | None = None
    current_time: str | None = None
    body_parts: list[str] = []

    # Helper to flush the current utterance
    def _flush():
        if current_speaker and current_time and body_parts:
            utterances.append(
                {
                    "speaker": current_speaker,
                    "time":    current_time,
                    "text":    " ".join(body_parts).strip(),
                }
            )

    # Iterate through the children of the section to extract speakers, timestamps, and text
    for child in section.children:
        # Skip plain text / whitespace nodes
        if not hasattr(child, "name") or child.name is None:
            continue

        tag = child.name.lower()

        if tag == "cite":
            # New speaker – flush the previous utterance first
            _flush()
            body_parts = []
            current_time = None
            # Strip the trailing colon that Transistor appends to speaker names
            current_speaker = child.get_text(strip=True).rstrip(":").strip()

        elif tag == "time":
            # The timestamp anchor is the <a> inside <time>
            a = child.find("a")
            if a:
                current_time = a.get_text(strip=True)
            else:
                current_time = child.get_text(strip=True)

        elif tag == "p":
            text = child.get_text(" ", strip=True)
            if text:
                body_parts.append(text)

    # Don't forget the last utterance
    _flush()

    return utterances

# Fallback strategy
def _parse_utterances_text(soup: BeautifulSoup) -> list[dict]:
    """Last-resort: dump the entire page text, split on lines, and look for the
    pattern "Speaker Name:MM:SS" followed by utterance text."""
    raw = soup.get_text("\n", strip=True)

    # Use regex to find lines that look like "Speaker Name: MM:SS"
    utterances = []
    current: dict | None = None

    # We look for lines that start with a speaker name
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue

        # Regex to match
        m = re.match(
            r"^([A-Za-zÀ-ÿ''\-\. ]{2,50}?)\s*[:\u200b]\s*(\d{1,2}:\d{2}(?::\d{2})?)$",
            line,
        )
        if m:
            if current:
                utterances.append(current)
            current = {
                "speaker": m.group(1).strip(),
                "time":    m.group(2).strip(),
                "text":    "",
            }
        elif current is not None:
            # Accumulate body text
            current["text"] = (current["text"] + " " + line).strip()

    if current:
        utterances.append(current)

    return utterances

# Main processing function
def process_year(target_year: str) -> None:
    """Scrape transcripts for every episode published in *target_year*."""
    # Fetch and filter episodes by year
    episodes_all = fetch_rss(RSS_URL)
    episodes = [e for e in episodes_all if e["year"] == target_year]

    # Catch empty years
    if not episodes:
        print(f"No episodes found for year {target_year}.")
        return

    print(f"Processing {len(episodes)} episode(s) for {target_year}…")

    folder = target_year   # relative path, matching the download script

    # Load the transcription log for this year (same log that 2_transcriber.py uses)
    log_path = os.path.join(folder, LOG_FILENAME)
    already_done: set[str] = set()
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            already_done = {line.strip() for line in f if line.strip()}

    os.makedirs(folder, exist_ok=True)

    # Open the log file for appending
    with open(log_path, "a", encoding="utf-8") as log_file:
        for ep in episodes:
            title = ep["title"]
            token = ep["token"]

            # Work out the base filename (no extension, no "_transcript" suffix)
            base = find_existing_base(folder, title) or sanitize_title(title)

            # The .mp3 filename that 2_transcriber would look for
            mp3_filename = base + ".mp3"
            transcript_base = base + "_transcript"

            txt_path = os.path.join(folder, transcript_base + ".txt")
            md_path  = os.path.join(folder, transcript_base + ".md")

            # Skip if BOTH output files already exist and are non-empty
            txt_exists = os.path.isfile(txt_path) and os.path.getsize(txt_path) > 0
            md_exists  = os.path.isfile(md_path)  and os.path.getsize(md_path)  > 0
            if txt_exists and md_exists:
                print(f"Already transcribed: {base}")
                continue

            # Also skip if recorded in the log by mp3 filename
            if mp3_filename in already_done:
                print(f"In log (skipping): {mp3_filename}")
                continue

            # Fetch and save the transcript
            print(f"Fetching transcript: '{title}' ({token})")
            transcript = fetch_transcript(token)
            time.sleep(REQUEST_DELAY)

            if transcript is None:
                print(f"⚠ No transcript available for '{title}'")
                continue

            # Save .txt
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            # Save .md
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            print(f"Saved: {txt_path}")
            print(f"Saved: {md_path}")

            # Record the mp3 filename in the log so 2_transcriber.py skips it
            log_file.write(mp3_filename + "\n")
            log_file.flush()


if __name__ == "__main__":
    year_arg = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    process_year(year_arg)
