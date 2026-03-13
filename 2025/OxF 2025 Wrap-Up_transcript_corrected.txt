[Bryan Can trill] [00:00] Hello, Adam.
[Adam Levinthal] [00:01] Hello, Bryan. How are you?
[Bryan Can trill] [00:02] I'm doing well. How are you?
[Adam Levinthal] [00:04] Pretty good. Pretty good. Lots going on in the world, but glad to be here.
[Bryan Can trill] [00:08] Oh, is there anything going on? Is there any anything of note?
[Adam Levinthal] [00:11] I wouldn't, you know what? If you've missed it, wouldn't bother looking.
[Bryan Can trill] [00:14] Exactly. Please don't. Yeah. This is I'm excited about this episode. You know?
[Bryan Can trill] [00:19] I'm I'm excited for this tradition, the our annual wrap up. Actually, before we get there, because we honestly, if we hadn't already planned this episode, we might be talking about this RFD that I wrote a week and a half ago, the RFD five seventy-six on using LLMs at oxide. I have been shocked at the am I stupid to say this?
[Adam Levinthal] [00:41] No. I people feel really people feel really excited about it, I think. Is that what you're saying?
[Bryan Can trill] [00:47] The the am amazed at how hot this issue is just in general. I mean, because I felt like I was saying something that was very, like, very neutral in the way. It's like very, like, reasonable middle of the road, not too extreme and I this thing got a huge amount of pull. I mean I made the RFD public because I thought like one or two people of Blue Sky might like to find a spelling error which actually they did. So thank you Blue Sky.
[Bryan Can trill] [01:13] The spelling error is jumping up. But then I was like, we're going to a dinner party this last week, and it's the top story on Hacker News. The number one story on Hacker News.
[Adam Levinthal] [01:21] That had escaped my attention. I would say, and I mean this with all respect, like, I read it, and I think my feedback was like, yeah. Okay.
[Bryan Can trill] [01:29] Milquetoast.
[Bryan Can trill] [01:30] No. I mean,
[Adam Levinthal] [01:31] I don't I mean, no disrespect was just like No.
[Bryan Can trill] [01:33] No. No. No. No. This was my view.
[Bryan Can trill] [01:35] Like, my view was like very like just like punching a clock doing, you know, like, yeah, like just making sense. It's fine. Like nothing like not a number one story on Hacker News. So that was an an a shock. And then I was going to be like, okay, we're about to go to a dinner party.
[Bryan Can trill] [01:50] It's the number one story on Hacker News and the comments are just like, I'm like, I have to like to turn my phone off. I'm like, God's plan. What you whatever happens at this point, you know? And fortunately, it was like it was all fine, basically. I mean, more or less, you know, the but the haters eventually they once you get to a certain amount of traffic, like, haters are always going to show up.
[Bryan Can trill] [02:11] For
[Adam Levinthal] [02:11] sure. But I feel like, I mean, your point of, like, you know, you should spend as much time writing a thing as you expect people to spend reading the thing. I can understand it as being, like, I don't know, like, not obvious, but like I
[Bryan Can trill] [02:28] feel exactly the same way. Like, I guess I was splitting the atom on that one. Didn't feel like it really. But a lot of people like, that in particular, that really resonated with a bunch of folks. I think we're kind of feeling the same thing and struggling to kind of put words to it.
[Bryan Can trill] [02:45] So Yeah. All of that kind of put me on like, I wanted to flesh out a little bit and I got some great feedback and I updated a bit. And then I wanted to go back and listen to something I'd started listening to which is Evan Ratify's Shell Game podcast. Have you listened to any of this?
[Adam Levinthal] [03:00] I've started it. Yeah. I started this weekend.
[Bryan Can trill] [03:02] It is very good. It is outstanding. I guess so if you are especially, you know, kind of in the holiday season here, there are a lot of menial tasks that need to be done where, you know, maybe a podcast and some spiked eggnog might help you get you through it. You you you want to be putting on shell game.
[Adam Levinthal] [03:18] There you go. That's halfway there. Then and then pull up the eggnog. Right?
[Bryan Can trill] [03:21] And pull up the eggnog. It is so if you are you on season one or season two?
[Adam Levinthal] [03:25] I skipped season one. I went straight to season two.
[Bryan Can trill] [03:28] Which does I think like the that's that's a good idea. Although I think Susan in season one is excellent. The one thing that you get, and I think you should listen to season one even after having listened to season two. The and in season one, he creates a persona of himself that he unleashes into the world, and it is really fascinating. But season two is absolutely unhinged because he creates a startup with these personas that he creates.
[Bryan Can trill] [03:57] And I mean, I don't know. Have you I'm more are you going to get I'm just finding it mesmerizing? Think it's amazing.
[Adam Levinthal] [04:02] I think it's great. I think I actually played Ultimate Frizzy with Evan for many years in San Francisco, and I think if I recall correctly in Wired, probably, like, fifteen years ago, he, like, tried to delete himself from the Internet. And He did.
[Bryan Can trill] [04:16] That's right. Yeah. He did. And he was found after a month. Yeah.
[Bryan Can trill] [04:19] He challenged the internet to find him and the internet found him. Yeah. Which well, you know that you definitely recall correctly. So the fact so we got a I mean, I know this is not it's supposed be a wrap up, not a preview of next year, but we have to get him as a guest. Yeah.
[Bryan Can trill] [04:32] For sure. Yeah.
[Adam Levinthal] [04:34] And Morris Chang too. Right.
[Bryan Can trill] [04:36] Morris Chang. Yeah. I mean, think I played ultimate Morris Chang. So maybe I'll go after, you know oh, actually the fact that you played the ultimate evidence, does that mean that I should be asking him, or you should be
[Adam Levinthal] [04:44] asking him?
[Bryan Can trill] [04:45] I mean, you can hear this in the spirit, which is attended. Right? Mean, this
[Adam Levinthal] [04:49] is very astute question and I can ask him in this case only.
[Bryan Can trill] [04:56] Okay. That's good to know. You're on the same team. That's good. Yeah.
[Bryan Can trill] [04:58] They that's that's that's good to know. And so anyway, highly recommended it. Highly recommended podcast. Really, perfect listening. And I'm like, next episode of season two drops on Wednesday.
[Bryan Can trill] [05:11] I can't wait. And perhaps in fitting with that, actually, before we talk about like wrapping up 25, I feel like there's a there are some headlines of 25 from an oxide and friends perspective.
[Adam Levinthal] [05:24] Okay.
[Bryan Can trill] [05:25] I mean, actually, one kind of surprising thing, do you and have you already done this about the number of episodes? Or maybe you know, just automatically know this. Maybe your brain is just hardwired in the transistor.
[Adam Levinthal] [05:34] You mean, like, how many we've done
[Bryan Can trill] [05:36] this How many we did in 2025 versus 2024 versus '23?
[Adam Levinthal] [05:40] I don't know that off the top of my head. My guess is
[Bryan Can trill] [05:42] What's your intuition?
[Adam Levinthal] [05:43] My guess is more than last year and probably more than the year before, but maybe less than the year before that.
[Bryan Can trill] [05:50] That is exactly right. And it but the numbers this year, last year, the year before is all basically the same. I thought we did a few episodes this year. I really did. Furthermore, I thought we know, but I had to go was down in Mexico with the did my mom, and I just felt like we or we did fewer episodes, but we didn't.
[Bryan Can trill] [06:06] We actually are going to do, like, one more episode this year than last year.
[Adam Levinthal] [06:09] Yeah. I I I I did know that we were, ahead of pace. I think we had some, like, hiatus where it wasn't working out for you and me, and I had seen that we were ahead of pace. So why see why, you know, we can skip it. We can give ourselves some time off.
[Bryan Can trill] [06:20] Yeah. No. It's good. Alright. So that was a little bit of a surprise to me, but I thought that was interesting.
[Bryan Can trill] [06:25] But I feel that the the big news, if a big reveal last year was the all the sweat on the brow with the images. I mean, I thought it big reveals last year. I think I go. I think that people, you know, they knew they appreciated it, but they didn't know why. And now we've got and so how do you feel?
[Bryan Can trill] [06:46] Because now, mean, obviously changed everything. We kind of broke the seal on that and now, you know, we pulled back the curtain.
[Adam Levinthal] [06:53] I mean, a lot of pressure, obviously. I was looking back at the Europe images, and they were like, good. I don't know. Like, I feel like
[Bryan Can trill] [07:00] Come on. Come on. Come on. Are we no? I understand what you're doing, and it's fine.
[Bryan Can trill] [07:06] You want us to walk out. No. Let walk us up to it. So we so we call our someone's that are really special.
[Adam Levinthal] [07:13] I will say there were a couple that I really liked. A couple I really liked.
[Bryan Can trill] [07:17] And I
[Adam Levinthal] [07:17] bet you and I are gonna we should write it on a card and flip it over.
[Bryan Can trill] [07:19] I don't think
[Adam Levinthal] [07:20] we need
[Bryan Can trill] [07:20] to do that. I think we know what it is.
[Adam Levinthal] [07:22] Okay. But
[Bryan Can trill] [07:23] I'd say I
[Adam Levinthal] [07:24] have absolute confidence. Okay. On three. One two three. No Egress.
[Adam Levinthal] [07:28] Oh, wow. Okay. Hey. Oh, wow. What was what the AI was the AI discourse one?
[Bryan Can trill] [07:35] This is with Flank. Right? I think it's AI discourse.
[Adam Levinthal] [07:38] Yeah. Yeah. Yeah. Well, I'm I'm trying to remember what the image was.
[Bryan Can trill] [07:41] Oh, come on. Yeah. Yeah. I just wish Oh,
[Adam Levinthal] [07:44] yeah. I did love that one. This is
[Bryan Can trill] [07:46] I I I knew it. So you were thinking of was second place, which is fine. I didn't
[Adam Levinthal] [07:49] know we were doing second place.
[Bryan Can trill] [07:50] I thought we were bringing in order from first to second, not to second to first.
[Adam Levinthal] [07:54] This was an image. I mean, I don't know. The reason I think I think I think I didn't pick that one because the thing I love most about it, like, only I love about it. So the images of you shared
[Bryan Can trill] [08:07] That's not true. I love about it too.
[Adam Levinthal] [08:09] I love it about it too. It's you sharing a milkshake with a robot. With a robot. Which I really enjoyed. But then the thing that had me tittering, and I think basically nobody else, is if you watch is you watch the YouTube episode, it pans over the span of, like, literally twenty minutes.
[Adam Levinthal] [08:29] It pans over to me, like, checking my phone next to you. Like, I'm third wheeling it with you on a date with a robot, and then it pans back.
[Bryan Can trill] [08:39] And you had told me that there was something very spec actually, are two very special things in that episode. So we'll talk about the second as a segue to something else I wanna talk about. But the there are two very special things in that episode. One of it is this kind of panning thing. You had but not been as specific.
[Bryan Can trill] [08:53] You said, I really want you to listen to this episode. I think you're going to like it. And I was grocery shopping, listening to the podcast as one does. And it what it had its desired effect where it's just kinda like, I looked out on my phone like, what's when did that pop up? Like, when did it's now Adam.
[Bryan Can trill] [09:07] And it wasn't Adam wasn't here and then it so no. I wish you could have been I wish I should have been wearing, you know, the the the helmet cam when I was in the grocery store. But the the the selfie cam, you would have really you would have really Okay. It hit the mark. It is you could not have asked for anything more.
[Bryan Can trill] [09:26] I it was confusion, and then it was delight, and then it was, oh, what whimsy. What what what a whimsical what a whimsical cohost I have.
[Adam Levinthal] [09:34] There you go.
[Bryan Can trill] [09:35] How delightful. It was really it was all these feelings.
[Adam Levinthal] [09:37] It was really great. I love that for all of those folks who are, like, staring at the unmoving YouTube video. Right? The people who are like, no. No.
[Adam Levinthal] [09:46] I'm going to listen to Oxide and Friends and stare at the image for an hour and
[Bryan Can trill] [09:50] a half. It's kind of like up in a window or whatever. No. This is what makes it even better because it's just like off to the side. And then you're like, wait.
[Bryan Can trill] [09:56] Has it changed? It's like, it has. It has. I'm glad you asked the question. So I thought it was great.
[Adam Levinthal] [10:01] The one I picked Yeah. The the the episode that we had done that you titled I believe you picked came up with the title, hell is other networks or maybe
[Bryan Can trill] [10:08] those collaborations. Networks, but Maybe. But give it to you. Yeah. Fine.
[Bryan Can trill] [10:13] But I'll take it.
[Adam Levinthal] [10:13] But then having the know, you're using the the the complaining on no exit, making it no egress just felt like I love that one.
[Bryan Can trill] [10:26] It was genius, and it should be said that was a ChatGPT or that was an LLM suggestion.
[Adam Levinthal] [10:31] That's right. ChatGPT joke, but perfect.
[Bryan Can trill] [10:35] It was like the first and maybe only ChatGPT joke that I actually, like, laughed at.
[Adam Levinthal] [10:41] Yes.
[Bryan Can trill] [10:41] That was funny. Yeah. No egress is funny. That's like no egress is just straight up funny, which tells me that it's just like cribbing the joke from someone else. Has someone else already done no egress?
[Bryan Can trill] [10:49] Surely. You know, we have we checked the mailbag recently? We probably have some a letter from an angry podcaster who's like,
[Adam Levinthal] [10:56] you stole
[Bryan Can trill] [10:56] not just my gag, but my image. Like, the LLM did it. We did.
[Adam Levinthal] [11:00] We Well, I made the image. The LLM just gave me the idea in Well, it is
[Bryan Can trill] [11:04] a great image. It is it is a mean, I thought that was genius. And that was really no. I mean, I thought that was also like, it's a level of seriousness that you often don't find in awe. I mean, it's just like really getting into existential thread, you know.
[Bryan Can trill] [11:16] Absolutely.
[Adam Levinthal] [11:17] The deep cuts. Yes.
[Bryan Can trill] [11:19] The the the deep cuts. So I thought that was are there other images that we wanna call, and how has it been to have though to kind of democratize this and have other people aware of this? Has it helped you? Has it been kind of like, need people to kinda get out of the workshop while I'm working? Is this just like, you
[Adam Levinthal] [11:36] know No. No. No. I think it's like I mean, I was looking back at the images from this year. A bunch of them I was kinda counting how many were just AI?
[Adam Levinthal] [11:46] Because I don't know that I love that affect. And actually, not that many were just Not
[Bryan Can trill] [11:50] that many. No. No. No. We don't use it.
[Adam Levinthal] [11:52] Yeah. But almost all of them, I've I have some AI assistance,
[Bryan Can trill] [11:56] which Yes. Which is sort of telling. It is telling. Yeah. You know, aspect ratio this is the aspect ratio is wrong is the thing I get from you a lot.
[Bryan Can trill] [12:04] The aspect ratio is wrong. Can you fix this? Never mind, I've got it. I feel like I've got that exact dialogue in the several oh, I guess several times over.
[Adam Levinthal] [12:13] Yeah. That's right. But, like, you know, just having it again, not the subject of the image, but the surround, just like great for the lazy man's Photoshopped.
[Bryan Can trill] [12:25] And then we did hit I would say we hit the Simpsons a little harder this year.
[Adam Levinthal] [12:29] 100%. This was like
[Bryan Can trill] [12:31] really tacked into it, and it's just like, we're let's just mask off. We're just gonna really let's see if we can get that cease and desist.
[Adam Levinthal] [12:38] Exactly. No. Totally. It's like Fox like Disney, please. Like, the cease and desist will just post the address right on the images.
[Bryan Can trill] [12:45] Yes. Please, we're kinda begging for it. But so no. I thought and a bunch of good ones. I mean, I thought a bunch of, like, good I mean, you could look.
[Bryan Can trill] [12:51] You can rely on us that, like, if you're going to get a Simpsons reference from us, I mean, there are certain things you know about it. You know it's going to be certainly in the first twelve seasons, probably in the first eight. It's going to be something that you should be aware of that a Simpsons scholar and I we've gotta like talk about the grown up CFS data corruption bug image because I feel like that's a deep cut. That is a Simpson's deep cut.
[Adam Levinthal] [13:14] That is a Simpson's deep cut. Yes. This is Rusty the clown holding up a contract. And this was like a reference. I mean, even within the episode, it's a deep cut.
[Adam Levinthal] [13:26] It's
[Bryan Can trill] [13:27] It is. It is.
[Adam Levinthal] [13:28] I mean, because it was a reference to, like, Matt Aron's, founder like, creator of ZFS, giving us an email, which we have referred to instead as the affidavit as though it is some binding contract, which news to him.
[Bryan Can trill] [13:43] I mean, was funny because we referred to the affidavit so frequently inside of Oxide that it had only occurred to me that we had never really told Matt about this. And that's like, what? Yo yo yo. Sorry. You were under oath when you sent that email.
[Bryan Can trill] [13:52] Are you unaware? Yeah.
[Adam Levinthal] [13:53] Well, I
[Bryan Can trill] [13:54] thought well, anyway, you were. So
[Adam Levinthal] [13:57] So, you know, that's what's up. Yeah.
[Bryan Can trill] [14:01] But then you is, but it's its a deeper cut than that because wasn't that trimmed from the broadcast?
[Adam Levinthal] [14:07] Oh, that's right. That's right. That I forgot about that. Yes. Right.
[Adam Levinthal] [14:11] So that was a scene that you were familiar with because you have been watching streaming. And I only watched, like, in college on broadcast TV, You know? And they cut scenes from syndication. So this is from one of the scenes that was not in syndication.
[Bryan Can trill] [14:32] Yeah. We are at undergrad. We are deep into grad school here when we're talking about the Simpsons. This I thought that was really that was an impressively deep cut. And you had a couple of it, I thought.
[Bryan Can trill] [14:41] And then also, like, I mean, some very just important, you know, you've got, like, clearly, Major Bob stepping on the rakes. I mean, it's just like this is I mean, if you're not, if you haven't watched that scene, I mean, you just these are things that you should be, you know, trying to help you out in your education. That's right.
[Adam Levinthal] [14:55] That's right. Homer designing a car pointing to it. I felt a little bad implying that, like, Dave, our esteemed colleague who gave a great talk was Right.
[Bryan Can trill] [15:04] It was a
[Adam Levinthal] [15:05] a dumb shit pointing at a doodle. You
[Bryan Can trill] [15:08] can't take these apart too much. I mean, like, AI in higher education with Michael Whitman had a homer again while the nerds are are are busy at work. And I'm not even sure who's what in that metaphor. So you can't take this apart.
[Adam Levinthal] [15:21] You have to pour yourself into it. Like, I think we can all see ourselves in that picture somewhere.
[Bryan Can trill] [15:25] Exactly. Exactly. You're all in that picture somewhere.
[Adam Levinthal] [15:27] We are all the nerds, and we are all homer.
[Bryan Can trill] [15:29] We all Homer. The'll reflect. Please write a non LLM generated essay. Okay? Because I we in Simpsons three zero one or whatever course this is.
[Adam Levinthal] [15:39] Another image I love
[Bryan Can trill] [15:42] so I I I when you're going to go there, I'm I always want to put episode. Over. Image the Go.
[Adam Levinthal] [15:48] At the episode, long time in the making, this is the TLB speculation data corruption
[Bryan Can trill] [15:53] bug Yeah.
[Adam Levinthal] [15:54] That I had been pestering you about for two years, like,
[Bryan Can trill] [15:59] Yeah. Literally.
[Adam Levinthal] [16:00] Yeah. Is just you, head in hands, like, to output that made no sense. Like, literally could not happen output.
[Bryan Can trill] [16:12] It is a great image. It is a really, really good image. No. And that and that one is just like a screen grab from a meeting basically.
[Adam Levinthal] [16:19] That's just
[Bryan Can trill] [16:19] that is just like literally be in my basement trying to like grapple with tears in the fabric of reality. And that was perfect. No. I thought you're going to say AI materials and fraud with Ben Schindler on the Aware the World's Crumble in San Diego.
[Adam Levinthal] [16:37] And That was fun.
[Bryan Can trill] [16:39] That was a thought that was a great image that you
[Adam Levinthal] [16:43] Yeah. Scrapped together. Yeah. Was fun.
[Bryan Can trill] [16:44] Yeah. Was that not I mean, am I ever playing that one?
[Adam Levinthal] [16:47] No. No. I like that. It took a little bit of, you know, artistry of form. And that was a fun episode.
[Adam Levinthal] [16:53] And you sent me an article recently from the Wall Street Journal where they had been apparently listening to the podcast. I
[Bryan Can trill] [17:00] think it's a little generous. Yeah. Let's say. Let's say. Let's say for purpose.
[Bryan Can trill] [17:04] Yes. Yeah. And what's going to happen if I drop in that gift link into the discord? I think it'll be fine. We'll put the gift link at the discord and then the Wall Street Journal can send me a cease and desist.
[Bryan Can trill] [17:14] Then you know what, Wall Street Journal, unlike Fox, I feel I can't rely on them to send me a cease and desist. So Fox, you could really learn a thing or two from the Wall Street Journal. The but that was like it would because it was an update on know, you know, I re listened to this. You re listened to that episode, or we listened to that episode No, First, I'd like to apologize for my bad audio while I was in Mexico. So I know the apology is not accepted for many people, but I just want to put that out there that I am I'd like the record to reflect that I am apologizing.
[Bryan Can trill] [17:41] It really was kinda bad. So It was as I recall, it was like echoed. Right? It was echoed. Yeah.
[Bryan Can trill] [17:46] It was I was in a mean, my mom's place down there is a very know, it's a lot of tile.
[Adam Levinthal] [17:51] Yeah. It was like tile it was like you were, you know, sitting in a tile cube. It was like
[Bryan Can trill] [17:55] I was sitting in the tile cube. I was. So I, but I feel like that's that's a bit of an excuse. I feel like I could have done better.
[Adam Levinthal] [18:00] So Yep.
[Bryan Can trill] [18:01] I apologize for that.
[Adam Levinthal] [18:02] Well, look. An apology not accepted. And to the haters who are like, your audio sucks. It's like, yes. Our audio sucks where we're sitting.
[Adam Levinthal] [18:10] Like, no amount of taking out a Discord is going to improve Brian sitting in a six sided cube of tile.
[Bryan Can trill] [18:17] Like, that's not Discord's fault. This is you can't hang out on Discord. That's on me. Wait a minute. Hold on.
[Bryan Can trill] [18:24] That's what I wait. Oh, man. Duck season fire. Thank god. A 100%.
[Bryan Can trill] [18:31] That is you know, that's a duck season fire, is that a reference that that travels? No way.
[Adam Levinthal] [18:37] No way. Not a chance. Really? Like, I feel like I mean, bugs I feel like Bugs Bunny is like But baby go overtly racist? No?
[Bryan Can trill] [18:48] Oh, what? You can't make has Bugs Bunny been cancelled? I can't make a Bugs Bunny reference?
[Adam Levinthal] [18:52] I'm not sure. I you know what? I'm just not going to. Maybe Chad can weigh on this one. I'm just not I'd like a 100 a 100%, there are some impersonations that Bugs done has done that were not okay at the time and certainly are not okay now.
[Bryan Can trill] [19:09] Well, dear listener, if you are hearing this in the podcast feed, we have decided that Bugs Bunny is insufficiently not cancelled to leave it in, or we couldn't find it.
[Adam Levinthal] [19:18] Sorry. Forgot to look for it.
[Bryan Can trill] [19:20] I forgot to look for it. But okay. So the know, the other thing that I that was obviously a very big deal this year was the introduction of the chime. Yes. That's very controversial.
[Bryan Can trill] [19:35] Okay. So and actually, just kind of meta question on the the chime. Are we ringing the chime in this? Have you decided
[Adam Levinthal] [19:45] before we're gonna No? I think we think it would be
[Bryan Can trill] [19:47] Kim kind of been I've I've kind of okay. Can can can we workshop it a little bit? I said, you say no chime in this episode just because you think the chime would be going off all the time.
[Adam Levinthal] [19:55] That's right. That's right. I think the whole thing is a retrospective. And to chime I mean, the the the chime is actually intended god. I can't believe I'm saying this.
[Adam Levinthal] [20:06] As like a gift to listeners. Right? To know more. To know more.
[Bryan Can trill] [20:10] Oh, that's great. That I definitely was going to say that. I do listen. Let let let the record reflect that as Adam who believes that is a gift. I know it's you.
[Bryan Can trill] [20:19] It's for you. Sure. You're like, can I do you keep the receipt? Is it have a gift receipt? Can I
[Adam Levinthal] [20:24] Was it this I think it was the season that we did the JJ Air horn?
[Bryan Can trill] [20:29] Okay. That was the second thing I was going to say from that the AI discourse episode was the so you had introduced the chime. I think the chime is delight. I think the chime is so delightful that I think that we should potentially have it be in this episode. I will I think it's for your consideration because I think that the because it will make it very clear noted.
[Bryan Can trill] [20:50] It will make it very clear what the chimes for, which apparently some people confuse the chimes for. The chimes to make reference to previous episodes. In the end we think we only kinda do it for once per episode. Like, we bring up an episode we haven't talked about. We hit the chime.
[Bryan Can trill] [21:01] We don't like we don't nail it on every sentence you're talking about.
[Adam Levinthal] [21:04] Yeah. And dear listener, I have been reducing the volume of the chime with each episode to the point where it's fainter and fainter.
[Bryan Can trill] [21:11] Oh, really? You big chicken. I didn't notice that. Yeah. A little insight there, a little insight or information for folks.
[Bryan Can trill] [21:18] That's what that the it's like, you know, I was an Oxide fans back when the chime used to be abrasive. Now you can barely hear it.
[Adam Levinthal] [21:27] I when you yeah. Used to be, oxide listeners, that you had to know it was coming and take off your headphones, lest you be deafened. Yes.
[Bryan Can trill] [21:33] Yeah. Exactly. You would duck and covered. So the no. So I think the chime is delightful, but I was re listening to I was re listening to the AI discourse episode and I truthfully had forgotten about when because we would always joke with Flank that whenever you know whenever he hit you know JJ, we mentioned JJ you know you got to kind of ring a bell And he hit JJ, and boy, you did a lot more than ringing a bell.
[Bryan Can trill] [21:57] That was a what do you even call that? What does that sound? That's of like
[Adam Levinthal] [22:01] That I know that as MLG Air horn.
[Bryan Can trill] [22:05] MLG Air horn. Do know MLG
[Adam Levinthal] [22:07] Do you know what MLG stands for? No. No. My understanding is it stands for Major League Gamer. Major League Gamer?
[Bryan Can trill] [22:15] Yeah. Oh, interesting. Is that okay. Where are we? Are we like millennial, gen z?
[Bryan Can trill] [22:20] Where are we on that? Obviously not Hers. I On that one.
[Adam Levinthal] [22:23] Think it's like gen z creeping into millennial and like, we sound like boomers to be clear.
[Bryan Can trill] [22:28] Like right now, we are getting boomer. Don't care. We are giving we are giving old people, which is as Susanna described, the change lock music. Yeah. Don't care about that one.
[Bryan Can trill] [22:37] I that one is the I'm I'm really just, you know, I'm I'm I'm just trying to expand my knowledge, man. There you go. So
[Adam Levinthal] [22:46] and there was one Yeah. I think I only did one other sound effect this season, which was another gift to you more recently. Do you remember this was for the episodes not done?
[Bryan Can trill] [22:58] The episodes not done?
[Adam Levinthal] [23:00] So you were talking about yeah. We were you were talking about, like, an episode. I think we like, we didn't do an episode on, but we should have probably on one of the rust async bugs that Rain had encountered.
[Bryan Can trill] [23:13] Okay.
[Adam Levinthal] [23:14] And you were, like, calling for the chime for an episode that didn't exist. And I gave the price is right failure, like, womp.
[Bryan Can trill] [23:23] Womp. I know, I think I had remembered that, but forgotten it.
[Adam Levinthal] [23:28] There we go. Or
[Bryan Can trill] [23:29] know. Know. Getting Womp in there. That that that's so when that must have been well, I don't know. Off code Dig
[Adam Levinthal] [23:34] by that. Most recently with rain. Like, just a couple of weeks ago, think when
[Bryan Can trill] [23:38] we were talking about yeah. And maybe future lock.
[Adam Levinthal] [23:40] Future lock?
[Bryan Can trill] [23:41] Yeah. Yeah. Yeah. Future lock, a great episode. So we did ask, I love the chime.
[Bryan Can trill] [23:49] I thought I think the chime was a great add. It's a deep pull. I think it's, you know, the fact that it's a sound from a visceral sound from your youth, our kind of shared youth, that was great. And I I I love kinda having that callback through these episodes and I know people online hate it. And I guess, I mean, it is what it is.
[Bryan Can trill] [24:07] I don't know what does I think that the Agree or disagree. Agree or disagree. I want I'm like, this like, we have no ads. Like you, you literally never have to fast-forward through anything other than our banter and like yeah, you get the occasional chime. Like that's think of it as a sub second ad.
[Bryan Can trill] [24:22] So that's that's what I have to say on that. Okay. So I also did the experiment we did too of, you know, that's kinda like that it's been super busy and I just didn't have a huge amount of time to prepare for this. So you know, as you do, want to see what our little LLM friends would how they would do a wrap up for this year. Did you do
[Adam Levinthal] [24:42] this? No.
[Bryan Can trill] [24:43] Oh, it was fascinating. So I did a wrap up with both Gemini and with Changed. So this Change five two and Gemini three with deep thinking or whatever on the you know, everyone's you know, deep research three five I don't know whatever. Pretty interesting. So one, I will say this, on the asked them to like to taxonomize it and both of them really nailed it.
[Bryan Can trill] [25:10] I mean, one of the things that we, you know, the episodes did have a different tone this year. I don't know that it's deliberate. I think it's I mean, it's consequence of couple different things. But, I mean, what would you what would you say is a big theme for this year? Bugs.
[Bryan Can trill] [25:25] Bugs. Yeah. Bugs are
[Adam Levinthal] [25:28] perfect. Was delighted. You know what was less of a theme that I anticipated was AI.
[Bryan Can trill] [25:34] AI was less of a theme. AI was less of a theme and I think the think it's because it's like less on the horizon and more like in the business now. You know what I mean? Like it's more like it's like kinda everywhere now. It feels so we did have a couple of AI episodes including the one on material the AI materials and fraud which I I I and I that was really delightful episode and conversation just because I feel that that fraud.
[Bryan Can trill] [26:04] I's like okay. Can we just actually maybe we should talk about this for a second? Jokes that we think our jokes mean, it's Ghoulish I laugh your own jokes, but that's never prevented Jokes that we thought are funny. Our own jokes, like, I'm sorry the Aiden Turner Rogers if I did it, that that killed me. I every time I really listened to that, it killed me.
[Bryan Can trill] [26:22] I just I thought the OJ Simpson, Aiden Turner Rogers mashup was I loved. Yeah. Did you have any that you Any
[Adam Levinthal] [26:35] any joke jokes of my own that I want to like relive?
[Bryan Can trill] [26:38] Yeah. Yeah. Exactly. But now is the time when we can weep in the know, we get to laugh at our own jokes right now.
[Adam Levinthal] [26:44] Yeah. You know what? I I I none really come to mind. I know that I know that you doubt that completely, but I don't think I retained them well enough. Yeah.
[Adam Levinthal] [26:54] I'll need to I'll need to think that one through. But I I I do like, when I am listening to our episodes, I am embarrassed by, like, sometimes needing to pull over and, like, titter at a joke that I told to myself five months ago. So at least I know my audience, which is
[Bryan Can trill] [27:06] Exactly. Exact exactly. So that's good stuff. Well, anyway, so the, so I, but we had a lot of episodes on debugging and a lot on bugs. I mean, just we did not have including some fascinating stuff.
[Bryan Can trill] [27:19] So I mean, that's like both LLMs picked up on this as a pretty big theme and both kind of properly taxonomized. It didn't hallucinate episodes, which is, you know, a nice thing about having all the the got only knows if it's getting it out of the GitHub repo or out of the out of Maybe the transcript. Speed or the transcripts. I'm I'm not so sure about the transcripts for reasons I'll get into in a second. I think the LLM may be studying on the train on this one.
[Bryan Can trill] [27:45] I don't think that like we've done a lot of deep work on the because the very, very good superficially and then things kind of fell apart. But properly kind of taxonomized all these episodes. And we had mean, I count we've got so into debugger driven development with Dave. And then we had really what five different gnarly bugs that we did an episode on each of those bugs. So when async attacks
[Adam Levinthal] [28:15] Actually, I think I have six. Yeah. Okay. You go. Okay.
[Bryan Can trill] [28:18] When async attacks, adventures and data corruption, future lock, our grown up CFS data corruption bug, death by uptime. Am I missing one?
[Adam Levinthal] [28:27] Hell is other networks?
[Bryan Can trill] [28:28] Hell is other networks. Of course.
[Adam Levinthal] [28:30] Because that
[Bryan Can trill] [28:30] I mean, that was absolutely. Yeah. Yeah. That and actually, that bug in many ways is like actually an even bet I mean, the thing I love about that bug is that is something we actually saw in the field.
[Adam Levinthal] [28:41] Yeah.
[Bryan Can trill] [28:43] Which I thought was great. So I yeah. No. We got a lot like really those are all great episodes. And actually, it's funny because we did so many of those that our colleague Laura has a great blog entry up last week.
[Bryan Can trill] [28:58] And on a bug that we had in the service processor in bringing up Cosmo. And there was like, it didn't quite get the traction on Hacker News that deserved, you know, next time I guess write a milk toast RFT as opposed to like really deep technical work, apparently. But I actually probably need to get that one in the second chance pull on Archer News. But there was one comment on Archer News which is like, oh yeah, you know, I love the podcast episode of this. And I'm like that we actually didn't do a podcast episode.
[Bryan Can trill] [29:28] This is actually a different I mean, I know it feels I know it feels like everybody How is that possible? And we probably should do a podcast episode of this, but you're actually thinking of the different SP walk even though think of death by uptime. But the I loved I was so great I think to have on each of those having the team on and being able to to to kind of and because each of those was a really gnarly problem. Like the I don't feel like any of those was a simple problem. And it was great to get people in their own words talking about it.
[Bryan Can trill] [30:01] So I love that. I mean, know what you're I mean, clearly, I know that you'd be you'd be right to love and call me right now because you're like, oh really? Oh, this is interesting. Oh, people like an episode that where we talk about an interesting punk that we debugged. Oh, I wonder if anyone had ever made that observation before.
[Bryan Can trill] [30:17] No? Oh, okay. Thanks.
[Adam Levinthal] [30:19] I know I mean, in the spirit of Festival and the airing of grievances, even though I know I've already aired these grievances, like, do you remember the I I I think I pasted into chat in during that episode all the all the DMs I had sent you wanting to do that episode. And they started to be like, hey. I really love that idea you had, Brian, to do an episode about this. I was trying to kind of
[Bryan Can trill] [30:44] intercept you. Yeah. Yeah. You're trying to accept me. It's like no.
[Bryan Can trill] [30:46] I like it. It was the end of the hey. Look. And one of those worked. We can't say which one.
[Bryan Can trill] [30:50] But but one of those worked. Yeah. No. That that was, and even the dog loved it. I mean, I think it was the those were so yes.
[Bryan Can trill] [30:59] Of course, we know the dog is like, I'm not saying I loved it. No. Sorry. I've got I'm saying I was here for
[Adam Levinthal] [31:05] it.
[Bryan Can trill] [31:05] Yeah. I had to listen for it. Exactly. Don't put barks in my mouth, please. But I thought they would we the other thing I love about this, I mean, is what you and I like I think love about these just in general too, is that when these systems fail, they will reveal themselves.
[Bryan Can trill] [31:21] And every one of these failures, which are actually pretty different, I mean, except death by uptime sounding a lot like the bug we described the plug entry even though it's totally different. But each of these is a kind of in a different aspect of the system. So I thought it was and there's a lot to learn from it. So I thought the anyway, I thought those were great. I just wish you had told me sooner that we should be talking about adventurous data corruption.
[Bryan Can trill] [31:43] If only is you had said it sooner or more frequently You know?
[Adam Levinthal] [31:46] That's on me. That's right. Right. There's only one person to blame. That's me.
[Adam Levinthal] [31:51] No. I love that there's a theme too. I mean, I just feel like, you know, I think sometimes we talk about, you know, junior engineers reading this, college I mean, listen to this and or college students listen to this. And I think that those are all such terrific episodes and such terrific learning experiences. Like, I learned from those episodes.
[Adam Levinthal] [32:11] You know, certainly, as we're debugging, no one person is the way I mean, maybe except Cliff last week. But, by and large, it's not just one person figuring it out. And, and a lot of great techniques, a lot of great sorts of, you know, guidance for just how to take incremental steps on those things. So I think those are always super fun.
[Bryan Can trill] [32:33] Totally. And Cliff would be the first to say that very much the baton was passed. There were a bunch of folks who've done a lot of work on that problem that allowed him to really take the kind of the next step on that. So no. I agree with you.
[Bryan Can trill] [32:42] Each one of those was a real team effort. Yeah. And it was so the, so I asked the I asked our LLM friends how 2025 contrasted to 2024. And the the presence of these episodes on debugging, has it drawing some big philosophical conclusions that I'm not like, I'm not sure. Like, it's ridiculous.
[Adam Levinthal] [33:05] Wow. You guys write garbage code now. Like, 2024, your code was tight.
[Bryan Can trill] [33:10] No. They both said that, like, you know, 20 the 2024 was about the philosophy of building systems. And 2025 was about the pathologies of those systems when they're built. This is about the the believe it was ChatGPT that called 2025 relative to 2024, quote, painfully concrete, unquote, which I'm like, again,
[Adam Levinthal] [33:34] I don't
[Bryan Can trill] [33:34] know if this is like Did you
[Adam Levinthal] [33:36] like, is it reviewing us on, like, Apple Podcasts? Because, like, no, thanks on that one.
[Bryan Can trill] [33:41] Yeah. I know painfully concrete is I feel like something mean, I feel like this is feedback I may have gotten more than once in my life. So the but I thought that was it. You then I kept thinking about it, maybe that does actually counterbrief. I mean, because we're talking about a couple of these things that we are that you only do get in a bit in a system that is a bit more mature or is in an is in the field.
[Bryan Can trill] [34:02] So I think there's some like slight accidental truth. I think we've been debugging really gnarly problems all along. And I think we've been talking about them somewhat all along, and I would in particular like I think that if one is interested also in the hardware side like to bring up episodes, all of them, and we had brought up Cosmo this year really get into all the nasty issues we see in bringing up a new board. The so I think we've been talking about it all along, I think it's also true that like, yeah, we actually definitely talked about more in 2025, and maybe it does reflect, know, he I and again, all the LM suggestions on this are, you know, they want, and would you like me to write a one sentence paragraph on each of these years and do you want me to do this? I mean, it's always like it always ends with this like, do you want me to take it much further kind of question to you?
[Bryan Can trill] [34:48] Do know what I mean? Like, do you want me to like, should I go tattoo this on my knuckles and, you know, strip it away and run through the streets? I'm like, no. No. No.
[Bryan Can trill] [34:55] None of that would be necessary right now. Thank you very much.
[Adam Levinthal] [34:58] You know, I think I am a victim of, like, the memory that ChatGeePeeTee has because I have told it to be terse so many times. Oh. And then I've I in fact, I've told it to be terse to the point where I am asking it for more information. Like, if I'm not asking it for more information, it's not being terse enough, that it now just gives me one word responses, like, very frequently. So I think I may have overfit
[Bryan Can trill] [35:25] that one. Maybe, maybe overshot
[Adam Levinthal] [35:26] the mark on that one.
[Bryan Can trill] [35:27] Yeah. They like, Chat Deep is like, look, frankly, I'm walking on eggshells with you. So I am trying to use the fewest words possible. I and I've got a bunch of ideas of things that I want to do, but I'm going to go save all them for Cantwell. He's he seems to love them.
[Bryan Can trill] [35:41] I'm like, which I don't. Don't want any of these, but you know, I
[Adam Levinthal] [35:44] I'm not going to tell you that. That's fine. Yeah. I get it.
[Bryan Can trill] [35:46] Yeah. So I so that that was a big theme. Mean, of course, it wasn't they weren't all debugging episodes, but there were more that were just about engineering at Oxide. I think we had more on and a fewer hot take. Right?
[Bryan Can trill] [35:59] I think which is, like, probably good. Right? I think.
[Adam Levinthal] [36:01] Yeah. I think I counted, like, eight or nine or 10, like, Oxide kinda like hanging with the oxide crew, what it's like to build this oxide, you know, bringing up something, you know, having Robert on, Dave on, talking about some of the kind of structure around how we build stuff.
[Bryan Can trill] [36:18] Yeah. That was I thought episode with Robert was great. Yeah. For sure. Really, really enjoyed that conversation with Robert.
[Bryan Can trill] [36:24] Also, can you talk about the AI work on that one? That was great AI work on the image.
[Adam Levinthal] [36:29] Yeah. So that that was like an AI assisted image. It was an image of Robert at a whiteboard drawing. The original image had, like, five other people in it that I thought were extraneous.
[Bryan Can trill] [36:42] Yeah. Just like we're actually gonna we're going to airbrush these people out of the're gonna,
[Adam Levinthal] [36:45] you know Exactly.
[Bryan Can trill] [36:46] Channel our inner Soviet. And it's like, yep. Nope. Not you. You're No.
[Bryan Can trill] [36:52] You're now. It was just
[Adam Levinthal] [36:53] Robert designing everything in a whiteboard by himself with no audience. No questions.
[Bryan Can trill] [36:59] And, I mean, admittedly, to be fair, it's like, these are actually people that were all, like, broadly so affiliated with the company. It was just like it's just like their legs or what. I mean, it's like it wasn't it wasn't flattering.
[Adam Levinthal] [37:08] It was just the framing. It was right. It was framing. Right.
[Bryan Can trill] [37:10] Yeah. So anyway, that that that was the that
[Adam Levinthal] [37:12] was a
[Bryan Can trill] [37:13] excellent image and I love that conversation. I thought that conversation was really great. I think that the mean, obviously, we're we all feel very, very lucky to work with all of our colleagues, but Robert's disposition was one that really I mean, it really was an an a great kind of one episode synopsis of our engineering ethos and approach. Really merits to relisted with it. That was very good.
[Adam Levinthal] [37:36] Yeah. Because someone mentioned it in chat, I guess they they they talk about you know, we talked about running into Dennis Ritchie trying to give a Trace demo. Apparently, we talked about it this season. But we
[Bryan Can trill] [37:48] I in fact, TTC episode. Right. Yes.
[Adam Levinthal] [37:51] But we had in fact told that story maybe two years previously. But so I, but I'm delighted that for somebody, it was a highlight of the season even if for somebody else, it might have been a highlight of a different season. And maybe we'll tell it again next year.
[Bryan Can trill] [38:05] You know, I think that people should take some solace in us retelling a story that we've already told because you'll find that the details tend to line up. You know?
[Adam Levinthal] [38:17] I mean I was going to say it really emulates the Brian and Adam, like, IRL experience as well.
[Bryan Can trill] [38:22] It does. What's really emulates I think, like, you're much better than this than I am. I mean, like and I so pride myself on like, I mean, I really try to pride myself. I live in fear, I should say, of just, like, end endlessly pity.
[Adam Levinthal] [38:34] What's the opposite of Oh, yes. Oh, it's private self.
[Bryan Can trill] [38:37] Right. Like, excuse me. I'll hold on a beat just being handed this. No. If the and I and then, of course, like, you read this in podcast, was like, oh my and like, it's like, it's the, you know, where were you when MCA died, which I think we've referred to like eight different times over the history of the podcast just like okay I need to wind that down.
[Bryan Can trill] [38:55] So these things I thought I hadn't repeated, but I was able to actually surprise you with things about me that you had not heard.
[Adam Levinthal] [39:02] Yes,
[Bryan Can trill] [39:02] true. Which I thought was in particular my own the first $5 I made as a software engineer, I have not heard that story. So beside that was good. But that was earlier in the year than when we were all at the Bowers game together as when we met up as a company. And I was telling a story that I was convinced you had never heard, and you literally identified it from a single syllable.
[Bryan Can trill] [39:34] You're like, wait a minute, I know this one.
[Adam Levinthal] [39:35] Is for You that too.
[Bryan Can trill] [39:36] Yeah. No. And I'm like, and I'm so that I'm not going to give people more context. That's only that's the only thing I'm gonna I'm going to tell people. But I so I I I am always worried that we're that we're repeating these things too much, but the Dennis Ritchie story, I'm glad that we have told that twice, apparently.
[Bryan Can trill] [39:54] Very good. So far. We'll get some other favourite moments. So this is Tyrone in the chat dropping in some other favourite moments. The other books in the bonfire.
[Bryan Can trill] [40:06] I love books in the box. Really love books in the box. I I I and I'm reading, and I believe a recommendation we got from books in the box. Know this is like an off I'd like off cycle books in the box, but the eccentric orbits the Iridium story that we got that was a recommendation we got in Books in the Box. And I'm really I'm loving that.
[Bryan Can trill] [40:28] It's very good. So I really love the Books
[Adam Levinthal] [40:31] in the
[Bryan Can trill] [40:31] Box episodes.
[Adam Levinthal] [40:32] Yes. I listened to actually the Neal Stephenson book Terminal Shuck. Started that, like, the kind of the day after and really enjoyed that. And it felt very much previous Neal Stephenson I'd read, and it felt very similar to, like, you know, experience from twenty years ago. But it's great.
[Bryan Can trill] [40:52] That yeah. That am I and do you recommend it? I need to go Yeah. I I I I I have to check it out. Yeah.
[Bryan Can trill] [40:57] Yeah. I have not read any Neal Stephenson. Am I in a safe space?
[Adam Levinthal] [41:01] No. No. I think I think you may have already answered
[Bryan Can trill] [41:05] that. Do I say that in every podcast episode? Yes. It's happening again. Are we going to get it like what's the chime we're going to ring when I for my early onset dementia?
[Bryan Can trill] [41:14] Are we going to have one for that?
[Adam Levinthal] [41:14] It's like It's your good night and good luck.
[Bryan Can trill] [41:17] It is. Goddamn it. Alright.
[Adam Levinthal] [41:20] Well, I trimmed in the sign-off just because I feel
[Bryan Can trill] [41:23] like it's a little repetitive. But A little repetitive. You said everything I've said. Look. I still haven't read any else.
[Bryan Can trill] [41:28] Know. I just I feel that that's like I feel that that's an aberration a little bit that I That's right. I was now the time to no this is not the time to mention this one mention anyway. You know I've been kind of fantasizing about a madman but for Fairchild Semiconductor. Someone needs to make that.
[Bryan Can trill] [41:47] And like I guess ring the early onset dementia chime because it's got nothing to do with anything we're talking about, but I wanted to get that out there, and now it's out there.
[Adam Levinthal] [41:55] To get it off your chest.
[Bryan Can trill] [41:56] I think it'd be amazing. Yeah. It'd be amazing. I'm in. I'm in.
[Bryan Can trill] [42:01] I think a period piece. Is it a Kickstarter? I'm I'm in. I'm in. Okay.
[Bryan Can trill] [42:05] It's a Kickstarter. It's a Kickstarter for a period piece about Fairchild. Super large demographic kind of show.
[Adam Levinthal] [42:11] So Speaking of poor segues, one of the things that I was hoping for this season that are are are predicted, no pun intended, was more about intel. And we had our predictions' episode where you made a great prediction about A great prediction. About Laputan. Amazing prediction.
[Bryan Can trill] [42:28] Well, no. My prediction was that the co CEOs would still be in place.
[Adam Levinthal] [42:31] No. If it was sort of but you talked a bunch about Lip By Tan.
[Bryan Can trill] [42:35] About Lip By. Yeah. Yeah. Yeah.
[Adam Levinthal] [42:36] Yeah. So and then Lip By Tan joined, and then we haven't had much to say since then.
[Bryan Can trill] [42:41] No. We should have
[Adam Levinthal] [42:43] I sort of thought there would be more to say. That's all.
[Bryan Can trill] [42:46] Yeah. Yeah. It's I'm I'm less surprised that there's not more to say. I wasn't I, you know, I who who knows what the future holds on.
[Adam Levinthal] [42:55] Yeah. Big highlight for me. John Holloway dropping the oxide bingo
[Bryan Can trill] [43:00] for those not familiar. Very good. Wait. Because I was just here. Feels like we've always had that, but that is actually that that yeah.
[Bryan Can trill] [43:06] Yeah.
[Adam Levinthal] [43:06] Oxide dot bingo. Amazing.
[Bryan Can trill] [43:11] Really amazing. That it'd been delightful. Yeah. And, you know, I think, you know, we've got I need to ask the the LLMs what they kind of think of the oxide bingo card. See what they've okay.
[Bryan Can trill] [43:27] Because this gets into the as I was like so they're kind of cutting these big themes of 2024 versus 2025. And I thought that was kind of interesting. And then I asked for some fan favourites. And this is one of things got a little started to get a little funky Where because and this is, you know, the shell game podcast gets into this. But the mean, the big challenge with these things still is they really struggle with like, I don't know.
[Bryan Can trill] [44:04] And they still like will go just absolutely bonkers if they feel that that's what you've asked them to do. And so like they're just happy to make up what they think are popular episodes. And they're like make up reactions, and it was, and you know, like some of it is like this like could I mean, this is like not an unreasonable thing. Like, yes, the death by uptime could be a favourite episode. We also only cut that two weeks ago.
[Bryan Can trill] [44:30] Is that like, this is what ChatGPT has convinced has become a touchstone episode as what one that people you know, as test of time and I mean it was it's like, okay. And ChatGPT Musically is like, well, I obviously don't have access to any of the view counts for this stuff. So it kind of acknowledges that I will ground this in observable audience signals that you do have. Repeat references, community chatter, longevity of discussion, and how often episodes become shorthand. EG, the async episode or the ZFS bug one etcetera.
[Bryan Can trill] [45:09] Which sounds like a great idea, but then it doesn't do any of that. Like all the mean, like, I don't know how has death by uptime become shorthand. It's our most recent episode. That doesn't make any sense.
[Adam Levinthal] [45:18] I this I mean, I feel like this intern has, like, started their internship very strong, but then kinda didn't really follow up.
[Bryan Can trill] [45:25] Then they kinda drifted off. Exactly. This is felt this is often happening with the LLM intern. What emerges says ChatGPT is that audiences favour favourites skewed heavily towards painful specificity and earned insight. It's like, okay, come on.
[Bryan Can trill] [45:42] Tone it down. The and I mean, then it kinda goes on like every episode like why it landed, and you know why it's a favourite. It's like you're just making all this stuff up. So the anyway, so then like things are beginning to drift. I go over to Gemini and ask it the same question.
[Bryan Can trill] [46:01] Gemini kind of interestingly is like, does not have any of the same reticence about going into view counts. Gemini is like, oh, YouTube's a property. I can actually go. Was kind of interesting. Right?
[Bryan Can trill] [46:12] It's like, I actually well, sorry. I actually do know all your view counts by the way. I also know your banking account balance by the way, I can kind of factor that in. And Yeah. So Gemini like our
[Adam Levinthal] [46:23] demographic breakdown, and it probably knows Yes.
[Bryan Can trill] [46:26] Exactly. Like, I know also it's like, I know exactly what kind of ad to put in front of you right now. By the way, a word from our sponsor. So it has what it calls the undisputed heavyweight. Gemini does.
[Bryan Can trill] [46:38] It's undisputed heavyweight. Of the has one that's just like, this one is got it's got the highest view counts of the year, which as far as I can tell is actually true.
[Adam Levinthal] [46:50] I'm going to guess it's system software in the large with data. Bingo. Bingo. That's it. Yeah.
[Bryan Can trill] [46:57] That was a great episode.
[Adam Levinthal] [46:59] Perfect episode, and I do know that the view counts were high. And, you know, the the the chatter such as it was, you know, was pretty good. So I think it was people took a lot away from that. And I I I do see it referenced from time to time.
[Bryan Can trill] [47:15] And, you know, as usual, like, Gemini, like, wrote one sentence too long on this. So it was like, you know, it bridged the gap between code and reality, the the the the, you know. And then its final sentence on this is, it resonated with every engineer who has ever had to push a scary update button. It's like, yeah, cut strike.
[Adam Levinthal] [47:33] Did not know. That one's not. Yeah.
[Bryan Can trill] [47:37] And then and then it kinda goes into and then again, it is kind of makes up the popularity of the others. I mean, it think. Right? I mean, it's like the they talk about scaling manufacturing. That's how it's made favourite.
[Bryan Can trill] [47:50] I'm like, I think it's a great episode. I'm not just like I mean, I would love to think that I don't know.
[Adam Levinthal] [47:56] Yeah. The home clappers who are trying to ramp up Sweep the scale. That's fair. Yeah.
[Bryan Can trill] [48:03] It does he do call out founder versus investor as the crossover hit. I did Sure. I'm exactly sure why not. Furthermore, I really do. I love that episode.
[Bryan Can trill] [48:13] I thought that was fun. And the also loved the fact that Liz's current startup has an LLM based on that one has kind of with one's own voice and expertise. And then we could actually go to that and people were during the episode going to the LLM that features Liz and Jerry as LLMs and like positing things about the episode, and then they were replying in kind. And it was like, it was pretty good. So pretty sassy.
[Bryan Can trill] [48:37] It's funny.
[Adam Levinthal] [48:38] So That was good. We haven't talked about I think the episode that was not the most popular, but, like, I think that we were most excited about, which was character limit.
[Bryan Can trill] [48:48] Oh, character limit is outstanding.
[Adam Levinthal] [48:51] Kate Conger and Ride Back On, I think we kind of we're both very excited about the book and really excited to have them on. And audio issues abounded as they do, But it was a really fun conversation with those guys.
[Bryan Can trill] [49:05] And biggest get your get the biggest get. I thought that was the that was a great get of the year. Yeah. I thought it would, that was, and it was a great conversation. I love that book.
[Bryan Can trill] [49:14] Yeah. I made the arguable mistake. Like I left my physical copy with my mom in Mexico. I'm like, mom, you have to read this. This is so outstanding.
[Bryan Can trill] [49:26] She hasn't. And now I'm kind of got the awkward thing of like, I want the book back. You're obviously not going to read it. So just like, again, anyway.
[Adam Levinthal] [49:32] Mean, that's a book I like I referenced last night. That's an it's something that I's
[Bryan Can trill] [49:37] very good.
[Adam Levinthal] [49:38] I talk about frequently that along with careless people. Careless people. Kinda hand in hand.
[Bryan Can trill] [49:44] And, you know, I also there's a there's a joke that we the term jog your memory about jokes that you have that we laugh at. Just they kind of the Tinker Bell character for the for Sarah Williams. Sarah Wynn Williams as a frequent guest.
[Adam Levinthal] [50:00] Like, I think you think I'm kidding, but, like, I do want to do that episode. Like, I want to have Sarah Wynn Williams in the in the office with us.
[Bryan Can trill] [50:09] In the office with us. Absolutely.
[Adam Levinthal] [50:11] Not saying anything per the court order or whatever. It's just us pretending to have heard something about it.
[Bryan Can trill] [50:19] I think it'd be great if, like, in addition to Meta issuing a restraining order against Sarah Williams, Sarah Williams issues a restraining order against us from using her as a'm not on I'm not on your podcast. I'm like, well, that's what we're just abiding by this restraining order.
[Adam Levinthal] [50:36] Wait. Wait. We know you were never on the podcast.
[Bryan Can trill] [50:39] No. Seriously, this is disturbed, and I like you're actually not abiding by the restraining order. So you need to stop, please. I, you know, I think that 2026 needs to be a year. Like, we have to get a c and d from someone.
[Bryan Can trill] [50:53] I just feel that, like, it's it is gets Stretch goal. It's a stretch goal. We just haven't arrived into it. We haven't got the lawyers involved yet.
[Adam Levinthal] [51:00] Clearly, Fox is not going to send it to us. Like
[Bryan Can trill] [51:03] We're not I we don't know how much harder we could be trying.
[Adam Levinthal] [51:06] The estate of Jean Paul Sartre is going to. Like, when are we going to get this letter?
[Bryan Can trill] [51:12] When are we gonna this letter? Come on. But that book is so, so, so good. I would love to also have her on if and when she can join us because I thought that was the the the book is obviously sending. No.
[Bryan Can trill] [51:26] I thought that that episode was great. I think, you know, another an episode that I am okay. What are episodes that you have sent to people, if any?
[Adam Levinthal] [51:35] I sent the one with Michael Littman, the AI in higher education.
[Bryan Can trill] [51:40] Oh, that one.
[Adam Levinthal] [51:41] Yeah. I sent like, I sent that one to my folks. I've sent that one to my both my technical and non-technical college friends. Furthermore, I think it's like Michael is so terrific. I thought he had such a thoughtful take on AI.
[Adam Levinthal] [51:57] And, you know, not to throw out my shoulder patting us on the back, but, you know, I was pleased that, you know, we came up with this way. There I thought this was a very good guest to have a better conversation about AI. I think we had had a lot of conversations about AI that were good, but I think this was an area where it's easy to be simplistic and reductive. I think Michael had had a had such a thoughtful, considerate conversation with him. Furthermore, I really enjoyed that.
[Bryan Can trill] [52:26] I really enjoyed that too. And I also sent that to I sent that to my 18-year-old, my college freshman to get his perspective on it. Because this is something that everybody is grappling with, and it's a really important subject especially in higher ed and I thought Michael was great. I thought it was really it was that was a terrific conversation. Another great get for you by the way.
[Bryan Can trill] [52:46] Oh, thank you. We are keeping And you're I and I know that this is all about getting to be getting Morris next year and I trust me, I am feeling the heat. I am feeling the heat because he
[Adam Levinthal] [52:57] is Good. Especially if I get Evan, forget about it. You're like way behind.
[Bryan Can trill] [53:00] Even Evan, I get yeah. I'm still going to be like, wait a minute, that guy I played ultimate with that guy. I don't know. Furthermore, I'm like, no, no no, no. Furthermore, I didn't play ultimate with you.
[Bryan Can trill] [53:07] You can come. It's fine. The that was a that was a really great conversation. And I so I sent I have definitely sent that one. And then another one that I've actually sent a decent amount is and I know it's off our demographic, but diving in with Robert Bogart.
[Bryan Can trill] [53:24] And the I've I've had a decent number of parents of athletes reach out to me after my blog post about college baseball, venture capital, and the long, maybe. And that and then that listening to that episode as well. Yeah. So I was really grateful for Robert for joining us. And again, I know it's I know it's a little bit I we but we have to take you off the beaten trail a couple of times.
[Bryan Can trill] [53:49] You know, I feel like I I I just don't bother me that like we're going to have things that are that that people aren't necessarily expecting from us.
[Adam Levinthal] [53:55] That's right. I mean, we did have, like, a 100% fewer baseball episodes this season.
[Bryan Can trill] [54:00] Yes. I mean, if you're calling I mean, but we had we also had a million percent or more. I'm not sure what you're coming up from zero, but what on NCAA swimming. Right? I just thought so I'm not sure.
[Bryan Can trill] [54:08] Like I mean sure. I mean, they'll like you know, out of the frying pan into the fire. Yes.
[Adam Levinthal] [54:13] That's fair enough.
[Bryan Can trill] [54:14] But I thought that was another great one. And so that one I I I've sent to a bunch. And I of course, we also end up as you can imagine, sending episodes to folks that are contemplating becoming Oxide customers or becoming Oxide want to apply to Oxide. So it's been a great factor for that. And I've sent a bunch of them out for that.
[Bryan Can trill] [54:32] But those are episodes that I've sent to more personal folks.
[Adam Levinthal] [54:35] So Yeah. Yeah. Yeah. Same. But that but kudos to you for bumping the listen count for everyone applying to Oxide being sent a bunch of podcast episodes to listen to.
[Adam Levinthal] [54:45] Yeah. Exactly. Good strategy.
[Bryan Can trill] [54:47] Yeah. You have to gain this somehow, and you might as well do it with applicants. So, you know, you have to go actually would be curious to go because, you know, we do point every oxide applicant to our conversation with Gergay Ores. Yeah. Yeah.
[Bryan Can trill] [55:03] From from from 2024. From 2024. Is that what that was? 2024. Okay.
[Bryan Can trill] [55:08] Yeah. God. They's all I that one should have much higher view counts. Listen counts. If it but I'm not convinced it does because I'm we definitely get plenty like, if you're going to apply to Oxide, please do listen to this thing by the way because it's like, it does have there 's's a bunch of stuff in there that is helpful and germane.
[Adam Levinthal] [55:26] That was 2023. Jeez. I'm That's what I thought. Yeah. Know it's late twenty-twenty three.
[Adam Levinthal] [55:31] Know
[Bryan Can trill] [55:31] you're Yeah. That makes sense. No. I know it was late because it was like dark and cold in the office. Late in terms of like late in the year in the winter.
[Bryan Can trill] [55:39] But yeah, that's it. So but that does that one have higher view counts? I mean, are you on the transistor looking at the transistor dashboard there?
[Adam Levinthal] [55:46] I'm not. I should what am I doing here? Why am I
[Bryan Can trill] [55:49] the way, looking at transistor, as long as we're looking at transistor, we got, you know, we get country downloads and, you know, we I'd be interesting to know how we're doing. I think, you know, last year we called out like our downloads in Namibia. We've got, you know, 20 downloads in Namibia this year. So not sure where that that kind of accounts. We do sell some countries with zero downloads.
[Bryan Can trill] [56:11] Several which are war torn. What about just like Papua New Guinea? I feel like Papua New Guinea. If you're is you're in Port Moresby, I feel that you can listen to Ox Head Friends. Like Papua New Guinea, I think you can just, like, up it a little bit.
[Bryan Can trill] [56:21] I feel like you know?
[Adam Levinthal] [56:22] Yeah. Just grab the baseball episode and send it to your buddy in Papua New Guinea, we'd really
[Bryan Can trill] [56:26] You know what? I will. I think Port Mores Beacon really I think it will that'll that'll resonate with them.
[Adam Levinthal] [56:31] So the Gurgle episode hiring process is top six. Top six.
[Bryan Can trill] [56:35] Okay. Of all time. Of
[Adam Levinthal] [56:37] all time. Sense.
[Bryan Can trill] [56:38] Yeah. That does make sense. So that one that stat you can definitely view as gamed because we are asking people. That's that is that's wild. What are some of the others in they are there any this year that are in the top episodes of all time?
[Adam Levinthal] [56:53] Okay. So the stats are a little Specious. Funky. So the reason the stats are funky on Transistor in particular is and the reason why the while the United States is our the most common country that has downloaded it, the most common state?
[Bryan Can trill] [57:12] Arizona, baby.
[Adam Levinthal] [57:14] Arizona, where in somebody's basement, they were, like, downloading the most recent 10 episodes over and over again for a year and a half, and then it stopped. So thanks for not downloading them anymore, but it means that our twenty-twenty five stats are not like, we have fewer downloads because that computer in Arizona has been turned off.
[Bryan Can trill] [57:36] Yeah. Okay. So then when you're what are you looking at for are you looking at all time? Or are you looking at for the okay. Not for the first yeah.
[Bryan Can trill] [57:44] Interesting.
[Adam Levinthal] [57:45] Yeah. So Yeah. If I look all time actually, our predictions' episode this year was our most popular episode this year. And then after that was the one with Robert, Holistic and Shearing.
[Bryan Can trill] [57:56] Yeah. That's great. Yeah. Nice. Well, good stuff.
[Bryan Can trill] [58:00] I the and I guess all time I think that's funny that our second all-time least one I'm looking at is crucible. Yeah. Though they whether you promised that Alan can come join us because don't worry, no one will listen to it. It's like actually everyone will listen to it as it turns out. That's right.
[Bryan Can trill] [58:17] And good to see the r f d episode right up. I love that was that's a that was a great conversation.
[Adam Levinthal] [58:22] Yes. Yes.
[Bryan Can trill] [58:23] So I'm really glad to see that one up there. Yes. Yes. Some some some good stuff. The alright.
[Bryan Can trill] [58:29] So the that that was a great episode. Are there others that we before we get off of this because the it's another thing, the theme I want to hit.
[Adam Levinthal] [58:39] Yeah. Those were the episodes that I had called out in particular.
[Bryan Can trill] [58:42] Yeah. So okay. So then I with the fan favourites, you can feel the LLMs wobbling a little bit. Like they're beginning to move into bullshit. And this is just like, okay, this is not And then I asked it for well, in part because I actually was genuinely curious about what it would find.
[Bryan Can trill] [59:05] I say, my prompt being the podcast infamously makes Gen X references. Were there some notable ones this year? And this is where all LLMs just went straight into the wilderness and lost their confidently with absolute confidence completely lost their mind and just started absolutely making up shit and making up references to, oh, like, yeah, the make up they make a bunch of office space references, which I think we basically don't make. Like, maybe. Maybe a little bit.
[Bryan Can trill] [59:41] No. I mean, the only I mean, I feel like I the office space reference that I make, I would say the most frequently is like a Michael Bolton m dash mashup of like, you know, that
[Adam Levinthal] [59:54] Yeah. Right. Right. Right. Right.
[Adam Levinthal] [59:56] He's the one who's going to change his name because A 100%. He's one who sucks. Yeah.
[Bryan Can trill] [01:00:00] That's right. That's right. And so I'd like that I feel as but okay. Don't think I made that here, but I don't know then again. So like no.
[Bryan Can trill] [01:00:07] Then it says like they make references like we definitely No. 100% don't. Bugs Bunny Don't know. Like that going could go either way. That goes one way, one way only goes straight there.
[Bryan Can trill] [01:00:20] There will be no references on this podcast. And if that quip makes it into the recording, I'll be amazed because that's how cancelled as far as we're concerned. Like that is a zero percenter. We are not making references. And then it's it just went it's like, they make Nirvana references and grunge era references.
[Bryan Can trill] [01:00:39] And they started like these are the ones that they made a Nirvana reference in. It's like I mean, it was just I mean, absolutely unhinged. At one point, ChatGPT says when summarizing all of this up, it says this isn't nostalgia, it's epistemology. I mean, that's got to be the most LLM thing ever generated.
[Adam Levinthal] [01:01:13] Oh my god. That's crazy.
[Bryan Can trill] [01:01:15] I mean, I I I just don't know the cognitive dissonance that you would have to make. I mean, hopefully, that doesn't sound like me. I mean, my god. And then it's like, they're they're making like they think we make a bunch of talking heads references. I don't
[Adam Levinthal] [01:01:33] know that I would confidently even know how
[Bryan Can trill] [01:01:36] to do that. I don't know. Furthermore, I would I if you ordered me if you if you put a bayonet in my ribs and ordered me to make a day a talking head reference, talking head reference, I don't even know, like, how I would start on that.
[Adam Levinthal] [01:01:47] I mean, I like I did see David Byrne live talking to Dave Eggers.
[Bryan Can trill] [01:01:53] Stabbing the ribs. Nope. Not good enough. I mean, it's just like, sorry. We're not asking for facts about talking heads.
[Bryan Can trill] [01:01:59] I want you to make a talking heads reference. I'd like
[Adam Levinthal] [01:02:01] Okay. I will say that I he did get on stage and do they had a karaoke machine from Japan that had Talking Heads with, like, the lyrics messed up, and he was just going along with it. So that was fairly delightful.
[Bryan Can trill] [01:02:16] Okay. That counts. That you know, we wanna Good. That's what over the track of bandits of your most ever track of bandits. My ribs are going to get it, though.
[Bryan Can trill] [01:02:25] I think that that is so and then they and then they actually this is kind of and this is where you do wonder about the power of these things to kind of induce a sense of dementia where they're like, oh, then they make War Games references. I'm like, okay, maybe. We might. We might go on. Expand.
[Bryan Can trill] [01:02:45] A big topic of me.
[Adam Levinthal] [01:02:46] Did we talk about Dave Hits this season? Okay. That's good.
[Bryan Can trill] [01:02:49] I think it was last season, wasn't it? I think that was
[Adam Levinthal] [01:02:52] Yeah. Good. Yeah. And so it was his last season. They said Dave had said had come up in as another source of cease and desist.
[Adam Levinthal] [01:03:02] Yes.
[Bryan Can trill] [01:03:04] That's right. That's right. And then and then it is calls out the meta Gen X humour of weaponized weariness. Perhaps the most on brand Gen X reference of 2025 wasn't a specific artifact, but a tone. Dry fatalism.
[Bryan Can trill] [01:03:19] Humour without hope washing. Laughing at complexity. Not away from it. It's like, what where are we? We're just we're just making shit up at this point.
[Adam Levinthal] [01:03:28] That one feels more personal to me. I mean I am exhausted, but yes.
[Bryan Can trill] [01:03:32] But you can't know that. No. We can't know that. We, sorry. Yes.
[Bryan Can trill] [01:03:37] Yes. But we don't know that's not what we're doing here. We're not I don't think that drive fatalism here like no. I mean No. I thought that's a lucky guess.
[Bryan Can trill] [01:03:44] That that's not I mean, it's just a lucky guess. And that's got nothing to do with the actual podcast. Yeah. And then I asked it for of like, no. Okay.
[Bryan Can trill] [01:03:54] I want the Gen X reference in the content itself. So do want to actually, This is I was just kind of curious to see if they would pull it. But one of my, I have to say favourite moments was when we had Oliver had joined us on the stage. MMM.
[Adam Levinthal] [01:04:10] And the Books in the Box episode.
[Bryan Can trill] [01:04:12] Books in the Box episode. And start he like is comp either we're making a Knight Rider reference, and he's rolling with it or maybe he even he made a Knight Rider reference. Whatever it was, he was rolling with Knight Rider. And I'm like, doesn't add up. I don't add up like that does not make sense because I know for sure that thing did not leap the generational chasm to the contrary, Kit is lying at the bottom of a ravine.
[Bryan Can trill] [01:04:39] The like it absolutely did not. And so I pushed on like, how do you know about Night Rocks? I know that Oliver's just like not of not an excerpt, not of the vintage. And I'm like, there's got to be something. And then he revealed that like actually it was they were they referenced in the SpongeBob movie.
[Bryan Can trill] [01:04:57] I just felt like that was a moment of just like a maximum triumph for me. That was my that was my biggest triumph
[Adam Levinthal] [01:05:02] of the year. Okay. Good. Good. Good.
[Adam Levinthal] [01:05:05] Good to hang your head on that one.
[Bryan Can trill] [01:05:06] I just felt like I called it. I knew it. I knew that. So I wanted to see if it would actually pull that out, which is just like a ridiculous hope because like obviously it's like it's good, but it's not an actual like magician. And so it Is asked it for like explicit like what about Gen X references in the content itself and it just I get it's just off into the absolute weeds and more just like and like so it's like saying, oh, like the episode in which it referenced was system software in the large and shoot out at the CNCF corral.
[Bryan Can trill] [01:05:43] And then it's got like quotes from that are references that we didn't make. It's like, wow. That is okay. Yeah. That is so my Gemini, you're ChatGPT just, just lit itself on fire.
[Bryan Can trill] [01:05:57] So you're up, pal. Are you going to do any
[Adam Levinthal] [01:06:01] I'm amazed you didn't just make a Top Gun reference? I felt like I felt like I saw that one coming.
[Bryan Can trill] [01:06:07] That I didn't make a Top Gun reference right now?
[Adam Levinthal] [01:06:09] Right now. Right this moment.
[Bryan Can trill] [01:06:11] Right now. Did that you know, I that I should have. That cougar was number one, lost his edge turned in his wings. Now you're number one? Yeah.
[Bryan Can trill] [01:06:18] You know I should have. Gemini. Gemini? I can't believe I have to do this Gemini. I have to send you to Miramar.
[Bryan Can trill] [01:06:27] Thank you. Good luck. That's right. Alright. That was good.
[Bryan Can trill] [01:06:31] Thank you. Thank you for the prompt on that one. Ain't going to lose my edge maybe a little bit. Yeah. Does feel like a bit of a layup for myself as long as we're on Gen X references.
[Bryan Can trill] [01:06:38] You think that like you know all those synapses would be hot, but I guess not. Okay. No, that's a great reference. The so I asked Gemini the same thing and this got a little bit like weirder and a little more like both more accurate and less accurate. So first, it's like, well, first, you've got to talk about the Fox reality TV throwback in when async attacks, a clear reference to when animals attack, which I guess it kind of is.
[Bryan Can trill] [01:07:06] MMM. Yeah. But it's like not an explicit homage.
[Adam Levinthal] [01:07:10] No. Yeah. I mean, I yeah. Not an explicit homage. Think like riffing on a theme.
[Adam Levinthal] [01:07:17] I think
[Bryan Can trill] [01:07:17] we would also, like, we would make an if we're going to make an explicit homage, it would be to man versus beast. Did you ever watch any of those?
[Adam Levinthal] [01:07:24] This is like Kobe Cash or like Joey Chestnut versus a bear.
[Bryan Can trill] [01:07:29] Yeah. Yes. Did you watch those? They are so good.
[Adam Levinthal] [01:07:34] It's like it's like an Olympic sprinter, like Usain Bolt versus a zombie horse or something.
[Bryan Can trill] [01:07:39] A zebra. A zebra. Zebra. Yeah. I just felt like that was extremely educational about the about I mean, I think that and, I mean, you know, I'd also like to say for my own children, you know what has cast a long shadow is wildcats.
[Bryan Can trill] [01:07:51] Do you guys watch wildcats Yes. On PBS? That thing is like super informative, hits kids at an age when they're impressionable, and they watch a lot of it. So there's an entire generation like drifting around with some super weird like animal knowledge about like, you know, a loris or whatever or, you know
[Adam Levinthal] [01:08:12] Astronauts two. Astronauts two embeds a lot of like esoteric marine knowledge.
[Bryan Can trill] [01:08:18] That is great. You know, and I look forward to these gen z podcasters of the future, like casually dropping wildcats references, and I'm gonna I'm going to roll with that is is is what I want to say. So the anyway, man versus beast. And then also the orangutan versus the sumo wrestler. It's super educational.
[Bryan Can trill] [01:08:36] Like it just like the orangutan is like much smaller. It looks I mean, lighter, and it like effortlessly defeats the sumo wrestler in a tug of war. I mean, is effortless. You do not want to mess with the chimpanzee. I mean, our orangutan rather.
[Bryan Can trill] [01:08:50] Anyway, deep thoughts. Man versus beasts worth checking out. It is turns out like we are slower, and then we are slower than absolutely everything, but also smarter than absolutely everything. And as it turns out like that's a that's a big difference. Did you know that that humans are the only animal that use wind direction to hunt?
[Adam Levinthal] [01:09:10] I did not know that.
[Bryan Can trill] [01:09:11] Isn't it amazing?
[Adam Levinthal] [01:09:12] It is amazing.
[Bryan Can trill] [01:09:14] How you've learned? You're like, where are we right now? Are we on they are you just like stop generating? Are we on, a just like, are you on a chat to But
[Adam Levinthal] [01:09:21] are you
[Bryan Can trill] [01:09:21] still You're still reading the transcript? You're still reading the transcript. Where are you? This is still Gemini. Is Gemini.
[Bryan Can trill] [01:09:29] Is like, oh my god. That's actually you. Okay. Jesus. Like,
[Adam Levinthal] [01:09:32] I've I've told it to be as terse as possible. You're like, just go.
[Bryan Can trill] [01:09:35] Just go.
[Adam Levinthal] [01:09:36] Like, just
[Bryan Can trill] [01:09:36] Just go. Rip.
[Adam Levinthal] [01:09:37] Just whatever's on your mind.
[Bryan Can trill] [01:09:39] Whatever is Just let it rip.
[Adam Levinthal] [01:09:41] Just let it rip. Absolutely. So
[Bryan Can trill] [01:09:44] alright. So then so that is like a kind of barely holding on, and then it just gets like super weird. The Fischer knot. I'm not even sure if that's a reference. Oh, we think we're making a reference to seven with Brad Pitt.
[Adam Levinthal] [01:10:01] Oh, I don't think I'd make a ref a seven reference like in public.
[Bryan Can trill] [01:10:07] I I I definitely I just think that would be a very weird reference to make. And then like, so okay. Let's actually go into like, what about the content itself? And again, it just actually it kind of like with more specificity, but absolutely wrong goes through all the references we made to Logan's Run again with quote to Space balls again with quotes to The Princess Bride again with quotes to Glengarry Glen Ross, to Clark's, to Spinal Tap, and all just like making up quotes. And like, wow.
[Bryan Can trill] [01:10:41] Okay. So Yeah. I feel
[Adam Levinthal] [01:10:43] like we're insufficiently like culture and literary, and we should drop more references to these important works.
[Bryan Can trill] [01:10:49] No. I actually don't feel we should no. I feel that the the know. Furthermore, I feel that we drop I know because I think that, like, we do drop references that travel less than these.
[Adam Levinthal] [01:11:00] That's definitely true.
[Bryan Can trill] [01:11:02] Which is like I mean arguably undermines the point because it's like well okay then people will get it. They just think it's like they should be ringing their onset dementia chime. They actually don't think that this is don't realize that you're making a reference to something. I do like it when you and I make a reference to only our shared history that no one can possibly know, which we do try to explain, but we don't always do that.
[Adam Levinthal] [01:11:20] Probably fail. Yeah.
[Bryan Can trill] [01:11:22] I mean, I feel like we would make a casual reference to Adam Lecithal hardware engineer and not people would just like A lot.
[Adam Levinthal] [01:11:27] I think a lot. I think Do
[Bryan Can trill] [01:11:29] think we do that a lot? Do we get
[Adam Levinthal] [01:11:30] that actually? I think in my life, I I I mean, in my life at Oxide, I do hear about Adam Elemental hardware engineer, which is even more awkward since we work with a lot of hardware engineers who definitely don't necessarily get the joke. Yeah. That's right. We
[Bryan Can trill] [01:11:43] work Joke is doing a lot of work on
[Adam Levinthal] [01:11:44] that one. I'm not sure,
[Bryan Can trill] [01:11:45] but yeah.
[Adam Levinthal] [01:11:45] Also, a fair amount of discussion about Adam Levinthal, tax expert or Tax adviser? Adam Levinthal.
[Bryan Can trill] [01:11:56] Absolutely. Yeah. Absolutely. No. I mean, Adam Levinthal mob accountant.
[Bryan Can trill] [01:12:00] I mean, I feel like there's That's right. Yeah. I wear many hats here. Yeah. Many
[Adam Levinthal] [01:12:05] hats. Absolutely. Talented many hats.
[Bryan Can trill] [01:12:07] Yes. Yes. Yes. I mean, that's kind of what you're getting here at a limp all esquire. You're getting a Yeah.
[Bryan Can trill] [01:12:15] So at that point, I'm like, okay, these guys are just kinda off the. So I think they kinda lost they but it was interesting. Like, the cultural resonance does not actually they have a harder time on the cultural resonance. Makes sense. Yeah.
[Bryan Can trill] [01:12:29] Makes sense. Alright. What were some other oh, I also loved our the the the Richard Carry conversation. Dana's gorilla finally making a cameo Yeah.
[Adam Levinthal] [01:12:42] With this Matthew. This Yeah. Yeah. Talking about, you know, all all all the folks in busy town making oxide work. Yeah.
[Adam Levinthal] [01:12:50] That that was one of my favourite images as well even though I mean, especially because it took no work.
[Bryan Can trill] [01:12:53] But I the best kind. But, I mean Even the abstract. Yeah. Well, he also just raised it like busy town. It's like if is busy town resonates with you, like, you know, you're you're our people.
[Bryan Can trill] [01:13:04] I just think that there's something great about busy town. Yes. Everyone's everyone so I thought that was very great. Oh, the other thing is the that Gemini identified is like, and then they did an April fool's joke with rating the mining bar. I'm like, what?
[Adam Levinthal] [01:13:21] No. Okay. That episode was in March, first.
[Bryan Can trill] [01:13:25] Seconds. Right. I think it was actually it was in March. You're right. It was recorded in March.
[Bryan Can trill] [01:13:30] It was released on April 1. So I think Oh,
[Adam Levinthal] [01:13:31] was it? Oh, okay. Yeah. Yeah. Just took me a while to edit.
[Adam Levinthal] [01:13:34] Alright. Well, jokes
[Bryan Can trill] [01:13:34] are good. Exactly. But it's also, like, not it's like, it's a great episode, but it's not there's nothing deadly serious that episode. So there's no April Fools' Day about that one.
[Adam Levinthal] [01:13:45] There's no laughing matter. No.
[Bryan Can trill] [01:13:48] And then I also it should be oh, we also had our first, what do you call a podcast that is about an entity that is unnamed? Do you know what I mean? Like, it's a subtweet, but it's a podcast.
[Adam Levinthal] [01:14:02] That's funny. You know, as I was categorizing the episodes, I was also reflecting on this subtweet of an episode that was very important to you.
[Bryan Can trill] [01:14:14] It is very important. So this is transparency in hardware software interfaces.
[Adam Levinthal] [01:14:17] Yes. Yes.
[Bryan Can trill] [01:14:18] Which is on the one hand about every hardware vendor, and on the other and the other in another more specific way about exactly one. Yes. And, know, dear, you know, dear listeners, if you think, you know, if you think it's you, you're probably right. So
[Adam Levinthal] [01:14:34] And have you written an RFD on that subject as well? Am I remembering this correctly? Okay.
[Bryan Can trill] [01:14:38] Yeah. I've written an RFD
[Adam Levinthal] [01:14:39] on it. So you had the long form subtweet and then the
[Bryan Can trill] [01:14:43] And then the audio subtweet.
[Adam Levinthal] [01:14:44] Yeah. Exactly.
[Bryan Can trill] [01:14:46] And I'm not sure what we call that. I mean, is there another there's going to be another name for, like, a kind of cultural subtweet.
[Adam Levinthal] [01:14:54] That's right. Like, it would be like Twitter cannot have invented the subtweet. Sure.
[Bryan Can trill] [01:14:59] That's a good question. Like, yeah, you feel
[Adam Levinthal] [01:15:01] like Alexander Hamilton, like, subtweeted fucking everybody?
[Bryan Can trill] [01:15:04] Yes. I do. That our first blogger too, feel on that guy. That guy, he invented so much, Alexander Hamilton. You know, I remember reading I think I was with you when I was reading Cher no's Hamilton before the musical.
[Bryan Can trill] [01:15:18] Could you do you remember why I was doing this?
[Adam Levinthal] [01:15:23] It has to do with, like, eliminating the $10 bill. I mean, the the like, removing Hamilton from the $10 bill.
[Bryan Can trill] [01:15:28] That's an excellent guess. No. That happened afterwards. No. Was because I were contemplating naming Alexander, and I just wanted to do, like, a quick, so I read a bio of Alexander Hamilton.
[Adam Levinthal] [01:15:42] Let me do a quick 700-page read to make sure there's
[Bryan Can trill] [01:15:44] nothing in fairness. Just like, I mean, you're not going to name a kid Adolf. You wanna just like make sure let me just like I want to go in eyes open. You know what I'm saying? Like it feels like you know, I'm saying this all out.
[Bryan Can trill] [01:15:57] It's pretty peculiar. I love it. I like imagine you slamming
[Adam Levinthal] [01:16:02] the book shut and saying Bridget, we're going with it, you know.
[Bryan Can trill] [01:16:05] We're coming with it off. Let me tell you. I read about the Whiskey Rebellion, and I don't know. This Adolf character just can't be as bad as this guy's.
[Adam Levinthal] [01:16:13] No. This affair that he had, I just can't, I just think we're back to our place.
[Bryan Can trill] [01:16:19] I just think we're we can't god. I know the well so okay. The appearance is great, but I also do love the mean, you know, what he because what he said about Aaron Burr is still kind of like not known, but people kinda like historians basically think like he had it coming. Like what he said was really like he knew what he said, and it was terrible. I think that they they they believe that you know, Aaron Burr lived with his daughter Theodore.
[Bryan Can trill] [01:16:46] Yes. Yes. And Alexander Hamilton was I think pretty explicit about his idea that that that they may have been that there may be something untoward in their relationship. Yeah. Which it's like, hey, you got a hand to that guy, know.
[Bryan Can trill] [01:16:59] You know, real taser tongue. But no, so I that's why I was reading Alexander. No. And I came then I also read a bio on Alexander the Great. Alexander of Mastodon.
[Bryan Can trill] [01:17:10] Of I thought it just said Alexander of Mastodon, which is why I had Right. Which was right. It's got to be now we
[Adam Levinthal] [01:17:17] gotta check if that guy's been cancer.
[Bryan Can trill] [01:17:19] Yes. Right. Exactly. That that's Alexander the upset. That's that's a that's a different okay, Mastodon, settle down.
[Bryan Can trill] [01:17:26] I know Mastodon gets super upset when we say that they're upset. So the're fine and
[Adam Levinthal] [01:17:32] you have a great sense of humour.
[Bryan Can trill] [01:17:33] Yeah. You've got a great sense of humour. I do. Okay. On my LLM piece, mass this was kind of only on Mastodon.
[Bryan Can trill] [01:17:41] One of the things that the RFT opens with LLMs have been in this it has been indisputably one of the breakthroughs of the last five years. And people are like, that's not true. Like, you can come on. You cannot say an LL Web is not a breakthrough.
[Adam Levinthal] [01:17:54] It's a breakthrough. In Mastodon, people are saying
[Bryan Can trill] [01:17:57] MMM. Not a breakthrough.
[Adam Levinthal] [01:17:58] In in in the flavour of this actually, is it that it happened?
[Bryan Can trill] [01:18:03] In our chat as well. People are like, alright. You want people to say it? I'll say it right now. It's not a breakthrough.
[Bryan Can trill] [01:18:07] Okay. Well, I'm going to say the I'm going to say it is a breakthrough. It is you can disagree with everything about it, but it is a breakthrough.
[Adam Levinthal] [01:18:12] Was it that it happened not within the last five years, or was it that it was not a breakthrough at all?
[Bryan Can trill] [01:18:19] Not a breakthrough. Not a breakthrough at all. Mike, yeah, I just can't, I mean, come on. You's a breakthrough. You can disagree with everything about it, but it's an it's breakthrough.
[Bryan Can trill] [01:18:28] But the and Alexander the Great was also you know fascinating. I'm not sure if you know we should really be naming children after Alexander the greater Alexander of not Macedon of Macedon. But the doc you know he died incredible at an incredible young age like in his early thirties of cholera. Isn't it amazing?
[Adam Levinthal] [01:18:49] Anyway. It is amazing.
[Bryan Can trill] [01:18:52] I I I would name the kid Alexander. So there you go. You know, it all. Anyway, I'm not sure. Fuck exactly.
[Bryan Can trill] [01:19:01] Not really sure what the outcome was, but and highly recommend Cher no. You read Cher no's biography. Yes. Yes. Very, very good.
[Bryan Can trill] [01:19:11] And he feel yeah.
[Adam Levinthal] [01:19:12] And I remember you were going to see Hamilton, and I think I told you, like, the the the musical. And I think I told you, be prepared for the greatest thing you've ever seen in your entire life, and I'm in no danger of overselling.
[Bryan Can trill] [01:19:24] Yeah. You did not oversell. It was amazing. You did not oversell. It really was outstanding.
[Bryan Can trill] [01:19:28] It was very good. No. I'm the and Cher no's biography is so good. The one of the things I remember from Cher no's biography is reading about something like the Whiskey Rebellion, which I absolutely agree with the way Hamilton handled the Whiskey Rebellion by the way. But reading about something like that where he dedicated kind of three pages to it and thinking to myself, this person Alexander Hamilton is so fascinating I should read a biography of him.
[Bryan Can trill] [01:19:53] And my other part of my brain is like, Jackass you are reading about this is like a know, whatever it is, a 900-page biography of him. Like, this is not, but that's how kind of fascinating his life is. Yeah. So Yeah. You know, come for the year wrap up.
[Bryan Can trill] [01:20:06] Stay for the free book in the box, I guess. Oh, also a half century Silicon Valley with with with the Randy shop. That was great.
[Adam Levinthal] [01:20:14] That was fun. That and that that inspired me to read a book about Xerox, Fumbling the Future.
[Bryan Can trill] [01:20:21] Fumbling the Future. Yeah.
[Adam Levinthal] [01:20:23] Which I know is like dumped on your desk or whatever.
[Bryan Can trill] [01:20:25] No. And I need to read that because that that is really, and I thought that that aside from the fact that that had a built-in image for you. So Yeah. That part is Perfect. Right.
[Bryan Can trill] [01:20:37] That I thought that was an amazing conversation.
[Adam Levinthal] [01:20:40] Really fun. And actually, you know, when I when we went down to the computer history museum more recently, I was thinking about that episode because I think it put a lot of that stuff in context for me, like a lot of the Xerox PARC work and just like the stuff that of that era.
[Bryan Can trill] [01:20:55] So you know what I liked about that episode? And I may be the only one that, but I think an important point that we made in that episode is that this was this kind of extraordinary time we're talking about how lucky Randy's dad was and then also reflecting on the fact that that time like more broadly was kind of a terrible time like 1970. 1973 was bad in a lot of ways. And I just think it was a good reminder that like, that you can find there's a golden age happening right now somewhere. And probably many golden ages happening.
[Adam Levinthal] [01:21:30] Yeah. So if you happen to be listening to this at a shitty time.
[Bryan Can trill] [01:21:34] Yeah. Exactly. No. I'm serious. That, like, that you could that you that you should not be overwhelmed with the despair and find the interesting bits because there are interesting bits that are out there.
[Bryan Can trill] [01:21:45] I thought that was Sure. That was perfect. Alright. I think it would
[Adam Levinthal] [01:21:49] be I think it would be remiss if we didn't talk about the big oxide milestones of which raising a $100,000,000 this year was pretty big deal.
[Bryan Can trill] [01:21:57] That's pretty big. That the LMs are definitely big on that one. They they they feel that one is an extremely important episode. I mean, I obviously enjoyed getting that out there. We got the bingo card out there.
[Bryan Can trill] [01:22:07] That was a lot of fun.
[Adam Levinthal] [01:22:09] Yeah. It's fun. I, you know, I like these where I get to pluck comments from social media and read them at you and Steve. I think that's
[Bryan Can trill] [01:22:16] that's a big read. Yeah. Which is this what do you call this Passover tradition? Right? Because it's Passover.
[Adam Levinthal] [01:22:23] Right? Yeah. That's right. That's right.
[Bryan Can trill] [01:22:25] With the wise child. Yes.
[Adam Levinthal] [01:22:28] Yes.
[Bryan Can trill] [01:22:28] The four children.
[Adam Levinthal] [01:22:29] Yes. What do
[Bryan Can trill] [01:22:30] you call that? Is there what's the name for that?
[Adam Levinthal] [01:22:32] I think it's just like the four children. Like the
[Bryan Can trill] [01:22:34] It's a really great and insightful and kinda wise tradition. I really like it.
[Adam Levinthal] [01:22:39] Yeah. The wise, wicked, simple, and the child who doesn't know how to ask.
[Bryan Can trill] [01:22:43] Right. Yeah. And I thought no. I and I'm like reading hacker news comments in those different again, I think we talked about this. Like, we should have a tag on hacker news where you can like to tag it wicked, simple, wise, doesn't know how to ask.
[Adam Levinthal] [01:22:58] Right.
[Bryan Can trill] [01:22:59] And I think it'd be, you know, the world would better
[Adam Levinthal] [01:23:01] It is like respond in kind too. Right? Like, because sometimes you get, like, what seems like a rude question, but it's actually a simple question. And it's an opportunity to, like, respond in a simple way as opposed to a wicked question where you can respond in a more testy way.
[Bryan Can trill] [01:23:17] Yes. This is where we have this is like, you know, where Dave has very short responses on Hacker News and you know that it's like, what Dave spent a lot of time on that response. Yeah. I I I am, and I think it was the Future Lock RFD that made Attacker News and with some comments that were less than productive. I thought Dave did an excellent job as always.
[Bryan Can trill] [01:23:39] Yeah. And I also think we had Dave was a frequent guest this year. And I mean, know, Rayne was a frequent guest, Eliza, we had a bunch of folks that were frequent guests, but Yeah.
[Adam Levinthal] [01:23:47] You know, someone on social media on that episode about Future Lock had, you know, in the in replies said, you know, but before listening to the episode or maybe as we teased the episode, talked about future lock as, like, really just you know, sometimes you're a bad programmer, and you make bugs, and, know, you doesn't mean it's somebody else's fault or whatever. And then after listening to the episode, I think it softened that position and, you know, had some contrition on the things they had said previously. So, you know, one person at a time on social media. What can you do? One person at
[Bryan Can trill] [01:24:21] a time. You know, what else can you do? I think that's pretty great. That's what you know, we're we're just doing our part here. Yeah.
[Bryan Can trill] [01:24:25] Very and then I think very, very grateful for listeners. I'm sure you mean, I I I feel I get a lot of positive feedback about the podcast, and it's really terrific. Really appreciate people calling it out, and you know, I I I got spotted in the airport a couple of times this year wearing an oxide shirt. People calling out oxide and friends references. I thought it was pretty great.
[Adam Levinthal] [01:24:50] So That's awesome. In kind of more small town news, I've sometimes parents at my son's school have said, oh, do you do you are done you are you that Adam? So that that's been fun too, you know, just in the local community finding like-minded tech nerds. That's great.
[Bryan Can trill] [01:25:09] Yeah. Yeah. That it's been so that that was really nice, I thought. I thought, but we had sounds like that was happening to you a decent amount this year too. Yeah.
[Adam Levinthal] [01:25:16] Yeah. No. It's great. Very, very grateful that, like, folks are tuning in, recommending it to folks, and tolerating us for all our foibles.
[Bryan Can trill] [01:25:25] I do feel that I want a like a chime that I can carry in my pocket that I can ring when in conversation I make a reference to a podcast episode.
[Adam Levinthal] [01:25:33] Yeah. You do it I am
[Bryan Can trill] [01:25:36] do it a lot. I do it a lot, and maybe I do it a maybe that's like, yes. I'm glad you in fact, we're thinking he should be a shock collar, not a chime. So we have actually been in the chat that includes everyone except for you. We've been taught we've got a lot of ideas that you're
[Adam Levinthal] [01:25:51] You work for a fun example. Yeah. Exactly. Exactly.
[Bryan Can trill] [01:25:54] You know, got a bunch of good ideas on that one. But well, good stuff. It's been a great year. I've really enjoyed it. Again, thanks for all the listeners.
[Bryan Can trill] [01:26:03] All of our guests have been terrific. Really enjoyed folks being willing to join us and looking forward to another great year, honestly. Yeah. And this will for the year for us. So this is this idea to 2025.
[Bryan Can trill] [01:26:18] We're out for the next two weeks. And then we will be back with a predictions' episode. Yeah. So which all the LLMs did rightly call out as a as an annual favourite. So this is going to be it'll be a good one.
[Bryan Can trill] [01:26:36] I think this is going to be a hot year. It'd be a good year to go back to where we can go do some checkups on some three year predictions. We've got some six year predictions that don't have very long to run at this point.
[Adam Levinthal] [01:26:48] Yeah. It should be fun.
[Bryan Can trill] [01:26:49] Yeah. So be thinking about those. I hope everyone has a great holiday And thank you again very much for all of your support of the podcast and of Oxide. We really deeply appreciate it. Alright.
[Bryan Can trill] [01:27:05] And thank you, Adam. I'd be remiss not to thank you. Thank you.
[Adam Levinthal] [01:27:08] Thank you, Brian. Thanks for doing this.
[Bryan Can trill] [01:27:10] This is always fun. I know it's great. This is I I I really enjoy it. I do really, really, really enjoy it. So thank you very much for Yeah.
[Bryan Can trill] [01:27:16] For everything you do. I love that question. Pledge to get better audio and Morris Chang. Sure. Now I'm gonna start to play.
[Bryan Can trill] [01:27:24] You know I'm gonna I'm going to get to Morris Chang. I like what you're doing with Evan. I'm going to try to get to Morris Chang. Furthermore, I bet a guy plays pickleball. Furthermore, I'm going to go play some pickleball and
[Adam Levinthal] [01:27:34] If he plays pickleball, I'll do that one too.
[Bryan Can trill] [01:27:37] Oh, you're going to pick him
[Adam Levinthal] [01:27:38] and then he need to go to Taiwan to play pickleball like that.
[Bryan Can trill] [01:27:41] I've always used that. Okay. There you go. Take one for the team. That's what it is.
[Bryan Can trill] [01:27:46] Alright. Thanks everyone and see you in 2026.