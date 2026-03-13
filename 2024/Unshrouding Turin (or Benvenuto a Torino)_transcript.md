[Bryan Cantrill] [00:00] Noticed that you, you changed out the title.
[Adam Leventhal] [00:02] You you you did not like my No.
[Bryan Cantrill] [00:04] Okay. Yeah. Go ahead.
[Adam Leventhal] [00:05] Go ahead.
[Bryan Cantrill] [00:06] Alright explain yourself
[Adam Leventhal] [00:06] Here's where I wanted to start. I love your title.
[Bryan Cantrill] [00:08] Okay. I I I mean, why would I mean, why would someone say, obviously, I love my title. I love your title. There's a butt coming.
[Adam Leventhal] [00:16] There's not a there's not even a butt coming. Like, I
[Bryan Cantrill] [00:20] listen, pal. We've been rejected by enough VCs. I I know a breakup male when I see it.
[Adam Leventhal] [00:24] No. Like, unequivocally, I love it. Period. The end.
[Bryan Cantrill] [00:28] We love meeting oxide. We're very excited about oxide. Okay. Yeah. Go on.
[Adam Leventhal] [00:32] Yeah. Look. No. I'm not cheering from the sidelines. I wanna be in the game.
[Adam Leventhal] [00:36] I'm with you. I'm in the game.
[Bryan Cantrill] [00:38] Okay. Go on. So you love No. That's it. I My subplot title was I love unshrouding terrain.
[Adam Leventhal] [00:44] Yeah. Love it.
[Bryan Cantrill] [00:46] But I noticed the title here is is Benvenuto Aterino.
[Adam Leventhal] [00:51] That was for Robert.
[Bryan Cantrill] [00:52] That was for Robert.
[Adam Leventhal] [00:53] I thought he'd enjoy that more. Robert, which one do you prefer?
[Bryan Cantrill] [00:57] Oh, put Robert on the spot.
[Bryan Cantrill] [00:59] Go ahead, Robert.
[Robert Mustacchi] [00:59] (Speaks in Italian)
[Bryan Cantrill] [01:01] Oh, yeah. There we go. What what what an all pro. You know, you this reminds me of this reminds me of, when my now 20 year old was 4. He, we understood from one of his friends in the neighborhood that, he and this girl were gonna get married.
[Bryan Cantrill] [01:21] And they were like, okay. That seems like a little bit heavy for 4. And we were talking to another parent at the preschool, and she was saying that her daughter and Tobin were gonna get married. Oh my god. This kid's a real gets around real gigolo here.
[Bryan Cantrill] [01:37] Well, as long as as long as, you know, he's got his I guess he's got, you know, when you're a 4 year old, I guess you have a a playmate in every port. And we are at the beach. We're at Crissy Field with one of these girls, and the other girl comes up.
[Adam Leventhal] [01:54] Oh, man.
[Bryan Cantrill] [01:55] Oh, and you're like, okay. What and I'm reminded a little bit of, Robert on the spot over here. And like Robert, the but my my 4 year old takes the hand of 1 of the girls, takes the hand of the other girl, and then the 3 of them all go running off together. Delightful. I'm like, alright, you know, go for it.
[Adam Leventhal] [02:18] You're like, I'm just gonna write this down to tell at your wedding.
[Bryan Cantrill] [02:21] Yeah. Absolutely. Or or weddings. I mean, who's to say that this you know, I I who's to say that the, this will carry into adulthood. Yeah.
[Bryan Cantrill] [02:29] So I'm raising a bigamist. Anyway, I so I am regardless of the title and and who it was designed to appease, I am very we're very excited to be talking about Turin and the Turin launch. This is AMD's latest part. George, thank you very much for joining us. Really appreciate you're a you are a a repeat, friend of Oxide.
[Bryan Cantrill] [02:47] It's good to have you back.
[George Cozma] [02:49] Good to be back. Excited to be here.
[Bryan Cantrill] [02:52] So I got a so you had a you had a great blog entry that, I I I was excited to see it at the top of Hacker News over the weekend. A lot of were you surprised by that?
[George Cozma] [03:06] No. I've noticed that Hacker News has been picking us up more and more.
[Bryan Cantrill] [03:11] That's correct.
[George Cozma] [03:14] And, ironically enough so we we recently moved over to Substack, and we noticed that seemingly the SEO for Substack is a lot better. So we that article got a lot more traction.
[Bryan Cantrill] [03:34] Oh, interesting.
[George Cozma] [03:35] So I it being at the top of multiple sites I mean, other sites doesn't surprise me.
[Adam Leventhal] [03:41] You know, it may maybe the SEO, it may just
[Bryan Cantrill] [03:43] be also that you just got a a great article on a hot topic. You know, this could be
[George Cozma] [03:47] Yeah. And what's funny was the video actually did really well.
[Bryan Cantrill] [03:50] So okay. I'm glad you
[Adam Leventhal] [03:51] brought up the
[George Cozma] [03:51] video. At oh, so the the the there was the video part of the article.
[Bryan Cantrill] [03:57] No. No. I'm glad you brought it out because those you the comments on that video were the nicest YouTube comments I've ever seen in my life.
[George Cozma] [04:07] Yeah.
[Bryan Cantrill] [04:10] I I I need to know YouTube comments could be nice.
[George Cozma] [04:13] Yeah. And and most, what I've noticed is that, so you guys can't see the like ratio, but, it it currently has a 100% like ratio.
[Bryan Cantrill] [04:26] I mean, what is going on? This is this can't be a YouTube video.
[George Cozma] [04:29] No idea. I it's not YouTube.
[Bryan Cantrill] [04:31] It's not YouTube. There's something this thing has fallen into some alternate reality and, like and the comments are all, like, you know, thanks for all of your diligent work and, you know, I just I I mean, just it's great. God. Like, we talk about lightning in a bottle. I don't know if you saw these, Adam, but it was just like I had
[George Cozma] [04:47] I think a lot of it is because, like I mean, we what? Last month or the just the month before, Anantec closed? Yes. Yeah. Their hat for the last time.
[Bryan Cantrill] [05:03] A lot of
[George Cozma] [05:04] the older folks like Ace Hardware Review, Real World Tech, David Canter doesn't really write anymore. So a lot of the in-depth stuff has sort of disappeared over time.
[Bryan Cantrill] [05:16] Yeah. So you think that this has given the Internet some gratitude. You you've managed to domesticate the Internet. More
[George Cozma] [05:26] more so that I think people want an alternative to that that really goes in-depth.
[Bryan Cantrill] [05:35] Well and look. It was like a if there was a if there was a YouTube video that we're gonna start having nice comments on,
[Adam Leventhal] [05:41] that was a good one to start on. That was a great
[Bryan Cantrill] [05:42] great great video, went in-depth. I love that you kinda had the the the the surprise ending where you, you set a a a world record in your hotel room. Maybe we should let's start with air. What was that benchmark that you were running? And you were you were running that on Turin, obviously.
[George Cozma] [05:59] So so that was, YCruncher, a 100,000,000,000, b p t, b b b b b p, excuse me. It's hard to say. But, basically, it it all it does is it's a compute benchmark. So it just wants as many threads and as high clocks as you can get. It's not memory bound at all.
[George Cozma] [06:28] But the prior record at the time of that video was about 10 seconds, and that was a sub five second result. And I see Jordan in the, chat or as one of the audience members, he was running it with, someone else in the room, Jeff from Craft Computing and I was I was doing my video and I see him in the in my eye trying to wave this laptop, I'm like, I couldn't really say anything. I was like, what's going on? And he's like, do do you wanna show the audience that we just broke a record? I'm like, okay.
[George Cozma] [07:00] Completely unplanned. I had no idea that was going to happen.
[Bryan Cantrill] [07:03] Oh, it's pretty great. It it was pretty great and I love that you're, like, kinda wrapping it up. You're like, no, no, actually wait a minute. Hold on. I'm not being I'm not this laptop just being handed to me.
[Bryan Cantrill] [07:11] We hope that's a lot of
[George Cozma] [07:13] Wait. There's literally, I pulled I pulled the Lisa Sue. Wait. There's more.
[Bryan Cantrill] [07:16] There's more. Yeah. Okay. So and, obviously, that, setting and the it it's helpful to know this is a very, compute intensive workload. Because I'm one of the things that I think that we've heard from a bunch of folks is this thing is so much more compute that it now you've gotta really ask questions about balance of the system and memory bandwidth and so on.
[Bryan Cantrill] [07:35] So I wanna get into all that. I guess one thing I would kinda ask you from the top, just what is your kinda top takeaway from the Turin launch, and was there anything that surprised you? Was there anything that you either didn't know what was coming or didn't know the kind of magnitude or you're still yeah.
[George Cozma] [07:55] Sort of three things here, if you don't mind. What surprised me most about Turing specifically was, 1, the fact that they hit 5 gigahertz on some skews Yeah.
[Bryan Cantrill] [08:07] I was gonna
[Robert Mustacchi] [08:07] say on a
[George Cozma] [08:07] server CPU.
[Bryan Cantrill] [08:08] Yeah.
[George Cozma] [08:10] But not just hit 5 gigahertz. Like I wrote in the article, Wendell from level 1 text in a in a, essentially, web server workload was hitting 4.9 gigahertz all core. That's nutty. That's utterly, utterly nutty.
[Bryan Cantrill] [08:28] That is crazy. Because I feel like the last time we were released it's been a minute since we've seen clocks that high from anywhere, I feel. I feel it's been like I mean, IBM was hitting you with power.
[George Cozma] [08:39] Yeah. Well, no. IBM c is the only are really the only folks that do that sort of over 5 gigahertz consistently in server. Intel back in the day, if you remember those black ops CPUs, they were doing 5 gigahertz. And I believe that there was 1 the last Oracle Spark CPU, the m's the m 8 went up to 5 gigahertz.
[George Cozma] [09:04] Right? But other than that, it's like, I'm having I'm having to, like, draw upon, like, some fairly niche CPUs here. Right. The fact that what is effectively a mainstream CPU can do this is not is crazy. But add on to that, just the fact that Zen 5 c, so sort of those compact cores Yeah.
[George Cozma] [09:27] Yeah. Have a full 5 12 bit FPU.
[Bryan Cantrill] [09:30] Yeah.
[George Cozma] [09:31] I I think that that's really impressive considering that they're sticking 16 of that get to a single CCD now.
[Bryan Cantrill] [09:40] Yeah. So let's elaborate on this a little bit because this is, I think, a a really interesting point that that that so because we're seeing this from Intel too. Right? Where in order when once you get the density up to a certain level, you've gotta make some compromises. But the compromises that AMD seems to be making are much less than the compromises you're seeing.
[Bryan Cantrill] [09:58] I mean, the Zen 5 c cores are they're they're still Zen 5 cores.
[George Cozma] [10:03] Yeah. So so here's here's the difference between Zen 5 and Zen 5 c from an architecture perspective. Nothing. Once until you hit until you hit l 3, there's no difference.
[Bryan Cantrill] [10:17] Yeah.
[George Cozma] [10:21] Now are they on different nodes? Yes. Is there an f max difference? Yes. But the fact that they're still hitting 3.7 f max, so that's your top clock, is really impressive.
[Bryan Cantrill] [10:35] And the node difference is, I think, you're on, what, 3 nanometer for the 5 c and 4 nanometer for the Yes. The Zen 5. Is that right? Yeah. These are all TSMC, obviously.
[George Cozma] [10:43] So on their c course, they jumped, 600 megahertz. So from 3.1 to 3.7.
[Bryan Cantrill] [10:51] God. That is amazing.
[George Cozma] [10:52] Yeah. Yeah. And and I there was a good point made, and I think the biggest jump in in recent Andy history in terms of the server performance is not Zen 4 to Zen 5. It's Zen 4 c to Zen 5 c.
[Bryan Cantrill] [11:10] Interesting.
[George Cozma] [11:11] I think Yeah. That performance jump is far from like, I think that that's really, really exciting. But what I really like about TURN is not just that there's these big old high end SKUs, the 128, and 192 core SKUs, but they've paid attention to this mid range. Right? With the 95, 75 f, that that's a high frequency 64 course queue that I was talking about that was getting 4.9 from Windows testing, on all cores.
[George Cozma] [11:48] I think that that sort of cue, the fact that they still are paying attention to the sort of the midrange is is really good. It's expensive, no doubt, but
[Bryan Cantrill] [12:02] Yeah. Yeah. And and the fact that you've got this kind of SKU stack now that is kind of a a uniform SKU stack where you can start to really make some interesting trade offs as you look at Mhmm. At workload. And it just it it feels like, you know, because and Robert here is is our our resident, SKU Stackologist, which definitely I mean, there were times with Intel where you've got, like, these 3 different where you have, like, gold, silver, and platinum, and you've got Also bronze.
[Bryan Cantrill] [12:32] With bronze. Right. And it just Yeah. It it did require, like, you to get a post doc to figure out, like, which one you want. And, Robert, what do you make of this of this Turin SKU stack?
[Bryan Cantrill] [12:44] I mean, it seems like it's a it it it's a pretty clean SKU stack in terms of making different trade offs as you go up and down it.
[Robert Mustacchi] [12:49] Yeah. I think AMD's biggest strength is the fact that you're basically only choosing the number of cores, what the frequency is, and, you know, cache size. Otherwise, all the other features are the same. And I think that actually ends up being pretty powerful. You're not getting to a case where it's like, oh, do you wanna have fast memory?
[Robert Mustacchi] [13:04] Different skew. Do you wanna have Right. A different, do you wanna have RAS features? Oh, sorry. That's gonna cost you.
[Bryan Cantrill] [13:10] Yeah. That's gonna cost you.
[Robert Mustacchi] [13:11] Right? So
[Adam Leventhal] [13:12] you're not having to make trade offs. You kinda you kinda take from the buffet, table, but you're not needing to compromise. Is that right?
[Bryan Cantrill] [13:20] Yeah. I mean, certainly and I think that that the you know, when on the Intel side, when you go from these p cores to e cores, Adam, you're going from the p is for performance and the e is for efficiency.
[George Cozma] [13:32] You're like, uh-oh. As, so Macurray from Joe Macurray from AMD put it economy course.
[Bryan Cantrill] [13:43] Economy course. I
[Robert Mustacchi] [13:45] when he
[George Cozma] [13:45] said that on stage, I was Ian and I were laughing were laughing for about 5 minutes straight. That's really good.
[Bryan Cantrill] [13:52] Yeah. And well, because in particular, like, you don't have AVX 512 on those on
[Robert Mustacchi] [13:56] I mean yeah. That that's the most shocking bit to me is that you basically still never despite Intel championing it and trying to put all that energy into everything over the years, you still just got nothing.
[George Cozma] [14:06] And I let's just say that's that's something I've harped on Intel about is they really the fact that they now have an ISA segmentation
[Bryan Cantrill] [14:16] Yes. Yeah. Is bad. It's bad.
[George Cozma] [14:18] Don't segment your ISA, please. Yeah. Like, that's that's how you shoot yourself in the foot something fierce.
[Adam Leventhal] [14:26] And and just to elaborate on that, so what that means is, like, the operating system needs to make scheduling decisions within the same Yeah. Like, chip about whether certain workloads can can run on certain of the cores. Is that right?
[George Cozma] [14:42] Not on so on the client side, yes. That's true. On the server side, that's not correct. The serve all server chips have the same cores. So there are 2 Xeon 6 lineups, the Xeon 6000p's and the Xeon 6000b.
[George Cozma] [14:58] The e's are for the e course and the p's are for the p course. There's no merger of course like Just to be clear,
[Bryan Cantrill] [15:05] it's like it's like Ryanair. It's like all economists on this one. And they're all heavy.
[George Cozma] [15:11] But but the thing with that is and here's sort of the cleverness of Zen 5 versus Zen 5 c, and that is AMD can just have one big SKU stack and that's it. Yeah. Intel, you need these 2 different SKU stacks, and it can start getting confusing with what has what and where.
[Bryan Cantrill] [15:32] Well, and then it's like so it's it's really tough too because if you are, you know, in in in our position of, like, we are we are selling a rack scale computer to someone who's making compute available to their kind of customers, You know, we're asking, you know, if you if you have to ask them, like, why are you using AVX 512? Be like, I don't know. I gotta go I have to ask my users that. And, you know, it it it makes it really hard and you're kind of at this big fork in the road. So to to be able to have a to not have to give up, I mean, just as you said, George, to not have to compromise on ISA and to get the same ISA everywhere.
[Bryan Cantrill] [16:11] And, yes, you may be giving up, you know, the the you're making some trade offs in terms of max frequency and so on, but you're not, like, dropping off on foot.
[George Cozma] [16:18] Trade off is an area. Right. Right? Yeah.
[Bryan Cantrill] [16:21] Yeah.
[George Cozma] [16:21] You you
[George Cozma] [16:21] have to spend that area. But the the the thing here is I think the area would be even if it was a bare bones implementation, I don't know if you guys remember Centaur Centaur c, CNS. That was if you guys remember Via, that was a Via, CPU that would that never actually hit market, but you were able to test, thanks to a couple guys who acquired some during the Centaur, buyout days about 3 years ago. It had a very basic and bare bones AVX 5 12 implementation. Okay.
[George Cozma] [17:09] Is it but I feel like fine.
[Bryan Cantrill] [17:11] I feel like the last time you were on, I was getting a bunch of grief for dropping some dated references. Sentra, this is an old part, just to be clear.
[George Cozma] [17:19] Well well, here's the thing. Right? It's an old part, absolutely. But Intel bought the team and Uh-huh. I I don't we don't quite all we know is that it was essentially an Accu hire.
[George Cozma] [17:32] They got the folks from Centaur, 3 years ago.
[Bryan Cantrill] [17:38] Oh, so this is a recent thing. This is not Centaur No.
[George Cozma] [17:41] No. No. No. So Centaur was broken up essentially in 2021 as the Wikipedia article says. Via still has x86 licensing, but the Centaur team isn't at Via anymore.
[Bryan Cantrill] [17:54] So this was in 2021. So the I assume you were, like, you were talking about the, like, the okay. This isn't you're not talking about a chip that was made in, like, 19
[Robert Mustacchi] [18:04] No. No.
[George Cozma] [18:04] No. No. No. I'm talking about a chip that was date that was due for release in 2022.
[Bryan Cantrill] [18:11] And they were
[George Cozma] [18:12] broken canceled just before launch.
[Bryan Cantrill] [18:14] Okay. So alright. Well, I've got so many questions about this Wikipedia page. So they were broken up. First of all, like, nice use of the passive voice.
[Bryan Cantrill] [18:21] Like, they were like, what broke them up?
[Robert Mustacchi] [18:24] So The iceberg. The iceberg broke the So
[George Cozma] [18:28] Via Via Via, who was the parent company, what basically shuttered the Interesting. The Austin headquarters
[Robert Mustacchi] [18:39] Yeah. And then
[George Cozma] [18:40] sold and and and the team was acquired by Intel for a $125,000,000.
[Bryan Cantrill] [18:46] That's a lot of new hire.
[George Cozma] [18:49] Yeah. The here's the thing. It was very quick. Nobody was expecting it, and it was very the information that has been shared about it has been close to 0.
[Bryan Cantrill] [19:04] Interesting.
[George Cozma] [19:05] And if you ask anyone that formerly was there, they they don't say anything. It's it's kinda weird.
[Bryan Cantrill] [19:11] Oh, wow. Okay. Interesting. And so then and Via I didn't realize that Via was an x86 license holder.
[George Cozma] [19:16] So they they had licenses from IDT, which is what Centaur used to be, and Cyrex because they acquired Cyrex.
[Bryan Cantrill] [19:25] Right.
[George Cozma] [19:27] So they had license again. I think they still technically do, and which is how Xaoxing, which is a Chinese x86 manufacturer, has the ability to make x86 CTUs, which that's a whole history out of itself. I
[Bryan Cantrill] [19:46] I just I god. Thank you for opening up all of these doors. Did you see this? No. There's this documentary, the rise of the centaur, covering the history of the company.
[Bryan Cantrill] [19:55] It's like, okay. That's not that's must see TV. How I mean
[George Cozma] [20:02] so but the reason why I brought them up is because their their what was supposed to be their newest core, CNS, was supposed to have had ADX 512 capabilities, was a very bare bones implementation of ADX 512.
[Bryan Cantrill] [20:16] Oh, interesting. Okay.
[George Cozma] [20:17] And if the ecourse had had a a bare bones implementation, I think that would have been fine. It does have to be good. It just has to be there.
[Bryan Cantrill] [20:28] Yeah. Interesting. And the fact that it's not there at all really does it is as you say, it's a separate ISA.
[George Cozma] [20:34] Yeah.
[Bryan Cantrill] [20:35] Is that a good segue to the AVX 512 improvements on tourniquet? I mean, that that I felt like going into this launch, I mean, I felt that's one of the headliners was the improvements to the DX 512.
[George Cozma] [20:49] And if you want an even deeper dive, Alexander Yee, the creator of, YCruncher, did a very good write up on on zed 5's AVX 5 12 implementation.
[Bryan Cantrill] [21:05] Oh, yep. And
[George Cozma] [21:09] he he went very, very into it and basically said, yeah. This is this is the best ADX 5 12 implementation so far. Yeah. Really. There are some Yeah.
[Bryan Cantrill] [21:23] Check and it's
[George Cozma] [21:24] There's some
[Bryan Cantrill] [21:25] The data path is obviously a big part of that, I assume. The the fact that it's going from a 256 bit wide data path to a 500 bit wide data path or or or deeper than that.
[George Cozma] [21:33] That's part of it. Interesting. That's part of it. Another part is just the increase in the number of registers. They doubled the number of registers.
[George Cozma] [21:46] They made a lot of ops single cycle, which is nice. There were some trade offs that were made. Some of the integer stuff was made to cycle, which was a bit of a cavity in the tooth, so to speak, flying the ointment. But other than that, it's the way that AMD can just not have to so with Intel, you always had that sort of clock offset where if you run any AVX 512 code, you would suddenly decrease in your clocks. Right?
[George Cozma] [22:29] AMD doesn't have that. How they accomplish that, I have no idea, But the but you can throw it AVX 5 12 instructions, and while you'll have thermal and power, like, clock speed, pull back, it won't have this turbo clock thing where you have where where if you introduce any AVX 5 12 instructions, even if they're just load and store instructions, they'll decrease the CPU clock regardless. You don't have that with with Zen 5 or Zen 4 for that matter.
[Bryan Cantrill] [23:10] And was that on was that Sandy Bridge or Haswell, Robert, where it was like a a v I mean, AVX512 has always been kinda had this kind of problematic property that if one thread starts using it, it kind of, like, browns out the rest of the part.
[George Cozma] [23:23] It's Skylake.
[Robert Mustacchi] [23:24] Skylake is what did that, but you also had this problem on Broadwell with AVX 2 and the others. And Yeah. It's actually is worse than just running an instruction. If you actually just leave the, AVX 5 the AVX save state bit, such that Intel thinks it's modified in the register state
[Bryan Cantrill] [23:42] Yeah.
[Robert Mustacchi] [23:42] That's enough to trigger this slowdown sometimes. Yes. Oh, man. We had a we had a nasty you might not remember this. We had a nasty bug back at Joynt, where we had a guest in Windows, and we just weren't properly, clearing one part of the save state in the initial state.
[Bryan Cantrill] [24:01] Oh, man.
[Robert Mustacchi] [24:01] So the initial state basically was like, you know, like, the 256 bit, op masks or the 256 bit register state, YMM state is valid. It's like, okay. I'm gonna no longer boost.
[Bryan Cantrill] [24:12] Wow. And so you basically run this guest and it would, like, crater performance for the whole box for no actual purchasable gain because no one's actually using it.
[Robert Mustacchi] [24:20] Yeah. I mean, basically, just that one for it was just for it, but it was just that's I think that to me is kind of the even more telling budget. Even if you just leave the state in the save state
[Bryan Cantrill] [24:30] Yeah.
[Robert Mustacchi] [24:30] Then you're you're toast.
[Bryan Cantrill] [24:32] And it's really hard to have a feature like that, where if you use this feature, it has this this kind of this adverse effect on the rest of the
[Adam Leventhal] [24:41] monkey's paw kind of feature?
[George Cozma] [24:43] Yes. Yeah.
[Bryan Cantrill] [24:47] It it it reason about the performance when you have these kind of problems. So and the and and AMD is not needed and I I mean, you know, and it sounds like George, you got the kind of the same question of, like, I I you've just come so accustomed to these kind of intense compromises that come with AVX 5 12. It's kind of amazing that we can have it all.
[George Cozma] [25:10] Yeah. It's how do I put this? I so it I think what Zenf the it it and if you read the initial sort of coverage of Turin, Sorry. Not of Turin, of Granite Rapids. So that's Intel's newest Xeon chip.
[Bryan Cantrill] [25:38] Right.
[George Cozma] [25:40] They their all the coverage was like, yeah. It's good. It competes with Genoa. But we were all briefed before this. And we were just sort of thinking, yeah, but is this actually gonna compete with what's coming up next?
[George Cozma] [25:59] And it it's let let's put it this way. At least AMD isn't competing with itself anymore, if if you get what I mean. But it's it's not a good competition for Intel. Like, it's not a winning one for Intel. They can at least bid at something and not be laughed immediately out of the room.
[George Cozma] [26:24] But
[Bryan Cantrill] [26:26] Yeah. And and they and you would expect that to, like, I mean, flip a little bit with with Sierra Forest, but, then you end up with this this kind of this ecore business. And, I mean, I think it's just there's it's gonna be I mean, there's gonna be things that are gonna be interesting over there, but, touring is a very hard part to compete with. It's done a pretty good job across the board. Yeah.
[Bryan Cantrill] [26:53] And so I think you George, I don't actually go to all 3 of the things that you had that were so you had the the the the frequency, the the the high number just in terms of the of the the f cores and getting that up to to 5 gigahertz especially across all cores.
[George Cozma] [27:08] In the the fact that there's only 2 500 watt SKUs, I actually really like that.
[Bryan Cantrill] [27:15] Yeah.
[George Cozma] [27:15] The fact that while they are going up to that 500 watt SKU, they're only really leaving it for the highest end parts. Yeah. Whereas everything else is 400 or below. And I I really actually respect that.
[Bryan Cantrill] [27:30] I can tell you that we at Oxide also like that.
[Adam Leventhal] [27:33] Yes. Folks think about
[Bryan Cantrill] [27:36] the kind of the rack level because we you know, we're we're kinda left with the the the rack level power budget. And, yeah, we definitely it's nice to have a SKU stack that is not all sitting at 500 or 500 watts plus. Right? I mean, I think that that's Yeah.
[George Cozma] [27:51] Yeah. For it is 400 watts is still a lot lot large amount of power. No doubt. But if you remember the slide that AMT showed with a 7 to 1 consolidation
[Adam Leventhal] [28:03] Yeah.
[George Cozma] [28:05] That's if you can if you could do that, right, if you can go from a 1,000 racks of, 82 eighties to a 131 racks of
[Adam Leventhal] [28:19] Oxide? What?
[George Cozma] [28:23] But yeah. But if you could do that reduction
[Bryan Cantrill] [28:25] Yeah.
[George Cozma] [28:26] It's even though the single SKU power has gone up, your total power savings has gone has gone like, your total power of the data center has gone down.
[Bryan Cantrill] [28:37] It has. And I think you're you're the economically too, it's interesting. Even though these are expensive parts, but they can do they they can do so much, especially at that that high core count level when you're not having to sacrifice on what this course can go do, that you can make it make economic sense, I think. Yeah. It's a big, it's a big step function over where they've been.
[Bryan Cantrill] [29:00] I mean, I think that we you know, I think like a lot of people, like the Genoa SKU stack was, a little less interesting for us.
[George Cozma] [29:07] It was it was obviously a lot more focused towards the high end. Yeah. Like, it was it was very much skewed, pun intended, towards the hyperscalers, right, towards those people who can take that much power and just not care. But I think, especially with with the current SKU stack, I think it's a lot more sort of a refresh across the board
[Bryan Cantrill] [29:39] Yeah.
[George Cozma] [29:40] Which is which is really good.
[Bryan Cantrill] [29:45] Yeah. It it is I mean, it's a good segue, Robert, to the kinda our thinking on Turin because we so, George, we as we're kinda thinking about our I mean, our next gen sled is obviously a a a Turin based sled. We've, we did deliberately elect to, to kind of bypass Genoa and to intersect with with Turin. I'd maybe describe our thinking a little bit there, Robert, and we've got
[Robert Mustacchi] [30:09] Sure. Yeah. We we can go a different bunch of different places. I think the the starting place is really actually going back to Milan. Yeah.
[Robert Mustacchi] [30:16] Because, actually, like, 64 core, Milan, like, the 7713 p, or even if you go up a little bit, getting that in 225 watts or, you know, 2 40 watts, that was actually really
[Bryan Cantrill] [30:26] nice. Really nice.
[Robert Mustacchi] [30:27] Yeah. That was really nice.
[Bryan Cantrill] [30:29] You know, performance per watt on Milan is really pretty great.
[Robert Mustacchi] [30:33] Yeah. I mean, I definitely I mean, it when you get you know, it's hard to compare to the, you know, a 190 2 Zen 5 c cores Yeah. In in that range. But, you know, once you kinda get to Zen 5 I mean, I I still miss that there's no 225 watt 64 core Yeah. Core core part.
[Robert Mustacchi] [30:53] But I think, you know, this is where you're gonna see this this from our end, trying to think about how do we get a little more flexibility, leverage the fact that you have, base DRAM, has increased in capacity without going to 3 d stacked, RDIMMs. Yeah. Just because that part of the balance and price equation starts getting, really thorny. So the fact that you have a 128 gig RDIMMs, is useful, especially when you look start looking at the fact that 2DPC stops making gets challenging Yeah. Fast, there.
[Robert Mustacchi] [31:23] So I think there's a bunch of different SKUs you can kinda start to look at. You know? I think one thing I've been keeping my eye on is actually the 160 core, Zen 5 c, as one thing to look at. Because, like, that kinda keeps you below 400 watts. So I think it's still like a group e, CPU as opposed to a group g in the IRM.
[Bryan Cantrill] [31:45] So do you wanna describe a little bit
[Adam Leventhal] [31:46] of this term? So what what what what when
[Bryan Cantrill] [31:48] you say the the group g versus group e, what are those?
[Robert Mustacchi] [31:52] Yeah. When AMD creates a new socket, they they put out what they call an infrastructure roadmap or IRM, and then they basically are predefining different TDP ranges into these groups. So, for example, group e probably has some range. Also, I'm ahead from, like, 320 to 400 watts. These new 500 watt CPUs, I I sometimes joke are group g guzzlers, just because they they definitely take a lot.
[Robert Mustacchi] [32:19] Yeah. But you can design your platform to different TDP kinda thresholds, these kinda different infrastructure ranges, and then you'll get different kinda CPU and core counts. So, like, I think if we look at, there's like 3 or 4 different 64 core CPUs. I think there's like the 9535, which is kinda like the, you know, almost 300 watt, 64 core. It's like that'll be like a group a CPU.
[Robert Mustacchi] [32:45] Yeah. And that kinda gives you what the tells you kinda what the TDP range and what you, as the platform designer, can kinda tweak, from what the min to max is on there. Whereas, like, the others will come to group e or some of these even smaller ones, like some of the 32 and 16 cores, if they're not getting cranked up for frequency, might even be in like group b, or and related. And then
[Bryan Cantrill] [33:10] But as we're as we're thinking about Cosmo, Cosmo is our code name for our next gen Turin based sled, s p 5 based sled. What were we thinking in terms of what groups we wanted to target and kind of, like, the the trade offs there in terms of flexibility?
[Adam Leventhal] [33:23] Yeah. That's a good that's a
[Robert Mustacchi] [33:24] good point. So I think a lot of what we do, there's a bunch of work that we do with, actually, Eric who's also on here. We're trying to figure out, hey, like, what's the right balance of, how many stages, how many components do we need to kinda reach what, kind of what power group. So, like, for example, if we designed when we did s p 3, we designed what they called group x, which was the group they added later for the 3 d v cache and, like, max frequency skews. Yeah.
[Robert Mustacchi] [33:48] Which had maybe it's like a 2 40 or 2 80 watt max, but then we ran kind of a 2 25 watt CPU in there the entire time, giving us plenty of margin, plenty of headroom, which meant that, you know, our power subsystem was, very clean. So here we kind of are saying, hey, let's let's you know, we were said, hey, we're gonna start with group b as our target. We're We're gonna see what does it cost us to fit group g. You know, does it actually cost us more stages, more inductors, more more other parts? And, you know, then the first question of can we cool can you air cool 500 plus watts, which is a different question entirely.
[Bryan Cantrill] [34:22] Yeah. Eric, do you wanna describe some of the kind of the thinking there as as you're as we're looking at the what the PDN for this thing was gonna look like?
[Eric Aasen] [34:30] Yeah. So, generally, the the trade off is not even so much cost. It's space. So if you look at that, in the chat, there was a server that had 2 sockets and, like, 48 DIMMs or some insanity on it. And if you look at that thing, there's a whole lot of power stages in it.
[Eric Aasen] [34:46] And if you look at the board designs for those things, having that many power stages basically creates a giant wall for you to route around, which sucks. So you have to pull pull out all those lovely PCA lanes we love to use and, route them around all those power stages because they don't really like going through them. And
[Bryan Cantrill] [35:06] when you mean route, you're what you're talking, the physical layers
[Eric Aasen] [35:09] Traces on the PCB.
[Bryan Cantrill] [35:10] Traces on the PCB. Right.
[Eric Aasen] [35:12] Yeah. And so for our power design, we I I tend to bias towards the conservative side of things, one, because we're not building, you know, a million of these, and I don't have a finance person beating down my door over $5 in extra components, and 2, because it gives us flexibility. Right? So if we wanted to run those 500 watt chips, I'm going to be able to do that.
[Bryan Cantrill] [35:39] Yeah. Yeah. And I feel that, like also, Eric, I think whatever size oxide becomes, even we're selling millions of them, I I will help slay the person that comes to your door on the 5 because I feel like on on so many of these these parts I mean, yesterday, like, they add up and it's part of the bomb.
[Robert Mustacchi] [35:56] But, man,
[Bryan Cantrill] [35:57] the the look at the cost of these CPUs is so much greater and getting the flexibility is so much more important.
[Eric Aasen] [36:03] And having the reliability of having margin
[Bryan Cantrill] [36:06] Yes.
[Eric Aasen] [36:07] And not having to worry about it. It's like, okay. Oh, you know, I I can push it down to, like, 4 millivolts of margin to the spec. It's like, but but why? So I can save $5?
[Eric Aasen] [36:17] Like, that's dumb. You can do that.
[Bryan Cantrill] [36:21] And then so I
[Eric Aasen] [36:21] would love to get a bunch of commodity servers and just start throwing them through, power testing and see what they do.
[Bryan Cantrill] [36:27] Oh, well, I don't know if you
[Eric Aasen] [36:28] is how close they are.
[Bryan Cantrill] [36:29] Oh, and I think I mean, George, I'm I'm sure. I don't know what your experience has been up there, but I definitely like, I I do have a bunch of the reviews online of Turin cautioning people to not do exactly this. Like, yeah. By the way, your, your s p 5 motherboard may not be able to take some of these cues.
[George Cozma] [36:48] Yeah. Basically, what what AMD has said is the there's these 500 watt SKUs. But if if you are a, like, an end user, like, if you bought like, if you're a small medium business and you bought, say, 4 turret servers from Dell or whoever, don't just swap out the chips. Please make sure that that you actually let your boards can actually support these chips.
[Bryan Cantrill] [37:16] Yeah. And the and having, like and because the problem too will be that if you push these things to the margin, I mean, you you can get, like, misbehavior. It's not it won't be as simple as, like, burning the house down. The And you can get
[George Cozma] [37:31] some very weird weird bizarre behavior that you're just going, why is it doing this?
[Bryan Cantrill] [37:39] And it's And you'll
[George Cozma] [37:40] tear your hair out for a week trying to figure it out, and it's just because of the power.
[Bryan Cantrill] [37:47] Yes. Or if you if you recall us on our, the tales in the bring up lab, episode where Eric was regaling us with some of our adventures on Gimlet where our power was already pretty good, but we could not figure out why this chip kept going but would would reset itself after 1.25 seconds. So we made our power even better. And, Eric, my recollection, this was AMD's like, I we have, like, never seen power like, this power's amazing. Like, you've got amazing margin.
[Bryan Cantrill] [38:15] It can't be that. Sure enough. It was not that. It was firmware, of course.
[Eric Aasen] [38:20] Oh, yeah. It was it was firmware on a power stage.
[Bryan Cantrill] [38:23] Oh, on a power stage. Power. Yes.
[Adam Leventhal] [38:24] Yeah. Yeah. Yeah.
[Eric Aasen] [38:26] It was the the the control interface that the AMD processor uses to tell the power stages what voltage it wants, turned out to need a firmware update. It actually face slapping.
[Bryan Cantrill] [38:39] George, this is kinda hilarious because we were not the SVI 2 was the protocol this thing uses that the the part uses to talk to to the the regulator. And the SDLE, which we had used, it's great part from AMD that we had used to actually model all this stuff. As it turns out, didn't have a hard dependency on getting the back from the controller when we set the voltage to a specific. The part is it turns out wants to hear that as we learned. Yes.
[Bryan Cantrill] [39:05] We learned that the hard way. We learned that the hardest, most time consuming, most expensive possible way.
[George Cozma] [39:12] Yeah. I But
[Bryan Cantrill] [39:12] we did learn in the process. I actually I thought it was super interesting to learn that our power margins were really good on that, because that was, like, our our a a first natural line of attack was our power margins aren't, like, that's why this thing is resetting because it's it it is or in a reset loop because our power is not good enough. But we actually learned in the process of doing that. Like, no. No.
[Bryan Cantrill] [39:33] This power is actually quite good.
[Eric Aasen] [39:35] Yeah. It's it was it was rock solid, and it was just stupid margin.
[Bryan Cantrill] [39:39] So, Eric, because you're just kinda thinking about, like, okay. So we need to, you you know, there are things we need to do. And is your are you were you coming to the conclusion that, okay. I think we can make this all fit? I mean, as you're doing that kind of that that trade off?
[Eric Aasen] [39:52] Yeah. And so the the the big trade off is, okay. Are we gonna have customers that need it? Are we going to even want to run a 500 watt? Can we air cool 500 watts because we're not water cooling?
[Eric Aasen] [40:07] And it to to me as the power person, it basically came down to it doesn't hurt anything for me to put another power stage on this thing. Yeah. And I can always turn it off, and then it's just not doing anything. But it's also not contributing any heat to the system. So if I wanted to, I could turn it off, and I wouldn't pay that much of a penalty.
[Bryan Cantrill] [40:28] And importantly, we're able to use the same regulator that we're it's not like we're having to swap regulators to accommodate this. We were able to use the the the same renaissance, parts for this. And and then the and then from a thermal perspective, so we then okay. So that that's kind of like, alright, that we we've got the insurance there. And then, from a thermal perspective, we also needed to do the because he said we're not water cooling this thing.
[Bryan Cantrill] [40:51] So, you know, can we and at 500 watts, I think we definitely know we will not be talking about how quiet the fans are because No.
[Robert Mustacchi] [40:59] You will not. You'll be lucky if you can hear us talk over the fans.
[Bryan Cantrill] [41:04] Yeah. And we know the fans will be cranking, but I think that the I mean, we've done the and Doug and and crew have done the model
[Eric Aasen] [41:10] of that. I'm calling it weak and air cool it.
[Robert Mustacchi] [41:12] Yeah. Yep. No. The that's the the one thing.
[Eric Aasen] [41:15] Not max off hands.
[Robert Mustacchi] [41:16] Yeah. I mean, right now, we've done all of our our worst case studies, which is basically saying, assume the CPU is going 500 watts. Right. All the dims are going at their maximum. You've got every SSD going at its maximum and the NIC.
[Robert Mustacchi] [41:29] Right. And, you know, some amount of loss you're paying some amount of loss for all the stages. We we still think we can cool that. And then practically speaking, even though the CPUs with turbo boosting have a good way to eat up the rest of your power Yeah. You're usually not getting all of those devices maxed out all at the same time.
[Bryan Cantrill] [41:46] It is in particular. Like, it's real hard to max out the the DIMM, the draw on your DIMM and the draw on your CPU at the same time without being mean spirited. I mean, you have to be really,
[Eric Aasen] [41:56] Maybe maybe x 512 will let us do it this time.
[Robert Mustacchi] [41:59] Yeah. They've also gotten
[Adam Leventhal] [42:00] a lot more clever about
[Robert Mustacchi] [42:01] how they do all the hashing across It's true. Yeah. Across DIMs Yes. Yeah. Substantially.
[Eric Aasen] [42:05] So
[Bryan Cantrill] [42:05] Right. Okay. Yeah. I should you're right. I should not be tempting the gods here with, some
[Eric Aasen] [42:10] One thing that I'll that surprised me coming into this, like, outside of the industry and coming into this is seeing, like, okay. You got your 500 watt TDP, but that's not actually the peak power you can draw. They can draw over 800 watts transient as they're scaling things up and down. And I'm just it just blew my mind. It's like, wait.
[Eric Aasen] [42:29] This 500 watt part can just spike up over 800 watts and then scale itself back down? Like, the like, yeah, that that's great thermally, but damn it. I gotta I gotta provide that. Right.
[Robert Mustacchi] [42:42] Right. Yeah.
[George Cozma] [42:44] And and with the voltages that current server CPUs are running, you're having at at those 800 watts spikes, it's not 800 amps. It's a 1,000 plus amps. And which means more power stages
[Eric Aasen] [43:00] And just turning your board into a giant resistor, essentially.
[George Cozma] [43:04] Yes.
[Robert Mustacchi] [43:06] But
[Eric Aasen] [43:06] It turns out copper is not like a 1,000 amps running through it.
[George Cozma] [43:10] Yeah.
[Eric Aasen] [43:11] Normal PCB thicknesses.
[George Cozma] [43:13] So actually sort of the thing. Sort of related but unrelated to turn directly at the event that was announced was Pensando new piss stuff.
[Eric Aasen] [43:26] Yes.
[George Cozma] [43:28] And I sort of want your take on this.
[Bryan Cantrill] [43:32] Interesting is our take. I mean, it's like definitely interesting. I mean, I think that we, we would love to be able to get some parts. The the the draw does become an issue back there for us.
[Robert Mustacchi] [43:45] Yeah. I mean, the p 4 programmable nature for us is saying that's actually really powerful. We leverage that in our switching silicon a lot and have been looking for something to get that into the NIC. The big challenge is just I think where we're a little different is a lot of the DPUs have been designed to basically be like, we're the compute the DPUs, the computer in charge, and, hey, you big big CPU that's, like, running guests over there, like, you're subordinate to me. So, like Yeah.
[Robert Mustacchi] [44:12] You don't you don't you know, you exist, but, like, only at my pleasure. And we were not quite as, split brain, there slash we're not trying to sell the entire server. So, like, you know, it just gets thorny when it's like, okay. That that device also needs its own DDR 5. Yes.
[Robert Mustacchi] [44:29] Some questions around,
[Eric Aasen] [44:30] like, how am I doing? Like, oh, but think of how much it could offload your processor. It's like, yeah. But the processor is still gonna get maxed out. So now I've just increased my overall power.
[Bryan Cantrill] [44:38] Totally. Yeah. So when we
[Robert Mustacchi] [44:40] end up designing for kind of not absolute density, but trying to get the best density in a fixed power budget, which because, you know, unlike the hyperscalers, we're not basically building a power plant next to every new DC. That that's where it gets a little more challenging. So we're trying to work with folks to figure out, you know, hey, if I don't need, say, all of the arm cores that show up there, or let's say I didn't run with DDR 5, you know, where can I what can I get? What can I kinda still get out of there? You know, how can we kinda change this from, you know, some of these parts are and I don't remember what this one was, you know, or 50, 75 watts.
[Robert Mustacchi] [45:14] And, you know, that's that. Or, you know, maybe I I play games and I say, you know, I've got a lot of SSDs, but maybe I don't need all of the IOPS or all those SSDs, so I can double up, you know, capacity instead. And that gets me back some of the power and I can send that to the NIC. But it's it's definitely, we're not in a you know, even with just increasing power for the CPU, I'm already trying to think about, like, well, what do I do for folks who don't have all that power? If I've got 32 sleds, how do I,
[Bryan Cantrill] [45:42] Well, and I think that, you know, and and, Ellie, in the chat is segue. I don't think people realize how, you know, how restrictive the oxide power budget is. And it I don't necessarily it is is restrictive. It's more that we are really we are taking that rack scale approach. And so we're kind of the ones that are, like, always adding up the Visa bill.
[Bryan Cantrill] [46:01] And, and, you know, the, when you have, you know, 30, 40, 50, 60 watts, 70 watts, 80 watts in your neck, like, that adds up in a hurry. And, yes, you can you can offset it elsewhere, but, we're what we're trying to do is try to get you the maximum amount of useful work out of that rack scale power budget. And, you know, by being the ones that are doing that, we're we're the ones that are, you know, sometimes having to deliver some tough messages to folks about, like, we like this. This is interesting, but it's drawing way, way, way too much power. But yeah.
[Robert Mustacchi] [46:40] So overall, really good. Really nice to see. Excited to see that kind of p 4 continue there. And, you know, hoping someday we can find a way to make it make sense for us. But I think there's a lot of other folks who it does make a lot of sense for.
[Bryan Cantrill] [46:51] Yeah. I mean, we love we're huge p 4 fans, as as folks know. And I think we've got, actually, that's if folks can see it out there, we've got an exciting announcement, in terms of, Excite Labs and using their part as our next gen switch, which and it's p 4 programmability. So we're we're really excited. We're we're we've been using p 4 on the switch.
[Bryan Cantrill] [47:16] We're gonna continue to do that. And using p 4 or programmability at the at the NIC, we're really interested in. But, it's gotta it's gotta happen in a way that we can accommodate everything else we need to go do with the rack. So, George, a long answer to your question there, but it's interesting, but for sure.
[George Cozma] [47:33] So so speaking of how you guys don't wanna do DPs, because AMD didn't just announce DP, which is, Pensando Selena 400. They also announced Polaris, which I think is just a standard Nick. Like, it's p 4, but it's not a DPU.
[Bryan Cantrill] [47:51] Yeah. Which is something that's gonna be and and that is something that's gonna be, like, we're definitely interested in.
[George Cozma] [47:58] Okay. Yeah. Because I was gonna say, is is that the one that you're more interested in?
[Bryan Cantrill] [48:02] Yeah. I think so. I mean, you know, that's not gonna intersect our our first cut here of Cosmos. So Oh, no. The the but no.
[Bryan Cantrill] [48:09] That is we're really, really interested in it. And and, again, great to see that p 4 programmability. We are you know, there were some moments where it felt like it felt like we were a bit of a lonely voice, but I think, other folks are beginning to realize, and I think as as the hyperscalers themselves have known, that having that network programmability is really essential.
[Adam Leventhal] [48:32] Hey. Brian, we've talked about p 4 in the past, but do for folks who maybe haven't listened to the back catalog, should should we give a little overview? Sure. Yeah. I mean, Rara, you'll do the honors.
[Adam Leventhal] [48:42] I'm happy to give my my my p four spiel, but I'll,
[Robert Mustacchi] [48:45] Sure. I'll I'll see if I can do it justice. Effectively, the way I think about p four is it basically is a programming language that you can use to compile a program that operates on the next data plane. And I think this this is an important part because for a lot of these things, the value is, to actually run at line rate. So you got a 100 gig, 200 gig, 400 gig, especially with all these a 112 gig SerDes coming along, you basically can't necessarily treat that as a general purpose program that's coming in, DMA ing everything back to normal, you know, to a normal course memory and processing it and sending it back out.
[Robert Mustacchi] [49:23] But instead, this kinda lets it, process the packets kinda in line in that hardware receive path.
[Bryan Cantrill] [49:30] And having that higher level of abstraction, really, allows us to it allows you to to kind of express something programmatically that they can then use hardware resources efficiently. The our big challenge has been, working with vendors to give us a substrate upon which we can build a true p 4 compiler. Honestly, the the the biggest challenge in that part of the ecosystem has been the proprietariness of the compilers. So, George, I'll tell you that one thing that will be a factor for us is we're looking at at a kind of a p 4 based NIC is we have been looking for is what is that kind of x86 like substrate gonna be? Something that is a documented committed ISA that we can write our p 4 compiler against.
[Bryan Cantrill] [50:16] So what we are not looking for, because we are coming out of a bad relationship in this regard, it what we are not looking for is kind of a proprietary compiler. We really, want to and we have written our own p 4 compiler for we use our we developed our own p 4 compiler and have open sourced it, x four c, for purposes of just doing development, software development and testing and so on. But we really wanna take that and have that use that to actually, to compile for these parts for both the the switch for sure, and then ultimately, the neck, would definitely be our vision for where it's going.
[George Cozma] [50:56] Yeah. And I know you guys as were a lot of us disappointed with, Intel discontinuing the Tofino line of switches.
[Adam Leventhal] [51:11] George, I really appreciate your sensitivity
[Bryan Cantrill] [51:13] of taking us into the kind of the grieving room. And, your your your bed your bedside manner here is really exemplary.
[Adam Leventhal] [51:19] And Yes. Yeah.
[George Cozma] [51:20] I I
[Bryan Cantrill] [51:21] I I I was really feeling you kind of passing the tissues to us as you
[Adam Leventhal] [51:25] as you really felt our loss. I really appreciate that.
[Bryan Cantrill] [51:28] Yes.
[George Cozma] [51:29] But yeah. And one question I one question I have with, AMD is, does it make sense for them to make their own switch eventually?
[Eric Aasen] [51:45] In I I mean, are we
[Adam Leventhal] [51:47] gonna meet you on our answer? Are we
[Bryan Cantrill] [51:48] in charge of Amdino? Because we got, like, lots of ideas. Yeah. Robert.
[Eric Aasen] [51:51] You know
[Robert Mustacchi] [51:51] what I mean? This is I mean, actually, George, this is the pitch I've tried to make to them, just because it to me, it's like, if you actually look at Nvidia and what they've done with NVLink and basically buying Mellanox Yeah. At the end of the day to really be able to, you know, deal with that, what they're doing with Ultra Ethernet, it feels like you have a p four engine. Yes. It's gonna be a big change.
[Robert Mustacchi] [52:14] Take it from, you know, the NIC kind of 2 cert you know, 2 port form factor, to, you know, a switch ASIC in kind of dealing with power. But I think that if you really wanna, do well in that space, you can't rely on just like, hey, I'm gonna convince Broadcom to let me pass through, you know, x g m I, you know, through my switch. And I you know, or whatever they're calling the that trans that Infinity Fabric transport these days. But yeah.
[George Cozma] [52:42] It's now it's now UALink.
[Robert Mustacchi] [52:44] Yeah. Exactly.
[George Cozma] [52:45] Which ironically enough, Intel is now a part of.
[Robert Mustacchi] [52:49] Right. So yeah. So but but so, yeah, I think it's, like, it's good that you have that consortium, and you'll be able to push some stuff there. But I also feel like at the end of the day, you know, where you see a lot of value from Nvidia is that they are building, you know, where they've been successful is because they have vertically integrated a whole lot of that stuff.
[Bryan Cantrill] [53:05] Yes. Yeah. And, you know, so yeah. I mean, I absolutely. We it would be great for them to do that.
[Bryan Cantrill] [53:12] Although that said, we we are you know, they need to do it in the right way, and the right way from our perspective is really establishing a substrate that people can build an open ecosystem on top of. And this is something that, you know, always I find vexing is you would think if you make hardware, it's enormously in your best interest to allow many many software stacks to bloom, by having a well documented committed interface, but, they really don't. It's a challenge, I would say. I I wouldn't say they they don't. It's too reductive.
[Bryan Cantrill] [53:49] I think that they are they fight their own instincts on it. And, so we're we're very excited with the excite labs. Again, you can see our announcement today or their announcement today, actually. But but if it it features, oxide for sure, and we definitely see eye to eye with them on their x two. We're looking forward to to moving forward with that with that part.
[Bryan Cantrill] [54:11] And I and and we think that there should be we we wanna see programmable networking everywhere. We wanna see this open ecosystem everywhere. The, on the note of, like, the kind of the lowest levels of the platform that can be hard to get at. So, George, you may recall that we have no bias in our system. So, with there is no Giza.
[Bryan Cantrill] [54:33] There is no AMI bias. So, when we, buy us buy us, am I
[Adam Leventhal] [54:42] Nailed it.
[Bryan Cantrill] [54:43] Oh, thank you.
[Eric Aasen] [54:44] We have
[Adam Leventhal] [54:44] we have lots of bias.
[Bryan Cantrill] [54:45] Up and at them. Up and at them. Better. Do you wake up your kids that way, Adam? No.
[Bryan Cantrill] [54:54] As as Rene Wolfcastle Rainier Wolfcastle is saying up an at them.
[Adam Leventhal] [54:59] I'm not as good a parent as you in that regard.
[Bryan Cantrill] [55:04] It was very loaded. I bet my kids have definitely gotten sick of that particular Simpsons reference. Rainier Wolfcastle, no longer welcome in our abode. But in the we have no bias, and so, Robert, that lowest level platform enablement has fallen to us. What are some of the differences in Turin, from or even from Genoa, but then from Milan?
[Robert Mustacchi] [55:25] Yeah. I think, actually, we've been talking about PCIe a a bit. So I actually think one of the things that I find has been both fun and sometimes little vexing, but it's ultimately good for the platform, not always, as fun for us, in how the register numbers sort themselves out, is that they've actually increased the number of IOMS, entries in there. So, basically, in the past where you had, a group of 32, PCIe lanes, which are basically 2 x 16 cores, they were consolidated into one connection to the data fabric. Actually, one of the more interesting things is that we've seen that in turn, each x16 group is connected to the data fabric independently through Interesting.
[Robert Mustacchi] [56:04] Yeah. Kinda IOMS slash IOHC, which are all, I guess, internal Yeah. Those are all datums.
[Bryan Cantrill] [56:11] Yeah. Those are effectively hidden cores. Right? Are they those are the core ish?
[Eric Aasen] [56:16] I mean
[Robert Mustacchi] [56:17] yeah. I don't know how much I'm sure there's a z 80 hidden and everything. So I mean Right. Or an 8051. So I'm sure there's a everything's a core at the end of the day.
[Robert Mustacchi] [56:24] But, but, yeah, actually, if you just kinda look at it, this this part's a little is less hidden. Yeah. Because if you just look at, hey, show me the PCI devices on Turin, you'll see, hey, there's 4 there's 8 AMD root complexes where there used to be 4.
[Bryan Cantrill] [56:39] There used to be 4. Yeah. Interesting. And that is presumably so you are you're just increasing the parallelism there, and I mean, is is that the
[Robert Mustacchi] [56:48] That that yeah. That would be my theory is that basically it's getting you more, because there's more data fabric ports Yeah. That you can have just more transactions in flight to different Right. To different groups of devices.
[Bryan Cantrill] [57:01] And so but but those kind of changes, which if we were at some level of software, that's an implementation detail you don't need to see. But at the level of software we're at, like, you actually need to go go accommodate those differences. Yeah. Yeah. That that's definitely it.
[Bryan Cantrill] [57:18] Otherwise it's Milan to Genoa was more, there are
[Robert Mustacchi] [57:22] more changes than Genoa to, turn
[Bryan Cantrill] [57:25] in kind
[Robert Mustacchi] [57:26] of some of the lower level stuff. Some of these kind of bits, like how do you do PCI initialization, hot plug have stayed more the same,
[Bryan Cantrill] [57:36] from Genoa, from
[Robert Mustacchi] [57:37] kind of Genoa to turn. Yeah. They have some different, firmware blobs that you talk to. So like, you know, the smooth interface has stayed the same across these, but like they, they moved to a new, what they call MPIO, framework, which is what goes in programs, the DXIO crossbar. And does you kind of, PCIe device training is kind of a collaborative effort, between that core and, 686 cores.
[Bryan Cantrill] [58:06] And could you describe what device training is? Like, why does a link need to be trained? What is that? Yeah.
[Robert Mustacchi] [58:10] So there's there's 2 different pieces here. So if you see AMD, first off, when they sell, you know, in their other markets, say, hey. We've got a 128 PCIe lanes, which is great. But the first thing you have to figure out is, well, actually, how do those work on the board? You know, I've got are these x16 slots?
[Robert Mustacchi] [58:26] Are they x 4 slots that are actually connected to an SSD? You know, what's their size and width, and how do they actually fit across the board? So the first one of the first things that everyone has to do is they kind of will tell the the AMD's firmware, hey, here's how this is actually connected. You know, these logical these physical PHYs, you know, I've got an x 16 slot. I've got, you know, in our case, we've got 10, x 4 slots for basically every front facing u dot 2.
[Robert Mustacchi] [58:57] Right. You know, an x 16 slot for a Nick. You'll have other things for other folks. Or if you have a kind of like a a board, like, showed up in the chat, you know, you've got some number of x 16 slots that map to things, some some probably m dot 2 slot. So you have to tell it what is all, you know, what all is there.
[Robert Mustacchi] [59:13] So it can basically go and reprogram, the internal crossbar to say, okay. These lanes should be, PCIe. You know, George mentioned earlier that when you have a 2 processor configuration, you know, some of those lanes are being used for that. Right. So it yep.
[Robert Mustacchi] [59:29] That's part of it. If you use SATA, which I you know, getting less and less common. Yeah. That's right. You know, some of those lanes are come from those same PCIe lanes.
[Robert Mustacchi] [59:43] So, that's the first step is you're kind of doing that. Then the next phase is after you've done that is, if you open up the PCI, base specification and, like, chapter 2 is a very long state machine. It has a lot of different states and a lot of different phases. But, basically, what does it mean to basically have a PCIe device end up at the other end and have both sides be able to talk? And so device training is basically going through that process, discovering, is there even a device there?
[Robert Mustacchi] [01:00:14] Right. And from there, trying to say, okay. Let's start talking to one another, figure out how we can talk, then what speed we can talk at. Once we're good at, you know, a certain speed, then they'll increase to additional speeds, sending these things called ordered sets and training sets and lots of different, acronyms that you hope generally just work and you don't need to think about. And then, unfortunately, sometimes you do need to think about them.
[Bryan Cantrill] [01:00:39] Right. When they when they misbehave.
[Adam Leventhal] [01:00:40] But so there's a lot of so there's
[Bryan Cantrill] [01:00:42] a lot of of low level work that we need to go do, as and how do we in terms of, like, we don't yet have I mean, we're the Eric and Daniel and crew are are working on Cosmo as we speak, kind of finishing up Cosmo. How do we work on that before we have our own board in hand?
[Robert Mustacchi] [01:00:59] Yeah. So the main way we do this is that, there are often reference platforms. So, you know, if you look at George's article, all of his testing was done on a volcano platform, which is the name of a platform that AMD developed, for that is specific for Turin. There's a couple older generations
[Bryan Cantrill] [01:01:16] Is it too much to hope that someone has a sense of humor that named that thing volcano?
[George Cozma] [01:01:22] Honestly, I would not surprise me if somebody did have a sense of humor.
[Adam Leventhal] [01:01:26] I mean, you had
[Robert Mustacchi] [01:01:27] volcano, you had, Purico. I'm trying to remember what the other 2 were. The ones before that were all metals. You had, like,
[Bryan Cantrill] [01:01:34] Yeah. So Onyx. Yeah. No no sense of humor. I I just love the idea that, like, Inferno, you you're going with the, so yeah.
[Bryan Cantrill] [01:01:42] So we got the volcano reference platform from from AMD.
[Robert Mustacchi] [01:01:44] Yeah. So we are doing ours mostly on a bunch of, Ruby platforms, which were the ones that first came out for, Zen 4. And so we have those, which gives us generally most of the schematics and other bits there. You generally get most of the firmware, but not all of it. So you can't always do all the things on the board that you think you should, like a reference platform will let you do.
[Robert Mustacchi] [01:02:09] Right. But that lets us that gives us a development platform. So, you know, we're fortunate that we were able to get some early silicon from AMD, so we could actually start doing development of that ahead of launch. Right.
[Bryan Cantrill] [01:02:20] And then, Nathaniel, do you wanna talk about kinda how we how we use those dev platforms? Because we've got a little a great little board there.
[Nathaneal Huffman] [01:02:29] Yeah. So, notably, we, were able to take the b m so in Ruby, AMD made this BMC board called the Hawaii board that has an a speed BMC and kinda all your your traditional BMC stuff, but it's on an OCP card. So we can pull that out, and so we developed our own OCP, form factor card. And we, we call that the grapefruit, and that goes into that BMC slot and connects to the OCP connector. But it has RSP and ROT and, a Xilinx FPGA there and some Flash and, you know, kind of basic.
[Nathaneal Huffman] [01:03:06] So I I three c level translators, that kind of thing. So we can kinda hotwire into the the Ruby dev platform with our you know, what is effectively our BMC topology and do some development there. And so that's, that's kinda I've been working on, Grapefruit a lot the last few months, I guess, and doing some of the FPGA work and trying to get the thing integrated so that, Hubris runs on it, and we've got, you know, our Ethernet stack runs on it and all of that. And that's all going pretty smoothly, and we're getting close to, being able to use our Grapefruit board as an eSpy boot target. So I don't know that we have talked a lot about
[Bryan Cantrill] [01:03:46] eSpy boot. Yeah. We should talk about eSpy because this is a this is definitely a difference in Turin.
[Nathaneal Huffman] [01:03:51] Yeah. So Turin supports, you you can do the standard, like, Spynor boot, like, you know, all of the, you know, all of these devices have done for a while, but they added eSpy boot, which is it's based off an Intel standard. And and so it it's an extension to eSpy, which is kinda like an LPC replacement. But it's an extension to that that allows, you to have what what they call slave attached storage and or slave attached file storage or some flash storage, something like that. And, that allows you to boot off of, over the spy network, and it's basically built exactly for the server use case.
[Nathaneal Huffman] [01:04:29] So, you know, you have a BMC or some kind of device sitting there, and then the flash is hiding behind that. And so you talk spy to that device, and then it goes off and fetches the flash and does whatever it needs to do, you know, out of Spynor or NAND or I guess you could, you know, do it off of NVMe or something if you'd like. And you just feed it, the bytes that it requested back over the eSpy interface. And so
[Bryan Cantrill] [01:04:51] And YT that's how we're planning.
[Adam Leventhal] [01:04:53] So so What's that?
[Bryan Cantrill] [01:04:54] Why is why why did we need to enhance spy to do that? Why can't we just use spy?
[Nathaneal Huffman] [01:05:00] Well, I mean, so you can talk spy to a Norflash, but that's that's basically all you can do. And the eSpy protocol kinda sits on top of what looks like a fairly standard spy, like quad spy interface. But it allows you to go request transactions, and then, you just wait until the device goes and gets them. So, you know, Flash is notoriously slow. Right.
[Nathaneal Huffman] [01:05:21] And so if you are the only device talking to a, like a quad spy, and you ask it for something or you ask it to go do an erase or whatever, you basically just kinda have to hang out and spin your tires until it finishes and wants to give you that data back. And the with over the eSpy interface, they do posted and non posted transactions. So you can do these non posted transactions and say, hey. I want, you know, a a kilobyte of flash from this address. And you send that message, and then you can continue on using eSpy talking to the device doing other things while the whatever the eSpy target is goes off and does the work to get you your kilobyte of Flash.
[Nathaneal Huffman] [01:06:00] And then it'll let you know with an alert that it has data for you, and you can come by and fetch it when you want.
[Bryan Cantrill] [01:06:06] That's right. And spy, as my kids would say, spy has no chill. Spy is, spy, you need to give it what it needs in like, you're set on the clock. Yep. There's no clock stretching in spy.
[Bryan Cantrill] [01:06:21] So, you can't and so spy in a position becomes a real nightmare, because you need to get everything you need to get done. You need to get done in that one clock cycle. It's like, yeah, not that's Right.
[Nathaneal Huffman] [01:06:34] And and, like, on Gimlet, what we did is we put, actual, like, analog spymuxes in so we could flip between our, like, a boot and b boot flash images. So we'd actually just swap between chips that way. With eSpy, we can actually use, you know, none of these images are very large. So you end up buying, you know, a commodity flash part with, like, say, a gigabit of flash storage, and you only need 32 megabytes or something like that. You know, you need these small, like, PSP images there.
[Nathaneal Huffman] [01:07:03] So with eSpy, we can also go down to 1 flash part. And then the the FPGA that's acting like the eSpy target will just translate, you know, into the high or low pages basically of the flash. And, but the AMD doesn't really have to know the difference. So that makes things a little simpler on our end.
[Robert Mustacchi] [01:07:20] Yeah. And the other nice bit there is that as you get into DDR 5, one of the big problems is training time. Yes. So Yeah. One of the things that, AMD has is that you actually after you train the first time, you actually end up writing back a bunch of this data into that spy flash.
[Robert Mustacchi] [01:07:38] Yeah. And if you have it virtual if, you know, without that virtualization, then if you're trying to kinda hash or figure out, like, you know, how do I make sure this contents are all what I thought I wrote down and that it just gets gnarlier. And this kinda just indirection layer, you know, computer sciences, you know, it's one contribution is adding another layer of indirection just to cheat, just comes in handy.
[Bryan Cantrill] [01:08:02] Yeah. And the and just on the training times, without that, without kind of and so dim training where you're you're trying to defy find the search for the constants that are going to allow you to to to, not have interference when you're talking to these dims. That search can take a long time. And, Robert, how long does it take you when you put the first that that first genoa that you've got?
[Robert Mustacchi] [01:08:30] The yeah. The first thing I had, which admittedly was
[Bryan Cantrill] [01:08:34] Early. So I did Early.
[Robert Mustacchi] [01:08:35] Early. A zero a zero silicon.
[Bryan Cantrill] [01:08:37] And then I'm not this is no shade on AMD. This is not this is but I think
[Robert Mustacchi] [01:08:40] it was one dim one dim of DDR 5. Not that big. It's definitely it felt like minutes.
[Bryan Cantrill] [01:08:49] It was 11 minutes, I believe, was the number. Was it really? Yeah. It was it was I've put it out of my brain. Yeah.
[Bryan Cantrill] [01:08:56] George, I don't know if if you've seen some long boot times, but d d r five takes a long time to train.
[George Cozma] [01:09:02] So I I know when I was first booting my 9950 x system, I put in the DIMMs, I turned it on, I went, grabbed a cup of coffee, came back, noticed it was still booting, was like, okay, let me go feed my cats. Fed my cats, came back, was still booting. It's like, okay, let me go run to the bathroom, Cut back. Still booting. I'm like, is it actually booting?
[George Cozma] [01:09:27] Like, what's taking it? And I was about to turn it off when I saw it in the corner of my eye that my monitor flashed up. I'm like, okay. It finally booted.
[Bryan Cantrill] [01:09:37] It's alive.
[George Cozma] [01:09:38] Yeah. I'm like, okay. Thank thank god it's actually done. And I did screw something up. Because I had to update the BIOS, which is always a bit of a nerve racking experience.
[George Cozma] [01:09:52] Yes.
[Robert Mustacchi] [01:09:53] When you
[George Cozma] [01:09:53] when you have to do it over just watching a flashing light go, you're like, is it done? Are you done? Did you work? I hope it worked. And then you turn it on and you're just like, okay.
[George Cozma] [01:10:05] Hopefully, this works.
[Bryan Cantrill] [01:10:07] Oh, Adam apparently really prefers your pronunciation, George, to mine Yeah. To, Myos.
[Adam Leventhal] [01:10:12] That was delightful.
[Bryan Cantrill] [01:10:13] I'll I'll
[Adam Leventhal] [01:10:14] With suffering through bias. Right?
[Bryan Cantrill] [01:10:16] I'd alright. I'll have, like, do my Duolingo with George on there. The,
[Nathaneal Huffman] [01:10:22] I I will say one of the other interesting or one of the other major reasons for using eSpy was that it gains us back our second UART channel, which we lost in Turin, because we like hardware handshaking, and the second UART in Turin doesn't have hardware handshaking. And so we you know, we're gonna plan to do our IPCC protocol between the SP and the, and the SP 5 or the the Turin processor over eSpy as well. So that'll be a multiplex path, and that was something that we had to solve regardless of east eSpy boot.
[Robert Mustacchi] [01:10:56] As a former colleague of mine, who retired was fond of saying, why do we have pins for Azalea on s p 5? And they couldn't give me 2 pins to have a second flow controlled u r.
[Bryan Cantrill] [01:11:07] It it was yeah. We definitely and I'm not sure, you know, maybe we're I I I guess we're a bit unusual on this, but boy, we were We're unusual. We need the yeah. That so, George, we were using as just as Nathaniel mentioned, we were using one of the u rts as the the IPCC, which is our, the inter processor, right, communication channels. The the the this is the, but this is our protocol for the, the socket, the host OS to be able to speak to the SP, which are the the our replacement for the BMC.
[George Cozma] [01:11:42] Okay. And
[Robert Mustacchi] [01:11:43] we were specifically looking for something that that we could use that didn't require PCIe training or very much, from the peripheral space that kind of keeps us stuck in the FCH. Even USB obviously requires a lot of smooth bring up and shenanigans, so that was out of the picture. So we ended up with the UART and, actually the AMD UARTs can go up to 3 megabaud, which is more than you do.
[Bryan Cantrill] [01:12:07] Well okay. Well so okay. So they actually, they they can't go up to 3 megabaud by default. They didn't.
[Robert Mustacchi] [01:12:14] We we actually we needed a a, and Well, the RS 232 level translator to go from, like, the 3.3 volt to I don't know. Minus 12 plus 12, that could not do 3 megabaud.
[Bryan Cantrill] [01:12:31] But we the 3 megabaud ended up being very load bearing for us because Oh, 22. Yeah. Because during well, because the, Yes.
[Robert Mustacchi] [01:12:40] When we wanted the when we wanted the PS when we were doing dim training Yeah. And and are doing dim margining, and we were the PSP is spewing output, it was just happily going at 115200. Yes. And there was no token to change it to anything. Yeah.
[Robert Mustacchi] [01:12:53] That's For real, it's not to get a 3 megabod. So it was very it's
[Bryan Cantrill] [01:12:56] very slow. It was very slow, and, our friends at AMD, fortunately, got us a a a fix to the PSP to operate at 3 megabod. And that was very it was life changing for, for I mean, I know for 30:30 x
[Robert Mustacchi] [01:13:12] makes a big difference.
[Bryan Cantrill] [01:13:12] For r f k. Thirty x means when when it's 30 minutes, that 30 x is like a real actionable human 30 x. Not all 30 x's are the same. And when something takes 30 minutes, taking 30 x off of that is, is a big deal.
[George Cozma] [01:13:26] So So The good
[Nathaneal Huffman] [01:13:27] good news is with with the eSpy, I think we can get significantly faster than 3 mag too. So it'll be interesting to see what that looks like in practice. ESpy is a little weird. It's like it's it's simplex, so you can only transmit one direction, you know, at any one time. But you can get you can do a quad at 66 megahertz, so we should be able to get, something a little bit faster than 3 meg, I think.
[Bryan Cantrill] [01:13:51] And that is yeah. Sorry, George. Go ahead.
[George Cozma] [01:13:54] It's really funny that you you guys are talking about, like, 3 megabond and whatnot because so slight slight tangent. So I used to work, back when I was in college, I used to work at the at the on campus observatory, and the there was a data uplink from the observatory to the lab, which was about a mile and a half distance. It was still running 800 baud for some serial connection.
[Bryan Cantrill] [01:14:22] Oof. 800 baud.
[George Cozma] [01:14:25] Yes. Yes.
[Robert Mustacchi] [01:14:26] You could practically run a message up there faster.
[George Cozma] [01:14:30] Yeah. But mind you, this was just a a all it was was basically just the go signal to start the power up for everything.
[Bryan Cantrill] [01:14:38] Yeah. The go signal still takes several minutes to transmit that the, the
[George Cozma] [01:14:42] It what yeah. So, basically, you would send the message, and then you would either walk or drive up. And by the time you got there, it was done. Wow. But it was like and then and then the way that you had to connect to all of it was through a through a BBS.
[George Cozma] [01:14:57] I'm not even joking.
[Bryan Cantrill] [01:14:59] This sounds like a dream that I would have that I would describe to Adam.
[George Cozma] [01:15:03] My system was built in, like, 19 eighties. It was not updated until 2020.
[Bryan Cantrill] [01:15:10] Yeah. Wow. It's definitely I'm sure I would like to leave that original designers and Oxide and Friends listeners to be like, oh god.
[George Cozma] [01:15:17] They're still that was still in use.
[Bryan Cantrill] [01:15:19] That was supposed to be
[Eric Aasen] [01:15:20] that was supposed to be for
[Bryan Cantrill] [01:15:21] a weekend. That was not supposed to be Right.
[Adam Leventhal] [01:15:23] That was a temporary fix.
[Bryan Cantrill] [01:15:24] Totally.
[George Cozma] [01:15:25] Oh, no. This was no temporary fix. It was designed like that. The
[Bryan Cantrill] [01:15:29] So Well, and and so the Nathaniel, maybe worth elaborating a little bit why the 3 megabod is so actionable for us beyond just the margining and the MS results. Because this actually ends up becoming because this is our conduit for the SP to talk to the host CPU, we use this in the recovery path. So, like, if you've got a system that can't talk to anything else, it's gonna load its image via that link and being able to go faster than 3 megabot is gonna be really, really nice.
[Nathaneal Huffman] [01:16:03] Right. Yeah. Yeah. I mean, that's that's kind of the big thing. I think the big hope here is that for Cosmo, when we do recovery, we could potentially use the, you know, a a like, I don't know.
[Nathaneal Huffman] [01:16:13] I'm hoping to get it, you know, somewhere up in the 12 megabaud, but it's gonna depend on, you know, how busy we are doing other things on that link too because it's a shared resource. So
[Adam Leventhal] [01:16:22] Yeah. And when when we talk about recovery, we're we're think about, like, DFU ing your phone or whatever. Like, we use this during the manufacturing process. So if a if a server has kinda gone out to lunch in some way or we just wanna wipe it clean, we're using this mechanism at and go to 3 megabot.
[Nathaneal Huffman] [01:16:39] Yeah. And I think we're replacing the the Spino image basically over 3 megabots. So it's, you know, slow.
[Bryan Cantrill] [01:16:45] It takes a minute as the kids say, but it actually takes like We're we're
[Robert Mustacchi] [01:16:48] actually doing 2 different things, Nathaniel. So we we first are writing the Spynor, which actually goes much faster.
[Bryan Cantrill] [01:16:54] Yes. That that part is quick.
[Robert Mustacchi] [01:16:56] But then we basically instead of sending the full m dot 2 image that we would boot from, which would be like a gig and basically be, you know, an eternity in in that world, we have a slim down basically kind of phase 2 image. So unlike a traditional BIOS where you're basically splitting up, you know, the BIOS is in your spy flash. It's it it sits there and then kinda goes and pretends to reset the world back into 1970 after waking up and changing everything and, you know, know, turning on all the CPUs so we can turn them off again. You know, we basically have a continuous operating system image. So basically but we just kinda say, hey, you find that half your, like, RAM disk, half your modules somewhere else.
[Robert Mustacchi] [01:17:38] So, we end up when we end up doing the recovery, we end up sending
[Bryan Cantrill] [01:17:42] kind of a, like, slim down just just, you know, a measly a 100 megabytes over this this small link. And actually and so George, in all honesty, like, part of the rationale for this, is to get us out of those moments of terror when you are flashing a bias, and you have gotten often no recourse if that if that goes sideways. And so this gets us out of that because we know that the system at the at the absolute lowest layers of the system, we can get the system to to be able to boot. And we it gives us much more control over the the reliability of the system, upgradability of the system, manageability of the system. That's how we're able to get at with oxide rack and can arrive power on and and get going and provision the m's in in minutes instead of days, months, weeks, whatever.
[George Cozma] [01:18:36] Speaking of sort of, again, sort of a question to you guys because this is stuff that I I know a lot more about CPUs and GPUs than I do sort of the networking and and the sort of lower level intricacies of all this.
[Bryan Cantrill] [01:18:51] Well, I feel like this is like we're like the sewer people, and you you you know, like, you get to I mean, you've got this glorious palace in terms of the cores that have been built. And meanwhile, it's like, the sewer people are happy about not being at 3 megabot. Like, what's going on? And it's like, no. It's it's a big deal down here in the sewer.
[George Cozma] [01:19:10] Yeah. But, sort of, I asked you this back when I was at your back
[Eric Aasen] [01:19:17] when I
[George Cozma] [01:19:17] was in San Francisco meeting you guys in person. What do you think of, sort of the updates to OpenSyl and how that's been going?
[Bryan Cantrill] [01:19:27] To
[George Cozma] [01:19:27] get rid of a GISA or
[Bryan Cantrill] [01:19:29] Yeah. Yeah. So we are, all in favor. So we have been and actually, it was funny because I actually first heard Turin, the the code name Turin, when it was accidentally blurted out on one of those open cell calls. I'm like, okay.
[Bryan Cantrill] [01:19:45] What is Turin? And I remember asking Robert Lightwave, like, no. That's a a city in Italy, so it must be the next thing, but we hadn't heard of it, yet. And we an open sail was gonna intersect with Turin, which, of course, when we were first doing that, it's like, oh my god. That just feels like Buck Rogers.
[Bryan Cantrill] [01:20:00] It's like in, you know, the year 2041. Mhmm. But, of course, Turin is not here. And we like, that work we are very very supportive of. We are not actually using any of that, because it it it's a different model.
[Bryan Cantrill] [01:20:17] It's kind of going to it's still a traditional model of a bootloader that's going to effectively make the system look like it's gone backwards or send the system backwards to boot a host operating system. And we've got, the this staged approach where we are running a single operating system the entire time. So it it doesn't fit our model, but we're extremely supportive of it because we believe that we want these lowest levels of the system to be completely documented, and we want there to be room for many different approaches. And so I think that we're very supportive of it so in that regard.
[George Cozma] [01:21:00] Yeah. Because I know when when we last talked about OpenSyl, it was very much in sort of the initial stage of it being ramped up and and what was happening with it.
[Robert Mustacchi] [01:21:16] And it
[George Cozma] [01:21:16] does seem like AMD is adopting more open standards with regards to sort of because they also announced Calibra, which is open source root of trust stuff.
[Robert Mustacchi] [01:21:30] Yep.
[George Cozma] [01:21:31] Yeah.
[Robert Mustacchi] [01:21:32] So we're we're excited to see how all that kinda starts to starts to change. I mean, the there's a recent, I dropped a link in there. I think they did this at OSFC. They talked about how they're they're gonna have open cell kind of be the mainstay more so for, Venice. And it's the and so I think, you know, from our perspective, this is all good.
[Robert Mustacchi] [01:21:52] It kind of gets us out there. We can start to point to things that, you know, are in open cell and ends up being a a win for, for everyone. So I think it's it's basically it's excited. We're we're excited to see it. Parts of it.
[Robert Mustacchi] [01:22:08] You know, we may able to leverage directly, but if not, you know, we can be inspired by it. They can be inspired by us and vice versa.
[Bryan Cantrill] [01:22:14] Yeah. It's and it's very nice to be able to go compare notes, especially when things aren't working. Helpful to have multiple implementations out there. And, I I also think that, like, that the the model for a Giza, the programming model makes it very difficult to reason about the overall system. This is where Robert's eyes are gonna start to twitch because Robert spent a lot of time in the absence of documentation having to, like, really understand what this code was doing.
[Robert Mustacchi] [01:22:48] And I mean, I I still think the best bit is, for me is is in s p 3 where the smooth, to do hot plug, it it speaks over I squared c and I'm pretty sure it the Smoo itself does not reset the I squared c peripheral to run at a 100 kilohertz. When the when the I squared c peripheral restarts, it starts in basically fast mode plus, which is this weird push pull mode at like faster than a 101 megahertz, which basically means it don't work. And, the only there was definitely no explicit initialization. It's just that, Hey, this Dixie module in a, you know, dependent on this Dixie, which probably just did a generic blanket I squared c initialization, which changed, you know, which reset everything to a 100 kilohertz.
[Bryan Cantrill] [01:23:35] Well, and that's it.
[Adam Leventhal] [01:23:36] I mean, you when you have these kind of this is
[Bryan Cantrill] [01:23:38] why it's so healthy to have different software ecosystems on the same hardware because you you don't want things to be working by accident. You want them to be, and it it's you want things to be well documented and with well committed abstractions. And failing that, it's good to have this the the software out there. So it's, no. It's been George.
[Bryan Cantrill] [01:23:57] It's been good. We're in we're, I think excited to continue to to see that. The some of the other, like, lowest level lowest level differences on Turin. We you mentioned the Dimps for Channel, and we Mhmm. We we kinda had a, a fork in the road in front of us in terms of 2 DIMMs per channel, 2 DPC versus 1 1 DPC, and there's a trade off there
[Robert Mustacchi] [01:24:24] Mhmm.
[Bryan Cantrill] [01:24:25] To be made. And, Robert, what was the I mean
[Robert Mustacchi] [01:24:28] Yeah. So the big so I think to help understand making the trade off for DDR 5, you kinda have to go back to DDR 4. So, when you have 2 DIMMs per channel, the way it works is that kind of in the channel or you go back even further in time, you'll actually find platforms with 3 DIMMs per channel. You basically are daisy chaining, the channel. So the the the traces will literally go up to the first dim then continue on to the second dim or to the third dim Right.
[Robert Mustacchi] [01:24:58] In those platforms. So, just the presence of that of that second of having 2 dims on there sometimes changes the SI. In DDR 4, it often didn't. So if you only had 1 dim populate, it could still get the maximum memory speed, possible. However, in DDR 5, just the presence of 2 dims per channel drops dramatically.
[Robert Mustacchi] [01:25:23] Oh, yeah. What maximum speed you can hit? And then if you actually make the mistake of populating it, then that drops
[George Cozma] [01:25:31] to GDP. The fact of having that channel. Right? So Yeah. Like like so for Turret, right, it's 6,000 up to 64100 with validation, but 6,000 with 1 DPC, 44100 with 2 DPC, and then 52100 if you're running 1 DPC in a 2 DPC board.
[George Cozma] [01:25:53] So the fact of just having that second channel
[Eric Aasen] [01:25:55] Yes.
[George Cozma] [01:25:56] You you're losing a whole bunch of your memory clocks.
[Robert Mustacchi] [01:26:00] Yeah. Then for us so then the other big changes that from s p 3 to s p 5, you went from 8 channels to 12 channels. Yeah. And so just for us, since we're kinda have this half width system, that's, I guess that's what about I don't know. One of the other, I don't know.
[Robert Mustacchi] [01:26:17] Eric and Anthony,
[Eric Aasen] [01:26:17] do you remember what the It's gonna be 10 inches wide.
[Bryan Cantrill] [01:26:19] Yeah. 300 millimeters.
[Eric Aasen] [01:26:20] So I was gonna say A PCB is, yeah, 10 inches. So 300 millimeters ish.
[Robert Mustacchi] [01:26:25] So, basically, we were in a place where, you you could fit 16 dim slots, but you weren't gonna make 24 dim slots magically appear in the space of 16. Nautilus, you got very creative. So we ended up saying, okay. Between that and the fact that you now had 96 gig and a 128 gig r dimes without going to 3 d s, which means you can actually purchase them and pay for them without, you know, a lot of blood money, then or or really you're not basically fighting against the GPUs and HBM, which means you can actually get them. Then that that kinda kinda put us down to okay.
[Robert Mustacchi] [01:27:01] Well, that you know, you want the memory bandwidth. That's definitely one of the big values here, and the memory latency for a number of applications can definitely matter, and you can still get to capacity in other ways. So that that's kind of coming
[Eric Aasen] [01:27:16] up kind of going at a
[Robert Mustacchi] [01:27:17] kinda 12 channel 1 DPC kinda configuration. Because we looked at saying, okay, was that better? The other option was, hey. 8 channel, 2DPC, and that just kinda seemed
[Bryan Cantrill] [01:27:28] Worse. The worst of all worlds.
[Adam Leventhal] [01:27:29] It seemed like the worst of
[George Cozma] [01:27:30] all worlds. I think that the 12 channel, 1DPC move is probably the the the right move. I do like that AMD is giving the option for a 2 DPC setup with all 12 channels, but I could definitely see how people would really want, especially if we especially if in the future we go to, say, 16 memory channels. There's no way you're doing 2 DPC on that.
[Adam Leventhal] [01:28:00] Right. Yeah.
[George Cozma] [01:28:02] Right? We're we're going to have to go
[Eric Aasen] [01:28:03] to 1
[George Cozma] [01:28:03] DPC. Now stuff like MR DIMMs can help with capacity and bring it bringing back that sort of 2 channel capacity, or the capacity that 2 DIMMs per channel will get you. But, yeah, I think the 2 DPC has been the writing has been on the wall for it for a long time
[Bryan Cantrill] [01:28:25] now. When I think it just in general, if when we had a trade off where we'd have to give up memory latency, we we have always felt that memory latency is you is really important. You wanna get maximum you you wanna minimize memory latency, and you you don't wanna take a a hit there. Yeah.
[Robert Mustacchi] [01:28:42] Well, in in the DDR 4 world where you went from 32100 to 2933, that was it was a very easy You've got to pay. If you were telling me to go from 64100 to 6000, you'd probably could make that you could probably make convince yourself that that that that that is actually worthwhile.
[George Cozma] [01:28:58] Mhmm.
[Robert Mustacchi] [01:28:58] But, you know, 5200, 44100, that's a that's a that's a lot farther from 6,000. It's a
[Bryan Cantrill] [01:29:05] big yeah. Right. It's a big big chunk to take out. And in terms of MR tims, because this is in a domain where, you know, in Intel is still, basically the I mean, they because we're pretty JEDEC standard on MRDIMMs. Right?
[Bryan Cantrill] [01:29:19] Yeah.
[George Cozma] [01:29:19] Get here. Let me let me let me get on my soapbox for about 30 seconds because Intel's MRDIMMs on Granite Rapids is not the JDeck MR GIMS. They are different. It's essentially just MCR GIMS relabeled, which made me tear my hair out because they're not technically compatible standards.
[Bryan Cantrill] [01:29:38] Yes. Yes.
[George Cozma] [01:29:40] So I I wanted to scream and shout and let it all out, as the famous song goes, because that was utterly infuriating to me because you're saying you have MRDIMMs, but they're not really MRDIMMs, the jadex spec. So You
[Bryan Cantrill] [01:29:57] you know, Georgia, what I love about Oxide and Friends is when it comes to the soapbox of a dims being, not being per jadex standard, it's actually a line at the soapbox here at Oxide and Friends.
[Adam Leventhal] [01:30:08] There's actually this is this is the,
[Bryan Cantrill] [01:30:12] because I this is a a soapbox. Robert, you you know the soapbox. You you you've been on the soapbox, and it's yeah. It's frustrating. But they but MRDIMS, I think when the when they are jadex standard or Rex, they will be.
[Robert Mustacchi] [01:30:26] Yeah. The the m r part of it is there. I think you'll then once the questions, you know, as it slowly enters the market and memory controller support and, you know, seeing the cost, you know, assuming you can get the cost, not to be ridiculous because volume is definitely one of the big parts of the DRAM business. But, you know, for us, because we have a platform that's not trying to scrunch everything into a 1U, you know, a higher dim just means a new thermo formed, thermoformed airflow shroud. Right?
[Robert Mustacchi] [01:30:57] And that's pretty easy to go go fit in. You know, for us the added height is not a problem. For other platforms and other chassis, you could be kinda SOL.
[Bryan Cantrill] [01:31:09] Yeah. When I think that, you know, one of our kind of big, revelations and again, this is not due to us. I think the other hyperscopes on this as well, but that the you actually, the way to have maximal density is not necessarily to have maximal physical density that you wanna open up some room, for airflow, and you can actually get higher density by having a by using a little bit more space and being, you know, we're, the rack is is 9 feet tall. And so we, you know, using some of that, trying to use some of that space, to get higher density. The, actually, can you just talk about backfilled vias for a second, Eric?
[Bryan Cantrill] [01:31:54] Just because you mentioned in the chat. I don't know. George, do you know about backfilled vias? This is this is truly amazing stuff.
[George Cozma] [01:32:01] I don't.
[Adam Leventhal] [01:32:02] Yeah. I was just Yeah.
[Eric Aasen] [01:32:06] I'm sure somebody will put a link to what the definition is in the chat as well. But, basically, whenever you design a circuit board, you have a circuit board is essentially a 2 a set of 2 dimensional layers that are interconnected in a 3rd dimension. So it's kinda like 2a half d. And so to interconnect between these layers, you have what are called vias. And these vias are, in their most fundamental form, just a tiny hole drilled in the board that's plated with copper that connects multiple layers together.
[Eric Aasen] [01:32:36] Mhmm. Unfortunately, when you get server motherboards and these bigger, higher density things, you have to use more layers and they get thicker. And it turns out that when you run IF speeds, the length of that via from the top of the board to the bottom matters. And so if you have a signal from the very top of the board going through a via to the very bottom of the board, you can make that via look kind of like a trace, like a wire Mhmm. To the signal, and it won't really notice it.
[Eric Aasen] [01:33:08] However, if you go, like, from the top layer to one routing layer down, which is, like, layer 3, skipping a ground layer, going from 1 to 3, great. Fine. But then you have this via barrel, this wire, essentially, that's hanging off this trace that goes from layer 3 all the way down to the bottom. And that piece of wire looks a whole lot like a capacitor, if I remember right in my RF. Right?
[Eric Aasen] [01:33:38] And so it basically creates a stub that causes a resonance. And when it resonates, it sucks all the energy out of your signal. And it turns out that things like DDR5 have high enough frequencies in them to require backdrilling. And to give you an idea of when you need to do backdrilling, it's I've designed boards that run, like, 10 gigabit lanes, so 10 gigi on a single lane. That's a normal, you know, 2 millimeters thick kind of thing and didn't need backfilling on it.
[Eric Aasen] [01:34:12] And 2 millimeters thick is is fairly standard for a server motherboard. 1.6 is like a commodity PCB. On when you run, like, 28 gig, you have to back drill it. And, certainly, when you run higher than 28 gig, you have to back drill. So PCIe is 32 gig in Gen 5 now, so that has to be backdrilled.
[Eric Aasen] [01:34:33] But what's crazy is even DDR running at, you know, 6 gig per lane, 12, you know, double data rate, whatever, the frequency isn't that high, but the frequency content is high enough. And because it's single ended, those vias start adding up, especially when you're routing in the top layers. And so you we now have to back drill a whole ton more vias than we used to because it used to be just those super high speed lanes like PCIe and, you know, 100 gig Ethernet and stuff like that had to be backdrilled. But now you're doing, like, thousands of these things. And it turns out backdrilling a via is really hard.
[Eric Aasen] [01:35:11] So what they do is they take and remove that stub that's left over by shoving a bigger drill bit in from the other side. So they literally drill out drill it out twice, once from the top, plate it, and then put it back in the drill, and then drill it again from the bottom. And what's absolutely crazy about this is getting those 2 drill holes aligned to within, like, a thousandth of an inch or 25 microns. And they have to do that because otherwise, they'll short things out on the rest of our board. And that takes a fabricator with very high skill.
[Bryan Cantrill] [01:35:42] What? I just love the fact that we're gonna, like, we're gonna take a drill to the underside of the board. It does feel like a a Adam Leventhal PCB engineer kind of approach to
[George Cozma] [01:35:50] this of, like, here, hold on. Pass me
[Bryan Cantrill] [01:35:52] the drill. But it it it Chris. Exactly. I need a drill and a running start, and we'll learn.
[Adam Leventhal] [01:36:00] Yeah. But I'll fix your signal integrity issue with my drill.
[Bryan Cantrill] [01:36:03] I'll fix it real good with this this here drill. The, but it it it is a total precision, and it is I mean, 25 microns is just amazing, Eric. This is and and then we we've got simulation tools that I mean, how do we that kind of figure out where this needs to be done and this is
[Eric Aasen] [01:36:24] Yeah. So we we use both ANSYS and ADS. ANSYS is our full three d, full wave solver, and then ADS is used for most everything else. But, basically, we take the board geometry or even just a theoretical via and put it into something like ANSYS HSFS and we can simulate the effect of what that via design will be on our overall channel, and you can do it by basically putting in a fake channel in EDS and seeing the effect on performance.
[Bryan Cantrill] [01:36:53] into something And yeah. Well, I was just gonna I I was gonna ask, like, these f series parts may be actually relevant for you, Erica. You and Tom and maybe yeah. Exactly. Or
[George Cozma] [01:37:52] To the 79100.
[Eric Aasen] [01:37:55] Yeah. 79100. So it's not the 3 d cache one, but it's just the normal one. But that one will boost up to over 5 gigs. So idling right now, I'm at 5.2 gig.
[Eric Aasen] [01:38:03] And that turns out to be really helpful when you're running when you're running these simulations in ANSYS that are insanely single threaded.
[George Cozma] [01:38:12] The the 9175 f is a 16 core turn part up to 5 gigahertz, but it's it's 12 c it's sorry. It's 16 CCDs with 1 core per CCD. It's designed for EVH stuff. It is it
[Eric Aasen] [01:38:27] is Absolutely.
[Bryan Cantrill] [01:38:29] I I and I just love the fact that you gotta think of, like, you know, who wants that, like, that thing in the SKU stack? It's like, oh, the engineer that actually, like exactly.
[George Cozma] [01:38:37] That's all the EDA folks.
[Bryan Cantrill] [01:38:39] It's all the EDA folks who
[Eric Aasen] [01:38:40] are, like put this thing under his desk.
[Bryan Cantrill] [01:38:42] Exactly. So we gotta get that skew for Eric and Tom and the other the other folks
[Adam Leventhal] [01:38:46] that are running these these simulations. Yeah.
[Eric Aasen] [01:38:48] I got a 5 one of those monster SKUs sitting around one of the 500 waters. I'm like, yeah, that's cool. It'll pull a lot of power. I want the 5 gig one, man.
[Bryan Cantrill] [01:38:57] Yeah. The, we we gotta get that for you. The, not a cheap part, by the way, but still No. That that it is, we had the answers folks on, Adam. Remember we had the answers along with Tom on talking about the, the our use of simulation, which is another great episode.
[Bryan Cantrill] [01:39:15] I really enjoyed talking to those folks. And you just learn about, like, the the physicality of the stuff just blows me away. And, like, I feel I mean, I don't don't you feel bad that we end up running, like, our dumb software on top of this stuff at the end of the day? I just feel like we're Kind of.
[Adam Leventhal] [01:39:29] Yeah. Seriously. Well, we've taken all these gigahertz for granted too and just like the level of complexity underpinning is is is bananas.
[Bryan Cantrill] [01:39:38] It's like we back for this thing to run PHP. It's like you look. Yes. Sorry. Yes.
[Eric Aasen] [01:39:45] Well, I can serve up cat videos on YouTube, pastor.
[Bryan Cantrill] [01:39:47] Yeah. Right. Totally. Totally. But it's just, just amazing.
[Bryan Cantrill] [01:39:51] And and this part is a great part. You know, I think that that that we're you know, I think, George, we were really excited to see, I mean, obviously, your in-depth review was terrific. But, I mean, I think, George, since from your perspective, like, this is a part that has really hit the mark in kind of, like, every dimension it feels like.
[George Cozma] [01:40:09] Yeah. So the 9175 f, I think, for any EDA workloads is sort of the turn part for that. Then you have the 9575 f, which to me feels like the drop in replacement for all the OEMs
[Bryan Cantrill] [01:40:25] Yeah. Interesting.
[George Cozma] [01:40:25] For Genoa. You you just take out all your Genoa chips and you put that in, and it's just you you get better ST, so single thread and sort of low thread count workload performance to the 96 54. So that's the top end general SKU, but basically just as good multithread performance at similar power pulling, similar power numbers. So to me, that feels like the drop in replacement. Yeah.
[George Cozma] [01:41:00] And then the big boys, the 9965 and, the 9755, those are the top end, big performance that the hyperscalers and and all the, people who can use that power will grab.
[Bryan Cantrill] [01:41:22] Right? And I think that we we are gonna be I think, you know, another thing that we're looking at is partnering with Murata and getting for those folks that actually do wanna go more than 15 k w for the rack, which was our original design target, but which felt very aggressive in 2019. But then, you know, I think I I feels like NVIDIA is like, that's like 2 GPUs now, for Yeah. And for you. Exactly.
[George Cozma] [01:41:46] I can get that to you.
[Bryan Cantrill] [01:41:49] We are are, will be for folks that can go be up above 15 k w for the rack, we'll be able to go do that. And, it's it's again, it won't it won't necessarily be quiet, but we, we think we're gonna be able to air cool that, and those that's where you get that you get that kind of 7 x consolidation that AMD was talking about. Yeah. And I think that there's And Yeah.
[George Cozma] [01:42:12] Speaking of of GPUs, something that wasn't covered in in the media, even by us, was that when AMD gave their turn presentation to the media, while AI was a big part, they didn't just when asked about HPC and FP 64, they're like, yeah. We're absolutely supporting that. Do not worry. And that was that was sort of a big relief on on my shoulders because it was like, thank god you're not just talking about AI. Like, there's there's HPC going on here.
[George Cozma] [01:42:46] There's some there's there's more than just, like, low data types. There's there's f p 64 things happening, thankfully.
[Bryan Cantrill] [01:42:58] Yeah. And I and I mean, I think that we're, I mean, excited for the AI workloads too, and I think they're gonna get a nice pop from AVX 512, certainly the 512 bit data path there, and you're gonna see, you know, a lot of those there are nice pops to be had, we think, but you're right. It was not just AI. There are, as it turns out, other we we also need the workloads to simulate the computer for the AI as it turns out. Eric Eric needs the the the,
[George Cozma] [01:43:27] So so, yeah, the the 9575 f was was targeted towards sort of the head node for AI CPU. That that was its what AMD was targeting it as, but I honestly think that in a general compute sense, it's it's sort of the all rounder in my opinion. Yeah. So
[Bryan Cantrill] [01:43:50] Yeah. We think so too.
[Adam Leventhal] [01:43:51] And I think that, you know, I think unlike with our first gen where
[Bryan Cantrill] [01:43:54] it was kind of, at every we only had one SKU, the 7713 p. We're gonna allow for some flexibility for oxide customers inside that that SKU stack. We're excited to kind of extend that and then do some of the work, around dynamic power control. We got a bunch of ideas on how we, you know, we've got the right foundation to go actually manage power holistically across the rack and and use some of the there's all we got a lot of stuff to go, a lot of knobs to turn, and I think it's gonna yield a pretty great product. I mean, the hats off to AMD for sticking and landing.
[Bryan Cantrill] [01:44:28] I mean, we are definitely wedded to AMD in a lot of ways in terms of our lowest level of of platform initialization and so on. So we're always relieved when they execute well. They Yeah. And decision in 2019.
[George Cozma] [01:44:41] Yeah. Yeah. And sort of wrapping up with instinct because there were some a lot of people were concerned about the APU chip, which I think you and I had talked about.
[Bryan Cantrill] [01:44:58] Yeah. We talked about APU. We yeah. Boy, we're we're hitting all the sympathy cards here. Alright.
[Bryan Cantrill] [01:45:03] So hold on.
[George Cozma] [01:45:03] So now I
[Adam Leventhal] [01:45:04] I did oh, do you hand me
[Bryan Cantrill] [01:45:05] the other sympathy card now?
[George Cozma] [01:45:06] So I think there was some misunderstanding or was misheard in what was said. Because when I when I went and I asked for clarification after, after the presentation, what it sounded like was they aren't making APUs every generation right now because their customers see sort of the x skews as the AI chip and the a skews as the HPC chip. So all of the big hyperscalers are only looking at the x skews. Yeah. And it's like, when when you have to fight between the hyperscalers and and this slightly more niche part, it's like, yeah, unfortunately, that will win.
[George Cozma] [01:45:49] But from what I was able to gather, it they do see the APUs as the future for not just AI, but for HBC and and moving forward. So they are continuing development. There's no ending going on. Just much like 3 d v cache, it that was announced that Turin X is not coming. And it's because there aren't the cadences are different, and there's certain dials that you get to pick, so to speak.
[George Cozma] [01:46:24] And and, Drew, when you when
[Bryan Cantrill] [01:46:25] you were asking about the APU, did they or, like, did the oxide people put you up to this? Are you No.
[George Cozma] [01:46:30] So so so this was this was something that I've been bugging them for a while about. And by the way, if you guys see an AMD Mi 300 a dev kit come out, I I'm gonna claim some some level of responsibility for that.
[Adam Leventhal] [01:46:44] Oh, that's great. Yeah. We would be the we've we've asked for yeah. That'd be great.
[Bryan Cantrill] [01:46:48] We you you will deserve responsibility for an Mi 300 A380. We'd love it.
[George Cozma] [01:46:53] Yeah. I, I've been trying to get them to to put that out. It's sell it on NewWave, like Ampere Computing sells their amp their Alterra Max bundle where it's the board and a CPU. I'm like, just sell that on Newegg for I don't really care how much money. Just have 1.
[Bryan Cantrill] [01:47:19] George, I don't know what we're gonna do for you if an m I 300 a dev kit is is for sale on Newegg, but we're gonna do something very, very nice for you. I don't know what it's gonna be yet. I I think that it is gonna be the, that would be great.
[Robert Mustacchi] [01:47:33] They We get George a whole wheel of his favorite cheese?
[Bryan Cantrill] [01:47:35] That we it's yes. Absolutely. That's right. We we for sure. But I totally agree.
[Bryan Cantrill] [01:47:43] And, yeah, we definitely noticed that the, you know, we have brought up APUs so frequently with them. We've we I feel we've kind of overstayed our welcome with respect to that sort of like, you know what? We're gonna let you guys say the next thing about APUs. We're gonna stop telling you how much we love APUs, and we'll let you do the next thing. Or we'll
[Adam Leventhal] [01:47:59] let George do it for us, which is which is great.
[Bryan Cantrill] [01:48:01] Much more effective much more effective. Well, we'll say yeah. Again, if we get we if we get an m I three hundred a dev kit on on on Newegg, it's gonna be I we're gonna have to do, it's gonna be something spectacular. Yeah.
[George Cozma] [01:48:15] But, yeah, I I I've been pushing them to to do that. And in general, I've been pushing them as much as it's within my ability to, fix certain parts of their software stack. Rock them.
[Bryan Cantrill] [01:48:31] Yes. Yeah. Yeah. Well, you know, and I think that you I think and just actually, honestly, with OpenSail, I mean, I think one of the things that we really like about AMD is it's a company that does, like, it listens.
[Adam Leventhal] [01:48:40] I'd like they they
[Bryan Cantrill] [01:48:41] kinda they know what the right direction is. It takes them a while to get there sometimes because it's a big vessel and, but, you know, I mean, I remember when we were getting Naples stood up way back in the day and, you know, there was a lot that was still needed to be done, but you could see that, like, okay. This is not a trajectory that's really interesting. And then with Rome, it's like, okay. This has just got a lot more interesting.
[Bryan Cantrill] [01:49:09] And it was clear to us in 2019, Robert, that they were they were, on a trajectory or they were surpassing Intel effectively. And then obviously with Milan and and with Genoa and now Churn, I mean, it's like we've seen them, like, continue to execute, execute, execute. And,
[Adam Leventhal] [01:49:25] so, yeah, let's go let's keep Adam on the APU side. Let's
[George Cozma] [01:49:29] Yeah. Yeah. On the APU side in in just in general on the sort of getting there. Because the perennial problem for AMD has been software.
[Robert Mustacchi] [01:49:37] Yes.
[George Cozma] [01:49:37] And and to the best of my ability, I've been trying to
[Bryan Cantrill] [01:49:41] Well, that's okay.
[George Cozma] [01:49:42] Get through to them that Let offside that software. Rackham support on every single piece of AMD. Anything that has the AMD logo on it should run rock, period.
[Adam Leventhal] [01:49:54] Yes. Right? Yes.
[George Cozma] [01:49:55] With the one exception maybe being consoles because those are a special little thing, but that's that's, that's a different argument over there. That's for Sony and Microsoft to take up.
[Bryan Cantrill] [01:50:07] Absolutely. Yeah. No. No. Love it, and I totally agree.
[Bryan Cantrill] [01:50:11] And, you know, we're it helps. They're hearing it from from
[George Cozma] [01:50:14] Yeah. But it And if any AMP users are listening to this, at at supercomputing and at CES, I'm going to be harping on you guys.
[Adam Leventhal] [01:50:23] Yes. So we we love the parts and, and and we're gonna be, we want you to
[Bryan Cantrill] [01:50:29] be got some ideas for things to be even better, but, touring is a great part. We're really excited about it. And, George, thank you very much for for joining us. It's been great to have Well,
[George Cozma] [01:50:41] thank you for having me.
[Bryan Cantrill] [01:50:42] Oh, yeah. It's great to have the team. I mean, and, Nathaniel and Eric here and, and Aaron as well. It's been, and obviously Robert here in the studio with me. And then Adam, of course, to correct my pronunciations and to inform me that my running start is not quite big enough on the back drilling.
[Bryan Cantrill] [01:51:00] The, you know, I I think it's been, we're really excited about our forthcoming. So I don't think it's we're excited about is, of course, you're gonna be able to take the taking a touring sled and putting it into a an unused cubby in an, in a an oxide rack that has Mulan sleds and just have the whole thing just work. So we're really excited about that, and onward. Great part. And, George, thanks again.
[Bryan Cantrill] [01:51:24] Really, really appreciate it, and and thank you all for joining us. Thank you, Adam. Speaking of ex
[Adam Leventhal] [01:51:30] speaking of excitement.
[Bryan Cantrill] [01:51:31] Speaking of excitement, we do have one very exciting announcement. That's right.
[Robert Mustacchi] [01:51:36] Take it away.
[Adam Leventhal] [01:51:37] DTrace dotcom. We're back. So, DTrace dotcom is our approximately quadrennial 12/16. We're excited for 2020, canceled, and now we're back. So, we're gonna put the link in the notes.
[Adam Leventhal] [01:52:09] Link is gonna go out to the folks who are here live, but is December 11th coming right up? So we'll it's it's gonna be an unconference?
[Bryan Cantrill] [01:52:18] It's gonna be an unconference. If you were a DTrace user, you wanna come hang out at Oxide, we that we we are gonna charge you
[Eric Aasen] [01:52:24] for tickets. Not gonna charge
[Bryan Cantrill] [01:52:25] you too much money, but we do have to charge you something. Otherwise, it'll be, immediately, consumed by teenagers. Teenagers will consume every ticket if we don't charge you anything. So, very limited supply. So, hop in there if you're interested in joining us.
[Bryan Cantrill] [01:52:41] Yeah. It's gonna be Adam, I I'm I'm really excited for this. This is gonna be fun. Oh, it's
[Adam Leventhal] [01:52:44] gonna be great. I I mean, I I mean, I I feel like it's rude for me to say it's my favorite conference, but I've always loved it. I've I've loved it.
[Bryan Cantrill] [01:52:51] I've always loved it.
[Adam Leventhal] [01:52:52] It's been terrific.
[Bryan Cantrill] [01:52:53] And it's gonna be yeah. It's gonna have a different complexion and flavor this year for sure. It's gonna be a lot of fun. So,
[Robert Mustacchi] [01:53:00] I'd I'm looking forward to it. That's for sure.
[Bryan Cantrill] [01:53:01] That's right. We're I know, Robert, you got to everyone is just like, okay. What do I need to get done now before I've got until December 11th to get said to get my, with but we got a lot of things to talk about. So it's gonna be fun. So join us.
[Bryan Cantrill] [01:53:12] Tchoice.com 2024. And I will I I will not try to I will not violate any more copyrights by I mean
[Adam Leventhal] [01:53:20] With your helmet. I think I think I think we dodged the bullet on that one. I think Yeah. I don't I don't know that it was so recognizable.
[Robert Mustacchi] [01:53:26] Exactly. That's
[Bryan Cantrill] [01:53:28] Awesome. Alright. Well, George, thanks again. Thank you, everybody. And, yes, you at dtrace.com 2024.