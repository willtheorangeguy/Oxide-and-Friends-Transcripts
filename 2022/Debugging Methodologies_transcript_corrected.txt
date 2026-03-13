[Speaker 1] [00:00] So Jordan was asking, can I join the Twitter space? Oh, which, of course, no. Of course not. Of course not. Because that would be a useful feature.
[Speaker 1] [00:09] And I'm like, look. One of my top feature requests is a green room.
[Speaker 2] [00:13] And Jordan apparently is green room not a common term? If no. Oh, gosh. It's the children that are wrong. No.
[Speaker 2] [00:22] Well, still Jordan's like, Jordan, I'm sorry. That must
[Speaker 1] [00:24] have sounded very peculiar. Just someone who never heard me at home.
[Speaker 2] [00:26] So Luke man, you just joined us. Can you hear us?
[Speaker 3] [00:32] Hello? Yeah.
[Speaker 1] [00:33] Hi, Gary. Hey. Alright.
[Speaker 2] [00:35] Luke man, green room. Is this a term that has any meaning for you whatsoever?
[Speaker 3] [00:41] Not at all. No.
[Speaker 4] [00:44] Alright.
[Speaker 1] [00:45] Okay. Well, the yes. The generation is still good.
[Speaker 5] [00:48] I mean, I could infer from context, but I did want to hear you
[Speaker 1] [00:51] explain. So a green room is a room in which one waits to be a performer. The where, it is often backstage. It's got, you know, it's got it's catered in the so that I went I'm like
[Speaker 2] [01:08] What's that thing before, like, late night televisions?
[Speaker 1] [01:11] Yeah. Exactly.
[Speaker 2] [01:12] People stay in the group. Yeah. Everybody knows that. Surely.
[Speaker 1] [01:17] Alright. Well Yeah.
[Speaker 3] [01:18] Surely, we've all been in front
[Speaker 1] [01:19] of Yeah. Exactly.
[Speaker 2] [01:20] It's like when you're on Kimmel. Right? I mean, right, Josh? Yeah. I mean, just the other day, I was on Letterman.
[Speaker 2] [01:26] Right.
[Speaker 1] [01:26] Yeah. But he was hawking his NFT. So don't read too much into that. But so the but where is the origin of the term green room? And you go to the green room Wikipedia page.
[Speaker 1] [01:37] It's like, because the room was frequently painted green. And I'm like, you are not going to leave it at that Wikipedia. Fortunately, that there is an entire section below on possible sources of the term, and it goes back to London's Black Friars Theatre 1599. So this is an old term. Anyway, if Wikipedia is to be believed, which it
[Speaker 2] [02:01] sure. Let's do that. Let's do that. Let's experiment. Yeah.
[Speaker 1] [02:04] Anyway, they don't have the feature. So you're welcome to the green room, everybody. It's the same thing as being on stage. So we just kind of pour out. But Jordan and Luke, thank you so much for, for joining us.
[Speaker 1] [02:18] And so, Jordan, I wanna kick this off with, your, this NVMe bug that you found. We're talking about debugging methodology today, and, the in particular, Jordan had this terrific analysis of a problem. And then I when Luke had a totally unrelated problem some number of weeks later, I also had a terrific analysis that he wrote up. And part of what I want to get to today that I love about both of these is both of you did a really, perfect job of describing your methodology, which I feel I mean, I don't think that happens that frequently. I feel that, like, often, it's just kind of the solution is revealed as if a magic trick, and people don't describe what they did.
[Speaker 1] [03:05] I don't know. Adam, do you agree with that?
[Speaker 2] [03:08] I totally agree. I agree. There are many bug reports that were sort of I hit a problem and here it is. And what I love about both of these write-ups is the to a degree, like, the mystery and the methodology that, as you alluded to Brian, is repeatable, right? Like, it's not just that if I read it, I understand this specific issue, but people can learn how to debug, you know, other types of issues in that vicinity by reading.
[Speaker 1] [03:38] So with that, Jordan, I think that we maybe hand it over to you. 1, maybe you wanna talk though a little bit about specifics of the bug as well, or go in the can arbitrary gap there. But, 2, what prompted you to write all of this up and kind of have this narrative flow to it?
[Speaker 5] [03:58] Sure. So first, if I don't write things down, particularly when I'm exploring a new area or something that isn't something that I really know well, I will forget it. So, like, half the reason for writing it down is partly selfish just because I want to remember what I discovered and learned. Another thing that is very motivating for me to write stuff down, when debugging is that I have frequently come across bug reports where the bug seems fascinating, but I have no idea how the person that debugged it figured it out. And there's a lot of I mean, everyone has different context and experience and knowledge, so some things might be obvious to some people and not others.
[Speaker 5] [04:38] But as much as possible when I write bug reports, I try to include enough context that someone that doesn't have as much experience could learn from it and figure it out. I can talk about the specifics of the bug too. Yeah. If that's interesting.
[Speaker 1] [04:51] Absolutely. I think the specifics of bug are interesting. Well, first, just I on that. Because I think that that's so interesting in terms of writing it down both for your future self, which I absolutely am with you that I really need to your know, I keep a notebook at my side. I really feel that I need to write things down.
[Speaker 1] [05:05] I it really helps me process things. But then I love the pedagogical approach too of teaching people how to debug. Because, I mean, Jordan, I don't know. I mean, I believe that debugging can be taught and learned, but I'm not sure that everyone believes that. I and, clearly, you believe that.
[Speaker 5] [05:21] I definitely believe that. It's not it's not easy to learn, but, it's its something that I think with more and more experience yourself doing it and seeing other people doing it, it, you can definitely learn it.
[Speaker 2] [05:34] But you hit a perfect point there, Jordan, which is I think it is hard to learn in part because there aren't that many folks trying to teach. So I think it's great to see this kind of example where people can learn from this. Like, this is a strong example if someone
[Speaker 5] [05:49] wants to learn more. MMM. Yeah.
[Speaker 1] [05:51] And then do we yeah. Do we get a little bit in the into the bug itself too because the bug itself is pretty gnarly in that it's a failure mode that's in a spot that's actually pretty tricky to debug?
[Speaker 5] [06:02] Yeah. Sure. So, Josh Kuala, who's I doingn't know he's going to be joining, but I see he's here, had encountered this bug originally. So we have some, lab infrastructure for oxide, and some of the machines when they were rebooted would seem to hang. And so Josh was able to narrow it down to specifically the NVMe class path.
[Speaker 5] [06:27] And because I have some experience with NVMe on a Lumps, he asked me if I would look into it. So the first thing that I did, because this is a hang, I wanted to see if we could NMI the box and then get a crash dump. But because of You
[Speaker 1] [06:42] wanna just explain briefly what NMI is?
[Speaker 5] [06:45] Yeah. Just, I mean, send an interrupt to the box that, I'm sure other people can explain this better than me, but that will generate a crash dump and reboot it. Right? So then you can take that crash dump, attach a post-mortem debugger to it, and look around at the state and see what it was doing, when you generated the dump.
[Speaker 2] [07:05] And when non makable interrupt traditionally, like and now this is getting into green room era nomenclature, But, like, this was a physical button or jumper that you would press, like, on a actual box to, like, send an external interrupt.
[Speaker 1] [07:21] In Black friars Theatre 15 minutes. That's right.
[Speaker 2] [07:24] As
[Speaker 1] [07:25] we all recall. Yes. You know, I don't know that there was ever. Was there a physical button? Oh.
[Speaker 2] [07:31] I'm a Yeah. For sure. For sure. And often, I'll tell you from experience, they cost extra. And I worked for a company that didn't pony up.
[Speaker 2] [07:43] So I would at times be stabbing away at jumper pins with a knife from the kitchen to try to cause an actual interrupt. Which I think the like the original Macintosh had a plastic
[Speaker 6] [07:56] box you could buy that would jam in a
[Speaker 2] [07:58] hole in the side to reach the thing. Right? That's right. In, like, 1984. What is
[Speaker 6] [08:03] this knife in the
[Speaker 2] [08:03] kitchen story that did they just
[Speaker 1] [08:04] Hold kitchen story that did I just
[Speaker 2] [08:06] Hold on. Hold on.
[Speaker 1] [08:07] Did I just dream that? No. No.
[Speaker 2] [08:09] I'll, I'll send you a picture, but we had a then opened Polaris box. This is when I was at Delphi, that was hung mysteriously, so we wanted to generate an external, non makable interrupt in there, AIR. And like, we didn't, we hadn't paid, you know, some random HP box. We had not bought the little Jumper Goober. It was going to take 2 weeks to get there.
[Speaker 2] [08:32] So what I needed to do was short out 2 pins and the most expedient this is Adam Summerhill hardware engineer.
[Speaker 1] [08:38] I was Adam Summerhill hardware
[Speaker 2] [08:48] of this, but, I used this to generate a picture.
[Speaker 6] [08:51] Hu Hewlett Packard seeking rent on a small piece
[Speaker 2] [08:54] of plastic and metal is pretty on brand.
[Speaker 1] [08:57] It is pretty on brand. Okay. I know, I just never real I think I'd always done this via PMI or the BMC. I didn't I guess I didn't realize they had actual physical buttons. But, Jordan so, Jordan, we I'm sorry.
[Speaker 1] [09:11] We we we digress. Did you No?
[Speaker 5] [09:13] It's alright.
[Speaker 1] [09:15] So did were you able did you have to get out a knife? Did you have to go
[Speaker 2] [09:19] did they get out of
[Speaker 1] [09:19] the kitchen knife, or
[Speaker 2] [09:20] were you
[Speaker 1] [09:20] able to send an NMI to the to this box?
[Speaker 5] [09:23] So no. Knife or otherwise. My point was that this was not even something that was available at this stage of reboot.
[Speaker 1] [09:31] Yeah.
[Speaker 5] [09:33] So, you know, other measures had to be taken.
[Speaker 1] [09:36] And when you say it was not available, was this because the system had already been that it was we were kinda past the point where we could reasonably take a dump?
[Speaker 5] [09:44] Yes. Like, the these are some of the of the devices is some of the very last things that happens, before it goes away.
[Speaker 1] [09:52] Yeah. That's brutal. That is brutal. And this is the problem about a crash dump, but we're relying on a flawed system to actually write its state to disk. And if that flawed system has already passed the point and no return, it's very hard to do that.
[Speaker 1] [10:03] Right.
[Speaker 5] [10:04] We're we're telling it to stop using the disk, actually.
[Speaker 1] [10:06] Right. That's actually what we're trying to do. Right. Exactly. Okay.
[Speaker 1] [10:10] So that's a good approach that, but that's not gonna work here.
[Speaker 5] [10:14] Right. But so, we can still use KMDB.
[Speaker 1] [10:21] And quick do you want to describe KMDB in a sentence?
[Speaker 5] [10:24] Yeah. It's, it's a debugger. The k is for kernel, I assume. But it only it basically stops the entire machine and is only running on 1 CPU. So normal MDB would not do that or normal MDB dash k would not do that.
[Speaker 5] [10:41] So, basically, if I'm on KMDB, no one else no one else or nothing else can be using the box.
[Speaker 1] [10:47] Right. So this is an in situ debugger. The world is stopped when you're at the debugger prompt here.
[Speaker 5] [10:52] Right. And I can advance the instructions, like a step debugger, which is what I did. The first thing I wanted to do was to figure out where it was hanging, since I couldn't know that with a crash dump. So I set some break points on functions inside the NVMe function, which is where Josh had narrowed it down to. And the very first thing I noticed was that it wasn't actually hanging, but that it was, looping.
[Speaker 5] [11:25] So there's it the NVMe class function does 2 big things. 1 is, it will send a shutdown notification to the device, which is part of the NVMe spec, and then it will do a reset of the device, which is another, thing to the in the NVMe spec, and both of these are done by rights to the controller configuration register. And so yeah. I mean, I can keep keeping digging in there? There 's's a lot of stuff I did.
[Speaker 1] [11:53] Yeah. I mean, if you mean, this is great. Sorry. You got I'm at the edge of my seat. I you Sure.
[Speaker 1] [11:58] You kind of read this, though.
[Speaker 5] [12:00] Yeah. So, the so I noticed that it was looping. If you look at the code for NVMe reset, what it does is it will write, all zeros to the controller configuration register, which the primary purpose of that is to clear the enable bit, which is how you tell the controller that you want to reset or enable the device. And so if you clear it to 0, that means you're wanting to reset it. And then the way that the controller tells the operating system that it's processed that is that it sets another bit in a different register, called the controller status register, and that tells the operating system that this device is reset, and you can move on.
[Speaker 5] [12:40] And so, basically, what that loop was doing was checking that bit over and over again and never seeing that the controller had processed that reset.
[Speaker 1] [12:48] And these are phenomena that are specified in the NVMe specification. Correct?
[Speaker 5] [12:54] Yes. Yeah.
[Speaker 1] [12:56] It so I think sometimes it's it is, for folks that they haven't done necessarily low level systems programming, don't necessarily maybe they get accustomed to, like, documentation being poor. And when you get to these hardware standards, like, the documentation is actually pretty good. I mean, they're they're pretty complete. And you can go to the documentation for generally an authoritative answer. So I imagine you were going to the the were in the specification at least a decent amount to understand what the behaviours were of all these things.
[Speaker 5] [13:23] Yeah. And it definitely all the information I needed was there. Sometimes it can be hard to figure out where you need to look. Right. But, they are pretty good.
[Speaker 5] [13:33] And I've spent some time in the NVMe site before, so that definitely helped.
[Speaker 1] [13:37] Okay. So you've got the know what's what's kinda supposed to be happening here and then but what's actually happening?
[Speaker 5] [13:44] Well, it's that so it's checking for this bit, the controller status ready bit to be set to 0, and it's its not seeing that ever. So it it's its just there's a time-out that's specified in the spec and that the code is kind of just, like, spinning, until that time out is up, and then it moves on. And so what this actually means is because of the wait time between looping, it ends up actually not hanging, but taking about 10 minutes to reboot, about 2 2 minutes or so per, device. So it will eventually actually reboot, which is better that I think than hanging, but, you don't want to have to wait 10 minutes for your machine to reboot.
[Speaker 1] [14:27] Yes. And this is a variant of a time-out. And a poet I know once said something very good to me about time-outs. Mister Kaluga, would you like to do an out loud reading of your famous poem? Is he?
[Speaker 1] [14:40] Josh has given up on us after
[Speaker 6] [14:42] Oh, I'm here. I'm here. I'm here. How does it go? Time out to time out.
[Speaker 6] [14:49] Always wrong. Some too short and some too long.
[Speaker 2] [14:55] Bravo.
[Speaker 1] [14:57] Words submitted by. Excellent out loud performance. Thank you.
[Speaker 2] [15:00] We're coming up on our 5th year anniversary of that
[Speaker 6] [15:04] jumpy. Also, also, like, it is pretty ironic that I thought it had hung because I had waited only 5 minutes for
[Speaker 1] [15:13] a few minutes staring as
[Speaker 6] [15:16] you do after quiz at the prompt that does nothing.
[Speaker 2] [15:19] It doesn't even echo characters back to you.
[Speaker 6] [15:21] It's like, well, it's probably hung. Wrong. Come
[Speaker 1] [15:24] on. It's as it turns out, it's just if it is actually just in a very long time out very repeatedly. Yep. Sorry. So, Jordan, we now know that, time out's always wrong.
[Speaker 1] [15:35] Some too short, some too long. This seems maybe perhaps to be of the too long variety, but is what the spec more or less says. Right?
[Speaker 5] [15:42] Yeah. Yeah. It was spec compliant for sure.
[Speaker 1] [15:45] That's always depressing.
[Speaker 5] [15:46] The, the time-out in the control like, so the time-out actually is from the device. So maybe the
[Speaker 1] [15:57] So how do we, so why doesn't everyone see this problem, and how do we how do we fix it? I guess that was the kind of the next batch of experiments.
[Speaker 5] [16:05] Yeah. I mean, I didn't put this in the analysis, but I looked at I have a Lumps desktop too with NVMe devices. So I kinda looked at that and made sure that it behaved in the way that we would expect, and it did. Those devices also had a much smaller time out, which was interesting. But, yeah, so I didn't, like, really know what to look at next, but one thing that I thought was kind of strange was the way that the controller configuration register was written to, which is the one that has the bit to reset the device.
[Speaker 5] [16:39] For most register rights and device drivers that I've seen, typically, you'll do a read, modify, and then write of the register. So you'll read the value that was there, just change the bits that you wanna change, and put it back. And in this case, was just clearing all of them
[Speaker 2] [16:55] Right.
[Speaker 5] [16:55] Which might not matter, but, I wanted to see if it did, because this clearly is weird. So this is kinda where it got fun because I was able to change what things were actually getting written to the device without doing an operating system build.
[Speaker 1] [17:12] And that Yeah. I was almost going to call this, like, debugger driven development. MMM. Because the are kinda treating the debugger as an almost a rebel for the system and changing the behaviour of these devices and then observing how they change.
[Speaker 5] [17:28] Yeah. Because we're writing to or because the value that gets written to the register is just an address in memory that is also in a register. It's all accessible, you know, through the debugger. And I had some help here from Robert Mustachio a little bit to kind of figure out how to trace the exact mappings of, like, the virtual address to the physical address and things like that. But once I had that tool available, it was pretty easy to iterate.
[Speaker 1] [17:55] Yeah. That's really cool. And so it, and then you kinda in your analysis, you go into, what happened when you did that, but then it ultimately ends in a bit of a dry hole. Right?
[Speaker 5] [18:09] Yeah. So I tried the read, modify, write path, and the behaviour didn't change. So that was kind of disappointing. And because I had gotten, like, some outside help to figure out how to do this process, I was worried that maybe there was something I didn't understand, and I spent a bunch of time reading code and, like, spent more time than I should have. And then I realized that it would be much more productive to just try something else.
[Speaker 1] [18:35] Okay. This is a fascinating point. I was going to ask you this earlier too when you said that you were before doing this experiment, you felt like, I'm a little stuck. I don't know what to kinda what to do. So you kinda just did something, which I thought was interesting.
[Speaker 1] [18:50] Like, alright. I'm just going to explore, like, this aspect of this problem. And I kinda find it that to be an in a kind of important, psychological, kinda, aspect of debugging. When you get stuck, it's important to actually unstick yourself by just trying to understand the system better. I think it's generally a good way to unstick yourself.
[Speaker 1] [19:13] Yeah.
[Speaker 5] [19:13] It's definitely something I'm very tempted to do, of, like, going in a deep rabbit hole trying to understand something without just experimenting. Experimenting, I tend to find to be much more fruitful. So the thing I tried next was, so I mentioned earlier that the NBB QS does 2 big things. It does the shutdown notification and then the reset, And the shutdown notification also writes to that same register, but a different set of bits. So I was curious if maybe I did that in one single register.
[Speaker 5] [19:47] Right? So do the shutdown notification and the reset in the same right instead of 2, if it would behave any differently. And my intuition about these things also comes from, like, some experience with dealing with NVMe firmware before. Just
[Speaker 1] [20:02] Right. Right. So Right. This would be the first time that firmware would be fickle about this.
[Speaker 5] [20:08] Right. So in a previous life, at Joy ant, when I was looking at some NVMe related things, I ended up debugging an NVMe or PCIe firmware, issue where a right to 1, like, register of 1 device would affect another device, which is very strange.
[Speaker 2] [20:28] Yep. That is very strange. Can you say just a little more about that?
[Speaker 5] [20:32] Yeah. So, the basically, what we observed was if you powered off one of the slots, which is, like, where you plug in the disk, using a command line tool, another disk would report that it was removed, which didn't make any sense because I could see that it wasn't removed. It was right there.
[Speaker 2] [20:54] It's great.
[Speaker 1] [20:55] But That
[Speaker 3] [20:56] that is a great bug.
[Speaker 1] [20:57] That there is something just I'd be just so chaotic about that bug.
[Speaker 5] [21:03] Yeah. So that bug was very fun, but it also, like, showed me that my the abstraction of, like, registers. Maybe isn't always as clean as I thought.
[Speaker 1] [21:14] Like, that bug taught you to trust nothing or yeah. Like, I can trust absolutely no one at any time? That's so okay. So you've had this experience with, like, with firmware doing things out of bounds. So wouldn't be the first time.
[Speaker 1] [21:28] So, hey, let's try giving this some the giving this thing the rights differently. Let's see if it actually wants them as separate rights. And does that change anything?
[Speaker 5] [21:37] Yeah. The other thing I would mention that previous firmware bug is that, when I was working on it, I got very frustrated that MDB could not tell me which bits were set because the way that these registers work is they're like a 32 bit value where you've set some bits, which is your know, easier for computers to read than humans if you're just looking at a single hex value.
[Speaker 1] [22:00] It turns out. Yeah.
[Speaker 5] [22:02] And so, Brian, you went and implemented the j format, which will take a value and show you which bits are set and the masks, associated with it. And then I use that all over this bug, and I was just, like, overjoyed.
[Speaker 1] [22:16] That is so great. And it is, and it should be said that the Jay format character stands for Jordan. Jordan needed it. And so And I need
[Speaker 5] [22:24] it again.
[Speaker 1] [22:25] And so you don't know this happened.
[Speaker 2] [22:27] No. I I I, you know, I haven't seen lowercase j before. Very cool. I also, like, I know I don't doubt for a second that it stands for Jordan. I also wonder how many letters were available.
[Speaker 1] [22:39] Well, not very many. Yeah. I mean, I Lots of damage.
[Speaker 5] [22:43] I think it's gassed up.
[Speaker 1] [22:46] It actually, I did feel like I'm like, look. I can't just be, like, Jordan asked for this in the man page. So I'm like, I have to find some way of justifying this. So, yeah, I think I was jazzed up, which is pretty still is pretty weak
[Speaker 2] [22:58] at the time. That's that's right there with flow indent.
[Speaker 3] [23:02] Before
[Speaker 1] [23:03] Woah. What is a flow indent? You, I'm sorry. And you have you view Originally said 4
[Speaker 2] [23:11] minus f for fancy. That is true. That is
[Speaker 4] [23:15] true. Damn it.
[Speaker 2] [23:15] That's
[Speaker 1] [23:15] true. Yeah. No. I'm pretty
[Speaker 2] [23:16] top there. So that was a Trace green room lore.
[Speaker 1] [23:20] You know, I had, believed my own marketing literature on that one. I had actually I had actually kinda forgotten about minus cap f is actually fancy. For fancy? And I had flow indent seemed so plausible. I thought that I but you're right.
[Speaker 1] [23:34] No. No. It was
[Speaker 2] [23:35] It was for fancy. Right.
[Speaker 1] [23:36] It was for fancy. Alright.
[Speaker 2] [23:37] Anyway, for jazz jazzed up binary. Cool.
[Speaker 1] [23:40] Yeah. And it's actually it is actually super useful, honestly.
[Speaker 3] [23:43] I's
[Speaker 2] [23:44] really useful for people to hear.
[Speaker 5] [23:45] 50 b just to, like, get use the jazzed up format.
[Speaker 1] [23:49] Use the jazzed up format. And I feel that, like, this I have to this is just quick aside. One thing that I absolutely love about Rust is its ability to express binary literals, and I know that, like, that there are c extensions that do this as well. But, when you are it when you're dealing in binary, which you are with the register, for example, where different bits represent different states, it's very nice for the code to be able to also deal in binary. And I have to Jordan, if I were to add something that maybe we should add something to jazzed up.
[Speaker 1] [24:17] I love the underscores, the arbitrary underscores that you can have in, in Rust as a delimiter to make it a little bit easier to kinda count,
[Speaker 2] [24:26] nibbles. So holy smokes. I mean, that is such a minor breakthrough that
[Speaker 1] [24:30] was sitting right there.
[Speaker 2] [24:31] I know. People could have had it forever and would have eliminated so many bugs
[Speaker 1] [24:37] absolutely.
[Speaker 2] [24:37] Just to let people not need to count digits.
[Speaker 1] [24:41] So and when you use are you referring to 0 b as the delimiter, or are you referring to just the ability to have the underscore?
[Speaker 2] [24:49] Actually, just underscores, but 0 b is obviously also, like, a game changer. Like, why couldn't we have had that when, like Right.
[Speaker 1] [24:56] We had everything else You know?
[Speaker 2] [24:57] When 0 as a prefix stood for octal, like, anyway, the underscore is just
[Speaker 3] [25:04] just great.
[Speaker 1] [25:05] It's great. It's really nice. Yeah. So, Jordan, you are you're able to interpret the binary quickly of all these registers, which is very helpful. And, it's only, and I should also say that the on the one hand, it's, I mean, obviously, it's great to be able to use this thing and implement it.
[Speaker 1] [25:21] I feel we have done this. We, collectively, have seen this so many times over in our careers where when we needed something, we stopped and implemented it. And then we were really grateful later when we were debugging something else to have the thing that we had stopped and implemented years prior, months or years, whatever, prior. And I I I do feel that, like, something that we we we really culturally encourage at Oxide is if is you need the tooling, stop and implement it because you're probably going to need it again. It's probably not the last time you're going to need the tooling.
[Speaker 5] [25:53] Yeah. Absolutely.
[Speaker 2] [25:55] That that's one of my favourite things about our culture is the window because when you're building tooling that, you know, you think you might need, it might save you 5 minutes by spending 5 hours writing. It's always hard to justify, but it's so great working with so many engineers who have seen the benefits so many times, who can just remind you that you to have seen those benefits.
[Speaker 1] [26:17] That that's right. Yeah. Because I sometimes it can feel like, what am I doing? Like, am I should be back. Like, I'm now I'm on 4 tangents deep.
[Speaker 1] [26:25] And it's we, again, we've seen that payoff just so many times. We definitely saw it pay off here. So, so, Jordan, where did you, so where did that leave you? Did the because I think that experiment also was a bit, the and part of why I love you about your write-up is you're talking about these
[Speaker 5] [26:51] one thing that I hadn't mentioned here yet, is that the shutdown notification, there's there are 2 kinds that you can do for the spec. 1 is normal, and 1 is abrupt. And this code was using the abrupt shutdown notification, which seemed interesting.
[Speaker 1] [27:08] Yeah.
[Speaker 5] [27:09] And so I had wondered, can I do a normal one? Would that be fine? I looked at the spec, and, it seemed like the abrupt shutdown was kind of a heavier hammer than was really needed for this path. So I wondered if maybe just trying that would work. So I repeated that same experiment of writing the notification and the reset in one right, but this time with normal shutdown.
[Speaker 5] [27:39] And, for the first time ever, the ready bit, which was the thing that the reset was looping on, actually said that it was 0. So that was that felt like, okay. Like, there's something here with abrupt shutdown.
[Speaker 1] [27:52] And that must have felt great to have that you're like, okay. I meant I I I've now tried a couple of different things, but, boy, okay, now I've actually got a direction that's yielding progress.
[Speaker 5] [28:03] Yeah. And at this point, this is, like, a Friday. It was probably, like, 4 o'clock, and I just felt like I had, like, a Red Bull or something. Like, I was so impressed to figure it out at this point. Yeah.
[Speaker 5] [28:17] So the last step was to just kind of go back to the normal path and split those back into 2. So instead of changing what the reset does, just changing the normal shutdown notification, the shutdown to use normal notification, and it worked.
[Speaker 1] [28:32] That's great and very satisfying. And then, had you been writing this up as you've been going through it, or did you, and you said, like, hey. I really should write up everything I did here. What where was the kind of decision to write everything up?
[Speaker 5] [28:47] So I kind of, like, I had been taking scattered notes. So this is something I actually wanted to mention. I feel like a lot of my debugging reports or bug reports are very, like, narrative and linear, but that's not always really how it goes. It's only something that you can, for me at least, make sense of after the fact a lot of the times.
[Speaker 1] [29:10] Totally.
[Speaker 5] [29:10] So once I figured it out, I immediately started to write it down because I was like, if I wait until Monday or something, I'm going to forget all of this. So I wrote it down, posted it over the weekend. But, yeah, if it was definitely, it was not this clear until the end.
[Speaker 7] [29:29] Right. You know?
[Speaker 1] [29:30] Well and, again, I mean, I love the all the talking about the dead ends, and the things that didn't work, things you experimented with because I think, it allows people to 1, it allows people to understand. I think one of the most important things to convey when teaching debugging is that there are a lot of dead ends. There are a lot of things you investigate that don't go anywhere. And you don't be fooled by the person next to you that seems to know the answer because they actually probably went down a bunch of dead ends as well. And when we don't show that to other people, we would, they can think like, oh, I can't debug this because I don't know the answers.
[Speaker 1] [30:07] No. No. No one knows the answer. You would need to actually, like, and you have to go explore these different paths. So that's part of what I loved about the write-up.
[Speaker 1] [30:13] That was really great.
[Speaker 2] [30:15] Agree with that, Brian. I think the other pathology that can come, is that people kind of taking stabs in the dark or rather not having the level of rigour that Joe described in this. Yeah. And instead using this sort of pattern matching oral tradition of debugging where they say, one time I saw an NVMe hang and it was this thing. So let's, you know, it must be that again.
[Speaker 2] [30:40] And I think that when you don't see the process, and you don't see those blind alleys, it can lead people to thinking that it's always kind of this monotonic magic.
[Speaker 1] [30:51] I totally agree. And, like, I have a really hard when people are like, oh, it's this. I know it's this. And they're kind of like, okay. Wait a minute.
[Speaker 1] [30:57] We're like, let's gather some data. It's like, no. No. I've got a fix. Like, I've pushed the fix.
[Speaker 1] [31:01] It's like, you pushed the fix. What? Where are we right now? Right.
[Speaker 2] [31:04] Right. What's the problem that we're
[Speaker 1] [31:05] It's like, Are we, like is this, like, moving fast and fixing things? Like, what do we do what do we think we're doing? And, of course, like, oh, actually, that wasn't it. And, oh, but now no. No.
[Speaker 1] [31:14] It's this. It's this. It's like, okay. Oh, yeah. You're giving me a headache.
[Speaker 1] [31:17] Can be just, like can we actually gather the data, ask the questions, do the experiments, and, like, let's get this thing, like, really, really nailed. And then we've got this little confidence.
[Speaker 2] [31:28] And that is the power of tooling. Right? Because Yeah. I think we are, you know, intrinsically or at least maybe I'm speaking for myself here impatient. Right?
[Speaker 2] [31:35] Like, we want to see progress.
[Speaker 1] [31:36] Yeah.
[Speaker 2] [31:37] And Jordan, to your point, you don't, you did all of this without needing to take a turn of the kernel for each of these experiments. But there certainly was an era where that's what you would have needed to do. And by having, you know, KMDB and all of these facilities that allowed you to do all these experiments. I mean, it probably felt ponderous at the time, but much more expedient than it would have been without this kind of tooling.
[Speaker 1] [32:02] Yeah. Yeah. Totally. And then, well, this is a hard problem without an in situ kernel debugger. This is a hard one to this is actually really hard to debug.
[Speaker 1] [32:10] You're kind of like you, you're going to take iterations on, like, a print f equivalent kind of because you can't even really log anything because this is a're resetting the system. So all your state is going to be technologically lost, and this is a really hard problem to debug in that regard. Absolutely. Alright. So maybe it's a good time to get looping in here.
[Speaker 1] [32:30] And so, looping, you'd hit an an a totally unrelated bug sometime later, an an a Rust SEG fault, but you took us on
[Speaker 2] [32:42] a very similar journey to Jordan.
[Speaker 3] [32:47] Yeah. But, actually, to clarify, though, it was, one of our other coworkers, Patrick, who ran into it initially while they were trying to get us updated to, like, a newer rest nightly or something. And they're running into this issue where compiling even a basic example that used, a library that used inline assembly was just causing for us to crash in default.
[Speaker 1] [33:13] And okay. So, Luke, do you have, like, alerts? Because, like, I feel you've done this a bunch of times at Oxide where, like, you feel there's, like, a disturbance in the force, and, you know, people are looking at a rust issue. And all of a sudden, like, Luke is here, like, with, like I that's like you are very, tuned in when anyone is having an an an a challenge with the Rustic Power in particular.
[Speaker 3] [33:36] I think it's just I had this need to, like, get rid of that little white dot in element. So I'll just always, like, click through the channels. And then at least in the oxide Rust one, I can understand a lot of things. It's like, oh, maybe I can figure out what's going on here.
[Speaker 1] [33:50] Okay. Interesting. That's great. Okay. So you but you
[Speaker 2] [33:53] see you see Patrick has seen this issue and MMM.
[Speaker 1] [33:55] This is something that you obviously know a lot about, and you're you're ready to go kinda take a swing on this. Do you want to describe the actual the symptoms of the problem?
[Speaker 3] [34:05] Sure. Yeah. So I think, it was, like, already reduced down to something pretty easy to just run. It was just, like, build an example from, like, the USDT crate. USDT here being the actually, I don't remember what it stands for, but die something dynamic tracing.
[Speaker 2] [34:22] Usually and statically defined tracing.
[Speaker 3] [34:25] There you go. Thank you. So it's like, okay. Let's just run that and see what happens and, you know, type faults. Okay.
[Speaker 3] [34:34] And then it's kinda like going through the motions. Well, already, I think Cliff had narrowed it down to something failing in LVM, like the control flow construction failing. So it's like, okay. So something's failing in LVM. Usually, that's because of maybe some kind of invalid IR that it's trying to work with.
[Speaker 3] [34:56] So let's just try to verify the IR that we have.
[Speaker 1] [34:59] I was going to ask you, like, how many? Because I have, I don't feel I've seen that many Rust cycles. And to be clear, so people understand, this is the compiler that is cycle vaulting. It is not a Rust program. It's the compiler itself.
[Speaker 1] [35:11] Have you seen a bunch of these? Look at them. I mean, obviously, you've been you've been in Rust for a long time, so maybe this has been more common or maybe you've seen a bunch of these.
[Speaker 3] [35:21] I don't think in they happened. I feel like these happened especially more so around LVM upgrades.
[Speaker 1] [35:28] Interesting. Yeah.
[Speaker 3] [35:30] It's probably the time that you'd probably notice them the most. But yeah. So it's like from there, it's just like, okay. Well, let's see if we could even just figure out if we're giving it valid IR to begin with. And, you know, it kinda got lost a little lost there because of the flag's not exactly doing what they said they were doing because of a different bug.
[Speaker 1] [35:55] And is that flag is verified LLVM IR. Right? That's the flag that's not doing what it should be doing?
[Speaker 3] [36:02] Yeah. Or Right. At the time yeah. Because, at some point, LVM had switched from, like, a to a different pass manager. And as part of that switch, the way certain flags were handled, changed.
[Speaker 3] [36:15] And for some reason, it was not respecting that one.
[Speaker 1] [36:19] And so I
[Speaker 3] [36:19] was, like, totally saying, yeah.
[Speaker 1] [36:21] Oh, that's frustrating. So, I mean, alright. A couple of things here. 1, I do think that one of the things you know, And I've seen you do this a bunch of times when there are a lot of rust flags out there that can be passed to various stages, and they can be really, really helpful in debugging these kinds of problems. And I don't know if you had these or have you dug into all the there's a lot there.
[Speaker 2] [36:40] No. I mean, I've I've seen the list and, only enough to, like, know to be overwhelmed by the number of options there.
[Speaker 1] [36:49] And so, look, I'm going to go ahead, and it's great that, like, you know the tooling and, like, okay. I've got this tool I could use. And then it must be frustrating to be, like, okay. That does not do what it's supposed to do. Never mind.
[Speaker 7] [37:02] So I guess. Yeah.
[Speaker 1] [37:03] So what's next? So that's alright. That is not the the this verifies the the verify LOB MIR is not doing what it should be doing.
[Speaker 2] [37:11] Actually, I
[Speaker 3] [37:12] should clarify. It was doing it by itself. It was when you combined it with a different flag. So when you yeah. So it was saying, yes, it was outputting.
[Speaker 3] [37:22] Okay. Yeah. So we are getting some invalid error where, like, there's a basic block that doesn't end in a terminator instruction or something like that. Yeah. And it's like, okay.
[Speaker 3] [37:33] Well, can we actually look at that so we see what it looks like? And so I was just basically trying to narrow it down to that and get that output so we can at least look at it, see if it even looks right.
[Speaker 1] [37:49] So the because this is a theme I think we saw with Jordan as well where you're you're very good at kind of, like, being curious about it. Like, as opposed to being overwhelmed by it of, like, oh my god. Like, how is this possible? I think it's, and I think kind of stoking that curiosity is a really important part of the body.
[Speaker 3] [38:16] Yeah. I mean, a lot of it too here is familiarity.
[Speaker 1] [38:20] Yeah. Interesting.
[Speaker 3] [38:21] You know, it's like kind of knowing where to look and kind of what avenues might be interesting, I think definitely helps with not feeling as overwhelmed by it. But you can also just kinda decide to choose one place and sort of drill down there. But it's kinda like balancing between how deep to go versus, you know, how wide to go sometimes. And I think something like Jordan said before, it's like having the intuition also really helps.
[Speaker 1] [38:48] Yeah. And, of course, and then building that intuition over time Yeah. By just debugging these things. Okay. So you've got this thing, reproducible, and are you able to yeah.
[Speaker 1] [38:59] What do we learn about the IR's? You're kind of asking these next questions.
[Speaker 3] [39:03] Yeah. So, like, once you actually tell it to verify instead of crashing, it'll tell you, okay. So, you know, there's this basic block. Doesn't end in a terminator expression. It's like, okay.
[Speaker 3] [39:14] And we eventually figure out how to get it dumped out, and we're looking at it. So we see it's like, invoking the inline assembly, and then after that, it's trying to do a store. And the problem here is that, yeah, invoke is supposed is the terminator expression. You're not supposed to have anything else in the basic block after that. So why is the store happening there?
[Speaker 3] [39:39] And so from there, it's kinda like, for me, it was like, okay. Well, now that I know what the IR looks like, I can kinda go backwards and see where it must Rust we're generating that. And it's like, okay. So this is where the in line ASM thing is happening, and that store, at least in there, looks like it was storing the result, like, one of the outputs. So it's like, okay.
[Speaker 3] [40:00] Where are we doing that in Rust c, And what does that kind of look like?
[Speaker 1] [40:03] So how do you answer that question? Like, where is this store coming from? How do you like, what tools are you using to get from, like, about where that's happening to us?
[Speaker 3] [40:14] I guess, knowing sort of the structure of how
[Speaker 1] [40:18] Yeah. Interesting. Okay.
[Speaker 3] [40:19] Rusty kinda does this. Again, it's kinda like knowing where to look sometimes. Yeah. But, also yeah. Some I also just will use, like, rip grip to just, like, show me all the places that have, you know, the in line as, Yeah.
[Speaker 3] [40:34] Like, AST type that they're manipulating and just kinda look at them. So there's probably only so many places that are relevant.
[Speaker 1] [40:41] So I feel that there is and if someone knows of 1, I would love to know. I feel that there is a missing code Rust code exploration tool, a la c scope. I Adam, do you use c scope on Rust?
[Speaker 2] [40:53] No. I use Rust analyzer, and it's amazing. And I don't know.
[Speaker 1] [40:57] I don't know how you
[Speaker 2] [40:58] live, honestly. Like, I're right. It's its it's just hard for me to imagine.
[Speaker 3] [41:04] Yeah. Definitely. I use Rust analyzer as well. And it's like, yeah. You can and it's like very simple.
[Speaker 3] [41:10] It's like, okay. Well, show me all the references that call, you know, this method or whatever, and, you know, just look through them.
[Speaker 1] [41:17] And so yeah.
[Speaker 2] [41:18] Rust analyzer is so good. Like, I have a hard time looking at code review because rust analyzer like annotates everything with all of these unstated types, and it just can orient you in space in, in a way that, like, I now find load bearing for understanding Rust.
[Speaker 1] [41:37] And even when you are not writing Rust but just trying to understand a foreign code base, you will use Rust analyzer.
[Speaker 6] [41:45] Even just the jump to definition button that
[Speaker 2] [41:47] you can push in your editor, it makes everything Look. This is an intervention, Brian.
[Speaker 1] [41:52] I this obviously is. I was especially
[Speaker 3] [42:03] slightly faded, but, like, still show up? Like, the inlay I think that's what they call inlay type hints?
[Speaker 1] [42:10] I need to get all the way there with Rusty and Eliza. I'm truly living in a barn. I I I I get that message, like, loud and clear that I need to actually, like I there are better tools that I need to use. So talk about better tools. I
[Speaker 2] [42:20] need yeah. The neat thing about the LSP stuff is that you can both live in
[Speaker 6] [42:24] a barn and have, like, running water. It's good.
[Speaker 1] [42:30] Oh, there we go. Like a rustic barn. Like, like a bed and breakfast barn. A Vermont bed and breakfast barn. Fancy barn.
[Speaker 1] [42:35] That's the
[Speaker 6] [42:36] that's the one.
[Speaker 1] [42:37] Alright. Yeah. I want to live in a fancy bar. Okay. So clearly that well, thank you for answering my question.
[Speaker 3] [42:41] Namely Yeah. Yeah. And I mean, you can like, I definitely also have, like, rest analyzer set up for, like, the, you know, the checkout of the rusty code that I have. So it's, like, easy to kinda jump around in the code with that. You know?
[Speaker 3] [42:53] It's like, okay. I see this call. Just, you know, just click and go to the definition. You know? It makes it a lot easier when you're sort of jumping around and just exploring too.
[Speaker 1] [43:05] Yeah. I'm embarrassed to say how I've been living. But,
[Speaker 2] [43:07] so yeah. So do we use c scope for Rust? No. We don't, Brian. Great
[Speaker 1] [43:11] question. We don't have any stuff. No. We don't do it. No.
[Speaker 1] [43:15] I mean, I was like I was asking for me. I was asking for a friend. I obviously I mean, obviously a friend. Obviously, you're supposed to analyze. I mean, I just don't know how to tell it to this jerk.
[Speaker 1] [43:24] Alright. Yeah. Anyway, we'll meet right along. So but, you know, actually, that's actually good honestly, that's good to know is I I I guess I didn't realize that folks were using Rust analyzer on code bases other than outside of being an IDE and using it purely as a code exploration tool on another source base. That's that's very helpful.
[Speaker 1] [43:45] I obviously need to start using this thing. And Yeah. Sorry. So you're using that to figure out where is this phrase store coming from?
[Speaker 3] [43:55] Yeah. And, actually, I guess part of it is also, like, once I saw the LVM IR, it's, okay. Well, we know the IR is, like, invalid. What about from Rust's perspective? So I was kinda trying to there's, like, a whole little journey about trying to dump out the RESMR, so the middle what's that word called?
[Speaker 3] [44:13] Yeah. Middle IR. And looking at that. And it's like, okay. Well, we're looking there, and it looks reasonable.
[Speaker 3] [44:22] So something in between going from the MER to the LVM IRR is where the issue seems to be. And a lot of the
[Speaker 2] [44:31] Can I ask, Lachman, what in the MRR was it that you were familiar with it, and it seemed fine based on your expertise or that you were sort of less familiar, but nothing stood out as obviously wrong?
[Speaker 3] [44:48] A bit familiar with it. Not like super, but still Okay. Enough to say that, okay, this looks reasonable.
[Speaker 1] [44:55] Okay.
[Speaker 2] [44:55] Like, not obviously fucked up. Still might be a problem, but, like, enough to move on. Got it.
[Speaker 3] [45:00] Yeah. Enough to, like, at least say, I don't see how we went from this MERE to this LVM IR. Like, there's a disconnect here. Yeah.
[Speaker 2] [45:10] Cool.
[Speaker 3] [45:13] And then it was kinda just, like, verifying those assumptions, you know, in the code and figuring out, like, a lot of the more, like, you know, details of how it actually works sort of thing. And then also and for me, at least with this kind of bugs, I always try to see if I can make, you know, like,
[Speaker 2] [45:32] a reproduction of it. There was already the example, but, you
[Speaker 3] [45:35] know, use external crates. For compiler issues, I feel like if you can get it to a single file, that's great.
[Speaker 1] [45:41] Yeah. Absolutely.
[Speaker 3] [45:43] Yeah. So it was like, okay. Now that I sort of have an idea of what's going on here, can I kind of do that in a single file? And here, it was kinda getting lost for us. It's, like, trying to figure out, okay.
[Speaker 3] [45:55] Well, how do I get Rust to use an invoked here? So part of the issue was that it seemed to be because only happening when it was calling the inline assembly with a call instead of an invoke construction. So I guess to back up a little bit, inline assembly in LVM is, something that you would call like a function, kind of.
[Speaker 1] [46:19] Okay.
[Speaker 3] [46:19] In their IR, so it's like you do something like call in line as in or invoke in line as in. The difference being ease invoke when you want to do to opt into the unwinding happening the unwinding. So, you know, if you want to say my in my NASA can potentially unwind, and I want it to be done the single file repo because I couldn't get it to use the book until I realized, wait. This is because of the whole unwinding thing. And I think I mentioned somewhere in the article, it's like, okay.
[Speaker 3] [46:55] Yeah. So if we actually tell it explicitly this as may unwind, we run into this problem. But then it's like, going back to the USCG example, we're not generating this, you know, inline assembly that can potentially unwind. So, you know, what's happening there? And from there, I think it was what?
[Speaker 3] [47:17] Part of me is just kinda paging this back into what I was doing at the time. But, yeah, it was kind of like looking at the rusty code and getting that epiphany. Wait a second. There is. This is happening because we're doing this inside of an async block.
[Speaker 3] [47:36] And async blocks in the Rust compiler are cogenerated using, you know, generators. And then anything like, it's something like if calls inside that need to be handled, anything that can invoke inside that needs to be handled so that they can poison the generator. It's, like, very much implementation specific stuff.
[Speaker 1] [47:56] Right. Interesting.
[Speaker 3] [47:57] Yeah. So part of it was also actually just, like, looking at some old RFC and being like, okay. I understand why this is the way it
[Speaker 2] [48:07] is now.
[Speaker 1] [48:07] And so I have to say one thing I love about your write-up is as you are, like, digging in, you're always pointing out the flags that you're using, and, like, dump mirror seems extremely useful. I feel like there's all there the like, I want to understand mirror a lot better. Like, I think we've done a lot of interesting things with Mini as well, which is kind of ruling that relies on that layer. I see there's a lot to understand there that, it seems like it's very valuable. And, certainly, you were using it to great effect here, Luke.
[Speaker 3] [48:35] Yeah. Although, it's I feel like yeah. Miró is definitely very much implementation stuff right now. Implementation specific detail thing. It'd be cool if we had a tool for it to, like, just output it and then run optimizations directly on that, that kind of thing, but that's still a ways off, I think.
[Speaker 2] [48:53] Oh, you mean to sort of, like, out it kind of almost pause compilation in the middle, just show your work, and then be able to examine it, make changes, and resume that that that kind of idea?
[Speaker 3] [49:03] Yeah. Like, right now, you can output it. If you can't actually consume any, like, textual mirror because it's Yeah. It's true. Mostly just like a, I think, debugging tool, at least from my perspective.
[Speaker 3] [49:15] Yeah.
[Speaker 1] [49:15] Yeah. Yeah. Interesting.
[Speaker 2] [49:16] I mean, to I mean, that almost gets back to Jordan's methodology of being able to insert yourself in the process and make modifications in the middle, and then that was an avenue that wasn't available to you.
[Speaker 3] [49:28] Yeah. It's like recompiling. Yeah.
[Speaker 1] [49:31] Right. Exactly.
[Speaker 5] [49:34] Yeah.
[Speaker 1] [49:35] Yeah. And so you I mean, so you were able to get to I mean, you get this thing reproduced in relatively tightly, which is obviously valuable. And then in terms of the actual, like, how do you fix this
[Speaker 3] [49:50] thing? And then yeah. So it's like, I had already found kind of where we were going from the, you know, the rest representation to the LVM. So I knew where this was happening. And once I kind of understood, like, all the kind of the moving parts about and the issue on the LVM side too.
[Speaker 3] [50:08] It's like, okay. I understand. It's because the outputs that we're writing, we wrote them into the wrong basic block. Like, it was just a, you know, I guess, just a bug that someone did, you know, while they're writing this up, unfortunately, you know, because we're all human. And it's like, okay.
[Speaker 3] [50:27] Well, now I can verify my understanding. You know, it was, like, I think, 3 lines or something. Just write the thing into the right block and recompile and test it, and it worked. Party flat.
[Speaker 1] [50:40] Yeah. Totally. That was again, it must have felt great. Just like with Jordan, when you're actually seeing the actual bit set or cleared properly, it must have felt great to actually be like, hey. That's it.
[Speaker 1] [50:50] Like, that really validates my understanding of the problem.
[Speaker 3] [50:54] Yeah. Luke, when
[Speaker 2] [50:56] I know there was a very significant, or I think there was a very significant change to the way that ASM works in Rust fairly recently. And it, but it must've been something it can't have been related to that. Like, it must've been some more recent update. Like, do you know, like what changed or this is not the cast blame, but to understand, like, what was in the vicinity that introduced this error?
[Speaker 5] [51:19] I don't know that
[Speaker 3] [51:22] it was a recent change. Oh, I think no. No. The right. The change, I think the reason why we noticed it was because of allowing inline assembly to participate in unwinding.
[Speaker 3] [51:37] That's what it was. Yeah. I see. Okay. Interesting.
[Speaker 3] [51:40] Right. And it was all the, you know, the like, the framework to handle all of that stuff, there's just, like, one little part that was missing, basically, is what ended up happening.
[Speaker 1] [51:52] And how frequent I mean, is it because, synch and ARYM is kind of a rare combination? Is that
[Speaker 3] [51:57] I think that's probably why, you know, it hadn't been probably widely run into.
[Speaker 2] [52:05] Right. And for context, I mean, the're running a bunch of async code and embedding Trace probes within it. The Trace probes are, macros that emit ASM blocks because that's the best way we could think of doing it. So all of a sudden, this uncommon thing became very common. Right.
[Speaker 1] [52:28] Well and what I love about this looping is you kind of, like, go through this debugging it. I think I understand it. Fix the compiler. Okay. That fixes the problem.
[Speaker 1] [52:37] That tells me I definitely understand it, and then you're able to go back to a reproduction that's now even tighter. And it must have been great when that site vaulted on playground. That that that had to have been a good feeling.
[Speaker 3] [52:50] Yeah. It's like, I can easily point at this now. You know? Yeah. Like, very small, well contained.
[Speaker 3] [52:56] Doesn't need to rely on anything else.
[Speaker 1] [53:00] And I think that, you know, it's someone just seeing their bug report may wonder, like, oh, this person, like, wrote this, and it didn't work. It's like, no. No. There was a huge amount of work that led up to this very simple, reproduction, but if it is great. But it was really nice to have a simple and I love being able to do that.
[Speaker 1] [53:23] I've I mean, it's so satisfying when you go from very complicated rare problem to being able to understand it to, wait a minute. If I understand it, then if I just do this, I should be able to reproduce it. I feel like that's, like, one of the greatest feelings in software engineering, I have to tell you. We are able to to make that because it just feels so affirming of your own understanding.
[Speaker 2] [53:44] And to
[Speaker 5] [53:44] go back to what we were talking about earlier about, like, teaching other people, I really loved that Luke man put the reproduction reproduction reproduction example on a playground link and not just, like, as a code block in the gist or the blog post. Like, you could actually go run it yourself. I just thought that was really cool.
[Speaker 1] [54:03] Oh, I think it's great. You can go Sank Vault it yourself. Everyone can go Sank Vault last day.
[Speaker 2] [54:08] You know, one of the things about these minimal reproducers, exactly as you say, Luke and Brian, often it's like the last step. And when you often when you read bug reports, it's presented as the first step. And it's its the thing, you know, that a, you know, this kind of narrative shows you that it was the validation of your understanding, not the, well, here's the problem, and now let's go understand it.
[Speaker 1] [54:36] Yeah. And that's something I feel strongly about is when you have someone who's finding a bug in your own code or reporting a bug in your own code and has it as kind of won't necessarily take you on this long journey from these symptoms far away that I spent all this time distilling it down to this thing that is very tangible. It's part of the reason you always want to be very appreciative when people approach a body of your software with something that's so tight. You'd be like, thank you very much for all the work that you've done to get this so reproducible because you can sometimes it's not a lot of work, but oftentimes, I think people have done a lot of work to be able to get it down to something that's so tight.
[Speaker 2] [55:13] Yeah. Absolutely. Yeah.
[Speaker 1] [55:16] Well, that was great. And then so, Lupin, would I was kinda same question for you as for Jordan. Then what prompted you've done this. This is terrific work. But then you also choose to, like, write the whole thing up.
[Speaker 1] [55:28] And, also, as with Jordan's, like, you showed some things that, like, you explored that were not that didn't end up being it or that you kind of you showed all of your notes. What kind of prompted that write up?
[Speaker 3] [55:41] Well, Well, I mean, yeah, like, I think the inspiration in this case was definitely, like, Jordan's bug report that we were just talking about, like, that was shared, like, I think not very much before this, like, around when this was happening. So I was like, that, you know, that was an amazing read. I feel like I learned so much about it. It was, like, it was going through the journey
[Speaker 7] [56:02] too.
[Speaker 3] [56:02] And I was like, I already have a lot of, basically, the content of what I wrote, you know, scattered about in my terminal history, just like a scratch pad notes. So I was like, I can take that all and now collate it into this actual, you know, journey of going through this bug, figuring it out, fixing it.
[Speaker 6] [56:22] It's, you
[Speaker 3] [56:22] know, something to do while I'm waiting for things to recompile anyway. I know. That
[Speaker 1] [56:27] is awesome. Jordan, that must be especially gratifying for you to hear, because I think it let you if people are wondering how you create a culture where debugging is valued, like, this is a big part of that is that you that, you know, getting inspired by one's colleagues. And I'm in Jordan. That's great that that's great that your work was able to inspire a colleague to
[Speaker 5] [56:48] That was, like, the nicest thing anyone's ever said to me
[Speaker 4] [56:50] at work.
[Speaker 2] [56:51] It was so nice.
[Speaker 5] [56:53] And also because Luke man's, like, bug report was amazing and had a meme in it. It's like, well, okay. The bar has been raised.
[Speaker 1] [57:00] I thought it has to be I'm totally glad you mentioned the meme. It's not just a meme. It's a Scooby-Doo meme. I think, like, Scooby-Doo is the universal language. It transcends generations.
[Speaker 1] [57:11] My my my own children, I think, aspire to be Scooby-Doo scholars based on the, the intense Scooby-Doo based debate that happens in our household. So I thought the Scooby-Doo meme was just genius.
[Speaker 3] [57:24] Yeah. No. I was trying to figure out. You know, I was like, there's a lot of text here. I need something to break it up.
[Speaker 1] [57:32] Yeah. And you pretty much I mean, I think you you you nailed it. And you've you've raised the bar for all of us, I think, that we to get more more more memes and debugging. But that I think really, really cool stuff. And I thought the think what was also neat is that with both of these, I love the fact that, both of you were doing this in the public.
[Speaker 1] [57:55] You'll mean these are open source projects we're working on, and it must have been neat for both of you to see, you know, we kinda both of these got put out on social media. There are a lot of people interested in it. That must have been gratifying.
[Speaker 3] [58:10] Yeah. It was interesting because I think you had posted it, while I was, like, away from, like, even looking at Twitter or anything.
[Speaker 1] [58:18] And then I come back if I recall correctly.
[Speaker 3] [58:20] Yeah. Yeah. And then I come back, and I was like, oh, this is, like, hundreds of notifications. I'm like, what's going on?
[Speaker 1] [58:26] And what had happened is I had okay. So sorry. I had submitted this to Hacker News
[Speaker 2] [58:32] because I do when I there
[Speaker 1] [58:33] are things like this. I feel like this is the stuff Hacker News should care about. Like, instead of all the there's plenty of stuff that Hacker News cares about that I don't think they should care about. I think, like, people should care about these kinda of bugs. So I always kinda submit these things to Hacker News.
[Speaker 1] [58:49] And in part, you know, looking at a
[Speaker 6] [58:50] I mean, it's its literally hacker news.
[Speaker 1] [58:53] It is literally news for hackers. I'm looking, you had a great hook in it with the chief and unlocked Rusty Seagull. And so you came back to speak a number one story on Hacker News, which probably was what you were expecting.
[Speaker 3] [59:05] No.
[Speaker 1] [59:08] But I thought it was and I know, I thought it was and it, like, it stuck there for hours and which I thought was really awesome, honestly, because I think it's this is the kind of thing, like, this is the kinds of things that we should be broadcasting broadly within our domain. This is everyone's got something to learn from this, and I think you know, this gets us out of kind of, you know, the debates of the day or what have you. And, so I think this is I think it's terrific. I I I was really glad to see. Ultimately, it's like it's kind of like people are responsible for deciding what's important in hackerism, what's not.
[Speaker 1] [59:44] Ultimately, you know and the fact that so many folks gravitated to it, I thought was really cool to see.
[Speaker 3] [59:50] Yeah. I feel like, although I got the inspiration for the title part from was it Steve Slapstick's first response to this when Patrick posted it? He was like, oh, no slash congrats?
[Speaker 1] [01:00:01] Right. Right. Right. Yeah. Which is it being kind of a no no slash congrats.
[Speaker 1] [01:00:07] I mean, it's if it is, and I think, you know, one of the things that actually both of these bugs had in common that I, and I want to understand both of you about this because both of these bugs were more or less dead reproducible, a term that apparently I only I use. Did we have I had this conversation, Adam? I don't
[Speaker 2] [01:00:27] think we've done it on this space. No. But also people, that you've infected with it.
[Speaker 1] [01:00:34] It is yes. It is I am the Typhoid Mary of dead reproducible, and I don't know where I came up with. Jordan, do you use this? Or maybe are you were you previously an author? I think I
[Speaker 5] [01:00:46] do now.
[Speaker 2] [01:00:47] I don't know.
[Speaker 3] [01:00:47] Okay. And possible. Wait. To clarify for the rest of us, what exactly does that mean?
[Speaker 2] [01:00:52] What do you think it means, Luke, when?
[Speaker 3] [01:00:54] Always reproducible? No.
[Speaker 1] [01:00:56] Yes. So there you go. There you go. There you go. It's a way It's an intensifier.
[Speaker 1] [01:01:02] And we are so Okay. But this is one of those things that I was a term that, like, I like, everyone uses this term. And I just and I wanted this is embarrassing. I'm like, I think I want to put it in a tweet about when or the other of your bugs. And I'm like, dead reproducible, hyphen or not.
[Speaker 1] [01:01:20] So I didn't know. Like, do I do with a hyphen or not? And I just wanted to check it out. And so I googled dead reproducible in quotes. And there's, like, this moment of horror where it's, like, there are only 3 pages of results, and they are all me or people I know.
[Speaker 2] [01:01:36] This is, like, the end of the usual suspects. Oh, it's probably it. This is a long con that you have perpetrated against yourself for decades.
[Speaker 1] [01:01:44] Oh, absolutely. And I'm like, what do you what? And then there's this moment of, like, have I had been this, like, the equivalent of, like, having lettuce on my teeth for 25 years?
[Speaker 2] [01:01:55] I mean Nobody said anything.
[Speaker 1] [01:01:57] Nobody said anything. And it's like, is this something, like, oh, no. No. Like, you're dead and reproducible guy. Like, we all think it's weird, but no one wants to say anything.
[Speaker 1] [01:02:06] Like, you would say something. Right? MMM. I hope.
[Speaker 2] [01:02:09] Sure.
[Speaker 1] [01:02:10] Oh, god. No. That's not at all. That's that that's not at all convincing. But so a term that I think it's a useful term as opposed to completely reproducible.
[Speaker 1] [01:02:19] So I'm gonna I would like to say this world. I'm going to continue to use it. I don't care. Furthermore, I know that I apparently sound nuts, but it's its just We'll put
[Speaker 2] [01:02:27] it is on your tombstone.
[Speaker 1] [01:02:28] Please. And it'll be Dead reproducible. Yeah. He's dead reproducible is fine. Reproduce in peace.
[Speaker 1] [01:02:36] Reproduce in peace. Exactly. But I so I do the it is very satisfying when also, when you have a bug that's dead reproducible, there's a there's a solace in it and that you feel like I and I sometimes I have to tell myself, like, if it's dead reproducible, I can debug it. It may take me a very, very, very long time. I may take a very indirect route.
[Speaker 1] [01:02:59] But if it's completely reproducible and I one thing I've I've said before is that bugs may be either psychotic or nonreproducible, but not both. When you have a bug that is psychotic and nonreproducible, that is gonna absolutely brutal. But in general, bugs are either psychotic or nonreproducible. In this case, like, these bugs are pretty gnarly. Both of these bugs are pretty gnarly, but they're reproducible.
[Speaker 1] [01:03:31] Did you think Jordan, Lupin, did you kinda have that solace as well? Like, I did do that help your determination to know, like, if I sit here long enough, I can debug it?
[Speaker 5] [01:03:40] Yes. Totally. I feel like a lot of debugging is very emotional.
[Speaker 1] [01:03:46] Totally.
[Speaker 5] [01:03:47] And and and being able to just reassure myself that there is an answer on the other side, is very useful.
[Speaker 1] [01:03:54] If it is very useful, though. I totally agree that a lot of debugging is emotional. I think that is actually a very pithy way of putting it, Jordan, because I think you're right. It can be really a struggle, especially if you feel like, I'm not making progress. I am, like I'm just, like, taking laps to this problem, and I'm not getting anywhere.
[Speaker 1] [01:04:12] One thing that I tell people is if you've got a problem like that, maybe spend some time and write some tooling. Maybe that's a good time to write some tooling, actually. Because then you can feel like, well, I didn't debug it, but I implemented equals j for the jazz department. You know what I mean? The the're
[Speaker 3] [01:04:29] just ready for the next time.
[Speaker 1] [01:04:31] Yeah. Yeah. You're ready for the next time. But I off I often find that also just in doing that, it feels like I'm doing something, and then it often helps my emotional state as I go back to attack the problem. Jordan, do
[Speaker 2] [01:04:43] you find that to be the case as well?
[Speaker 5] [01:04:46] Yeah. Another thing I've said this a lot publicly, but, in one of the very first CS courses I took, one of the things our professor said was that there is no magic in the course, and that is something I find almost like a mantra, like repeating to myself, like, there is no magic. This is all even if it's very complex and deep and there's years of history here, there it's not magical.
[Speaker 1] [01:05:11] It's all knowable. It's all knowable. No. I totally agree. And I also kinda feel them, like, you also have when you've got a bug and I this is not true for either of these.
[Speaker 1] [01:05:20] But when you got a bug where it's like, these are wildly varying symptoms or these symptoms are crazy. And just knowing, hey. If this is going to be when I figure out when we figure out what's the the the kind of the common strain is across these wild, biggest spread symptoms, it's going to make for a great story. I kinda feel like, wow. Furthermore, I can't wait to understand because there's I feel like and maybe you feel this as well in terms of bugs you can remember where you've got bugs.
[Speaker 1] [01:05:50] Like, this can't possibly be a single issue that is manifesting these wildly disparate symptoms. And then you debug it. You're like, oh, right. Of course. Yes.
[Speaker 1] [01:05:58] That makes sense. And, wow, that's fascinating that this single symptom had the single cause had these wildly different symptoms.
[Speaker 3] [01:06:07] Yeah. Like, in that sense, like, a psych fault that happens every single time, give me those kinds of bugs all the time.
[Speaker 2] [01:06:14] Absolutely. Absolutely.
[Speaker 1] [01:06:17] Yes.
[Speaker 3] [01:06:19] It's, like, so much easier when you have something like
[Speaker 2] [01:06:23] that. No. Rather than the like, 10,000 things happened and then one out of 100 times, we get a sick fault. Right?
[Speaker 5] [01:06:31] Yeah.
[Speaker 1] [01:06:32] Yeah. It is yeah. It's a beauty of, when the compiler fails, it does tend to do so relatively deterministically, which is a real beauty of the power bugs.
[Speaker 3] [01:06:41] Yeah. I mean, like you said, I feel like we can make the tooling better. Like, that's why things like you know, I really like, r, time travel trace, this kind of things. Like, if you can keep it running attached the whole time, and then when you finally run into it, you can finally you can debug backwards. Like, I think that's amazing.
[Speaker 1] [01:07:00] It's amazing. Yeah. And I think the other key the key is that, like, if you've got a problem that's amenable to that, it's great. And I think that the there's not going to be one debugging methodology to rule them all. Like, Jordan, I thought it was interesting that, like, you started in trying one methodology, post form of debugging, and then had to switch, like, that's not going to work.
[Speaker 1] [01:07:18] Like, this doesn't work in this case. I have to move to a different methodology. I have to use in situ debugging for this instead. And, like, we must be flexible about the kind of methodology we use, not any given problem.
[Speaker 5] [01:07:30] Yeah. That was my first time using MDB as a step debugger.
[Speaker 1] [01:07:33] Yeah. It's an interesting. Right?
[Speaker 2] [01:07:35] MMM. MDB and KMDB or just MDB full stop?
[Speaker 5] [01:07:39] I mean, it was KM.
[Speaker 2] [01:07:40] No. Just, just wondering. There was definitely a moment where you were like, why did nobody tell me about this?
[Speaker 1] [01:07:45] You're like
[Speaker 5] [01:07:48] I I might have said that. Well, there one thing that was really nice, was being able to do like, with the breakpoint command, you can give it a command to run every time it hits the breakpoint. So, like, when I was figuring out when I thought the code was looping and not hanging, I found where I was incremented and printed the value there and then just continued, so I didn't have to keep, like, you know, pressing step or whatever. And that was magical.
[Speaker 1] [01:08:18] Yeah. That was cool. And I love the fact that you described that as well, in the in the bug report was great. And, yeah, I think that the know, in situ debugging is when it's useful. It is I think there are a couple of things like this that it's like it's this technique that when it's useful, it's extraordinarily useful, but it's its not useful for every problem.
[Speaker 1] [01:08:39] I mean, it's useful for I certainly feel that way about, like, Adam, I don't know if there are g trace features for that, come to mind on this. I feel that way about anonymous tracing. Anonymous tracing allows us to trace drink boot, which is the kind of thing you don't care about until it saves your life.
[Speaker 2] [01:08:56] Yeah. Similarly, like speculative tracing. Right? Like, for, again, those kinds of, problems that happen one time out of a 100, one time out of a1000. You know, they're maybe not so common, and it's a don't know how many folks have used speculative tracing, but similarly I can't imagine it's that many.
[Speaker 2] [01:09:13] Right? I mean I I I thought you were going
[Speaker 1] [01:09:15] to make some sort of blanket statement about 80% of the people that have used speculative tracing did a bug a problem in these 200 states right now. That may be the case. Alright.
[Speaker 2] [01:09:23] But I still think it's pretty useful.
[Speaker 1] [01:09:25] It's super useful, and I think that the other thing that it is highlights is that the all these things have arisen from the need to debug specific kinds of problems. And I think having your this is why it's so important to debug tooling when you have a bug in front of you because you are much more likely to debug tool to develop tooling that is itself useful when you're debugging a problem because it's the problem that motivated the tooling. So I saw a couple of other folks asking to speak here. I've got, other questions for Jordan Lippmann or your own, war stories, your own thoughts on debugging methodology. But, I don't know if, needing in captivity or Jason want to get in here.
[Speaker 1] [01:10:08] But
[Speaker 2] [01:10:09] Well,
[Speaker 8] [01:10:10] I just from earlier, and I just don't know if I misheard it. I so you're asking about, you know, with the night, you know, with Rusty, how you can do, like, the underscores and everything. And Does do MDB have the ability to put an MDB.
[Speaker 1] [01:10:26] So Does MDB have the ability to put underscores in Well, that's why I was
[Speaker 8] [01:10:31] asking because Robert put it in.
[Speaker 2] [01:10:32] So it's
[Speaker 1] [01:10:33] not Oh my gosh. That's embarrassing. God, for sure, it's the analyzer. And now I'm sorry, Robert. I'm sorry, Robert.
[Speaker 1] [01:10:38] Robert. Jeez. Exactly.
[Speaker 5] [01:10:40] You can
[Speaker 3] [01:10:41] have separators in what was it? C plus 14. They're just the single quote, I think.
[Speaker 1] [01:10:50] So sorry.
[Speaker 3] [01:10:53] Like, as a digit separator, like the underscore and rest. Right? But you can do it in c plus type 14.
[Speaker 1] [01:10:58] Oh, c plus. Yeah. Yeah. Yeah. No.
[Speaker 1] [01:11:00] I did, and I think I also think that you can do that in I mean, I was using kinda I was using, Hello with XC, and I think that there are many c extensions allow that as well. It's just it's its been a really nice thing to have in Rust. It's been it's its one of the one of the nice things that rust lets us have, as Steve is fond of saying.
[Speaker 2] [01:11:20] Yeah. And I will admit that I am such a cave person that I have not used it in any other language.
[Speaker 1] [01:11:27] Well, at this point, I mean, I feel like, I mean, virtually everything I'm doing is in Rust and Yeah. It's kind of a yeah. Exactly. Kind of a're doing a lot of stuff in Rust, obviously. Well, this is great.
[Speaker 1] [01:11:39] I don't know. And and and, again, if I don't know. Other folks have got questions or or or comments, but this was, Jordan Lachman. This was terrific. I I I really enjoyed I obviously really enjoyed reading, both of your write-ups.
[Speaker 1] [01:11:55] I love the fact that Jordan's inspired Luke ones even though they're on totally different subjects. And, you know, I would say that this is an aspect of our culture that we would love others to copy, please. Like, this is, I think we would be well served as a discipline to, encourage one another to debug problems, encourage one another to actually write them up for our both our own understanding and, Jordan, as you said, off the jump, pedagogically, so we can teach others, how to, how to actually debug. So, I Ben, did you have a closing comment you want to get in here? Oh, I was not.
[Speaker 4] [01:12:39] Yeah. I was wondering if, we could hear a little bit about the debugging adventure that I started for you with the UP 2 inserted on, get unchecked.
[Speaker 1] [01:12:49] Oh, yes. The yes. They this was the triple fault. Right? Yep.
[Speaker 1] [01:12:56] I believe. Yeah. This is the Rick is here and was had jumped in on that one. I was not debugging that one. I was, I was definitely a spectator to that one.
[Speaker 1] [01:13:11] I don't know, Brent, if, Rick, if you're in position too just to speak up the details. Ben, had you that was, I guess, you had seen the consequence of that one. But we are super weird in part.
[Speaker 4] [01:13:23] Yeah. So when I implemented this, I had some idea of the chaos that I would produce. Because we have right. That's why I confirmed that it would detect a couple bugs that I detected in other crates. Right?
[Speaker 4] [01:13:36] With this, you know, sort of just sudden sig ill in the middle of your test suite, which is not the best experience. And so I was my actual fear was that people would report this as rust bugs. Like, the compiler broke.
[Speaker 1] [01:13:52] Right. Well, that's not what happened to us. So, yeah, do you want to describe a little bit about the work that you did to introduce the u d 2? I do. And then
[Speaker 4] [01:14:02] Sure. So there's a number of, unsafe APIs, especially in core. And, a significant fraction of them have predicates, which are checkable at run time, but like the whole point of the unsafe function is that it's not checked. And so this has been tossed around in the community for actually a pretty long time that, like, wow, wouldn't it be cool if these were checked in debug mode? Right?
[Speaker 4] [01:14:32] So you write your code, you know, with got unchecked or non-null, you know, new unchecked or something like that, and then, you know, you do the wrong input. And then in release mode, you get undefined behaviour or whatever. Right? But in debug mode, you get a test failure. So crawling through the implementations in core, someone else had come through.
[Speaker 4] [01:14:53] I think it was Ralph? Ralph J, Ralph Young, came through and implemented, little wrapper that instead of launching a panic, in the interest of code size and compile time, would call core intrinsicsabort, which just compiles down to the fastest way to halt the program, which on x86 is just an ud2. So you just get a branch to an ud2. And so I just sprinkle these everywhere that I could think of in core and put up a PR.
[Speaker 1] [01:15:27] And so it should be said that u d 2 is an is defined to be an undefined instruction, and that will generate an if you are on a running as a process, that should generate a sig ill or its equivalent, and you should ideally have something that you can debug. So you've got a core dump. You've got all this the tooling, which is presumably the reason that you want to sprinkle the UT twos everywhere.
[Speaker 4] [01:15:51] So, really, what I wanted to do was produce something which is unambiguously in error. And so, yes, I found it useful because I have my desktop configured to collect cordons whenever anything crashes. So for me, it's super easy to dive into whatever is going on. So I I I found them occasionally useful. I actually I fiddled with the PR a little, trying to see if I could get a workflow down where I could tell people, oh, you just open up GDP, do this.
[Speaker 4] [01:16:18] Right? And you'll get a back trace that'll point you straight into the function that you screwed up in. The back traces are close that you can get on a sort of desktop environment or a hosted environment, but they're not they're not ideal.
[Speaker 1] [01:16:30] But, of course and this is obviously not something you could necessarily know, but we are using Rust in this case in a very, very, very different environment where we are effectively in a bootloader that has no net underneath it. This is very, very, very low level software. This is as we are starting the host CPU and taking it taking executing an undefined instruction, is going to have, a are actually going to what's called the triple fault where the machine is gonna effectively reset. So, Rick, you're here. Do you want to describe know that you and John Gallagher and a bunch of folks were debugging this inside of Oxide?
[Speaker 1] [01:17:09] Do you want to describe kind of what the manifestation of this was?
[Speaker 7] [01:17:13] Yeah. So as Brian just said, we Normally, when you boot an x86 machine, like, it is comes into the reset vector, and that's going to run some startup code at for EFI or BIOS or, you know, whatever your firmware stack is. In our case, we don't do that. So when we come out of the 8, reset vector, we actually jump directly into, Rust code. And in our case, it's a very small bare metal bootloader system called NATO blurs, NATO by dashes.
[Speaker 7] [01:17:50] And because it's extremely minimal, you know, we've been using this for basically doing development work. And so its main feature is, like, it gives you kind of the KMDB style interface, but at a bare metal, you know, ring zero context and has the ability to do things like receive data over x modem so you can load binaries into RAM.
[Speaker 1] [01:18:17] Rick, people may be wondering if they heard you correctly when you said modem. Yes? Modem. Modem. Year of our Lord 2022 modem.
[Speaker 7] [01:18:28] And if you know, this is all happening over a serial port. It's the intent is we want to be able to actually test out the early bring up code for the system. And so this gives us just an initial entry point. But because it was written to be extremely minimal, it skipped some steps. And so some of the steps that it skips are things like loading what's called the IDT or the interrupt descriptor table.
[Speaker 7] [01:18:54] So there's no interrupt handlers because it doesn't generate any interrupts. There's no hardware enabled to run any interrupts.
[Speaker 1] [01:19:01] Or so it takes.
[Speaker 7] [01:19:04] Well, I said interrupts. However, exceptions also go through the IDT. And exceptions are something that can happen, for example, when you run an u d two instruction. So in our case, the way this manifested was if we updated the tool chain for Nablus and you loaded it, it would just hang. You would run certain commands, and it would just hang.
[Speaker 7] [01:19:32] And it wasn't there's no output because literally when you hit the situation, you know, it is the machine is already in an extremely low level state. There's no error handling hooked up. So the machine doesn't have any way to indicate what went wrong. So we spent a fair amount of time just trying to figure out what error path was being hit. Was it spinning in a loop?
[Speaker 7] [01:19:57] Was it waiting for something? Or had it done a triple fault? And, so we had an an a couple of people working different avenues. I was, grabbing the AMD's actual hardware debugging, interface and trying to get the processor to give me information in this situation where it's hung. And the best I could get was all the x86 cores shut down, and it wouldn't tell me why.
[Speaker 7] [01:20:28] But we because we knew that the x86 core shut down, it was pretty good guess that what had happened was a triple fault. So that got us at least going back and instead of because if it was spinning in a loop or something, I should be able to stop the processor and kind of inspect this the architectural state of the processor. And I couldn't do that. So once we knew it was a triple fault, we're like, well, how in the world are you getting a triple fault? Like, we're not generating interrupts.
[Speaker 7] [01:20:57] There's nothing there. And that's when we finally started coming around to, oh, it must be generating an exception. And, you know, it took us quite a while to dig through this and started looking at, disassembly of various instructions and basically encountered this path of in a certain situation, one of the crates we were using had some undefined behaviour, and that was being encoded as a UD2. And when you hit the ud2, it goes to fire the exception handler. It goes which goes to look up in the IDT.
[Speaker 7] [01:21:31] There's no entry in the IDT for the exception handler. So the processor just gives up and turns off.
[Speaker 1] [01:21:39] And, I mean, it's worth saying that this is not necessarily our first thought that we mean, we've got all sorts of things that could be happening that would be much darker. So it this is, and this failure mode is just brutal. In general, the triple failure mode is really unfortunate and brutal, and it is a very difficult failure mode to debug. But, Ricky, you highlighted something else that, actually, I just want to mention briefly. Wasn't the case in I don't think although, actually, Jordan, you mentioned talking about to Josh and Robert about this.
[Speaker 1] [01:22:11] I think that one of the things I love about debugging is that it's a real team sport in that people can explore different avenues in parallel in a way that's kinda much easier than when you're developing software together. I think it's much easier to debug parallel than sometimes develop software in parallel. And, Rick, as you said, like, people were kind of everyone was kind of exploring different hypotheses, on that that triple fault if I recall correctly.
[Speaker 7] [01:22:37] Yeah. I mean, we because we couldn't inspect the machine in that state. Right? I was kinda the only person who really equipped to do that. Other people were just looking at various Cohen outputs, trying to compare between builds that seemed to work fine and builds that didn't to see what functions were different.
[Speaker 7] [01:22:57] Of course, when you change the compiler version, all the functions look different. So that didn't really help narrow things down. And so, yeah, there were just a bunch of different avenues. Honestly, on our bingo card, undefined behaviour in a crate that we depended upon was pretty low on the list.
[Speaker 1] [01:23:15] Pretty low on the list. I mean, it's a relief, honestly. It's the best possible answer, because it is its something that we could definitely fix in lots of different ways. But, yeah, it was low. I was surprised.
[Speaker 1] [01:23:26] It was low on the list. It actually was one of these that we're just talking about earlier about, like, you know, how do you get from there to there? And, Ben, have you were you surprised to see, the kind of the manifestations of this be and in terms of how we hit this.
[Speaker 4] [01:23:45] Not particularly. I was Alright. I was a little bit surprised that I mean, just my priors maybe, but I was surprised that I only heard about it after it was fixed, not the screaming in pain as attempting to debug it.
[Speaker 1] [01:24:02] Yeah. Well, we know, we're very used to being self-sufficient in this regard. So and, actually but I have to say, I one thing I really appreciated in this is, that when you that you kinda volunteered, like, hey. This is sorry. I introduced this, and, I want to help.
[Speaker 1] [01:24:19] I want to understand, like, what the failure mode was. And I honestly, that felt great from our perspective just to, you know, I think debugging is so needs to be so collaborative. And, you know, obviously, this was, a change that you're making that was very well-intentioned and had very surprising ramifications. And also did, I mean, point us to I mean, it should be said. Like, the the the root cause is really the fact that we had this crate that was doing something it shouldn't be doing.
[Speaker 1] [01:24:49] Yes. Maybe this shouldn't be a capital crime for the program, but, that was the actual fix, was to fix HELPS. And I think we ended up fixing that. Greg, if I recall correctly, we ended up making, finding a couple of other issues and fixing or I think we end up looking at the heapless dependency carefully. Maybe that's the best way to say that.
[Speaker 7] [01:25:09] So John Gallagher started running Nanolux's builds under oh, there's a tool that that looks specifically for, undefined behaviour type issues. I can't remember the name of it. So
[Speaker 4] [01:25:27] I'm also a MINI contributor.
[Speaker 2] [01:25:30] Oh, yeah.
[Speaker 4] [01:25:32] Yeah. So of particular interest, if you're is you're intensive users of MINI, I finally, managed to merge a PR this weekend. I don't know when it will appear in Rust Knightly. That significantly enhances the diagnostics when it tells you about a stacked borrows' error.
[Speaker 1] [01:25:51] Oh, that's awesome.
[Speaker 4] [01:25:53] If you have any sorts of feedback on MINI, one of the biggest problems is the core MINI contributors are seriously starved for feedback from users or the community in general. So whatever you have, however you can send it to me, issues, Twitter, would be great.
[Speaker 1] [01:26:10] Oh, I do will do. That's great. That is great to hear. And that's, I mean, I I I think Mary played a mean, played a very load bearing role in this, in John's analysis of this. So, and, they pointed us to the undefined behaviour that we need to go fix.
[Speaker 7] [01:26:27] Yeah. And to be fair, this also pointed to we, we really should implement an IDT and specifically an exception handler to catch and dump the state to the UART?
[Speaker 1] [01:26:40] Yeah. I think of it. There's kind of another object that's in there too, isn't it, Rick? But the sometimes you think, like, this shouldn't happen. And so, well, I don't really need to handle it.
[Speaker 1] [01:26:48] Like, well, if it shouldn't happen, like, all the more reason to put something in there that is going to make it very clear that it has happened, because it if you don't, the the the consequences of get the consequence of taking a fall without an IDT are pretty great for Next eighty 6. And as I recall, I think, that I'll also inspire Dan Cross to add to NATO blurs an actual like, an IDT that actually does a register dump, if I recall correctly. So if we see this again, we will see, I mean, well it is will be night and day in terms of being able to debug where this is coming from.
[Speaker 7] [01:27:24] Exactly. Yeah. And, I mean, this all kinda came into, let's go spend some time to update Nanolux to the latest tool chain and, you know, see what other problems we have lurking because we've just been lucky, and we got away with it for a long time. But now that we know we're not quite as lucky anymore, let's let's go in and put in some of the infrastructure so that we know when something goes wrong.
[Speaker 1] [01:27:47] Yeah. I mean, honestly, Ben, your work did ultimately, like, really improve the system. Yeah. It improved our own failure mode in this case. It improved our use of p plus for sure.
[Speaker 1] [01:27:57] So, it's good stuff. And, thanks again for your work on it and for Mary as well. It was, it's been really valuable stuff.
[Speaker 4] [01:28:09] Yeah. Always, always glad to hear your work's appreciated. Thanks.
[Speaker 1] [01:28:13] Yeah. That and that was a good one. That was another fun one. I I I do, it's so again, not one that I actively participated in, but it was really fun to watch people different people investigating different hypothesis, going different directions, and then finally getting that one to total and complete understanding. And, Rick, great work from you and John Gallagher and a bunch of other folks that that were working on that one.
[Speaker 1] [01:28:37] And, Luke, I feel like you were in on that one as well. I feel like there 's's again, there's, like, the disturbance of the force whenever there's a whenever Rust is involved, then you're often, in there with
[Speaker 3] [01:28:48] I think it was very limited. That one maybe just, like, which it was something like which commit broke something or something like that, but very limited.
[Speaker 1] [01:28:56] I another thing that I also did just maybe to close on, I think that one aspect of this is and, yes, we've been using IRC forever, but especially in this all remote world, we use chat a lot for debugging. And, you know, Luke, when you said mentioned this earlier that, like, you are able to kinda lurk when someone's debugging and then be able to find ways to help. I also think that when people are talking about the problems they're hitting and how they're debugging them in chat, it's it can be a good way for other people to see and and and help out. And it's changed the way we debug software for sure. Alright.
[Speaker 1] [01:29:36] I know Adam has gone off to, Adam's let the recording run, but I know he yes. Oh, there you go. Adam, you're here.
[Speaker 2] [01:29:41] I'm here. I'm here. I'm listening to the law, you know, negotiating with the toddler, but still here.
[Speaker 1] [01:29:46] And that's what what the toddler is so supports us adding an IDT to NanoBorders, I assume?
[Speaker 2] [01:29:53] He's, he's ambivalent, I
[Speaker 1] [01:29:55] would say. Right. Exactly. Well, you tell him he can debug the next problem where we have. We'll do that.
[Speaker 2] [01:30:02] That's a good idea.
[Speaker 1] [01:30:03] Yep. Awesome. Well, this has been really great. Jordan, Lupin, thank you so much for this. And Josh, Rick, thank you.
[Speaker 1] [01:30:12] And Ben, thanks for your work on Murry. It's been, a lot of fun to talk. Debugging methodology is a subject that is near and dear to our hearts, so, always fun to compare notes.