[Speaker 1] [00:00] Bill, thanks for the the the the segue. So, Adam and I were chatting this morning. We're like, hey. What should we talk about in the space today? And, like, I don't know.
[Speaker 1] [00:07] Kinda what's in the news and headed over to Hacker News. And I'm like, that's strange. Like, why is there a seagate just, like, skew in as a hacker news story? And, Adam, did you know about this Wikipedia page? I'm I'm I don't think I did.
[Speaker 2] [00:20] No. The to totally news to me, and it's always one of those funny ones when it's just, like, a bare Wikipedia page on Hacker News, so I'll I'll also pick my end.
[Speaker 1] [00:28] Right. Which I actually like. I I mean, I think it's because you know, it's like, okay. This thing is so interesting that we're just gonna drop it as a noun. Like, there's no headline.
[Speaker 1] [00:35] This is just a thing.
[Speaker 2] [00:37] And That's right. This this fact that is unknown needs to be known. Yes. Excellent.
[Speaker 1] [00:42] And so this is the the the, s t 3,000 d m zero zero one. This is what what we knew is the 72100 dot 10. We actually never we use the successor to this drive, the 72100.11, which, code name Moose, was an absolute disaster for us, and I would definitely wanna tell our stories. I wanna I'm hoping other people will tell their stories as well. So if you've if you've had stories with this very, very bad class of drives because, Adam, the one thing I learned so that I mean, among other things, first of all, this is a drive that has a class action suit section in the Wikipedia page entry.
[Speaker 1] [01:22] How great is that?
[Speaker 2] [01:23] I mean, you it gotta be a unique or or very small number. Interesting to know the stats on that.
[Speaker 1] [01:29] They should know the stats. And I feel like it's it should be every company and product's aspiration to avoid the class action section of the just to have a Wikipedia page entry that does have a class action section. The did you go through some of the firmware bugs that this thing had? I don't know if
[Speaker 2] [01:45] Yeah. I I looked into some of them. Yeah.
[Speaker 1] [01:47] We did not see the worst ones is what I can't believe. I mean, so the and I I Adam, actually, do you wanna give the, the because I I do feel like memory, it can become fuzzy here. We I think we should tell the story that we had with our drives, and then we can use that as a segue.
[Speaker 2] [02:05] You know, I think you lived it much more indelibly. You you should do this one.
[Speaker 1] [02:10] Alright. So we were so Adam and I, along with a bunch of other folks, were together at Sun back in the day building a storage product. This is in we started 2006. We shipped in 2,008, and we had several different storage products. One was based on Hitachi drives, h GST.
[Speaker 1] [02:28] And this is all gonna get confusing because h GST and Western Digital later merged and took the name Western Digital. Because I know that Rick Alither, I know, has got some WD stories that I wanna get to too, and you have to figure out if that's the WD post HGST merger, pre HST merger. But we were using Seagate tribes in one product and HGST tribes in another product. And the, I mean, Adam, you obviously remember the firmware rev.
[Speaker 2] [02:54] You know what? I'm embarrassed that I don't have that off of the table.
[Speaker 1] [02:57] Are you serious? How many years did the therapy worked? Like, you
[Speaker 2] [03:00] I know. I know. I know that you still have the tattoo.
[Speaker 1] [03:03] I can't forget it. I like, so s u zero d is the is the the the drive firmware rev that that so this thing damn near ruin our lives. So what would happen, and this happened happened with a couple of customers, they'd buy our product and it would be great. And they go, this is great, and it seems great. And so they put more and more load on it.
[Speaker 1] [03:25] And then sadness would start. And there'll be, like, a first, like, raindrop. And then you'll be, like, 4 more raindrops, and then it was all fucking hailstones as the product just, like, came to its knees. And in particular, what would happen is the we started seeing these outliers, latency outliers. It's, like, 560 millisecond latency outliers, which is like it's spinning media.
[Speaker 1] [03:49] These are 700 RPM drives, but, like, that's a long ass time. That's fucking half a second. And what you would see is, like, one drive would start seeing them, and then another drive would start seeing them, and then 3 more drives would start seeing them. And do you remember MIT Broad was a customer? Adam, did you ever deal with them?
[Speaker 2] [04:06] Yes. Yes. I remember the Broad. Yeah.
[Speaker 1] [04:08] Yeah. So the I mean, the admin from MIT Broad was crying on the phone with me. Like, he and I were both crying. Like, this is is clear. Like, this is like I but but but he was, like, actually crying.
[Speaker 1] [04:18] And he had been crying maybe a bit strong, but I don't think it was too strong. He said in a way that barely had control of his emotions. And, again, I not had control of my own emotions, so this is all very reasonable. It's a reflection on on on Seagate, not on him. He's like, I just want the system to be back to what it was.
[Speaker 1] [04:35] And I'm like, that's what we all want. We all want that. And what was what was happening, we were getting a huge runaround from Seagate, and they're being very cagey. And what we understood to be happening but I would love if anyone has got kind supporting detail about this, I would love it because the firmware is all proprietary, and it's very hard to reason about. But according to to what we received from them, there was a firmware bug whereby the head would be misprogrammed due to a polarity error.
[Speaker 1] [05:05] And instead of being programmed to decelerate at high LBAs, it would be programmed to accelerate at high LBAs, which would destroy the drive if it allowed it to do that. So the drive would actually reset itself. And what we were seeing, those 560 millisecond outliers, was the time it took for the drive to
[Speaker 2] [05:29] sometimes I I I feel like some of this was like in a dream. So I'm not sure if I remember this correctly, but the one of the reasons we tried to see this pathology in our lab, and as I recall, one of the reasons we didn't see this was that in well climate controlled labs, you would encounter this problem because it had to do with the ambient temperature. Whereas our lab at FishWorks averaged around, like 95 to a 105 degrees as I recall. And so in this, like, super baking hot lab, we, like, wouldn't encounter this pathology.
[Speaker 1] [06:03] We were left like a sit. I don't know. Is that I I mean, I definitely I'm not sure if I ever knew that detail if that were the case. I I mean, honestly, we were so what we knew from Seagate is that upgrading from SU 0D to SU 0E was gonna solve this problem, and it did. And at that point, I think I was just that at that point, the desire to understand this problem ended, and the desire to forget it, began.
[Speaker 2] [06:30] And and now was this also the one that would cause the g list to to to grow incorrectly, or was that am I conflating firmware bugs?
[Speaker 1] [06:39] That so this is where when I was going through all the firmware bugs on on this piece of garbage, this is where I realized, like, man, there were a lot I mean, of course of course, there were a lot of firmware bugs in this thing. And so, no, that I think is a second disjoint firmware bug, I believe.
[Speaker 2] [06:54] Okay. Okay. But because remember, we we would see problems like this where these drives would, incorrectly report sectors as bad, and then the GLIST would grow and grow and incur nasty performance pathologies. And then all of a sudden start, reporting the smart, you know, predict fail, and we'd get these drives back in hordes.
[Speaker 1] [07:15] Well, in the, the right and there were apparently also firmware bugs where I mean, again, like, so if you go to the Wikipedia page on Seagate Barracuda, not on the SKU I mentioned, but the the Seagate Barracuda on both the both the the 7200 dot 10 and 7200 dot 11 entries have got extensive firmware bug descriptions. And I feel that you mean, you should take a look at that, Adam, because it like, that, apparently, there was a bug, by the way, where this thing could forget where it's effectively metadata was on the spindle, and the drive would just never boot again. Wow. It's alright. So with that, those are our stories.
[Speaker 1] [08:00] We upgraded this thing from s u 0 d to s u 0 e. Those problems went away. There were a bunch of other problems that we had. And then before I kinda throw it over to others for their for their stories, the other thing I would add is Seagate themselves were a giant you want it to work. Like, like, we want it to work.
[Speaker 1] [08:29] You want it to work. We all want it to work.
[Speaker 2] [08:31] You feel so strongly that we should record that.
[Speaker 1] [08:33] Yes. Yeah. But, no, I do feel that, like, when when a customer is, like, really, like, abusing you because the thing doesn't work, a part of you has to be, like, you're abusing me because you want this to work, and I want this to work too. And this might not be the way I would conduct myself, but I have to forgive you for it. Right?
[Speaker 1] [08:48] I mean, I There's
[Speaker 2] [08:48] a lot there's a lot of empathy there, but that's great. Yeah.
[Speaker 1] [08:51] That year was a tough fucking year. So we had, a bunch of different firmware problems. And so you recall we had the, the SSRD problems. Very We had and I can't believe you if you've forgotten, the the, the expander SaaS expanders had the 3 r 20 problem. The the the do you remember what we call that one?
[Speaker 1] [09:08] A blue light special. Oh,
[Speaker 2] [09:10] yeah. This is where the the lanes would, like, go out to lunch. Right? Like
[Speaker 1] [09:14] That one, there was that one too. In this one, the service light would come on, but there was no other problem. Oh, lord. Right. This is why we call this a blue light special.
[Speaker 1] [09:25] So the service light would come on, and then all of humanity would spend its precious resources trying to figure out what was wrong with the system. As it turns out, what was wrong with the system was that the service light was on. I mean, it was very it was very, like, meta in some ways. So what you actually needed to do was reseed it. If you reseed it, the service light would go out, and then everything would be fine.
[Speaker 1] [09:42] Oh, that's right, man. That and then we upgraded the 3 r 22 to get out of that one. That was on the SaaS expander. But then we had the the LSI.
[Speaker 2] [09:49] The the LSI's HBA. That's what I was thinking.
[Speaker 1] [09:52] Right. The HBA, the PHYLOCK problem.
[Speaker 2] [09:54] Yeah. Fine lock. Right.
[Speaker 1] [09:55] Where the one where a 5 would lock up and then be like, I'm just done. Like, I've locked, like, nothing you can ever talk to me again. And you
[Speaker 2] [10:01] had and you had 4
[Speaker 1] [10:03] of them.
[Speaker 2] [10:03] You had 4 of them. And and and, like, one would go, and you'd lose 25% of your bandwidth. Right. And then 2 would go, and you'd be halfway. And then Right.
[Speaker 2] [10:09] This year or later, they'd all they'd all be gone. Right. And there's no recovery.
[Speaker 1] [10:13] That's right. And it turns out losing that last file is particularly painful. As with this is the you I mean, Adam, we've talked about the title of your forthcoming best selling book, from 1 to 0.
[Speaker 2] [10:23] That's right.
[Speaker 1] [10:23] This is I feel this is another chapter of from 1 to 0 because That's right. From 1 to 0 for the, for those who don't know, Adam is not necessarily a fan. I think it's fair to say.
[Speaker 2] [10:34] Yeah. It's fair. We can record that. Yeah. Of of of 0 to 1 Peter Thiel's, like, how to book on on, called Cargo Cultism.
[Speaker 2] [10:44] And
[Speaker 1] [10:48] I like the Josh. I need some stuff to go after. I was gonna make a comment, but I couldn't. Well. Okay.
[Speaker 1] [10:55] It didn't am I making up the fact that you like interviewed with Peter Teal or something.
[Speaker 2] [11:00] No. You're that that part you're making up but Peter Teal in his book and now we're wandering far field, but we Peter says the way he interviews people is by asking something that they believe that other people don't generally believe, which I think would be an entertaining interview question. But I'm not sure any of the results, like, would correlate with them doing a good job.
[Speaker 1] [11:21] It is a weird signal.
[Speaker 3] [11:23] I got it.
[Speaker 2] [11:23] It's weird signal. Right? And and, and, and so I thought that was a terrible interview question. And someone asked me that as an interview question. And I said, well, a lot of people think 0 to 1 is a good book.
[Speaker 2] [11:37] And I don't think it's for a good book at all. And that was not the right answer to that interview.
[Speaker 1] [11:43] That is awesome. That's an email. How long have you been sitting on that one?
[Speaker 2] [11:48] Actually, like I I never thought it would come up. But then because I'm a because I'm a good New Englander, I tried to pull up from that nosedive of that that I'd put this in. And I said, oh, well, what's your answer to that question? And the person with whom I was interviewing said, I've never thought about it. And at which point at which point, obviously, I should have left, but I I stayed.
[Speaker 1] [12:10] Okay. So I've got a lot of follow-up questions. 1, have you ever used the phrase good New Englander in conversation? Have you been using that for years and I've just missed it? I've never heard you say good New Englander.
[Speaker 1] [12:18] I mean
[Speaker 2] [12:18] I mean, like, you know, like, you know, don't like, we don't hug. We're not hugging people. You know, there there are a lot of characteristics of of New Englanders. I don't Listen.
[Speaker 4] [12:28] The guy's the guy's a Red Sox fan. Alright? That's all you need to know.
[Speaker 1] [12:32] Yeah. Yeah. Yeah. It is. It is.
[Speaker 1] [12:35] In fact, the guy is such a Red Sox fan. I know we're gonna be proud of the field. We're gonna get back to Seagate. I promise. He is such a Red Sox fan that Adam and I were together for his for an historic game.
[Speaker 1] [12:45] Oh, great, beautiful, delicious game. Sean and I as no hitter against the Red Sox. No. Dan escorted us in. No.
[Speaker 1] [12:53] This is, dude, this is speaks to what a Red Sox when you are. We are you had never seen a no hitter in person.
[Speaker 2] [12:59] Yeah.
[Speaker 1] [13:00] This is the first no hitter you've ever seen in person. It is there we are in the 9th inning, and there are 2 outs. Yep. And I asked you, does any part of you want to see a no hitter? And you're like, no part of me.
[Speaker 1] [13:13] I wanna see a base hit
[Speaker 2] [13:13] right now.
[Speaker 4] [13:14] I I I I remember the ball doesn't hit the wicket.
[Speaker 1] [13:17] That's that's why the ball doesn't hit the wicket. And and what did the Adam wanted the wicket keeper to to score a try.
[Speaker 2] [13:22] And and, I mean and you were so excited that your hand you you couldn't videotape because your hand was shaking. And I remember Hanley Ramirez was the last at bat and I I said, knock it out of the park, Hanley. And you turned to me and explained that I was a terrible person.
[Speaker 1] [13:37] I I felt like no explanation was really needed in that situation. Absolutely. That's like obvious self evident that we are in Oakland watching a no header. Alright. That's fair.
[Speaker 1] [13:44] Anyway, we do we do right.
[Speaker 2] [13:46] And and they completed the no header.
[Speaker 1] [13:47] But yes. Back to Seagate as a customer though. Hopping the stack up. So Seagate is a customer and they are this thing is not working for them. And they are furious, and they're, like, like, furious.
[Speaker 1] [14:01] They're furious, and, like, they're been kind of tough to deal with, tough customers. So and I am thinking, please, god, let them be seeing the s u 0 v are so upset about is their own company's problem. I'm like but, of course, there that that was not to be in the they were saying FileLock. So it's like, oh, come on. Can't I
[Speaker 2] [14:29] That's right.
[Speaker 1] [14:29] I've I've only wished the s u 0 d pathologies on one customer in that direction.
[Speaker 2] [14:34] If only LSI had been seeing the same problem. There was some sort some, like, gift of the badge eye kind of
[Speaker 1] [14:39] That's right. That's right. So those were our experiences with that thing. We we did notice that when we saw so many problems, because there was the spurgeon issue, which I think I wonder if that was the issue you were referring to in terms of temp. Maybe the the the LBA issue was temp related to
[Speaker 2] [14:54] I I thought I thought the LBA was I thought that the seagate issue was related to temperature because that's what was tell the firmware was making a decision about the fly height in part based on the ambient temperature.
[Speaker 1] [15:05] That would make sense. Yeah. No. No. That makes sense.
[Speaker 1] [15:07] I just don't think I ever got that detail.
[Speaker 2] [15:09] And again, I think part yeah. Again, I don't remember how hot our lab was at FishWorks. One of my one of my big interviewing mistakes is I had some interns come in to make some ethernet cables and I parked them in the lab not realizing it. It was a 110 degrees in the lab that day. And the fact that any of them they were their their fingers were sweating.
[Speaker 2] [15:29] It was it was the worst interview most abusive interview I've ever given by accident.
[Speaker 1] [15:34] And it should be said that these were high scorers who Yeah. These I mean, these were these were children. This is child abuse. I mean, these were children. This is child abuse.
[Speaker 4] [15:43] Violate some sort of child labor law?
[Speaker 1] [15:45] Absolutely. Without question. Oh, man.
[Speaker 4] [15:50] It was, like, 7 years ago or whatever. So no trouble. That's
[Speaker 1] [15:55] you know. That's there
[Speaker 4] [15:55] you go.
[Speaker 1] [15:57] If you're listening now, like, lawyer up, kid. It's not too late. It's you you know, you may be in your mid thirties, but you can That's
[Speaker 2] [16:04] right. I'm I'm I'm like, LinkedIn buddies with those guys still. So
[Speaker 1] [16:08] I they they were great. Character. It definitely they were I I actually, I really liked both of those 2. They and they endured a lot. Yeah.
[Speaker 1] [16:17] Yeah. Alright. So I would like to hear I think because I know other people have experiences with this c I actually not only do I well, I should say I now know. I mean, I think it's like watching that hacker news. We didn't need those comments on there.
[Speaker 2] [16:30] Get crazy.
[Speaker 1] [16:31] But it also felt like it felt very vindicating. And and hold on. I'm trying to get oh, Bill. Yeah. There you are.
[Speaker 1] [16:37] Bill, you just asked to be a speaker. Are you do you have some
[Speaker 5] [16:42] Yes. I worked in the federal space dealing with that particular variant of Seagate Drive I had a lab with 50 HP Z620 workstations that we had fully pimped out with 192 gigs of RAM, which was sweet. We had the OS on a solid state drive, but for bulk storage of local data we had 2 of those 2 of those c git drives in each machine in RAID 1.
[Speaker 1] [17:14] Uh-oh.
[Speaker 5] [17:15] And that was the longest, you know, you know, they can't all possibly, you know, we can't lose a third of the in the 24 hour period, can we? Oh, no. Oh, wait. Oh, what? Yeah.
[Speaker 5] [17:31] But it was all local transient storage. So all the gold all the gold reference copies of the data were stored on a tape robot, which has its own set of problems, which yeah. But yeah. No. That's my single longest shift as a government employee, over 2 days.
[Speaker 5] [17:51] It was 15 and a half hours each day, me and one other person.
[Speaker 1] [17:57] And were you trying to reconstruct? I mean, it we it was first of all, which pathology were you seeing the one of these firmer pathologies? What what what what were you seeing?
[Speaker 5] [18:07] We were doubt that far down the rabbit hole. We were just seeing we we went from, oh, that's weird. Why is it taking so long to access a drive that's in the kit? Why is this why is it lying about block status? What it I mean I didn't really have an adjective to describe it until somebody introduced me to James Mickens.
[Speaker 5] [18:30] So myself and myself and the lieutenant colonel who were swapping drives out for, Western Digital we referred to it as the McKinsey of Dystopia.
[Speaker 1] [18:43] Yeah.
[Speaker 5] [18:44] So but, yeah, that was that was fun. It was and then the tape robot started having problems the fall oh, the following month, but I don't work there anymore. It's all better now.
[Speaker 4] [18:57] You have a lieutenant colonel swapping out hard drives. You've got some real serious problems.
[Speaker 1] [19:01] Yeah. That's what you've got. Things have not gone according to plan. If lieutenant colonel's in there solving drives. I think is that fair to say, Dan?
[Speaker 5] [19:09] Oh oh, yeah.
[Speaker 2] [19:09] Yeah. Yeah. I mean,
[Speaker 4] [19:12] If that had happened in the Marine Corps, like it would have been, I mean, that's the apocalypse right there.
[Speaker 1] [19:18] Right. Exactly.
[Speaker 6] [19:22] Moose was slightly before I ran Google's hard drive team. So, I I only heard about the after effects of it, but it definitely was one of those, things where we learned a lot about how hard drive vendors manage their firmware development. Specifically things like they don't use source control.
[Speaker 1] [19:47] Yeah. This is weird. Like, is there a WTF emoji that I can, like, launch? I mean, this is just amazing to me that and so, Rick, how did you have insight? So I feel like we never got that insight even though we were a huge customer of Seagate.
[Speaker 1] [20:00] Like, we did not have the throwaway to get that kind of insight.
[Speaker 6] [20:03] Well, you weren't that big of a customer. Yeah.
[Speaker 1] [20:05] Fair enough. Right. Exactly. There you go. That's it.
[Speaker 1] [20:07] That's what they kept telling us.
[Speaker 6] [20:08] When you're a big enough customer for hard drive vendors where you're you're ordering which is its own complete set of disasters. Because the mainline firmware that ships to the the commercial box units or even to the OEMs for, you know, system integration, the bug fixes that go into that train, someone has to manually put them into your train.
[Speaker 1] [20:43] That doesn't sound error prone at all. Yeah.
[Speaker 6] [20:47] So, you know, there there were many issues. That's how we figured out how to deploy hard drive firmware at scale. And, yeah, the the Western Digital Sparta was the one that I spent a lot more time on. So it was a 2 terabyte from Western Digital. And that drive, the the short version of the story is they had copied a previous drive, design specs.
[Speaker 6] [21:14] They changed the fly height to be closer because they needed to to increase the the aerial density. They did not realize that the error on the flight height was expressed to the percentage, and they did not change the percentage when they reduced the
[Speaker 1] [21:31] fly height. Knows.
[Speaker 6] [21:33] So the drive was built so that the height the fly height would never be able to be within a safe margin, and it was basically during rights impacting imperfections on the disk. So it was a very early case where, you know, the the number of hours of consecutive writes or the numbers of, amount of data written was a good indicator of how quickly the drive was going to die. So that's when I got to see things like scanning electron microscope images of drive heads where they had a crater in the front of them. And, yeah, figuring out, is it even possible to fix this with the firmware bug? And how do you run a screen?
[Speaker 6] [22:18] Because now you actually have to deploy firmware to these drives that let you run a test that you can do to figure out how many drives are even affected. And and at Google scale, that that's all quite a big challenge.
[Speaker 2] [22:31] Wow. Hey, Rick. When you're making custom firmware updates in your, you know, mega warehouse disk, what kinds of functionality are you are you sneaking in there?
[Speaker 6] [22:42] A lot oftentimes, people are just asking for pretty basic things like adjusting the number of read, retries, because you may not want the drive to be trying really hard if you're running a cluster file system that has replicas elsewhere. You actually want it to stop early.
[Speaker 2] [22:56] Fail fast. Yeah. For sure. Makes sense.
[Speaker 6] [22:58] There's other tweaks to, like, you know, scheduling behaviors. Do you want background scrubbing to how intensive do you want that to be? You know, fairly benign things. But it's enough that if they chain tweak those things, you end up with your own fork of the firmware and then good you know, you have to stay on top of what's happening everywhere to make sure that your firmware builds get appropriate fixes.
[Speaker 2] [23:21] Right. Gotcha.
[Speaker 1] [23:22] And is this so WD's Sparta, is this is this an HDST drive or is this a WD drive?
[Speaker 6] [23:28] Yeah. This is pre merger.
[Speaker 1] [23:30] Right. Okay. So this is on the WD side, not the HDST side.
[Speaker 4] [23:33] In fact, the merger,
[Speaker 6] [23:34] I think, happened not too soon after they had finished all of the Sparta mop up.
[Speaker 1] [23:41] Yeah. Interesting. Because I I I was with a I mean, it is amazing the fly height. I mean, you talk about the you know, the fly height is so important to these things from just reliability and performance and so on. And I know that I've said this before, but I just kinda found this number mind bending when the we were with the VP of quality for HST, and he was asking us a bunch of questions around temp because apparently, temp really affects fly height.
[Speaker 1] [24:07] And or rather, temp affects the performance of the drives. And we were talking about fly height, and the, Adam, do you know what the did we talk about fly height during a write for a drive?
[Speaker 2] [24:18] Oh, I all all I know is I need to take my best guess and then, like, divide it by a factor of a 1,000.
[Speaker 1] [24:23] Yeah. That's basically it. I mean, my guess was gonna be I think, like, the tip I a reasonable guess on this, I'm sure, would have been my guess. Would have been, like, I don't know. Like, like, a micron seems small.
[Speaker 1] [24:33] Like, is it a micron? And it is, the fly height during a write is 0.8 nanometers. And I fell out of my chair. And I said, do you mean 800 picometers? And he's like, yeah.
[Speaker 1] [24:50] I guess I do. I never really thought about that way. But, yeah, 800 picometers. Yeah. That is what it is.
[Speaker 1] [24:54] It's 800 picometers. It's like, okay. If I had to deal in picometers, like, I would make I would inflict picometers on everybody. I'd be using picometers all the time. And I saw that brick.
[Speaker 1] [25:04] Those spaces may have dropped dropped brick, but, the yeah. That is that is wild.
[Speaker 2] [25:12] Astounding. Yeah.
[Speaker 1] [25:14] And just in terms of how sophisticated these things are mechanically, I mean, it's easy to bag on them. Although I although that said, I feel like I spent too long apologizing for Seagate's firmware because of the the endemic difficulty of the problem. And then you warned me think that they're not using source control and all this other stuff. Now this feels a lot less sympathetic. This is a hard problem.
[Speaker 2] [25:35] Right. You don't need to create additional obstacles here.
[Speaker 1] [25:38] You don't. And, I mean, I think in this is where I feel I mean, I don't know. I I feel that that kind of whole experience and not just s u 0 d, the Seagate experience, but the Seagate experience, the LSI experience, the the SaaS expander, the Quanta experience, the I effectively every piece of firmware on that box really failed us. I feel it really radicalized me with respect to the need for open source firmware. Because I do feel that, like, a lot of these problems would be at least making them visible to us would have made a big
[Speaker 2] [26:20] and then to be able to to actually correlate the phenomena you're seeing with the software that as you can understand it is so important especially in these production environments. I'm totally with you.
[Speaker 1] [26:32] Wait, no. You're asking yourself like, am I crazy? By the way, the vendor is helping you out with their hypothesis, namely like, you're crazy. Right. It's like, oh, okay.
[Speaker 1] [26:41] Right. Right.
[Speaker 2] [26:41] Right. Is everybody except us? Are you kidding me?
[Speaker 1] [26:44] Right. The like, we're not I mean and, like, no one else is seeing that problem is something that I I mean, how often you've heard that from a vendor? Like, we or we've never heard of anyone else having this problem. We've you're the only one who's seeing this.
[Speaker 2] [26:57] But it that I mean, it feels like language from a lawyer.
[Speaker 1] [27:00] I just think
[Speaker 4] [27:00] I think Dell have put that as a low numbered item in one of their support script. Oh, I Like, the cut the the the support technician is just supposed to read that line out regardless of whether it's it's true.
[Speaker 2] [27:12] But that person's not even a Dell employee. That's just off a script from some generic
[Speaker 1] [27:16] call center. Exactly. It's right under dude, you're getting a Dell. We've never heard of that problem before. You're just like, oh, well.
[Speaker 4] [27:22] No no no customer other
[Speaker 2] [27:23] than you is experiencing the problem.
[Speaker 1] [27:25] It's like, really? Okay. But it look it looks like the website's broken.
[Speaker 4] [27:28] Now reboot the computer and update the BIOS and get back to me.
[Speaker 1] [27:33] Tom, I saw you unmute unmuting yourself.
[Speaker 4] [27:37] Oh, you did? Did am I on?
[Speaker 2] [27:39] You are.
[Speaker 4] [27:40] Amazing. I'm I'm on a Twitter beta app, and it's a little sticky. But, yeah, I was gonna say about the custom firmware that Dell and HP do. Yeah. Back back in the day, there were actually reasons for it, but now the main thing is to put their names in the vendor field so that their RAID software can check that you're actually using their own drives.
[Speaker 2] [28:05] Oh, that's great value. I mean, it's
[Speaker 4] [28:06] for which for which they charge a lot more. It's just rent seeking. Sun did this too. Yep. Yep.
[Speaker 1] [28:12] It We we we tried
[Speaker 4] [28:14] to buy we tried to buy a JBOD from some once, and they were like, well, you gotta buy a disc in all 24 slots. Alright. Well, but we've got lots of discs.
[Speaker 1] [28:23] Oh, no. You don't. Can we and
[Speaker 2] [28:26] Not yet. You don't.
[Speaker 5] [28:27] And, yeah.
[Speaker 4] [28:28] I was just like, well, we're not gonna sell you the sleds. How about that? But the sleds are a small piece of plastic. Can we have the sleds please? Like, no, no.
[Speaker 2] [28:36] $1,000,000 each. The sleds
[Speaker 4] [28:38] are the cost of a drive plus 10%. Cause you're annoying. Like Yep. So so there there is the opposite extreme of that, though. We dealt with JBODs a lot at at DriveScale.
[Speaker 4] [28:49] But WD was selling these populated JBODs that were so cheap that people would buy the JBODs, take the drives out, resell the drives, and then sell the empty JBOD on eBay for for, like, $500.
[Speaker 1] [29:02] Yeah. Yes. Basically, we had pretty amazing.
[Speaker 4] [29:05] We had a galactic pile 250 gig spindles that no one was ever gonna use, basically. Because in the end, that was just easier than because we could replace them with 2 terabyte spindles at at a huge a huge decrease in price.
[Speaker 1] [29:20] Tom, when you were at DriveScout, you got you were obviously dealing with a bunch of storage. You must have seen all manner of drive firmware problems.
[Speaker 4] [29:27] Yeah. One one one of my favorites was CGI was that just just to query the smart status. You know? Tell me tell me a few counters. It it was a 200 millisecond overhead.
[Speaker 4] [29:39] Nothing nothing else would happen on the drive.
[Speaker 1] [29:43] And this is like, you're like, what is going on for 200 milliseconds? What are you doing? How many headseeks is it to ask your smart status?
[Speaker 4] [29:51] Yeah. Like, what what could they possibly do?
[Speaker 1] [29:55] Fizzy dumping core. I or yeah. Or maybe, like, or rebooting. I mean, you just, like, not being able to kinda see into what's actually going on. And I think, like, smart is another good example where I mean, smart for those what does the even acronym stand for?
[Speaker 1] [30:09] It's it's sadly, it's an it's it's an acronym, but this is for the giving you drive health statistics that are infamously always 0 because the vendor doesn't want the drive to come back. So, of course, like, the vendor's like, no. No. If I'm telling you I'm gonna sec I'm gonna do it on a hidden mode page. I'm not actually gonna do it in the smart data.
[Speaker 2] [30:27] Yeah. I've got it I've got it up, Brian. Do you wanna guess what smart stands for?
[Speaker 1] [30:33] Does the s stand for smart, first of all?
[Speaker 4] [30:36] It's gotta be it's gotta be simple something. Right?
[Speaker 2] [30:39] So it's self monitoring.
[Speaker 4] [30:40] Oh, cell phone.
[Speaker 1] [30:43] Self monitoring and?
[Speaker 2] [30:47] Analysis and reporting technology. Technology.
[Speaker 1] [30:52] Yeah. That's no. It's right there.
[Speaker 2] [30:54] Bad. Yeah.
[Speaker 1] [30:56] It's bad. It's it's all bad. It's like, one, I think, like and I say this as a company that worked for it. We had a product called, like, smart everything. I think smart is a terrible name.
[Speaker 1] [31:04] I didn't name those products. I think smart is smart just sounds smarmy. Like, don't don't call yourself smart.
[Speaker 4] [31:11] You just didn't foggy to us. I think you're just
[Speaker 1] [31:13] about using disaster by calling yourself smart. Exactly. Don't call yourself smart. And then
[Speaker 4] [31:17] I I I like the products that call themselves dumb. And and the the a d m three a, they act they actually marketed it as a dumb kernel. That's awesome.
[Speaker 1] [31:25] Well, there there you go. That's right. Well, that's it. You know, that it's we call that simple, where I'm coming from. I guess it's simple.
[Speaker 1] [31:31] It's good. We like simple. Simple is definitely good. The when I did you know, Rick made an interesting point, unfortunately, before before I'm gonna assume the Twitter spaces ran out of memory and dropped him. But the, made an interesting point, and I think, Adam, this is true for us as well, that the one upside of having terrible drive firmware is it really requires you to get the firmware upgrade story right.
[Speaker 2] [31:52] And Oh, yeah. Yeah. Yeah.
[Speaker 1] [31:53] Which we definitely did. I mean, we we did spend a lot of time and energy allowing you to upgrade your disk firmware and getting that all correct. And that can all happen, fortunately, without actually, I mean, it it has it can happen while the machine is up, which is which is gratifying.
[Speaker 2] [32:08] Yeah. And and Brian, with regard I'm I'm getting, like, more firmware, like, horror story flashbacks. And call. Tell me if this is like just, I've talked to myself into this. If this is an embedded memory or a real one, but like with the LSI Filoc problem, do I recall correctly that it was insufficient to like reboot the box?
[Speaker 2] [32:28] Because that's that because that HVAC actually stayed powered.
[Speaker 1] [32:31] That's right.
[Speaker 2] [32:32] So the the the per support procedure for that was put down the phone, walk over to the system, yank out the power cables, and put them back in. Am I am I making that up? No.
[Speaker 1] [32:42] I don't think you're making that up. Yeah. No. You're no. You're not making that up.
[Speaker 2] [32:46] Yeah. Because because And make sure
[Speaker 4] [32:47] you wait 30 seconds for the capacitors to drain through.
[Speaker 1] [32:50] Right? That's right. That's
[Speaker 2] [32:51] right. Count to 30. Right. And and and part part of the problem was that an oversight of that system was that, that, like, the the LOM couldn't actually do a full power reset of all those components.
[Speaker 1] [33:05] Yeah. And speaking of the LOM, we were not spared The the the the the most cruelly ironic firmware bug that we actually had on that system, I felt, was an actual Sun firmware bug where the the service processor was a Java program, of course. Because what what else would you write a service processor in? Like, let's make sure we're running it in
[Speaker 2] [33:25] Just just check your stock ticker and write it in that.
[Speaker 1] [33:28] No. Stop. Oh, that's so cutting. God. That's so cutting.
[Speaker 1] [33:34] Oh, man. That's now now just sad. Alright. Yeah. I'm so fine.
[Speaker 1] [33:38] Yeah. Check your stock ticker. Write it in whatever application is reflected in the the where language is like in the stock ticker, in this case, Java. And which is also, again, also, like, fine perhaps, but this thing would do what many job programs would do is it would actually, grow without bounds and get to the point where GC is running all the time and not finding any garbage because the heap is effectively grown without bounds. And then it would somewhat amusingly, the service processor would in this by the now, like, allocations are failing, and it now doesn't know about itself from the CLI.
[Speaker 1] [34:20] So you would say, I wanna reset slash, what? Reset/sys/sp. Right? Something like that. I'm trying to remember exactly.
[Speaker 1] [34:27] Right? And it would tell you, like, no such object, sp. It's like, you are the SP. And we're we're having Who
[Speaker 2] [34:34] do you think I'm talking to?
[Speaker 1] [34:36] Right? We're having a very metaphor like, a very metaphysical kind of a solipsistic conversation here. But, like, simulation? Is none of this real? Yeah.
[Speaker 1] [34:47] Are we all filled with existential thread? Which is that that was very so that was very frustrating. But when that would happen, we would now neglect to control the fans properly. And the fans would
[Speaker 2] [35:01] Well, the other way around, the fans would say, what the fuck happened to the SP? Right. Like like, you know, full full power to the torpedo.
[Speaker 1] [35:10] Full power to the torpedoes, which it feels like a sensical like, best feels like a fail safe kind of thing. It's run the fans full speed. It's like, well, it might be if we didn't have these little Hitachi Bronco case in there that were very vibe sensitive and a chassis that was maybe not really, maybe had some vibe issues.
[Speaker 2] [35:29] That's right. And I, I remember this part, but we we had chosen the processor on these systems to be a little a little cooler and then capped the fan speed at like 80% knowing that that was safe. But this fail safe mechanism blew through that 80% cap to to go at full a 100%.
[Speaker 1] [35:50] Full a 100% and then the drives themselves started getting ridiculous IO latency outliers. So then you you start saying, like, thousands of milliseconds because it's getting what are called non repeated runouts, which where the the the head is the whole chassis is vibing itself to death. So the head is having a very hard time tracking and is constantly having and, you know, interesting point too about just changing the number of retries on a drive where the drive has no other way of telling you, like, I'm in tremendous pain and there are many problems here, and I need attention. So it all it has really is read and write and tell me how you're feeling. And, like, by the way, I can never tell you that I'm feeling sick because otherwise, you'll replace me.
[Speaker 1] [36:30] So I don't want that. So I need to, like I'm always like, by the way, I'm feeling great. And, the on the reads and writes, it's like, I'm just gonna keep trying. Like, I what else am I gonna do? It's like, well, fuck.
[Speaker 1] [36:41] You could, like I don't know. Like Like, the data's here somewhere. The data's here somewhere.
[Speaker 2] [36:46] I'll have it for you in 2 weeks. Like, I
[Speaker 1] [36:48] swear I Totally. Totally. Totally. It's like someone who's made, like, a cascade a I got a payday loan for the Mastercard, and now it's like now they're repoing every it's just like the whole thing's coming
[Speaker 4] [37:05] on Google.
[Speaker 1] [37:05] Like, the ads
[Speaker 4] [37:08] Retry forever failure is also one way in which they've created artificial differentiation between consumer and new line drives. Oh,
[Speaker 1] [37:17] that's right.
[Speaker 4] [37:17] Consumer draws will retry forever, basically, which is not terribly good for a writer writer that could say, well, I look, you know, just fail, and I'll I'll figure it out. Right?
[Speaker 1] [37:26] That's so You know?
[Speaker 4] [37:27] Wrong. So that they they can charge, you know, 80 extra bucks a drive or or or a 150 or something for for slightly better phone.
[Speaker 1] [37:35] Oh, you want me to break out of that loop? That's I mean, I can do it, but it's gonna cost you. But it's not free. It's gonna it's gonna cost you. It's not free for me to do less work.
[Speaker 1] [37:43] You're like, I what what's going on? Right. Why are you yeah. That's brutal.
[Speaker 4] [37:48] This is in line with other, products where the consumer product is cheap and full of features and the professional
[Speaker 1] [38:02] Yeah. We and certainly after I came out of that I don't know, Adam, if you ended up so we, after Sun, you went to Delphonics. We were at Giant.
[Speaker 2] [38:13] Well, I mean, I I when I went out of Sun, I mean, the lesson I learned from that, which was different than the lesson you learned, the lesson I learned was stay the hell away from hardware. I mean, obviously, I've I've unlearned that fast.
[Speaker 4] [38:24] Right. There you go.
[Speaker 1] [38:25] You forgot that lesson. Right? We're trying to remind ourselves.
[Speaker 2] [38:27] That's why I coasted into, like, virtual virtual.
[Speaker 1] [38:31] So you'd well, that's this is not an uncommon lesson that people learn when dealing with hardware. It's like, I never wanna deal with hardware again. Like, this is actually hardware is hard. I mean, it's painful. It's it's awful when these things Well, well, I think in particular at the
[Speaker 2] [38:44] time, you know, people were call it, was accurate, which was it was hard enough for us, Sun, to get the attention of all of these component vendors to to please fix these these, what would have been business ending bugs. And for, like, a insignificant startup to get that good attention would have been untenable. And I think the the world has changed a lot since then.
[Speaker 1] [39:12] Yeah. I know. I think you're right. And I think that the I think also in a world of all closed all closed firmware, all proprietary firmware, it is actually, I mean, this is part of why we need an open firmware ecosystem is to allow for more innovation and and more companies to be able to do things more cheaply because we you could not you're exactly right. That, like, we could not have done it simply because we could not have gotten the attention that we needed.
[Speaker 1] [39:35] I mean, hell, at Oxide, it's hard to get the attention that we we were very good at making a racket, but it is hard to get what what you know, we've got and we've got very little proprietary firmware in the stack. But as Laura can attest, like, the proprietary firmware we do have is making its proprietariness well known,
[Speaker 3] [39:54] unfortunately. So I'm curious with this group of people who've been tortured by hard drives and have tortured them in return. What do you actually want from the hard drive API? Like, do you wanna be able to say on every request, hey, give me a fast read or give me a reliable read or give me a really absolutely try as hard as you can to give me a read read. So I Like, it feels weird to change the firmware on the drive rather than having a different kind of request for that request.
[Speaker 1] [40:24] So in all honesty, and I know this is just very on brand me to say this, I actually want an open ecosystem. I I I want I don't think one size fits all. And I think that different people may want different behavior, and we should have just as we are able to programmatically change our behavior elsewhere in the stack, we should be able to programmatically change our behavior with respect to drive firmware. So
[Speaker 3] [40:47] Software defined hard drive.
[Speaker 1] [40:49] We well, the thing is we already have a software defined hard drive. It is just that it's a proprietary defined hard drive right now. And so we Oh,
[Speaker 4] [40:56] it it all there's a major philosophical thing too, which it all comes from the school. I thought that nothing is ever gonna fail except except in very rare situations as opposed to the networking point of view. It's like, you're lucky if anything works. And and you if you architect the whole stack to be, you
[Speaker 2] [41:14] know, get lucky, then
[Speaker 4] [41:16] things work a lot better.
[Speaker 2] [41:17] Tom, it's it's interesting you say that. And and and, I think the Apple, WDC conference was today. And and I I bring that up because like in 2016 or something they were rolling out their APFS, their new file system from scratch and I went and talked to some of those folks. And to your point, Tom, they actually claimed that they did not see bit errors. That that bit rot was a was like the product of of of of mass hysteria.
[Speaker 4] [41:48] Yeah.
[Speaker 2] [41:49] And, to which I said, well, in with HFS, you're, you know, the fastest monitoring for years, you just wouldn't know because you just have things change, and you'd have no way of identifying that.
[Speaker 1] [42:00] And and Well,
[Speaker 4] [42:00] it makes perfect sense from a company that only sells consumer stuff, but no parity on memory, you know, either. Yeah. Fair enough.
[Speaker 1] [42:07] Yeah. We don't see any memory errors. By the way, we've got no capacity to see memory errors. We have no, like, we actually have no nerve endings there. Like, we I we can't see one thing.
[Speaker 1] [42:15] Like, why what's the problem? It's like, am I is this a Dell support call that I'm logging right now? Like, what's going on?
[Speaker 2] [42:22] Right. You're the only one seeing this problem.
[Speaker 1] [42:23] You're the only one seeing this problem. It's like oh, okay. Sorry. I was asking for, like, your company address. You're the only one asking that question.
[Speaker 1] [42:30] We've never heard that question before. We've never That's right. Yeah. That's I mean, that so that's the kind of the APFS analog. And just in terms of, like, the and, Tom, that's a very good point too about this kind of the storage thinking versus networking thinking.
[Speaker 1] [42:47] Because I feel we saw this too. I feel we were helping to perpetuate this, Adam. I feel like we just we were captain hires in 2,000 6, I feel. Like, we had we were trying to sell highly available, highly reliable storage by pretending that a partition couldn't possibly happen.
[Speaker 2] [43:05] Yeah. Yeah. And I I don't know the degree to which we were pretending with well knowing and or pretending well not knowing.
[Speaker 1] [43:12] Right.
[Speaker 3] [43:13] You can't just go around declaring that the network is the computer.
[Speaker 1] [43:16] That's right. Not unless you're CloudFlare. I yeah. And I think that the, so I think part of the problem is that just as Tom said that the the there's been this, the way you deal with failure. See, the problem I think, is that, like, if a if a packet is dropped, the NIC does not get returned.
[Speaker 1] [43:37] So it is there's there's obviously so much that can fail on the network that that's not necessarily on the component. I think that the drive feels that, like, if I report an error, like, I'm gonna I'm gonna be returned. It's like, well, yes. Probably. But you still need to report the error.
[Speaker 1] [43:50] Doesn't mean that you Well
[Speaker 4] [43:53] and then the the whole ecosystem. So if if if if there's a link error talking to the drive and it gets recorded, everyone goes completely bat shit in saying all the way up to the application. Yeah. As opposed to saying, oh, there was a glitch. Let's try again.
[Speaker 1] [44:07] Right. That's right. I mean and I and, also, I mean, I think there is a degree to which, like, it is actual you know, it's persistent. So if you do have these failure modes, like this crazy firmware failure mode that we didn't see where the drive would lose metadata and never be able to boot again. Yeah.
[Speaker 1] [44:23] You do have these pathologies that arguably much more acute, But still, it's like, oh, man. We can do better than this though. So Aaron, I don't know. Say, how do how is that as an answer to your question?
[Speaker 4] [44:36] Sounds good to me.
[Speaker 1] [44:39] Yeah. I think it well, it sounds good to a lot of people. I mean, I think that, you know, we've obviously got a bunch of kinda core beliefs at at Oxide, but open firmware is is is a pretty deeply held one.
[Speaker 2] [44:48] Yeah. And I I wonder how, you know, behind a lot of the the firmware that we're talking about here is this real complex engineering and science and physics and, that that while complex is often tending towards commoditization. So, you know, one of the questions I have is how we break this idea that firmware is the path to, to greater revenue and margin and, differentiation.
[Speaker 1] [45:17] And also yeah. This is a good point, Adam. And like that firmware is your path to for to preservation of that innovation.
[Speaker 2] [45:24] That's right.
[Speaker 1] [45:24] And it is, like, super tragic, especially when you get into the physics of these drives, which are the and and we are not using rotating media at oxide, not yet anyway, not in our first product. We I presume we will at some point, just because the density advantage is so great. But the I I do you have anything about hammer versus spammer, Adam? Have you have you ramped up on any of this stuff? Or have you been No.
[Speaker 1] [45:46] Yeah. Right. You've been so you the you would love this stuff. Stuff. So, Hammer is heat assisted magnetic recording.
[Speaker 1] [45:53] MAMR is microwave assisted, magnetic recording. And they are effectively so with HAMR, you are super heating for periods of femtoseconds, literally, in extremely small area so you can write higher density bits. And it's, like, crazy interesting. And you're like, wow. How is the physics this, like, off the charts nuts?
[Speaker 1] [46:22] And then you're, like, not using source code control for your firmware. I feel like I mean, it makes me feel bad as a software engineer. Right?
[Speaker 4] [46:31] Yeah. Yeah. I think the trouble is they these companies don't admit that
[Speaker 2] [46:41] I mean, to your point, Tom, that that it you know, this becomes the weak link in so many devices.
[Speaker 4] [46:46] Right. I mean, software is eating the world, and these guys are software companies but they won't admit it.
[Speaker 1] [46:52] Yeah. That's that's interesting actually that you should that you said that because we definitely we've got one colleague in particular who is very he he is fighting the loan fight against the term firmware. It's like firmware is software. Like, do not like, we are it is software. It is a soft it is very low level software, and it is.
[Speaker 1] [47:12] Like, he's not wrong. It is software.
[Speaker 2] [47:14] Well, well, and it's not even necessarily very low level anymore. I mean, look look at like, you we we talked about hard drives, but look at SSDs, which are taking a totally different technology and then pretending to be hard drives out the other side. Right? Masquerading is this interface that made sense for spinning media to a degree and just really doesn't for those. So the complexity of the software in there is enormous.
[Speaker 4] [47:37] And hybrid hybrid storage devices. I mean, how many of these things are running up like a badly patched copy of the Linux kernel? Right. That's my question.
[Speaker 1] [47:47] Right. Right. Exactly. Well, now you see, you run what's really troubling is that you run strings on these binaries that you're getting from the vendor. You're like, why is there a URL in this firmware binary?
[Speaker 1] [47:56] What's going on exactly? Dan, to your question about, like, how much how much unpatched Linux kernels, what have you is are are around your node. It's very troubling. And and and and the point about, like, these SSDs being these very complicated little worlds in there that have got their own tons of their own complexity that we don't have visibility into because it's trying to pretend it's something else. It is there any exactly.
[Speaker 1] [48:20] You know, it is funny. Is that there is speaking of SSDs, the only firmware that did not give us really acute pain I feel like we did not have a Logzilla problem. Am I wrong, Adam?
[Speaker 2] [48:31] Yeah. No. I think that's right with with, STech, which With STech. Acquired by w d or where did they get bought? No.
[Speaker 2] [48:39] Yeah. They went to WD, I think, actually. Yeah.
[Speaker 1] [48:41] But, I mean, the s I mean, are you gonna tell the STechs? The STech story is pretty great.
[Speaker 2] [48:46] So I mean yeah. Go ahead, please.
[Speaker 1] [48:49] Well, you know that that that that so we were dealing so s tech was a company that I mean, Adam was, I dare say, the first person to really look I mean, other people were making this observation at the same time. But, Adam, you were very early on making the observation that Flash could be used in an enterprise storage product.
[Speaker 2] [49:07] Yeah. We we were really at the right place at the right time there. But but because with the advent of the iPhone, the the the economics on Flash changed really, really quickly. I mean, right out from under us, where the point where the early flash drives that we got were, intended for use in, like, helicopters and high vibe and vibrance environments. And then a month later, the the samples we got were they had figured out, like, high performance, flash could be more economical than just shoving a bunch of DRAM in a in a battery into a 3 and a half inch enclosure.
[Speaker 1] [49:40] And we which is what we want to avoid. We wanted to avoid the the battery in particular. We were using flash first and foremost for non volatile store that we could write to quickly. And we found this company called STech that was the leader of the space, really. I mean, they were the pioneer in the space.
[Speaker 2] [49:57] Well, you know, they they bought this company, GnuTech, to buy them way in. Esteq had this whole consumer brand of, like, rebranded s, hard drives and rebranded memory, which later they divested. They bought this company, Ganutech, out of England. So I don't know if you remember this project.
[Speaker 1] [50:13] I've gotten that. Yeah. When you say Ganu Yeah. I'd like to interject for a moment.
[Speaker 2] [50:19] Yeah. Yeah. No.
[Speaker 4] [50:19] That that is not Linux.
[Speaker 1] [50:21] Yeah. Right.
[Speaker 2] [50:22] Right. I don't remember this part, Brian, but the first samples we got of those STEC drives, we couldn't plug in until I had gone down to the coal hardware to get metric screws because they they we they wouldn't the screws we had would not fit into the these components.
[Speaker 1] [50:39] Adam, you'd be happy to know that that googling GNUTECH, STech yields your blog on I I I was trying to corroborate what you were saying, but I'm like, oh, this this person seems to be hey. Wait a minute. It's it's it's passed. I don't know. Wait a minute.
[Speaker 1] [50:54] But so we were, I mean, an early customer for that. So the the the Mark Macchady, one of the these these two brothers that were running the company, the Macchady brothers. And Mark was spending a lot of time with Fish Works.
[Speaker 2] [51:10] Yeah. Yeah. Yeah.
[Speaker 1] [51:10] And you know that I mean, you know how you know that Mark came within a hair's width of going
[Speaker 2] [51:16] jail. I do know that. I do know. I, I followed that with great interest.
[Speaker 1] [51:20] So they, as it turns out, were crooked as all get out in a well, and and actually, Tom, I would I would love to know how classic this scam is. They were stopping the channel. So they were public company. They were stopping the channel, which is where you basically are marking a bunch of sales that you haven't necessarily made because you filled the channel with your product. And but as a but so your sales will go way, way up, and then they'll come way, way down because people now have your product.
[Speaker 1] [51:47] They're not gonna need it for a long time because they they've stockpiled a bunch of it effectively. And I Adam, if memory serves, they were stopping the channel with EMC, I think.
[Speaker 2] [51:54] See, yeah. I think actually, I think one of the problems that they ran into is that, they had sold a bunch to EMC, but EMC was not able to move them quickly enough. And I remember this, but but EMC priced them just ludicrously. These parts that we were selling for 5, 10, $20,000 they were selling for like $100,000 And when we did the math, we determined that they were using, spinning discs to get a price per IOP and then just multiplying that based on what these SSDs could do. So they were they were ludicrously expensive.
[Speaker 2] [52:28] So then they they had bought a bunch of them and then weren't selling them. Communicated this and Esteq was a public company at this point. Communicated to Esteq that they weren't going to be buying anymore for a while. Esteq then, you know, in their in their earnings call, in their in their 10 k or 10 q or whatever, you know, made no mention of this. And, and then some some insiders traded on on that non public information.
[Speaker 1] [52:55] Yes. It turns out they sold high. It turns out, like, they had some insider information. Namely, we've stuffed the channels. So we're going to we're just gonna, like, sell it all.
[Speaker 1] [53:02] As it turns out, like, the SEC is, like, this is the SEC is, like, yeah, actually, you're not the first person to think of this crime. This crime is not the master crime that you might think it is. This is actually Right.
[Speaker 2] [53:11] We have a whole name for that one.
[Speaker 1] [53:12] We have a whole name for that one, actually. It's like you're going to jail. But he didn't I feel like he walked on a technicality. I the
[Speaker 2] [53:21] I I I yeah. I think they're they I I think they were able to clear it up somehow, in some like, arrested development type scheme. But I I don't know I don't know the details. But but but kind of pull pulling out of this particular nosedive to your point, yes. I don't think their firmware ever screwed with us the way that other Well,
[Speaker 1] [53:39] this is, like, the irony. It's just, like, is this what we need to do to get, like, correct firmware? You need to go
[Speaker 4] [53:43] to, like,
[Speaker 1] [53:44] crooked people. Like, can we come on, world. Don't make us go I I I do have the I mean, god bless the SCC. I do actually have the full SEC complaint featuring the Zoos IOPS, which is the product that we had that we called Mozilla, very prominently. So it's all it's all a statement of fact on the record.
[Speaker 4] [54:03] I I seem to remember the spec drive. I don't know if it's the same one, but it had no firmware at all. It was an actual hardware device.
[Speaker 2] [54:15] No. You know what? They did have an FPGA on there.
[Speaker 4] [54:18] Okay.
[Speaker 2] [54:18] So I don't know what I don't know how we're gonna wanna classify that as firmware, software, or none of the above. K. But but I do remember that, that that, the FPGA was doing a lot of the work there.
[Speaker 1] [54:30] Oh. And one
[Speaker 2] [54:31] of their the big piece of their milestones was was going to an ASIC version of their product.
[Speaker 1] [54:35] But that
[Speaker 2] [54:35] I mean, again, this is ancient history.
[Speaker 1] [54:37] Yeah. Well, it's But that's actually really interesting, though.
[Speaker 4] [54:39] It's when microprocessors show up that all the trouble starts, I think.
[Speaker 1] [54:44] No. Yeah. That's right. I think that's really interesting that, like, that, actually, the fact that it I did not realize that, Tom. But that makes sense, actually, that we that you because it is FPGAs don't tend to have the same pathologies as firmware.
[Speaker 1] [55:03] And that is really interesting. Yeah. As as you when the microcontroller show up, that's when the trouble starts. That's that's definitely true. Yeah.
[Speaker 1] [55:12] That is, that is sad. I mean, we gotta do better than that though. Right? So I mean so what we need so, Tom, how do we we counter that? I think you're right, that does seem to be a problem.
[Speaker 1] [55:24] Obviously, I think open source is a big part of the answer. What's your take?
[Speaker 4] [55:28] Yeah. I mean, a clearer boundary between hardware and software and admitting that software is never correct. So there has to be a way to for it to improve rapidly. But, managing managing firmware like it's just another hardware component is a disaster.
[Speaker 1] [55:47] That is it. Yeah. Managing I think that think of you gotta think of firmware firmware is software. It is actually not hardware. And thinking of it as a hardware component is the way you end up delivering things on home directories and
[Speaker 4] [55:59] And and software having software is clearly never done, is never correct. It can only get better and but usually gets worse.
[Speaker 1] [56:10] Oh, I thought you're gonna leave us on such an optimistic note, and then that that that kinda that kinda try gotta drag us right back down. Alright. Everyone. Definitely let us know things you wanna talk about, other feedback you might have for us. I know I Adam, I'm I'm continuing to have fun doing this.
[Speaker 1] [56:33] I'm not how how you feel, Tom? Thank you so much for joining us.
[Speaker 2] [56:39] Yeah. Thanks, Tom. Thanks, everyone, who who chimed in with their stories. Really appreciate it.
[Speaker 4] [56:42] Good fun.
[Speaker 1] [56:43] Awesome. And I think we're gonna take, I'm out next week. We may be taking next week off. But, I don't know. Adam, we gotta line it.
[Speaker 1] [56:49] Figure out our summer we'll figure out our summer vacation schedules and and get a a schedule for our Twitter space. But That's right.
[Speaker 2] [56:55] We'll keep you posted, folks.
[Speaker 1] [56:56] Awesome. Thanks, everyone. Take care.
[Speaker 2] [56:58] Thank you.
[Speaker 4] [56:59] Thank you.