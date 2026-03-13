[Speaker 1] [00:00] While we're waiting for Jason, why don't you explain how we, how we got here?
[Speaker 2] [00:06] Okay. So, Twitter. I I think I'll I'll do my best to infer what you mean here. But, Twitter the other morning was like, hey. You've been here for 15 years wasting your life.
[Speaker 2] [00:18] And it suggested I tweet about it. So I did. So I tweeted why I signed up for Twitter, which was that, Brian and then I joined you were in the Twitter offices debugging a problem. Correct me if I'm wrong, but I think Jack Dorsey at one point walked across. We were sort of sitting almost in their lobby.
[Speaker 2] [00:40] I mean, it was it was a start up. It was a small building at that point. Walked through the lobby, kind of called over his shoulder. Hey, did you fix the problem with Solaris yet? Because they were experiencing some nasty performance problems, that, that they were seeing in production or in production on the joint cloud, which was hosted, which was, you know, based on open Solaris.
[Speaker 2] [00:59] And they weren't seeing the same performance problems on, like, their Linux desktops under no load. And, and therefore his inference was that it was a Solaris problem. And I don't think we had an opportunity to respond to that. Like, no, it's not a Solaris problem. He sort of stalked off.
[Speaker 2] [01:15] Am I remembering that right?
[Speaker 1] [01:17] Yeah. That is my memory as well. The, I remember he did come in and ask, have you found the problem with Solaris yet? And at this point, we had found the problem, and it was in Rails. And I'm like, who's this asshat?
[Speaker 1] [01:29] And and, the guy that Blaine was the and it was not Twitter. Right? It was obvious at the time. And Blaine was the obvious engineer. So it was, we were with Blaine and Jeremy among others.
[Speaker 1] [01:46] And, Blaine said, actually, we found it. It's in rails. And he was just kinda, like, walked off. And I'm like, go fuck yourself. Why am I sitting here debugging your app, pal?
[Speaker 1] [01:58] Like, who is that?
[Speaker 2] [01:59] I did not you know, I assumed that this must like, that was I did not remember that it was obvious. I remembered, I I Can you I
[Speaker 3] [02:09] We're just what is obvious?
[Speaker 1] [02:12] What is it's the obvious test. No. With Obvious is the this is the name of the company, it was Obvious.
[Speaker 2] [02:17] But was the so it's be was this because they started as, like, a podcast in company?
[Speaker 1] [02:23] Wait. Why were they called Avios? I don't know if Jason can get his tail in here. Okay. Yeah.
[Speaker 1] [02:27] Alright. He so Jason says he's showing up for the list. He's finally updated the app. I thought I tried to prepare him for this, but, you know, I prepared him poorly. I you know, that's a good Jason's gonna know this history better than it.
[Speaker 1] [02:40] It's not better than I do. But they were they had pivoted from whatever they were into and they were, Twitter had fewer vowels. I don't think they had do they have an e? I think they hit they did have an e when we were there by the time we were there.
[Speaker 2] [02:59] Yeah. But at the time we were there, I think it was, like, mostly on SMS.
[Speaker 1] [03:05] It wasn't it right? That was that was
[Speaker 4] [03:07] pretty early.
[Speaker 1] [03:08] It was definitely early. So this is in April of 2,007. This is why we're here because it's calling out the 50. So we got out of that, and I wish and I'll explain to the the the bug that that we debugged. But the we came I I came away from that being like, those guys are such clowns.
[Speaker 1] [03:27] I really liked Jeremy a lot, but I felt like Dorsey was such a clown. And I'm just like, that's got that thing's got no future. And I was like, there's there's Jason. I'm like, there's no way I'm gonna, I'm gonna create an account there. And you you came back with the opposite of pressure of, like, that's pretty cool.
[Speaker 1] [03:47] I'm gonna add an account.
[Speaker 2] [03:49] Oh, no. Actually, except for the first part. I I just came away with the I'm gonna create a account because there was a time in my life when it I desperately wanted to be AHL on as many platforms as possible.
[Speaker 1] [04:01] This is an AHL maximalist thing.
[Speaker 2] [04:05] Yeah. And, like, including, like, I I have other stories about how I social engineered my way into AHL and GitHub and and on Hacker News and things like that. No. This is this is my problem. This has nothing to do with with Avia's or Twitter.
[Speaker 1] [04:19] Right. And now did you did you were you cognizant of the American Hockey League when you did this? No. No.
[Speaker 2] [04:24] No. No. So I I, I welcome Jason, by the way. Oh, there we
[Speaker 4] [04:28] go. Well There.
[Speaker 2] [04:30] That you you got got email out here. What a what a trash
[Speaker 1] [04:35] can. It is. You know what?
[Speaker 4] [04:37] That's that's not all of
[Speaker 1] [04:38] our Oh, it is so true.
[Speaker 4] [04:39] So you but you can't but you can't use a fucking microphone on,
[Speaker 1] [04:44] Oh.
[Speaker 4] [04:44] The desktop app or
[Speaker 1] [04:45] You just search for a mobile phone or You that's exactly right. That's That's
[Speaker 3] [04:50] what $45,000,000,000 buys you. Alright? Come on. Okay.
[Speaker 1] [04:53] Yeah. No. It's it's bad. It's bad.
[Speaker 4] [04:57] I see.
[Speaker 1] [04:58] I'm so sorry to be, to It's okay. To drag you into the bad news. So the Adam
[Speaker 4] [05:04] So you so you wanna you wanna know the where where I heard you guys talking. You wanna know where Twitter actually came the fuck from and how Yeah.
[Speaker 1] [05:11] Well, so actually, Jason, I mean, you got if you could just take us back to that that give us that 2,006, 2007 South Park site guys, because there are a lot of IT companies happening that run that time.
[Speaker 4] [05:25] Yeah. Well, it goes it goes a little bit further back than that and that, they started occupying that office in, beginning of 2005. So we were because I was even using a desk in there for like 2 years before Twitter existed.
[Speaker 2] [05:41] And was this like over on Bryant? Am I remembering that correctly?
[Speaker 4] [05:44] No. No. It was over like in South
[Speaker 1] [05:46] In South Cal. Yeah.
[Speaker 4] [05:47] Okay. Yeah. Yeah. Yeah. And and, no.
[Speaker 4] [05:51] No. So it started the the the the original company was Odeo, and that started in the summer of 2005, and that was Ev, Williams, who, of course, made Blogger, and it was Noah Glass. And, the company that did Blogger was technically called Pyra Labs and that's what Ev was one of the founders of, of course, and Google bought, you know, Blogger. But there's some fucking thing where they bought Blogger, they didn't actually buy Pyra. He was able to still use it.
[Speaker 4] [06:22] Noah Noah Noah had done this company called AudioBlog. And so they sort of took AudioBlog and Pyra Labs, and they raised some money from the guys at CRV and then a whole bunch of angel investors. So like, for example, James Hong, you know, of hot or not fame, was probably the biggest biggest thing. Yeah. Because I actually when Ev gave James his money back for Odeo not happening, meaning the podcasting thing, I actually was then across the street at a bar with James drinking with them looking at this check.
[Speaker 4] [06:59] It was it was hopefully, it was sort of funny. But so the, but so it was no one no one ever did did that. So they did, Odeo, and it was Odeo sitting there. And Odeo had a, like, we started doing, like, we had, like, a Ruby on Rails, you know, little sort of meetups around the city, and we started doing them then at the Odeo office too because they had, you know What
[Speaker 1] [07:32] were they making?
[Speaker 4] [07:33] Were they making
[Speaker 1] [07:33] up you said they were podcasting.
[Speaker 4] [07:34] It was a it was a it was literally so it was it was also flash based, if you were to go all the way back. But it was just a it was like a directory in search for people's podcast. So it's just a way to share podcast. It's literally just an early podcast directory website. Like, almost a RSS aggregator, but for fucking podcast.
[Speaker 1] [08:02] For super early podcasts?
[Speaker 4] [08:03] Yeah. Yeah. Yeah. That's right.
[Speaker 1] [08:04] Where are podcasts in 2005?
[Speaker 4] [08:07] You know, I think everyone was saying that. It it wasn't, like, successful. And so so Right. Right. That's important.
[Speaker 4] [08:15] But, you know, Noah, of course, was there doing, like, I think I'm pretty sure Noah did the the fail whale design, you know, eventually. But then, Florian was there doing rails programming because the part of the audio back end started being more and more in rails with, like, a flash. I mean, imagine a flash front end with the rails back end and you can see what a fucking
[Speaker 1] [08:39] Yeah. What what can go wrong.
[Speaker 4] [08:40] Trash trash can on fire that was. It's still sniffing. So, so did it that. And Florian was one of the you know, because at the time, there was 7 core rails committers. There was, of course, David, Hannah Mayer, Hanson, you know, and Toby who's now the CEO, of course, of of the CEO and founder of Shopify.
[Speaker 4] [09:02] And then we had like Scott and Mike and like 2 others. We had 4 total committers that joined and then Florian was another Rails committer. He started working at Odeo. And so that that This
[Speaker 1] [09:13] is Scott Baron. Right? Is that remember that correctly?
[Speaker 2] [09:15] Yeah. Yeah.
[Speaker 4] [09:16] Yeah. Because Scott was the one that did all the, the All the details probes. Yeah. You remember that? Yeah.
[Speaker 4] [09:21] Yeah. That and and, and, and also was the one that worked with Apple to get all the details probes into the Ruby version they were shipping to on on Macs. And so, so basically, it was a type of thing where then because Florian was not a Odeo Odeo. Odeo was one of, 4 companies in existence. You know, basically, you know, whatever the fuck Shopify was called before it was called Shopify, it was called something else, but it was a snowboarding website, you know, at the time and then, Odeo and then Giant and then of course, 37 signals were like the 4 companies that had rails committers, you know, sort of in it.
[Speaker 4] [10:01] So we started doing like so we started doing little rails meetups and shit in the audio office. And, they decided to sort of do one of these, you know, weekend hackathons. And, you know, at that period of time, a whole a whole bunch of us, you know, strangely myself, it was either myself or or or Tom Tek was like the number 1 dodgeball user in San Francisco at the time. It was all, you know, Dodgeball stuff. You know what I mean?
[Speaker 4] [10:31] Where you're talking Dodgeball. Yeah. You know what you're you're all checking over you're checking in over SMS and that type of thing.
[Speaker 1] [10:38] You're right.
[Speaker 4] [10:38] Yeah. But Dodge bought also been bought by Google at that time and was sort of, you know, increasingly less used for that kind of thing. But basically on that one of those like little hack day, sort of hack weekends, Blaine and Jack and Florian mocked up this whole fucking thing that was like dodgeball. You know, you would like check-in and that. But I had to sort of, you would chat back and forth sort of element too.
[Speaker 4] [11:05] And that was, twtrr.com. So Twitter with no vowels.
[Speaker 1] [11:14] No. Vowels. Okay. And so and this is all the SMS?
[Speaker 4] [11:18] Yeah. So the main thing there was, the main interface was I mean, like, the website, it lets you read stuff, but it was basically non interactive. The main user Right. The the the input and output, if you will, was was was SMS. And it was funny because even even in the first, you know, because we took, you know, actual Twitter into production in January 2007.
[Speaker 4] [11:44] And, a big part of that infrastructure was all of the SMS demons and the like. There was as much, you know, there there was there was more SMS sending and receiving and email sending and receiving in that than there was for the website, actually. It was no one gave no one gave a fuck about the website. But no. But it so it was Odeo and then it was sort of like Twitter and then, they all decided to go, like, all in on Twitter and, of course, being called twttr.com with a weird fucking bubbly, you know, version of that wasn't gonna fly.
[Speaker 4] [12:24] So Ed went out and spent the money and bought twitter.com. It was owned by somebody the fuck else. I think they spent, I don't know, $500, $600 on it. And then they decided to not do Odeo. So, Ev bought out, you know, CRVs, Charles River Ventures and gave, you know, James's money actually had people sit down and say, okay, well, you know, we'll come on board of this, this Twitter thing or that type of bit.
[Speaker 4] [12:57] And so, so, yeah, it became, you know, Twitter sort of at that at that point. And then later on,
[Speaker 1] [13:07] And so this is, like, is this 2,006 at this point? Where are we?
[Speaker 4] [13:12] Yeah. Yeah. We're like
[Speaker 1] [13:13] Okay.
[Speaker 4] [13:14] We're, well, the the thinking's 2,000 6, but we're like, because when the web when when twitter.com went live in January 2000 7, like, that sort of, you know, actual with the new name and the the current look and that kind of thing.
[Speaker 1] [13:33] That was in January. Okay.
[Speaker 4] [13:35] Yeah. I still have the fucking like, I still have the quote and the architecture and, you know, it was and we went it was literally January 15, 2007 because, we, it was a clean billing cycle, basically. That sounds And
[Speaker 1] [13:51] then okay. And then so we because I think we were in there in April. So certainly between I mean, the thing obviously is has got overwhelming popularity basically from the jump.
[Speaker 4] [14:04] Well, no. Not honestly, not no. So the funny thing about it is the first it you know, it it you know, I get I guess it did, but, you know, the the thing that took like, the first time there was a major outage because like a big user showed up was, when John Edwards got on Twitter, when he was running for yeah. John Edwards was the, the first big Twitter user. Yeah.
[Speaker 1] [14:43] Okay. And so that that is strange. Of course, that is actually that kind of fits with him. He's running in 2 1,008. So it is early 2,007.
[Speaker 4] [14:51] Yeah.
[Speaker 1] [14:52] He's getting ahead of things.
[Speaker 4] [14:53] Yeah. Yeah. And he was, he so, you know, it's funny because, you know, because, you know, there wasn't really any, quote, unquote, outages in Twitter sort of January, you know, February, you know, sort of time frame of 1st sort of 60 days because, I mean, it was, the way it did the Twitter infrastructure there is is it actually was fronted by because of it because it was pretty clear in interacting with sort of the development team there that they they they didn't, you know, really, you know, they they weren't exactly
[Speaker 2] [15:29] Not rigorous?
[Speaker 4] [15:30] Yeah. Yeah. Yeah. And it was a very it was actually like, it was it had so many, but I have solutions to that. The solution back then, meaning 15 years ago, the solution there is that if you, if you don't trust what somebody's doing is you you put them behind, gigantic big IP load balancers that you can go change the logic of almost everything inside of, you know, iRULES and by writing Tcl.
[Speaker 4] [15:57] So so, you know, Twitter was behind
[Speaker 1] [16:00] to A big f five or whatever.
[Speaker 4] [16:02] Literally 2 clustered big IP 64 100 that were, you know, like on 2 gigabit, you know, per second, you know, times 4 uplinks to, you know, fucking, you know, level threes Internet. And, but you had essentially big IP sitting in front of it. And then, Mongrel was brand new, if you remember Mongrel, you know, one of the ways of running, like, a freestanding little rails, you know, process.
[Speaker 1] [16:33] Right.
[Speaker 4] [16:34] So we, I basically, I was load balancing off the big IP, big IP 64 100 directly to just as many mongrels that I could jam across, you know, that sort of memory space as possible. So it's a bunch of mongrels sitting there. And then, separately on that, I mean, NGINX and didn't exist yet. Light HTTP did, light did. So we had, like, sort of static, you know, dot twitter.com for all the static assets.
[Speaker 4] [17:08] And then that was basically off of, Lightspeed, which was a proprietary, you know, sort of web server, you know, initially back then. But it was it could fucking you know, it was the it was the engine x of its of its of its of its of its time. Okay.
[Speaker 2] [17:24] And, Jason, you should clarify because you you were not at Twitter.
[Speaker 4] [17:28] I was not at Twitter. No. No. I was I was at Joynt. But,
[Speaker 2] [17:34] in in Joynt where all of Twitter's infrastructure was hosted. Correct.
[Speaker 4] [17:38] Yeah. Yeah. That's right. Now, we happen to be things where I would work at a desk in that that building, just like how Myo Kennedy didn't work at Twitter, but he worked at a desk in that building. So I was working out of that office, you know, 3, 4 days a week, in that period of time.
[Speaker 4] [17:58] Because Joy was all I lived in San Francisco, but Joy was in Sausalito. Who wants to go, you know, across the Right.
[Speaker 1] [18:05] Who wants
[Speaker 4] [18:05] to go across the fucking bridge or take the ferry every fucking day just to sit at the computer somewhere else, you know. And so, no, in that period of time, I was pretty much pretty much there. And that was, you know, Jeremy Latross was doing ops, you know, there.
[Speaker 1] [18:21] I I love Jeremy.
[Speaker 4] [18:23] Yeah. But he's a good classic, you know, ops guy, you know, where for every major outage gets a tattoo to remind himself of it. Super, super, super, super, super professional from that standpoint. But it was big IP load balancers in front of Mongrels, then then also then, I set up a load balancing thing and sort of a cluster of my SQL in it. And then, some of the stuff that was cheating, I mean, all of the messaging stuff was all Ejabberd and done in Erlang.
[Speaker 4] [18:54] But because we had done a at that period of time, we had done a lot of of Erlang based chat infrastructure for people like, you know, Major League Baseball and different stuff. So we had a good handle on how to operate that stuff. And then there were these SMS demons and mail demons and some different things that, you know, fucking Blaine basically wrote in fucking Ruby. That was, that, you know, that that that stuff was a bit of a bit of sort of an issue. But there was, you know, there was the funny thing about it was, I mean, every and the first outage is a good example.
[Speaker 4] [19:31] You know, the first big outage of, like, why the fuck's the site down? Came when a bunch of, like, 5,000 all of a sudden John Edwards signed up. John Edwards had 5,000 followers. Right? And that that would have that would, you know, in sort of the current Twitter, that doesn't seem like that big of a deal.
[Speaker 4] [19:54] But, you know, Evan and Jack and these guys, they've only had basically less than a 100 followers, at Twitter back then. And the way the the website worked was these geniuses didn't, they didn't, and it's funny because every issue that was ever there is entirely not surprising and entirely predictable. You know what I mean? It was, like, there was never a problem there where you sat down and was, like, oh my god. You know, there's, like, jeez Jesus Christ.
[Speaker 4] [20:24] You know, someone's, you know, someone's getting a fucking Turing award for that one. There's never there was never that. It was always like, well, yeah. Yeah. Like, why the fuck would you turn the caching headers off?
[Speaker 4] [20:34] Why would you do that? Why would you do that? Well, we wanna make sure it's updating all the time. Yeah. Yeah.
[Speaker 4] [20:38] But that's not how that works.
[Speaker 2] [20:39] It's a photo.
[Speaker 4] [20:40] Yeah. So so followers were not paginated. So if you loaded up John Edwards page and loaded up 5,000 profile pictures from 5,000 followers on a single page. Uh-oh.
[Speaker 2] [20:56] Yes. Sounds like a problem.
[Speaker 4] [20:57] So and then, the the transfer. The pages were, also had some JavaScript on them that every 60 seconds had reload the page on its own to give you sort of the latest update. That was the JavaScript that was up there.
[Speaker 1] [21:12] So,
[Speaker 2] [21:12] like, all these abandoned web browser tabs would just be, like, DOS of the site?
[Speaker 4] [21:17] If if if if one person had an open tab in their browser just back there somewhere that and they had John Edwards page there, every 60 seconds, that that browser would make, 5,000 plus requests to the application. Yeah.
[Speaker 1] [21:35] I would like to I believe this predates tabs for whatever it's worth. I think this has to be a browser window in this It
[Speaker 4] [21:41] would 2007 era. Right? It would, it it's it's it's around the same time that it came out, I guess. But but it's a
[Speaker 1] [21:50] Wow.
[Speaker 4] [21:51] Yeah. So, so that that was when the the great feature showed up where all your users don't show up as a list of as a list on the right side of the page. It became paginated, you know, so it's only, like, sort of your top, that's sort of there in the user experience. We had a lecture about why you know, it's not really a big deal if somebody updates their profile picture and it's stale for an hour or so. But, you know, let's not let's not turn off, you know, headers or sort of do this or sort of do that.
[Speaker 4] [22:24] But it was one of the ones where, you know, they basically the the call always starts with, you know, you picked it up, and it was always, Jeremy or, you know, once Jack was running it, if you if they're really upset, then it was Jack calling, you know, like, you know, he fucking called me on Thanksgiving, you know, 2007. That was another fun one. So but, you know, but it's, you know, it's like, why is, you know, why is your network down? Why are your servers down? It's like, well, the network's not like, nothing's down.
[Speaker 4] [22:58] So, you know and and then you sort of go in and, you know, and, you know, you start you know, at that time, you know, $150 for a pair, but allowed you to sort of go into a customer and looked at what was going on kill the page off after a certain size or something like that. So I just went in there and quickly did a thing where we just chunked all the requests. You know? So it's, like, 20 It's it's for you. Yeah.
[Speaker 4] [23:40] It's basically, you know, the after the first 20 k came out of that page, that was sort of it.
[Speaker 1] [23:45] But, cutting you off at the bar.
[Speaker 4] [23:48] Yeah. But the way they had it, though, is the text came out first anyway. And it just means that, you know, the 300 pages of John Edwards' follower profile pictures didn't load, but, you know, that that was sort
[Speaker 5] [23:59] of okay.
[Speaker 4] [24:02] But but, no, John Edwards was the first person that broke Twitter. Yeah. That was that was, the first big one.
[Speaker 2] [24:09] The thing he'll probably be done for.
[Speaker 1] [24:11] I I it'll be the 4th sentence in his obituary.
[Speaker 4] [24:13] That's Yeah. Yeah. That's that's right.
[Speaker 1] [24:16] It so the I recall us, and I kinda went back to our earliest correspondence. And so, it must be the case that by the time they hit March, April 2007, like, they're in pretty consistent pain. Because, certainly, by the time we got in there, they were in very consistent pain, and they had I just remember walking in there. And the the Jason, you can tell me if your memory, is is different. But I remember Jeremy telling us that the, the requests were taking several 100 milliseconds Yep.
[Speaker 1] [24:55] Each. Yep. And I'm like, good news. We just need to find the IO.
[Speaker 4] [24:58] Yep.
[Speaker 1] [24:58] Like, that's that that's great. Yep.
[Speaker 4] [25:01] And he's
[Speaker 1] [25:01] like, no. No. There is no IO. I'm like, no. No.
[Speaker 1] [25:03] There has to be IO because Yep. You you can't spend a 100 milliseconds executing instructions. Like, that's a that's the the that's too many instructions.
[Speaker 4] [25:11] It's not how it's not how it's not how computers work.
[Speaker 1] [25:15] Right. As it turns out, no. And so just to, and I don't know if it's worth at this point or if it's worth just, talking about the specific issue that we found.
[Speaker 4] [25:25] Yeah. Yeah. Yeah. Go ahead.
[Speaker 1] [25:26] Okay. Yeah. So the so, they had I mean, they just do as you were describing, that they were very frustrated that they could not deal with more requests simultaneously. They, these CPU's cores are absolutely pegged doing CPU work.
[Speaker 4] [25:43] Mhmm.
[Speaker 1] [25:43] And, you know, busted out DTrace pretty quickly and, like, where are we spending our you time? It's all in b copy.
[Speaker 4] [25:50] Yep.
[Speaker 1] [25:51] Why are we in b copy and looking at the stack back trace? I just remember us being and I'm not sure actually, looking at the bug report that Alan Coopers have dug up, I actually don't think that my memory was wrong on this. I just remember 434 stack frames, Steve.
[Speaker 4] [26:04] Mhmm.
[Speaker 1] [26:05] We we are very deep doing these constant b copies, and it didn't take us too long to figure out that what was actually happening is that we were in the Ruby code that was gathering a back trace, a symbolic back trace Yep. Because we were throwing an exception. Yep. And the reason we were throwing an exception is because we had decided, we collectively humanity, had had decided that the way to we don't, like, want to just iterate a a for loop with a terminating condition.
[Speaker 4] [26:34] Yeah.
[Speaker 1] [26:34] We should actually walk off the end of an array and get an out of bounds exception. This is a much more elegant way of solving a problem
[Speaker 4] [26:41] Yeah.
[Speaker 1] [26:41] Which makes exceptions look very, and that was, that was all we needed to do is change that for loop.
[Speaker 4] [26:49] Yeah.
[Speaker 1] [26:50] And it was a, it was a so what do you remember?
[Speaker 2] [26:55] Brian, just to clarify a little bit more on that because Yeah. We so when we'd run off the end of that array, then we throw an exception. And part of throwing that exception because the runtime didn't know necessarily where it was gonna be caught was to gather up ants and make symbolic the entire stack
[Speaker 4] [27:10] trace.
[Speaker 2] [27:10] Yes. And so that was a shit ton of work.
[Speaker 4] [27:13] That shit ton of work.
[Speaker 2] [27:14] That was immediately thrown away. So because we were like 300 frames deep or something. Right?
[Speaker 1] [27:18] Yes. And it's gonna be thrown away by the next frame by the call.
[Speaker 2] [27:23] Right. By, like, the by almost the next instruction. Right? And, and and then doing that ad infinitum.
[Speaker 1] [27:30] Exceptions would be exceptional. Yep. I mean, I actually came to Mitch not leave exceptions at all in part because of this. I I think exceptions are I I don't I I actually much prefer Rust mechanism for using algebraic types to do this. But if you have exceptions in your language, they should be exceptional.
[Speaker 1] [27:47] They should not be for routine conditions because you're you're taking yourself into a collision course with parts of the runtime that are not optimized. So I remember finding this and I remember thinking like this is great, this is a big win, and they are gonna be very grateful.
[Speaker 4] [28:04] Yeah.
[Speaker 1] [28:04] That was I would say gratitude was not the emotion that was No.
[Speaker 4] [28:09] No. Because you're talking about a a group of people that, you know, when the milk and their latte's warm, they would spit it back to the barista. I mean, it's not a you know, I mean, that's sort of, like I mean, that
[Speaker 1] [28:23] It was a problem.
[Speaker 4] [28:25] You know what? You know what? Yeah. I started you know, I'm I'm just sitting around in my Los Gatos compound, sort of retired. I don't give a fuck.
[Speaker 4] [28:30] I mean, these guys were some of the, like, least educated ghetto developers I've ever experienced in my life. And I felt so bad for Jeremy in, like, a day to day basis.
[Speaker 1] [28:40] I did do that, Jeremy.
[Speaker 4] [28:41] But, you know, just imagine a bunch of fucking high school dropouts that are now learning rails before they could go copy shit off of, like, you know, stack overload or something. I mean, it was fucking terrible. I do remember when we run into these types of issues where it's like the fact that this group of people are now here together debugging this like thing. Okay? And we're not over there at Blaine's desk lighting him on gunfire.
[Speaker 4] [29:11] Okay? You know what I mean? Is is it's just it's, you know, it's just sad.
[Speaker 1] [29:18] Well, and I I remember and I can't remember if he said it to me or to you and you relate it to me, but I recall vividly at some point Jack describing having, like, 22 years of real time systems experience. Am I remembering this correctly? And me being like you said
[Speaker 4] [29:31] something like that.
[Speaker 1] [29:32] And I'm like, aren't you 27? How is that possible?
[Speaker 4] [29:36] I don't think he was even I don't think he was even that old. But but it was, yeah, I mean, you know, it was it was a it was a learning experience, I guess, from that point standpoint. I mean, the funnier the the, you know, the I'm gonna give you another example of, like, give you an example of one that, like, I I didn't pull in geniuses like yourself to take a look at. You know, there's things where literally, you know, rails at that time would be like, you know, / home/appnames slash, you know, images. Right?
[Speaker 1] [30:17] And,
[Speaker 4] [30:20] we were sitting there and what you know, again, the the site basically wasn't working. And and the and the skip to the end, I was sitting there trying to get into, and it was always failing on basically pulling things out of the image directory. And so I was trying to trying to, like, get into the image directory, and I couldn't and I couldn't and I couldn't. I was like, what the fuck's going on in in here? And, you know, long story short, what I discovered was there were 1,000,000 and 1,000,000 and 1,000,000 of profile pictures in this single directory.
[Speaker 4] [30:55] If not if not billions. I mean, it was basically it it Nice. Oh, yeah. Yeah. And it was sitting right in relatively spanking brand new, you know, ZFS too.
[Speaker 4] [31:06] Right? You know? So so that was that was even it was that image directory that, for example, you know, they're all like, well, we'll just reboot the server. Took, like, I don't know, fucking 8 hours to finally load that directory up. But that was self inflicted too, because I I went I said, well, there's not even, there's less than 10,000 users on the fucking website.
[Speaker 4] [31:33] How the fuck can there be literally a 1000000000 profile images or a 1000000 or, you know, and it was ridiculous. I mean, it's one of the ones where, you know, oh, no. I remember how we we we I remember how we discovered the number. I couldn't get in there, and so we still had a bunch of NetApp around. And I said, well, you know what I'll do is I'm just gonna it's letting me, like, send copy it across.
[Speaker 4] [31:58] I'm gonna I'm just gonna, like, copy I'm gonna try to just copy it over to the the the NetApp filers and see what happens. So it's like chugging away doing that. And then, you know, a big error pops up and says, you know, you can't have more than 38,400 files inside of a directory type, you know, error that NetApp used to spew out. Because if you used filers back then, you'd have to do your own hash directory structures and lay it out yourself and, you know, organize things nicely in it. So then I was like, oh, okay.
[Speaker 4] [32:27] Well, somebody's somebody's fucked up here. And then, did a thing where yeah. Then then, you know, you know, ran something. And I remember it took hours to run and it came back that it was, you know, this gargantuan number of files inside of it. It was 1,000,000 or billions.
[Speaker 4] [32:43] It was, like, fucking ridiculous and they weren't that big and then these little profile pictures. So then I said, okay. Well, I'm gonna I'm I'm gonna, I'm gonna take a guess here. Right? And so I do it again, and I just grab for, like, the name test in these files.
[Speaker 4] [33:01] And at the same time, I'm starting to poke through all the unit test files and stuff that they're in the rails app and sort of everything else. Right? So the fucking guys working on it, part of the unit test they would run would be to, like, write a profile image. And then they had this other thing where, it would, like, not clean up and the test would fail. And there's this comment in there about guy said, like, failed test, so adding random string generator in front of test.
[Speaker 2] [33:42] Oh, got it. So
[Speaker 1] [33:43] Oh, no.
[Speaker 4] [33:44] So what what they they had a unit test They were running all the fucking time that was writing a profile image, but, you know, the engineer that did it wasn't able to remove it. His quick little thing he commented was he just put random string and then with the word test on it. And they had That's
[Speaker 1] [34:02] kind of like removing.
[Speaker 4] [34:03] They had they and then what they did is
[Speaker 1] [34:05] It's kind
[Speaker 4] [34:05] of a removal. Yeah. And then I and I don't know how you can run a test that many times either. They managed to run this test so much that there was, like, random string test dot PNG millions of times in this directory. And that that that that degraded the performance of the website
[Speaker 1] [34:26] for some
[Speaker 4] [34:28] period of time. That was probably so so there was just, there was just, like, a lot of that stuff.
[Speaker 1] [34:36] And I feel that what made them frustrating at the time was I was telling you I felt this way with the issue that we found. You must have felt this way with the issue that you found. You the it's on the one hand, it would be it's like, oh, boy. Gosh. How do we do that?
[Speaker 1] [34:48] Sorry. We're growing so fast. This is a mess. But it it this felt like there was a kind of a level of indignation of, like, well, why can't the directory have billions of entries? It's like it should the website should be fast with billions of entries.
[Speaker 1] [35:02] Like, oh. Yeah.
[Speaker 4] [35:03] But, you know, the thing is it's just the it's just the like, that's just the, it's just a it's just a case study of the Dunning Kruger effect, my friend. You know? And that is you know, people have limited knowledge and competence. Will always overestimate that knowledge and and confidence. And, you know, they'll always if if you've been making because you got to appreciate some of the mindset of some developers in that period of time.
[Speaker 4] [35:31] They're coming and making relatively small websites that a small number of people would use. Right?
[Speaker 1] [35:37] Right. I mean, we're coming out of the nuclear winter of the .com.
[Speaker 4] [35:40] Yeah. And, you know, and things like you know, rails and the like made that super easy. It made it super easy to have a website that a 100 people would use. But when you started sort of heading into real system engineering land, and, you know, the like, you know, it turns out that, you you do have to, you know, understand that computer science basically is not just you typing your little novel in a thing and turning it into a movie. Like, that's not it's not what it is.
[Speaker 4] [36:17] You actually have to understand the systems that you're on and what they do and why they're being architected. And, you know, I mean, it's one it's you have to you have to actually have to do fucking engineering. That's what you have.
[Speaker 1] [36:29] Yeah. And I I I I feel like that that period of time too was this really kind of interesting shift where Silicon Valley historically was making infrastructure, but not really consuming that infrastructure. That infrastructure was being consumed elsewhere, certainly, like, in New York. And one of the feelings that I had being with Twitter is you need to actually get some people from VPNs or Goldman Sachs. You need to get folks who like, you think what you're do or or Bloomberg because, like, what you're doing with this looks a lot like, like, a ticker plan.
[Speaker 1] [37:02] I mean, this looks like a trading system, and these problems actually have been solved by people that are super smart and are are very experienced, but they're not here. They're not in San Francisco, at least not right now.
[Speaker 4] [37:13] Yeah. And but even but even the challenge with those folks is that, you know, a high frequency trading system and these things can be high performance, but there may be, you know, on, you know, less than 120 physical systems. Tell me, like, I mean, like, what what a lot of the web guys were dealing with, and I think people don't when you sort of think even 2007 to today, you know, people almost get I mean, because, you know, Twitter back then ran on, you know, basically a rack of servers. Right? And, you know, it's it's you know, on one hand, you know, the paradigm that started happening was everything became everything basically became a variation of a chat app.
[Speaker 4] [37:57] I mean, there's sort of this messaging at the core and there's high speed messaging needs. And, you know, it is, it is elements of what you see in exactly the financial services space historically. But then those tend to not even be as large as some of the systems that had to start being done in the web space. And you have this like you just you have this explosion in the back office. Yeah.
[Speaker 4] [38:21] And, and, all and she guys did you ever, did you ever notice the you you ever heard the story of their their, like, the third their, like, first Hadoop cluster there?
[Speaker 2] [38:35] No. No.
[Speaker 4] [38:36] What
[Speaker 1] [38:36] what year are we talking about for that? Fuck.
[Speaker 4] [38:39] It was, well, so, yeah, that was probably 80. Yeah. I forget exactly. But but the short version of it was they they they wanted to they wanted to do super fast Hadoop. You guys will love you guys will love this based on your background.
[Speaker 4] [38:59] They want they wanted to do quote unquote super fast Hadoop. So and they were gonna do that on, you know, brand new spanking SSDs. And, so they got a whole bunch of servers. They stuck these in switch data center, like, by by us when we were in there. So I was having a chat with, you know, like, Walt Walt on our own joint stuff at Switch, talking to the Twitter people, you know, that, like, had their thing in Switch there.
[Speaker 4] [39:25] And They were sort of relaying to me the issue they were dealing with at that point in time. And it was a, basically the Hadoop cluster would really get going, and then the whole fucking thing would just pause. And Firmware time.
[Speaker 1] [39:41] It's firmware o'clock.
[Speaker 4] [39:43] Oh, no. It gets it gets it gets better.
[Speaker 1] [39:45] Oh, really?
[Speaker 4] [39:45] Yeah. It gets better. And and there basically be no disc IO for some period of time. Like, just just I was always, like, right when these and these fucking things, you understand, like, when they were doing stuff in this, it, like, it was one of those ones where it was it's like, you know, watching a low rider bouncing around. Like, you're like, oh, yeah.
[Speaker 4] [40:08] These servers are doing fucking work right now. Like, okay. Like, you could just feel this thing vibrating. You know, so long story short, you know, we're digging in there. And, you know, the guys are trying to figure out this and trying to figure out that.
[Speaker 4] [40:21] And and, I remember, like, looking at the stuff and they had all the shit on the floor and I'm picking it up and and, you know, I'm staring at it. I'm like, okay. Well, you guys stuck all SSDs in here. Right? Yeah?
[Speaker 4] [40:33] And I go, you went, like, cheap SSDs? And, they did. And they had they had they had bought laptop SSDs that all had, like, drop and vibration protection. So the systems would actually get enough vibrating from the workload they were doing, and it would actually turn all the protective mechanisms on all the SSDs to protect them from damage. So then, that was that was an easy fix.
[Speaker 4] [41:12] You just have to replace all of those. And, yeah, I think they got all this. They they were getting all that shit from Dell. But but they stuck but they bought they went off on their own and bought a bunch of laptop SSDs and stuff up and the vibration sort of things kicked in. So there's always little things like that there.
[Speaker 4] [41:33] And I just, you know, the thing too is people were just before that, everyone's just used to buying a big fucking box and you're right on a big box and
[Speaker 1] [41:39] I gotta tell you, I would love right now, I would love to be on that system looking at those laptop SSDs because that feels to me like I so I'm going with my my original hypothesis. I think that that is bad firmware or firmware that is trying to desperately rewrite Flash. You filled up your Flash and the FTL layer is not key.
[Speaker 4] [41:57] I I think that is a perfectly valid assumption. I think it's a perfectly valid assumption.
[Speaker 1] [42:05] Definitely buying consumer grade SSDs and putting them in a data center, you're gonna get a whole new series of pathologies.
[Speaker 2] [42:11] Well, especially at that time because it was pretty early for consumer SSDs.
[Speaker 4] [42:15] Yeah. Yeah. It
[Speaker 3] [42:16] was there even trim yet?
[Speaker 4] [42:19] I don't think so.
[Speaker 1] [42:21] Not really. Yeah. Matt, you've had your hand up for a little while.
[Speaker 5] [42:26] Yeah. Okay. Am I on?
[Speaker 1] [42:27] You're on.
[Speaker 5] [42:28] Yeah. So I was, I was just wanted to say I was surprised to hear the the anecdote about all of the the the thousands or millions of images in one directory because I I I don't know where I picked up this bit of, like, Unix best practice, you know, type folklore. But as far back as 2004, when I was 23, I knew that if you've got a whole bunch of files, you you wanna use, like, you know, prefix directory names to, you know, to split them up into subdirectories. And I I don't know where I picked that up, but I know that I did.
[Speaker 4] [43:05] But but but there was a lot of, you know, what I would explain to people, and it was in the the kind way that I was explaining it to the team back then, as I said, look, you know, there was a a bunch of us that had experience with email systems. When you go and design like the storage back ends for large scale email systems, you do exactly as you just described. I mean, you know, particularly
[Speaker 5] [43:26] I might have picked that up from looking at, like, a a Qmail server
[Speaker 4] [43:30] or something. Literally, like, Qmail heading in the post fix in the whole conversation in the email server space back then was exactly how to horizontally scale out, you know, tons of in visual, you know, emails, you know, sort of like in there. But in that period of time, if you went, like, even, you know, I mean, I think we ended up making, like, a, you know, a Ruby gem, you know, or one of those sort of rail modules that basically made it easier to do, like, a hash directory structure under the images thing. But you you started sort of keying it up. It was still pretty junky.
[Speaker 4] [44:06] And and the funny part being is that, the solution we ended up coming up with then was just to get them to stop storing those images. And, it was right when, because, you know, Amazon Web Services had dev pay, and then they did simple q service, and they just launched s 3. And so, you know, the way we quote unquote fixed, you know, the sort of illogical way they kept on trying to come up with solutions to store these profile pictures as we just, moved all of Twitter's profile pictures on the fucking s 3.
[Speaker 1] [44:49] Yeah. Interesting. And, I I mean, also the irony of of that the record case is that the, ZFS actually does way better than, certainly, than UFS
[Speaker 5] [45:03] does personally.
[Speaker 4] [45:04] No. We we I was having this conversation with, you know, Jeff Jeff Bonway soon after. I was like, oh, dude. You know, by the way, like because normally, if literally what have happened if that was if that was a NetApp filer on I think it's I it is. It's like image, you know, whatever the fucking why is my brain blanking on the multiple?
[Speaker 4] [45:27] But, you know, it's like 32,400 or, you know, but it's, like, literally it would have hit exactly sort of file 3,000, 30000, you know, 240, and it would have done an error and it would have written another fucking file again. Like, that's that's, you know, but CFS was just sitting there going,
[Speaker 1] [45:45] just give it
[Speaker 4] [45:45] to me.
[Speaker 1] [45:46] I know what CFS is trying to get accommodated. I was just writing.
[Speaker 4] [45:49] And it was just Right. And so we I'm just sitting there. Yeah. I was just talking to Bonwick, you know, after that discovery. And I was like, I can't believe how much shit got jammed in that.
[Speaker 4] [46:00] And the but the whole the whole rest of the system was completely fucking fine. You know? It was just literally stuff was taking a long time in that directory.
[Speaker 1] [46:09] Right.
[Speaker 4] [46:09] You know? And then and I was like, I that was, not that's that was a that wasn't, you know, like, normal file system behavior from an ops guy, you know, I mean, from, you know, like, the experience you would have. Normally, that whole system would just shit itself, you know, if that was the case. But, but no. I mean, it's I mean, it was it was a funny thing that, you know, basically, it demonstrated that, you know, ZFS was just fucking fantastic.
[Speaker 1] [46:35] We we and it was interesting because I think, like, all of those companies, certainly Twitter had a total brain transplant over the years. None of those original folks, early folks at Twitter. I mean, Jeremy would I remember Jeremy looking at me being, like I was kinda rolling my eyes to something Zach had said. And Jeremy's, like, basically, the first opportunity I have to get out of here, I'm gonna get out of here. And, and he did.
[Speaker 1] [46:58] I you're good for him. Like and I think he I I caught up with him years later. He's like, oh, yeah. Though I sold it all, I did it early. Yeah.
[Speaker 1] [47:05] Never regretted it for a second. Never looked back.
[Speaker 4] [47:08] Yeah. I I mean, you know, it's, but, I mean, you know, ops guys are and I always think of my myself as being very ops y in mentality. But ops guys like Jeremy, they're just, you know, it's it's a it's a little bit like, you know, what's that one? Famous Alexander, the great speech where he's like, show me your stars, and I'll show you mine. All mine are on the front.
[Speaker 4] [47:38] You know? Like, there's there's, you know, there's never, you know, good ops guys are like that They're just ones where, you know, you basically roll in and it's already you know, you start you start heading through this journey of human psychology all the way through to then sort of what the technical issues are. But, you know, you're just,
[Speaker 1] [47:57] you know But they clearly changed their DNA over the years and got a much more, I mean, I think and and as also those companies as the traditional vendors began to to fade as kind of epicenters of technological innovation. The the the Twitters began to the Twitters and the Googles and so on began to and obviously, Amazon began to emerge as as places where
[Speaker 4] [48:20] But just but look how but look how like, take take an example like Snap. Right? You know, where, you know, maybe Snap Snapchat is even how Snap came. Snap snap's a good example of, you know, sort of the next Twitter, if you will, that was done that was a 100% on clouds from the very fucking beginning. And, I mean, it just blows my mind sometimes to sit down and even look at their, you know, the little, you know, their annual reports and I don't know, they talk about spending, you know, 1 and a half to $4,000,000,000, you know, with Google Cloud, you know, around sort of like doing x.
[Speaker 4] [48:58] And so, yeah, it's true. I mean, basically between, you know, an Amazon, Microsoft, Google, you know, there's enough things there that you can sort of piece together. I mean, it's just all this shit that exists from a SaaS perspective and, you know, there's 300 plus services, you know, that that, you know, exist inside of each of those. Plus, you can still do some stuff on your own if you wanna do it. I mean, there's just so many fucking options out there right now.
[Speaker 4] [49:24] Because it just didn't exist 15 years ago.
[Speaker 2] [49:26] So, Jason, rolling back to that, you know, there was a there was a period in Twitter where it became almost the experience became dominated by the fail whale. I mean, I guess the fact that we still remember the fail whale and they bothered to make, like, an adorable icon for when everything was fucked up, I think, speaks to the to the zeitgeist. So their reaction, as I recall, was to blame you, like, to blame Joyant and say that they're the reason why Twitter is down. Am I am I misremembering that?
[Speaker 4] [49:55] They would they would they would do that. Yeah. Yeah. And we always I didn't give a shit. I mean, meaning, like, when they left, they were down for 2 days after they left.
[Speaker 4] [50:09] I mean, and that was because they were moving over to, NTT, like in like NTT, but all Vireo data centers, and they were actually moving over to, like, NTT hosting. And they moved all of Twitter over there and then, you know, got it up and running and switched their domain names. I mean, switched, you know, the sort of name servers and that kind of thing. And we still had, of course, all the replicas running on us. But but, you know, they went and they went down hard and then called us, and we ended up, you know, in about 24 hours having them back up and running on us for, like, another month or 2.
[Speaker 4] [50:51] Because what, you know, what they what they learned is, like, joint was always, we were all I mean, we were 1 in 10 gig as soon as you could be 1 in 10 gig. I mean, we were, you know, trying to get, you know, stuff out of force 10. And then, you know, when Arista was brand brand new and everything else, we were always trying to, you know, have a really good network. Right? And, they went over to, you know, NTT, which is, as you can imagine, is almost like was, like, the big corporate hosting sort of, you know, equivalent, you know, out there 15 years ago.
[Speaker 4] [51:23] You know, head over to Vireo and get your sort of things. But every fucking server had a 100 meg port in it plugged into a 100 meg switches, you know, with, like, 100 meg uplinks. And so, literally, these guys, you know, all the customer base here sits on 1, 2 megabits per second of, like, traffic maybe. So they rolled right into this old 100 megabit per second network, and they just came off a 10 gig network. And, I can tell you too, like, that that type of messaging design and everything else in that, that just doesn't that does not work on 100 megs.
[Speaker 1] [51:58] Yeah. And once you, of course, once you actually hit bandwidth on those, once you're at throughput on the link, you're obviously you're queue you're gonna hit queuing delay. You're gonna go nonlinear. It's gonna get very sad.
[Speaker 4] [52:09] Yeah. Yeah. Yeah. And there wasn't I mean, people forget too. Just even 15 years ago, it wasn't like there was you know, it was a real sort of, like, echo chamber sort of anyway.
[Speaker 4] [52:20] And, but we just I mean, I think the first, you know, their first bill was about, you know, $38100 a month or something like that. And then, you know, they ended up being a 100, 150, $200,000 a month customer. You know, I'm pretty sure. Or if we were just we were just I mean, the the name of the game there was basically just brute forcing it with mongrels. You know?
[Speaker 4] [52:46] So, like, it was just essentially sitting there and staring at a a mongrel process, and it's like, how many mongrel processes can we run? And so it was just one system after the other just basically running that. I mean, it was a really good, example for me too because because we had brought on, you know, we just started thinking a lot about how can we get a faster Ruby runtime. And that was something multiple people were doing at that time. So, you know, you know, there was sort of the Ruby implemented in Ruby, you know, type sort of thing.
[Speaker 4] [53:19] There was this e Ruby, you know, blah blah blah.
[Speaker 1] [53:22] K, Ruby.
[Speaker 4] [53:23] Yeah. And when we first brought on, Ryan Dahl, it was to you know, it was because of the work that he was doing on the Ruby runtime optimization.
[Speaker 1] [53:33] I know that. It wasn't because of Node?
[Speaker 4] [53:37] No. Mark pointed out that, like, the Ruby guy on the team has this cool thing called Node. But, no, it was it was Node turned out to just be a side thing that
[Speaker 1] [53:48] I I did not know that.
[Speaker 4] [53:50] I I Yeah. Has been
[Speaker 1] [53:51] I thought I thought we had brought him in or I thought you had brought him in. It's pretty it's me at Joyant, but I thought that was be because of Node. It was because it actually to get Ruby.
[Speaker 4] [53:58] It was actually Moving faster. Bay based on his, it was based on his, Ruby runtime optimization work and everything he was doing with E Ruby. That's that's what it was 44. And then, it became a bit of you know, because you sort of look at at what Node JS became. You know, in a lot of ways, the instructive aspect for for for Node for me was, like, you know, Node is what Twitter should have been written in.
[Speaker 4] [54:32] You know, it's a very good example back then. You know, if if we were sitting there and Node DS was a thing in 2004, 2005, then, there actually would have been a lot less pain in the web space, you know, in sort of, you know, 6, 7, 8.
[Speaker 1] [54:49] Yeah. I mean, you need to have, v 8. Right? I mean, the the v 8 is very low bearing in that regard. V 8 is the actual the, in terms of having high performance VM.
[Speaker 1] [54:58] And I think and Twitter moved to Java at some point along I mean, post join.
[Speaker 2] [55:02] They Java and Scala. Apparently, they call
[Speaker 1] [55:04] it Razorback Scala.
[Speaker 2] [55:05] Instead of having smaller mono repo or many repos, they have 2 mono repos. They have the entire world built in Scala and and a similar world built in Java.
[Speaker 4] [55:15] Yeah. And, of course, I mean, isn't Scala implemented in the JVM? Yeah. Yeah.
[Speaker 1] [55:20] Right. Yeah. Yeah.
[Speaker 2] [55:21] Yeah. So one VM, but but 2 collections of code and coders who apparently hate each other.
[Speaker 1] [55:27] Yeah. And it wouldn't
[Speaker 4] [55:29] and it wouldn't surprise me a lot of the the Java stuff is more it's it's probably separated by, which domain the guys are working into. I mean, a lot of the Java stuff is probably people that are doing the, you know, the map reduce back ends and different sort of analysis like that. And that's all sort of flow, if you will. And Scott Scala is probably much more for the website and shit.
[Speaker 2] [55:52] And I should note this debugging session that we're that we're alluding to, you know, back in 2007, Brian was writing some heroic d trace
[Speaker 4] [55:59] because Yeah.
[Speaker 2] [56:00] There were no, like, we had we had done this work for the JVM to collect stack back traces at runtime, but nothing like that existed for for Ruby. And I don't think even in JavaScript. Right, Brian? We did that.
[Speaker 1] [56:14] No. No. No. No. No.
[Speaker 1] [56:14] Definitely.
[Speaker 3] [56:15] That was Python one. Yeah.
[Speaker 1] [56:18] The Python one also did not exist at that point. That was No.
[Speaker 4] [56:21] It did.
[Speaker 1] [56:22] Or maybe maybe it just did. Maybe. Yeah. That was work that John Levin did. Maybe kind of concurrent in there.
[Speaker 4] [56:29] But but I think that
[Speaker 2] [56:30] that opened our eyes to some of the needs around dynamic languages and ways to to use USDT, which had been developed for an entirely different purpose
[Speaker 4] [56:38] Yeah.
[Speaker 2] [56:39] And for these, these other DTrace helpers for dynamic languages.
[Speaker 1] [56:43] Oh, totally. Yeah. What I felt like that this may I I don't know if this was, before, during, or after our brief love affair with Perrott as the second coming of Christ? Do you remember those times?
[Speaker 2] [56:55] Well, I think Perrott was earlier because we at this point, we were at Fishworks, and the Perrott love affair happened while we were still in the kernel group.
[Speaker 1] [57:02] And and it this is a brief love affair. This is a weekend fling with Parrot. And Parrot being a, a VM to rule them all. So we saw it's like we thought, oh, this is great. We're gonna have, like, the VM to rule all VMs that you could do all languages in.
[Speaker 1] [57:15] And then we just instrument this one VM, and we will be able to instrument everything that Parrot can implement. Of course, it was maybe not so much.
[Speaker 4] [57:23] You don't
[Speaker 2] [57:23] feel like Parrot and, like, Raku or whatever it is, have come up an alarming number of times as, like, a basic basically a dead end technology that we love talking
[Speaker 4] [57:33] about. Yeah. Because because yeah. Raku, Jesus Christ. Yeah.
[Speaker 4] [57:35] Because that's the meta model on a runtime virtual machine. And look, Jason, I only know
[Speaker 2] [57:39] Raku because this is the 4th time we've we've had to dredge that
[Speaker 1] [57:43] without Okay. So I know I know we we have brought up Raku a lot. Are you sure we brought up Parrot this much?
[Speaker 2] [57:49] You think we're talking about Raku
[Speaker 4] [57:59] God. We've got it
[Speaker 1] [57:59] here at that
[Speaker 6] [58:00] point.
[Speaker 4] [58:00] Hey. You know. But the funny part is, you know, Perot's Perot's still on GitHub, and it's, last release was in 2016. I think But the good news is is, you know, it's it's, you know, it's it's successor actually had a release today or yesterday. Look at that.
[Speaker 4] [58:17] More VM, baby.
[Speaker 1] [58:20] More VM?
[Speaker 4] [58:21] M o a r v m. Yeah.
[Speaker 1] [58:24] MorVM is the success we definitely need to talk about that.
[Speaker 2] [58:27] Yeah. That's a first. Right?
[Speaker 1] [58:29] We have not talked about the about the success.
[Speaker 4] [58:31] It says it says more VM was created to allow for greater efficiency than pair it by having a closer internal representation to the model
[Speaker 1] [58:41] system. Look at that.
[Speaker 4] [58:42] Yeah.
[Speaker 1] [58:43] I am not as convinced that we talk about parent quite this frequently, but I'm I'm I am too, I'm frightened. I'd actually don't wanna back up on that because I'm sure we have. I'm sure I am sure that I do not have the biological ability to talk about parrot, but I'm also missing parrot And our our brief parrot love affair. Yeah.
[Speaker 4] [59:00] Parrot parrot say, talk about a talk about, like, a a point in time time capsules. I don't know what the fuck they even call that, but it's like a yeah.
[Speaker 1] [59:10] It it though, it was definitely like you had to be awake for that particular
[Speaker 4] [59:13] That's like that's like bumping into somebody that has a certain style of a mustache, and they're the only one that has it. But it was really popular for, like, 2 years there Right. In one city.
[Speaker 1] [59:23] Right. And in Perrot's case, I think that city might have been Portland. Yeah. I just remembered, like, OzCon 2005. Parrot was I wanna say look.
[Speaker 1] [59:30] We just need to, like, completely talk about Parrot. Adam then will never talk about it again. I wanna say OzCon 2005 peak parrot. That's what I'm that's
[Speaker 2] [59:38] what I'm saying. I'm totally with you and I think I I read that parrot book on the way back from either that OzCon or, like, Euro OzCon that year or something.
[Speaker 1] [59:47] Alright. I'm so sorry that we talked about that a lot of times. The but I yeah. I mean, I definitely remember it was we were getting on our kind of hands and needs to be able to figure out what that Ruby stack trace looked like. I feel like we learned this lesson a couple of times.
[Speaker 1] [59:58] Definitely saw it vividly there that the biggest performance problems in the stack were higher in the stack rather than lower in the stack. And in part because of that era with of of suboptimal VMs. I mean, I think with with Node and then with Go and then with Rust, I I would like to believe that that is becoming less true. But
[Speaker 4] [01:00:16] No. I think it's entirely there's there's just this, because we because we forget too that that in that period of time I mean, what? April 2003, you know, AMD came out with a 64 bit x86 chip, but but nobody else had 64 bit x86. It's like their fucking 64 bit strategy. Right?
[Speaker 4] [01:00:37] I mean, even I I mean, even Intel's Itanium and bunch of people sold shit on, you know, Spark and sort of everything else. And so it wasn't even clear exactly which fucking instruction set architecture everyone was getting ended up on. You know? And so you're sitting around in x86 land. And then you have this explosion of fucking languages that people are writing and sort of like whatever, and it was all just a fucking unoptimized mess from I don't know what, 2004, 2012.
[Speaker 4] [01:01:09] But since then, everything's, like, exceptionally well done. I mean, you know, if you're basically writing stuff in Rust and Go and and everything else, or it's it's it's tough to fuck up an app now. At least at least the way some of those are.
[Speaker 1] [01:01:22] And I do feel it's because we, humanity, spent a lot of our mental energy on these consumer facing web applications, these SaaS applications. And we got we got better at it. I I actually I actually think that I asked this for a a hot take. I actually think the the YouTube era allowed us to better communicate best practices. And the the kind of the whole rise of, like, the recorded presentations where people could you know, you could watch videos from Surge and learn.
[Speaker 1] [01:01:53] I feel like Surge was RIP, was a conference that, Theo and crew held. Did you ever make it to the surge, Adam?
[Speaker 2] [01:02:01] No. I don't think I did.
[Speaker 1] [01:02:02] Oh, man. They were so good. They were always
[Speaker 4] [01:02:05] for it.
[Speaker 1] [01:02:06] The surge was great. And the surge 2010 in particular was the first one. I just feel like there was a lot there was a pent up demand for sharing expertise because you had now what had been kind of, the
[Speaker 6] [01:02:20] folks that
[Speaker 1] [01:02:21] were not really systems thinkers necessarily in 2005, 1,006, 2,007 had now you have people that were real systems thinkers tackling these problems. Yeah. And and the and the the systems themselves were a lot better. Like, the fail whale went away. Right?
[Speaker 1] [01:02:33] Like, the ultimately, Twitter Twitter figured out their problems. I do want I just because I we we we promised we we would, Jason, and also because Adam and I can't biologically resist it. We do need to talk about what a post along Twitter looks like. I before we do, though, I Adam, I just wanted to go back to the AHL. Yeah.
[Speaker 1] [01:02:57] Well, no, because I Jason had a really interesting tweet. I I don't know what a couple weeks ago, Jason, where you're like, I'm actually glad that I'm Jason h, not Jason.
[Speaker 4] [01:03:06] Yeah. Or Jay. I mean
[Speaker 1] [01:03:08] Right. Right. You could be Jay.
[Speaker 4] [01:03:10] So I I I was Jay and I was Jason, and then I've been Jason h. I mean because even Jason Calacanis, who's Jason, he's the 3rd Jason. He's had Jason. You know what I mean? So, because I I was I was, like, there when the single letters were being handed out.
[Speaker 4] [01:03:28] They were they weren't handed out to just people. I mean, so, like, I mean, in my in my because, you know, you know, my wife, MJ. MJ and I, she's MJ. Okay? MJ and I lived with at k and at c.
[Speaker 4] [01:03:40] They were married, and we were splitting a house in San Francisco. So literally, in my fucking house, like, just amongst just amongst house just among my housemates.
[Speaker 1] [01:03:51] Five letters for 6 people.
[Speaker 4] [01:03:53] We we've actually had dinner parties where, it's been 10 single letters and 2 double letters at the party.
[Speaker 1] [01:04:03] Wow. How do you feel as a as a peasant triple letter, Adam? You you you can eat on the street.
[Speaker 2] [01:04:10] Yeah. Exactly. Seriously. Just leave it out for me.
[Speaker 4] [01:04:13] Yeah. So so no. I mean, I I, you know, I I mean, because I think,
[Speaker 1] [01:04:17] Hey is still around. C has been suspended by Twitter. I'm sorry. As I'm checking up on what what has happened to this single letters?
[Speaker 2] [01:04:24] Where are they now?
[Speaker 1] [01:04:25] Where are they now? This the single letters, the alphabet.
[Speaker 4] [01:04:27] At, at j is like, let's say she's at the New York Times or something like that. But and then, of course, Jason right now is Jason Calcanos, but but like I said, he's he's at least the 3rd Jason that's had that. But I'm sure he acts like he's always had it, but he hasn't always had it.
[Speaker 1] [01:04:46] So so Adam was AHL, then the American Hockey League comes along. And you how did you negotiate your troops so American Hockey League.
[Speaker 2] [01:04:54] Well, so I I feel very lucky that I that my initials aren't, like, NFL or MLB or something like
[Speaker 1] [01:04:59] that because
[Speaker 2] [01:04:59] I'm sure there wouldn't be a lot
[Speaker 1] [01:05:01] of conversation there. Not if it is cordial.
[Speaker 4] [01:05:03] I would have
[Speaker 2] [01:05:04] just, like, tried to log in one day, and it wouldn't have worked. Right.
[Speaker 1] [01:05:07] But, no, I didn't
[Speaker 2] [01:05:08] know anything about the AHL, and, like, Twitter wasn't that popular. But then at some point, it started getting popular. And then I'd get these tweets that are like, go wolverines and like checkers.
[Speaker 4] [01:05:17] Oh, yeah.
[Speaker 2] [01:05:17] It's the Calder Cup, you know. And I and, and I was like, what the fuck is going on here?
[Speaker 1] [01:05:24] Yeah.
[Speaker 2] [01:05:25] And so that's that's when I discovered the AHL. And, and, I bought a bunch of AHL Jerseys because I guess I had $40 to spend on eBay, too many nights in a row. But the AHL is at the AHL. And I've actually had some funny interactions over the years where, they've said things like, well, you keep us well informed about whatever it is you're tweeting about, Adam. Yeah.
[Speaker 2] [01:05:56] So, they they acknowledge me. I think, you know, I I don't wanna I wanna stay off of their toes so they don't get hungry for a better
[Speaker 4] [01:06:04] Twitter Is
[Speaker 1] [01:06:05] it making you nervous that we're talking about it
[Speaker 2] [01:06:07] this week? A little bit.
[Speaker 1] [01:06:08] A little bit. No.
[Speaker 4] [01:06:09] But the lesson but the lesson for me is, like, because, you know, I was Jason at WordPress. I have, like, my my my it's it's my name at Gmail. It was my name at rocket mail. You know, so I had so once you start you're the last fucking thing you need is, like, jason@yahoomail. It's like the worst email address in the world.
[Speaker 4] [01:06:29] Right. Exactly. So, like, the absolute one of the absolute worst ones in the world. And so then, no. We sort of sat down that, and it's like, yeah.
[Speaker 4] [01:06:37] I mean, you know, it's it's it's like, yeah. You do. It's like, yeah. Of course. I'm gonna sign up and just I'm I'm Jason everywhere else.
[Speaker 4] [01:06:47] I mean, no one's gonna I mean, there's so many there were so many even customers like Twitter that don't even exist anymore, you know, that you go and sign up for their app for. You know what I mean?
[Speaker 1] [01:06:58] So when looking for, I was trying to remind myself about context, about Twitter, and it is funny all of the companies that it's mentioned at the like, Tail Rank? I just forgot about Tail Rank.
[Speaker 4] [01:07:11] Yeah.
[Speaker 1] [01:07:11] It's like, I I've got a sentence that I sent in 2007. Companies like Twitter, Tail Rank, and Ning. Yeah.
[Speaker 4] [01:07:18] Yeah. Yeah. But I was Jason with Ning, know? You know, we that kind of thing. But the, well, you know, the funny thing about Ning is, you know, the,
[Speaker 1] [01:07:27] I love Ning, actually. That's You know the you
[Speaker 4] [01:07:29] know the TV and Yeah. But but but there was a pair of engineers we were interacting with there, Ernie and Hassan, and that Hassan is Hassan Manoj, the fucking comedian.
[Speaker 1] [01:07:42] That's pretty funny.
[Speaker 4] [01:07:43] Yeah. Yeah. He worked at Nave.
[Speaker 1] [01:07:46] The what and, Adam, I've got a a a code of your HR experience. The, are you aware of the fact that Alexander's become that my my 14 year old has become a huge hockey fan?
[Speaker 2] [01:07:58] No. No.
[Speaker 1] [01:07:59] I didn't oh, I I was on a business trip to Minnesota where we were doing bring up. I was I've been gone for, like, 1st business trip in whatever it was, 2 years. I'm in the airport. I wanna buy some for the kids. I got them some, I don't know, Minnesota wild socks.
[Speaker 1] [01:08:14] As it turns out, what I didn't realize is from a sports perspective, the Broncos were doing poorly, and the A's like to torture their fan base. So, my 14 year old was immunocompromised. And when I dropped those wild socks on him, he's like, okay. I'm a hockey fan now. Like, I I I actually, like, I'm so angry with the Broncos and the A's that whatever the sport is, I'm gonna watch this.
[Speaker 1] [01:08:39] And he's like, I guess I am a Minnesota mild. That's what it's upside down. Wild. Oh, Minnesota Wild. So he's like, oh, there's a game on this afternoon.
[Speaker 1] [01:08:46] So he has become a hockey super fan. This is only since October.
[Speaker 4] [01:08:50] Really?
[Speaker 1] [01:08:51] He he goes from, like, never having seen a hockey game at all to being he's he now views Minnesota as, like, his ancestral homeland. Like, I have never had an airport tchotchke purchase.
[Speaker 2] [01:09:03] Oh, you gotta be over deliver like that.
[Speaker 1] [01:09:05] You do be careful. You gotta be very careful. Like, I I feel like, god, could this have happened to any one of these things? But so he is but in particular, he is now, like, following these hockey players through the minor leagues. And he you you probably know where this is going.
[Speaker 1] [01:09:23] But he's like
[Speaker 2] [01:09:24] like the the some recent minor league incidents?
[Speaker 1] [01:09:27] No. This is more like Okay. Hey. Why does Adam have the American Hockey League's Twitter account? And this is and I'm like, I mean, you've known this kid since birth.
[Speaker 1] [01:09:37] I'm like, what do you mean why does Adam have why does the American Hockey League get his Twitter account? That's the question. And he's like, Adam should really give them the handle. And I which I view as an act
[Speaker 4] [01:09:47] of this Wow.
[Speaker 2] [01:09:49] Honestly. That that is ridiculous.
[Speaker 1] [01:09:50] No. That is absolutely ridiculous. No. I I you know what? You can talk to him as well.
[Speaker 1] [01:09:54] I have punished him just so you know. I I I
[Speaker 4] [01:09:57] you know? Good. Well, I I'm just like moments. Hey. The sad part for me I mean, the the where this hits, like, real life is my wife is at MJ on Twitter, and I'm I'm flying in, from from fucking somewhere.
[Speaker 4] [01:10:12] I landed SFO. I turned on my phone, and I look at Twitter, and there's a tweet from, you know, Ohm, you know, a friend who's tweeting, I can't believe we've lost at MJ, you know, you know, rest in peace, none of the dunk. And I, like, was like Oh my god. I was like, oh my god. Oh my fucking god.
[Speaker 2] [01:10:33] This is how I'm finding out?
[Speaker 1] [01:10:34] I'm calling This is how
[Speaker 4] [01:10:35] I'm finding out. I've been on the I've been on a plane. I'm calling my wife, nobody's picking up. I'm calling Ohm, nobody's picking up. And I call, you know, a common friend Matt, nobody's fucking picking up, nobody's fucking picking up.
[Speaker 4] [01:10:47] Right? So now I'm, like, looking at what's he talking about? And I I go, like, you know, at MJ and I go over my thing. Okay. He was talking about Michael Jackson died.
[Speaker 4] [01:10:57] Michael fucking Jackson died. Okay. And somebody who's got Yeah. This is the this is the danger. Okay.
[Speaker 4] [01:11:03] Literally goes, oh, my whole my whole wife's thing is at MJ for Michael Jackson or at MJ for Michael Jordan the whole fucking time. But, like, when
[Speaker 2] [01:11:13] with Michael Jackson
[Speaker 1] [01:11:14] It is actually funny. You go to MJ's Twitter profile, and she's like, this at is not for sale. Sale. That is true.
[Speaker 4] [01:11:21] Oh, yeah. Because, I mean, it comes all the time.
[Speaker 1] [01:11:23] He's not a pop star athlete or narcotic.
[Speaker 4] [01:11:25] Oh, but if anyone's, you know believe me, it's it's it's like it could be for sale. So the, everything's for sale. But it was but it was just, you know, it's just it's just a thing on there where, you know, a, like, highly sophisticated long time two letter user himself like Ohm, right, like, rips off a tweet
[Speaker 1] [01:11:48] About, like, hey. Oh, you're talking about that death. I mean
[Speaker 4] [01:11:50] oh, no. Yeah. Yeah. No. Exactly.
[Speaker 4] [01:11:52] But this isn't like like a random dude on the Internet.
[Speaker 1] [01:11:54] I mean, this is not
[Speaker 4] [01:11:56] like, oh, yeah. Like, at the wedding, come to the house for fucking dinner.
[Speaker 1] [01:12:01] We just
[Speaker 4] [01:12:02] saw each other in London. You know, like, you know my wife's fucking Twitter handle. You must know it. There's no way you don't know it. You know?
[Speaker 4] [01:12:10] And it's like, god. Fuck Michael Jackson. Fuck Michael Jackson. I was, like, shaking. I'm serious.
[Speaker 4] [01:12:17] I'm running out of the plane. I'm like, Twitter. Man. Doubt she she's dead on Twitter. That's what happens.
[Speaker 4] [01:12:23] That's what happens. That's how this goes.
[Speaker 1] [01:12:25] Fuck. Oh my god.
[Speaker 2] [01:12:27] Yeah. Oh my god.
[Speaker 1] [01:12:28] Alright. So I I we we gotta get to to Elon predictions. Adam, do you have any that are that he's got lined up?
[Speaker 4] [01:12:36] He's gonna let Trump back.
[Speaker 1] [01:12:38] Yeah. So do you okay.
[Speaker 2] [01:12:39] That feels like a safe one.
[Speaker 1] [01:12:40] Oh, I'm not sure. Okay. So okay. Okay. That I feel is I feel actually the prediction is that he moves the headquarters out of.
[Speaker 1] [01:12:50] That I feel is the I I I feel that is the absolute unquestionable lock. 1st act, headquarters moved maybe to literal Mars, but if not literal Mars, then, like, I I am moving them to, like, what, like, Okeechobee, Florida. Like, what is where can I move it to that is gonna, like Right? Just get under the fingernails of as many employees possible.
[Speaker 2] [01:13:12] That's a great prediction.
[Speaker 4] [01:13:13] Yeah. Yeah. Yeah. That just feels like a lot
[Speaker 3] [01:13:16] of Also remote work is canceled. You need to move.
[Speaker 1] [01:13:19] Right. Remote work is canceled. You need to move, and then, oh, actually, we can't get out of this lease and it's kinda complicated. And so, actually, we're gonna, you guys are gonna work from this building and, basically, nothing changes. It's my prediction.
[Speaker 1] [01:13:32] That's quite
[Speaker 2] [01:13:33] a parlay. I like it. I mean yeah. Yeah.
[Speaker 4] [01:13:36] I don't I don't know. I mean, it's not like, you know, Twitter is the ongoing juggernaut of industry crushing features. It's a it's a good example of an app and I'll just call it a fucking website, I guess. But, like, a website that despite everybody's attempt to make it not successful, it just it just it just it just it just can't help itself.
[Speaker 3] [01:14:03] Including many people at Twitter.
[Speaker 4] [01:14:05] Yeah. I'm talking about people at Twitter. Yeah. No. I mean, like, literally, everybody there's everybody there.
[Speaker 4] [01:14:10] I mean, even Jack is, like, tried his fucking best to have it not succeed, like, everybody there. And it but it just you can't I mean, it's it's it it's literally one of these few examples of just you know, I guess what it plugs into from a human standpoint is such that, like, it's just the it just it's can't fail.
[Speaker 1] [01:14:36] Well, I so I think that so I think there are a couple of scenarios. I do think that there's a tomb war scenario here where the and so you I mean, you guys think it's a lock that Trump comes back on. I don't necessarily think that that's a lock. I do think that I
[Speaker 4] [01:14:49] was just trying to pick stuff that, you know, would have, you know, would have some predictability. Some some like, hey. Yeah. You know?
[Speaker 1] [01:14:55] That happens. That does happen. Yeah.
[Speaker 4] [01:14:56] Yeah. I'll also take I'll I'll take $20 on that. Well, I'll take $20 if Trump isn't coming back. It's like, alright. Alright.
[Speaker 4] [01:15:02] We can do that. Oh, are we? You gotta
[Speaker 1] [01:15:04] God, you are reminding me. Okay. You walked us there until the last time I won $20 off you.
[Speaker 4] [01:15:09] Yeah. Yeah. Oh, is it paid?
[Speaker 1] [01:15:13] It was paid. It was paid because we were meeting Steven O'Grady at the at the House of Shields.
[Speaker 4] [01:15:19] Yes.
[Speaker 1] [01:15:20] Of course.
[Speaker 2] [01:15:21] His office in San Francisco.
[Speaker 1] [01:15:22] His office in San Francisco. And, of course, my opener, great to be here at the House of Shields, across from the Palace Hotel. Yeah. The the Palace Hotel is, of course, the the the the site of the death of president Warren Harding.
[Speaker 4] [01:15:35] Yes. Of course.
[Speaker 1] [01:15:36] Who doesn't
[Speaker 2] [01:15:36] know that? Right.
[Speaker 1] [01:15:37] Who who doesn't know that? Well, that's and so immediately, Jason starts to nerd chain me and says, you are the only person that knows that. I'm like, listen. I get that Warren Harding died a while ago, but he was fucking US president. Yeah.
[Speaker 1] [01:15:51] Lots of people know that. And in fact in fact, I was like
[Speaker 4] [01:15:56] And I was like, you fucking nerd. No one knows that.
[Speaker 1] [01:15:59] No. Right. And I'm like, every single employee at the hotel knows that. And he's like, I don't think a single employee knows that. I'm like, great.
[Speaker 1] [01:16:06] This is easy to resolve. $20. We're gonna walk across the street.
[Speaker 4] [01:16:09] Yeah.
[Speaker 1] [01:16:10] 1st employee we see, we're going to we're we're gonna ask them. Fine. Yeah. Yes. Absolutely.
[Speaker 1] [01:16:14] Maybe we both have a couple drinks in us. We're definitely zed up. I know I am gonna absolutely win money. We walk in. 1st employee we see is the concierge.
[Speaker 1] [01:16:23] Yeah. I say, sir, a US president passed away and I didn't even get to the rest of that sentence.
[Speaker 4] [01:16:32] Yeah. He was true.
[Speaker 1] [01:16:33] I remember he just The the the look in his eyes, I could have asked him anything about the Harding administration. We could have talked about teapot dough.
[Speaker 4] [01:16:41] Yep. We
[Speaker 1] [01:16:41] could have talked about about the convention. I could have talked about I mean, this guy is like, what obscure aspect of Warren Harding do you wanna know? Yep. And so it's so he's like he is, like, took book of total knowledge. I'm, like, just give me the money now.
[Speaker 1] [01:16:55] And he's like, yes. How can I accommodate your request? What would you like to know? Like, well, my friend here doesn't doesn't believe that you employees know who this this person is. Could you just give us the name of the president?
[Speaker 1] [01:17:06] And, of course, I can remember being like, Warren g Harding, 26th president of the United States of America. I can't even remember his but he I mean, he definitely was adding, like, as much superfluous detail as possible.
[Speaker 4] [01:17:18] He did it he did it, like, in a special voice and everything. Yeah.
[Speaker 1] [01:17:21] Right. And and then Jason again we've had a couple of tricks in us. Jason is like, fuck you. That's the concierge. Like, the concierge's job True.
[Speaker 1] [01:17:29] Is to answer questions. And then I'm like, okay. That was $20. I want I now want a $1,000
[Speaker 4] [01:17:36] Yeah.
[Speaker 1] [01:17:36] That we can find someone who for whom the question has to be translated who knows the answer.
[Speaker 4] [01:17:44] Yeah.
[Speaker 1] [01:17:45] And at this point, I saw a look that I haven't seen very frequently in Jason's eyes, namely fear. Jason's like, no deal. No. No. No.
[Speaker 1] [01:17:52] I'm not doing that. We're yeah. We're we're done. I think you you paid your point, asshole.
[Speaker 4] [01:17:56] Yeah. We're we're good.
[Speaker 1] [01:17:58] You're not the only person that knows about Warren Harding.
[Speaker 4] [01:18:01] Yeah. But the thing is I just I
[Speaker 1] [01:18:02] Alright. So so sorry. When are you gonna put $20 on?
[Speaker 4] [01:18:05] Oh, I don't know. I forget now.
[Speaker 1] [01:18:09] Warren Harding. So I But you always pay
[Speaker 4] [01:18:12] me back. Bets.
[Speaker 2] [01:18:12] I always pay me back.
[Speaker 1] [01:18:13] You do. You do. And you I paid right on the spot. I say. Right on the spot.
[Speaker 1] [01:18:18] The So
[Speaker 2] [01:18:19] so so the thing I mean, I just have fears. I have fears that, like, are we gonna feel good about using this platform in, you know, to make it to our 1 year anniversary of doing Twitter spaces? Like, how you know, at is there a point where it actually gets achy?
[Speaker 1] [01:18:34] Okay. So yes. I think that is what I that is the Biffed Hanen scenario. So so so so the Biff so I think here's the reason that I think you should have solace about this. I think that this is not gonna be, like I feel, like, slightly worse about being on Twitter.
[Speaker 1] [01:18:51] I don't think that that, like, the dial isn't that fine. I think if Trump is back on the platform, they will likely because if they eliminate all moderation, let's say, or eliminate the the ability to block people or mute them, I mean, if if they eliminate all the safety features they've added, if they were to go I mean, I don't think Jason I don't think Elon knows what an unmoderated Internet looks like. I don't think he's he's not close enough to the Internet to actually have seen an unmoderated
[Speaker 4] [01:19:18] I don't,
[Speaker 1] [01:19:22] the unmoderated like
[Speaker 4] [01:19:23] that is just 4. You know, but the funny part yeah. And I don't think, Of course, he's a very smart guy, but I don't think he knows what normal is for for any I guess part of it is, like, it's this stuff is such a fucking
[Speaker 3] [01:19:36] sewer. It's I mean, the best
[Speaker 1] [01:19:37] He's no clue though. He does not know that, like, the sewer that is being prevented 247, 365.
[Speaker 4] [01:19:44] Well, the best rant I not the best, like, threat I saw on Twitter about this was from the, former, you know, Reddit CEO. Yeah. And it was a little bit Yeah. It was good. It was a bit of, like, you know, if you're in the market recent, Elon Musk age of Gen Xers, like, your concept of the Internet is not what what it is.
[Speaker 1] [01:20:06] It's not what it is. Yeah. Did you see this thread, Adam? This is a very good thread about Oh.
[Speaker 2] [01:20:10] No. I didn't. Is this is this Alan Powell?
[Speaker 1] [01:20:13] No. No. No. No. This
[Speaker 4] [01:20:14] is No. No. No. It was it was, oh god. I forget his name before.
[Speaker 1] [01:20:19] Hold on. Let me take it on.
[Speaker 4] [01:20:21] But he really but he he nailed he nailed the issues in my opinion. And because, you know, you just sort of, now at the same time, do I think that, you know, Twitter has done, you know, the best possible job from like a product and productization perspective and really, you know, maximizing the value of what they have here? No. Like, not at all. I mean, it's it's it is it's one of these, like, cockroach of the fucking Internet.
[Speaker 4] [01:20:55] You can just stomp on it over and over and over again, and you can do stupid fucking products and kill them. You can buy Vine and stop it. You can do, you know, all the sort of I I mean, like, Vine's a good example. Okay.
[Speaker 1] [01:21:09] Vine is a good example. Yeah. Vine is good.
[Speaker 4] [01:21:11] They had TikTok years before.
[Speaker 1] [01:21:13] They had TikTok. Yeah. Yeah.
[Speaker 4] [01:21:15] So yeah. You know what I mean?
[Speaker 1] [01:21:16] Well, and and the and then, like, I mean, just your earlier point about, like, them not being able to kill things. Like, the literally, users are inventing the features that are compelling, like retweets. Right? Retweets are user invented and Hashtags. Only begrudgingly adopted by Twitter.
[Speaker 1] [01:21:33] And so I think in the Biff Tannen scenario, this is where Twitter turns into Microsoft Tay, if you remember that. Adam cut.
[Speaker 2] [01:21:42] I I I can remember a name that I couldn't assign it a value. What is Microsoft Tay?
[Speaker 1] [01:21:47] Microsoft Tay is where Microsoft created this friendly bot that would be on Twitter and you would at Microsoft Hey things and Microsoft Hey would learn things and their speech would get better and better and better. But of course I mean, Microsoft Hey lasted on the open Internet for, like, 18 milliseconds and 18 milliseconds.
[Speaker 4] [01:22:06] It was it was
[Speaker 2] [01:22:07] it was just immediately. Right? No. There was no It
[Speaker 4] [01:22:09] went it
[Speaker 1] [01:22:10] went crazy racist. People crazy racist.
[Speaker 4] [01:22:14] People purposefully fed it that. Fed it. Yeah. That way. Yes.
[Speaker 4] [01:22:18] Because that's how, I mean, the funny part is, you know, because Elon Musk is a little bit trolly, but, like, he doesn't even under I don't know if Tom would even really appreciates the level that some people have brought the art of trolling to.
[Speaker 1] [01:22:32] He he he is such an amateur from a trolling perspective, and he has got no idea, the professionals, the preteen professionals, the 14 year old professionals that are going to troll him under the table. So what they figured out, Adam, in particular, is if you at tweeted Microsoft Tay, you could then feed it a bunch of additional information that wouldn't be displayed, but would be factored into the model. So that's where you just read this thing like the most unspeakably racist things that humanity has ever imagined.
[Speaker 4] [01:23:12] I've I've never seen, like, a a software system basically spit out Hitler and hard r's and, like, a somewhat, you know, like, you know, an an actual fucking sentence. I mean, it's just I mean,
[Speaker 1] [01:23:28] it is, like, If you're a Microsoft execrating this, you're like, cut the power to the data center. It's that bad.
[Speaker 3] [01:23:33] Oh, yeah.
[Speaker 4] [01:23:33] You're just
[Speaker 1] [01:23:34] like, we'll deal with all the records that creates. It was very, very bad. So I but I think that the in in this world, I think that where it looks like there's no kind of floor. It goes full, absolute free speech, bonkers, Bifthann and bonkers, and brands all pull. Like, because then you're gonna have, like, McDonald's and Starbucks and United Airlines all the time.
[Speaker 4] [01:23:57] Saying that they
[Speaker 2] [01:23:57] then they can't advertise. They can't get any revenue.
[Speaker 1] [01:24:00] Then they right. And then they they pull up the platform and then I think you see them. I I think you will see in that I also see.
[Speaker 4] [01:24:06] I I'm a bit more positive.
[Speaker 1] [01:24:10] I think that is positive. Isn't that possible?
[Speaker 4] [01:24:12] Impression of Elon Musk is that, you know, he's not he's not dumb. He just may not know something right now, he seems to always run a certain process to learn. And if he sat down and sort of got a bit of an education on the fact that there are nation states attempting to sway elections or people that are actually the targets of crime or, you know, all of those you know, I don't see him, ignoring those or, you know, like somehow changing those or the like, And, and in a lot of ways, you know, he doesn't have a history of really doing bad investments either. Right? I mean, the guy makes more money every year from stuff that he does.
[Speaker 4] [01:24:58] And so, you know, and I think a lot of it's be he just bought this for, you know, $44,000,000,000 And I think in his mind, Twitter should be worth 200, 300, $400,000,000 And, I think they'll actually work on some ideas that'll potentially make it that.
[Speaker 2] [01:25:18] You think it was his childhood with his folks owning the Emerald Mine? Worldview? Yeah.
[Speaker 3] [01:25:25] Well, and and subsequent experience with, you know, with the building the Hyperloop that's now in operation and and, the battery, the pow wall that's in every home and Yeah.
[Speaker 1] [01:25:37] I'm joining this Twitter space from the hyper I was going back and forth from San Francisco to LA in the hyperloop for this entire time job. I've I've taken I've taken 12 class.
[Speaker 3] [01:25:44] Yeah. Presumably using using the installer link to access DNIS. Right? I mean
[Speaker 4] [01:25:49] Yeah. That
[Speaker 1] [01:25:49] that And and I
[Speaker 3] [01:25:50] assume you, actually, you're joined through your neural interface.
[Speaker 4] [01:25:53] Well, that's what I mean. I mean, I I don't.
[Speaker 3] [01:25:55] Good track record
[Speaker 1] [01:25:56] is what it's your to John.
[Speaker 4] [01:25:57] No. It's just the guy, I I don't see him spending $40,000,000,000 to just throw it away. I think he actually spent the money to make more money.
[Speaker 1] [01:26:06] But I think he's gonna get bored. I think that that it's gonna be I think if it doesn't go full Biff Tannen, which will be, I think, actually kinda mesmerizing because I think this thing can unspool crazy fast. And we which you have seen the other social media can unspool really, really quickly.
[Speaker 4] [01:26:24] I'm gonna I'm gonna just I'm gonna triple down on what I just keep on saying and that is that there is nothing that anybody can do. Stop Twitter from existing. Not even Elon Musk can fuck up Twitter. Okay. Elon Musk.
[Speaker 1] [01:26:41] That that that's a that's a good idea. Okay. So another scenario I've got for you is
[Speaker 4] [01:26:45] No. I just
[Speaker 1] [01:26:47] The the PeopleSoft scenario is he comes in and just, like, absolutely decapitates everyone who's got a level of, like, director or above, replaces them with cronies, and then walks away.
[Speaker 4] [01:26:58] Yeah. But that would be it's a good example that not a single person that currently works at Twitter is required for Twitter's survival of existence.
[Speaker 1] [01:27:07] That's not true. We've got some people in this space or place of Twitter who are absolutely very clever.
[Speaker 4] [01:27:12] Twitter is this autonomous
[Speaker 2] [01:27:14] Present company.
[Speaker 1] [01:27:15] Present company excluded. No. Please.
[Speaker 4] [01:27:16] Twitter Twitter is this autonomous we, like, sentiment being just can exist on its own. Nobody can fuck it up.
[Speaker 1] [01:27:25] Okay. So Twitter Spaces. What do you think is gonna happen with Twitter Spaces?
[Speaker 4] [01:27:28] Then? I have no idea. I didn't even know it existed until you literally DM me. The the best kept secret. I didn't.
[Speaker 4] [01:27:35] I I I you know, the funny part was it took me a couple minutes to get on here because I had to download the Twitter app to my phone. It's terrible. My phone either.
[Speaker 1] [01:27:44] It's terrible.
[Speaker 4] [01:27:44] So, I mean, next year
[Speaker 2] [01:27:47] in Clubhouse? I mean, are are we gonna see, you know, other social Clubhouse is
[Speaker 5] [01:27:51] a fun one.
[Speaker 2] [01:27:52] Is like a thing.
[Speaker 4] [01:27:52] Clubhouse is a funny one. Someone it was, god. Who is it? I think my oldest daughter mentioned Clubhouse to me, and I was like, you're not going on Clubhouse. And she's like, what's it, man?
[Speaker 4] [01:28:02] I go, that's the one that people go and, you know, like, they they they chat and masturbate like that one. She's like, no. That's it. I'd I'd somehow somehow I'd I'd made, like, Clubhouse and The same yeah. No.
[Speaker 4] [01:28:17] Exactly. But they just blend it together into this one dad moment where I was like, you're not going on there. People just sit there and masturbate on video. She's, like, that's not it.
[Speaker 1] [01:28:27] Oh, wait. It's this.
[Speaker 4] [01:28:28] And I was, like, oh.
[Speaker 1] [01:28:29] Oh, so
[Speaker 3] [01:28:30] they're they're not cameras.
[Speaker 1] [01:28:31] And and meanwhile, she's like, what the hell are you thinking of? Like, what's your problem? Yeah. But yeah. You're like, no.
[Speaker 1] [01:28:37] No. No. It's just cat roulette. It was a thing. I'm you know, don't go there.
[Speaker 1] [01:28:40] Don't go to chat roulette. I'm really sorry I thought about it.
[Speaker 4] [01:28:42] No. But once I, you know look. My once once I once I sorta had, you know, like, direct experience and, you know, these platforms being used to, you know, turnover governments and that kind of thing as we were heading through 2,008, 9, and 10, it just became less interesting to be on these in my opinion. I think you have my tweet volume in the last decade. It's basically non existent.
[Speaker 1] [01:29:11] True. So I and I then I think that the I mean, I think there's a possibility that Twitter gets marginally bad. There? Maybe I maybe this is the story that you're talking about, Jake. That that you'd be Yeah.
[Speaker 4] [01:29:24] Yeah. I think it will.
[Speaker 1] [01:29:25] I Matt, what's your what's your take? So you got your hand up.
[Speaker 5] [01:29:34] So I was just thinking if, if Twitter does go downhill and and have you guys started, thinking about possible alternatives to, to doing these chats on Twitter spaces?
[Speaker 4] [01:29:48] Yes.
[Speaker 5] [01:29:48] So I mean
[Speaker 1] [01:29:49] Yeah. Right. We're we're not gonna be on Biff Tannen's platform. So so here's my hypothesis. Feel free we we can kinda check-in on this one after a a couple of months, of the kind of the post Elon Twitter.
[Speaker 1] [01:30:01] I think, again, this is, like, not gonna be close. I think this so the platform is gonna stay, like, largely the same or get so bad so quickly that nobody can stay on it. And in that model where it gets very bad very quickly, other things are gonna appear. I think because the I the fundamental nugget of the idea is so important and so good. I think that that we may actually we may be in one of these moments.
[Speaker 1] [01:30:26] It kinda reminds me of, like, when the polarity of the Earth switches, which had just happened many times over geologic history. It's not I last time I checked, anyway, it's not probably clear why this happens, but it hap does happen very quickly. It's very non it it's nonlinear, and once it starts to happen, it flips very quickly. I kinda feel like we have seen movements where, like, Friendster did die.
[Speaker 2] [01:30:51] Right. Friendster, Myspace, Facebook. Right?
[Speaker 1] [01:30:53] Right. Livejournal does happen. And and so it's
[Speaker 4] [01:30:56] But I'm talent. But I'm but I'm there's been so many challenges to Twitter, and we'll do sort of here and there. It's like every fucking year, even without Elon Musk doing it, there's always some Twitter killer that basically existed. But but, Jason, I
[Speaker 1] [01:31:09] agree with you. But the the problem is that Twitter has been, like, okay. And and in a world where Twitter has gone, like, full Microsoft hay and people have to leave the platform. That's, I think, a different world.
[Speaker 4] [01:31:24] I don't think it's gonna happen.
[Speaker 1] [01:31:25] I think that's I kinda I kind of think I hope it doesn't happen. I don't know what I've what I want.
[Speaker 4] [01:31:30] No. I just I think it's it's, I don't know why anybody in their right mind would sit down right now and say, hey, you know what? I'm gonna start a company and we're gonna be, like, the thing that replaces Twitch.
[Speaker 1] [01:31:43] I think it's a great thing to do right now.
[Speaker 4] [01:31:44] You know? Oh my god. It sound well, I mean, maybe for somebody, but, like, for me personally Right.
[Speaker 2] [01:31:50] For somebody else. I mean, are you investing in that company, Brian?
[Speaker 4] [01:31:53] That sounds about as as as painful as it could get.
[Speaker 1] [01:31:57] So I yes. I would. I so okay. This is why I'm not a venture capitalist, and don't worry. Like, I'm like that's what we're sticking with the consumer company for the foreseeable future.
[Speaker 1] [01:32:05] But I actually do think that the that would be an interesting bet to make if the team is right. And I think that there are some I think there's some folks inside of Twitter. I mean, watch for high profile resignations inside of Twitter that could actually go build a reasonable replacement having learned from it. I do think that those people absolutely exist, And that's
[Speaker 4] [01:32:26] I just you know, the thing is is, like, once you start because I think a lot of the, you know, the fact that Twitter itself has changed in some ways so little and there you know what I mean? It's not one of these things where there's like explosion of features or capabilities or anything else like that. There's always a sort of core set, like, you just like, it's always confusing to me how such a large product team can have such little output.
[Speaker 2] [01:32:52] I mean, just, I mean, just that, Jason. I mean, the the number of employees there and the number of visible features you see, the size of that building on Market Street Yeah. Compared with the number of things coming up the door is astounding.
[Speaker 1] [01:33:05] It,
[Speaker 4] [01:33:06] and then the way that I'm saying it, like, you would expect more output. Yeah. Yeah. Absolutely. And that's but I think the root of that though is and I'm not and, I mean, and I'm trying to give everybody there the benefit of the doubt.
[Speaker 4] [01:33:17] I've never actually worked there, but I actually think that it's an exceptionally complex product environment to be working in
[Speaker 1] [01:33:25] I agree. Yeah.
[Speaker 4] [01:33:25] You know, to where and what I mean is, like, you actually will go and say, well, you know, we have this idea here. But if you would take it through, like, all the consequences of it and what it would sort of go and be used at, you you always, like, basically, anything you do has got the possibility of being like that Microsoft tag. You know, it could, like, really just take it entirely off the rails, you know. And I and I think it's, I think being that type of I mean, you just looked at even I mean, I thought Twitter was popular. And then when you looked at how fucking Trump used it, And then the fact that it's Trump's off of it, and while it's still here, you know, everyone, you know, and, you know, and everything else.
[Speaker 1] [01:34:10] And then it's But, I mean, forget Trump. So if they let Trump back on, that means out No.
[Speaker 4] [01:34:13] I mean, it's it's very it's very it's very hard to do something like Twitter. I don't think it's an easy thing to do.
[Speaker 1] [01:34:19] I agree. I agree.
[Speaker 4] [01:34:20] Like Yeah. Yeah. Because because if someone sat down, like, oh, you know, come in here, you know, you get ahead of product. And if I sat down and, like, was really, you know, sat down and said, okay. Let's let's put the product manager head on.
[Speaker 4] [01:34:31] Let's dig through this. I'd I'd think I'd start going through it being like, oh, this isn't this is too hard.
[Speaker 2] [01:34:37] Well, even even if you just even if
[Speaker 4] [01:34:39] you just had
[Speaker 2] [01:34:40] a a direct clone, then, I mean, you need to seed it with all the content, the users, and whatever. And building that seems like a monumental thing to
[Speaker 1] [01:34:49] So I am hoping that I not that you of course, you won't. But with all this slow with all this freedom talk, I would love to see a restoration of the Twitter API because that actually would that would allow people to leave faster. And that would allow and our and I'm just gonna say the quiet part loud.
[Speaker 4] [01:35:09] But I but I
[Speaker 1] [01:35:10] The so the that I think and if so if whether it's her or someone like her, if someone like Leah Culver were to start a who's currently a Twitter employee. If she were to start a Twitter rival, I think that that would
[Speaker 4] [01:35:26] She did start a Twitter rival twice.
[Speaker 1] [01:35:28] And 3rd time's a charm and the time is right. Oh. And and, like, spaces is a result of that that's so I think that there are people inside of Twitter that I would pay I mean, certainly, I would pay a lot of attention to that.
[Speaker 4] [01:35:43] Yeah. I don't know. They just may have, which I again, I think they may have a thing where, you know, it could be that the the new owner and the new ownership structure is more receptive to even letting them do the things they wanna do.
[Speaker 1] [01:35:56] That's another possibility, actually. Is it in terms of, like okay. So so a positive possibility is
[Speaker 4] [01:36:00] It's not it's not like, you know, it's not like, you know, you know, Tesla and other environments is like that. It's not like, those are bad products or bad product companies or have bad product approaches. I mean, relatively speaking no. I mean, I don't own a fucking Tesla, by the way. Yeah.
[Speaker 4] [01:36:21] There's there's, That's a super McBag. I'm gonna burn dinosaurs until, you know, I don't have to anymore. Well, I try to walk, I guess.
[Speaker 1] [01:36:31] Well, your dinosaur burner is much less likely to run itself into a pylon. Alright. So
[Speaker 4] [01:36:35] No. No. But but but but the but, you know, the Tesla you know what I mean? It's, like, it's it's it's, you know, they're not they're not shitty companies. So
[Speaker 1] [01:36:44] Alright. Well, I think we should, I I don't know. Adam, are you and I know you were getting in here for the other other Twitter predictions at at
[Speaker 6] [01:36:53] I just I just shared a tweet, into the space about the implications to employees, at Twitter today who count on our issues as part of their package and the uncertainty that lies ahead for, for those employees. And, in today's job market, the the, risks associated for Twitter with, potentially losing a large number in 4 years as a result of that uncertainty. I feel like the like, there is a likely scenario in which this is a sufficient distraction that nothing really changes over the foreseeable future. When I say, you know, it's the next 6 months or so. Twitter just is mostly the same because there will not be material changes to they won't be able to, like, muster enough people and, like, political clout within the company to be able to really change direction in the short term.
[Speaker 6] [01:37:58] I think it's gonna take a little while before anything really shakes out.
[Speaker 1] [01:38:02] Alright. Well, I I I think, again, I'm seeing the change of headquarters lock. So I think that's a that that that's a change you're gonna see. I think that that that's a hallmark of these kinds of hostile acquisitions is that really wanna send a message is that you you and and it wouldn't also surprise me to see things like changing the logo, other things that constitute burning the flag.
[Speaker 2] [01:38:26] I will I'll I'll put I'll put it on the line and say predict a either a direct listing or an IPO within 3 years.
[Speaker 3] [01:38:33] You mean going back to public?
[Speaker 2] [01:38:36] Yeah. I mean, but but with a different structure potentially. I mean, or at least that And a and a That's the result
[Speaker 4] [01:38:41] of what the Ian was saying. Market cap. Yeah. And a higher market cap. Right.
[Speaker 1] [01:38:46] Okay. Then I I I actually do think that the the other kind of wildcard in here is this is actually a lot of money. That's a lot of it is debt. It's being Exactly. Collateralized with with Tesla stock.
[Speaker 1] [01:38:57] There's some nonlinearities here that that could unfold. If this thing doesn't go well, it thinks other things could unspool. But I, so you your prediction is an IPO in 3 a decade, and it's sold for less than it than it it's being bought for now. Like, because I think that the I I think it's gonna be but I don't know. Maybe I I think Yvonne's gonna get bored of this.
[Speaker 1] [01:39:33] I think I think this is not fun. It's gonna be hard.
[Speaker 4] [01:39:35] But, like, you guys, would you guys rather would you guys, like, you guys personally, would you let's say, would you rather work at a Twitter that's run by Jack or a Twitter that's run
[Speaker 1] [01:39:44] by Elon?
[Speaker 3] [01:39:45] What's Ocean City?
[Speaker 2] [01:39:47] Yeah. Right. I mean, I guess Yeah. I guess, I of those Definitely. I'd say I'd say Jack, but also Jack with the board of directors as opposed to Elon and, you know, the emperor walking in every day, with some new good idea.
[Speaker 4] [01:40:01] Yeah. Like, who who if if they said they hadn't said anything about who's gonna be running Twitter. Right?
[Speaker 6] [01:40:07] No.
[Speaker 1] [01:40:07] No. Alright. No. But, put me down for Antonio Garcia Marquez Martinez rather running, the Facebook guy.
[Speaker 4] [01:40:17] Oh, yeah. Well, that makes sense. So
[Speaker 1] [01:40:20] the the That's a good prediction. Yeah. That that would be pretty consistent, and he would be the kind of velociraptor that I think that, Elon wants to feed Twitter middle management to.
[Speaker 4] [01:40:31] I just I just I just so can't believe that he worked a 4 20 joke into his share price. I mean, imagine having that much money where you look at it and it's like, well, it's really worth $49 when you go, hey. Can we bump it to 5420 to make a 4 20 joke?
[Speaker 1] [01:40:50] It's scary to me.
[Speaker 4] [01:40:52] I mean and I get but I guess I guess 69.42 was too high. I mean, like, he's just making marijuana and sexual position jokes in all of his share price of
[Speaker 1] [01:41:04] Pretty much. I I I I would say it's as if a 14 year old bought Twitter, but my I I I think the 14 year olds have got a
[Speaker 4] [01:41:09] more specific sense of humor, I gotta say. Yeah. So Yeah. Yeah.
[Speaker 1] [01:41:13] Alright. Only time only time will tell. Jason, thank you very much for joining us and taking us on a walk down memory lane with the, I thought we used to be donning our authentic 2,005 and 2006 garb, Adam.
[Speaker 4] [01:41:25] Yeah.
[Speaker 1] [01:41:26] This reenactment of the, early web search.
[Speaker 4] [01:41:30] Put on one of my put on one of my brown scale with rail t shirts.
[Speaker 1] [01:41:35] That's right.
[Speaker 2] [01:41:35] There you go. Yeah. Thanks, Jason.
[Speaker 1] [01:41:38] Awesome. We got mess. We're gonna have a great space next week. 2 of our colleagues, are gonna be, who each have separately debugged really interesting issues. Luke and Aden and, and Jordan Hendrick's gonna be here describing, their their methodology.
[Speaker 1] [01:41:55] It's gonna be a lot of fun. I don't know. I'm really looking forward to that one, Adam. So that'll be Yeah.
[Speaker 2] [01:41:58] It's gonna be great.
[Speaker 1] [01:41:59] It'd be great. So join us next week. Thanks, everybody.