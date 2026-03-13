[Bryan Cantrill] [00:00] Hello, Adam.
[Adam Leventhal] [00:01] Brian.
[Bryan Cantrill] [00:02] How are you?
[Adam Leventhal] [00:03] I'm doing well. How how are you?
[Bryan Cantrill] [00:05] Doing well. I sound as good as I'm gonna get. I'm just I I just am in a as you know, I'm not in the litter box at the moment. I'm in a
[Adam Leventhal] [00:12] That's right.
[Bryan Cantrill] [00:13] There's a lot of tile in here. It's very bouncy.
[Adam Leventhal] [00:16] Undisclosed, echoey location.
[Bryan Cantrill] [00:19] Undisclosed, echoey location. So, yeah, I just I, yeah. I'm I'm with my mom while she's recovering from a surgery. And my sister was just out here, and she's like, we gotta get rid of all these carpets. These are these carpets are are trouble for her.
[Bryan Cantrill] [00:35] And I'm like, I'm kind of resisting her, like, rolling up all these carpets. And I'm I'm I don't wanna con I don't wanna tell her that the reason you can't roll these carpets is because of the podcast. Look. Hey.
[Adam Leventhal] [00:49] Look. The risk the risk of mom falling, I get it. That's real. But we talked about reverb for a second. Can we
[Bryan Cantrill] [00:55] can we just talk do you know how much abuse we take over audio on this thing? Like, I'm just you know? And people think we don't try. We do try. I try.
[Adam Leventhal] [01:03] Oh, yeah. No. We try for sure. We're just bad at it. Yeah.
[Bryan Cantrill] [01:06] We're just bad at it. We're just bad at it.
[Adam Leventhal] [01:08] It's much worse than not trying.
[Bryan Cantrill] [01:11] And, you know, in my sister's way, she's like, you cannot give me one reason for leaving these carpets here. And I'm like,
[Bryan Cantrill] [01:18] you know what? I can't.
[Bryan Cantrill] [01:20] That's correct. Let's just roll it up. I'm just gonna go. You know what? It is gonna be way faster to apologize for this on Monday.
[Bryan Cantrill] [01:27] So, anyway, there you go. It's I'm I'm reverby, and I agree with my apologies. Hey. Good memory on this Austie episode that we did. How did you get that out?
[Adam Leventhal] [01:38] Oh, so I I was thinking about the Usenix ADC, which is, you know, spoiler alert, the subject of
[Bryan Cantrill] [01:47] this conversation. Spoiler alert. Oh my god. Jumping into the intro so quickly. Okay.
[Bryan Cantrill] [01:52] Yeah. Wow.
[Adam Leventhal] [01:53] Yeah. Sorry. Sorry for folks who wanted to listen for half an hour and then figure out what the what the fuck it was we were talking about. So I I was looking at the history of the Usenix ATC, and I can't remember when Usenix ATC and Ausd merged, but fairly like, within the last ten years or something like that. So sorry.
[Bryan Cantrill] [02:12] No. No. They didn't merge.
[Adam Leventhal] [02:15] Then Witch Media was wrong.
[Bryan Cantrill] [02:16] Stanford. I it's a really?
[Adam Leventhal] [02:23] I mean, really, that's my recollection based on looking at the at Wikipedia recently. Yeah. Yeah. It says in 2021 onward Oh, okay. No.
[Adam Leventhal] [02:32] Not first.
[Bryan Cantrill] [02:33] Collision. Yeah. Yeah. Collocated.
[Adam Leventhal] [02:34] Got it. Collocated. Sorry.
[Bryan Cantrill] [02:36] Yeah. Collocated. Sorry. Even what? It's like sleeping on Ozzy's couch, which is, like, even kinda sadder.
[Adam Leventhal] [02:44] Yeah. I mean, you're right. Not not merged in the most literal sense, but I think, like, not inaccurate. Right? Like, co located.
[Bryan Cantrill] [02:51] He's sleeping on Ozzy's couch. Ozzy's like, look. Using it like ATC, you can't keep sleeping here. You gotta go. Right.
[Adam Leventhal] [02:58] I hear you've been telling people we've merged, but you're just sleeping
[Bryan Cantrill] [03:01] on my couch. Right.
[Bryan Cantrill] [03:04] Yeah.
[Adam Leventhal] [03:04] Yeah. Part of it. Yeah. So then, OSDI reminded me of the put the OS back in OSDI episode from a million years ago.
[Bryan Cantrill] [03:12] From the It is truly a million years ago. It is truly and I I actually god. I mean, that is from my early, early days. And, like, people think we complain about the audio now. We had accidentally lost the audio from the previous episode, which we spent, like, twenty minutes on that episode talking about, like, you know, so it was but it was it was, good to go refresh a little bit.
[Bryan Cantrill] [03:35] And I'm really I'm really impressed you pulled it out because I had honestly forgotten it.
[Adam Leventhal] [03:40] No. And I think it was I did not relisten to it, but it was about like, I think Muthi Roscoe had given a presentation, that was very, like, on the nose oxide, especially at the time, as I recall. Yeah.
[Bryan Cantrill] [03:53] Yeah. And and and kind of decrying the lack of real OS innovation at Ostie and hitting on some similar themes for sure. Yeah. And the and I just I, you know, I did not realize that that ATC was sleeping on Ostie's couch, which actually makes a little more sense now. It was it was kind of like it had been transitioned to kinda hospice care in hindsight.
[Bryan Cantrill] [04:11] And I the so and did you I don't know if you saw this announcement last week when it I mean, what over a beer. You
[Adam Leventhal] [04:20] know how offline I am. So I was particularly offline over the weekend and last week. So, yeah. I missed that until until you hit me up this morning. No.
[Adam Leventhal] [04:29] I had not seen that announcement, so I was catching up in a hurry.
[Bryan Cantrill] [04:32] And we have been so I I think I have been in some to three ATCs, and you've been to at least two.
[Adam Leventhal] [04:38] That's right. So I I we we went with when the when the DTrace paper that you wrote and then put my name and Mike's name on, I think, is not inaccurate, but I'll take it. When when we when we went, you know, back then and when we met Dennis Ritchie, by the way. I'm not sure we're gonna get into that. But
[Bryan Cantrill] [04:57] We we are for sure gonna get into that.
[Adam Leventhal] [04:58] We have to get into that. Okay. Okay.
[Bryan Cantrill] [05:00] Good. So so this is like run, Brian, run and us eating horse and gent, which I am convinced we have retold 15 times on Oxnard and Friends. How how many times have we retold the Dennis Ritchie story?
[Adam Leventhal] [05:11] I think zero times.
[Bryan Cantrill] [05:13] Oh my goodness.
[Adam Leventhal] [05:15] Because it makes me a little uncomfortable to tell, at least the way I tell it. So I think I would remember that I told it to everybody.
[Bryan Cantrill] [05:22] Okay. Yeah. The way I tell it, I think, makes you even more uncomfortable. Doesn't make me feel uncomfortable, but let me be odd.
[Adam Leventhal] [05:28] Yeah. That sounds right. So then and then
[Bryan Cantrill] [05:31] myself do not let Brian tell the Dennis Ritchie story.
[Adam Leventhal] [05:34] Right. How can I move on as quickly as possible? Oh, here's a shiny object. And the la the the next time was when we were receiving the Stug Award, right, for for DTrace. This is and and, and and you speaking of your mom, she was there to to watch you receive the award.
[Bryan Cantrill] [05:51] In fact, she reminded me of that when we were talking about the story. And I I completely forgot about that. And that was in Boston, I think.
[Adam Leventhal] [05:58] Yes. Right?
[Bryan Cantrill] [05:59] Yes. Yeah. And then I went back for this the ATC, which we we we hit on briefly in the the episode that we recorded several years ago, and then I did reference in the blog post, but that they made this huge mistake of inviting me back to give the ATC keynote in 2016 very clearly not having done any research on me whatsoever. I would love to know, like, the backstory on how they'll they clearly clearly, I was their age choice or something. And they
[Adam Leventhal] [06:36] Or or somebody, like, lobbed in this apple of Discord with your name on it.
[Bryan Cantrill] [06:40] That's another possibility that it was an act of spite by the enemies of the organizers. Like, look. I can't make the conference, but this is the guy you should have. This is the guy that you jerks should have given your keynote. No.
[Bryan Cantrill] [06:51] That's also plausible. Yes. It it was, it was hot. It was definitely hot. And I Was this the one my chest.
[Adam Leventhal] [07:01] This the one they they put, like, a warning over, or was that a different topic?
[Bryan Cantrill] [07:06] Look. I mean, you're gonna have to be more specific. I know they had given you know, they they had put a warning over my Lisa talk, another dead conference. I'll could I I I will thank you not to conflate my hot talks at dead conferences, sir. No.
[Bryan Cantrill] [07:21] This is That's
[Adam Leventhal] [07:21] whole series. That's a whole
[Bryan Cantrill] [07:23] series of hot talks at dead conferences. The no. That was in, Lisa two thousand eleven where I gave some unvarnished opinions on Oracle, which it it's it like, it is almost like there are it is if there's a bot responder on Hacker News. Whenever Oracle comes up, someone feels an obligation to kind of drop the reference to the stock. And at thirty three minutes in particular, I, you know, I, well, I'm just candid as far as I'm concerned.
[Bryan Cantrill] [07:51] But they, yeah, they put a warning on the talk, and then they put a warning above my head the entire time I'm speaking. Here, they didn't actually have a video. They had audio only. Right. Which itself is like, this is not a good sign.
[Bryan Cantrill] [08:06] This is like a cat that's no longer cleaning itself from a conference perspective. You know what I mean? Like, this is like this is this is not good. Is not good. Like, you're like, you it also but I think it also reveals that, like, this the the part of the the endemic problem in the annual technical conference is that it it was really it was no longer a conference in any way.
[Bryan Cantrill] [08:30] And I felt like when we were there in 02/2004 so we were there to and and we we we described AAD bug before and get in 02/2003. But it was there that we're like, we really in terms of, like, we we felt strongly that we needed to publish DTrace, and we wanted to publish it academically. We wanted to do it in Usenix. And I have ATC like, Usenix ATC felt like exactly the right vector because that's clearly the conference aimed at practitioners. And, you know, I was kind of floored about how low the acceptance rate was.
[Bryan Cantrill] [09:02] The acceptance rate, you know, when we got when when our year 02/2004 was, like, under 13%, which is super low. Yeah. And this just means, like, you're just throwing out good stuff at that level. You know? I I unless you are just, like, attracting total turkeys when you are at that level for a conference, like, there's gonna be good stuff that you're rejecting.
[Bryan Cantrill] [09:23] And I don't I mean, do you I so what I what do you remember about about ATC two thousand four? This is a long time ago now.
[Adam Leventhal] [09:29] I remember, being I'm I'm trying to remember that it was, like, kind of Nutella Networks mania is what I remember. It was sort of like
[Bryan Cantrill] [09:39] Nutella, like the chocolatey spread?
[Adam Leventhal] [09:42] Wasn't that what they were called? Like, these, like, massively distributed networks? Help me out, Chad. Come on. I'm not making that up.
[Adam Leventhal] [09:49] Yeah. Thought I thought, like, it was it was the network named after the chocolatey spread. Chocolate hazelnut spread network.
[Bryan Cantrill] [09:55] Okay. Okay. Okay. Yeah. Okay.
[Bryan Cantrill] [09:56] And then what else happened?
[Adam Leventhal] [09:58] In this in this dream that I was in?
[Bryan Cantrill] [10:00] Maybe next. Okay.
[Adam Leventhal] [10:01] No. I remember a bunch of talks on on these subjects that that felt kind of very abstract, but, like, the kind of thing that is, you know, what it what it felt like at the time achievable with the resources of a university, which sort of makes sense, as opposed to sort of, you know, some of the stuff that we had been doing at Sun around massive multiprocessing, things that were novel in that 02/2004 era, but were pretty inaccessible or or tough tough to access or expensive for university students. So it it didn't feel I don't think we walked away or I didn't walk away feeling like there was stuff that we learned that we could apply when we got back to Menlo Park.
[Bryan Cantrill] [10:43] For sure. And I think I was also just I know I was surprised be by the fact that we were the only folks presenting a paper that were writing software for a living. That everyone else was basically in a lab or a grad student. Like, I I just think I I thought it was still, you know, we that those proceedings from the the Usenix proceedings from the nineties where they they I I love everyone in the chat trying desperately to help you out on Nutella, by the way, Adam. I think it's the Nutella stuff maybe.
[Bryan Cantrill] [11:22] The but, you know, I just remember those weird because, like, had done this lab allocator paper, right, in that the the summer use exciting '94. And just like you look at those mid nineties Usenix proceedings, and we're like, you know, NFS three is a paper. You know? It's like, wow. Okay.
[Bryan Cantrill] [11:40] And it just felt like, wow. This is, big industrial stuff. People that are are at you know, at the time, it was at Sun or SGI or HP or what you know, at, like, doing real systems presenting their work. And I just assumed that ours would be one of many like that. And it's like, oh, no.
[Bryan Cantrill] [11:59] It's like just us. And then after every talk, they'd be like, and, hey, just as a reminder, this person is looking for a faculty position.
[Adam Leventhal] [12:08] Right.
[Bryan Cantrill] [12:09] And I'm like, this is really just not what I was expecting. And this is in an era this is where we sound like I mean, down at the Gen X home in Dickity Two of, like, this is, that talk is not recorded, the one that we gave Really? On Wow. Price. Yeah.
[Bryan Cantrill] [12:25] Right? I mean, it's not really literally, it's not recorded at all.
[Adam Leventhal] [12:31] That's kinda crazy.
[Bryan Cantrill] [12:32] Recall that we had twenty minutes to present that entire paper, which was all of DTrace?
[Adam Leventhal] [12:38] I do. And I rim I mean, like, you you generously say that we presented. You presented it, and we're talking at at full speed. Right? Like, throttle
[Bryan Cantrill] [12:48] I Full throttle. And in many of my talks, if you listen closely, because I insist on being able to see a clock, especially if I if we've got a if I got a time bounce, unlike this podcast, which, of course, goes just destroys all of your domestic life with its total lack of adherence to a time bounce. But the exactly. The the clock in front of me. But I you can hear me, like, see the clock in some talks, and all of a sudden, you're like, okay.
[Bryan Cantrill] [13:20] What just happened? Like, we just launched. It's like, oh my god. You guys are only, like, a quarter of the way through my tech and have exhausted half the time.
[Adam Leventhal] [13:28] Right. The right. That feeling when you're, like, cruising along at 25 miles an hour and realize that, like, you're definitely not gonna make it on time and gun it to 75.
[Bryan Cantrill] [13:36] That's right. That's right. In contrast, that talk, not recorded, was like, we don't have a chance unless, like, we come out of the we peel out of the garage at, like, one twenty five. So we the that I I don't think I ever put more content into twenty minutes than that talk. And I'm like and it's like I'm sure it would advise.
[Bryan Cantrill] [14:00] I'll be like, I need to present this entire, like, body of work that the three of us had worked on for three years in twenty minutes. And, I mean, it was and I'm like and I need everyone's attention to do it. And I definitely got everyone's attention because, you know, like, people I will induce a fight or flight reaction where people are afraid to look away because they are, like they they got this animal reaction is engaged. And that was definitely that's what I recall from that talk. And, our friend Peter Galvin, who we've known for years, and Peter wrote co authored one of the the great OS textbooks.
[Bryan Cantrill] [14:35] Peter looked out over everybody, and because there's kinda, like, silence after, like, I hit time, basically. And Peter's like, everyone looks like they just got off of a roller coaster. It just looked just looked like they are so yeah. And that not not recorded. And then but I I just remember us doing a and then, of course, the first question.
[Bryan Cantrill] [14:59] You remember the first question? It must
[Adam Leventhal] [15:01] have been something something like rage inducing like Linux or what's the license? Probably Linux.
[Bryan Cantrill] [15:07] Linux. Keith, is before open source. So it's, of course, there's no license. Like, when do when do gonna port this to Linux?
[Adam Leventhal] [15:12] You're like
[Bryan Cantrill] [15:13] Yeah. Yeah.
[Adam Leventhal] [15:13] Okay. Was it so I thought we open sourced DTrace in 02/2003. Is that not true?
[Bryan Cantrill] [15:18] No. No. No. We no. We shipped it first to customers 02/2003.
[Adam Leventhal] [15:21] Oh, pardon me.
[Bryan Cantrill] [15:22] January 2005. Excuse me. It's kind of in this, like well, this is kind of interesting. Right? That's a really good point because this is the world's only introduction to the thing we've done.
[Bryan Cantrill] [15:33] We live it I mean, we're kind of in this era of proprietary systems, and, like, this is kind of it. Like, there's not a you know, you can go get the manual and so on, but this is not it's it's a proprietary era. We haven't open sourced it. There's not a GitHub repo. Like, this is our way of kind of projecting all of this, of of letting people know what we've done.
[Bryan Cantrill] [15:55] And it's like a really different era. It's just a long time ago now, you know, in the do you remember, Bridget was there? Oh, really? Very, very pregnant with Tobin by now twenty twenty year old. Wow.
[Bryan Cantrill] [16:09] Yeah.
[Adam Leventhal] [16:11] Do you remember what was the I remember another thing I remember is you really thinking that we're in the running for best paper, which I don't think we are. Do you remember who like, what paper won best paper?
[Bryan Cantrill] [16:24] You know, I I don't even remember having that hope, sadly.
[Adam Leventhal] [16:28] Oh, I remember when they were announcing it,
[Bryan Cantrill] [16:30] they were,
[Adam Leventhal] [16:31] like, vibrating.
[Bryan Cantrill] [16:31] And and Oh, no.
[Adam Leventhal] [16:33] And I, I thought, were being very supportive. But I would say, in your defense now, years later, I googled it because I was trying to figure out who it was. And the AI overview says that the paper and I I don't believe this, by the way, you'll see why. It says it was given to energy efficient prefetching and caching. Okay.
[Adam Leventhal] [16:52] Plausible. I don't believe it. Because it says
[Bryan Cantrill] [16:55] Something's a dumb idea.
[Adam Leventhal] [16:56] It says this paper was presented by Brian Cantrell, Mike Spiro, and Adam Leventhal and focused on DTrace.
[Bryan Cantrill] [17:02] I like it. I think the AI is not totally wrong. I think the AI is half right.
[Adam Leventhal] [17:07] Sure. We'll take it. Take take that win, I guess.
[Bryan Cantrill] [17:09] We'll take the win.
[Adam Leventhal] [17:10] Weird. I don't remember that being the title, but, you know, fair enough.
[Bryan Cantrill] [17:14] No. I I'm pretty sure the best paper went to inhalable insulin at that conference.
[Adam Leventhal] [17:19] That is a that's another deep cut.
[Bryan Cantrill] [17:21] That is
[Adam Leventhal] [17:22] that was the Wall Street so Wall Street this is the proudest moment in my career or very proud moment in my career because I could finally explain to my parents something that I had done. Or, actually, I really, I could just give them something to coherently brag about, which is when we won the Wall Street Journal Award for Technology, we we beat out inhalable insulin. And so it made it very easy to explain something that we were better than. Although it turned out inhalable insulin was kind of, like, not good. Is that right?
[Adam Leventhal] [17:51] Is that fair
[Adam Leventhal] [17:51] to say?
[Adam Leventhal] [17:52] Didn't make
[Bryan Cantrill] [17:53] it. Well, I would say it was more that people had drawn the inference that we felt that inhalable insulin was not an important problem and that actually misbehaving systems were actually much more important than actually helping people who are diabetics. So the I just remember people being like, where did you come to get like, why do you think you're better than inhalable insulin? I'm like, I don't. They dates.
[Bryan Cantrill] [18:14] They do.
[Adam Leventhal] [18:15] The Wall Street Journal does.
[Bryan Cantrill] [18:17] So The Wall Street Journal does. So I don't know. By the way, went for inhalable insulin. So, you know, there's lots of inhalable insulin now.
[Adam Leventhal] [18:23] Yes.
[Bryan Cantrill] [18:25] But, no, I had forgotten that. I had forgotten that I that I got my I got my hopes foolishly up. I should have got my hopes up because I was that it's it was an academic conference. But yeah. Exactly.
[Bryan Cantrill] [18:34] And they're just and how is how many attendees do you think were at that conference that year?
[Adam Leventhal] [18:42] I mean, it felt busy. I mean I
[Bryan Cantrill] [18:45] think it felt busy. Yeah. I agree. I think I mean, I think that they were, like, a 50 or 200 in the room where we presented, which was right? I mean, I
[Adam Leventhal] [18:53] think it
[Bryan Cantrill] [18:53] doesn't feel like a huge exaggeration. I feel like there were, like, on the order of four to 500 people at
[Adam Leventhal] [18:59] the conference. I was gonna guess, like, 500. So yeah. Yeah.
[Bryan Cantrill] [19:02] And, apparently, it hit a high close to 2,000 in February. It hit, like, 1,700 or something like that in February. And but it and there were definitely but so I think that that year that we were there was a very much a shoulder year where it was and and maybe that was the first year where it was transitioning to really being an academic conference versus a practitioner conference. And the, and now that said, there were practitioners there. Is now the time that I get to make you feel uncomfortable by telling the search historian?
[Adam Leventhal] [19:35] Do I why
[Bryan Cantrill] [19:36] you tell why don't you tell your version that has the least amount of discomfort?
[Adam Leventhal] [19:39] Well, just me telling it has discomfort, but I will say. So we we we we saw Dennis Ritchie was there. Think we had we had kinda seen him and then kinda bumped into him in, like I think literally as we were kind of passing in a hallway or leaving one other talk. And we're really excited to talk to Dennis Ritchie because, obviously, we had drawn tremendous inspiration from his work. You know, there's, like, c and awk and, like, there's all kinds of stuff in the design of DTrace that we wanted to show him and talk about it and and geek out about one of our, I think, collective heroes.
[Adam Leventhal] [20:13] So we maybe came on too strong
[Bryan Cantrill] [20:17] as Did he doubt it?
[Adam Leventhal] [20:19] He he he was not he was not cornered per se, but, like, certainly quickly got the look of, like, a a caged animal as we kind of all kind of confronted him laptop open, kind of telling him how excited we were to show him this thing. He explained that he needed to go catch a train right away. And then to like, I think all of us agreed, sprinted into the women's bathroom.
[Bryan Cantrill] [20:47] Yes. He definitely ran away. We cornered him with a demo and, like, look, accosted him with a demo. I don't feel that that's like
[Adam Leventhal] [20:54] Yes.
[Bryan Cantrill] [20:55] We were not a not a crime, but there is a yeah. In fact, we were excited. It's not a crime. We were excited.
[Adam Leventhal] [21:02] Yeah.
[Bryan Cantrill] [21:02] And But he was less excited. Was a lot less He was a lot less excited. And he wanted to be polite and said that he had to run for a train, but then in his fight or flight motion, did not go to the exit but dashed into the the bathroom. You asserted the wrong bathroom, but he went into a bathroom of that, I am certain.
[Adam Leventhal] [21:27] We can definitely agree on that.
[Bryan Cantrill] [21:30] And we're like, what do we do now? Because he's definitely, like like, there's no exit in there.
[Adam Leventhal] [21:36] So what do we do, dear listener? We followed him into the bathroom. No.
[Bryan Cantrill] [21:40] No. We did not follow him into the bathroom. We did it, but it was a moment of deliberation. Like, do we stake him out? We I mean, we I definitely remember us joking that we were gonna go into the bathroom and, like, look under the stalls, and he was gonna be standing on one of the toilets, like, you know, just terrified of, like, please don't make the demo come back.
[Bryan Cantrill] [21:58] Please. Please make it leave.
[Adam Leventhal] [22:00] I I will say there are not many times in my career when I've been incapacitated by GiggleFits, but that was one of those times.
[Bryan Cantrill] [22:09] The idea of Unix pioneer Dennis Ritchie standing on a toilet because he was afraid that we would accost him with a demo.
[Adam Leventhal] [22:16] And and and us staking him out, us kind of looking into the stalls, us doing a bathroom demo of D Trace, all of those things, I think were fairly incapacitating for me.
[Bryan Cantrill] [22:28] Yes. I do think as I recall, we had some kind of vivid fan fiction for ourselves of, like, sitting in the next stall, like, loudly doing a demo while yeah. We we had a whole bunch of we we we had a whole bunch of ideas. Poor poor dentistry. And dentistry, I think, was actually just candidly was beginning to decline at that point.
[Bryan Cantrill] [22:46] I think he the the but we did not stake him out. I feel
[Adam Leventhal] [22:52] We did not. That's right. But we took we took I need to catch a train and go into the bathroom instead as like a clear signal that he was not that interested in our demo, which is fine.
[Bryan Cantrill] [23:03] Right. Right. No. But we drove through all of the other social stop signs that indicated that I am absolutely not interested in this. It was the I need to catch a train while
[Adam Leventhal] [23:11] working in the bathroom, and it actually turns out,
[Bryan Cantrill] [23:13] you know what? I think you might not be that interested in this.
[Adam Leventhal] [23:15] Social restraining order. Yeah.
[Bryan Cantrill] [23:18] Based on this restraining order, I think he's not interested in our ideas. So, yeah, sorry to the wait, Dennis, Richie, for, for giving you a fight or flight reaction. But then I do I'm trying to remember, like, the we had a boss. I do remember that, that we had a, like, boff that night. That was pretty interesting.
[Bryan Cantrill] [23:37] We got, like, some there were some, some good conversations. The, but then I I kinda got back, and I was like, man, this is that was really not what I was expecting.
[Adam Leventhal] [23:47] Do we need to explain what a boff is? Is that is that a thing that everyone knows?
[Bryan Cantrill] [23:51] That's a good question. Is a boff that's a you know, we we might. Yeah. Boff. I don't
[Adam Leventhal] [23:56] go ahead. Because, like, conferences are kinda I mean, I feel like they're I mean, back then, I think we could count on our colleagues having having gone to conferences, being familiar with and don't think that's the case anymore. So
[Bryan Cantrill] [24:08] Yeah. That's fair.
[Adam Leventhal] [24:09] You you wanna take on BoF?
[Bryan Cantrill] [24:10] Yeah. No. Yeah. Go for Take it away. What's the BoF?
[Adam Leventhal] [24:13] BoF is birds of a feather session. Kind of a weird name, I thought. I continue to think. And it's like a sort of, like, focused mid conference, like, get together on a particular topic. Is that accurate?
[Bryan Cantrill] [24:27] For sure. It's apparently a deck is term from the deck user group.
[Adam Leventhal] [24:32] Wow. It
[Bryan Cantrill] [24:33] is a weird birds of a feather is a is a I mean, these birds of a feather stick together is the is is what it's a reference to. Right. Wait. Maybe that wasn't obvious, but also, like, a very, like, antiquated kind of folksy saying.
[Adam Leventhal] [24:47] Very folksy. Right. I mean, I kind of think that, like, even as you say it, I'm like, could I convince my son that that's a real term, like, expression? Probably not.
[Bryan Cantrill] [24:57] I think you're right. I think that definitely sounds like that's a I think it like, certainly, my 17 year old would be like, I that's a Simpsons reference, but I don't know which one you're making. I'm like, no. That's not a that's not an ape Simpsonism. So, yeah, goofy kinda term, but, basically, it's a group of folks that get together.
[Bryan Cantrill] [25:13] It's a it's kinda it's a little bit of structure on the hallway track. We're gonna, like, actually, you know, get get some beers and and and those were, like, really important and I'm sure and I know they still exist at conferences, but, like, in especially in the kind of the that earlier era, this was the way that you would exchange ideas because it just was not like, the the things were just not new as online. So the I mean, obviously, in 02/2004, that was changing. But certainly in 1994, it's kinda like that or used that. I mean, there's not a whole lot of other vehicles for this stuff.
[Bryan Cantrill] [25:43] So the the so we had a bob session on Detroit, so I remember that night, which is great. But I don't remember, like, I don't coming back from that, I'm like, that was just not what I was expecting, which is part of what prompted me to to kinda write this blog post on, like, what's going on with this conference that I titled with their Usenex? And it feels like this should have been all practitioners, and it's not. It's all academics. And I kind of went into a bunch of other conferences that I thought kind of should be similar, and you get a lot more kind of academic, practitioner coauthors on papers, and that was definitely not the case.
[Bryan Cantrill] [26:24] And they this is what they also had Phrenics. Do you remember Phrenics? No. So Phrenics was this, like, short lived I think, again because to Usenix's credit, they Usenix was awake during the surgery. They definitely knew this was happening.
[Bryan Cantrill] [26:40] Like, that this is because and the I don't know if you you read Rick Farrow's piece that I linked to. Like so there was there was a very, very good piece, that was, written after I gave my my my very hot ATC twenty sixteen talk. The so Rick Farrow wrote a very good piece talking about kind of the history of Usenix and how, like, academics and kinda deliberately sought out Usenix ATC because it had a big audience. And the the the that big audience was way attractive to those academics. So, like, there's a degree to which the and and the kinda 02/2004 games, one of those shoulder years where the academics are now kind of, like, now coming to control all of of ATC.
[Bryan Cantrill] [27:32] And they know that this is happening, so they wanna kinda create this other track, Phoenix, which I don't think Phoenix lasted more than a couple years. I think Phoenix did exist in 02/2004, though, which is around actually open source software, which is of interesting. But the the standards were much lower. Just wasn't a like, people weren't really paying attention to it, so it did it it kind of withered.
[Adam Leventhal] [27:49] Was it sort of like OSCON, like, adjacent in the early days or something? Was that was it a similar kind of vibe?
[Bryan Cantrill] [27:57] I think that that was kind of the idea, but I just thought it was a good idea, and I don't know why they discontinued it. Because I kind of thought I thought that it was it was again, it was this kind of referee track. Let's get started in 02/2001. So I think in 02/2004, it definitely was still happening. But I think it was kind of done by, like, maybe 02/2007 02/2006, '2 thousand '7.
[Bryan Cantrill] [28:19] And I think that the kind of the idea, the hope was that you would create this vector for what we would call more like practitioner authored content. And I was, like, just looking at, like, the free index 02/2004 track. Was like, yeah. That actually looks like like that. Interesting.
[Bryan Cantrill] [28:34] Like, I that that does look better. Or at least it looks like I mean, like, just looking at the the FreeNix two thousand three agenda, I mean, you got, like, the flexibility in ROM, a stackable open source bias. Right? Like, that's I wanna go dig that one up. That seems interesting.
[Bryan Cantrill] [28:51] I mean, there's some interesting stuff in here, least stuff that that seems germane that was not gonna be in Usenix in the Usenix AIoTecho conference, Usenix ATC. And so this kind of like there's beginning to get this kind of stratification where you're getting this all academic conference in Usenex. And I was kind going back to that. It's kind of amazing. I had this I can't easily resuscitate the comments section, unfortunately, for our old WordPress blog.
[Bryan Cantrill] [29:21] I need to find a way to do that. Because the comments are kind of amazing for this. It's like I am going back and forth with Werner Vogels in the comments having, like, meaningful discourse. It's which just got, like, kinda like, wow. That's the comment section for a blog.
[Bryan Cantrill] [29:37] Used to be where we would
[Adam Leventhal] [29:39] It's crazy. And that that and that was the only place. Right? Like, I mean, maybe on, like, Newsroots
[Bryan Cantrill] [29:45] or something like that. Exactly. Yeah.
[Adam Leventhal] [29:46] Or the or, like, IRC. Yeah. Or slash that. Exactly. But, like, where else are you gonna have that?
[Adam Leventhal] [29:52] It it's even the thought of a comment section of a blog is is sort
[Bryan Cantrill] [29:57] of so quaint right now.
[Adam Leventhal] [29:59] Yeah. I know. Right? Right.
[Bryan Cantrill] [30:01] I know. Is it very quaint? And we're kind of going back and forth on this stuff. And, you know, and basically, like, he saw the same problem that we saw, which is, like, academia is controlling this conference. It's lost the practitioner content.
[Bryan Cantrill] [30:16] And the question is like, how do you get that back? You Verner's point was like, look, we need more practitioners to be on program committees. Like, if you don't have more practitioners on program committees, we like, we're not gonna go solve this problem. I I, you know, I I felt it was more on Usenix to find a solution to this. I think it's a little bit much to to lay have you been on a program committee ever?
[Adam Leventhal] [30:43] Only only your program committee. So should I count that for for the systems we love?
[Bryan Cantrill] [30:49] Systems we love. Yeah. That was a good what'd you think about that program committee? Yeah. That was a good was great.
[Adam Leventhal] [30:54] Thought It was great. I'm just annoyed with it. They didn't accept my paper, those jerks.
[Bryan Cantrill] [30:58] Is that true? That's proof
[Adam Leventhal] [31:00] of But it's okay. It's okay.
[Bryan Cantrill] [31:01] Yeah. We did a you know, because it was the systems we love, which was this conference, I well, I had unspent marketing dollars. You know this is the origin this is the origin of this.
[Adam Leventhal] [31:14] The thing I love most about it is the unspent marketing dollars went into this conference for which the t shirt, like, forgot to mention Joann, Triton, like, any of your stuff. Right? It's it's like just the logo. Enough.
[Bryan Cantrill] [31:28] Yeah. It's a great t shirt.
[Adam Leventhal] [31:30] Amazing t shirt. It's just remarkable that, like, those those excess marketing dollars couldn't, like, put up, like, a logo on it or whatever. I'm glad it doesn't have it. To be clear, it makes it much more wearable. But
[Bryan Cantrill] [31:43] But may we may we all be blessed with unspent marketing budget that has so few strings attached. So we basically had to spend 40 k in, like, in, like, forty five days. And I'm like, I can do it. I can do it. I can I can do it?
[Bryan Cantrill] [31:59] And I what I I was trying to do with systems we love, and it was actually was coming after this twenty sixteen ATC talk that I gave. I was actually we'll we'll kinda get systems we love in a second. But we we so we were kinda having this back and forth about, like, the right way to get folks engaged. In 02/2010, I was asked to be on the parking committee for OSDI for the the optics, and we talked about OSDI in our our previous episode. And it was really and I will direct people to my, my e the a my ATC keynote on what a disaster it was, but it was a disaster.
[Bryan Cantrill] [32:37] The crew the program committee was based I mean, it was really, really, really bad. Wasn't, like, one didn't you have,
[Adam Leventhal] [32:43] like, someone like Keith or someone else on the program committee with you? Didn't you have some some, someone else in industry to get this commiserate with
[Bryan Cantrill] [32:51] asked him Keith asked me to do it, but I think he was not act if he was a he certainly was not in the meeting, the program committee meeting, and maybe I he he wrote me into it. I can't remember if he was actually on the PC or not. The no. It was bad because so I was one of extremely few practitioners on that PC. And every paper that I I I liked plenty of papers, but those papers were all killed.
[Bryan Cantrill] [33:17] I was the only one that liked a bunch of papers. People are like, this is and it's even it's like it's that same criticism that we've seen before. Right? Where I like something because it was real. Academics had disdain for it because it felt small or insufficiently novel.
[Bryan Cantrill] [33:33] Interesting. And I don't know if you if you actually I don't know if you went through the those some of those old blog entries. Do know what I held up as an example of something that's, like, small but interesting and real?
[Adam Leventhal] [33:47] No. Tell me.
[Bryan Cantrill] [33:48] No hut minus p.
[Adam Leventhal] [33:51] Right. Right. My my my great claim improvement on the late Joseph Osana's, no hop. No hopping of running
[Bryan Cantrill] [34:00] process. Yeah. Yeah. So maybe I Could you describe the hop minus p? Because this is Yeah.
[Bryan Cantrill] [34:04] This is really this is something that I mean is, like, it is is this expansive? No. But it's actually, like, real, and it's tricky. Right? It's actually a risky problem.
[Adam Leventhal] [34:12] It it actually intersects with my proposed topic that for systems we love that you rejected. So the folks have run NoHop, and now now NoHop minus p is also on Linux. But way back in in the day, what would happen is I'd run man. I'd I'd go to build the Slayer's kernel. And the way you did this is with the command called nightly.
[Adam Leventhal] [34:35] Now, dear listener, how long do you think it was expected to take if the name of the command was nightly? Okay. So it took a minute. It took a while. I wonder if
[Bryan Cantrill] [34:43] you could It took twenty five hours, by the way. That was actually a real moment of crisis where it's like and actually, it can't be fortnightly. It actually has to be nightly. We have to make this thing go faster.
[Adam Leventhal] [34:51] So like we so you'd like you'd start running nightly. It would churn for like an hour of the 25 it was planning on run, and then you'd realize that you had forgotten to nohub it, and like you'd be wanting to run out the door or whatever, but not being able to kill that terminal session. So no hub the the right way to run your command was under no hub so that it would mean that when you closed your terminal, it wouldn't kill off the process. But the way that everyone ran it for
[Bryan Cantrill] [35:18] me was to plant one, Adam.
[Adam Leventhal] [35:19] That's right. Right. So this is like I think this would annoy us for everyone, but particularly for me, because I would always forget to run things under no hup. So we say, why can't we do it after the fact? And NoHUB ing things after the fact turned out to be fairly tricky and involved in our implementation of Solaris, the use of the agent LWP.
[Bryan Cantrill] [35:40] I'm not
[Adam Leventhal] [35:40] sure if we've talked about that.
[Bryan Cantrill] [35:42] We have not. No.
[Adam Leventhal] [35:43] Maybe Yeah. We must have we we one of the maybe for episode two, I think, was or maybe three was talking about
[Bryan Cantrill] [35:50] we talked about Roger. No. We talked
[Adam Leventhal] [35:53] I think it's I think the title of it is like slash proc to proc macros. So it's not impossible that we've talked about it, but it's been Are
[Bryan Cantrill] [35:59] you like rain man for Oxide and Friends? Like, you mentioned the agent LWP, and you're dropping the episode number. This is insane.
[Adam Leventhal] [36:07] Yes. I am. Okay. Alright. You said the the agent LWP deserves several episodes all on its own if we haven't done it yet.
[Adam Leventhal] [36:18] But or maybe a talk at a conference someday. But the the Noah minus P allowed us to.
[Bryan Cantrill] [36:25] You have to give a little more context for the agent LWP.
[Adam Leventhal] [36:27] Okay. Agent LWP is awesome. So agent LWP is and and it I think it's not just awesome in its own right, but it's a really neat programming model. So I think that a lot of other systems have ptrace. Ptrace let debuggers kind of do things to a process.
[Adam Leventhal] [36:44] Roger Faulkner, you know, one of my mentors, may he rest in peace, one of our great inspirations at Sun, colleagues at Sun, invented the slash proc file system, and he invented this cool mechanism called the agent LWP. And what it allowed you to do is send in an LWP, effectively a thread, to do work for you. It's amazing. So you could send in this thread, and the thread was very bare bones. Like, if you wanted to have a stack, you had to make a system call to M Maps and memory to get it a stack, and it could do all kinds of work for you.
[Adam Leventhal] [37:19] So is that a fair synopsis of the agent?
[Bryan Cantrill] [37:22] It is. You know, it wasn't always that way. It used to be that you would hijack a you would stop the process, and then you would hijack an LWP and make it execute system calls on your behalf. And Roger kept tracing so you basically like, the the the process is under, like, general anesthesia. Right?
[Bryan Cantrill] [37:40] And it does not know that it's out. It stopped while you're controlling this. You would you would pick this representative LWP, and the representative LWP would do this work for you. And the problem is you kept chasing these bugs where there'd be these little artifacts that would be left behind where your architectural state from an LWP perspective would be subtly wrong. Mhmm.
[Bryan Cantrill] [38:06] And they were just they were becoming impossible to clean up. And the and the reason you want this at all is because if you can have the process act on its own behalf, albeit at the at the behest of a process that's outside of it, you can ask any question about the system. So
[Adam Leventhal] [38:25] yeah. Not only that, but you don't need to invent like an alternative world in the debugger. Like That's right. You don't you don't need sort of the system call for myself or system call for somebody else. Open a file for myself, open a file for somebody else.
[Adam Leventhal] [38:37] But but rather the agent LWP was a way to make use of all the stuff that a process could do, but execute it remotely. And then as as, you know, rather than kinda hijacking a particular thread, one of the neat things about the agent LDP is that if it is present, then all other threads are stopped. So it allows for cleaner semantics on the behalf of the debugger.
[Bryan Cantrill] [38:59] Yeah. What was the what was the sitcom with the girl that stopped time? In did you Yeah. No.
[Adam Leventhal] [39:05] I I do. I'm not gonna I'd not
[Bryan Cantrill] [39:07] Out of this Nice. Well done. Out of this world, did you the did you ever watch out of this world? It was like I'm sure I did. Back to back with small wonder.
[Adam Leventhal] [39:18] Remember this Small wonder.
[Bryan Cantrill] [39:20] The the I I actually think that children should be forced to watch these things just so they can get a little more appreciation for how bad it was when we were growing up. The but but the you got as you say, like, if you are just in the context of the agent LWP, you know that everybody else has stopped, which gives you some luxuries about like, you you know some things about it. So so how do we use the h and l p? Why did know how minus p necessitate the h and l w p?
[Adam Leventhal] [39:45] Yeah. So let's see. What you need to do when you're doing a no hub minus p is, like, close all of the file descriptors. Like, a closed file descriptor zero, one, and two, and then reopen them to, like, a a new file. Right?
[Adam Leventhal] [39:59] So rather than sending output to a terminal, you'd send it out to a file. And as a recall, like, you need to send in the agent to go close those file descriptors. And, also, I remember there's some subtlety to it. Like, it it sometimes it would block. Sometimes you had to actually just wait for you know, if there was an intervening IO operation, it could cause the close to fail.
[Adam Leventhal] [40:24] So you had to, like, nudge things forward until the files file descriptor became closable. But then once you got everything closed up, then you could reopen those files or or or reopen those file descriptors to the the place where you wanted the the process to send its output.
[Bryan Cantrill] [40:41] That's right. And it was like which is like so there's like a lot of tricky details to get right on something that just feels like, can't you just do this? Like, why? It's actually it's really complicated. It's complicated.
[Bryan Cantrill] [40:54] It requires just, like, a bunch of mechanism that if you didn't have, you would need to invent, basically.
[Adam Leventhal] [41:00] Right. Right.
[Bryan Cantrill] [41:01] And I, like, use that as as an example of, this is something that, like, academia would view as trivial and uninteresting that we actually viewed as, no. No. It's actually, like, pretty interesting, and it's definitely not trivial. It's actually hard to get all this stuff right. And we like that stuff, but they're like, no.
[Bryan Cantrill] [41:21] We don't we do not like that stuff. That stuff is not which is and I think it kinda showed that, like, that that disconnect that, like, no. No. We want a the like, OS research or or research should be we emphasize novelty over all else. And for a practitioner, it's kind of utility over all else.
[Bryan Cantrill] [41:43] And the novelty is, great, but it's actually it's the utility that trumps the novelty.
[Adam Leventhal] [41:48] I was gonna say also it's that it's that sort of last mile, right, where Yeah. I think in in research, it can be sort of boring or sort of beside the point or maybe past the point that you need to in terms of a little bit of the distinction I felt early as an engineer, the difference between completing an assignment and shipping a product. Where you're like completing assignment, it's like, yeah. Like, it works, you know, like most of the time or whatever. Like, maybe sometimes it doesn't, but like, what's the big deal?
[Adam Leventhal] [42:15] As opposed to systems programming where, like, the the tests and the edge cases are everything. Right? Like, that last mile is everything. And I think that was some of that dichotomy that we were seeing between the practitioners and the academics.
[Bryan Cantrill] [42:28] Totally. Did you take Morris's, lock and wait for data structure course?
[Adam Leventhal] [42:32] I didn't actually. No. No. I didn't. Did
[Bryan Cantrill] [42:35] you work with Morris? This is Morris Rollehi, a professor that we had in common. Really a super interesting professor. But so he in that course, you would I loved it because you like, the entire coursework for the course was taking a research paper and implementing it. And effectively, everyone that implemented the research paper discovered a bug in the research paper.
[Bryan Cantrill] [42:57] That's awesome. That's surprising. Well, actually, I'm not sure if I, maybe we haven't said it here, but so, Mike was working with Tim Brennan. I'm not sure if you know Tim. Yeah.
[Bryan Cantrill] [43:09] Okay. Yeah. So they were working on implementing a, diffracting trees, which was this hot new weight free data structure for this guy near Shabite. And so they implement it, and it's like the results are just like terrible. Like the results are way worse than, like, just doing the dumb thing.
[Bryan Cantrill] [43:32] You know what mean? It's one of these things that, like, diffracts contention. So you end up you you kinda look at it and you're like, is that gonna pay the freight? Because that's really optimized for contention, and you're gonna do a lot of more you're gonna do a lot more memory accesses. So it's like, boy, if you end up, like, hitting a line that's not there, like, you're gonna endow it.
[Bryan Cantrill] [43:48] And so it's like, I don't know. I I I'm kind of skeptical about it. So they but they it's like, they go to implement this thing, and it's like, doesn't work, or it's the price is terrible. And I'm gonna go do this right. This an amazing story.
[Bryan Cantrill] [44:00] So they are like, okay. We're screwing something up. So they kinda went back over it and like, okay. We're screwing something up. No.
[Bryan Cantrill] [44:05] We can't find him. We can't find him. We find him. So then they go back is they so they mail Shameet. Like, hey.
[Bryan Cantrill] [44:11] Like, like, we're we're we're struggling to replicate this work with, like, something that barely exists in in academic computer science, like, replicate the work. We're struggling to replicate this work. Like, can you help us out? And, of course, he's like, I look. I didn't actually do my implementation.
[Bryan Cantrill] [44:26] Like, my grad student did the implementation. Right? So they get handed off to the grad student. They're having some communications issues with the graduate student, and they're just not able to get, like, the they can't find how they've misimplemented this thing. And Mike's getting increasingly frustrated.
[Bryan Cantrill] [44:44] And finally, it actually, like, pretty good idea. He says, like, I am doing exactly what you're doing, and I'm getting literally the inverse of the results you're getting, and I don't understand what we're doing wrong. But all of this, this is like before S and P machines really existed. I mean, they existed, but they were not so prevalent that you could do research on them. So they they were using a simulator for this, not an actual machine.
[Bryan Cantrill] [45:12] And so Mike is like, give me the configuration for your simulator. And he in the configuration, you know, you specify you wanna parameterize the simulator. So you specify all these different, like, latencies effectively for all these different kinds of accesses. They had configured it such that a local access in cache yes. A local access in cache took longer than a remote cache hit from another CPU.
[Adam Leventhal] [45:42] Yeah. I mean, that'll do it.
[Bryan Cantrill] [45:44] That'll do it. It's like, hey. You know, I gotta tell you. Like, it's a real greenfield for algorithms in upside down Alice in Wonderland can't be big world.
[Adam Leventhal] [45:53] Yeah. If you're like, if if your cash has a negative impact, then, yeah.
[Bryan Cantrill] [45:58] It's a negative.
[Adam Leventhal] [45:58] Yeah. Yeah. It's like,
[Bryan Cantrill] [46:00] wouldn't I just turn it off? That's another paper right there, my friend. Like, why don't you publish that? No. It was, so and this is like this should be a isn't this like and, you know, this was happening right when ColdFusion, which is now I think people think of ColdFusion as kind of like a Theranos like brand or maybe not.
[Bryan Cantrill] [46:23] But ColdFusion, this group at Utah thought they had ColdFusion, that kind of desktop fusion, and they didn't. And it was like, you know, there were
[Adam Leventhal] [46:32] Is this like late nineties? Like, this this is
[Bryan Cantrill] [46:34] Mid nineties, I think. Or even like
[Adam Leventhal] [46:37] Yeah.
[Bryan Cantrill] [46:37] I think this the or, even, like, early nineties. When was that? And it was, was in the kind of that era, and it was a big scandal, of course, when this computer it was like this this superconductivity thing that happened. Remember, was like there was like Oh, yeah. There was like three days online when we thought we had room temperature superconductivity.
[Adam Leventhal] [47:00] I do remember that. Right. Yes.
[Bryan Cantrill] [47:03] And everyone just kinda lets their imagination run wild on that single result. And it's like, wow, this is like we're gonna, like, we're gonna actually, like, have world peace with room temperature superconductivity. It's like, it turns out the results were wrong. It's like, oh, great.
[Adam Leventhal] [47:17] So this is 1989. I just looked
[Adam Leventhal] [47:19] it up.
[Adam Leventhal] [47:20] And I think that
[Bryan Cantrill] [47:20] 1989. Wow.
[Adam Leventhal] [47:21] Yeah. I think there was a time, like, I must have been, like, right then when, like, maglev trains were, like, going to be real. And, like, everyone was going to kind of travel on Maglev trains. And this was like a a the kid, like I
[Bryan Cantrill] [47:38] mean, we've got a Maglev train together.
[Adam Leventhal] [47:41] Should I? Oh, yeah. I guess I did there you go. But
[Bryan Cantrill] [47:45] It just breaks my
[Adam Leventhal] [47:46] We don't we don't have them everywhere.
[Bryan Cantrill] [47:48] You you may everywhere. You may have noticed. I'm on my Maglev train right now. That's why the audio is
[Adam Leventhal] [47:53] so bad in here. Yeah. Calling from the Maglev.
[Bryan Cantrill] [47:57] You're right. We don't and there was this kind of idea, and Cole Fusion was a big part of that and had become this big scandal. And I'm like, this is a scandal? Why don't we publish this? And I remember and I'm like, dude, this is like they should go publish this at a conference.
[Bryan Cantrill] [48:11] And we're just like, you know, you could do that. But, if you were to publish this, you know, this, like, this paper was probably dated with best paper, probably beat out something that was much more deserving. But if you do this, they're just gonna spend their entire life trying to validate your results, and no one wants that. Basically, like, no one wants to you might as well just, you know, just go do something else. And I just remember being like, god.
[Bryan Cantrill] [48:34] That just I mean, it's just it felt really but it was also kind of I think I mean, I guess you can take that one in two ways. One is it's like it's it is pretty disheartening. On the other hand, it does from another kind of lesson to draw from that is, like, the details really matter in systems. And you can have an idea that seems valid all the way to the end and like, whoops, there's this one detail, you are simulating an impossible computer, that actually completely invalidates it. And you actually need to be able to have a system that's completely implemented to to be able to, to actually really validate the idea, which I think is, like, kind of a central I mean, I don't know.
[Bryan Cantrill] [49:14] That's a belief that, yeah, I think you and I definitely have.
[Adam Leventhal] [49:17] So yeah. Have I told you about my own brush with a a paper that that I couldn't who's no. So this is very relevant, actually. So we implemented ZFS RAID z, Then we implemented RAID z two, so double parity RAID. And then when I was going to implement triple parity RAID, I, like, could not get the math to work.
[Adam Leventhal] [49:41] Could not get the math to work was in particular recovery scenarios. That is to say, if I have a stripe of particular width and I have failures of particular drives that should be recoverable, it was not recovering. And and the paper said it should work. I did the math and and, you know, was one of the
[Bryan Cantrill] [49:59] things working in the notebook or was not working in the implementation?
[Adam Leventhal] [50:03] Not working in my implementation. K. Single and double parity, implementations were done and shipped. And in the meantime, triple parity rate was not working in my implementation of it. And I would also note that this was a highly stressful moment for me because I was thinking, did we not sufficiently test single and double parity enough?
[Adam Leventhal] [50:22] Like, are we have we shipped data corruption?
[Bryan Cantrill] [50:24] Yeah. Why? You know, when are you working on this? And Yeah. Yeah.
[Bryan Cantrill] [50:28] This this was in, like, February and, like, 07/2008, something like that.
[Adam Leventhal] [50:32] Yeah. This was at Fishworks. So yeah.
[Bryan Cantrill] [50:34] This At Fishworks. Yeah. Yeah.
[Adam Leventhal] [50:36] So then I'm, you know, I'm trying I'm this is causing me now to, like, go back to the abstract algebra that I ostensibly learned in college, and this is another great example of the difference between learning and implementing. Like, I thought I understood abstract algebra, and then I needed to go apply it to a real task. And then I I realized how little I actually understood. And it turned out
[Bryan Cantrill] [50:58] that this Can I just ask a question? Like, isn't the whole point of abstract algebra that like, aren't you talking about it, like, concrete algebra? Like, isn't the whole point of abstract algebra that it can't like, it has no actual it it can't be reduced implementation. I mean, just feels it's
[Adam Leventhal] [51:13] No. No. So this, like, Gau you know, that's where we learned
[Bryan Cantrill] [51:16] about Gauwat fields. Theory. Right? Yeah. Yeah.
[Bryan Cantrill] [51:18] Yeah. Okay.
[Adam Leventhal] [51:19] Yeah. Exactly. So the the Gauwat fields, which are very relevant for for a ratio in codes encoding and that kind of stuff. So, you know, exactly what rate is supposed to be doing. So finally, I I kinda learned enough to figure out, okay.
[Adam Leventhal] [51:35] This under these conditions, it doesn't work. Okay. We had used this paper by Peter Anvin for the single and double parity rate and then triple parity rate because it was so easy to implement efficiently. It it used kind of this this kind of more efficient implementation. So then I go back, and it turned out years later, they published an addendum that's like, oh, yeah.
[Adam Leventhal] [51:58] Yeah. Yeah. You remember that simple matrix that we told you you can apply and how it could use simple operations and be executed very efficiently? That's all not real, and you actually need to use this much more complex matrix. Wow.
[Adam Leventhal] [52:10] But we got away with it in triple parity RAID and only triple parity RAID. Quadruple parity RAID would be much harder because 255 has three prime factors, and and that was, like, a key insight that allowed us to get triple parity raid going.
[Bryan Cantrill] [52:27] So you would get it fixed? Because I remember we had RAIDs e three. Right? So you
[Adam Leventhal] [52:31] We do have RAIDs e three. And because three, five, and 17 are the factors of 255, you were able to construct the Galois fields in such a way where it is recoverable independently regardless of which discs might have failed. But it took that. Uh-huh. It was it's sort of like, because of that, it works for triple parity RAID.
[Adam Leventhal] [52:49] And if you wanted to go for wider RAID or or or more parity disks effectively or additional parity, you would have to use a slightly different scheme.
[Bryan Cantrill] [52:58] That's really interesting. And, of course, like, this was an mean, these were these super wide stripes. Right? This is what we're talking about, like, 46 plus three stripes or something like that. I just remember,
[Adam Leventhal] [53:10] like, this is these were We're we're, like, looking at a thumper, which was 48 drives or something like that.
[Bryan Cantrill] [53:15] Three drives.
[Adam Leventhal] [53:16] Saying, like, yeah, we're gonna do,
[Bryan Cantrill] [53:17] like Like, forty four forty three plus plus one or something like that.
[Adam Leventhal] [53:20] Yeah. Exactly.
[Bryan Cantrill] [53:23] And it's not like economics begin to break down too because, like, those those ultra wide stripes have got other problems associated with them.
[Adam Leventhal] [53:31] Yeah. Some some IOPs challenge opportunities challenges.
[Bryan Cantrill] [53:34] Challenges. Exactly.
[Adam Leventhal] [53:36] Yeah. But but, yeah, another I mean, in this case, I've like, they had themselves published an addendum, although we had not noticed the addendum until after we had implemented double and single parity RAID. But it was so it's, like, sort of an exciting moment when you're like, I'm worried that
[Bryan Cantrill] [53:56] all the all the
[Adam Leventhal] [53:57] integrity yeah. All this integrity that we think we shipped actually is just Oh my god. Data corruption.
[Bryan Cantrill] [54:04] Yeah. We've just gotten lucky the entire time. Yeah.
[Adam Leventhal] [54:06] Oh my god. But but but RAID z users know that you have not just gotten lucky. I mean, we got lucky in that it works for exactly up to RAID raid z three.
[Bryan Cantrill] [54:17] Yeah. Wow. Well but, again, it's like the it it was the implementation and the testing the implementation that got you to a flaw effectively now.
[Adam Leventhal] [54:27] Exactly right. Yes.
[Bryan Cantrill] [54:30] And it's, like, great when stuff is provable, but that doesn't happen very often in system software. And it's it it it so we, yeah. The guy that is that is really interesting. Well and I think I mean, this is why, like, you need the like, the implementation really matters. And just, like, over and over again, you see these ideas where it's like, this is not implementable.
[Bryan Cantrill] [54:47] And I think that that was part of the frustration with where with the the kind of academic systems work, it was kind of going where it was stuff that was because it's on the one hand, they would kind of deride something like no hop minus p is being too small. On the other hand, the stuff that, like, a grad student can do in a couple of years is also not, like, expansive. It's not like, I mean, it's really like, that work is actually kind of bounded in size. And, I mean, this was the the subject of Rob Pike's polemic. Did you did you go back and relook at that that that polemic?
[Adam Leventhal] [55:20] Yeah.
[Bryan Cantrill] [55:20] Yeah. Yeah. And do you remember that coming I mean, I definitely remember that coming out at the time. What was your
[Adam Leventhal] [55:25] I do. But I I I mean, I remember reading at the time, but I don't remember. I I don't remember in detail.
[Bryan Cantrill] [55:31] I just wanna be like, I think this guy is like he's making some good points, but he's also being, like, way too reductive. And it's, like,
[Adam Leventhal] [55:40] it is being really like Rob Pike.
[Bryan Cantrill] [55:41] Yeah. It does sound like Rob Pike. I know. And it's also, like, got this, like, funny I mean, I do wonder, is this, like, is this the original formatting for this document? Like, I think it is.
[Bryan Cantrill] [55:53] I think this is just, like, the original formatting is just, like it's not it's it's like, it's not really a slide deck. It's kind of, you know, written anyway, whatever. I'm Dijkstra would be very horrified by this. But the you know, I think he was like, there's not enough, like, big things happening. And then the irony is that, like, he did I mean, he ended and maybe this is why he wanted it'd be interesting to get his perspective on this.
[Bryan Cantrill] [56:19] Is he is he trying to be was he did he end up being the difference he wants to see in the world, or is it kind of happenstance that he almost, like, showed this to be incorrect by doing Go. Right? And Mhmm. Showing, like and maybe he doesn't call that research. I'm not sure.
[Bryan Cantrill] [56:34] And maybe that's where it hinges on. I don't know.
[Adam Leventhal] [56:36] Yeah.
[Bryan Cantrill] [56:39] The but his things to do slide, I think, is really interesting. Like, go back to think to thinking about and building systems. Narrowness is irrelevant. Breadth is relevant. It's the essence of system.
[Bryan Cantrill] [56:53] Work on how systems behave and work, that's how they compare. Concentrate on interfaces and architecture, not just engineering. That's like, okay. I don't really agree with that. Be courageous, try different things, experiment, try to give a cool demo, definitely agree with that.
[Bryan Cantrill] [57:06] And then funding bodies fund more courageously, particularly long term projects. Universities in turn should explore ways to let students contribute to long term projects. Absolutely agree with that. Measure success by ideas, not just papers and money. Make the industry want your work.
[Bryan Cantrill] [57:22] And I think that that's like that I think for academic systems work, that's been a struggle. But then when I look at kind of systems research larger, you know, it's now we we don't rely on Usenix or any other academic vehicle to I mean, like, I don't even, like, with ZFS, we didn't there's not a ZFS I mean, there probably should be a ZFS paper. But for for the stuff we did after that, we used, like, either ACM or blog entry. Mean, blog entries were obviously really important. Like, we just didn't use the the kind of the academic publishing vector as a publishing vector.
[Adam Leventhal] [58:05] Yeah. Which I think It's just lost its relevance for us. Right? Candidly. Yeah.
[Adam Leventhal] [58:08] I mean, both both based on the the the observations we had in 02/2004. But then, as you say, like, this was the dawn of blogs. Right? This is the you know, before Twitter. You know, there just became lots of different ways to reach our audience.
[Bryan Cantrill] [58:25] And the thing that kinda sucks about that is that you end up getting, I think, less cross pollination between academia and the practitioner,
[Adam Leventhal] [58:36] which I think would be good
[Bryan Cantrill] [58:37] if there were more cross pollination. And that I think is the kind of the big thing that we lost. And this is where you kind of get to this thing that I did. So, you know, this program committee that Keith had talked to to be on in 2010, It was a disaster because I was kind of the only practitioner. I the papers that I liked did not make it to the program committee.
[Bryan Cantrill] [58:58] And so what it meant was that on the program committee, the and, obviously, like, the stuff that everyone agreed should be accepted, we didn't talk about that. We probably should have, actually, have been a lot more mentally healthy to be like, no, no, let's take some time and talk about the stuff we all agree on so we can be happy, but we didn't do that. That stuff we just submitted. And so all of the time as a program committee, you're arguing over the stuff that's on the bubble, and I was always on the other side of like, no, this is like this idea is not implementable. And never alone, there's always someone else in the room that was arguing with me alongside me, but goddamn, I was arguing against the entire room so many times over.
[Bryan Cantrill] [59:36] And at the end of the day, people are like, you're a really negative person. I'm like, I'm actually not. I just I like, I've been in this position all day where I'm arguing against stuff and arguing about keeping stuff out, and I just hated it. And then the way like, after the fact, the program committee chairs decided that they didn't admit enough things. So one of the things that I had successfully kept out of the conference, they just decided to unilaterally admit to the conference.
[Bryan Cantrill] [01:00:05] And actually, it was funny because, like, I wasn't even like, at that point, I'm like, I actually don't even care. But that made that, like, weaponized everybody else. Everybody there were a bunch of other people in the program committee that were super upset by that. I I mean, probably for good reason because the program committee was a lie. But then when Usenix ATC in 2016 had me come back and give this keynote, again, huge mistake, didn't do their homework.
[Bryan Cantrill] [01:00:35] I'm like, well, I'm gonna, like, talk about everything that's broken in academic computer science and the fact that we use conferences as the publishing vector. Like, we're the only discipline that does this. And every other discipline uses journals or something that looks like it, and we seem crazy. I mean, if you've ever, like, talked to a neuroscientist or a biologist or whatever and explain if you do this, you explain what we do in computer science.
[Adam Leventhal] [01:01:02] Yeah. Yeah.
[Bryan Cantrill] [01:01:04] And they're like, what are you talking about? I'm like, I know. I know. I know. Know.
[Bryan Cantrill] [01:01:07] Just Why
[Adam Leventhal] [01:01:07] why do you think that is? How how do we get here? Like, why why is that the way it is?
[Bryan Cantrill] [01:01:11] Oh, I think it's the way it is because in the seventies, computer science was, quote, moving too fast. It's like we the journals are slow, and this is like in an era before desktop publishing. Right? So you would send something into a journal, and it would be published, like, nine months later. You know what I mean?
[Bryan Cantrill] [01:01:28] I think it's like Yeah. Right. I think that there is a legitimate in, you know, that world, which is now so distant. There is a legitimate thing to say, like, no. Like, we are moving faster than that publishing thing that publishing wheel can turn.
[Bryan Cantrill] [01:01:44] And I think what actually happened is kind of interesting is that I think every other discipline now moves as fast or faster. Right? And so the like, ultimately, like, clearly, the publishing models had to change. But computer science be this became entrenched in computer science. And now, like, it's one of these things that everyone thinks the system is broken and no one feels empowered to change it.
[Bryan Cantrill] [01:02:11] So people are like, no. No. Like, you because now you have to have these gigantic program committees for these conferences in order to have the workload. And it's like now being on the PC is part of the thing you need to do to get tenure. So if we eliminate those PCs and have them be standing journals like other disciplines do, how do these people get tenure?
[Bryan Cantrill] [01:02:31] And you're like, what problem are we solving
[Adam Leventhal] [01:02:33] here? Exactly.
[Bryan Cantrill] [01:02:36] I mean, it's okay. I feel like it's like, okay. So we're solving, like, OKRs or conflicting MBOs or whatever. You're kinda you're I feel like
[Adam Leventhal] [01:02:43] Yeah.
[Bryan Cantrill] [01:02:45] And it's and like so you kind of have, like, conference model is just and I was very even for me, I was definitely hot in that in that ATC keynote. The reaction actually was interesting, and there were some people who were very offended by it. But and I like, I'm particularly remember, and you could hear it on the audio, a guy kind of calling me out afterwards being like, you should not be saying this about that program committee because people will get the impression that that happens on many program committees, and that was just the program committee that you're on. It's like, alright, dude. But I was like, okay.
[Bryan Cantrill] [01:03:24] I was on one program committee, and this is what happened. So I don't know what what what do mean to do? I mean, it's sure they're not all crooked. Congratulations. I mean, the problem the model itself is broken.
[Bryan Cantrill] [01:03:35] And one thing I did definitely called out there, because I actually think one of the the the papers we love, started by cofounded by our colleague, Zeeshan, I think is great where you go back to some older stuff that's really great and bring that to the practitioner. I love that model. And so Systems We Love was really me trying to like, how do we get something that practitioners are gonna like, let's get a conference where we can talk about interesting work in a way that is exciting for practitioners and is not gonna look like an academic. And so that's good though. And also unspent marketing money.
[Bryan Cantrill] [01:04:12] Fine. And also like and we need to spend $40,000 in six weeks, whatever it is.
[Adam Leventhal] [01:04:17] Unlike papers we love, it was not, I think any of the people presenting, was, like, not their own work. Right? It was it was systems That's right. That they were consumers of and had really demonstrated that it was not, like, a fluke, but but durable.
[Bryan Cantrill] [01:04:32] Yes. And I thought that was I actually I thought that was great. That was Great conference. It was a lot of fun. And the videos that are still, like, are still great.
[Bryan Cantrill] [01:04:43] And, the problem is that we just didn't we, you know, we didn't have unspent marketing dollars the next year. So it's it was it's it was kind of a one and done kind of a thing. But I and then the other thing I think that I mean, as I've kind of been kind of reflecting on this more and more, it's like also, I mean, in terms of of talking about system software, like, open source is really important. That's you know, World War two is stressful. Open source is important.
[Bryan Cantrill] [01:05:10] Mhmm. Seems right. The but this is, like, where it it's like and, obviously, we know it's important. But now going back to looking looking at it from twenty years ago, it's like, man, it is so important because so many of these systems are now effectively published via GitHub. Yeah.
[Bryan Cantrill] [01:05:30] And we consume Go from raw pipe, but, like, Rust, I mean, like, Rust is like it's kind of amazing to me. I don't know. Do do I mean, don't you think it's kind of amazing that, like, a new programming language has been so profoundly important to both of us? I just feel like if you go back to my past self from twenty years ago, I would be surprised to learn that.
[Adam Leventhal] [01:05:49] Yeah. I mean, I I will tell you when I I mean, for sure, when I joined Oxide or shortly after I joined Oxide, you know, I thought, you know, a language is a language. And there were people who loved C and loved Java, and I was like, whatever. It should I don't think I'm capable of that kind of love. So it was very surprising to me that, in fact, I I was not dead inside, and I and I did learn to
[Bryan Cantrill] [01:06:12] love a language. Yeah. Well, because I think that there was this dichotomy that programming languages I felt like I mean, there there was actually kind of this interesting dichotomy in terms of, like, maybe almost like that academic practitioner dichotomy played in the small of, like, the interesting programming language work is not applicable to the practitioner. And the stuff that is applicable to the practitioner is, like, pretty like, the you know? So you you've got, you know, this idea that, like, well, in order to advance the practitioner, you can't do anything new, or you or you have to, like, bring along all these existing semantics, and then we end up with, like, c plus plus.
[Bryan Cantrill] [01:06:53] Right? You kinda end up with, like, the worst of all worlds. And, you know, I think, like, we had a couple different languages that kind of split that false dichotomy, and especially, again, with Rust where it's like, no. We actually can bring these very important ideas in a way that's very relevant to the practitioner, it's pretty great. You know?
[Bryan Cantrill] [01:07:17] I mean
[Adam Leventhal] [01:07:18] No. You're right. And I had previously observed or or felt like programming language research was not that interesting to me unfairly, because it lacked the applicability. You know what I mean? Because I saw for example, in as an undergraduate, we taught OCaml, a version of OCaml so early that the error messages were in French.
[Adam Leventhal] [01:07:40] I'm not making this up. And I I loved
[Bryan Cantrill] [01:07:44] OCaml. It was like I felt like it was I'm sorry. You're sucking, bro. I've got like a Tintin kind of like vibe to it. You know?
[Bryan Cantrill] [01:08:00] Yeah. I'm Like,
[Adam Leventhal] [01:08:02] I love the
[Bryan Cantrill] [01:08:02] And I
[Adam Leventhal] [01:08:03] was like,
[Bryan Cantrill] [01:08:04] yeah. But it was
[Adam Leventhal] [01:08:05] just like, yeah, that's for, you know, classwork. But, like, I can't I'm not gonna go not gonna go build anything real out of it. And, of course, people are building real stuff out of it, but it didn't it it it felt like there were very few choices when it came to doing stuff that you know, outside of an academic context.
[Bryan Cantrill] [01:08:22] Yeah. And the stuff that you would actually use just grew up gritty as hell. Right? You you just like and, I mean, okay, we had c, but then it was like, Perl, which is just like utility only utility. Like, the the no sense of or maybe c plus plus all these things that are just, like, pretty gritty and gross.
[Bryan Cantrill] [01:08:41] And we just kinda have, like, well, there's no alternative. And Right. It's pretty it's pretty great that we
[Adam Leventhal] [01:08:47] Well, Java was the alternative. Right? Java was the emergent clean Yeah. You know, like the the brave new world. Yeah.
[Adam Leventhal] [01:08:58] Such as it was.
[Bryan Cantrill] [01:08:59] But then it then you sacrifice all these other things as Java. It's like, okay. JavaScript, you can't actually use it on the systems that we care about. Right? We actually can't.
[Bryan Cantrill] [01:09:06] Like, Java's fine and valuable for some stuff, but, like, the you
[Adam Leventhal] [01:09:12] know, we Java's fine and valuable for some stuff. I think I think it's I think it's fair. I think that's a fair
[Bryan Cantrill] [01:09:20] It has no unsigned type. It has no unsigned type.
[Adam Leventhal] [01:09:24] I'm I'm not saying it's applicable to all things. I just think it may be underselling some some Java's like
[Bryan Cantrill] [01:09:31] Look, paper in ATC 02/2004, I'm still better. No. Think, yeah, five five five. Java, more broadly relevant. I yeah.
[Bryan Cantrill] [01:09:39] Should but it's like, it was never gonna be useful for the soft for for internal for software, for operating system software. It's like you're just not gonna use it.
[Adam Leventhal] [01:09:46] %. I I totally agree with that. I think absolutely.
[Bryan Cantrill] [01:09:50] What is your introduction to Haskell? Because I think you and I have the same introduction to Haskell.
[Adam Leventhal] [01:09:53] I don't think I've actually written any Haskell. I think like Is
[Bryan Cantrill] [01:09:57] the person you ordered Haskell at a debug 02/2003? Oh, probably. Yes. Do you remember when trying to solve an NP complete problem to generate to be able to generate a an error message that would give you any do you remember this?
[Adam Leventhal] [01:10:10] Oh, yeah. I do remember. I was like, well, like the Haskell type system is NP complete, therefore and you're like, okay. Just stop right there. Like, I
[Bryan Cantrill] [01:10:17] have lost interest. I just remember being like, I am like, I've just heard about this language for the first time, and I am crossing it off the list. It's like weird at that. But the so I think it's like it's pretty great that we have been able to generate a, like, a real innovation for the practitioner that is not quite coming out of the academy, but it's coming out of this kinda netherworld of the open source work that I mean, happening at Mozilla or happening at Google for Go that is, is at once kind of, like, practical and yet open ended and not having an immediate deliverable. Like, that kind of work actually ended up being extremely important.
[Adam Leventhal] [01:11:03] Well, and in the case of Rust, and I think to a lesser degree of gold, but maybe this is not fair, really extremely well informed by all of the research that came before it. Right? Like, just Yes. Not not obese into it, but certainly defiant of it and respectful of of what had happened before so that, like, the the good parts of OCaml or O'Castle or or Haskell no. Not Oh Haskell.
[Adam Leventhal] [01:11:26] The good parts of those language or the applicable parts of those language did did make it into Rust in some form.
[Bryan Cantrill] [01:11:33] Totally. Yeah. I would say Go has less of that property. I think Go could maybe they and I think it might have been part of Go's problems.
[Adam Leventhal] [01:11:40] That's I I think that's fair.
[Bryan Cantrill] [01:11:43] When apparently a bunch of, like, the inspiration for this, we gotta get, like, Klavnik going on the operating systems that, like so apparently, Simula and Clean. You heard of Clean?
[Adam Leventhal] [01:11:56] Maybe from Klavnik. But
[Bryan Cantrill] [01:11:57] No. Right. Exactly. And this is where p l people are like, don't are they seriously just learning about clean for the first time? I mean, I are you really like, this is but I don't know.
[Bryan Cantrill] [01:12:06] Apparently, the I had but I don't know. I love that about Rust. Right? They're, like, kind of pulling in all of, like, those great ideas. But I think that, like, that necessitated the like, open source is what allowed all that to happen.
[Bryan Cantrill] [01:12:19] I don't see how that happens in the proprietary world. I think you that that has to be open source.
[Adam Leventhal] [01:12:24] Yeah. I think you're right.
[Bryan Cantrill] [01:12:26] And so I just think that, like, that this is part of the reason why that kind of conference model I mean, and this is before UTC was before ATC was crashing on Ostie's couch. I mean, it was beginning to really erode quickly because, like, this is only existing as an academic vector. There's no reason for the practitioner to go here whatsoever. And I think it's I mean, I feel like I definitely feel ambivalent about them. I think it's probably for the best.
[Bryan Cantrill] [01:12:56] I think it was it would it would it maybe allow them to do something different. You know what I mean? Like, I would I would like Usics to experiment with different kinds of ideas. And, like like, how do we get to some of the things that conferences get to? And we talked about this, and we had a great episode with with Theo and I and
[Adam Leventhal] [01:13:18] Stupid. Yeah.
[Bryan Cantrill] [01:13:19] Yeah. Yeah. And Kellyanne on conferences. Right? And, like, what are the some of the challenge to conference?
[Bryan Cantrill] [01:13:25] But, like, how do we kinda get to some of that stuff where we get the practitioner to the kind of that advanced practitioner or the practitioner, the academic to really intermingle their ideas. Because I do think that, like, that's the bit that I that that we we do I think I think it's valuable. Right? I think it's I think it's it's given us some great stuff, and I think it's it's important that we kind of continue to do that.
[Adam Leventhal] [01:13:46] Yeah. For sure. I mean, I think we I'm not sure how that cross pollination really happens effectively right now. Like, I think there's there's kind of sponsored research across these different organizations, especially when you get to really big companies that that are investing in the universities. But, it seems narrow, and, it it'd be great to see more inspiration from, in both directions.
[Bryan Cantrill] [01:14:13] Yeah. I think so. And I think it's like how can we I'd I would like to and I know this is tough because I know that this is all, like, wrapped up in the tenure model. But, man, it would be nice to incent I mean, to incentivize academics to produce quality work, which I know sounds like that sounds pejorative the way I'm saying it. But you know what I mean?
[Bryan Cantrill] [01:14:34] It's like you'd
[Adam Leventhal] [01:14:35] be great if Yeah. Indexing it on the quality. Yeah.
[Bryan Cantrill] [01:14:38] Indexing it on the quality and using the quality to get and and I know it feels like very difficult to kinda change the domain in that way. But, man, you could do like, it would be great if you could incentivize that and incentivize people to kind of, like, to to find the quality, would be really and, like, how do you kind of, like, allow that to you know, how, what systems do you have to kind of encourage that quality? Mitch. I and I don't know the the answer to that. Hey.
[Bryan Cantrill] [01:15:12] How do we get Tom up on stage? I need to Tom's Tom's here. Yeah. Tom is I know has has definitely had some ATC back in the day. Tom, how are you?
[Tom Lyon] [01:15:23] I am good. I I wanted to steer you back towards Usenix history.
[Bryan Cantrill] [01:15:29] Absolutely. Yeah. Yeah. Do
[Tom Lyon] [01:15:30] it. Mostly so I can brag about things. But, know, Usenix ATC was just the rename of the main Usenix conference when they started having more conferences. And UNIX itself was an outgrowth of the UNIX users group, which started in 1975. And I missed the first meeting, but I went to the second meeting of the UNIX users group.
[Bryan Cantrill] [01:15:56] Oh, wow. And so the Unix different. It'd be and so that is what that that's what kind of begat Usenix. Right, Tom? That's when Usenix grew up.
[Bryan Cantrill] [01:16:05] And, I mean, am I wrong to lionize some of those the the I mean, I just look look at
[Tom Lyon] [01:16:11] those
[Bryan Cantrill] [01:16:11] Usenix proceedings from the eighties and nineties. You're just like, it's like Renaissance era Florence. It just feels
[Tom Lyon] [01:16:20] Yeah. Well well, yeah, a couple of things. The sense of urgency was there for the practitioners to connect with other practitioners.
[Bryan Cantrill] [01:16:32] Interesting.
[Tom Lyon] [01:16:33] Because the Unix community, we were like the rebel alliance, Right? It was not not how things were done. And, it was a fantastic community. So a couple couple of hundred people, you know, changing the world. It was great stuff.
[Bryan Cantrill] [01:16:52] Well, and you also it's like it's again, it's kinda hard to convey how distant that world is where it's like they don't really have like, they can't hop on a Zoom call together. Right? I mean, they like, this is the way they don't have other ways of actually connecting.
[Tom Lyon] [01:17:08] Right. Yeah, and so it was, yeah, if you were lucky you were on Usenet and you could send email, but it's hard to talk to lots of people at once that way. And just the social aspect of things and keeping track of people and moving around between companies and yada yada yada.
[Bryan Cantrill] [01:17:26] So, Tom, did you I mean, having been to those, just kind of been through that extraordinary time, I mean, how did did you feel kind of bittersweet about this announcement? Or are you kind of like, hey, I think it's like time to to wrap this up? I
[Tom Lyon] [01:17:42] had kind of given up on the conference aspects of Usenex. Because, again, like you said, it's all gone academic. And that was happening starting in the early '90s, I think. And actually, somewhere I saw a rant by Clem Cole talking about his experiences on the Usenix board and how it was being dragged towards academia. And he really wanted to keep it in practitioner land.
[Bryan Cantrill] [01:18:13] Where would I find that rant? That rant, I would like to inject in my veins attack.
[Tom Lyon] [01:18:19] It might it might be on the Unix heritage mailing list.
[Bryan Cantrill] [01:18:23] Oh, there we go. Doubt it truly doubt at the home, Adam. Have you been on the Unix heritage mailing list? This is where No. This is where it we know this it is it's good stuff.
[Bryan Cantrill] [01:18:32] Nice. Yeah. If you really want people to get off your lawn, that's the place to go. At some point, Adam and I are gonna come to the episode from your house where we're gonna go through the Recall from Books on the Box episode. But, yeah, I would love to see some of those old artifacts.
[Bryan Cantrill] [01:18:49] And and so, Tom, when was the last kind of use did you stop going then in the kind of the nineties? Is that when you
[Tom Lyon] [01:18:58] Yeah. It was pretty spotty. Even kind of late '80s, I got kind of too busy to keep going all the time. The last one I went to, though, was 2019, where they were having an Associated fiftieth anniversary of Unix meeting. And that was in Seattle, and they had the meeting at the Living Computer Museum with the creation of the PDP-seven Unix version zero.
[Tom Lyon] [01:19:28] So that was all very cool.
[Bryan Cantrill] [01:19:31] And the living computer museum is struggling to the living part of the computer museum is a bit of a struggle at the moment, isn't it? I think it like, did it
[Tom Lyon] [01:19:39] really repeat that? It's gone. They they closed it down. They auctioned off the machines. The the remaining outposts are these SDF guys who took a handful of the machines and have them running.
[Tom Lyon] [01:19:56] Anyway, I did have a couple of papers at Usenex back in the day. And 1985, I think, was all the chips that fit, which is a good rant about how screwed up hardware was.
[Bryan Cantrill] [01:20:11] All the chips that fit. Okay. Okay, we'll have to go find that one.
[Tom Lyon] [01:20:17] Yeah, it was kind of a long, steady slide to pure academia. And boy, it really pissed me off that the academics pursue these completely meaningless goals. And sometimes they're funded by the industry to pursue those meaningless goals. And I'm I'm pointing my finger at Intel and and persistent memory. Oh, the the I got so so sick of saying persistent memory papers.
[Bryan Cantrill] [01:20:50] Is I Adam, we need to have a chime when we reference previous episodes. I really love that, you know, this is what Adam does in the change log where they have a chime whenever they make a Silicon Valley reference. We need a chime that we can ring with, now Tom referencing our Optide episode where, Tom said that it was a funeral for a goldfish, which I still I still chuckle at. I feel that, yeah, I I Optane, there was that era when it was definitely, over published as as one might say.
[Tom Lyon] [01:21:23] It's still it's still it's still going. People are still publishing stuff about persistent memory. It's
[Bryan Cantrill] [01:21:28] like, why?
[Tom Lyon] [01:21:32] Academics just get totally disconnected from the state of the world.
[Bryan Cantrill] [01:21:37] Yeah. It'd be nice to get them kind of reconnected. Oh, yeah, Adam, you got the excellent. Yeah. Look at that.
[Bryan Cantrill] [01:21:47] I the you know, a Tom, there's a section called unholy wars in here. That's pretty great. Alright. I'm gonna have to go go read this. This looks great.
[Bryan Cantrill] [01:21:56] Usenix back in the day. Well yes, sir Tom. Go ahead.
[Tom Lyon] [01:22:04] I I forgot what else I was gonna rant about, but it was it was a it was a fantastic community back in the eighties.
[Bryan Cantrill] [01:22:16] Yeah. And I I I did it felt like there was one Adam, this is being discussed on Hacker News. Someone was like, you know, ATC was not even a prestigious conference, like OSDI or Sauce P. And I'm like, yeah. You academics killed it for nothing then?
[Bryan Cantrill] [01:22:31] I mean, like, you you the the you know, there's always the, so that was a little, I think it is it's unfortunate that we ended up in this this phenomenon where this conference became popular with practitioners, attracted a lot of people, a lot of people attracted the academics, and the academics then drove away the people that were going there. That's bluntly kind of what happened. And then and then it was crashing on Ostie's couch for a while, and then Ostie told her, you can't stay here. R I p h e c. Well, Adam, we're always gonna have 02/2004.
[Bryan Cantrill] [01:23:09] That's right. And and whatever beat us out for best paper, which I've obviously blotted from my from from my memory. Yeah. The, I need to go remind myself of that so I can harbor that resentment for sure. I really I really lost track of that.
[Bryan Cantrill] [01:23:27] Really, I need to do like a where are they now episode with whatever beat us out for, for best for for best paper. That would be
[Adam Leventhal] [01:23:34] a great retrospective conference. That that might look really silly.
[Bryan Cantrill] [01:23:39] That would be interesting. I well, and I do think that, like, I do think that, like, more I mean, my favorite conference, think we talked here before, but, like, history of programming languages is a great conference because people have to talk about systems that have been deployed for over a decade. And I think that that's like, more of that stuff, I think, is is really great. Yeah. So well, our IP is next ATC.
[Bryan Cantrill] [01:24:04] We will we we got the opportunity to chase Dennis Ritchie into a bathroom.
[Adam Leventhal] [01:24:10] And We'll always have that.
[Bryan Cantrill] [01:24:11] We'll always have that. And and we didn't we didn't we didn't actually stake you out. We let you leave. Alright. Well, again, apologies for all my reverb at them, but, thanks for Tom, thank you so much for joining us.
[Bryan Cantrill] [01:24:24] We as as we reminisce about ATC. And, yeah, we'll we'll see folks next time.