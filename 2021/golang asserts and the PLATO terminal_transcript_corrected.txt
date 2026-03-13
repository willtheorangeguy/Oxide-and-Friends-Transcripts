[Speaker 1] [00:00] With it. Because if we give it to you, you'll write confusing software. And I'm, like, oh, what makes it confusing? And it's, like, oh, well, you'd have to read it. And, like, it might be, like, syntax heavy.
[Speaker 1] [00:09] And I'm like, oh, I don't know. Like, I don't want any of that. Like, I don't like, none no part of me wants someone taking those choices from me and going, hey, kid. You're not smart enough to solve that problem. And, like, it just it drives me insane, and it makes me want to bite my fingernails off.
[Speaker 1] [00:26] And so, like, I just I will avoid it with, like, all of my ability, except sometimes when I'm like, okay. The right thing to do is to, like, use this language because the overwhelming amount of software in that space is written in that language or there's an overwhelming number of libraries and, like, you know, Chef wrote a lot I'm not sure if I'd have made that same decision because I just it drives me insane because I dislike that piece. And there are other people, Mitchell Hashimoto, for example, who I know loves that piece of it. He's like, yeah. I feel like that's great advice.
[Speaker 1] [01:05] We shouldn't do those things. People who do those things are bad people. And this is not the way, and I'm like, god bless you. Like, go on with it. But I think it's got nothing to do with language design.
[Speaker 1] [01:14] It's not about what's right or wrong. It's all about, like, do you want someone to tell you what's safe and good? If so, man,
[Speaker 2] [01:31] a second. Adam, I think there was when I approached Go, I think I saw, some things that I really liked that I hadn't seen. Like, I I I sort of grew up on c and some Java, and I liked the sort of snugness. I liked the opinionatedness of Go. And then to your point, some of those opinions, I just really disagreed with.
[Speaker 2] [01:53] So I I I found novelty in the strictures, but just, like, objected to some of the specifics.
[Speaker 3] [02:00] Well and I think it's so interesting because, Adam, to your point, and, Adam, to your point about Go as well. The fact that, like, Rust safety is so important for Rust. And yet even Rust is like, hey. Here's a here is actually an unsafe keyword, and you can actually remove not all of these structures, but many of them. And Rust allows you to do unsafe things in a language that that is built around safety.
[Speaker 3] [02:24] I mean, that is a lot of trust in the programmer. And at the same time, Rust also I mean, I Rust, I and Adam, I think if I feel the same way about you know, when I'm writing code, it's its a part of my expression. And there's freedom of expression there that is really important to me. And I feel like when you got a language, like, why will you go not trust me, the programmer, with asserts? Like, if I yes.
[Speaker 3] [02:53] I can abuse them. I can abuse lots of things. And it is you know what I mean? It's like it is feels like I'm not being trusted with my own craft.
[Speaker 1] [03:01] Yeah. That's because you're not. Like Right. And, like, Elm is Elm does the same thing. Like, hey.
[Speaker 1] [03:08] I'd like to write, like, a new, like, custom thing. And they're like, okay. Well, you can do it through ports, or you can get special dispensation from the god king of Elm. And I'm like, as soon as I saw that, like, oh my god. I have to appeal to the god king of Elm.
[Speaker 1] [03:22] Like, I was like, oh, fuck Elm. Like, I can't, I can't hang out with this at all. And, like, even though, like, it's definitely speaking to me, like, as an engineer, I'm like, oh, Elm, that looks perfect. Like, that's like a hot tub for me. This is a catnip, But, like, nope.
[Speaker 1] [03:36] Can't do it because God King has to say it's okay. And I'm like, nope. I'm out. Done. Can't hang out with you.
[Speaker 1] [03:42] Gotta go.
[Speaker 3] [03:44] Yeah. There is something, like, the God King is a turn-off, isn't it? I at least for me, maybe. But for some people, it's a turn on, I guess. I guess that's what your point Yes.
[Speaker 1] [03:51] For some people, they really like it. They're, like, oh, yes, please.
[Speaker 3] [03:54] Oh, thank god. God king is here. God king is here. Tell us what to do.
[Speaker 1] [03:57] Especially in Go, like, the God king is very impressive. Like, no part of me believes I'm a better programmer than the people who are telling me what I should and shouldn't do in Go. Those guys are great. They are uniformly stellar software developers.
[Speaker 3] [04:11] Okay. So they okay.
[Speaker 1] [04:12] And then they might not be, like, whatever in the grand pantheon of software developers. I'm sure there's better software developers, but, like, there are no slouches. It's not their first rodeo. Like, like, they're they're, like, entitled to their opinion or whatnot, you know? Like, but
[Speaker 4] [04:28] But if your first rodeo was planned 9 o s.
[Speaker 3] [04:32] That's okay. Well,
[Speaker 1] [04:33] yes. That was their second rodeo, to
[Speaker 3] [04:36] be fair. So this is where I do get, like, I feel that sometimes and okay. Like, look. I'm probably as guilty as anyone. I think we overly lionize UNIX a little bit.
[Speaker 3] [04:45] And in that, like, there's so much that's important about UNIX.
[Speaker 1] [04:48] As the UNIX superhero.
[Speaker 3] [04:50] Oh, okay. Is is that is that who I am? You'm just I'm just a man.
[Speaker 1] [04:55] You're many you're many things. But, yeah, you are you definitely have, like, a fucking Trace cape.
[Speaker 3] [05:01] Okay. But am I like, I hope that I have I probably have, like, overly lionized UNIX. I think UNIX is extremely important, but Unix as an actual engineering artifact was left a lot of room to be improved. Like, a lot of room to improved. Like, so much room to be improved that it took us, like, decades to actually get it fucking working.
[Speaker 3] [05:22] And, I mean, if you look at, like, 7th edition. Like, 7th edition is, like, it is it's its amazing, and it's incredible, and it's a breakthrough, and it's also, like, kind of shitty engineering artifact that needed a lot of work.
[Speaker 5] [05:35] Totally. Yeah. We so we're talking about asserts here. Right? And, like, one of the things is tearing down threads is a mess in almost every single run time out there.
[Speaker 5] [05:44] It's like what cert is going to go and do for you? But to drop a little kind of bomb into the conversation, there's a search in the Go standard in the implementation. Right? It's just a hand rolled assert for their own purposes. And I mean, I don't know who write that Wiki entry.
[Speaker 5] [06:02] Right? It might be the core team, or it might just be some random person, but, like, you can find a Hash c Wiki from free node and just, like, it's full of stuff. So, like, is the assert you know, we were talking earlier about, like, do you want a supervisor system or a thing that takes the process down? And you could implement your assert as OS exit, which is just going to tear the process down, not run any callback or anything else. Or you could implement it as panicked and do a supervisor.
[Speaker 5] [06:29] So, like, which one do you want?
[Speaker 3] [06:33] Or take a fucking core dump. I know that, like, this is where I I I don't know. I mean, Adam, this is where I do feel like I maybe wake her crazy because I feel that not many not the very best way to debug an errand system is to take a snapshot of system state and debug how you got into this errand state. And that snapshot state is called the core dump. And I feel we have failed because this is not something that many people do.
[Speaker 4] [06:59] I've had Had you ever tried to debug a Go core dump?
[Speaker 6] [07:02] I'd, I'd like to interject and, mention 2 brief SAS because I know we are on the Twitter spaces cap limit, and I'd like to take myself off the PSA. And I actually think it's, like, such a timely moment to mention this, with respect to core downs and snapshots. So PSA number 1 is that, today is, Alan Kay's 81st birthday.
[Speaker 3] [07:30] Wow.
[Speaker 6] [07:31] So Alan Kay did the small talk and also Yearbook. So, I
[Speaker 3] [07:37] Can I say on this moment, thank you for the Alan Kaye's wife also wrote Iron? Did anybody know that? I learned that yesterday.
[Speaker 6] [07:44] So there is this video that Alan Kay made to celebrate Ted Nelson's there was this event that they celebrated Ted Nelson's, and, Alan Kaye couldn't make it. And, Steve Wozniak, was physically present there. And instead of Alan Kaye dubbed, but Alan Kaye, recorded the video. And in the video, there is Alan Kaye and Alan Kaye's wife, and Alan Kaye's wife Alan Kaye's wife, describes how Iron was, typesetter on, Alta, I think, or something similar
[Speaker 1] [08:20] to that. I like that.
[Speaker 3] [08:21] Oh. I don't I don't You are blowing my mind. I thought my mind was blown when I learned this fact yesterday, and you are really detonating my mind. So Chuan was typeset on Alto?
[Speaker 6] [08:33] It's something like that. It's probably the first, what is it? Like, the film manuscript or what do they call the ones that they type in monospaced?
[Speaker 3] [08:45] Right. In the so are you actually I even know the scene they're talking. So for I don't think Iron's a great
[Speaker 6] [08:50] I've never liked Iron, so that's, like, the weird thing to talk to.
[Speaker 3] [08:54] But the light bikes are awesome. But, Adam, have you what is the last time you watch
[Speaker 2] [08:58] Iron? Me.
[Speaker 3] [08:59] Either either either Adam.
[Speaker 2] [09:00] Never.
[Speaker 3] [09:02] Adam Jacob, you watch Iron?
[Speaker 1] [09:03] So many times when I was a one of my earliest memories was, like, in, like, a daycare when I was, like, pre 1st grade. And they would take us to the movies, like, twice a week. And because it was clearly a very different era. And and and, like, and Iron was the only movie for, like, months. And so, like, that that is burned into my early memories the same way that, like, Mount Saint Helens exploding is burned into my memory.
[Speaker 3] [09:32] Is there a way that I can be assured that you and I will be in the same gen x retirement home, Adam? Because I just I I I could the story warms my heart. Yeah. The so, Nemo, I'm sorry. I didn't mean to sidetrack you on Iron, although you, because I know you got you had something else you wanted to say.
[Speaker 3] [09:48] That is just that is amazing, though. I can't get over so, Adam, I don't think Iron is that good at movie, though, is what I wanted to
[Speaker 1] [09:55] no. No. I mean, like, canonically good as a film. Like, I mean, way ahead of the time in visual effects or whatever. But, like
[Speaker 3] [10:03] Totally.
[Speaker 1] [10:03] But, like, you know, was Mary was, like, Bread knobs and Broomsticks a very good movie? Not really, but it did have, like, Angela Lansbury and a bunch of, like, knights. You know, like, it's pretty good. And there's, like, that weird animated segment in the middle where they, like, play soccer. It's pretty cool.
[Speaker 6] [10:19] Well, I guess my I guess my stack is pretty limited. So if you wanna pop the topic, we get back to Alan k's wife.
[Speaker 1] [10:29] So Alan k brought up
[Speaker 6] [10:30] in Ted Nelson's in the video that Alan k made, to celebrate Ted Nelson, Alan Kaye's wife, is, laying on the ground holding a copy of, Computer Lip Dream Machines, which is a book that Ted Nelson wrote and is very celebrated. And it's like a double book. So it's shot at in 2 scenes. Alan Kaye's wife is laying on the ground, reading it from left to right, and then and, you have to watch the video. So in any case, it's like it's like
[Speaker 3] [11:05] it's And that is in Iron? Alan Kay's wife is also she didn't know write Iron, but she's actually in Iron.
[Speaker 6] [11:11] I don't know about that. But it just it is happens to be that the story about typesetting Iron was how Alan Kay's wife and Alan Kay met.
[Speaker 3] [11:21] Adam Jacob, did you know this?
[Speaker 6] [11:23] No. So that's why No. No. No.
[Speaker 3] [11:24] Not at all. I mean, your mind has to be blowing up on this. Yeah. Okay.
[Speaker 6] [11:28] Really, really like Alan Kaye.
[Speaker 1] [11:30] Like, I
[Speaker 6] [11:30] feel It's really not a video that Alan Kaye made for Ted Nelson. It's a video that they made to say thank you, Ted Nelson, that you are pretty much the reason that we got to know each other because, apparently, Ted Nelson also had to do something with the transcript or something. Alan
[Speaker 1] [11:48] k is the perfect example, though, of the anti go. Like, Alan k, like, small talk, everything was open. And that's what made it great. It was like, yeah. You could do crazy stuff.
[Speaker 1] [11:57] And then, like, the crazy stuff could destroy the whole thing.
[Speaker 3] [11:59] But, like, but Yeah. Interesting.
[Speaker 1] [12:01] But, boy, like, the art of it was, like, fully expressed. You know? Like, Alan Kaye was never going to be like, oh, don't do that. That's too artistic. Like, that's too out of the bounds.
[Speaker 1] [12:11] Like yeah. And, anyway,
[Speaker 6] [12:14] I guess, yeah, I don't know, like, how to wrap the first PSA up, but, so happy Alan k's 85th birthday to everybody who celebrates small talk and snapshots and Dino Book and Trace and Swift Playgrounds. And the second PSA is that today is the tax deadline
[Speaker 3] [12:33] day.
[Speaker 6] [12:33] So if you're, demand or something, please do that. And, like, I would take myself off from the speakers because, like, somebody else should probably join it.
[Speaker 3] [12:45] So It is Lima, those are 2 very good SAS. I do love the fact that you're like, look. I'm with a bunch of software engineers, so you have to get these in the right priority order. And the top priority is, like, we have to talk about Alan Kay's 81st birthday, and then, like, yeah, I'll
[Speaker 6] [12:56] talk about You folks are talking about the snapshots on core DOM's, and I was like, a small talk is sound was relevant here. So
[Speaker 3] [13:05] So I ran across and then, Lima, thank you so much for expanding on the role of that Iron introduced Alan Kay to his wife. The, I ran across that fact just yesterday in the'm reading The Friendly Orange Glow by Brian Deer. Have you read this, Adam, on Plato?
[Speaker 2] [13:23] No. I haven't.
[Speaker 3] [13:25] It's an amazing book. I have to say it is well written, and the PLATO history is crazy. It is just like Internet alternate timeline. Do you know anything about Play Doh?
[Speaker 2] [13:37] No. No. Very little.
[Speaker 3] [13:38] So it says this is the system developed at the University of Illinois, in the seventies. And it's basically a network system that is quite literally, like, 15 years plus ahead of its time.
[Speaker 4] [13:51] I don't think they caught it until Khan Academy.
[Speaker 3] [13:56] Right. Right. No. That's right. So what Aaron is saying is, like, that we did not get to the point where PLATO, so PLATO is actually designed to be a pedagogical system, in part because that's the way they could get funding for this stuff.
[Speaker 3] [14:07] And just like breakthrough display technology. So they had the 512 by 512 at a time when, like I mean, that was way, way ahead of anything else. Plasma technology. And, anyway, this book, The Friendly Orange Glow, is, about, at this point, maybe what, 3 quarters of 3rd. And I knew about Plato from reading about, about CDC, the about control data, and their very strange CEO.
[Speaker 3] [14:37] But, anyway, that's how I ran across the the'll put a link to that in the in our Twitter space show notes, but highly recommended. It's a very good
[Speaker 5] [14:46] book.
[Speaker 7] [14:48] You just blew my mind with the PLAY Doh reference. I worked on Play Doh back in the what, early eighties, late seventies. I'm in all four. Furthermore, I don't even know why I'm on this call with you guys. Furthermore, I love you.
[Speaker 7] [15:03] You're all so passionate, so I just like to listen. But, Brian, you just blew me away.
[Speaker 3] [15:08] Oh, no. Bob, you blew me away. So tell me so tell me about it. How did you get exposed to Play Doh? Tell me all about it.
[Speaker 7] [15:13] Oh my god. Well, so
[Speaker 3] [15:21] Oh, did Twitter Spaces mute you, Bob? Is why? Back.
[Speaker 7] [15:26] I saw high school in the late seventies. Right? And my computing experience is a wrists PDP 11, which we would like dial into it, 300 board with a, you know, decorator teleprinter. But, I completely got hooked on computers in 11th grade through this experience, and I was an electronics geek even before that and stuff. But, anyway
[Speaker 3] [15:54] And, Bob, where did you grow up? Where are you going to high school?
[Speaker 7] [15:57] Wilmington, Delaware.
[Speaker 3] [15:58] Wilmington. Oh, okay. So this is the University of Delaware system. It's actually
[Speaker 7] [16:02] University of Delaware PLATO system that I'm Yeah. To. But the University of Delaware also hosted a time-sharing system for all the high schools in the State of Delaware. And that's where I really got my start on computers. You know, it was like some math class where it's like, okay.
[Speaker 7] [16:19] You can, you know, write a basic program to print out prime numbers or something. And, like, you know, my second day on the thing, I was like, how do I, like, hack into the operating system and figure out all the system calls?
[Speaker 3] [16:33] And so have you read Brian Deer's book? It came out about 2 years ago.
[Speaker 7] [16:38] No. What book?
[Speaker 3] [16:39] It's called the friendly orange glow. You're gonna I mean
[Speaker 7] [16:42] Oh, yeah. So yeah. I I I I will check it out for sure.
[Speaker 8] [16:48] Hey. Hey, Brian. Tom here. I
[Speaker 3] [16:51] Hey, Tom.
[Speaker 8] [16:52] I have a copy of the book that I haven't managed to read yet, but I did get to use the PLATO terminal way back around 75 or 76. They had it at Cornell, and I was visiting my brother there. And
[Speaker 3] [17:06] Of course. God, its god, Tom. It's like you're quite is this the same brother or is this a different
[Speaker 8] [17:11] Brother number 17 or whatever. But, yeah, one of the cool things about the Pueblo terminal is, you know, there's limited bandwidth even though they had the dot matrix screen. And I think Cornell's host was actually somewhere else, probably Illinois, but it just had this terminal. But some of the terminals had a facility where you could feed 35 millimetre slides into it and the program could select to display a slide.
[Speaker 3] [17:41] That's the PLATO 4 terminal has that. Yeah. They talk about that quite a bit.
[Speaker 8] [17:45] That's right.
[Speaker 3] [17:46] And I and so, Tom, when you saw this, I mean, that must it must have been mind-blowing to see this when you saw it. And, I mean, Bob, obviously, it was mind-blowing for you because it was your first computing experience. But I imagine it I mean, that sounds way ahead of its time in the seventies.
[Speaker 7] [18:02] Oh, oh, it was. No. My first computing experience was, like, on a teletype. When I saw, like, a bit mapped graphics display in, you know, 1979, I'm like, woah, baby. And, like, not just one, but a room full of them.
[Speaker 7] [18:17] You know? They were all, like, hooked up to some CDC mainframe or something. And they had, like, rooms full of them at the education department of U of D.
[Speaker 3] [18:27] Well, so
[Speaker 8] [18:27] the my first bitmap display was at Bell Labs in 1973, and that's that's not when I was working. That's when my other brother was working there. But they had these plasma displays, and they were flat. You know? So you look at the front.
[Speaker 8] [18:46] It's very cool. When you look at the back, and it's the same thing. It was just a screen. You could see both sides.
[Speaker 7] [18:54] The orange bow. Yeah.
[Speaker 3] [18:55] It's the orange bow. Yeah. What and they're Bob, you're gonna really love this book, and I'm sure you're gonna there they David Graeber at the University of Delaware plays a an important role in the book. But the book is very well researched and well written, which I feel is, like, unusual just in general. And it's been I
[Speaker 7] [19:17] don't I don't remember the name, but he might be one of the people who was, like, chasing me out of the room saying, what are you high school kids doing?
[Speaker 3] [19:25] Well, and so it's funny. This is why you're really going to like the book because that's a real theme of the book is all the high scores at in both Delaware and in Illinois that are exposed to computing via PLATO and how they are having to, like, sneak time onto these systems and, you know, all the hi jinks. And they talked about one lab where people would go into the would hide in the physically hide in the lab and wait for it to be closed so they could get compute time.
[Speaker 7] [19:53] Oh, yeah. All of that was going on for sure.
[Speaker 3] [19:56] And so did you I have to ask. Did you play Empire or Aviator? Is that the other one? What's the other one? Aviator?
[Speaker 3] [20:03] Is that the other one? The other one? No.
[Speaker 7] [20:05] I was all about writing my own lessons. I wrote my own lessons, like, on crazy stuff, like, you know, how to hack the elevators in Smith Hall.
[Speaker 3] [20:16] My god. Oh my god.
[Speaker 7] [20:18] It's just crazy, nutty stuff.
[Speaker 3] [20:20] So do you so I think one of the things that's that's, and it's tough in the book is that a lot of the stuff is just lost because their storage was so finite that things would just get
[Speaker 7] [20:30] I have it from before, like, 10 years after that.
[Speaker 3] [20:34] Yeah. Wow. And so, Bob, you wrote in tutor then. Right? That was the language.
[Speaker 3] [20:39] Yeah. So tell me about tutor because there's not, like, a lot on you kinda mentioned tutor, but, like, what's the analog to tutor today? It seems like a very educated tutor.
[Speaker 7] [20:50] I mean, I'm not, like, a language compiler guy. Like, I heard all you guys on the call, so I'm probably not going to do justice to that question. But, I mean, at that point, my only computer language experience was basic. You know? Line 10 print, line, you know, blah blah.
[Speaker 7] [21:13] And, you know, like Dartmouth, blah blah, on the deck minicomputer. But it is, I don't know. Was it object-oriented? I don't even remember.
[Speaker 3] [21:24] It from all the snapshots I can find, if I'm like, I don't see how you build anything powerful in this language, and yet people built very powerful things. I do not understand it. I'd like to understand a little it looks like basic and snowball had a baby. It just looks very strange to me. But the is it's also like it's its kind of in that pre c class of languages that just look antediluvian to the modern eye.
[Speaker 3] [21:51] And I but, clearly, it's incredibly powerful because people built lots of interesting things.
[Speaker 7] [21:56] Well, you know, it was kinda crazy different time because, you know, you're on computers with so few resources. I mean, you know, you didn't have, like, all the memory and stuff. You know? Nobody was talking about, like, garbage collection or anything because you had to, you know, just love every precious white you had.
[Speaker 3] [22:18] Well and I think, you know, one of the things that that came out in is come out in so many of our conversations in On the Metal and our the oxide podcast is how much those resource constraints, resulted in creativity. And I think that, like, actually, we do our more creative engineering when we have those constraints. Certainly, I don't know, Adam, I don't know I don't know how you feel. I certainly we feel that at Oxide where we are dealing with some embedded systems that have got very tight constraints and have to be very creative as a result. But it's amazing what was done on this.
[Speaker 3] [22:50] And so, Bob, you're gonna love this book. You the the the are gonna just because the book is about not just the technical advances of Plato, but then about the all the social dynamic of this kind of primordial Internet and how, you know, people are publishing online for the first time. It's its it's really, fascinating.
[Speaker 2] [23:11] Brian, on that topic, this David Graeber, have you stumbled across his blog that started in 1977?
[Speaker 3] [23:18] No. I haven't. I've only I haven't even Googled him. Is it
[Speaker 2] [23:23] I have fallen all the way down this rabbit hole.
[Speaker 3] [23:26] Oh my god. Is that where you've been for the last 20 minutes?
[Speaker 6] [23:28] Oh my god.
[Speaker 2] [23:28] It it's its some of this anti-war stuff. It is it is there's its deep. It's deep. Furthermore, it's great. Furthermore, it's going to be in the show notes for sure, but it's on grapenotes.com.
[Speaker 2] [23:40] And it's stuff that he was writing on the Play Doh in the late seventies, early eighties. It's its pretty interesting.
[Speaker 3] [23:47] Well, that's great that actually because I it's great that that's been preserved because they are they one of the again, the persistent themes are they've got such a finite amount of storage. They're constantly, like, deleting things. And then when they delete these things, there are no hard copies, and they're just gone. And so there was this news service effectively that was run for and, Bob, maybe you remember this, run out of the U of I for 2 years in the late seventies. That was, like, it for news.
[Speaker 3] [24:12] And it was this, like, first online news, and they're, like, they're scooping the the, the paper, the Killing paper there at the U of And then, but they were they're constantly having to delete articles to make room. So it's grapenotes.com, Adam?
[Speaker 2] [24:29] Yeah. Grape Notes. But this is doctor David Graeber. Right?
[Speaker 3] [24:34] Yes. That's it. Oh, I got it. Make sure. I get it.
[Speaker 3] [24:37] Yeah. I get it. Yeah. Yeah. Well, I will have to go well, we'll have to go check it out with the Yeah.
[Speaker 3] [24:41] And, Bob, you're going to have to check out the book and, so, Tom, did your brother end up actually doing anything on the Plano? Or did
[Speaker 8] [24:50] No. They were just there. I don't think he ever did much with him. So
[Speaker 3] [24:55] Because I would love that you'll be interesting to kinda compare and contrast the PLATO experience with the Xerox PARC Alto experience, which I gather was a similar kind of, like Tom, you've described it as, like, all of a sudden, I'm looking into the future. It'd be interesting to kinda compare and contrast those two experiences.
[Speaker 8] [25:11] Yeah. That, I mean, the Alto was much more of what we believe it to be a computer The Plato is saying was a terminal
[Speaker 3] [25:19] Was a terminal. Yeah. Well, I think it is kinda goes back to, like, the the what we're talking about earlier in terms of I do feel that, like, and I'm excited to kinda finish this book up and get Brian Deer's perspective on it. But PLATO was very, very centralized, and you do wonder if that was part of the know, the Internet took off because it was decentralized. That and it couldn't have worked if it had been centralized.
[Speaker 3] [25:43] And by
[Speaker 4] [25:43] the way, I know was vector graphics. Was alto pixels or vectors?
[Speaker 8] [25:48] No. PLATO was pixels.
[Speaker 3] [25:50] Yeah. But PLATO's bitmap.
[Speaker 8] [25:52] Physically, it has pixels, but I don't know what the programming model was.
[Speaker 3] [25:58] The programming model is very, very like, it's very coordinate based. It is not vector based. From what I can see,
[Speaker 8] [26:05] I'm tutoring, and they have quite a few Play Doh manuals about the hardware and stuff.
[Speaker 3] [26:11] So And I'm sure and there's going to be a when we these systems we love in Minneapolis, I was hoping to get an an a Play Doh talk. This is before the book was published. Now, of course, the book is, and the book is very is well documented, and there are so many notes in there. And, Bob, you are gonna if you go to the acknowledgments of this book, you are absolutely going to see people you knew because, he has clearly spoken with so many people who use the system.
[Speaker 7] [26:36] I'm going to get the book for sure.
[Speaker 3] [26:39] Yeah. I'll say I know you have to come back and tell us what you think and explain about it with with with some stories. So I've been we've been trying to hold this to about an hour, so I think we will probably wind it up here before we, before Twitter Spaces dies on me again. Adam, did we get I hope we got a recording of this.
[Speaker 2] [27:00] The we definitely the the part, which was the gold part rather than me just, you know, rereading the go statement on asserts over and over again. This part, I'm pretty sure we got. Alright. And, but, so this has been awesome. And I'd say next week, should we plug, Silicon Cowboys?
[Speaker 2] [27:18] Is that the plan?
[Speaker 3] [27:19] Yeah. I think we should. Yeah. I think the plan is to talk about Silicon Cowboys next week. So, the Silicon Cowboys is a documentary.
[Speaker 3] [27:29] If you try to watch Halt and Catch Fire so Halt and Catch I wanted to sit down and watch Halt and Catch Fire. I talked to my 13-year-old into watching it with me. But a lot of sex was breaking out in Halt and Catch Fire. It got to the point, like, in you know, we're not, like, so prudish with my my my 13-year-old definitely knows the birds and the bees, but he's definitely, like, we got a couple episodes in. He's like, dad, can we watch something else?
[Speaker 3] [27:49] Just a lot of sex in this. I'm like, there is a lot of sex in this supposed drama about a computer company. Like, a lot of sex breaks out. And the Halt and Catch Fire is based on the rise of Compaq, which is captured in this documentary called Silicon Cowboys, which and, Adam, I gather you watched it over the weekend.
[Speaker 2] [28:07] It was awesome. And It
[Speaker 3] [28:08] was a great yeah. It was good.
[Speaker 2] [28:09] So if you love Halt and Catch Fire, but hate sex.
[Speaker 3] [28:13] That's right. Yeah. Exactly.
[Speaker 1] [28:15] Or if
[Speaker 3] [28:15] you want to watch Halt and Get Fired with your kids. The I thought it was better than Halt and Get Fired in part because it's all true. The story of compact is amazing, but, we'll plug that. If people want to watch that, well we'll talk about that next time among other things.
[Speaker 7] [28:27] I have to come back next week now because I can tell you about my time at Compact.
[Speaker 3] [28:31] Yeah. Oh. Oh, there you go. That's a good teaser. Bob, you just delivered the goods.
[Speaker 3] [28:36] Alright. You got to come back and tell us about Compaq. Another quick plug is to read Rod Canyon's book, called Open on I mean, I think Compaq's a fascinating company. And Bob, you're going to have to give us your take when you come back.
[Speaker 7] [28:50] Will do.
[Speaker 4] [28:51] Also, one last comment on Spaces and Go. Spaces is written in
[Speaker 1] [28:55] Go, so we have to give Go that much credit.
[Speaker 3] [28:58] Well, maybe is it possible that we're being, like, punished when the we are speaking ill of the god king. So then the and a assertion is tripping somewhere, and we are dying.
[Speaker 2] [29:08] I'm sure it's looking for Brian
[Speaker 4] [29:10] Cantwell specifically and people who've criticized the Twitter stack when it was in Ruby.
[Speaker 3] [29:15] There you go. Sounds right. Alright. Hey, thanks a lot everybody. Thanks a lot.
[Speaker 3] [29:20] I hope to see you next week. Thanks for joining us. Thanks, Adam. Thanks.