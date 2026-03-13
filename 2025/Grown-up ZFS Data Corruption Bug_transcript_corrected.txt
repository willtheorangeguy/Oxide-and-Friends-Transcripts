[Bryan Can trill] [00:00] Alright. Well, this is and, you know, Adam, I was I like your title for this. Like, because I was like, is. No. Because I wonder, like, is it a ZFS data corruption bug old enough to vote?
[Bryan Can trill] [00:11] I mean, that is that's very, you know, that's Very wordy. Very, very wordy. Then And you got like, you know, you kinda wanna play into adulthood because it is 18 years old, but I just love it. You know, it's all grown up. Our little baby data corruption bug is all grown up, and it's gone into the world.
[Adam Levinthal] [00:29] Yeah. And definitely no question about whether we try it as an adult.
[Bryan Can trill] [00:33] No. No question whether we try this as adult. I mean, like, look, we probably would have I mean, if this had been a 16-year-old CFS data corruption, we probably would try it as an adult. Are you
[Adam Levinthal] [00:41] right? Exactly.
[Bryan Can trill] [00:41] But yes. Yeah.
[Bryan Can trill] [00:42] For sure. But now we don't even have to have that conversation. Now it's like this Precisely. This bug is going away for the rest of its life. So but that's you know what?
[Bryan Can trill] [00:51] Let's not go too far with that analogy. As we as many analogies, I wish I had stopped several elaborations ago.
[Adam Levinthal] [00:58] Sounds right.
[Bryan Can trill] [00:59] Okay. So this because this is the great thing about this bug is it includes a bonus data corruption bug that we debugged in trying to debug this one. So Alan is here. Alan, this one starts tell us how this one starts. Because I think this one starts with you noticing, that we had our, our pod just brings the chime early.
[Bryan Can trill] [01:27] We had our podcast episode on crucible, which may have been as recently as a month ago, as long ago as five years ago. I really don't know.
[Alan Hanson] [01:34] Somewhere in that range.
[Bryan Can trill] [01:35] Somewhere in that range.
[Adam Levinthal] [01:37] Well, well, I would just note on that crucible one. I think we, you know, I think Alan and James were a little bit reluctant to
[Bryan Can trill] [01:42] come on the show. And I think it
[Adam Levinthal] [01:45] was like, look. Don't worry. Nobody's going to listen to it anyway. It's fine. And it was, for a long time, our most listened to show.
[Adam Levinthal] [01:51] So sorry that we misled you on that one.
[Alan Hanson] [01:53] Even if you But,
[Adam Levinthal] [01:54] yeah, it was a minute ago.
[Alan Hanson] [01:55] Listens out. If you
[Bryan Can trill] [01:56] If you take your mom did, like, relisted to it quite a bit. She was clearly looking for something. So if we
[Alan Hanson] [02:02] take finding it.
[Bryan Can trill] [02:03] Yeah. Yes. Just not finding it. Exactly. Yeah.
[Bryan Can trill] [02:07] No. It was an it was an it was a popular one. Well, no. I think the reason to not wanna talk about it is the reason you never wanna talk about a system that's responsible for data correctness. Integrity.
[Bryan Can trill] [02:19] Data integrity because you don't want to taunt the gods. You don't want the the listener that you are worried about in that podcast is gods. The gods tuning in and being like, oh, that's a pretty fancy system you got there. It is sounds like you're pretty proud of it. That sounds like it always gets the data correct.
[Bryan Can trill] [02:36] Well, maybe it doesn't, pal. Yeah. So that that is the reason that I think we're all very superstitious about talking this stuff. And hey, we shot our mouth off and here we are. So MMM.
[Bryan Can trill] [02:48] Alan, I'm sorry. Clearly, data corruption bug is is is a direct responsibility of us convincing you to be on the podcast. So I'm really sorry for that. But so how does this thing start? Because you noticed that we've got some data corruption on crucible volumes in our dog food rack.
[Bryan Can trill] [03:05] Is that correct?
[Alan Hanson] [03:05] Yeah. Think well, I think Angela might have actually flagged the issue first, and then I went and looked and said Yeah, we are failing to decrypt a block which was very puzzling to all of us because we're like that how, what, a lot of confusion. And yeah, I mean you can sort of read the beginning of the issue, but certainly there's a lot of false there's a lot of confusion going on.
[Bryan Can trill] [03:40] What are the kind of the initial so we always encrypt by default. Yeah. So a failure to decrypt is alarming because that that can indicate well, it can indicate data corruption.
[Alan Hanson] [03:55] Yeah. And we hadn't seen like this particular panic trip in, I don't know, three and a half years or something. Since we were still developing the code. So it is very confusing and like how could we get here, what's going on. I think it took a day or so before we really analyzed the problem and figured out that we had this on this one extent, we had 32 k that was all zeros.
[Bryan Can trill] [04:30] I do like this issue, which we've linked, is itself literature. And I do love the line casting around in desperation. I find some detritus, which feels like, I mean, I the that just feels like a one line poem of for debugging data corruption. So yeah. So we what are you able to what do you find in the detritus?
[Alan Hanson] [04:55] I'd have to I need to bring up the issue too so I can reference my actual statement.
[Bryan Can trill] [05:03] I mean,
[Adam Levinthal] [05:03] it's And while you do that, Alan, I would just quick aside, and I hate to be the senator from context,
[Adam Levinthal] [05:08] but
[Bryan Can trill] [05:08] I would like to advise you that you're under oath. Is that where you're going with this?
[Adam Levinthal] [05:11] That's right. No. I was going to say, we are talking about the oxide storage service
[Bryan Can trill] [05:17] Yes.
[Adam Levinthal] [05:17] Which provides virtual disks to virtual machines. We talked about it a bunch on that episode, but just, you know, for teeny bit of context, it is having ZFSs, some underpinnings. We store data in triplicate on three different distinct servers and then provide a redundant, you know, virtual disk to these virtual machines.
[Bryan Can trill] [05:41] That's right. And we had actually so, I mean, Alan, you had said we had not seen this since we were developing Crucible. Yeah. But in fact, a very important change had been made to the surrounding system. In that, and queue episode, much more recent episode, we had, Dave had done and team had done this terrific work on update, and we were now updating a system while it was while it was more in motion.
[Bryan Can trill] [06:12] We were not parking the rack any longer to update the system which meant there was going to be more rebooting of sleds while there was effectively activity.
[Alan Hanson] [06:21] Yeah. I think this was this is definitely a key part of what the eventual issue is that we hadn't we had done a lot of testing of restarting processes and verifying things that way, but we hadn't done a lot of like power off the system, power back on testing. And I think that was sort of a new area for us.
[Bryan Can trill] [06:44] But that is probably not top of mind when you're seeing data corruption. Although maybe or maybe it was. I don't know. And the as you were casting about in desperation, finding detritus.
[Alan Hanson] [06:54] Well, I think, yeah, in the beginning, there's a lot of there's a lot of desperation. There's a lot of casting around. Part of the issue is that we're we're doing a lot of things here, and it's not clear which one is the one that makes a difference.
[Bryan Can trill] [07:08] Right.
[Alan Hanson] [07:08] So we're like, here are some things that there are lots of things that changed. One of them was the update. We pretty sure it wasn't update related directly but still not sure.
[Bryan Can trill] [07:20] Right.
[Alan Hanson] [07:20] There's always a lack of confidence in the code you wrote that's the first place you go to because it's got to be
[Bryan Can trill] [07:27] It's got to be me.
[Alan Hanson] [07:28] It's got to be me. Right. So you always you know suspect your own stuff. And then there were where some we weren't sure if the live repair was part of the prop. And I think one of our challenges here was that we didn't we didn't know that there was data corruption until we tried to actually read the block.
[Alan Hanson] [07:50] Okay. So something happened at some point in the past and now down the road we try to read the block and then there's a problem. So initially we were like well something has happened at some point, and we've we've got this corruption, but we don't know what the timeline is. We don't know the start date yet.
[Adam Levinthal] [08:12] And which is the insidious factor of data corruption? Data corruption both at rest and even in memory because the're separated at such a distance from discovery from when the thing occurred. And obviously, like, data at rest corruption is much worse. But in all cases, you're like, all I know is I found it here. There's, you know, the way where it was introduced, who knows?
[Bryan Can trill] [08:38] Yeah. Yeah. I mean, and it was introduced sometime in the distant past, and you often have at first little data other than the corruption itself. And the corruption itself can be important. And what are we able to determine about the kind of the contour of the corruption, if anything?
[Alan Hanson] [08:57] Well, we know that it's 32 k of zeros, and it's right at the start of the file. Okay. And so far, it took us a little bit to find that initially. And then once we had that sort of data point, we were able to sort of build a verify tool. Matt, you know, came up with a plan, and so we could go and then verify, and we went and verified every single downstairs that we had on dog food to look to see if this was anywhere else.
[Bryan Can trill] [09:30] Okay. And what did we find?
[Alan Hanson] [09:31] So on the the the first time we looked, we only found the one failure case.
[Bryan Can trill] [09:38] Okay. And so I mean, whether that's of is that a relief or not? That's that's kind of like, I mean, is what it is.
[Alan Hanson] [09:44] It is. Yeah. I mean, well, I if it's good because you don't want to find it. But then if is there's a problem, you want to find it and you want to find it as I don't know.
[Adam Levinthal] [09:56] Yeah. Yeah. If it was happening everywhere, in some ways, like, obviously, that's much worse.
[Bryan Can trill] [10:01] Yes. But it also means,
[Adam Levinthal] [10:02] like, it's probably going to be findable.
[Bryan Can trill] [10:03] Right. That's right.
[Adam Levinthal] [10:04] Right. It's like, if I have one ant, it's like, am I going to follow it everywhere? If I have a billion ants, like, I probably can find where they're going.
[Bryan Can trill] [10:11] Oh, that I'm going to try that next when we when the ants come back here in the wet season. I'm gonna I'm gonna I remind my going to remind Bridget, like, hey. Hey. Hey. At least we have a million ants.
[Adam Levinthal] [10:20] Glasses. Glasses. Our glass is a thousand percent full. Okay.
[Bryan Can trill] [10:25] Can you imagine how difficult this would be if we were just a single ant? I'm going to try that. Oh, that's I like that one.
[Adam Levinthal] [10:31] I'll, I'll work on that metaphor.
[Bryan Can trill] [10:32] Yeah. That that's right.
[Alan Hanson] [10:35] Yeah. So this and I unfortunately, this also gave us other escape routes that maybe we'll get to later but only having one case of this that sort of gave us the option of like, what if something else outside of crucible corrupted the file by accident. Right. So we sort of that was sort of like an escape hatch we had in the back of our mind, but I don't want to get too far ahead.
[Bryan Can trill] [11:04] Yeah. Yeah. And is that a and this yeah. That that just also is a kind of grip of terror too. Because something outside of crucible is corrupting, and it's like, I mean, worse.
[Bryan Can trill] [11:13] I mean, really.
[Alan Hanson] [11:14] Worse than me. For
[Bryan Can trill] [11:17] us. Maybe better for worse for somebody else. Exactly. Yeah.
[Alan Hanson] [11:21] Well, if is there was like some if we were running some program that was like trying to find problems and it I don't know. I don't know. If it was desperation.
[Bryan Can trill] [11:31] Desperation. Okay. So we find it in one this is the only spot basically. The the the place we found that and again, is what it is. Some solace, but we found it in the one spot.
[Alan Hanson] [11:42] And I think I found the desperation quote. And that was actually part of the challenge here was that we were doing all these rebooting of sleds, which was we beingn't able to get the logs on the sled right before the reboot. So we'd sort of lose some of our history.
[Bryan Can trill] [12:03] Right.
[Alan Hanson] [12:03] So we didn't know we knew, well, here are some of the things that happened, but there's some stuff that's in this sort of behind the moon, the dark side of the moon. We don't know what goes on there. Dave went in and added some additional stuff that would help us sort of pickup the logs after a sled had been rebooted, you know, in a surprise manner that later on would help us. Oh, interesting. Okay.
[Bryan Can trill] [12:32] One
[Matt Keeper 2] [12:32] of the other things we did at this point is started stuffing more data into spare bytes in the crucible extent files where we had, like, 48 byte slots for the encryption context, and we were using, like, 42 bytes of those for actual data. And so we just stuck other information in the remaining six bytes, so that we could then look at that after the system came back up. And so in this case, was, like, the specific flush number that had last been seen by the system.
[Bryan Can trill] [12:58] Yeah. Interesting. And I feel we've talked about this a lot on our most vexing bugs, but I think this is an extremely important technique that you're talking about, Matt. This is a half measure. This is not fixing the bug, obviously.
[Bryan Can trill] [13:11] In fact, this is presuming the existence of the bug, which is a very reasonable assumption. And then asking yourself the question, what additional information would we like to have when we next see this? And I actually think that this is not only is this very technically important because it assures that you will get more information. I actually think that this is very psychologically important because now you're rooting for the bug to occur again. And which, of course, you are always rooting for the bug, but you're also like I don't know.
[Bryan Can trill] [13:42] Maybe this is my own psychological terror that I'm gripped by, but it's like
[Alan Hanson] [13:45] Wait. It gives you something to do too. Like you're taking action. You're having some agency in the
[Bryan Can trill] [13:50] I do think it's, yeah, it's really important. Having some agency, right? Exactly. Like this is, the bug is no longer doing this to you. You are doing it to the bug, which is very important.
[Bryan Can trill] [13:58] So yeah, so we add, and so Matt, you're describing, so that was the actual so describe the flush number a little bit and why that was something that we actually wanted to have in there.
[Matt Keeper 2] [14:09] Yeah. So the way that Crucible works is its block oriented, and each block has both the like, raw data that's being stored, which is encrypted, and then some amount of encryption metadata, which is like the nonce and things that we need to verify that the encryption decrypted successfully. And those are stored in two separate places. So And we have a particular little dance that we use to make sure that there is always at least one set of valid encryption metadata for every block. So in this case, we have two what we call slots.
[Matt Keeper 2] [14:36] We write encryption metadata to one slot, then write the block data. And that way, if we lose power halfway through this, the encryption metadata from the other slot is still valid, we can decrypt the block. This is all, like in theory, there was actually a bug related to this that we found, while debugging this other issue. But those slots are just a fixed location on disk, and we weren't using all of it. And so the flush number is whenever we flush the system whenever the VM sends a flush, we increment the flush number internally, and then we write that, to each extent file.
[Matt Keeper 2] [15:09] And so having the flush number gives us some idea of ordering in the system where we can see, like, okay. This was flushed, or this block was flushed at a particular flush number, and this block was written at a particular different flush number, so we know the order in which they landed on disk.
[Bryan Can trill] [15:23] Right. Right. So we get that absolute ordering, which is which if it is, potentially hugely important, or it would be it would be a very important additional piece of data, about this problem. And then, Matt, when is it in here that we discover the bonus data corruption bug?
[Matt Keeper 2] [15:44] So the bonus data corruption bug, I think, was mostly thanks to Justin, who set up a little Jensen cluster with Crucible and, like, wrote a hacky adapter to be able to run Crucible with the Jensen style of, like, randomly killing the network and randomly restarting, systems. And he started noticing different looking data corruption and different looking failures to decrypt in his system, which was obviously another bad sign, but it was different shapes. So it was not like the first 32 k of data being zeros. It was that, like, specific blocks or specific contexts were failing to decrypt, but, like, scattered randomly through the file instead of always at the beginning.
[Bryan Can trill] [16:24] And then so okay. So then now we have got the bug that we've got because in that bug, he's we've got a decent amount of reproducibility on. And so we get we've actually got that one maybe in a position to be able to debug.
[Matt Keeper 2] [16:37] Yeah. And so that one, I was, actually out of the factory, theoretically working at the factory, but in practice, just working on data corruption because the factory was in good shape. And that ended up being us, misusing or relying on Crucible's ordering guarantees or relying on CFS's ordering guarantees in a way that was not quite correct. So there's a specific ticket. Let's see if I can find the specific link to this.
[Bryan Can trill] [17:03] And Matt, is now a good time to bring up what Matt Aaron's we have taken internally to calling the affidavit? Matt, do you know Matt Aaron's, do you know that we call this the affidavit? Is this like because this is such an expression that we use, I would say frequently, but we may not have
[Matt Ahrens] [17:21] No. I haven't heard that.
[Bryan Can trill] [17:22] Okay. Well, you're the one who signed the affidavit. I think it's maybe it's important for you to be aware of the affidavit.
[Matt Ahrens] [17:28] Uh-oh.
[Bryan Can trill] [17:29] Yeah. No. No. No. No.
[Bryan Can trill] [17:30] No. No. Uh-oh. No.
[Alan Hanson] [17:32] I mean, just because we have it printed on the wall. But we exactly.
[Adam Levinthal] [17:35] Look. You guys are going to make him start bringing a lawyer to every one of our text message conversations. Okay?
[Bryan Can trill] [17:40] No. In fact, I don't want him to bring a lawyer. That is actually you don't need to bring a lawyer in here. We don't need the lawyer's just going to slow everything down.
[Matt Ahrens] [17:46] When you say that, it makes it sound like I need a
[Bryan Can trill] [17:48] lawyer. That's fine.
[Adam Levinthal] [17:49] Oh, no. No. No.
[Matt Keeper 2] [17:50] It's not No. As it turns out, I was the one that needed the lawyer here, so
[Bryan Can trill] [17:53] you're fine.
[Matt Keeper 2] [17:55] But so the affidavit was way back in the past. Crucible stored its encryption metadata in SQLite, which was, like, very guaranteed to land on disk and very guaranteed to have strong ordering and everything, but also was flushing to disk, like, all the time, because that's what it does. And so we switched, a couple of years ago to what we called a raw file format where the encryption data and the block data were stored in the same file. And this is where I was talking about how we write one set of encryption data, then the block data. And if we lose power in a situation where things are half written, the stuff is still allowed to decrypt.
[Matt Keeper 2] [18:29] And I think Adam went to you, Matt, and asked, like, what guarantees do we have about the actual order in which CFS writes land on disk? And you wrote a very thoughtful write-up about this, explaining that things would mostly land on the disk in order with a few subtle exceptions, and we took that as gospel. And it turns out that we were violating one of those subtle exceptions, in this second bug that we found while investigating the first bug.
[Matt Ahrens] [18:54] Okay. So I was one for two in my, affidavit.
[Bryan Can trill] [18:58] No. No. No.
[Andy Friedman] [18:59] I think that the affidavit
[Adam Levinthal] [19:00] was correct.
[Bryan Can trill] [19:00] No. The affidavit is correct. Yep. The no. The the were we mis implemented very subtly the affidavit, the the the terms of the affidavit.
[Matt Keeper 2] [19:13] And so
[Matt Ahrens] [19:13] But the bug that the ZFS bug that you guys found seems like
[Bryan Can trill] [19:18] That would that one that that one
[Matt Ahrens] [19:20] That's wrong. Right? Like Yeah.
[Bryan Can trill] [19:21] Yeah. That is
[Matt Ahrens] [19:22] that is not adhering to the affidavit.
[Bryan Can trill] [19:24] That is correct. So in But as
[Adam Levinthal] [19:28] your lawyer, Matt, I would just say in Open ZFS at the time of writing the affidavit, it may have already been corrected. So, well we'll just submit that to the jury. But, but please continue, Matt.
[Matt Keeper 2] [19:40] Yeah. So the ordering issue was that ZFS writes will land on disk in order unless you have written the same region more than once. Because when ZFS goes to persist writes to the ZIL, it looks at the current state of data. So if you imagine writing offset zero to a certain value and then writing offset zero to another value later on, when it's persisting, it will get the later data when it persists the first write to the disk. This is all very hard to explain while just, like, gesturing mildly at my computer.
[Bryan Can trill] [20:09] I think we got you. We we can hear your gesturing. You're you're gesticulating is coming through in the audio. So I think it's a's and the yeah. That's what everybody's pointing out in the chat.
[Bryan Can trill] [20:20] Like, doesn't affidavits don't really have terms or sworn statements? And yes. This is a sworn statement from Matt about the way ZFS works. And so we that's that's exactly what this is.
[Matt Ahrens] [20:29] Even Yeah. I think that it's maybe confusing for folks because you would think that when you do operations, they either get logged or they don't get logged. Like, I'm doing some writes, and hopefully you're logging them. Right? Like, you do a write command, and then it gets logged.
[Matt Ahrens] [20:46] And then you do another write command, and then that gets logged later, right? But the delayed logging in DFS allows for improved performance in a lot of cases, but also can introduce these strange behaviours, like where you're saying you do a White, and then you do a later write, and then the logging pulls in the later data instead of the earlier data. It's all because of this delayed logging, the potential for delayed logging in ZFS, which I think is kind of maybe the root of all evil in at least in Aziz.
[Bryan Can trill] [21:21] Well, I mean, performance is the root of all evil. So by just by extension, this is this is very close to the root of all evil, but the need to make highly performing systems. The or actually maybe or correct systems. Because as Alan is fond of pointing out, it's like, if we can eliminate the correctness constraint, I can make this thing really, really fast. So, you know, between the two of them, there are two gnarly constraints in terms of correctness and performance.
[Bryan Can trill] [21:46] Okay. So Matt, we find a bonus bug and we
[Alan Hanson] [21:53] We're able to reproduce it.
[Bryan Can trill] [21:54] We're able to reproduce on the
[Alan Hanson] [21:56] racket. So where it's like, okay, yeah. We and Matt has a has an idea on where this is. Let's add this extra sink in at this particular step.
[Bryan Can trill] [22:11] And is as I recall, was the fix to that, like, actually fewer syncs? Am I remembering that correctly, Matt? Or
[Matt Keeper 2] [22:18] No. It was more f syncs.
[Bryan Can trill] [22:19] It was more f syncs.
[Matt Keeper 2] [22:20] We basically had to add an f sync. Yeah. Yeah. Of course. You know?
[Matt Keeper 2] [22:24] The cause of the cause of every it's either fewer or more f syncs. We'll fix everything. So we fixed this bug, but I think I remember at the time telling people, like, I do not understand how this bug could cause 32 k of zeros to show up at the beginning of the file. So, like, I was still waiting for the other shoe to drop at this point, because I was like, you know, my mental model of the bug perfectly predicts the behaviour that we've seen on the Jensen test and everything, but it really does not predict this data corruption.
[Bryan Can trill] [22:49] Which does have a very specific signature in terms of that the 32 k being zeros. And maybe actually, at some point, maybe now is the time, Matt Aron's, to because it reminds me a lot of the if I is memory serves the last 64 bytes being corrupted due to the is it the Silicon Image controller? Am I remembering that correctly, Matt? Do you remember this? No.
[Bryan Can trill] [23:19] Oh, do you I really? Am I okay? Now I'm now I'm worried that this is dementia. Because this is the is the data corruption bug that you and Bowie had early. And you're like, this the last 64 bytes of a block, I think was stale, if I remember correctly.
[Bryan Can trill] [23:44] The
[Matt Ahrens] [23:46] Yeah, I mean, we're going back like, you know, more than eighteen years.
[Bryan Can trill] [23:49] More than eighteen years. No, no, this is definitely more than eighteen years. This is way more than eighteen years. This would be This is definitely in the 20 plus category. And this is early enough in ZFS that you and Jeff are like, this is a ZFS data corruption bug.
[Bryan Can trill] [24:07] Like we've got data corruption somewhere in ZFS. This was at the time when people are starting to run it on their desktops and so on. So it's like, are running it kind of experimentally, but you two believe that this has got to be a bug in ZFS. And you're going back over and over and over and over ZFS and not actually finding anything. And then I can't God, I was really hoping you would remember because now someone observed that this was only happening on a particular DMA controller.
[Bryan Can trill] [24:44] And, but it's like a very And again, I think it's Silicon Image. And maybe is that Am I One, do I have that correct? Two, am I mispronouncing it? Because now I'm like, now I Am that that supposed to be Silicon Image? I
[Matt Ahrens] [24:58] I think it's Silicon Image.
[Bryan Can trill] [25:00] It's Silicon Image. So why am I getting it like I don't remember. Why am I making it fancier with Ahmad? What am I doing over here? Am I just but, know, I as we know, I mispronounce many things, including the word image, apparently.
[Bryan Can trill] [25:10] Although I knew I do know the word image. I'd like to say that. I just thought that they were, I don't know. The so is any of this coming is this are we still, like, still waters on this one? Is there anything that is rippling?
[Bryan Can trill] [25:22] Yeah.
[Matt Ahrens] [25:22] I don't remember this at all. That was, like, I mean, I was probably, like, you know, 23 years old or something. Yeah.
[Bryan Can trill] [25:28] No.
[Matt Ahrens] [25:28] Yes. I'm, like, twice that old now. So
[Bryan Can trill] [25:32] Adam, I know that you may
[Adam Levinthal] [25:35] not about childhood memories. Like, this is Matt's first memory.
[Matt Ahrens] [25:38] I know this is Yeah. Pretty much. Pretty much. Also, probably, you know, there were probably a lot of bugs in the first, like, year or two of ZFS, and this is one that rose to the level of, like, people outside the ZFS team noticing it or, like, hearing the story. But I've all it's probably lost in the, you know, tsunami of early No.
[Matt Ahrens] [26:01] No. It's its
[Adam Levinthal] [26:02] much easier. Now we're dipping into the realm of trauma. Like, Matt has erased this memory from his
[Bryan Can trill] [26:07] I know. I know. I I I I said at some point, I'm gonna but, Adam, do you remember this? Am I I I mean, I am now
[Adam Levinthal] [26:13] I can say with certainty you're making this up. You're making this up for attention or for content, but, no. Nobody else remembers
[Bryan Can trill] [26:21] this. I think we don't know why you're making it up exactly. The only thing we could say for certain is that this is completely fabricated. No. The so this but this DMA controller had the so it is it was always on the same DMA controller, but it was like, no, no, that's impossible because this DMA controller is like the is a very popular DMA controller.
[Bryan Can trill] [26:41] And there were literally millions of them in the field. And ultimately, it was found when the DMA satisfied certain VA constraints, it would simply not write the last 64 bytes. And it was wholly on the controller or on the HBA. This was I just remember, apparently I'm the only one that remembers this, or I implanted this in my own memory as something that was convenient, just because there was this moment, Matt, certainly I had the realization of like, there is rampant data corruption in the world that only ZFS is detecting. And it was just a real eye-opener about But again, this story is definitely having less resonance because I'm only the way to the fact that it's completely fabricated may make this slightly less impactful, unfortunately.
[Alan Hanson] [27:38] But not completely.
[Bryan Can trill] [27:39] I mean Yeah. Yeah. Thanks. Thanks for meanwhile, Adam's like, don't jump in there and save them. Let them drown.
[Bryan Can trill] [27:44] Let him drown.
[Adam Levinthal] [27:45] Well, just to just throw a small life preserver, I would say that Matt and I definitely got came to the same conclusion about data corruption being everywhere when we were at Delphi, where we were running ZFS on top of EMC arrays. And they would upgrade the EMC array, and we would detect all this data corruption. And customers would come back and say, well, none of our Windows boxes, you know, even noticed. Like, yes. Yes.
[Adam Levinthal] [28:12] Yes. You're welcome.
[Bryan Can trill] [28:13] Exactly. That's right. Right. Exactly. Well, so the the moral of that story slash fabrication was that the the the particular pattern of corruption, it does really matter.
[Bryan Can trill] [28:23] And the fact that you the fact that we had this first 32 k being zeros was a very specific fingerprint. Matt, as you say, the bonus data corruption bug did not match that fingerprint, and it just felt but the second one was still out there.
[Alan Hanson] [28:36] Well, this was actually my when I told my wife it was still in the first one. Like, she didn't know. Everything was on the table in the beginning. Yeah. It's us, is it us, you know, where is it?
[Alan Hanson] [28:45] So but finding this the first one that Matt found, I was trying really hard to convince myself this okay this could be it or there could be some other rogue agent that had done something to do this 32 k. Like, I don't know. I don't know. But maybe, maybe squinting really hard.
[Bryan Can trill] [29:09] And so we are I mean, we fixed that bug, Matt. You get the fix in for that, which is great. And we continue to test the get back to test in this release.
[Alan Hanson] [29:20] Yeah. And now that we sort of had this scanner that Matt had made for us, I was going out and scanning dog food you know like every other day I was scanning it and because it wasn't, we didn't really have it completely polished. Took a couple of hours to go dig through all the logs and make sure that oh, that's just a false positive because we're doing IO to the volume and things like that. So like we had it we had sort of I was gathering data on to look for this corruption while we were still doing updates in the background.
[Bryan Can trill] [29:55] Yeah. Okay.
[Adam Levinthal] [29:55] And dog food, it should be said, is our the instance of Oxide, the Oxide rack that we use internally, and we do our dog flooding, our eating our own dog food, that is to say, of the next release.
[Bryan Can trill] [30:08] Yes. And if you are actually in the Oxide office, dog food actually lives in the Oxide office and kinda looks the part. It's got you know, don't look at it's its, you know, it's taken some licks. That that is definitely not production anything, but it has been it's been invaluable for us to be able to. So we are continuing to do I mean, in part because we really want to test this update functionality, which has the side effect of bouncing boxes when they're doing real work.
[Alan Hanson] [30:37] MMM.
[Bryan Can trill] [30:39] Alright. So what's the what's the next? We've bonus data corruption bug fixed and all of us thinking that like, wow. Well, it didn't exactly match the fingerprint, but it was a data corruption bug. We actually knew, like, we definitely found a data corruption bug, which is very important, and we're very grateful to have that fixed.
[Bryan Can trill] [30:56] Matt, great going on that, great going by Justin to actually take this Jensen like approach to testing it. What was the next kind of the next turn here?
[Alan Hanson] [31:05] So I think we had we did the first update of dog food to the new bits, and we found a bunch of problems and there was some panic for sure, but then we had sort of looked at all the where they were and said, okay, this was the old code running as we're updating to the new code, and it was the problems we're seeing on the old code. So it is sort of made sense. Right. We could look at it and say, yeah. Okay.
[Alan Hanson] [31:38] That we do see a bunch of these zeros, it's all the old code where the bug actually happened during the update process. And once things had got to the new code, it looked okay. And so this was like I think Halloween weekend, and I was like, I'm going to continue to do my background scans, and I'm going to do three more updates to dog food. Yeah. So like we had the one the first one to the new bits bunch of problems.
[Alan Hanson] [32:06] I did another one no problems, another one no problems, another one no problems. So was like okay I think we got it because I've done a bunch of updates now which was our sort of reproducer.
[Bryan Can trill] [32:17] Right. Right.
[Alan Hanson] [32:18] And everything was looking okay. So I was like, alright, I think, you know, we'll let this one go into the wild. And then Angela did another update, and we had another instance that then panicked with this 32 k zeros problem. And I think I sent
[Matt Keeper 2] [32:45] Throughout this whole process, we've been posting, like, DEFCON pictures of various DEFCON levels in our group chat. So I think this brought us back to DEFCON zero.
[Alan Hanson] [32:54] Yeah. And I think, and it like, I was so sad at first that I only DM'd Matt directly. I didn't like to put it in the storage channel. So I was like I think found another one and you know. So we started messaging back and forth, and it was like, Yeah, this does look bad.
[Alan Hanson] [33:17] And then there was I had to go back to the product huddle that week and be like, you know, that bug that we said we fixed, and we had stopped the release for, and now we're like on a go. It's its not fixed.
[Bryan Can trill] [33:34] We're back to well, which again, I mean, the given the mismatch in fingerprint, there is some solace in this because like, there is this little piece that didn't add up from the previous bug. Like, just did not we it was really hard to talk our way into that what feels like an extremely distinctive fingerprint. This 32 k of zeros just sounds feels very unusual. Yeah. Yeah, Matt, how was it what was your feeling?
[Bryan Can trill] [34:02] What was your feeling when we, we hit this again?
[Matt Keeper 2] [34:08] Concern, I think was what I posted in all capital letters to Alan. Concern. Right. Right. But also the feeling like, yeah.
[Matt Keeper 2] [34:17] You know? Okay. Sure. I I I kind of I was waiting for this shoe to drop.
[Bryan Can trill] [34:20] Right. Right. Right. Right. Right.
[Bryan Can trill] [34:21] Right. We were kind of like waiting for it and like, okay. So we still have it. We we we fixed a bug. We know we fixed a bug.
[Bryan Can trill] [34:28] We fixed an important bug. We'd like no. We've got total solace in that. It was not the as it turns out, was not this bug, was not the bug that caused us to go search for this. So now what?
[Bryan Can trill] [34:39] How many corrupt blocks do you have, Alan, at this point?
[Alan Hanson] [34:44] I don't know if it was just one or if I had multiple. I think there may have been multiple cases this in this time when we had yeah. I think there was I think there was a couple that were bad.
[Bryan Can trill] [35:02] Bolded concern in all caps.
[Alan Hanson] [35:05] Yes. So what because we had a little more logging now, and I had been doing these regular scans. I knew that like on October 30 everything was good. And on November 1, we had a problem.
[Bryan Can trill] [35:21] Right. Right. So I
[Alan Hanson] [35:21] had like a
[Bryan Can trill] [35:22] Yeah. Time That's actually really important.
[Andy Friedman] [35:25] Yeah.
[Alan Hanson] [35:25] And so then from that and from the logging, the new logging stuff we had and sort of knowing a little better what we're looking for I was able to like walk all the way forward from the good time to the bad time and then once I had the sort of end state I then walked backwards with the like you know here's the truth table at the end, here's the truth table at the beginning and figure out where about where we got a corruption and a scary thing about this was that because this corruption was sort of hidden from crucible at one point crucible had repaired, and we have three we have a three-way mirror, and we had one of the legs of the mirror that had the corruption and two that didn't. But the IO is still going on. We don't even know that there's corruption out there. And then at some point we say, these three mirrors aren't in sync. Let me make them all the same again, and we copy the corruption from one of the mirrors to the other mirror.
[Alan Hanson] [36:25] Right. That was like, you know, the infection is spreading.
[Bryan Can trill] [36:29] Right. Right. It was yes. It was the opposite of repair.
[Alan Hanson] [36:32] The opposite of repair. Yeah. So but I was able to sort of walk backwards, figure out, okay. I'm pretty sure this problem happened during a power cycle of a specific downstairs when it was doing repair of one of the one of the extent files.
[Bryan Can trill] [36:55] Okay. So that's a that's a really important development.
[Alan Hanson] [36:58] Yeah. So like to know, okay, here is the condition that we think caused it because that enabled me to go over to our sort of
[Bryan Can trill] [37:07] So this is repeat this. This is a power cycle while we are repairing. And repairing is not I mean, it's not an abnormal mode of the system in that we expect there to be some repair whenever a sled disappears and reappears, there'll be some repair happening. Yeah. So and we expect sleds to come and go, but it's also, like, not, you know, in kind of the default operation, we kind of expect sleds to stay up.
[Bryan Can trill] [37:41] Yeah. And so we this is a slightly unusual operation to be engaged in a repair and then to have the loose power while doing the repair. I mean, we've we've got a more unusual situation, which might explain why we don't see it as much as we would otherwise. You could explain why you'd be able to do a bunch of updates and not see it.
[Alan Hanson] [38:04] Yeah. And I think it was the double thing here that really was the trigger was we need to be in this either repair or reconciliation and then lose power.
[Bryan Can trill] [38:17] Okay. So that's an important detail. What do you Then what do you do with this detail? Because right now you head over to one of our rackets and if I recall correctly, start pounding on them.
[Alan Hanson] [38:29] And start Yeah. So we do stuff to make sure that the discs are all busy so that we know that on a power loss there's going to have to be some repair that goes on. And then I just tried to keep narrowing the operations that still would show the failure. Right. And it does feel good when you're able to do it frequently because that really gives you hope that you're gonna you're going to get to the end.
[Bryan Can trill] [38:58] Absolutely. Yeah. Well, and then so then we, at some point here, you are able to reproduce this now on the Rocklike. Yeah. And you are able to reproduce it way more than once.
[Bryan Can trill] [39:12] Yeah. This is the which is great news. Yep. I mean, you were looking a little down, but I thought it was great news. Yeah.
[Bryan Can trill] [39:20] Because, this is I mean, we now be are beginning to get a corner on this thing. And I think the thing that that was both most vexing and most encouraging is all of this corruption had this same 32 k of zeros fingerprint.
[Alan Hanson] [39:36] Yep. Yep. That was really Yeah. That was the happy part of the dark part of, I guess.
[Bryan Can trill] [39:44] That was the happy part of the dark part. Also, it's just weird. It's just like 32 KS is just like not a number sloshing around in a lot of places.
[Alan Hanson] [39:50] We had some ideas, Matt had some great bad ideas about changing certain ZFS tun ables to see if maybe this 32 k was something that we could, you know, we were looking for anything that was 32.
[Bryan Can trill] [40:05] Anything that would I mean, I love that. I love it is a great bad idea because anything that I can do to like, can I turn a knob and just change this change the problem? That way at least I know that like, okay, these things are related somehow. And we can begin to because on the one hand, we've got a cordon around it and that we can reproduce it. But on the other hand, it's like it requires you know, we are, this only happens when we actually power off, hard power off a sled.
[Bryan Can trill] [40:30] So it's like, which is not exactly an easy failure mode to go debug because mean, the system is, you know,
[Alan Hanson] [40:36] it's off. And I think James I mean both James and Matt and myself we were all I mean there were lots of sorts of false trails that we had attempted that didn't lead to anything and there's lots of stuff going on where we're like we did the bug, and you can see like the knowing the result, it's entertaining to go back and read
[Bryan Can trill] [40:57] it and
[Alan Hanson] [40:58] be like, well, that's that's never going to work.
[Bryan Can trill] [41:00] Right.
[Alan Hanson] [41:00] Oh, that you should've you should've gone that way, but you didn't. You know? And you sort of see all the directions we're wandering around there in the dark.
[Bryan Can trill] [41:10] Yeah, I mean, always think that all those directions end up being important because one, they allow you to better understand the system. I mean, I'm going to go explore this aspect of the system. You come up with more confidence or in the case of Justin and kicking the snot out of one aspect of the system, you discover something else, which actually becomes germane. And or you do develop kind of the better tooling along the way.
[Alan Hanson] [41:35] Yeah, there were certainly improved tooling that we came out of this with where we can better inspect the sort of metadata and crucible and things like that we're definitely gonna keep going forward. Know?
[Bryan Can trill] [41:47] So Matt is saying in the chat that so ZFS immediate right size is 32 k. So let's change that to six lets hey. Why not? Change that to 16 k? And the but, Matt, that does not I'd a great bad idea.
[Bryan Can trill] [42:03] Truly great bad idea. I I I a terrific hypothesis, but no.
[Matt Keeper 2] [42:07] I just found this by prepping through, like, the entire ZFS subdirectory for any for that number showing up anywhere.
[Bryan Can trill] [42:14] Would you mean
[Adam Levinthal] [42:15] That is would a sign of inspiration.
[Matt Keeper 2] [42:16] Yeah. What Yeah. Yeah. It's not a good sign.
[Bryan Can trill] [42:18] Yeah. But, you know, you know, I think it's that's like it is. It's a great idea. And, and importantly, like, you can do the experiment, and you can really, and you can then really disconfirm it. Like, okay.
[Bryan Can trill] [42:30] This is actually, like, we
[Adam Levinthal] [42:32] 100%. It is both a sign of desperation and a great idea because it's one of these, like, hypotheses that is really easy to
[Bryan Can trill] [42:40] Easy to test.
[Adam Levinthal] [42:40] And explore.
[Bryan Can trill] [42:41] Yeah. Easy to test, easy to invalidate. Like, you're good. Not that one. Back to rip grab.
[Bryan Can trill] [42:47] And okay, so within what is the next kind of, the next sequence of events? Are we at that Friday yet?
[Alan Hanson] [42:54] I think this is about, we're at that Friday, yeah.
[Bryan Can trill] [42:56] Yeah, and where, because there's a moment when the because I was talking with you and Josh in particular about the prospects of this actually being a because our assumption has been this is a crucible bug. Yeah. Just in general. The Like, we had
[Alan Hanson] [43:17] Robert denies knowledge of this, but I had gone to him originally with my here's what we need to do when to make sure we're repairing extents on an unsafe shutdown, and we work together and came up with the sort of step by step copy the file, f sync the file, f sync the directory, move the file, f like this you know seven or eight f syncs around this whole repair process so that we could know where we are if interrupted at any point and recover from that if interrupted at any point. And I felt like we had come up with a good solid solution. Adam, I went back and looked, and you had actually reviewed this code and gave it your, you know, blessing. So I was like
[Andy Friedman] [44:00] No.
[Bryan Can trill] [44:02] Yes. Okay. Yeah. We actually we have a signed statement from you saying I had a Levinthal in perpetuity.
[Adam Levinthal] [44:09] MMM. Yeah. It's a deepfake.
[Bryan Can trill] [44:13] It is in this case.
[Alan Hanson] [44:14] This was pretty deep fake. So, yeah, this is we're on the Friday now, and I'm like, I don't I don't seem I really can't find anything with crucible that's wrong. And it's really kind of feels like this might be something in ZFS with the Pilot, but that how? I didn't understand how. Like, we're not you know, there are other people who use ZFS and like
[Bryan Can trill] [44:42] There are other people who use ZFS. Yeah.
[Alan Hanson] [44:44] I was like, just I don't know, but I don't know what to look for. Like, who you know what what can we do to try to figure out?
[Bryan Can trill] [44:54] Yeah. And I think that the and I definitely remember there's a little bit of like, well, can't possibly be a bug in CFS. And I think it's like, the fact that something has been used for a long time, even with a terrific track record, think does not, it may make it unlikely. And you should never, mean, it should never be one's assumption that this is, but it's like, it's like chip bugs. It's like these things do exist.
[Bryan Can trill] [45:22] And, you know, Matt Aron's, I know you're like it's like, These things definitely exist, by the way.
[Matt Ahrens] [45:30] Yeah. And I would add that, like, for sure, ZFS is used by a lot of people in a lot of different ways, but it's probably not you know, the lot those people are not pulling the power plug and then relying on, you know, strict ordering of a very careful system, carefully designed application that's using it. There's probably not a lot of other people that are doing what you're doing. There were enough that it was found in Open ZFS, ZFS on Linux, and fixed a few years earlier, but still it existed there. You know, it existed in ZFS for, like, fifteen years.
[Matt Ahrens] [46:08] So
[Bryan Can trill] [46:10] Yeah. And I think that you just can never really you have to be just very, very careful about appealing to the longevity of a thing. Mean, again, it's like it's all the reason in the world to say, this should not be our first assumption, but we should we just we need to follow where the data sends us and wherever that might be, even if it sends us much deeper into the system.
[Alan Hanson] [46:35] But I think next is the sort of breakthrough is James and what he discovered for us.
[Bryan Can trill] [46:43] Yeah. So James, why don't you describe your breakthrough? Because this was very important.
[James McMahon] [46:48] Excuse me. We had known that it was a power off during the repair process that that seemed to be the problem. So, we were talking about it, and it seemed we said it seemed like if there was an if this was true, that this was a problem, we should be able to reproduce this with a small program, not crucible, not the whole, you know, control plane and everything set up. So I had been doing I'd been working on something else, had been doing a little bit of this type of testing in a VM, in a Propolis VM, just running a program and terminating the Propolis hypervisor to simulate this power off, and saw the issue with a very small program. So simulating the part of the repair where we take something that we had copied from a remote downstairs into our current directory, and then copying that over the extent, you control like you terminate the Preplan server and then that simulated or reproduced the problem, you know, nothing else required.
[James McMahon] [47:49] So that certainly was a surprising result there. We originally thought it was something from there, we thought it was something in the Rust standard library, but we then reproduced it again with just a very simple c program. At that point, basically, everything was pointing to some sort of issue, with ZFS.
[Bryan Can trill] [48:09] Yeah. So in both so I and I want to get to that program in a second. But so, James, when you, reproduce were you surprised that you were able to reproduce this so easily in Rust in because, I mean, this is a is a huge lurch forward because now we are not powering off sleds. Now we are bouncing VMs. We are, and we've got we've got Crucible out of the picture, which is really great for from Alan.
[Bryan Can trill] [48:36] I mean, yeah.
[Alan Hanson] [48:37] Well, my wife, do you know? Don't worry. Don't worry.
[Bryan Can trill] [48:40] Don't Don't worry. I'm not sure about everyone else. I think I may be the only one at the company. We may get rid of everybody else, but they, the no. The mean, that was huge to get Crucible out of the picture.
[Bryan Can trill] [48:52] But now we've got Rust very much in the picture, and there is a period of time when, I mean, it's like, okay. This is a maybe this is a very weird Rust standard library. So it's like, you know, let's go into how this thing how complicated can it possibly be? The actual path that, like, writes to because what and James, you want to describe it just a little bit. Know you linked to it in the chat, but kind of like because there are a bunch of operations that are happening where we are we're we're renaming we're moving copying files, renaming files, and so on.
[Bryan Can trill] [49:29] Do you want to describe that just a little Because I think that that's really important here.
[James McMahon] [49:34] So the Rust program writes out a file. So this would simulate existing data in a downstairs. So it writes out an extent file. The second step would be created this dot copy file, write a bunch of random data there, completely different, simulating a file that we had pulled via the repair API from a remote downstairs. And then the third step was to use standard copy to overwrite from the copy file to the extent file.
[James McMahon] [50:06] The fourth step was a sync. And then it would keep doing this over and over, ticking up, incrementing the extents that it was working on, very much like our repair operation would do.
[Bryan Can trill] [50:19] And so this is great news because now this thing is much smaller, but it's looking like Ross is very much it has a possibility here. So Dan then realized, like, okay, I'm going to try to actually reproduce this in C. And I just kinda saw this go flying by in the chat. I don't know. For whatever reason, I'm like, I don't know.
[Bryan Can trill] [50:40] It feels like a long shot. But it which is which it shouldn't, because Dan is then able to, like, pretty quickly reproduce this at in a c program. And if he is we'd not been able to reproduce it in c, that wouldn't have necessarily That that wouldn't necessarily been a hugely valuable data point. That wouldn't have That would not have pointed the finger definitively at Rust.
[Andy Friedman] [51:02] MMM.
[Bryan Can trill] [51:03] The fact that we could reproduce it and see meant that like, okay, there's now a bunch of software that's not in the loop here. Yep. That now we are really down to to to not very much in terms of like, this is actually this is very clearly now a ZFS bug. This is the is crucible. Not only can crucible go home, all of Rust can go home.
[Bryan Can trill] [51:26] Yeah. So this is this is good news. And then, you know, this is one of the advantages of having a global team is, you know, sometimes when it's time for, some of the members of the team to go to bed, other team other members of the team are just getting up. So, Andy, at some point, you kinda come in here to, I think, your Monday morning and, and having seen all this having gone on.
[Andy Friedman] [51:54] Yes. Try. Came in Monday morning with my time zone advantage, and there was a lot of chat to catch up from over the weekend. But, you know, nice place to be in. We've got a small c program that reproduces this, and James has proven that it reproduces.
[Andy Friedman] [52:08] So I take that, and I spin up a VM and I reproduce it. And then I have to start looking at the operating system. What I did is I gave it a dedicated ZFS pool on a dedicated disk so that I keep it all separate from the operating system and sort of streamline the tracing I was doing because it ZFS gets a bit noisy if you start running Trace on it. And I started I had a bit of suspicion that this has something to do with, write caching or something to do with the ZIL which is a ZFS intent log where transactions get queued up before they're written out. And those are used and replayed if we have to recover from a power failure.
[Andy Friedman] [52:48] So what I do is I run a loop to reproduce this and every time that I reboot the machine I snapshot the disk, so I've got it in its state before it comes back up. And after I reproduce it, I can import that pool into a different VM and have a look at it and actually dump out the OIL. And then we had a think by then, that was very quick description, but by then, other people had started to wake up on the East Coast. We got on a call and I posted this data I collected. And I think it was Matt that very quickly came in and said, in this trace of records, I can see that we are doing four eight k writes, then a truncate, and then a whole slew of writes after it.
[Andy Friedman] [53:28] And wouldn't that explain why we have 32 k
[Bryan Can trill] [53:32] of zeros at the start of the file?
[Andy Friedman] [53:36] That's going to be And then
[Bryan Can trill] [53:37] That's going to be a great moment. Yeah. That just feels like blood in the water at this point. Yeah.
[Andy Friedman] [53:44] So at that point, the hypothesis is that when we replay the ZIL after booting a power cycle, a hard reboot, we're playing the transactions in the wrong order. All the transactions are in the ZIL in the wrong order. And at that point, you reach for Trace and some speculative tracing and start watching you have to use speculative tracing occasionally.
[Bryan Can trill] [54:09] Know, I don't know if you're
[Andy Friedman] [54:10] just saying That
[Bryan Can trill] [54:10] was a benefit or not, but I just you know, I let's just say that it
[Andy Friedman] [54:15] That's true.
[Bryan Can trill] [54:15] I did. I detractor once said that speculative tracing has never been used for anything, and I'd like to I every time we use speculative tracing on a bug, I I I think of that particular detractor. So anyway, sorry. Go on, Andy.
[Andy Friedman] [54:27] Oh, I'll be entirely honest. It's its maybe twice a year I use it, but when I use it, it's useful.
[Bryan Can trill] [54:31] That's right. Yeah. Exactly.
[Andy Friedman] [54:33] Yeah. I start logging the calls into the functions that put entries into the ZIL, and we run the reproducer, and I can correlate a reproduce bug happening in conjunction with the entries being written correctly. So the reproducer that's in c, which is linked to from the Lumps ticket is actually part of the Lumps ticket. It's presumably being pasted a few times in chat. It creates two random files, and then it copies one over the other, and it does that by opening the destination file with a truncate flag.
[Andy Friedman] [55:08] So the very first write to that file has been truncated, and then you get all your data going. And it writes the data in eight k chunks. And I can see that we end up with this corruption, but all the entries went into the ZIL or were queued into the ZIL log in the correct order, but they ended up on disk in the wrong order. And that was interesting. It showed up.
[Bryan Can trill] [55:30] That's a that's that's an important detail. And
[Andy Friedman] [55:36] there's a lot of detract involved here, but at the end, I realize that some of some of the right transactions are being committed to the ZIL as if they'd been synchronous rights to the file. And when you commit the ZIL to disk, you commit all synchronous rights first, and then you do all the asynchronous rights afterwards. And that explains why they're being reordered. But the question was why are these rights going in asynchronous? They weren't synchronous rights, but they were put into the ZIL as if they had been.
[Bryan Can trill] [56:09] Right.
[Andy Friedman] [56:12] And this comes back to an optimization that was put into Polaris in 2007.
[Bryan Can trill] [56:20] 2007.
[Andy Friedman] [56:22] 2007. Yeah. When Sun were doing
[Bryan Can trill] [56:24] July 2000. Exactly. I know. I want I both stared at this guy. It's July 2007 is when this thing comes in.
[Bryan Can trill] [56:31] 07/24/2007.
[Andy Friedman] [56:34] Yeah. So this is when Sun were bringing up their new Cool Thread service, the t one, the Spark t one, which were low power chips that had a lot of threads. So I think they had an up to eight cores, but each core could have six threads or something like that. That's something like 32 threads plus those early cool threads. They weren't particularly fast.
[Andy Friedman] [56:53] They'll have lots of limitations, like one FPU for every core. That's all I think.
[Adam Levinthal] [56:59] Yeah. That a very serious limitation of a turnout.
[Bryan Can trill] [57:02] Well, I mean, come on. Who actually does floating point operations?
[Adam Levinthal] [57:05] Oh, mean, the other oh, okay. Oh, Everyone all the time. Everyone all
[Bryan Can trill] [57:08] the Yeah.
[Andy Friedman] [57:11] And at the time, I was consulting for someone that was filling data centres with Sun blade six thousands and t sixty-three forty servers. And I had a lot of lots of work parallelizing things, basically, trying to but, yeah, some were doing this, and they were running my I'm reconstructing from what I can read in the Open Polaris book, which is the public information we've got, but it looks like they were running a whole load of benchmarks for different workloads. And they realized that when they did a workload that was supposed to simulate a busy mail server, which is lots of async rights and the old f sync, there was an extremely hot lock in the ZIL code that was causing f sync to be slower than it should be.
[Bryan Can trill] [57:52] In And it was this was coming out of the Niagara work. So I am actually okay. That's interesting. I thought this was actually this was coming out of the supporting CFS in the field, but that's that's actually interesting that it was coming out of an out of more of a synthetic benchmark.
[Andy Friedman] [58:07] Yeah. I mean, the ticket is all the information I've got, and it talks about some evaluation that was done, but I don't have the data. So Yeah. Interesting. They were seeing slow f syncs in a very, very hot lock.
[Andy Friedman] [58:19] And their solution appears to have been when a thread initiates an f sync, let's log the next four writes that that thread does into the ZIL as if they've been synchronous. And it takes a lot less work to insert it as if it was a synchronous write than if it was asynchronous because asynchronous write just goes into the global transaction group synchronous list as opposed to having to find the object, find the right list, chuck it on the end. That's what I think is going on.
[Bryan Can trill] [58:48] Yeah. Interesting. And
[Andy Friedman] [58:50] yeah. I don't know why it's I don't know why it's four, but if you write your data in eight k chunks, four is going to explain 32 k very nicely.
[Adam Levinthal] [58:58] I appreciate, Andy, that you're describing this in the most generous fashion. And even as you do so, you're like, that doesn't sound right. That sounds fishy.
[Bryan Can trill] [59:08] Well, also whenever there's something like this where you, like, have this 32 k, where could this possibly be coming from? And then you discover it's like, oh, it's four times a day. It's like, there's your answer, Fishbowl. But that I mean, I don't know, Adam. Do you does that I I I often think of that where they they have determined that, that Homer is mister Sparkle and why that has happened?
[Adam Levinthal] [59:33] Yes. Yeah. But even Andy's just saying it like, hey. This really complex, you know, primitive around synchronous semantics across which people reason yeah. A barrier across which people reason.
[Adam Levinthal] [59:50] What if we just, like, I don't know. Like, we're loose goose about that. What if that what is we just do that instead?
[Bryan Can trill] [59:57] Lucy goose, though, in kind of strange way. You know what I mean? Like, it feels does it is it kind of has, like, a feel of, no. No. Like, I'm making this thing synchronous.
[Bryan Can trill] [01:00:06] Like, making something synchronous is always, like, I don't know, always feels better to be synchronous. Isn't that better? Is that feels better.
[Andy Friedman] [01:00:13] Of course, if you is your system doesn't fail, it's fine because the data goes to disk in the right order and this stuff and the ZIL is never used.
[Bryan Can trill] [01:00:20] Yeah. Exactly. If it's just pieces of fail, why do have the ZIL at all? I mean, it's
[Adam Levinthal] [01:00:23] like Shut up, nerd. Right.
[Andy Friedman] [01:00:28] Yeah. And the only thing we have in the issue is something like, as was suggested in the evaluation, I'm going to hack up the suggestion. That's also a very positive result. And indeed, that they did get f sync down significantly. But, of course, unsafe at any speed from what they've done.
[Alan Hanson] [01:00:48] As a sort of callback, part of the part of the problem here was that we were f syncing. We had crossed the barrier into too many f syncs, and that put us into this window that would trigger this bug.
[Bryan Can trill] [01:01:03] Right. Right.
[Alan Hanson] [01:01:05] Like we had talked before about
[Bryan Can trill] [01:01:06] f syncs
[Andy Friedman] [01:01:07] followed very quickly by a lot of rights. Yeah.
[Bryan Can trill] [01:01:11] And Matt, Aaron, do you now do you recall anything? Mean, this is now truly I mean, obviously, eighteen years ago. And did this Yeah. Did this issue ring any bells for you? I mean, is this or or or maybe more recently because the Open I mean, this had been removed from Open ZFS, but honestly, not very long ago.
[Bryan Can trill] [01:01:34] So this is like a And
[Adam Levinthal] [01:01:35] kind of subtly, I like, in the Open ZFS repo, it was sort of a, oh, by the way, we're going to remove this thing that might cause data corruption. But, like Yeah. I was sort of SUS like, expected data corruption to be, like, the above Yeah. Like, the Yeah. Not paragraph eight subsection three.
[Andy Friedman] [01:01:58] I think it was act first I think it was first removed because they were having trouble with the TSD, the the the Fed specific data implementation on Linux or FreeBSD, whichever one they were bringing in. I think it was removed, then it was put back because it had a performance effect. And then it was finally taken out in 2023 with comments that said, you know, we need to guarantee the order of rights.
[Matt Ahrens] [01:02:21] Yeah I think the original bug I went back and looked at I mean I don't remember this particular where you know the original change that introduced this bug in Salaries back in 2007. I don't remember this particular change, but I definitely remember that era of ZFS is lower than other things, and we need to run lots of benchmarks, and we need to make lots of heuristic tweaks. And for sure, at the time, I remember being known like holding my breath for something to go wrong with messing with the inner workings of this sensitive you know the bill is very sensitive both to performance and correctness. And, you know, it's not like the easiest to understand subsystem. Yeah.
[Matt Ahrens] [01:03:21] Yes. So I love
[Adam Levinthal] [01:03:22] I love this description of this very politic description of your esteemed colleagues all volunteering to assist with performance work
[Matt Keeper 2] [01:03:31] Yes.
[Adam Levinthal] [01:03:32] Leaving you to work worry about the correctness work.
[Bryan Can trill] [01:03:34] That's right.
[Matt Ahrens] [01:03:36] Yeah. That's it's kinda what it felt like at the time.
[Bryan Can trill] [01:03:40] My job is to make the system faster. Your job is Yeah.
[Matt Ahrens] [01:03:46] And I mean, the bug report from back then, it has a lot of documentation about how they made the system faster. The lock is not as contended. The benchmark goes faster, which is great. Yes. But yeah, I mean, that you know, we were trying to get ZFS, like, to be more widely accepted.
[Matt Ahrens] [01:04:05] Performance is a big part of that. When you're competing with, like, simpler systems Yeah. Like UFS as well as Linux file systems like EXT. So it made sense to do this work, but I think it was known to be scary, and it just took a couple of decades for us to figure out why.
[Bryan Can trill] [01:04:28] And then in terms of when this work I mean, because as you say, if it was removed in Open CFS, what, like, years ago. Was Yeah. It feels like that might've been though as part of other work where someone realized like, oh, and also like, think this might have possibility for data corruption. Or do you know, or was there some, a similar experience where this was actually debugged from first principles?
[Matt Ahrens] [01:04:52] I don't know. I mean, the person who fixed that, Alexander, he didn't say in his bug report, like, if they had customers that hid this or whatever. It kind of seems like he noticed a bunch of code that wasn't needed and then kept digging around and then was like, that's weird. That's weird too. Gee, this is really not great.
[Matt Ahrens] [01:05:15] And fixed all that stuff, which is wonderful. Yeah. But, yeah, like, he probably buried the lead with, like you know, you're, like, five paragraph thin. He's like, yeah. We cannot randomly jump between sync and async, unless we want data corruption due to write reordering.
[Matt Ahrens] [01:05:31] Yeah. That that is true. But I thought that the analysis Andy did was great. And they're right up in the bug report, the most bug report that you did, Andy, was really wonderful and evocative and kinda told the whole story of where the bug came from and how it shows up. So I really appreciated that.
[Andy Friedman] [01:05:56] Well, then Andy One really nice.
[Bryan Can trill] [01:05:58] Yeah. Go ahead.
[Andy Friedman] [01:05:59] I'll say one really nice thing that the developer did for us, whoever integrated this, they made it attainable. That number four was not fixed. It was in a global variable. Yes. And I assume oh, I'm getting here.
[Andy Friedman] [01:06:11] I have to assume. I assume they want they did the number four would arrive that by playing with it a bit. Yeah.
[Matt Ahrens] [01:06:17] For sure. A 100%. He tried a bunch of values Oh my god. To see what would perform best on that benchmark on that hardware twenty years ago, and that was the best value. Nobody And ever looked at it since.
[Bryan Can trill] [01:06:27] Oh my god. I know. And what
[Adam Levinthal] [01:06:30] in defence of that so obviously a problem.
[Bryan Can trill] [01:06:32] I think
[Andy Friedman] [01:06:32] Oh, go. Yeah.
[Bryan Can trill] [01:06:33] Go on.
[Adam Levinthal] [01:06:33] That, like Wait.
[Matt Ahrens] [01:06:34] What else can you do?
[Adam Levinthal] [01:06:35] Well, there are numbers like that persist, I think, in ZFS, like 200 Metas labs per
[Matt Ahrens] [01:06:40] Oh, yeah.
[Adam Levinthal] [01:06:41] Disk where you're like That sounds like it worked really well on Jeff Bon wick's desktop machine in 2002 running at 5,400 RPM or whatever. I mean, I don't know whether that number should be higher or lower or whether 200 is, like, some universal constant. But, like, constants, you know, happen.
[Bryan Can trill] [01:06:59] I Adam, I love the love your in other entrée, like, in defence of this, because, actually, I want to go actually, I want to go after this other thing that southern this other I actually Yeah. Right.
[Adam Levinthal] [01:07:10] Let me sideswipe Jeff for no reason.
[Bryan Can trill] [01:07:12] Yes. Sideswipe Jeff. Exactly. But yeah. I mean, you're I mean, you're right.
[Bryan Can trill] [01:07:17] I mean, ultimately, when you have these things I mean, our objective is to make all these things auto-tuning. You can't do that for everything. But this was also a mean, the unable, I think, kind of indicated that this was, that there were some heuristics here. That there were this was not a and that number, yeah, again, comes from, as you say, twenty year a twenty-year-old machine, one that is that probably does not bear much doesn't bear much resemblance in many ways to the machines we run today. So but, Andy, this is in many ways the best possible thing.
[Bryan Can trill] [01:07:52] The fact that it is unable, one, means we can very quickly I mean, just to this one feels like we've got a lot more supporting evidence around than we did around the 32 k unable that Matt had found. This is feels a little like this is a little more on more solid footing than rice. But it similarly allows us to explore this by tuning this thing down to zero. And let's see what happens. I think that was the that was your next move.
[Bryan Can trill] [01:08:19] Right?
[Andy Friedman] [01:08:21] Yes. And one of our colleagues, Justin, had to set up in his lab, and I think over the overnight, he did 120 boot loops or something with it set with it set to various values and could prove that when it was set to zero, it the bug never manifested at all. So we're pretty confident by then. It that is not a complete fix because there are other ordering problems in Neville, but we weren't hitting them with the workload we're running. But they have now been fixed, but we didn't need to necessarily fix those to get the release over.
[Bryan Can trill] [01:08:50] Yeah. And we'd from a I's a strict, like, the because we were holding the release for this for obvious reasons. And, you know, I think we knew that we had a cordon around this thing, blood in the water felt like we were going to make, we're just going to, it's one these things where like, we're just going to know a lot more in a couple of hours. So let's see where And we mean, I was definitely concerned that like, yeah, we're going to know a lot more in a couple of hours. And what we're going to have is a really dicey fix where we're going to have a fix that itself is not going to be low risk.
[Bryan Can trill] [01:09:26] I mean, is always the concern you have with something like this. Yeah. Where we, yep, we actually know what it is, but now we need to go do surgery on the ZIL and then ship it to customers. Like what can go wrong? And I mean, that's obviously, we would do what we would have to do, but you just kind of hope God, don't know.
[Bryan Can trill] [01:09:44] I well, we're just going to know more. So let's go know more. And then like, oh, sweet Jesus, there's a unable we can set to zero. And just turn off this behaviour was I mean, the could not ask Yeah. For a quicker resolution from that perspective or a lower risk fix in particular.
[Bryan Can trill] [01:10:05] Felt like the risk of turning this to zero, there was some potential risk to performance, but- But not. Not a regression. A regression. Adam, I'm sure you've turned Alan's perspective on performance regressions. If you are transitioning the system from incorrect to correct, it's not a performance regression.
[Bryan Can trill] [01:10:29] It can't be because That's right.
[Adam Levinthal] [01:10:31] That's who's right.
[Bryan Can trill] [01:10:32] No. Be because the the the system, as Alan has said many times over, if correctness is not a constraint, I can make this thing really, really fast.
[Adam Levinthal] [01:10:42] Ergo. Right?
[Bryan Can trill] [01:10:43] Ergo, it is not a regression. Right.
[Adam Levinthal] [01:10:45] Yeah. I like that logic.
[Bryan Can trill] [01:10:47] I love that logic. I think whenever I mentioned this to Robert, Robert's like, well, I'm glad that you feel that way. It's like, By the way, the system is Okay, that's great. So I think that we
[Adam Levinthal] [01:11:01] Right now do Spectre and Meltdown.
[Bryan Can trill] [01:11:02] Yeah, I know. A 100%. Exactly. No, no. It's like, I'm glad you feel that way.
[Bryan Can trill] [01:11:06] Our customers may not see it the same way, obviously performance is very important as well. But it does give you, again, a release perspective, it's like, no, we're going to set this unable to zero. And now we've got a lot of confidence in actually shipping this thing out. Andy, that's not like tuning it to zero is not the fix that we actually want. We, I think, want to eliminate this entirely or that's the fix you ended up doing.
[Bryan Can trill] [01:11:35] You then have further analysis because, okay, there is a performance issue here. And so let's go understand that. And then you did some Could you describe some of the follow-up work you did to actually look at the performance of this thing? And actually going back to some of this, all right, let's go back to this original file bench profile, and let's see how this thing actually does.
[Andy Friedman] [01:11:57] Yeah. So, yeah, we obviously wanted to fix it properly. So I went through and wrote up a fix and went through all the ZIL logic and tried to fix all the things I thought were problems. And then I went and found the same commit in Open ZFS, and it was pretty much the same. They'd fixed the same things as we had.
[Andy Friedman] [01:12:13] Yeah. And a further optimization around the ZFS volume where we used to a CAT build transaction per object. And, course, there's only one object in the ZFS volume, so you can actually get a bit more speed there if you just treat everything asynchronous when it goes into the OIL. So we did I pulled that in as well.
[Bryan Can trill] [01:12:29] Oh, it should. Yeah.
[Andy Friedman] [01:12:31] And got that up for review in upstream Lumps, and then I did some yeah. I went and found File Bench and managed to get it to compile and managed to get it to disable SLR and all the other things you need to do and ran some benchmarks on old and new. I was actually on a Gimlet I went for just because there was one on the bench. Yeah. And I have to find the right word that isn't degradation, but the difference I saw.
[Bryan Can trill] [01:12:56] Yeah. Was
[Andy Friedman] [01:12:58] No more than sort of 2% change in F Sync performance. So
[Bryan Can trill] [01:13:04] F Sync performance is it. On this benchmark that is designed or this benchmark, which exhibited this problem.
[Andy Friedman] [01:13:12] So Yeah. And it's actually a benchmark that's pretty close to crucible repair. It's a lot of async rights and a lot of ever syncs scattered in the mix. I didn't spend the time to actually do one that looks more like Griselda, but we could do that. But at this point, we know it's not a massive blow to performance, and it is now correct, and it wasn't before.
[Andy Friedman] [01:13:33] So that is the route we're taking. But I think we can do some further work in the future on this lock that is highly contended. Yes. Yeah. But we'll do it properly.
[Bryan Can trill] [01:13:42] We'll do it properly. Yeah. Yeah. I think that there was some other kind of approach that we want to go take. And I think also, I mean, this is from the performance of our system.
[Bryan Can trill] [01:13:50] This is a crucible repair operation. MMM. That operation is itself asynchronous. Right? I mean, the it it's like if the performance were pathological on that, that could actually be that you could have ways that that would degrade system performance.
[Bryan Can trill] [01:14:07] But it's this is a code path that very much needs to be correct. All crucible needs to be correct, but this one especially so. And this is not, there are other paths in crucible that are the hot paths for performance.
[Alan Hanson] [01:14:24] Yeah, and this isn't one of
[Adam Levinthal] [01:14:25] them.
[Bryan Can trill] [01:14:25] This is not one of them. Is that fair to say,
[Alan Hanson] [01:14:28] Yeah, yep.
[Bryan Can trill] [01:14:33] Mean, this ended up being, We went from Friday feeling Oh, I don't know. I mean, I guess you felt kind of despairing. I felt like excited that we had this thing actually reproducible. So you know, we're going to get this. It may take us weeks, but we will get this thing this point.
[Bryan Can trill] [01:14:50] Yep. But I mean, as we've had, as we've seen so many times before, and as we saw, ironically on the bug that was happening kind of concurrently with the first round of this that we had Dave and Co on talking about, there was a baton being passed here as people are trying I mean, obviously, Justin and Matt, but then also James, you being able to reproduce it simply, Dan being able to produce it even more simply and see kind of setting it up for Andy to really be able to, again, put a corner around it and really cinch it tight. Was a lot of fun to see.
[Alan Hanson] [01:15:32] It's a lot of fun now looking back. Yeah.
[Bryan Can trill] [01:15:34] It's yeah. I mean, it is I mean, on the one hand, it's like, God, it is great content. It is such great content. On the other, it's like, maybe you don't need this much. We don't need to do that.
[Bryan Can trill] [01:15:46] We don't need Hey, gods. We don't need any I don't know.
[Alan Hanson] [01:15:50] Some content, but maybe Yeah.
[Bryan Can trill] [01:15:51] Yeah. Maybe we don't. We're okay on this, actually. We've kind of like I mean, people are like, Jesus Christ, another data corruption episode. How many of these things are you going to have?
[Bryan Can trill] [01:15:59] I mean, you know, let's get But I really was It was terrific. And I think there are, again, are a bunch of, I feel, lessons here. One of them, I mean, Matt, just in terms of your half measure that I think was important. Being able to When you see a pathology like this, instead of closing your eyes and pretending that it didn't happen, which is Which first, you can want to do. That's okay to want that.
[Bryan Can trill] [01:16:29] Just that the actually need to go do is really try to actually go hit the system harder where you think it might be more vulnerable.
[Alan Hanson] [01:16:41] And if you don't like, in the beginning, we didn't know what it was that would be hitting it harder. So what do we need to do to get that information? Like, okay. We can add more logging here. We can put some debug data in here.
[Alan Hanson] [01:16:55] Like, if is you don't know what it is to do to reproduce it, then go do what you need to do to get the information that will help you, you know.
[Bryan Can trill] [01:17:05] Right. Exactly. To actually go to and the information, the tooling that you need to actually get this stuff nailed. But Matt Aron's, you should know that the affidavit holds. And it continues to be very valuable to that.
[Bryan Can trill] [01:17:27] And I also very appreciative of having, even though we've kind of got different CFS implementations out there, very helpful to be able to compare notes across those implementations for sure.
[Matt Ahrens] [01:17:44] Yeah. Sure thing. I found that email that I think you're referring to, from October 2023, which was just a few days before the fix was integrated into, Open ZFS. So I don't quite have that excuse for not, you know, code reviewing and understanding all the ZIL before I sent Adam the affidavit, but glad it was helpful.
[Bryan Can trill] [01:18:06] Yeah. It is remains helpful. I if it was extremely helpful because it was again, allowed us to make this very important transition in the system that Matt described earlier. So, it is has been very helpful. And again, terrific work all around.
[Alan Hanson] [01:18:24] Truly a team effort. Like everybody from all directions throwing in little pieces that move sort of the whole process along.
[Bryan Can trill] [01:18:35] It's a very, very important aspect of this. Data corruption needs to be shared suffering. It is really is is is very important. And I also when debugging problems like this, I think they're very analyzable in the sense that people can try things out. I mean, when like, for example, when Dan was trying out writing this and see, it's like, that's fine.
[Bryan Can trill] [01:18:53] Like, yeah, go down that route. If it yields something, that's great. If it doesn't yield something, that's fine because lots of other routes didn't yield anything. And then, Oh, wow, it yields something. Great.
[Bryan Can trill] [01:19:01] Okay. That kind of lurches us in that direction. Yep. Well, awesome. Thank you everybody.
[Bryan Can trill] [01:19:08] Andy, thanks for your terrific analysis in the Lumps bug. We'll link in the show notes, but 17734 is the Lumps bug that that goes into the actual details and a really terrific work on all of this. And thank you everyone. Matt Aron's, thank you again the affidavit and for all of your great help from afar. And now I really need to go figure out if I'm hallucinating this DMA issue from twenty plus years ago.
[Bryan Can trill] [01:19:42] I is Silicon image. Silicon image.
[Matt Ahrens] [01:19:45] It sounds very truthy.
[Bryan Can trill] [01:19:47] It's it does sound truthy. It sounds truthy, which is what makes it so plausible that I have told myself some elaborate lie. I well, anyway, I'm not I'll go do my homework on that.
[Adam Levinthal] [01:19:56] Someone said you mentioned it in a talk like years and years ago.
[Bryan Can trill] [01:19:59] Oh, I for sure have mentioned it in talks like that. Sorry. If that's the standard for like, I definitely know I'm
[Adam Levinthal] [01:20:04] You've not accepted yourself. Oh, yeah.
[Bryan Can trill] [01:20:06] I mean, for sure on that one. This is what has me concerned. It's an implanted memory because it's extreme I mean, it's an it's an it's a great yard, you know. It's like Yeah. Maybe the thing is like, I even remember whose office I was in when this thing got I mean, it's like, if this thing's implanted, it's elaborate, and it's really I I I mean
[Alan Hanson] [01:20:25] Do you really want to know? Like, maybe you don't.
[Bryan Can trill] [01:20:27] You know, maybe I don't. Like, what you know, who's to say
[Adam Levinthal] [01:20:30] Just let it be.
[Bryan Can trill] [01:20:31] Yeah. Let it be. It's it is could have happened, and that's the point, really. Yeah. No.
[Bryan Can trill] [01:20:36] I definitely have told this one plenty. This true or not this truthy story, I've told plenty. It's a parable.
[Adam Levinthal] [01:20:44] It's a parable. It's got a's got a whole lesson to it.
[Bryan Can trill] [01:20:47] It's a parable. Awesome. Well, thank you very much everyone. And, yeah, thanks. I know what I will be giving thanks for at my Thanksgiving table.
[Bryan Can trill] [01:20:57] Correct data. Yep. There we go. Awesome. Thanks everyone.
[Bryan Can trill] [01:21:02] See you next time.