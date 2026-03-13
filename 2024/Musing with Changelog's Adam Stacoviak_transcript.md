[Bryan Cantrill] [00:00] First of all, Adam, should we break should we continue to break with tradition and introduce our, our guest?
[Adam Leventhal] [00:05] You know what? It actually worked out pretty well last week. So let's go.
[Bryan Cantrill] [00:08] It did.
[Bryan Cantrill] [00:09] It did. Alright. So we are joined by another Adam by other Adam, by other Jared. Adam Stacoviak, from, from ChangeLog. And, Adam, it is it is great to have you here.
[Bryan Cantrill] [00:22] We are big ChangeLog fans, and you have me very recently on the on changelog. And, you asked me really thoughtful questions. I told you I wanted to turn the tables on you. So
[Adam Stacoviak] [00:38] I'm excited about that. You know?
[Bryan Cantrill] [00:40] You're back, and we're gonna turn the tables on you. One of the things but I you know, I was I wanted to do a little bit of a of a lead in to explain the to warn people that there might be an HBO Silicon Valley reference coming, and then you literally just drop the reference right off the top. Like, we didn't even we didn't even get out of the out of the front door, and you'd already you'd already dropped in Silicon Valley references.
[Adam Stacoviak] [01:01] You did it on my show, so it's it's my turn to return the favor.
[Bryan Cantrill] [01:05] It's your turn to no. It definitely is your turn. The, and so, Adam, I don't know if you've the the Adam Leventhal, if so they ring a chime whenever the first Silicon Valley references dropped in a given episode.
[Adam Leventhal] [01:20] That's true.
[Bryan Cantrill] [01:22] Which I I think I feel I it's just deliciously passive aggressive to me. I feel it's like I feel this is the kind of thing that you do to me, which I think is it's just it's it's really it's well done. You know? It just it's because I That's
[Adam Leventhal] [01:36] great. And, Adam, you you are we're much more how long was that episode with Brian? That was, like, well into 2 hours. It
[Adam Stacoviak] [01:43] was an epic length. It was not even, like, measured in hours. It was measured in epics.
[Adam Leventhal] [01:47] That's right. No no intermission. Right? You had the no No p break.
[Adam Stacoviak] [01:51] We we it wasn't the storm.
[Bryan Cantrill] [01:53] No. I would
[Adam Stacoviak] [01:54] like, what, how many Doctor Peppers?
[Bryan Cantrill] [01:56] I I drank Diet Doctor Peppers, and I drank a couple of them. Sorry. The I was
[Adam Stacoviak] [02:01] worried about them. I was like, are you sure? Can you hold it? No. I we could take a break.
[Adam Stacoviak] [02:06] There.
[Bryan Cantrill] [02:07] No. No. No. No. No.
[Bryan Cantrill] [02:08] Let's roll. I I'm I I I'm I'm ready to roll, and I could've gone long. I gotta tell you. The you know, I think I a part of me died in the podcast episode that we did. We did a podcast episode with Jonathan Blow, Adam, and on for on the metal.
[Bryan Cantrill] [02:26] Yeah. And that guy truly outlasted me. We were we went like 3 and a half hours.
[Adam Leventhal] [02:33] And I got a flight too.
[Bryan Cantrill] [02:34] I had a flight. I had a flight. I a flight to go to New Zealand for Christmas. This is, like, not an easy one that likes you know, there's some that like, okay. You missed the flight to LA.
[Bryan Cantrill] [02:45] You kinda figure it out. But, like, you missed the flight to New Zealand for Christmas. There could be consequences. I had a flight to go to New Zealand for Christmas. We were in the garage at the time.
[Bryan Cantrill] [02:54] Hypothermia has long since set in, and I'm, like, deep into, like, hypothermia. Like, in, like, the stages of hypothermia where you just feel sleepy, you're like, you've stopped shivering, and now you're like, yeah, those are approaching. I need to pee so extraordinarily badly. And he, like a, a hurricane that has crossed Florida and entered the Gulf of Mexico, Jonathan Blow is gathering strength. I swear that guy could have gone for another 15 hours.
[Bryan Cantrill] [03:19] And I I kind of like a part of me died in that conversation, I feel, and now I have, like, I I I can channel his strength. And so, Adam, on the change log, I was ready to go with you. I I, yeah, like, you stopped me at, like, at 3 hours, but, like, you were begging for mercy. I was ready to go. I could be I could have gone another 8.
[Bryan Cantrill] [03:37] I I had the power. I had some Jonathan Bloke. Like, Yo. Oh, you heard me. You heard me.
[Adam Stacoviak] [03:42] I was I was going to go longer. I just didn't think you're anymore in you.
[Bryan Cantrill] [03:46] Oh, okay. I didn't even get to know.
[Adam Stacoviak] [03:48] I was like, there's more we could talk about here, and I was like, we we're gonna have to come back because I don't think you can live it whether this dot Doctor Pepper storm brewing anymore. So I had I had concerns for you, and I know that you got family and stuff. I just can't do that to them.
[Bryan Cantrill] [04:03] No. Okay. Meanwhile, I I had no family commitments that day. I could've gone a lot longer. Meanwhile, I don't live with all dozen of them.
[Bryan Cantrill] [04:08] It's like, hey. Hey. It's like, hey. The saber rattling here is making me somewhat nervous. Like, I actually do have
[Adam Leventhal] [04:14] I'm like, like, final look, guys. You can one up yourselves all all you want, but in 90 minutes, like, I turn into a pumpkin.
[Bryan Cantrill] [04:21] That's right. Alright. So with alright. With that then then let's dive in. So, so
[Adam Stacoviak] [04:26] disabled. Let's do it.
[Bryan Cantrill] [04:27] Am I gonna call you other how are we gonna differentiate the atoms here? You might be cool Adam.
[Adam Leventhal] [04:32] Give me AHL for this one. Yeah.
[Bryan Cantrill] [04:33] There we go. AHL.
[Adam Leventhal] [04:34] I'll I'll be handsome Adam.
[Bryan Cantrill] [04:37] Original Adam. I think you're a original Adam. That's right. The so it's making another exactly. To ring the chime there, for the for original Jared.
[Bryan Cantrill] [04:47] But, so alright. So AHL, I'll refer to you as Adam Levittall for you as a joke. American Hockey League. So, Adam, you, and I and and AHL, this is not working, are all podcast fans. And, I mean, we obviously we love podcasts.
[Bryan Cantrill] [05:04] We we each have our own, but you you got into this pretty recent. What, like, what is the history of you and the changelog? Where how how does this all start? Because this changelog starts in when? 2000 with when does it start?
[Bryan Cantrill] [05:18] A long time ago.
[Adam Stacoviak] [05:19] 1 year after GitHub. 1 year after
[Bryan Cantrill] [05:23] GitHub. 2009.
[Adam Stacoviak] [05:25] And, Wow. I was podcasting before that, though. So we were doing a show called the web 2.0 show at web 2 o show.comv. The archive is still there. So you can go back and listen to how bad it was.
[Bryan Cantrill] [05:38] Oh my god.
[Adam Stacoviak] [05:39] It was in in nostalgia. I didn't begin that show. I didn't found that show. I was invited in. And so I never thought I would actually podcast.
[Adam Stacoviak] [05:48] This is this isn't a day when, like, podcasting was just like, you would sponsor the show as charity. Like, you felt bad for the people. You know? You weren't actually getting value because there was such a small audience. Right.
[Adam Stacoviak] [05:59] It was terrible mics, and then serial later on up to everyone to say, okay. Podcasting should sound a lot better. That's fast forwarding. So back, I would say, in 2007, 2008, I wanna say, I was invited on to a podcast called the Web 2.0 Show. I came on as a co host and I did that and it was amazing.
[Adam Stacoviak] [06:20] I was working with a business partner in a consultancy and through sheer, I guess, maybe bad luck or good luck, I had to exit that partner. And so the assets of the podcast remained with the company I owned because I I I assumed 100% ownership. And so I was like, I can either kill this thing or I can keep it going and I kept it going. And so I probably did a couple more episodes probably like another 20 episodes I wanna say. And then it was sometime in 2008, a friend of mine, Wyn Netherland, that I met at a Ruby meetup here in Houston well, I say here in Houston.
[Adam Stacoviak] [06:54] I used to live in Houston, and now live in Austin, a cooler city. I met a guy named Wynd Netherland at a Ruby meetup, and he I thought he was sharp. I thought he was sharp as whip, and, we got long and we were in between, let's just say, gigs and we were noticing how fast open source was moving
[Bryan Cantrill] [07:15] Uh-huh. Now
[Adam Stacoviak] [07:15] it's just really hard to keep up. And GitHub it was founded in 2,008 obviously and sometime mid 2009, we're like, you know what? Gotta do something about this. And, obviously, I'm a podcaster by nature, and I'm like, the the best thing to do is to create a podcast and a blog to help people keep up with what's happening on GitHub. And so we did that and then for a long time, the change log episodes probably like the first 50 featured on github.com/explore.
[Adam Stacoviak] [07:46] Wait. Github.com /explore has since changed massively obviously, but that was kind of the beginning was back in 2009. It's like looking at open source, how fast it was moving, and just how incredibly hard it was in the in the sheer weight of what GitHub did to open source. It was to keep up, and it was to, like, even just pay attention to how fast things were moving.
[Bryan Cantrill] [08:08] And and so was this an official I mean, clearly, this must have been official, arrangement with GitHub at some level. I mean, they're they're basically using you as kind of like a so this is like this is like almost like this is a GitHub, not quite a GitHub podcast. It wasn't
[Adam Stacoviak] [08:21] accidental. It wasn't accidental. No. We, we format our RSS feed to be good for them to consume, and we had an episode, episode 10. And back then, we actually versioned our podcast, and it wasn't SemVer.
[Adam Stacoviak] [08:36] It was like 0 dot 0 dot 1 or something. Like, 0 dot 1 was, like, episode 1, and 0 dot 2 is episode 2, I think.
[Bryan Cantrill] [08:44] Okay.
[Adam Stacoviak] [08:44] I think 0 dot 1.0, I think was I'm trying to remember, was the episode we had Chris Wanstroff on. He was a big fan of the show, a big fan of what we're doing, obviously. And he was, like, listen, we gotta promote this more. We gotta get this on explore. People gotta pay attention to the show.
[Adam Stacoviak] [09:01] And so he's like, can I put this on there as, like, a an official podcast listen to? This fee was there. Obviously, our podcast was there but we also had a news feed that was chronicling the ups and downs of everyday open source at that time. Okay. And so it was like a consumption of like content written and then also content in terms of audio.
[Adam Stacoviak] [09:28] And do you You know, you Microsoft, that changed.
[Bryan Cantrill] [09:31] Oh, the interesting. So that that went through the Microsoft acquisitions. That went on for a a bunch of years then.
[Adam Stacoviak] [09:36] Almost. Yeah. Almost. Like, they knew about it, and I I wanna say it was probably around
[Bryan Cantrill] [09:43] 2013.
[Adam Stacoviak] [09:43] Wanna say around 2013 that changed. Okay.
[Bryan Cantrill] [09:45] Because they were they were changing by GitHub. Explore. Did Microsoft Microsoft bought GitHub a while ago? I I'm realizing, like,
[Adam Leventhal] [09:52] 2017. Forever ago simultaneously.
[Bryan Cantrill] [09:55] Yeah. Yeah. I think because they maybe because they left them alone. Yeah. Kind of.
[Bryan Cantrill] [10:01] I guess They for a while, people
[Adam Stacoviak] [10:03] thought our podcast was an official GitHub podcast. Like, for a long time, and I would I would probably even say, like, to this day, people see changelog in our podcast in some ways synonymous with GitHub. Yeah.
[Bryan Cantrill] [10:15] Interesting.
[Adam Stacoviak] [10:16] Everybody, but a lot of people who are, like, old school listeners. And it's, it's been wild, honestly.
[Bryan Cantrill] [10:22] It's a good podcast. Specifically another podcast. Tell you. Change Log is a good podcast name. I mean, just, you
[Adam Stacoviak] [10:27] know you.
[Bryan Cantrill] [10:28] As I was told idea. See, it's a
[Adam Stacoviak] [10:30] good idea. So yeah, man.
[Bryan Cantrill] [10:32] Change log and friends feels a little more, like, you may be imitating another podcast. That one may be,
[Adam Stacoviak] [10:36] like, you know, a little more derivative. Borrowing for your goodness. We just Yeah.
[Bryan Cantrill] [10:39] We'll get there, man.
[Adam Stacoviak] [10:40] You know? I like your m and m's. Those are my m and m's. Okay. Thank you.
[Bryan Cantrill] [10:44] You know what? We're here to share. Yeah. But so in what end, it but it was the change log since way back in those GitHub
[Adam Stacoviak] [10:51] days? It was literally the changelog. Like, not just changelog, but the changelog. The changelog. Yeah.
[Adam Stacoviak] [10:57] Changelog.com later on. So our first domain was changelogshow.com because we were not thinking long term and then it was the changelog.com which still exists. We own those 2 domains in redirect obviously. And then we were lucky enough to be able to purchase for $1,000 change log.com, which I think was an absolute steal. Yeah.
[Adam Stacoviak] [11:18] How does that that's that
[Bryan Cantrill] [11:20] never happens. Like, domains are have a bathtub curve. They are either $10 or they are a $100,000 or more. It feels like nothing. Like, that's in the that that that is in the the twilight zone.
[Bryan Cantrill] [11:32] No domain is a $1,000. I'm very impressed.
[Adam Stacoviak] [11:35] It shouldn't have been, but it was. And it was because I'm a good salesperson.
[Bryan Cantrill] [11:41] You wait a minute. Did you sell it to yourself? Wait. Hold on. I'm trying oh, you're you you're just a good negotiator.
[Adam Stacoviak] [11:46] I I talked to the person. They were based software. They knew of who we were. They knew we were indie, and I was just, like, you know, listen, we can really use this. You probably have no use for it.
[Adam Stacoviak] [11:57] I'm paraphrasing, obviously, but they could have said no. They could have said 5,000 or 25100 or 10,000 and I would have like why I can't afford that. I can't afford a 1,000. I'm like, okay. Cool.
[Adam Stacoviak] [12:09] Let's do it.
[Bryan Cantrill] [12:10] I would say that we do we do not have the same relationship with the owner of oxide.com. No. I would say that our relation They
[Adam Stacoviak] [12:18] love you. They love you.
[Bryan Cantrill] [12:19] Oh, no. No. No. No. I think that we have a
[Adam Stacoviak] [12:21] They love you.
[Bryan Cantrill] [12:22] Cool animus for one another that we we remind ourselves of every couple of years, in that they want I mean, the owner of oxide.com wanted the I I don't think it's what this thing. What the charge is like like, $350,000 for oxide.com. Yeah. And we're like, I don't know. Oxide dot computer is here for nighttime.
[Bryan Cantrill] [12:42] Better. Oxide dot computer is way better. So we're like So much better. The other one that we wanted that was in the the and I don't know if you've ever experimented with this with I don't know if, like, oh, is change all dotog? Is that is it dotogaatld?
[Bryan Cantrill] [12:59] We, we did get, o x I dot d e. We did price out, but that was gonna be I don't know. It's gonna be, like, €10,000 or something. I'm like, oxide dot computer is pretty good. It's 9.99 a year or so.
[Bryan Cantrill] [13:11] It's like, we are now setting an oxide dot computer. Alright. But you you you basically it must been fun to like realize the person who who has this domain is a fan. Like, likes what you're doing.
[Adam Stacoviak] [13:23] I wouldn't call him a fan necessarily, but they were definitely aware. And they seemed like like an old school programmer who just happened to have change log dot com and was willing to get the request. We also own change log on Twitter and that was really hard
[Bryan Cantrill] [13:40] to get for a while there.
[Adam Stacoviak] [13:41] I mean, somebody else was using it and they were actually using it actively Her name was change log and they were just like not at all change log. And so after probably a year or so of me just asking them and saying like, listen. Like, people are confused. Help us out. And then they they eventually just finally gave it to us.
[Bryan Cantrill] [14:03] Oh, that's nice. That's great.
[Adam Stacoviak] [14:04] Yeah. Very nice of them. And, you know, it's now x.com, of course, but, you know, it is
[Bryan Cantrill] [14:09] Not around here. Included.com/ozog. Yeah. We we don't. We, we we our position on companies renaming themselves is if the because I I Adam, I was reminded of the HL of your position on on Meta.
[Bryan Cantrill] [14:25] Yeah. That we would only refer to Meta and Metamates or metapotes, I believe, is the you're like the Greek philosopher.
[Adam Stacoviak] [14:34] Is that a thing?
[Bryan Cantrill] [14:36] No. They they wanna refer to themselves as Metabase, and I believe that Adam made the observation that, like, actually, maybe I as far as I know, this is a this is like a a Greek philosopher, an unknown Greek philosopher that you wanna be on as Matamides. Yeah. With Matamides, which so we we call them meta as punishment, but, we refuse to call them back also as punishment. It's gotta be
[Adam Leventhal] [14:56] Inconsistent, we realized, but we're sticking to it.
[Bryan Cantrill] [14:59] That that's exactly right. It. So okay. So those old episodes are have you gone back and listened to them? Are they Yeah.
[Adam Stacoviak] [15:07] But I but I'm so upset. Like, I don't I listen to them in total anger.
[Bryan Cantrill] [15:11] Do you okay. What what dude.
[Adam Stacoviak] [15:14] Because they sound like flat.
[Bryan Cantrill] [15:16] This is the odd It
[Adam Stacoviak] [15:17] sounds bad. Yeah. It just sounds like it sounds like we're so unseasoned at talking. Right? And it's just not that we're better necessarily, but, like, we've learned, I suppose, how to have meaningful conversations with people.
[Bryan Cantrill] [15:34] Oh, I see.
[Adam Stacoviak] [15:35] And so, like, episode 1, like, literally change law dot com slash one, you will hear how bad it is. Or go to slash 10 and listen to Chris Wanstroth one
[Bryan Cantrill] [15:44] of those early days GitHub.
[Adam Leventhal] [15:46] I always worry, Adam, that, like, when folks hear about Oxide in France or they hear about they listen to episode, they like it, that they're gonna make the mistake and go to episode 1. And it is I mean, it's kind of horrifying. Like, our episode 1 is, like, way worse than your episode 1. Having not listened to your episode 1.
[Adam Stacoviak] [16:05] I doubt that.
[Bryan Cantrill] [16:06] Well, our episode one's a bootleg.
[Adam Stacoviak] [16:08] You should listen to
[Bryan Cantrill] [16:08] what I love about our episode ahead.
[Adam Leventhal] [16:10] It's a total bootleg.
[Bryan Cantrill] [16:11] Our episode 1, because Twitter Spaces had no recording feature, it's recorded by someone who's just, like, has, like, a recording going on in the room or whatever. What it, but the so you so when you go back and are you or do you ever go back and listen to those episodes, Adam, or or are they just like, no. This is like too I I can't
[Adam Stacoviak] [16:32] Only in reference.
[Bryan Cantrill] [16:33] Oh, only in reference. And then Yeah.
[Adam Stacoviak] [16:35] Only in reference.
[Bryan Cantrill] [16:36] What was it? You kinda think back to those early conversations. There must have been at one of those early conversations where so I I feel this is one of the things that I certainly love is when you ask someone kind of on a lark, like, there's no way this person's gonna agree to be on this podcast, and they're like, sure. I'll be on your podcast. You're like, oh my god.
[Bryan Cantrill] [16:54] Okay. Great. What was a what were some of the early guests that were that where you were kinda surprised that they agreed to join you?
[Adam Stacoviak] [17:05] You're surprised. I expect everyone to say yes.
[Bryan Cantrill] [17:09] You did expect everyone to say yes.
[Adam Stacoviak] [17:11] I'm being suspicious, but I think the one actually there's only one that I thought would never say yes. And it's because they're not native English speaking, and they're pretty they're pretty big deal. It it was Matts from the Ruby world, The creator of Ruby. Oh, wow.
[Bryan Cantrill] [17:24] That is We had to
[Adam Stacoviak] [17:25] coax Max and we had to coax him into it by I mean, I had to really be like, we will edit. I know he shared apprehension, like, hey, you know that I don't speak English as a first handling. So it's hard to think. Right? When you have to play mental just gymnastics with, like, your native language versus the one that people are talking to you in.
[Adam Stacoviak] [17:45] Right. And you're talking about history and programming and I mean, like, it was a really good story. He went back to, like, the beginning of, like, literally learning how to program from books. He learned how to program from books. It was crazy, obviously.
[Adam Stacoviak] [17:59] It does. He would read it and then write it out. Like, I don't know. Like, he didn't learn from a computer.
[Bryan Cantrill] [18:05] This is users here too.
[Adam Leventhal] [18:06] Just Yeah. Yeah. No. I just
[Bryan Cantrill] [18:07] boy, this this this meeting has taken a turn for the very awkward.
[Adam Leventhal] [18:10] Books were a big upgrade from the stone tablets we started with.
[Adam Stacoviak] [18:14] Well, of course, but
[Bryan Cantrill] [18:15] I mean,
[Adam Stacoviak] [18:15] he didn't have a computer, though. Did you have a computer to program in?
[Bryan Cantrill] [18:18] Because he
[Adam Stacoviak] [18:19] wrote the programs. He read books and he would read things right, and he would program without a computer.
[Bryan Cantrill] [18:27] That's an important detail. Touche. To say that's they were, that's wild. So he and this is in he's in Japan. Right?
[Adam Stacoviak] [18:35] He grew
[Bryan Cantrill] [18:35] he grew up in Japan. So this is in, like, Japan probably in the eighties, but that's that must have been a so that's a when when was that conversation? That's yeah. That's an extraordinary conversation to be
[Adam Stacoviak] [18:48] able to get. Shaq Do you know
[Bryan Cantrill] [18:51] what you're looking?
[Adam Stacoviak] [18:53] Me look. You're looking. I wanna find out.
[Bryan Cantrill] [18:55] Yeah. Sorry. I'm at I'm at unfortunately, I got back.
[Adam Stacoviak] [18:58] Though. We have search. We're we have amazing search. This is a chance for me to tell you guys and your audience about my our awesome partner, if you don't mind. Typesense.org.
[Bryan Cantrill] [19:07] Open source Are you doing an ad break on our show? Wait. What? Absolutely.
[Adam Stacoviak] [19:11] Yeah. This is god.
[Bryan Cantrill] [19:13] This is this is not a master.
[Adam Leventhal] [19:14] Our guests are bringing their own ads?
[Bryan Cantrill] [19:16] They're bringing their own ads. Man, this guy's too good. You don't
[Adam Stacoviak] [19:18] have to pay me. I just do it for free. Typesense.org. Anyways, episode 202, 23 years of Ruby. Big show, Matt, the creator of Ruby programming language, joins the show to discuss where he began as a programmer, the origins of Ruby, the history and future, Ruby 3 point o, concurrency, parallelism, stream, Erlang, Elixir, and more.
[Adam Stacoviak] [19:41] Now he's jelly of of Elixir. He is jelly.
[Bryan Cantrill] [19:45] Really? Oh, that's interesting.
[Adam Stacoviak] [19:47] You can tell, but he also is jelly love. And it's like jelly love. You go back and that was 2016.
[Bryan Cantrill] [19:53] That's 2016. Yeah.
[Adam Stacoviak] [19:55] That's, like, forever ago.
[Bryan Cantrill] [19:57] It is, but you're already 202 episodes in when you did that. I mean, that's just a, it I mean, so you you said how many what do you want? You're on 500 and something. Yeah. Because I I think I was, like, 500 and what what what do you want?
[Bryan Cantrill] [20:12] Do you know? Do you keep track? What's your it's your most recent one, I
[Adam Stacoviak] [20:15] should say. I have a application that we built ourselves. It's homegrown, lovingly homegrown, written in Elixir, open source on GitHub, We're at 5:93 for that show. Wow. We also have
[Bryan Cantrill] [20:29] 3 one.
[Adam Stacoviak] [20:30] Change up on Friends, which you are you are not on the main official change of interviews with me solo. That was Friends. So Friends has its own number, and I think that episode that you were on was oh, no. You are. Sorry.
[Adam Stacoviak] [20:45] I'm I'm lying. You were on the main show. I almost dodged it there.
[Bryan Cantrill] [20:49] My bad. I've I've been on both. I've been on both. I'm I'm like, hey. I've been on the so I've been on change like twice.
[Bryan Cantrill] [20:56] I I kinda wanna be like the I wanna be like the Tom Hanks or Steve Martin to, to Saturday Night Live.
[Adam Leventhal] [21:04] You know,
[Bryan Cantrill] [21:04] they they they famously show I think Tom Hanks has hosted the show the most number of times. So that's what that's what I'm gunning for. So I don't know who who's been on change log more times, but I'm gunning for that person. I wanna I wanna set the record. Who is the person doing
[Adam Stacoviak] [21:18] the most? There are several who've been on, like, 5 or 6 times. And I Okay.
[Adam Leventhal] [21:24] I got it. I got the
[Adam Stacoviak] [21:25] whole idea. Search to find out those people. I wanna say off the top of my head, I can't tell you. But several. At least 5 or 6
[Bryan Cantrill] [21:35] Alright. Recurring
[Adam Stacoviak] [21:37] coming up. You know? Like, so you got you got 3 or so more. Alright. Yeah.
[Bryan Cantrill] [21:41] Alright. And and and off. I just assuming that they like it that that they stopped going on the show. I gotta, like I mean, I I gotta make up ground. Alright.
[Bryan Cantrill] [21:48] We gotta have to do a Keep
[Adam Stacoviak] [21:49] coming back, you know? We have some people we talk to on the year.
[Bryan Cantrill] [21:51] I gotta be coming back.
[Adam Stacoviak] [21:52] Twice a year, sometimes yearly. You know? That's that's how we do it. But you were
[Bryan Cantrill] [21:57] at We can talk about you. 592. 592. Yeah. Wow.
[Bryan Cantrill] [22:02] That's a lot of episodes. So you talk about, because you you've got the changelog, but then you've got these other podcasts that are kind of in the changelog family, like changelog and friends. Yeah. What what kind of prompted that thinking of? Like, let's start a different podcast for some of these, you know, we've got you've got one on founders.
[Bryan Cantrill] [22:21] You've got or start startups. You've got one on go. You got a couple of them. John, we got come on. I think I'm JavaScript or TypeScript.
[Bryan Cantrill] [22:28] So, Louis, describe kind of the thinking there and how this worked out.
[Adam Stacoviak] [22:34] They have, just one podcast. You know, why not have many? Of course. The idea for a long time was a network of shows, but not just the network of shows just to have multiple shows, but a family of shows that complement each other, had similar production value, etcetera. And my my business partner, Jared, is not in this conversation, unfortunately.
[Adam Stacoviak] [22:56] He is an awesome dude. He's right now coaching baseball. He's that cool of a person. He shows up for the children and he's and he just lays it, you know. But here I am not showing up for the kids.
[Adam Stacoviak] [23:06] Just podcasting. You know what I'm saying? But,
[Bryan Cantrill] [23:08] Jared's playing my little league baseball coaches in Adam and me. So we got Jared's very successful.
[Adam Stacoviak] [23:14] Soccer and stuff like that for my kids. I just not baseball yet. We haven't done that yet. But anyways, so he's not here to represent, but he is very much my better half when it comes to, like, a business relationship, you know? And so, unfortunately, he's not here to represent his side of it, but I can say on his behalf that our ideas my ideas are not just my ideas, they're our ideas.
[Adam Stacoviak] [23:38] And so we always what made us be a good business partnership and a good partnership generally, not even just business partnership, was that there's a lot of yin and yang to to he and I and how we operate. I'm very, you know I
[Bryan Cantrill] [23:51] believe you mean yin and yang.
[Adam Stacoviak] [23:54] Yeah. Good good job. It's actually Ring
[Bryan Cantrill] [23:57] and Yang.
[Adam Stacoviak] [23:57] That is a that is a
[Bryan Cantrill] [23:58] yang pull. No. That is a no. That is a that that is a Silicon Valley reference among other things.
[Adam Stacoviak] [24:07] I can give you That
[Bryan Cantrill] [24:07] is a wrong LeFlom.
[Adam Stacoviak] [24:08] Do you want the ding to put it in there? That I
[Bryan Cantrill] [24:10] want the ding right now. That is a that that is a I I that is an aces Ron Ron Laflum reference I just dropped. I feel. Oh, yeah. You did.
[Bryan Cantrill] [24:18] Sorry. But you but you you kinda botched it
[Adam Stacoviak] [24:20] a little bit though. You you it's yin and yang.
[Bryan Cantrill] [24:23] No. It's yin and yang. Yeah. Yin and yang. And then Ronda Flom says yin and yang?
[Bryan Cantrill] [24:29] Doesn't make any sense. This is the the lawyer that he has that I It's true.
[Adam Stacoviak] [24:34] It's
[Bryan Cantrill] [24:34] yin and yang. It's, like, no. It's written yin. Dude, this is the
[Adam Stacoviak] [24:37] yang. Yeah.
[Bryan Cantrill] [24:40] Everyone's on the show
[Adam Stacoviak] [24:41] as well as we do it. I was, like, what the heck are they talking about?
[Bryan Cantrill] [24:44] Okay. So let's just run through a bunch of Richard's corrections of other people. I love like, I there's must be a super clip of, Richard Hendricks, the founder of Pied Piper, fictional founder of Pied Piper on Silicon Valley. Sorry, Adam. We're here.
[Bryan Cantrill] [24:58] And the he is a broadly an unsympathetic character, I would say, as as most of the characters are, but he definitely exhibits some classic nerd behavior that exists in many of us, including me. And so he so, Adam, can
[Adam Stacoviak] [25:13] you Honestly. So we we we offended by that or not, but you kinda are.
[Bryan Cantrill] [25:19] Are you calling me Richard Hendricks?
[Adam Stacoviak] [25:22] Yeah. I think you're very Richard Hendricks. Don't be offended. He's awesome.
[Bryan Cantrill] [25:26] Okay. Oh, yay. No. No. No.
[Bryan Cantrill] [25:29] I well, no. So but you're not what I really like about the show is that that he loses his way, and very, like, morally loses his way. And it and, drifts into, does things that are contrary to what he had kinda set out to do. But to for for the kind of the the immediate he the the the means are justifying the, or the ends are justifying the means rather for for Richard. It's part of the reason that I
[Adam Stacoviak] [25:57] Yeah.
[Bryan Cantrill] [25:58] Okay. But so he has got there's I love his corrections of other people, including flaccid. It's flaccid. A lot of people don't know that. The, his doctor puts him together and accuse he says, like, you know, we're gonna turn you into a Frankenstein.
[Adam Stacoviak] [26:13] Frankenstein. Yeah.
[Bryan Cantrill] [26:13] Frankenstein as monster. Like, I think you mean Frank's monster to which his doctor says, are yeah. Are you oh, you're one of those guys? You're one of those guys?
[Adam Stacoviak] [26:22] He basically kicks him out at
[Adam Leventhal] [26:23] that point.
[Adam Stacoviak] [26:24] He's like, get the hell out of here.
[Bryan Cantrill] [26:26] And then and then, yin and yang. Not not yang and yang. I I don't know if we wanna go here now, but why do we both like the show so much?
[Adam Stacoviak] [26:39] Well, it's the best proxy to to our life. That's why I like it. It's it's the best proxy.
[Bryan Cantrill] [26:44] It's really good.
[Adam Stacoviak] [26:45] It's an absolute masterpiece. There is so many layers. You can watch it again and again and still get more from it, like, Gart in season 1 who I missed. You know, it's, like, I just totally miss that. Like and I've watched a lot.
[Adam Stacoviak] [26:59] I was embarrassed that I didn't get it. That's a shame.
[Bryan Cantrill] [27:02] To be fair, I only picked that up on my 4th rewatch.
[Adam Leventhal] [27:06] Right. We were talking about, you're talking about Ruinous Empathy the other day.
[Bryan Cantrill] [27:10] I was talking about Ruinous Empathy.
[Adam Leventhal] [27:12] Of the show not realizing it was actually part of the radical candor manifesto. Like, it it was
[Bryan Cantrill] [27:19] I was shocked by that. So you you Adam, do you recall the ruinous empathy that that other Adam, that original Adam is referring to the this is Yeah. Yeah. An episode that episode is actually extraordinarily good, extraordinarily tight. That is the parlance, by the way, original Adam of the the COO that that, Richard wants to poach.
[Bryan Cantrill] [27:45] It's the COO that seems like and and he's contrasting it. The Jared and the COO just seems, like, so polished, and he practices radical candor. And he then he cautions Richard that he's he's devolving into ruinous empathy, which I thought was hilarious writing. And you pointed out to me as, like, no. That's an actual thing from the book, radical candidates.
[Adam Leventhal] [28:06] That's right. Like, page 35 or whatever. Right?
[Bryan Cantrill] [28:09] Which is just I I mean, this is what makes this so good is that the line between satire and reality gets so blurry that in this case, I literally thought was satire when it was reality. And I think this happens over and over and over again with the show, which, I mean, is what makes it so terrific. I mean, it's such good satire. The good
[Adam Stacoviak] [28:31] thing, I think, more broadly about the show is that nobody else gets it. Like, it's it's literally the masterpiece for a very small subset of Earth. It's not There is definitely it
[Bryan Cantrill] [28:43] well, let's see when Richard breaks up with his girlfriend over tabs versus spaces, for example. Yeah. And which is gonna be something that to most people is gonna be like, what? And to software engineers, it's gonna be like, yeah. I've had relationships I know in white space.
[Bryan Cantrill] [28:59] Yeah. Makes sense.
[Adam Leventhal] [29:00] Yeah. Exactly. Right.
[Bryan Cantrill] [29:02] You know? It's like, wait a minute. Yeah. For sure. No.
[Bryan Cantrill] [29:04] It's and it it is very, very, very well acted. What are some of your kind of favorite moments, Adam, of just, like, some of the most the the moments in the show that are sublime to you. I'm just like, wow. That is so that represents so much. That's so like, because of these what I love about the show is these are little moments that if you haven't lived, they just kinda go in and out, but they are they're very good.
[Bryan Cantrill] [29:29] Do you have any that come to mind?
[Adam Stacoviak] [29:32] Absolutely. I think my favorite line in the entire show is the very last episode whenever they're discovering, spoiler alert, when they're discovering the problem. Right? And Guilfoyle walks in, and they're like I think Dinesh says, what's in the bag? And he goes, Cliff bars and a gun.
[Adam Stacoviak] [29:53] I'm, like, what a what a one liner. Right? That's the best right there. And then when he is describing when Gil was describing what's happening and, Jared says, I don't know how should I feel. And he's like, for you, abject terror.
[Adam Stacoviak] [30:08] I'm like, that's the best So point ever. That whole scenario.
[Bryan Cantrill] [30:11] I I feel we can original Adam. I I I feel we can describe that we worked with someone who is has a lot of guilfoyle characteristics. To anyone who's worked with this person and has seen the show is like that seems to be the direct and and this is not the only person like this. It's part of the reason why it's great satire. But the this issue of the gun does ring up.
[Bryan Cantrill] [30:37] This is, needless to say, someone who very much believed in their the right to bear arms. And at one point, one particularly divisive moment, was talking about his gun a lot. And Adam said, why don't you bring your gun to work? And he's like, I will bring my gun to work. I'll bring my gun to work tomorrow.
[Bryan Cantrill] [30:57] And Adam is calling him on his bluff. Original Adam is calling him on his bluff. He believes he's bluffing. He's like, I don't think I don't think you have a gun. And if you have it, I don't think you're gonna bring it to work.
[Bryan Cantrill] [31:06] Another colleague of ours is, like, original Adam, I think you'd agree, not totally illegitimately freaking out over this conversation. I Yeah. He is just like stop. Stop. Adam, stop.
[Bryan Cantrill] [31:21] Adam, stop. Stop. He's like, no. I'm just saying he should bring his gun to work. He's like, no.
[Bryan Cantrill] [31:24] Please stop. Don't do this. Please stop. Stop. And and and, of course, our our Guilfoyle is like, I will bring my gun to work.
[Bryan Cantrill] [31:31] I'm bringing my gun to work tomorrow. And it was getting, like, I mean, you, you know, you were kind of your your, older sibling was coming out, I dare say. And then you were, I mean, you felt you had an opening and you were taking it.
[Adam Leventhal] [31:43] Totally. I I think I didn't show up to work the next day if I'm working.
[Bryan Cantrill] [31:46] Oh, I I for sure didn't. I'm like, well, I'm just gonna wait wait for a couple days for this to cool off. I got nothing to nothing to gain. I can work from home today. I got nothing to gain by going to work, and I just exactly.
[Bryan Cantrill] [31:56] So, definitely, a, very much resonates. Gil and and there are many attributes of Guilfoyle that that that resonate, I feel, with, I also feel that, like, there's so many little characters that really resonate in in Silicon Valley. I mean, I the I I mean, god, it's like are there actually Adam, let me ask this question of you. Are there are there particular, like, characters that are smaller characters that resonate with you? Or that you're just like, wow.
[Bryan Cantrill] [32:28] I got I I feel like this is just nails. Who are your favorites?
[Adam Stacoviak] [32:34] I don't know. There's a lot of there's a lot of characters. I think double a was a good character. I think, is a good character. The stunt guy for double a.
[Adam Stacoviak] [32:48] I can't remember who this
[Bryan Cantrill] [32:49] guy is.
[Adam Stacoviak] [32:51] Well, he's done.
[Bryan Cantrill] [32:52] So the yes. So this is
[Adam Stacoviak] [32:55] Quick cut.
[Bryan Cantrill] [32:55] This is Is that cool? Yeah. Yeah. I think so. I think that we have to when we upload a YouTube, we have to say if it's for kids or not, which is super weird.
[Adam Leventhal] [33:04] Not for kids. We, we talked about a a former joint connection. We had Jason Hoffman on
[Bryan Cantrill] [33:10] Oh my god. That guy. GTO.
[Adam Leventhal] [33:11] It was it was like an episode of it was like The Big Lebowski here, like, in terms of how much how much f bombs that we're dropping. So, I don't know.
[Adam Stacoviak] [33:20] F bomb. But, like, you know, asshole is okay with me. I'm cool with asshole.
[Bryan Cantrill] [33:25] That's fine.
[Adam Stacoviak] [33:27] I think clip.
[Bryan Cantrill] [33:28] Like, we're gonna clip that out and promote it. I'm cool with Asshole.
[Adam Stacoviak] [33:33] You should you should warn me. So I think that was a I mean I
[Bryan Cantrill] [33:36] just did.
[Adam Stacoviak] [33:38] The the whole fact that they were, like, swatting the scenario But but okay. So was very crass, you know, I'm not gonna say that part, but, like, Gina
[Bryan Cantrill] [33:48] So so to give folks additional contact. You you should give folks additional contacts that that the this guy is a former colleague of Ehrlich who has started an energy drink called homicide, which is Right. Just genius. The on and the the the, to promote homicide, there's gonna be a stunt. Blaine is going to be, doing a stunt, and Guilfoyle and Dinesh realize that Blaine has miscalculated.
[Adam Stacoviak] [34:18] And he
[Bryan Cantrill] [34:19] they and Blaine is being a real dick to to Dinesh Guilfoyle. Blaine is miscalculated, and Blaine is going to die if he does the stun as he's calculated.
[Adam Stacoviak] [34:27] Yes.
[Bryan Cantrill] [34:28] And so they and meanwhile, Janesh has fallen in love with with Gina, his girlfriend who works there.
[Adam Stacoviak] [34:35] Does with every woman, basically.
[Bryan Cantrill] [34:37] As he does with every woman in the show. Yes. Yeah. So they do a SWAT analysis of strengths, weaknesses, opportunities, and threats. Adam, have you ever done a real original Adam?
[Bryan Cantrill] [34:49] Have you done an actual SWOT analysis? Yes. Yep.
[Adam Leventhal] [34:51] 100%. And before, like, before Silicon Valley was on the air or whatever, like, absolutely a 100%. And I think that's why both I mean, I'm sure for you too. That's why it both resonates so deeply, but also so painfully at times where I need to, like, pause it, like, take a walk and Take
[Adam Stacoviak] [35:07] a walk.
[Adam Leventhal] [35:07] Me a minute to get back.
[Bryan Cantrill] [35:09] I've been in this room. For that. Yes. I love that. I'm not
[Adam Stacoviak] [35:12] I don't have that depth like you all do. I was telling you, Brian, when you're on the show, I'm like, this is you've lived this. I've been watching this. Now I've been podcasting and tech adjacent in a lot of ways, like and tech steeped in many ways as well. But, like, you guys have lived nagging.
[Adam Stacoviak] [35:28] You know? Like, I haven't lived nagging. I've been so cool.
[Bryan Cantrill] [35:30] We have lived
[Adam Stacoviak] [35:31] I haven't lived swatted.
[Bryan Cantrill] [35:32] I just swatted
[Adam Stacoviak] [35:33] a couple things, but, like, not as deep as y'all have.
[Bryan Cantrill] [35:37] Oh, so I've got a Adam, I've got a great swat story for you because, so because you've had Scott Hammond on your show. Right?
[Adam Stacoviak] [35:45] A long time ago. Yes.
[Bryan Cantrill] [35:46] At some point. Long time ago. And so, Scott, I had not watched HBO Silicon Valley, and I'm like, you should you really need to watch this, and he started binge watching it. And then Scott has got a very dry sense of humor, and he would just start dropping Silicon Valley references into like, he didn't really care if anyone else got them or not, because, that's the way Scott's totally content to be the only one in the room and on the joke. It's like, no problem.
[Bryan Cantrill] [36:16] And we have a consultant in, and they start doing a SWOT analysis on some problem. And Scott just leans back in his chair and says, let Blaine die. And they're like, what the what are we? And I'm like, oh my god. He's referring to that Silicon Valley episode where they wonder what because out of the with the the what the swan houses they do is, should they let Blaine die or not?
[Bryan Cantrill] [36:40] So it's let Blaine die. It's got the and it's So it's a very, I you know, this is the the what's the power of it? You can kinda drop it right back in the conversation. So this is why everyone needs to see this because it's, like, it's great.
[Adam Stacoviak] [36:52] So My my prescription for life really is if you're in tech, if you're in software, if you're in this world, if you listen to this podcast, you owe it to yourself to level up your entire life by watching all 6 ep all 6 seasons, end to end All
[Bryan Cantrill] [37:08] 6 seasons. I get it. Once. I would say
[Adam Stacoviak] [37:11] end. Really
[Bryan Cantrill] [37:12] three times. Multiple times. Oh, yeah. I agree with that. I think I
[Adam Stacoviak] [37:15] am missing out. Like, you just, like, lost part of the world.
[Bryan Cantrill] [37:20] It it rewards multiple viewings. So there are a couple of characters that stand out to me as just like and, original Adam, I know you are you're still working your way through. At some point, you hit the episode where they fire the CEO and everyone reports to the chair. And if I recall correctly, you're just like, I can't do it anymore.
[Adam Leventhal] [37:38] There were a couple of moments where I was like, I'm living this day to day. Like, I can't this is too much emotional energy for
[Bryan Cantrill] [37:44] me. Right.
[Adam Leventhal] [37:45] Adam, maybe you'd, like, envy that moment that but those are the moments I needed to take a break.
[Bryan Cantrill] [37:52] Yeah. It's where it's just too real. And I do feel that well, I mean, I have also reported into the chair. And because Laurie Bream, the venture capitalist, makes clear that, like, we're looking for a new CEO, and it's not gonna be any of you, by the way. So just like you report we trust the chair more than we trust any of you.
[Adam Leventhal] [38:11] I reported to the chair too.
[Bryan Cantrill] [38:12] Yeah. I reported to the chair. I called the office of the CEO. And but the, and that is just after action Jack Parker is fired. Adam and the I I love acting Jack Barker's character and the conjoined triangles of success.
[Adam Leventhal] [38:31] I love I love you, Zeke. You can't make that up. Of course, I you know, I did make that up.
[Adam Stacoviak] [38:35] So recently. We had
[Bryan Cantrill] [38:36] to do it recently.
[Adam Stacoviak] [38:37] And I had to bring it in, like, literally as an example of what they should do. Like, the conjoined trial you know, like, this thing, this this visual I brought into an episode recently, and I think Jared sometimes, my business partner slash host, gets upset because, like, it's true, and it's also a Silicon Valley reference. That's how it works.
[Bryan Cantrill] [39:00] It it the one of one of my kind of sublime lines in the show is when Richard is at odds with action Jack Parker, the CEO, and propose and proposes a compromise. And Jack Parker says, compromise is the shared hypotenuse of the conjoined triangles of success
[Adam Stacoviak] [39:17] is. Yeah.
[Bryan Cantrill] [39:17] Which which original Adam can attest. I drop into oxide meetings with, I I I'm realizing that that's not a reference you can just kinda drop and expect people to get. Like, that's
[Adam Leventhal] [39:28] So, Brian, regarding the conjoined triangles of success, I just want, there is a CEO, former CEO that you and I both know of an observability company that was acquired who had that up on his wall. And I think that might make you like him all the more.
[Bryan Cantrill] [39:43] I do. I have that up on my wall at home. They could join triangles. Yes. I do.
[Bryan Cantrill] [39:48] I do. My my kids have realized that, like, we can get like, if we get dad any Silicon Valley themed anything, it's like it's it it's basically a grand slam. So they I've got the conjoined triangles success. I've got an Aviato shirt. Richard, I've got I'm wearing right now my Pied Piper shirt.
[Bryan Cantrill] [40:06] No. I we've got the what what nah. Are you just calling me out on the video thing? I am wearing a Pied Piper shirt right now.
[Adam Stacoviak] [40:13] Yeah. I almost said it, but, yeah, like, if I see you, I could tell if you're telling the truth.
[Bryan Cantrill] [40:18] I'm gonna and so do I have to, like, tweet out a selfie? Is that what I have to do? Because I
[Adam Leventhal] [40:23] With today's newspaper. Yes.
[Bryan Cantrill] [40:24] With today's newspaper, I I So don't really good one. How do I do I maybe do I do I what I need to do is, like, a a selfie of, like, the the the the Discord. Is that is that gonna be Sure. Yeah. I believe you.
[Adam Stacoviak] [40:39] You don't have to go that far. I'm a too.
[Bryan Cantrill] [40:43] You you do not believe me. You definitely did believe. I volunteered it.
[Adam Stacoviak] [40:46] Like, you're up you.
[Bryan Cantrill] [40:49] Believe me now. Now that I'm gonna tweet it, you believe me?
[Adam Stacoviak] [40:52] I don't want you to shame yourself by tweeting things like this. You know? I get you. I got you. You're okay.
[Adam Leventhal] [40:59] This isn't a minor character, but the character who who kinda gets me the most is Big Head. Just the the, like, scale up culture of Silicon Valley. Like, we all know a big head.
[Adam Stacoviak] [41:11] Oh,
[Bryan Cantrill] [41:11] we know a big head.
[Adam Leventhal] [41:12] We're like, how on earth is this person, like, succeeding despite no specific or general talent whatsoever?
[Bryan Cantrill] [41:20] I am really glad you brought up Big Head because, Adam, we know a lot of there actually are a lot of big heads. It's a very it because and and there there is actually a correlation here because in the dotcomboom, the people I know who made the most money made the most money because when they weren't that interested in tech. And so when things kind of exploded in 99 or 2,000, they're like, well, I'm gonna sell everything. Whereas the rest of us were like, oh, man. It's kinda it's kinda this is it's a new paradigm or whatever.
[Bryan Cantrill] [41:54] And so I know a couple of people I kinda wanna name a name. I wanna name a name. I feel I I feel I can name a name right now, Reginald.
[Adam Leventhal] [42:02] Know is edit out later or not.
[Bryan Cantrill] [42:03] Okay. So I feel he is not gonna be overly I don't think he's a listener to this podcast, but I think so. Did you know Bruce Hildebrand at Sun? Bruce Hildebrand, all that guy wanted to do is ride his bike. He this is the guy who who would like and, Bruce, if you're listening to me, you know this is true.
[Bryan Cantrill] [42:18] This guy would come in at 10, he would leave at 2, and he would take a long lunch. I mean, he all he wanted to do is ride his bike. So that guy sold every last ounce, and he'd been at Sun forever, sold it all at the tippity tippity tippity top. And how it was never heard from again. Good going, Bruce.
[Bryan Cantrill] [42:38] That that is like and it just like I mean
[Adam Stacoviak] [42:41] That's what
[Bryan Cantrill] [42:42] he meant. I I just hope he appreciates the role of absolute dumb luck, and I hope when he's watching Silicon Valley and seeing big head, he's like, that's kinda me. Because that is definitely Bruce, it's you. You and I both know it. It's not But there are many such groups.
[Adam Stacoviak] [42:55] 20,000,000. 20,000,000. Yeah. Totally. Totally.
[Bryan Cantrill] [43:01] And the roof. Oh god. The roof. So the, it gets original item I agree with, like, there are
[Adam Stacoviak] [43:08] Brian, do you have a burka?
[Bryan Cantrill] [43:11] The bow tie. Another line is so then big head burns through all this money is the other thing. And, spends a lot of money. Help. Not the swimming pool.
[Bryan Cantrill] [43:23] He had help. Well, no. But he had did have help. He's like, the swimming pool felt like it was a little too far away from the house. So I I moved it closer.
[Bryan Cantrill] [43:33] He's like, yeah. We moved it closer, but then you also moved it back. He's like, yeah. As it turns out, the guy who designed this house really knew what he was doing, and it was actually in the right
[Adam Stacoviak] [43:43] Imagine, like, what it would take to really move a house to do that there and back again?
[Bryan Cantrill] [43:50] To moving a swimming pool. Oh, it's so good. I feel like that's such a good metaphor. There's so much there's so much moving swimming pool back and forth in Silicon Valley where you're just like especially when people have far far far too much money. The, you know, another in so I actually how do you feel about the laters?
[Bryan Cantrill] [44:10] I really like the later seasons. I like every season of them equally.
[Adam Stacoviak] [44:16] There's so much goodness in every single one of them. Sometimes I just, like, begin at season 4 and go to the end. I, like, go right in the middle. I think probably my least favorite episode, and I'm I'm trying to figure out why. Actually, I was preparing for this.
[Adam Stacoviak] [44:29] Like, I think it's the bug manity insanity episode. I just like, something about that episode just doesn't oh. Like, I I like it, but it it feels like the one episode in the whole thing that it's just weird or doesn't fit well.
[Bryan Cantrill] [44:43] Oh god. I love that episode. So just to give people context, Arrowrock Bachman has found actually, in Big Head has found a partner. They formed Bachman Capital because Arrowrock brings the Bachman and Big Head brings the capital. He's right.
[Bryan Cantrill] [44:58] It's the Bachman capital reference for
[Adam Stacoviak] [45:00] your day.
[Bryan Cantrill] [45:00] And they blow this money on this lavish party in Alcatraz, where they decide to make it look tropical, which is the dumbest idea. Absolutely. The the absolute dumbest idea ever. And, no. I love that episode because they burn through all of their money effectively in one single episode.
[Bryan Cantrill] [45:19] They they they they burn through $20,000,000, and at the end, they are, like, finally getting on stage and the clip is dropping the chat. It's just like getting on stage saying aloha, which means hello. And then big head points out, oh, and also goodbye. It's just very good. I I it it felt believable.
[Bryan Cantrill] [45:35] He just felt like
[Adam Stacoviak] [45:36] like waste that money. Like, I don't think he wasted like, that episode is not believable. That's why. Like, oh, that is more than that.
[Bryan Cantrill] [45:44] Yeah. I got a prayer, my friend.
[Adam Stacoviak] [45:46] Oh, that is a prayer
[Bryan Cantrill] [45:47] that is you see just the the the level at which capital gets burned through when things are rich. It it I mean straight out
[Adam Leventhal] [46:00] of KubeCon? Like, the is that that it is
[Bryan Cantrill] [46:02] That that that's a that is a great example. Yeah. Describe straight out of God straight on a cube con.
[Adam Leventhal] [46:09] So this is Oh my god. Kubernetes conference. Ice cube to perform. I guess I I wasn't there.
[Bryan Cantrill] [46:16] Yes. It it it hires the ice cube to perform.
[Adam Leventhal] [46:19] The ice cube.
[Bryan Cantrill] [46:20] And actually, if you
[Adam Leventhal] [46:21] pay enough, they'll change the gear. Kick Hill. It'll be instead of straight out of Compton, it'll be straight out of KubeCon.
[Bryan Cantrill] [46:27] Right out of KubeCon. Like, you cannot imagine anything cringer. Like, I mean, honestly, Adam, I would put and I think straight out of KubeCon is a great example. I would put straight out of KubeCon as even less believable than block manity insanity. The problem is it actually happened.
[Adam Leventhal] [46:43] Oh, I I got another one that that's like that that yeah. I'm not sure you'll believe me. Like, what was it called? Nick Centa, this software defined, oh, ZFS appliance company. Yes.
[Adam Leventhal] [46:54] Had Hillary Clinton keynote their conference. I like I realized even as I'm saying it, like, it sounds like a dream that I'm telling you about, but this is a real thing. Oh, no.
[Bryan Cantrill] [47:05] This is crazy.
[Adam Leventhal] [47:05] I hold in my favors to, like, go be front row in that.
[Bryan Cantrill] [47:09] Oh, you're not gonna talk about the price tag?
[Adam Leventhal] [47:12] Oh, I have no idea what the price tag is. Do you know?
[Bryan Cantrill] [47:14] No. You told me what the price tag was.
[Adam Leventhal] [47:16] What was what did what did I tell you? I'm sure it was true.
[Bryan Cantrill] [47:18] $500,000.
[Adam Leventhal] [47:21] I I believe it. I'm I'm I got They
[Bryan Cantrill] [47:22] paid 500 paper to talk.
[Adam Leventhal] [47:25] That sounds right.
[Bryan Cantrill] [47:26] And I was just like, I was just on my lap.
[Adam Leventhal] [47:31] And if you come to my house, I've got a copy of her book, Hard Choices with a Nick sent a sticker on, like, the inside jacket.
[Bryan Cantrill] [47:40] Oh, just souvenirs. I love the I you know, it's so important to gather you know, I've got a, a a a friend of mine was an early, marimba employee, if you remember marimba from way back in the day. I've got a signed, bottle of marimba IPO wine, And that would just feels like it just it's such a time capsule. Undrinkable, presumably, but there's such time capsule.
[Adam Leventhal] [48:07] But, like, if that was in Silicon Valley, you might say, come on. Ridiculous. Like, how this that would never happen.
[Bryan Cantrill] [48:14] The and so the straight out of Cube Con, I did talk to folks that went to the Ice Cube performing. I mean, it sounds like it would be cringey and awkward. And I thought you're still bad for Ice Cube. Like, you're not you're like, you're an artist. I think Yeah.
[Bryan Cantrill] [48:32] You're a legend. I think Ice Cube is protective. It's like, yeah. I'm also, like, getting I'm getting paid.
[Adam Leventhal] [48:36] I'm also for sale.
[Bryan Cantrill] [48:37] I'm also for sale. Yeah. And this did lead us down to, like, how much does it cost to have ice cube? Or is and they do this in oh, this is not in the bockman insanity. It's a different episode where they have, Florida.
[Bryan Cantrill] [48:54] Right? Is at at the at, Peter Gregory's thing. At Peter Peter Gregor yeah. Peter Gregory's, toga party or what have you.
[Adam Stacoviak] [49:03] He's in 1.
[Bryan Cantrill] [49:04] The, so this is like no. This is this is what makes the show amazing is that it is recording things that actually happen as far as we're concerned. And the so the strain of the KubeCon, apparently was sparsely attended rather awkward. Ice Cube definitely left the second his contract was up, basically. It was a performed the the the contractual, but then we went on we started shopping for other celebrities, and some of them are, like, tantalizingly inexpensive.
[Bryan Cantrill] [49:34] And in particular, I remember doing this where we think we learned, if I recall correctly, that we could have Snoop Dogg at an all hands for, like, $40,000, and that feels like that felt the spent. It Well spent. I I just spent. Yeah. Spent.
[Bryan Cantrill] [49:54] I gotta say, like, the years of seeing all that stuff gives me an allergic reaction to more or less all of it. That all of the the kind of the lavish parties and I it's just like, it is basically money that has always lit on fire. It is not. And and the company, indeed, they the company that sponsored straight out of coupon, this is Mesosphere. I'm from Oh my god.
[Adam Leventhal] [50:15] I was gonna I was wondering if it's Mesosphere because, like,
[Adam Stacoviak] [50:18] I
[Adam Leventhal] [50:18] remember going to buy their office, like, right after they had raised. And it was just like it it was just money hung from all the walls. Like, they had 3 receptionists. They had, like, monitors dripping everywhere. It was it was ridiculous.
[Bryan Cantrill] [50:35] Right after they raised that big and effectively final round because it was a bunch of Gulf State Sovereign Wealth funds that invested. And this is where you get do you remember the character Maximo Reyes?
[Adam Stacoviak] [50:48] Oh, yeah.
[Bryan Cantrill] [50:48] Adam? Yes. The so original Adam, this is a
[Adam Stacoviak] [50:54] podcast. Yes.
[Bryan Cantrill] [50:57] Yes. Yes.
[Adam Stacoviak] [50:59] We are podcast.
[Bryan Cantrill] [51:00] This is a
[Adam Stacoviak] [51:01] Richard and I,
[Bryan Cantrill] [51:02] This is a a Chilean investor who wants to invest a lot of money in Pied Piper. It's great. Turns out he's also he's the the the son of a he's in a mining family that has had a long history of labor disputes in Chile. And so Richard is like this space seems very reasonable. So Richard and what to me, what is truly one of the sublime moments of the entire series.
[Bryan Cantrill] [51:28] Richard goes to Maximo's house. He's got this gorgeous house, and and he seems like very charismatic and plausible. And as Maximo is talking, there are the a bird flies into the window because he's got these huge clear glasses. And he doesn't like, Richard, like, jumps, and Maximo doesn't flinch. And birds through the rest of the scene, birds keep flying into the window and dying.
[Bryan Cantrill] [51:53] And there's just someone out there scooping the dead birds and and they then cleaning the glass. And I just think it is so Mhmm. I I don't know. I I I thought I mean, Adam Shrill, you thought that scene was just genius. I thought it was so terrific.
[Adam Stacoviak] [52:06] It was there's nothing ungenius about every scene. I mean, like, that is perfect because, like, that as soon as he was done scooping up the bird, there was another bird. And then he, like, turned around beguarging, like, oh my gosh. One more bird. And Richard is jumping every single time.
[Adam Stacoviak] [52:23] Masimo is not moving at all and it's the whole entire episode is called blood money. Yes. Right? Then he walks in as, like, several terimotos. He thinks it was 1,000,000 or whatever.
[Adam Stacoviak] [52:38] It was a 30,000,000 or something, and then it was actually not. It's more like a 1,000,000,000 something.
[Bryan Cantrill] [52:44] Yeah. It's a great it's a great character. I love the those later seasons I actually think, are are terrific.
[Adam Stacoviak] [52:51] House. You know? That's why the birds are trying to get there. There there's a tree in the guy's house. Like, it he built the house He should get around the tree.
[Bryan Cantrill] [52:59] Oh, god. That's such a good point.
[Adam Stacoviak] [53:01] That's why the birds
[Bryan Cantrill] [53:01] are trying to get there. That I forgot. Right.
[Adam Stacoviak] [53:03] The birds are seeing the
[Bryan Cantrill] [53:04] tree that's in the house. Right. Yeah. So the birds are seeing the tree. Right.
[Bryan Cantrill] [53:09] And he's doing nothing to kind of prevent this.
[Adam Stacoviak] [53:11] And, like, the birds in the house episodes later, she's like, I love this tree. This is a remarkable tree or something like that. Like, she was, like, looking at the tree.
[Bryan Cantrill] [53:22] It is. Laurie Breen Laurie Bream is another absolutely terrific character. Unbelievably well acted.
[Adam Stacoviak] [53:32] I mean,
[Bryan Cantrill] [53:32] the acting is just very, very good. Laurie Breen plays a venture capitalist. Do you have any particular favorite Laurie Breen lines, Adam? Alright. It'd be let let me know if you wanna stop talking about so I can die, by the way.
[Bryan Cantrill] [53:42] We can talk about other things. I'm just you know, I'm so I'm so happy to be among my my fellow fans.
[Adam Stacoviak] [53:47] Yeah. I think she gave I'm trying to remember the name honestly. I'm I'm feeling blanked but there's one thing she kept saying at the end. What was his name? Peter Gregory.
[Adam Stacoviak] [53:57] Peter Gregory is dead. Monica She kept saying that over and over to Monica.
[Bryan Cantrill] [54:01] Oh, no. We're good. She's like,
[Adam Stacoviak] [54:02] oh, I I know. I know. Monica, Peter Gregory is dead. The What's your point, lady? Come on.
[Adam Stacoviak] [54:10] Get to it.
[Bryan Cantrill] [54:11] I I I love the well, she becomes pregnant also. And then, wait.
[Adam Stacoviak] [54:17] She's like, I can deliver this baby and come to work the same day. Watch me.
[Bryan Cantrill] [54:22] Yeah. Is she but I love the when Richard is, Richard's been rich ripped off by Jin Yang who has is going to start a Chinese rival to Pied Piper, and has taken the software for Pied Piper, but it is a it is a it is a Christian dating site in China. And he's very concerned about this. And he wants Laurie Bream to do something to stop it. And Laurie Bream says, Richard, if you lose to a Christian gay dating site in China, look inward, which I it's another one of my favorite lines.
[Bryan Cantrill] [54:55] I love look inward.
[Adam Stacoviak] [54:58] It's
[Bryan Cantrill] [54:59] very good. So it is all very, very, very good. Another fair I I would take who would you want in a Silicon Valley spin off?
[Adam Stacoviak] [55:10] Oh, that's easy. Guilfoyle.
[Adam Leventhal] [55:12] Yeah. Easy one.
[Adam Stacoviak] [55:13] Yeah. Guilfoil and Dinesh. Like, I would love this
[Bryan Cantrill] [55:16] like Okay. You you which is like the the I'll write
[Adam Stacoviak] [55:20] it right now. You wanna write it right now? You're cool, baby.
[Bryan Cantrill] [55:26] Yeah. Alright. Is it is there Silicon Valley fan fiction? There must be. I would read Silicon Valley fan fiction.
[Bryan Cantrill] [55:32] Oh my god. I would read
[Adam Stacoviak] [55:33] make it. We should, like, invent it.
[Bryan Cantrill] [55:35] Well, I'm kind of living it a little bit. So, like, I I think I'd rather read it in this case than Ben.
[Adam Stacoviak] [55:42] True.
[Bryan Cantrill] [55:44] I, I also love the, the kid that plays the carver. Do you remember Remember they could they bring in this kid to do the database migration. He's the the the 14 year old good sub character. Yeah. That was pretty solid.
[Bryan Cantrill] [55:55] Doesn't have his Adderall and has a nervous breakdown.
[Adam Stacoviak] [55:58] Or he has too much, and he's, like, freaks out at the end. He's like, too much too much.
[Bryan Cantrill] [56:02] I but I I thought that was, oh my god. Original Adam
[Adam Stacoviak] [56:06] has the car registered my screen name.
[Bryan Cantrill] [56:08] Has is this really fan fiction?
[Adam Leventhal] [56:11] Yeah. It turns out you're not the first person to think of Silicon Valley fan fiction.
[Adam Stacoviak] [56:17] Well, yeah. I mean, it it's not invented here.
[Bryan Cantrill] [56:20] I I may be I yeah. This this is extremely dangerous. We we may need to get
[Adam Leventhal] [56:25] There goes your productivity.
[Bryan Cantrill] [56:27] Yeah. I know. We may need to get back on the page log before I start doing out loud readings.
[Adam Leventhal] [56:31] So it's so let's start
[Adam Stacoviak] [56:32] Let's hypothesize as a different. Let's swap this.
[Bryan Cantrill] [56:35] I think Gil won the Nash would be
[Adam Stacoviak] [56:37] an amazing spin off. I think There we go. Jared would be an amazing spin off. Like, in the in the nursery hall. Yeah.
[Adam Stacoviak] [56:44] Oh. Like no. Not prequel.
[Adam Leventhal] [56:45] Sequel. Okay.
[Adam Stacoviak] [56:47] It was cool. Like, after everything's happened, like, now he's just, like, dancing with old ladies in the nursing home. I don't know.
[Bryan Cantrill] [56:54] I'm state rated. I'm afraid to catch a case.
[Adam Stacoviak] [56:56] That's right,
[Bryan Cantrill] [56:57] man. I'm state raised. There's so many good Jared lines. There's so many good Jared lines. I and I'd the other thing that's looking at it so, so well is, like, Jared will have will say something kind of, like, absurd, and there's this, like, half a beat where they stop on Richard Hendricks looking at him or someone looking at him just being like, what the hell did you say?
[Bryan Cantrill] [57:18] Then it kinda cut away, which I think is just very, it it it's very good.
[Adam Stacoviak] [57:24] Oh, I mean, I could talk about this forever. So You
[Bryan Cantrill] [57:26] can't fall in love with everyone. This is your
[Adam Stacoviak] [57:28] show. I'm not in charge here.
[Bryan Cantrill] [57:30] No. I well, so and on your show when so they had me on your show. The first time I was on your show, you were not there.
[Adam Stacoviak] [57:37] And Jared was like, man, we have got a Silicon Valley super fan for you, Adam. Like, who is it? I ain't can't throw. I'm like Wait. No way.
[Adam Stacoviak] [57:45] That'd be awesome.
[Bryan Cantrill] [57:47] But the way that happened is, like, they thought they they they were they needed you. They honestly, like, I know you did the praise, Jared, you should, but, like,
[Adam Stacoviak] [57:56] they
[Bryan Cantrill] [57:56] I think they were unaccustomed to hosting a show without you.
[Adam Stacoviak] [57:59] And they were,
[Bryan Cantrill] [58:01] and I was definitely like the wrong first one that for them to do without and I mean, they got a little bit, they got a little they wanted to like channel you in absentia, which is a mistake. Mhmm.
[Adam Stacoviak] [58:11] Yeah. You can't do that.
[Bryan Cantrill] [58:13] They asked me a question about Silicon Valley. And I thought for a moment, I'm like, oh, man. I really wish they were asking me about HBO's Silicon Valley, but I know they're actually asking me about, like, Silicon Valley, like, the the the San Francisco Peninsula. So I'm like, well, I know you don't mean Silicon like, HBO Silicon Valley. They're like, no.
[Bryan Cantrill] [58:30] No. We do mean HBO Silicon Valley. And I'm like, excuse me. What? Are we gonna talk with the guy right now?
[Adam Stacoviak] [58:36] Tell you.
[Bryan Cantrill] [58:37] Yeah. I'm like, cracks knuckles. Oh, really? And you could see them both, like, the color drain because I think they wanted to ask me I think the question they had for me is, like, what character resonates with you the most in Silicon Valley or something like that? And I'm like, oof.
[Bryan Cantrill] [58:54] There's a and clearly, like, the only two characters these guys can name are, like, Gilfoyle and Danesh. Like, if I give a name that's not Gilfoyle and Danesh, we are off piste for them. But but, the the name that I actually gave them and my my kids, of course, heard this, and they're like, dad, you're Gort. I'm like, okay. Go to your room.
[Bryan Cantrill] [59:13] Gort being a the the the the the nerdy engineer that Jared defends in, that Jared starts a company with and what season 5. The, but I actually my my answer for them was, was Keenan Feldspar, actually. Even Keenan Feldspar has got some things I also don't like. I feel more more like a Keaton Feldspar than than Richard Hendricks. But I really don't feel like I feel like the show broadly, the characters are not sympathetic.
[Bryan Cantrill] [59:36] That's what makes the show captivating. So I would just like to say that I do not feel a deep resonance with anyone in the show. I just wanna make sure that that is out there and clear. Yeah. You don't buy it.
[Adam Stacoviak] [59:46] I don't I don't know you well enough to know if you're a Keene and Feldspar or not. Like, do you want things and they happen?
[Bryan Cantrill] [59:54] I feel that, like
[Adam Stacoviak] [59:54] But that's how he is.
[Adam Leventhal] [59:55] Do you
[Adam Stacoviak] [59:56] go by serving in Fiji?
[Bryan Cantrill] [59:58] Right. Like, clear your brain? Have you seen this episode? This is a he Adam oh, original Adam. Have you seen can you so Keith Elspar is like a Palmer Lucky like character, which, of course, the the but kind of a Palmer Lucky crossed with, but he but he's a very, he's a very optimistic and, it kinda creates a lot of enthusiasm around them that Richard, disparagingly calls the Kenan vortex, where it's kind of this reality distortion field that I I I was gonna.
[Bryan Cantrill] [01:00:31] But again, I I would like to say that I just for just for the record, have no deep resonance with any single Silicon Valley character, but I do think they're the show is absolutely glorious.
[Adam Stacoviak] [01:00:40] See, he ultimately screws people over though and gets bothered
[Bryan Cantrill] [01:00:42] by the other side of the screen. Right? I know. He he does. He he screws over.
[Bryan Cantrill] [01:00:46] Yeah. That that this is why I mean, this is what makes the show great, but also why, like, you can't like, every one of those characters is ultimately unsympathetic. Every single one of them are. I mean, I guess you could I guess you could argue that, like, Guilfoyle is kind of the truest character because Guilfoyle is basically what it says on the package. But for for everyone else, it was, more or less.
[Bryan Cantrill] [01:01:09] They they they descended at some point and they screwed out screwed over other people. I guess not big head, though.
[Adam Stacoviak] [01:01:15] Big head didn't screw anybody over. Dinesh didn't screw anybody over. He just failed to, like, check the box basically in terms of service. It's actually been pretty a pretty decent CEO if that didn't happen. And, like, you were mentioning Jack Barker early on, like, of the entire story arc, the box was the most successful thing of anything in the entire show.
[Bryan Cantrill] [01:01:39] Yes.
[Adam Stacoviak] [01:01:40] Yet it was the thing that didn't get, you know, all the
[Bryan Cantrill] [01:01:44] praise. I I and I know people want us to call the oxide rack. It's detox signature edition. And we are, I mean, why are we not doing that? Are we I I think
[Adam Stacoviak] [01:01:53] Yeah. You gotta get your signature on there, man.
[Bryan Cantrill] [01:01:55] Yeah.
[Adam Stacoviak] [01:01:55] I'm not sharing it with Banksy. Who's who the hell's Banksy?
[Bryan Cantrill] [01:02:00] I I I also love their, when they when they are offshoring, at Hooley, they are, they they're gonna move to Georgia and kind of the characters around Gavin Belson or
[Adam Stacoviak] [01:02:12] They're so stoked.
[Bryan Cantrill] [01:02:14] Yeah. There's again, Georgia, I could deal with that. Like, kinda, you know, dirty south. I could do that. I was like, no.
[Bryan Cantrill] [01:02:19] What are you talking about? Like, not no. No. Like, Not not not the state. Very well done.
[Adam Stacoviak] [01:02:27] Like, no, no, no, no. We need perks. We need access. That's actually a pretty good sub character. What is his name?
[Adam Stacoviak] [01:02:35] Denpock. Denpock is good. He's a pretty awesome sub character. Maybe it's a manipulator. Wow.
[Bryan Cantrill] [01:02:42] Yeah. Yeah. Yeah. Yeah. It's and it's it's very it's very yeah.
[Bryan Cantrill] [01:02:46] It's just all it's all very good, and I feel everyone should watch it. I know people, like like, don't like to watch it because they they feel that it is too close to home, but I feel very strongly that it is, I I think it is a release to watch it. I think it is also just very, very, very fun. Good. So the, maybe tacking back to the change log a tad.
[Bryan Cantrill] [01:03:10] But I know Adam's like, oh my god.
[Adam Leventhal] [01:03:12] Away from ours are are are are longest second sponsor of all time.
[Bryan Cantrill] [01:03:17] That's right. I pretty much. I would I would allow them to be I oh, that'd be god, that'd be great. I that's hey. That's right back.
[Bryan Cantrill] [01:03:25] You got me right back in it.
[Adam Stacoviak] [01:03:27] I have a serious question. Yeah. Yeah. Mostly for Brian, but Adam OG Adam, you can answer this too if you're this kinda fan. If it came out on 4 k Blu ray, would you buy it?
[Adam Stacoviak] [01:03:39] All 6 seasons. And how long would it take you to push buy?
[Bryan Cantrill] [01:03:44] So I would for sure that you I would actually love would be the any any kind of director's commentary I would love. So I actually do wanna know how they nailed so much. The writers nailed so much that they must have lived. And, like, I mean, I mean, Adam, like, the episode you're talking about where people are pointing to the chair, like, that clearly someone in the writer's room has endured that. They must have.
[Bryan Cantrill] [01:04:09] Like, how
[Adam Leventhal] [01:04:10] Wasn't just the writers like we, Brian, you and I know a bunch of people who consulted on the show.
[Bryan Cantrill] [01:04:14] We do. Yeah.
[Adam Leventhal] [01:04:15] Yeah. We, I mean, we can we can follow the the chain of consequence that that led to some of those things. But how about I mean, isn't that your dream to have been contacted? Like, wouldn't that have just made your life to to be a consultant for
[Bryan Cantrill] [01:04:29] them? It would. It would. You know, we you know, we should have we so Dan Lyon, we do have a I I I I'm gonna, you know, I gotta get Dan Lyon on here.
[Adam Stacoviak] [01:04:37] We gotta go deeper on this, man. We gotta own this.
[Bryan Cantrill] [01:04:40] We do. I agree. I agree. We're sitting
[Adam Stacoviak] [01:04:41] here director's commentary.
[Bryan Cantrill] [01:04:43] But what what we're we're kinda, like, we're we're fanboying and, like, fine, but we act I agree. We actually need to take action, and we actually need to go deeper. I agree. We we we so this is our this is gonna be a resolution coming out of this. And
[Adam Stacoviak] [01:04:55] you are the one who's really famous here, so you got the connections. Like, I didn't work at Sun. I didn't do things at Joanne and start Oxide. I just talking to Mike's. You know?
[Bryan Cantrill] [01:05:05] Yeah. So people are asking if so Jess did consult on the show and what and we'd have to what her what she told me anyway was like, what I they really wanted me for was to make sure they were they really wanted to make sure that the go was all correct. So anything on a whiteboard had to be correct. Anything that was shown on a monitor had to be correct. So they were very persnickety about making sure that the go all compiled.
[Bryan Cantrill] [01:05:31] So that was, so, yeah, she consulted, and I believe that that's what that's what she said. Her her, basically, her her role is, like, I was happy to do it, but, like, they didn't want code review. Yeah. It was code review. It was we it was code review.
[Bryan Cantrill] [01:05:44] Yeah. And I believe, Cliff Moon also, I mean, again, we know a couple people consult with her, and he it was similar. It was like, he was doing, like, whiteboard review to make sure that the things that were on the whiteboard with, like, sticky notes were things that would be and so, like, he had something that was, like, where they were, you know, rewriting something in Elixir or whatever it was. There's a sticky note about it. He's like, that is like that's due to me.
[Bryan Cantrill] [01:06:11] That sticky note, that's my sticky note, and and the the accuracy there. So if you do if you there's a lot of freeze frame fun to be had of. You can you can pause and and look at all their their their agile and their scrumming and their their, their tickets. It's all very good. So it it Adam, is he I just on the change log of pics.
[Bryan Cantrill] [01:06:33] I do. I well, actually, let me ask this. Have you had other guests? How do other guests react to Silicon Valley?
[Adam Stacoviak] [01:06:41] Only a lot of them blanket. Yeah. They like it. Most are apprehensive to watch all 6 seasons. Most have not finished because they're like, it's just too close to home.
[Adam Stacoviak] [01:06:55] And then there's a select few that are my favorites of the world that have watched all of them and they watch it lovingly and understand it's an absolute masterpiece and they they get it. But most, the reason why we have the ding though, right, the ding was not there in the beginning. It's because it kept dropping. Well, the ding originated because I just kept dropping Silicon Valley references in our podcast because it's satire, but it's so true. And I couldn't help but keep just in some way, shape, or form, oh, this is what Gavin Belson did.
[Adam Stacoviak] [01:07:32] Oh, this is what Richard Henderson did. Oh, this is what Guilford said. Or, oh, this is how Dan Meltzer reacted when x or whatever. Like, all these scenarios just kept coming up in people's natural stories when sharing them with us on the show that I'm, like I I kinda kept apologizing. Now I'm just, like, not apologizing anymore.
[Adam Stacoviak] [01:07:50] Like, this is life. Okay? Deal with it. And so Jared, my business partner slash host and an amazing person, we employ break master cylinder basically. Okay.
[Adam Stacoviak] [01:08:00] So break master cylinder
[Bryan Cantrill] [01:08:01] I saw that. Yeah.
[Adam Stacoviak] [01:08:05] They do not work for us full time only exclusively. Very much for hire, so you should check them out and hire them.
[Bryan Cantrill] [01:08:12] Adam, do you know Breakmaster Filanar.
[Adam Leventhal] [01:08:15] No. I don't.
[Bryan Cantrill] [01:08:17] The Yeah. Yeah. Adam, did you get break master cylinder from reply all?
[Adam Stacoviak] [01:08:23] So yeah. That's where I To to some degree, yes.
[Bryan Cantrill] [01:08:26] To honesty.
[Adam Stacoviak] [01:08:26] Yes and no. So learned about Breakmaster Cylinder, the composer artist who's famous now because of their work in and around podcast theme songs, blips, beeps, boops, all those things. And years ago, like, way, way, way back, I'm thinking, like, maybe probably 2017, 2016, sometime around there, I reached out. I I expected to get a hard no. Like, I'm not gonna hear back
[Bryan Cantrill] [01:08:55] from For her.
[Adam Stacoviak] [01:08:56] They they Yeah. I was, like, hey, I would love to have fresh beets that only we own, that you can't get anywhere else, that are based around things we like. We would love to work with you. And I expected to be like just ghosted never talked again, like, no response. Within minutes, break master cylinder responds, I'd love to, let's talk.
[Adam Stacoviak] [01:09:18] Yeah. And so we commissioned them to create the first thing we did which was the brand new theme song for the changelog and it it's, it's really cool. And then, and then after a while I'm, like, we really need this, like, on a regular basis. Can we just, like, give you money each month and you just keep, like, making beats for us? And so now Breakmaster is very much like family.
[Adam Stacoviak] [01:09:45] Like, we just talk all the time. Oh my god. If we have ideas, like so we were just at Microsoft Build. Don't don't be upset about that. A lot of
[Bryan Cantrill] [01:09:54] it No. No. Why why would it be upset?
[Adam Stacoviak] [01:09:56] A lot of it. It wasn't Oxides build conference. It was Microsoft's, you know. I'm like, it's the it's the bad guys. It's the evil empire.
[Adam Stacoviak] [01:10:05] Anyways, and and while we were there, before we were doing the show with with Shonda Person, we did a mic check, and I said mic check check 1212 Mike Mike Mike 5 Mike whatever. And we just kept doing this, and then Shondae jumped in. Then Jared jumped, and he's, like, mhmm. Mhmm. And so in post, I found this clip as I was, like, preparing to edit for this thing and prep it for our editing.
[Adam Stacoviak] [01:10:37] And I pulled it out and I was, like, brake master, see what you can do with this. And now it is like a little thing, like, there's music to it. There's breaks. It's so cool. Like, they took it, remixed it.
[Adam Stacoviak] [01:10:49] And I say they because brake master cylinder is largely anonymous.
[Bryan Cantrill] [01:10:54] Is anonymous. Yeah.
[Adam Stacoviak] [01:10:56] Right. He, she, they, there's no gender. It's just a I assume that 3 year maker was a doctor with a mask. They're not. They're not.
[Adam Stacoviak] [01:11:05] And That's amazing. One of the most amazing human beings ever ever. My respect, my love, and, like family now. So
[Bryan Cantrill] [01:11:16] I mean, do you could you could you intro us to to break master cylinder? Could you I mean, would we could we I mean, we we need, god. I mean, we that'd be great.
[Adam Stacoviak] [01:11:26] It'd be amazing.
[Bryan Cantrill] [01:11:27] Up on top of your
[Adam Stacoviak] [01:11:28] friends if you wanted to.
[Bryan Cantrill] [01:11:30] That is a I don't I don't know if we're ready for that kind of a that is a big level.
[Adam Stacoviak] [01:11:33] I mean, it's a clue that you ask. You just say, Adam, can you help me? And I say, yes. That's just all you do.
[Bryan Cantrill] [01:11:40] Yeah. We are really truly becoming a podcast company that happens to make computers at that point.
[Adam Leventhal] [01:11:44] You know, Brian, we introed our guest 2 weeks in a row and look where we are.
[Bryan Cantrill] [01:11:47] I know it this is what happens. This is why introing the guest was a slippery slope. And next thing you know, we also, break my system. Their work is extraordinary. I mean, it is a really, really good work.
[Bryan Cantrill] [01:11:58] And Thing that break customers do.
[Adam Stacoviak] [01:12:00] I I love hall and notes. There was this there was a a mash up out there. Well, there's there's a story behind the scenes with Michael Jackson and Hall of Notes. And, the the the the music is called or the song is called Billie Jean. You know the song.
[Bryan Cantrill] [01:12:16] I know Billie Jean.
[Adam Stacoviak] [01:12:17] Yes. There's another song called Can't Do. It's no can do. It's been it's called the no can do song from Hall and Oates. And Hall and Oates was at a party and Michael Jackson was at a party and Michael Jackson says to Hall and Oates, the folks who are part of Hall and Oates, hey, you know, I I do my Michael and Jack Michael Jackson impression on something.
[Adam Stacoviak] [01:12:37] I'm not gonna do it here. But Michael says to them, you inspired the baseline on Billie Jean. Thank you so much for like inspiring me. I'm paraphrasing because there's a whole YouTube clip you can put in the show notes out there and I can share that. And so because I'm such a lover of music, I'm, like, we gotta do this.
[Adam Stacoviak] [01:13:00] BMC, can you make us a an an ode to Hall and Oates and Billie Jean? Because Billie Jean's bass line was inspired by Hall and Oates' no can do song. They begin like, if you listen to them back to back and not through the song, you would swear they're the same song.
[Bryan Cantrill] [01:13:17] Oh, that's interesting.
[Adam Stacoviak] [01:13:18] And because of this, like, music history, I'm, like, we need to merge these 2 and, like, show some love to this story. So behind the scenes of our Little Tech podcast is, like, this music depth of Hollow Notes and Billie Jean and this inspiration, and we now have a, a whole song that's, like, based on on this. I think it's called, like I have to look it up. There's a and BMC makes amazing names for podcasts, like, or for these for these songs. Let me find it real quick.
[Bryan Cantrill] [01:13:51] And and these and there are no animus between the Hollow Notes and Mike and MJ for the for lifting the beat, I guess. I I'm just I'm reminded of for for every reason I'm going to to Vanilla Ice v David Bowie.
[Adam Stacoviak] [01:14:07] Oh, yeah. Mhmm.
[Bryan Cantrill] [01:14:08] And have you ever seen Vanilla Ice defend that? He's like, no. No. No. Under under pressure and Isis Baby are totally there.
[Bryan Cantrill] [01:14:16] His is that that that and mine is I'm like, you literally did the same thing twice. I I mean, okay. Look. I'm not musical and but,
[Adam Stacoviak] [01:14:25] Like, sampling is like, if you listen to Eminem, Hi. My name is that whole track there is from a whole separate from the seventies track that is literally lifted. Like, so this is a day whenever sampling was was frowned upon. And so Where
[Bryan Cantrill] [01:14:42] I I
[Adam Stacoviak] [01:14:44] Like, everything's a reality. Right?
[Bryan Cantrill] [01:14:45] How frequently do we reference Paul's boutique on this podcast, Adam? Do we do we do that frequently? Well, you'd tell me if we did that frequently.
[Adam Leventhal] [01:14:51] I think fairly frequently. Yeah.
[Bryan Cantrill] [01:14:52] Fairly frequently. Okay. We have okay. I this is what I was worried about. I'm not gonna say anymore.
[Bryan Cantrill] [01:14:55] But it's like
[Adam Stacoviak] [01:14:56] Mhmm.
[Bryan Cantrill] [01:14:57] Just insert, write your reference to Paul's boutique. And with the, I I my which my my 16 year old bought on vinyl. And I was it was it's a proud proud papa moment. I know. Exactly.
[Bryan Cantrill] [01:15:11] It's like you've got your son is buying c plus plus bucks and is on his is is on his way to go making something himself. Meanwhile meanwhile, my kids are buying the beast of boys on vinyl. Yeah. The grass is definitely greener on this one, I think. This is very, very much, much, much greater in this case.
[Bryan Cantrill] [01:15:30] I think it's, like, actual grass. You know this?
[Adam Stacoviak] [01:15:34] Let's see if this comes through. Okay. Rewind it. So that's BMC's version of it. What he made for us.
[Bryan Cantrill] [01:15:58] That's pretty great. It's called You can hear it, but yeah. You could definitely yeah. That is pretty great. That's pretty great.
[Bryan Cantrill] [01:16:06] Alright. I will details. And the fact
[Adam Stacoviak] [01:16:08] that We split the details.
[Bryan Cantrill] [01:16:11] You definitely do sweat the details. And I
[Adam Stacoviak] [01:16:13] It's all about the details.
[Bryan Cantrill] [01:16:17] But so you also discovered break master cylinder on Reply. Because Reply is where I I know them from, and know their work from.
[Adam Stacoviak] [01:16:23] It
[Bryan Cantrill] [01:16:23] sounds like that's also making
[Adam Stacoviak] [01:16:24] this music for these people that's this, not so much just this good but, like, this thoughtful, I wanna work with somebody exclusively. I don't wanna keep buying royalty free music. We had a, an issue there where well, like, John Deere, I think, was using the same track or, like, Craftsman or something like that. And it's not like those are bad brands, but, like, here's our show trying to be unique. We're trying to be a zebra.
[Adam Stacoviak] [01:16:50] Right? Zebras stand out. Right? The reason why I think that we have been 15 years successful is because we sweat the details. We absolutely love
[Bryan Cantrill] [01:17:00] our developers and love developers. And That is true.
[Adam Stacoviak] [01:17:03] We're just not just podcasters trying to, like, just talk. That's stupid in a way. And we sweat the details of
[Bryan Cantrill] [01:17:11] the language. Original idea. That's what we're doing over here. That's right. And so we
[Adam Stacoviak] [01:17:16] sweat the details and and here you are. You've got, like, music that's, like, being done with, like, Disney had a different track of ours. I'm, like, this is embarrassing. Like, there's nothing special about our music except for we like it and it kind of fits. And so we have literally albums that are successful on Spotify.
[Adam Stacoviak] [01:17:37] We've released full on albums with Breakmaster.
[Bryan Cantrill] [01:17:42] Really?
[Adam Stacoviak] [01:17:43] If you didn't know this, it's news now. Like, yeah, you can go to Spotify, search for changelog, and just listen to I think there's, like, 3 different albums there now.
[Bryan Cantrill] [01:17:52] Oh, but that's that's kind of an interesting crossover for, like I mean, developers oh, I mean, have the, do you listen to muse actually, do you, Adam, I assume you cut code. Do you?
[Adam Stacoviak] [01:18:04] Do I you're asking me if I write software?
[Bryan Cantrill] [01:18:07] Yeah. Right. Yeah. Do you write software?
[Adam Stacoviak] [01:18:09] Should I tell you no or yes?
[Bryan Cantrill] [01:18:12] I don't know.
[Adam Stacoviak] [01:18:12] What do you think?
[Bryan Cantrill] [01:18:13] Do you
[Adam Stacoviak] [01:18:13] think I write software?
[Bryan Cantrill] [01:18:14] I think the answer is yes. Yeah. I see the answer is yes, but maybe not.
[Adam Stacoviak] [01:18:19] Yeah. No. It's a 100% Well,
[Bryan Cantrill] [01:18:20] are you doing that for my benefit now? Now now I'm worried that I put my thumb on the scale. Like, I don't know. I I didn't wanna just get some people, like, you know, I don't know. Alright.
[Bryan Cantrill] [01:18:28] Like, I don't want you don't don't don't be insulted. I didn't
[Adam Stacoviak] [01:18:30] say it was good. I just said I write it.
[Bryan Cantrill] [01:18:33] That's good. No. No. No. No.
[Bryan Cantrill] [01:18:34] But I but when you write software, do you listen to music?
[Adam Stacoviak] [01:18:39] Oh, yeah. Yeah.
[Bryan Cantrill] [01:18:40] If so 100%. What do you listen to?
[Adam Stacoviak] [01:18:44] A lot of synth wave type stuff. I listen to some of our own albums even, like, when I write code. But this is what I
[Bryan Cantrill] [01:18:52] was gonna ask. I was gonna ask if, like, if the change log album is a good thing to to write code to.
[Adam Stacoviak] [01:18:58] Dance party. I would say go to Spotify, search change log dance party, and I dare you.
[Bryan Cantrill] [01:19:04] Change life. Dance party.
[Adam Stacoviak] [01:19:06] Double dare you not to dance when you listen to this. Like, it's gonna change your life. Okay. So that I
[Bryan Cantrill] [01:19:12] I do feel like do you adjust tempo based on the kind of software you're writing? Original Adam, do you do you same original Adam, same question.
[Adam Leventhal] [01:19:22] Do do you not adjust tempo? No. I'm I'm I'm pretty kinda middle of the road.
[Bryan Cantrill] [01:19:27] Do you listen to music? What you listen to music when you're right? Yeah.
[Adam Leventhal] [01:19:30] Yeah. I mean, I'm embarrassed that by what I call music, but I was to it. But I'm, like, on Pandora still, like a cave person. I'm like
[Bryan Cantrill] [01:19:38] I was I was just gonna tell you got nothing to be embarrassed about, and then I maybe you got
[Adam Leventhal] [01:19:42] And then there it was. Then you
[Bryan Cantrill] [01:19:43] Then then now and now it's kind of embarrassed for okay. So why why are you still why are you still on Pandora? That's very
[Adam Leventhal] [01:19:50] weird. Inertia.
[Bryan Cantrill] [01:19:52] Okay.
[Adam Leventhal] [01:19:53] To, you know, I, I don't like change as you know.
[Bryan Cantrill] [01:19:57] So but with Pandora, you don't have much control over what you was doing. Is that changed?
[Adam Leventhal] [01:20:00] But I like have no. I mean, you have some control or whatever, but you. Okay. I sort of.
[Bryan Cantrill] [01:20:05] And so you put on, like, a genre.
[Adam Leventhal] [01:20:07] Yeah. I've been, like, decoding to the same playlist for, like, way too long. And I just do that.
[Bryan Cantrill] [01:20:12] Wait. What's on your playlist? I mean, is this is this too personal? I know we oh, it's not those words.
[Adam Leventhal] [01:20:18] It's all kind of like there's, you know, kind of Moby kind of era stuff. Like, I'm I'm really stuck in, like, 2002 or whatever.
[Bryan Cantrill] [01:20:28] You're being too apologetic right now. There's no you should not apologize for the art that you like to consume. Whatever it is. I mean, we've already we like like, look, Adam has already broke the seal on hollow notes. So it's like, I don't I mean, not not that same hollow notes.
[Bryan Cantrill] [01:20:41] I just don't feel like, you know, I don't I don't I don't think I but I think it's a risk question.
[Adam Leventhal] [01:20:46] I'd like I mean, I'm saying it because, like, I think I should I should spread my wings a little bit, but I just like, you know, when I'm doing my thing, I just I just go back to what's comfortable.
[Bryan Cantrill] [01:20:56] I think it's a well, so I feel strongly that I that music helps me focus. I mean, that's why you're doing it. Right?
[Adam Leventhal] [01:21:05] Yeah. Yeah. Totally.
[Bryan Cantrill] [01:21:07] Like, you're not doing it because you're like, it makes you worse at what you do.
[Adam Leventhal] [01:21:11] That's right. I need more distraction.
[Bryan Cantrill] [01:21:13] And you were just right?
[Adam Leventhal] [01:21:14] Subtle and, like, when you're doing major surgery, what you need is some noise in the background. Yeah.
[Bryan Cantrill] [01:21:18] Yeah. And, Adam, I assume when you're no. Okay. Now, Adam, when you put on the change log dance party, is are you able to code to that, or is that just too much? Is that too dancy?
[Bryan Cantrill] [01:21:27] Is that too up tempo?
[Adam Stacoviak] [01:21:30] Absolutely love the album. I recommend everybody listen to it.
[Bryan Cantrill] [01:21:34] Buddy, can you co do it?
[Adam Stacoviak] [01:21:35] Yeah. Yeah. For sure. It's good. Yeah.
[Adam Stacoviak] [01:21:39] It's it's enough. It keeps you energetic. It's a lot of good stuff in there. I don't know. You should check it out.
[Adam Stacoviak] [01:21:48] I don't know how to describe it. I I honestly, though, I think I can have that track that Richard was listening to when he had his headphones on when he, like, cracked middle out, it was it was opposite to the tip. Right? When he went into that room, whatever track that was, I want that track.
[Bryan Cantrill] [01:22:04] I actually don't really reveal the mute. And it's kinda funny because, like, you know, like, I would say I mean, Adam, what fraction of of developers do you think listen to music when writing code? I mean, I think it's a big fraction. High. I would say high.
[Bryan Cantrill] [01:22:22] Hi. It was I would say
[Adam Leventhal] [01:22:24] in this, like, open plan, you don't get an office dystopia that we've constructed.
[Bryan Cantrill] [01:22:29] Okay. But even, like okay. Okay. But, mister, like, we don't even we're not even returning to the office. You're working the open plan dystopia that you're in is your house and the people, which is literally
[Adam Leventhal] [01:22:37] so much worse. It's like filled with humans and animals. There was a dog barking in the background a second ago for sure. Way worse.
[Bryan Cantrill] [01:22:44] Yeah. And I think it's kind of interesting is that, like, you actually don't know what's going on in, on underneath someone's headphones in terms of, like, what they actually, like, you know, if whether it's it's change log beats or hall and oats or Mobi or, Adam, if I turned you on to loyal corner, have we talked do we talk about loyal corner a lot of the podcast?
[Adam Stacoviak] [01:23:04] We did, actually. Do. Right?
[Adam Leventhal] [01:23:06] Looking up oh, you know what? You mentioned it. I was looking at at some episodes we had done, in our our our Thanksgiving episode for me. Yeah. That nobody.
[Adam Leventhal] [01:23:14] Yeah. Yeah. 0 people have listened to. Just to be clear from the stats, like, you've listened to it. You've listened to it.
[Adam Leventhal] [01:23:19] That's it. Where where you miss mentioned little car.
[Bryan Cantrill] [01:23:23] Okay. This this so this makes sense. Because I was expecting little carter really taken off by now, and but given that my my my mentions of it, but clearly, I mentioned Lil' Connor in a podcast I know I listened to. Lil' Connor, have you listened to Lil' Connor?
[Adam Stacoviak] [01:23:34] Some.
[Adam Leventhal] [01:23:34] It is After the episode. Yeah.
[Bryan Cantrill] [01:23:36] It is I'm it it is outstanding. It is so good. It is so good that my kids acknowledge that it's good. Even though it kinda kills them. Like, no.
[Bryan Cantrill] [01:23:44] That's
[Adam Leventhal] [01:23:46] yeah. Well, that's great.
[Bryan Cantrill] [01:23:47] Great fire.
[Adam Leventhal] [01:23:48] That's very serious.
[Bryan Cantrill] [01:23:49] No. It's really, really, really, really good. I think it's exceptionally good. I think you're really gonna like it. UK hip hop artist, and I just think it's exceptionally good.
[Bryan Cantrill] [01:23:57] But I also think it like, I, because you you do, like, the Spotify does your I guess, no. You're a Pandora. What am I doing this for? Adam, do you listen to Spotify, or are you, like, OG, original Adam here and and using Pandora?
[Adam Stacoviak] [01:24:13] I feel stuck in Spotify because Apple Music is not that good in my opinion. I don't even, like I think Pandora is only used by, like, 5 year olds or something. I'm not sure. I'm just I'm just trying to miss the ad. I'm not just being
[Bryan Cantrill] [01:24:28] kidding. Just joking. Yeah. Well, yeah.
[Adam Stacoviak] [01:24:30] No. My wife will change.
[Bryan Cantrill] [01:24:31] It's a 5 year old. Go play list. It's like 85 year olds, I think, on Pandora.
[Adam Stacoviak] [01:24:36] Yeah. Okay. You think? Touche. Point taken.
[Adam Leventhal] [01:24:39] I think you're both fair. Maybe maybe too
[Bryan Cantrill] [01:24:40] I was
[Adam Stacoviak] [01:24:41] trying to bust you a little bit, but I did I did poorly at the job of busting you. My wife has several Pandora playlist that, like, take her back to an era of her life that was not now, essentially. So I've I was never a Pandora user, except for through her, and I think I'm stuck in Spotify because nothing's tried to unseat it. And RDO So
[Bryan Cantrill] [01:25:04] I I will I will tell you my last day of Pandora was actually when MCA died, Adam. Because when MCA died, I'm like, I I just want to start with and, like, MCA, I feel like I mean, original Adam, don't you feel that that is like a super narrow, generational marker? Like, where were you in Sure. Where were you in MCA died is something that is like, okay. You are born between the years of, like, 1971 and 1980, if you I think, and maybe even this narrower than that.
[Bryan Cantrill] [01:25:38] I don't know. The, but that because I I was it affected me much more than I anticipated, and I just want I'm like, I wanna listen to every BC boys track from the very first I wanna listen to it from license till I wanna go all the way through. And then Pandora's like, no. How about I give you stuff that's like the Beastie Boys? Like, no.
[Bryan Cantrill] [01:26:00] You don't understand. A man is dead. And I actually and I'm I'm I'm in mourning. And so I created a Facebook account so I could log in to Spotify. Because Facebook, that those were the days in which you could only get into Spotify via a Facebook account.
[Bryan Cantrill] [01:26:17] Ugh. Made me do horrific things, MCA. I wish you'd I'd I'd I'd I'd just wish you'd
[Adam Leventhal] [01:26:23] forever ago.
[Bryan Cantrill] [01:26:25] It's a long time ago. Yeah. It's a long time ago.
[Adam Stacoviak] [01:26:28] That's why I'm doing in 2012?
[Bryan Cantrill] [01:26:32] Oh, gosh. I would do. Adam, you remember that. Right? Yeah.
[Bryan Cantrill] [01:26:35] I the the
[Adam Leventhal] [01:26:36] Yeah. I remember the day.
[Adam Stacoviak] [01:26:38] Remember the day?
[Bryan Cantrill] [01:26:39] But you were just like, I'm Pandora. You're just like, you know what? Pandora? I I love it.
[Adam Leventhal] [01:26:42] I already got it's fine.
[Bryan Cantrill] [01:26:43] But it be good.
[Adam Leventhal] [01:26:43] I have I have all those CDs, so that's that's what I did.
[Bryan Cantrill] [01:26:46] I'm over my car
[Adam Leventhal] [01:26:47] with CDs. Like, the other kind of cave person
[Bryan Cantrill] [01:26:50] I was. I will be in my car with my 6th CD changer, and and not to disturb disturbed no further notice. Hey. Fair enough. Fair enough.
[Adam Stacoviak] [01:27:02] That is awesome, man. Alright. Well, the 6 disc changers in cars are tight. It's a throwback to my other shop. Like.
[Bryan Cantrill] [01:27:10] So change log item change log Adam, I've got another question for you. I when people ask you about the podcast and you wanna put like, I'm gonna point you to, like, what I think are just like these are the episodes that are just the embodiment of the change log.
[Adam Stacoviak] [01:27:26] Do you
[Bryan Cantrill] [01:27:26] have kind of a a hot list that you point them to?
[Adam Stacoviak] [01:27:31] We do a show at the end of the year, every single year. We've done it since 2018. So I just point people to those episodes. We call them the state of the log. And so Jared and I summarize what we love.
[Adam Stacoviak] [01:27:45] And I think 2 or 3 years ago, I started to have, like, not just favorites, but then also must listens, which is, like, slightly different than favorites. And Jared makes one of me because, like, I've got this nuanced reason to, like, not just have a list of 5 favorites but also a a list of must listens. So I just point people to those episodes because Jared and I summarize and talk through everything we've loved that year. We bring in this last year, speaking of break master again, this last year, we we took in voice mails from our listeners, and rather than just playing those voice mails, we handed those voicemails to a break master and said do something with these things. And so break master made remixes of the voicemails of people, and they were just phenomenal.
[Adam Stacoviak] [01:28:33] So if you go listen to 5 episode 571, you'll hear a lot of these things. And because we chapter our podcast, you can delve around a lot pretty easily just from the show notes. Yeah. But I would say I'll I point people to those episodes because we kinda do that yearly as a a habit, you know, just to, like Oh. We're we're we're agile, man.
[Adam Stacoviak] [01:28:57] We retrospective. You know? This is a retro, basically, for the entire year for podcasts. And so he, in natural form, just, like, just laid out there. And they've gotten kinda longer and longer.
[Adam Stacoviak] [01:29:08] This most recent one was a 106 minutes, which is lengthy.
[Bryan Cantrill] [01:29:16] We've we've been 4 months.
[Adam Stacoviak] [01:29:17] I think. Yeah.
[Bryan Cantrill] [01:29:18] We've been original Adam, I think this is a very good idea.
[Adam Stacoviak] [01:29:23] I think
[Bryan Cantrill] [01:29:23] we should do this. I love it.
[Adam Leventhal] [01:29:24] I I think it's like, you know, kind of a bookend to the predictions episode.
[Bryan Cantrill] [01:29:28] The predictions episode.
[Adam Leventhal] [01:29:29] You know, maybe close-up close-up the year with, state of state of the, Oxide and Friends.
[Adam Stacoviak] [01:29:34] Oh, there you go. Just go ahead and borrow that. No problem. Here. I'm right.
[Adam Stacoviak] [01:29:38] Oxide and friends and
[Bryan Cantrill] [01:29:39] I'm a big fan. The Oxide and
[Adam Leventhal] [01:29:41] I appreciate this is a this is great affirmative consent. Thank you so much, Adam. This is Rick.
[Bryan Cantrill] [01:29:46] Thank you so much, and I will reap I will and I will hereby rip up our cease and desist to change login, friends. Or Okay. No. I think this so the so it's open source, baby. We're just, I'm just, forking you on GitHub over here.
[Bryan Cantrill] [01:30:02] No. I think it'd be Please do. I I also think that we do predictions at the beginning of the year. I think you should do that. I think I I I love our predictions app, mister Greg.
[Bryan Cantrill] [01:30:10] And so I I love this idea of going and because I I also I love it when we did this as a a single on the metal episode to point people to Oxide and Friends, and I loved that. That was so much fun.
[Adam Leventhal] [01:30:22] That was like our first crossover. The the oxide, oxide and friends on on the metal to let the subscribers know this is where we've been.
[Adam Stacoviak] [01:30:32] This is
[Bryan Cantrill] [01:30:32] where we've been. And this is by the way we're gonna stay. It it mean I it's still, I think, technically on hiatus, and I would do I think we would do another one. I just think that we, it was a it was a casualty of the pandemic, and then we did the Twitter spaces, and Oxide and Friends just kinda became what it is. And now and now it's, but I think we we we may one day do on the metal again.
[Bryan Cantrill] [01:30:59] It it is
[Adam Stacoviak] [01:31:00] Can I, like, inquire more here on the show?
[Bryan Cantrill] [01:31:03] Sure. In terms of, like, why I mean, really, it really is a casualty of the pandemic. We were so so one of the things I like about On The Metal is it is in person in the studio.
[Adam Stacoviak] [01:31:16] Oh.
[Bryan Cantrill] [01:31:16] And I think that this is to your to your point about, like, well, yeah. It definitely the pandemic made it very hard. So, it just, like Anyways,
[Adam Stacoviak] [01:31:25] it's hard anyways even without the pandemic.
[Bryan Cantrill] [01:31:28] Like, Yeah. It's hard. It's a 100% it is. Yeah. I I what I wanna do still is there is a there are these great computer history museum interviews, and I want to, and original, Adam, you've watched a bunch of these.
[Bryan Cantrill] [01:31:48] Yeah. I think. Yeah.
[Adam Leventhal] [01:31:49] In particular with our, our board member, our founding investor, Pierre Lamont has Yeah. Great one. Incredibly candid one. Everyone should go watch that for at least the, let's say, candor.
[Bryan Cantrill] [01:32:01] The candor's the, and Pierre was the first money in the YouTube. And I don't think he realized that this was actually gonna be on YouTube. I think he was because when I when I originally talked about that, he's like, how did you how did you find that? How'd you watch it? I'm like, it's on YouTube.
[Bryan Cantrill] [01:32:17] It's on the Internet. It's like,
[Adam Stacoviak] [01:32:18] oh, okay. Surprised they
[Bryan Cantrill] [01:32:19] did that. I think I would have said different things then. Like, oh, okay. Well, it's definitely on the Internet now. No.
[Bryan Cantrill] [01:32:26] There and there are are, a bunch of, change log item. I don't know if you've seen these. It's a real the computer history museum has done these oral histories. They are extraordinary. They're hard to find because they're only on YouTube.
[Bryan Cantrill] [01:32:38] They've got no podcasting back or forth. So we wanna publish kind of a what I love to do is curate those and publish them on on the metal, Because, I I think it'd be great. So that that's how I wanna revive on the metal a little bit. But I don't know. It's just a I it's not dead.
[Bryan Cantrill] [01:32:56] It's just resting. Just, we're we're It's
[Adam Leventhal] [01:32:59] just a farm upstate, Adam. It's okay.
[Bryan Cantrill] [01:33:02] It's fine. It's fine. It's yeah. Exactly. It's gray.
[Bryan Cantrill] [01:33:08] Still alive.
[Adam Stacoviak] [01:33:09] It's like, can I ask you some questions in about these things beyond what what I've already asked you?
[Bryan Cantrill] [01:33:13] Sure. Goddamn it. I I'm sure you're turning the tables on you, but go for it. Well, I have to. What,
[Adam Stacoviak] [01:33:21] and this is, like, kinda direct in a way. This is a direct and and maybe challenging in a way. So brace yourself.
[Bryan Cantrill] [01:33:29] Embrace.
[Adam Stacoviak] [01:33:30] What what business purpose does Oxide and Friends and On the Mill serve Oxide? Is there a business purpose? Like how do you how do you justify this? Your even your time.
[Bryan Cantrill] [01:33:45] Like, you
[Adam Leventhal] [01:33:45] guys are Talk about on the metal first, Brian, because I think that was I've had different purposes.
[Bryan Cantrill] [01:33:53] I I man, I was I was raised for a for a tough question there. That's a, I
[Adam Stacoviak] [01:33:57] That's a tough question? Okay. Sorry about that.
[Bryan Cantrill] [01:34:01] No. No. No. This is a softball in a couple different ways. Oh, okay.
[Bryan Cantrill] [01:34:04] Yeah. So hard balls.
[Adam Stacoviak] [01:34:06] The
[Bryan Cantrill] [01:34:09] you know what? Actually, god. This is the that's a tough question, and I would say, let me let me that is a tough question. I would certainly entertain no tougher questions. How'd be that?
[Adam Leventhal] [01:34:18] No more evading, Brian. Just answer the man's tough question.
[Bryan Cantrill] [01:34:22] It's not the oh, god. Finally. I if I if I must. I don't handle the truth. Trust me.
[Bryan Cantrill] [01:34:29] Oh, yeah. The so the truth is that actually the I mean, the the truth with On The Metal was always a podcast fan, wanted to do our own thing, and didn't have a company yet. Didn't have had not we were raising. I didn't have
[Adam Stacoviak] [01:34:40] money in the bank.
[Bryan Cantrill] [01:34:41] Early. Couldn't hire people. Couldn't do anything, and the podcast was something we could do. And we started having these conversations, and people are kind of, like, pouring out to us. Like, oh my god.
[Bryan Cantrill] [01:34:51] This is amazing. And I knew and I remember actually, saying to well, Pierre, not a fan of the podcast. I did describe the podcast to him early, and he's just like, that's a huge waste of time, and I hope you're not spending any money on that. Like, we're spending extremely little money on it, because it's just the cost of the podcasting microphones, but I will never mention the podcast to you again. Meanwhile, one of our other investors at the same firm was just took me aside and whispered, podcast is so good.
[Bryan Cantrill] [01:35:21] I love the podcast. So, no, we knew that the podcast would attract people to the company because it's like it's like minds. You know? So I knew we knew it was gonna be, it it was just felt like a total slam dunk to do that. And then, like, they were the conversations were great.
[Bryan Cantrill] [01:35:38] And I think the only thing that was a minus about it was it was a there was actually a lot of prep work, and then there was a lot of kind of post work. And, I mean, this is the the the the minus such as it is, is that it was just like a lot of work. And we, but I missed it.
[Adam Leventhal] [01:35:58] Yeah. Business value was immediate. Like, you hired
[Bryan Cantrill] [01:36:01] The business value is media.
[Adam Leventhal] [01:36:02] You hired me. Like, you hired hired Arian. Yeah. Exactly. Like, the the, like, get the name out there, tell people what
[Adam Stacoviak] [01:36:07] you're
[Adam Leventhal] [01:36:07] doing, and people started showing up.
[Bryan Cantrill] [01:36:11] Yeah. And and my prediction was we are gonna release this podcast. Someone who we do not know, who's not in our social network, is gonna present themselves to us because they're gonna listen to this conversation with Jeff Rothschild. Extraordinary conversation. Amazing technologist.
[Bryan Cantrill] [01:36:27] The, the it was founder of Veritas, was truly the first analyst at Facebook, and just an extraordinary person. And I know that, like, the that that was our first episode we're gonna drop out there. We did it when we announced the company, and someone's gonna listen to this podcast episode that they're gonna show up. And I don't know when it's gonna happen, but I know it's gonna happen. And it happened within quite literally hours of us dropping it.
[Bryan Cantrill] [01:36:51] And, Arianne was asking for an intro through a mutual friend via LinkedIn, and he and I are going back and forth on LinkedIn, and, he became a very early oxide employee. So it was to answer your question, it was very early. It was recruiting. We also had the the the problem of, like, this is a big build, a big long build. How do you keep, like, customers entertained while you're while you're waiting for this thing to come out.
[Bryan Cantrill] [01:37:18] So it was kind of a useful thing for that. And then on the metal was a victim of the pandemic, and, but I really missed it. And I wanted to do something that was, like, lighter, and then Twitter Spaces came along. And and original Adam, I talked to you into Twitter spaces, so I wouldn't die alone. And I'm very, very grateful, and it was great.
[Bryan Cantrill] [01:37:41] I think the one thing we missed from Twitter spaces that we don't have quite as much on Discord is, like, the the in Twitter spaces, there was no chat. So if you wanted to say something, you had to, like, say something, which was mixed. It wasn't always great, but we do I think, Adam, I think it's fair to say that you and I both missed that element of it.
[Adam Leventhal] [01:37:59] Yeah. That that was a nice part of it. Like having it, you know, more call and show.
[Bryan Cantrill] [01:38:03] Yeah. But the but and then, you know, from there, we, it but it's also been huge to have a chat, which Twitter spaces did not have. It was a big pain in the ass. But but from there, we've been able to it's been it's super light investment from our perspective. I mean, Adam, you do heroic work on the post processing, but it's not that bad.
[Adam Leventhal] [01:38:24] I mean, the the the bigger toll is, like, the marital karma that that Yes. As the show goes long. But, like, that that is the base extent for me.
[Bryan Cantrill] [01:38:33] Right. As Adam looks at his watch at 6:38 local time. Right. Like, tapping the watch.
[Adam Leventhal] [01:38:38] But then the the the right. Just very subtle hint to slide in there, Brian. But, you know, the value for us has been like continuing in terms of recruiting. But then it's been an amazing vector for the team to, like, talk about their work.
[Adam Stacoviak] [01:38:55] And I
[Adam Leventhal] [01:38:55] think people. Yes. I think people both get nervous about it, but then also love, you know, being able to pull up the microphone and talk about what they've been doing. You know, some colleagues talk about our storage subsystem. I told them, don't worry.
[Adam Leventhal] [01:39:08] Not that many people listen to it. It's our 3rd most downloaded episode, unfortunately, for them. But, it's been that's been great. And then I, you know, I said to folks, like, well, geez, like, we're not really expecting customer leads to come in through this, but then it turned out, like, I've got some conference. I got pulled into some customer leads.
[Adam Leventhal] [01:39:27] They have not closed, but, like, certainly, customers and prospects are listening and, like, they, you know, like the show and, like, what they hear about the product when we do talk about the product. So it's, you know, it's it's relatively cheap and, serves a bunch of purposes. Yeah.
[Adam Stacoviak] [01:39:45] I mean,
[Bryan Cantrill] [01:39:45] when I was at Red Hat Summit, and, people were I mean, virtually everyone's come up to the booth saying how much they love the podcast. I I love the podcast even the one on baseball. I'm like, you don't have to say even the one on baseball. You can just say hello to the podcast. You don't actually have to the, Oakland Ballers, by the way.
[Bryan Cantrill] [01:40:08] The home opener tomorrow night. Very, very excited about that. That's a great episode. So we yeah. It's been fun.
[Bryan Cantrill] [01:40:14] Adam, to answer your question. It's been fun. It's been super easy because it's very light lift. We just don't bother. One thing we we were doing with Audible is, like, we were having it, like, sponsored by ourselves, but, it it which ended up being not not not a good idea.
[Bryan Cantrill] [01:40:36] So we had just, like, the same ads over and over.
[Adam Stacoviak] [01:40:38] Mhmm.
[Adam Leventhal] [01:40:39] That I thought those
[Adam Stacoviak] [01:40:40] were You shouldn't have ads. I don't know.
[Bryan Cantrill] [01:40:43] What's that?
[Adam Stacoviak] [01:40:45] You shouldn't have ads in your own show.
[Bryan Cantrill] [01:40:47] No. No. No. We don't have ads. We we are I mean, it's like, you know, it kind of is the ad, sadly.
[Bryan Cantrill] [01:40:51] This whole thing is an ad more or less. I mean, but it's just an ad for, you know, the, like, yeah. Look. We're a podcasting company that makes computers. Adam, did you see that the I I because I was asking if people thought of of us as a hardware company or a software company.
[Bryan Cantrill] [01:41:03] Brian Steel Did you see that? Pretty sure you're
[Adam Stacoviak] [01:41:05] like responded.
[Bryan Cantrill] [01:41:05] A a pod podcasting company that actually makes computers. That's true.
[Adam Stacoviak] [01:41:10] That's fair enough. What was my response? I did respond to to that in some way, shape, or form.
[Bryan Cantrill] [01:41:16] Now all all of this said though, I I think that in especially after my medal up. Yeah.
[Adam Stacoviak] [01:41:20] I was trying to reference on the medal. I said medal up. Mhmm.
[Bryan Cantrill] [01:41:24] In response to
[Adam Stacoviak] [01:41:25] what do you think? Yeah.
[Bryan Cantrill] [01:41:26] What do you think we do? I was like, just meddle up. I mean, the answer is that we actually are. We we we are we are truly hardware and software. The actual answer.
[Adam Stacoviak] [01:41:34] I think it the only question is, like, there's something special here with, you know, this show, Oxide and Friends. Like, it's cool that you sort of, like, pull back the layers and just chill. There's an authentic thing that happens when you podcast. Like, podcasting isn't cool just because you get on a microphone. It's because you become it's a real conversation.
[Adam Stacoviak] [01:41:56] It's an authentic conversation. It's not canned or scripted, you know, and that you can can unscript it a bit more. It's so powerful because of those reasons. And
[Bryan Cantrill] [01:42:09] in a lot
[Adam Stacoviak] [01:42:09] of cases, it's unsensoryable. Right? Like, you have control over this in a lot of cases, like, maybe Apple can drop you from Apple Podcasts, but, like, what are you gonna do? Right? You're not gonna, like, upset them to that point.
[Adam Stacoviak] [01:42:20] There's no reason to censor it. Right? You can talk like you did on the show with me badly about your personal experience with Dell and one of the reasons why you created this company. You know, on your own, you can do that and no one's gonna stop it. Like, Michael Dell cannot stop that conversation.
[Adam Stacoviak] [01:42:38] It can be true. You could be a threat or a looming threat and there's nothing anybody can do about that. To me, that is the coolest thing. You have such a opportunity to like double down on it.
[Bryan Cantrill] [01:42:56] Are you asking for that? Are we are we wait a minute. Are we waiting? I I I I'm gonna get my shit. Anyway, I was when we talked about you should.
[Adam Leventhal] [01:43:03] Because we got an album. Are we ready to drop the album? I'm just
[Bryan Cantrill] [01:43:05] kidding. Exactly. Is this the are we gonna make a movie? Are we making a movie about Oxeye? Because that's what I that this is the we we we've been we've been waiting for this moment.
[Bryan Cantrill] [01:43:16] We're ready to fill with these I I I've often said that, like, oxide. Oxide is like a muppet heist movie directed by Quentin Tarantino. I feel it's like the analog for Oxide. I feel like I'm, oh, I'm ready for all that. Yeah.
[Bryan Cantrill] [01:43:32] Well, that is Adam, it has been great to have you here. This is, you are a huge friend of Oxide, and we I I I loved being on the change log. It was great to get a bit of the I'm I'm gonna go into some of these deep cuts on change log. I wanna go back to that conversation with Matt for sure and some of these old change logs. I did see I did tweet my out myself in the pipe hyper sure, by the way, just so you
[Adam Stacoviak] [01:43:58] know that. I did see that. Yeah. I see that in the
[Bryan Cantrill] [01:44:01] channel now. Yeah.
[Adam Stacoviak] [01:44:02] That's cool. It's it's Nice face too. You're like, this is me. Check me out, pied piper.
[Bryan Cantrill] [01:44:06] That is what, my wife calls line mouth. You're getting line mouth, which is my way of expressing dissatisfaction. So I'm I'm dissatisfied that I'm having to show you my my my Piper shirt.
[Adam Stacoviak] [01:44:19] But It's a decent microphone you got there, though. I like that mic.
[Bryan Cantrill] [01:44:22] It is. Yeah. You know? You're like, where where was this? Put another change log.
[Bryan Cantrill] [01:44:25] I know. I know. This is our our little podcast studio.
[Adam Stacoviak] [01:44:27] I know. We needed a better mic for that one for you. I was I was disappointed seeing this photo now and knowing what I got. I I'm disappointed. Sorry.
[Adam Stacoviak] [01:44:36] It's okay. It's okay. Well, I appreciate y'all have me on here. You know just so I can get it in audio one more time Yeah. You should double down.
[Adam Stacoviak] [01:44:44] On the metal there was something very special there and Alright. Not to do exactly that but a version of that and a version of this slightly more produced. It's funny.
[Bryan Cantrill] [01:44:56] Is this this is an intervention. This whole goddamn thing is an intervention. And I like the way Well, I'm here to say about types of stuff that'll work. I knew it. I knew it.
[Adam Stacoviak] [01:45:03] A couple of the sponsors. And I'm here to sell you on, like, working with me in some way, shape, or form to level up.
[Bryan Cantrill] [01:45:09] Alright. I I'm sorry.
[Adam Stacoviak] [01:45:10] That's the whole show.
[Bryan Cantrill] [01:45:11] God, you are good. You are good. This this has been this has been a sponsored episode sponsored by you. You're, the you're you're on it. Alright.
[Adam Stacoviak] [01:45:19] Yeah. Calls you and buys all all outside racks, you'll be like, you're so good.
[Bryan Cantrill] [01:45:25] Yeah. No. I like it. Alright. I do like it.
[Bryan Cantrill] [01:45:26] I like these are good ideas. I definitely the brake master cylinder is just I the the fact that
[Adam Stacoviak] [01:45:31] Make it happen.
[Bryan Cantrill] [01:45:32] Like, we can
[Adam Stacoviak] [01:45:33] touch base. It's awesome.
[Bryan Cantrill] [01:45:34] It's amazing. Yeah. Alright. Well, hey.
[Adam Stacoviak] [01:45:37] Is phenomenal.
[Bryan Cantrill] [01:45:39] Thank you. Thank you. Thank you. Thank you for coming. Thank you for that very thoughtful conversation.
[Bryan Cantrill] [01:45:43] That was a ton of fun, and I'm looking forward to, being back at some point, having you back at some point. But, truly, we are ChangeLog's friend, and you are Oxide's friends. It's great to great to hang out with you. I love
[Adam Stacoviak] [01:45:59] it, man.
[Bryan Cantrill] [01:45:59] And for developers, everyone to which if you haven't checked out the changelogs, start with something I'm I'm gonna go back to. So because I've missed definitely some of these wrap up episodes. I'm gonna go check them out. I love that idea of, like, going to those wrap up.
[Adam Stacoviak] [01:46:11] A lot of good waypoints in there. Yeah. Knew it. I say the greatest hits for, like, the last 7 years.
[Bryan Cantrill] [01:46:16] I just I I love it. I love it. Alright. Yeah. We're we're gonna go check it out.
[Bryan Cantrill] [01:46:20] Thank you so much for for joining us, Adam. Hope that the, good luck on the the the the, the the fam getting the fam back on the in your your your open office plan there at your
[Adam Stacoviak] [01:46:33] house.
[Bryan Cantrill] [01:46:34] Alright. And we are gonna be, we may be on hiatus here for a couple weeks. I'm I'm gonna be I got some weeks on the road. So, stay tuned, but, we'll be back in not too long. Alright.
[Bryan Cantrill] [01:46:47] Thanks, everybody. Take care.