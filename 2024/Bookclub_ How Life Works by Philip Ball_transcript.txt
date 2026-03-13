[Bryan Cantrill] [00:00] Alright. Adam, you there?
[Adam Leventhal] [00:02] I am. And, are you joined with by Greg?
[Bryan Cantrill] [00:06] I am joined by Greg Cost. Greg, welcome to Oxide and Friends.
[Greg Cost] [00:11] Thank you, Brian. Adam, pleasure to meet you.
[Adam Leventhal] [00:14] Yeah.
[Bryan Cantrill] [00:14] You you know, you've got a good, like, radio voice, Greg.
[Greg Cost] [00:16] Thank you.
[Bryan Cantrill] [00:17] I think so. Yeah. I'm not I don't I I know I'm I'm sounding surprised here. I really don't sound surprised.
[Greg Cost] [00:21] Someone said that a couple weeks ago about me. I I had not heard that before.
[Bryan Cantrill] [00:25] I don't know. We're gonna Take it as a compliment. Your the the your career as a as a podcaster could be launched right here on Oxide and Friends. This could be where it all begins.
[Adam Leventhal] [00:32] Right where you're discovered.
[Bryan Cantrill] [00:34] It's where you're discovered. Exactly. So, Adam, I was at Red Hat Summit, week before last. And Right. I you're like, wait a minute.
[Bryan Cantrill] [00:45] Are we talk what? Where are we right now? No. We're we're gonna get to the on topic. Was on at Red Hat Summit and was really great how many folks were coming up to me having listen being big listeners to the podcast.
[Bryan Cantrill] [00:57] We gotta
[Greg Cost] [00:57] That that's great to hear.
[Bryan Cantrill] [00:59] That's that's really fun. In fact, someone said, you know, I love the podcast even the baseball one. And I'm like, you you don't have to phrase it that way. You don't have you don't have to say even the baseball one. You can just say, I love all of the podcast in those totality.
[Bryan Cantrill] [01:12] You don't need to take our weirdest episode. So I am I am looking forward to someone in the future being like, I love the podcast. Even the crazy biology book, I loved. So I,
[Greg Cost] [01:24] I'll try to keep it second weird.
[Bryan Cantrill] [01:25] Yeah. I think you'd be we you know, we had, Greg, we had the the the co founders of the Oakland Pollers on here. Oh, cool. Yeah. It was pretty it was great.
[Bryan Cantrill] [01:34] I thought it was I thought it was great. But some people thought it was, weird, but it was not weird. I thought it was terrific. So that was a lot of fun. But the so the origin of this one and Greg I was explaining this to you a little bit before I got started is that we, have, through kind of the life of Oxide and Friends, which started out as a Twitter space and then moved to Discord.
[Bryan Cantrill] [01:54] We had some people who are who wanted to, like, let's go read a book together. Let's get kind of folks that are in the community. Let's read a book together. That was exciting. People may never ask that again.
[Bryan Cantrill] [02:05] We'll see. We're gonna say we're gonna say this may be we may be one and done on this. People will be like, okay. Well, we asked that and we saw what happened.
[Adam Leventhal] [02:11] Ask an answer. Right. Gotcha.
[Bryan Cantrill] [02:12] Ask an answer. Never know again. I think they're like, no. I would think I was thinking more like a like a kind of a book in the computer industry or a history of the computer industry or something that's a little more on brand for you too. Adam and I have both read a lot of books on on the industry and on computing and so on.
[Bryan Cantrill] [02:28] But I wanted to get a little further afield, and I wanted to do something that would be a bit more of a challenge that we could all kind of motivate one another to get through, and something that would be, kind of out of our wheelhouse. So the the folks that are certainly Adam and me, but a lot of the folks that are kind of the the oxide demographic, are all in computing. Right? So we're a a lot of computer scientists, a lot of software engineers. And I'm sure we've got I know we've got some folks that are also, biologists as well.
[Bryan Cantrill] [02:56] But but but they are 1st and foremost, we're really computer scientists. And, really, I I saw that that, my friend in particular, Gaurav Venkataraman, had and I have you met Gaurav, Adam? I don't I don't know. I haven't. Oh, man.
[Bryan Cantrill] [03:12] Gaurav's amazing. So I met Gaurav years ago at, when he and I were in an event together and really fascinating technologist, out of the UK. And I saw him tweet out a a review of this book. I think it was Dennis Noble's review of the book. But I still can't read because it's in nature behind a paywall.
[Bryan Cantrill] [03:30] So I I've got for all I know, that review of the book is, like, no. This is like it. This is a total stinker. Don't read it. But the, he had in particular, Gorav was tweeting that, like, this is a really interesting book, and this is kinda capturing, a lot of the pulling together a bunch of different ideas and new ideas in biology.
[Bryan Cantrill] [03:48] So that's kind of the backstory here for How Life Works by Philip Ball. And then, Greg, I I kinda sweet talked you into joining us. I'm very thank you very much for You're
[Greg Cost] [03:59] welcome. Oh, I I'm a card carrying biologist and love explaining and to be presumptuous for a second, and it was a it was a fun read and look forward to talking about it.
[Bryan Cantrill] [04:10] So, Greg, why don't you give us a sense of a kind of a focus, a sense of your background? Because I know this is obviously much of this is obviously not new for you. This is what you've been doing for a living. Sure. But could you describe a little bit kind of, your background, how you got into, into microbiology and and when kinda what you're what you're doing now?
[Greg Cost] [04:29] Yeah. Sure. Absolutely. So I have, started out with the bachelor's in chemistry, and then, decided I like the squishy part of chemistry more. And so, ended up when I was still a teenager, I was starting to work in a biology lab.
[Greg Cost] [04:42] Founded it it was really the problems I cared about, understanding how the chemistry of life worked. Right? And so, ended up going to grad school
[Bryan Cantrill] [04:50] in that. So you were as a teenager working in a lab and, like, hands on? Yeah. Okay. Yeah.
[Greg Cost] [04:58] Making DNA and all.
[Bryan Cantrill] [04:59] Making DNA. Okay. And that Pretty cool. You get
[Greg Cost] [05:01] your little white fluffy lip.
[Bryan Cantrill] [05:05] That's awesome. Pretty cool. And I and how did you get associated with the lab? I mean, was it
[Greg Cost] [05:10] there were, at my chemistry department, I'm in university, there were a couple other people who were also biochemically, you know, granted. And, they were talking about the role. And I said, that sounds like something I might be interested in. And I, you know, I want to explore there. And they said, well, we actually have a job for, as a lab aid.
[Greg Cost] [05:30] That was my first job. I basically you know, those petri plates that you grow bacterial colonies on, the round disk things with auger? I I made those for everybody, and I I autoclaved pipette tips and prepared tubes and like all the grunt work. Right. But, it's a great place to get your start.
[Greg Cost] [05:48] Right?
[Bryan Cantrill] [05:49] Well, totally. And I assume that I mean, for at least for me coming up computer science, like, the lab work was so such an important part of my own education. Like, you know, you kinda get the okay. I get how the system is supposed to work. But it's, like, actually the lab work of making the thing is, like, really connecting for me.
[Bryan Cantrill] [06:02] I it's I've gotta be different. Right? Yeah. Yeah. You you you
[Greg Cost] [06:06] Biology and I mean, you can't see molecules with your eyes. Right? So it's okay. Like, as we saw a lot of things in science, it's very theoretical. You have to use your imagination.
[Greg Cost] [06:14] Right? But actually doing it is a completely different thing than thinking about it. And so, yeah, definitely had a great experience, as an undergrad. Went to grad school. I ended up doing a postdoc, moved here to the Bay Area.
[Bryan Cantrill] [06:30] And so and then when are you kinda coming up in terms of so you're doing the the these kind of DNA based experiments. When is this kind of because I think it's Sure. Sure. That means so much of the backdrop of this book is kind of the the human genome project and the kind of the hubris that may have come around it or the h g p. So
[Greg Cost] [06:43] Yeah. Yeah. So I started in, 1993.
[Bryan Cantrill] [06:47] Okay.
[Greg Cost] [06:47] So 30 years ago. It had been a while. That's that's when I had that first lab aid job. I went to grad school in 995 to 2001.
[Bryan Cantrill] [06:57] Okay. So right when the Human Genome Project is, like, oh, I go Absolutely. Bull's eye
[Greg Cost] [07:01] for this. Literally every day or maybe it was every week, they would dump another 10 megabytes of DNA sequence onto the public server. Wow. Everyone to see. It was, like, the first time ever that it was revealed.
[Greg Cost] [07:14] Right? It was a pretty amazing time. And, you know, actually, at the time, I decided I one thing that people found when they looked at the genetic sequence, and this has been known before the sequencing, but there are a lot of transposons, like, a lot of these repetitive DNA elements. You know? Right.
[Greg Cost] [07:33] And I kind of made the offbeat choice that I wanted to study everything that wasn't a gene. Really?
[Bryan Cantrill] [07:40] And so and this was like the because I don't think this term merit to mention in Ball's book, but I definitely remember the the term junk DNA. Yeah. Being 1. And it feels like in in reading this book, I'm like, that term is not aging well.
[Greg Cost] [07:54] It's a little pejorative. It feels very pejorative. It's, in some ways, it's not terribly wrong. But, I mean, you could probably delete a lot of it, and we'd all be fine. We'd never be the wiser.
[Greg Cost] [08:08] Right? But, you know, I think evolution doesn't waste anything. And so if you have this DNA sitting around and and there it it finds a function
[Bryan Cantrill] [08:18] Yeah.
[Greg Cost] [08:19] Over time because, yeah, that's how it works.
[Bryan Cantrill] [08:24] So you got into these transposons and understanding their mechanism in terms of, like, what they were and what was kinda known at the time about transposons?
[Greg Cost] [08:33] Maybe they were discovered, probably in the forties by the woman named Barbara McClintock. Right? And, that's how you see in an era of maize corn. Right? The the kernels are all different colors and have stripes.
[Greg Cost] [08:45] It's act that coloration pattern is actually a result of transposition. That's actually something mentioned in the book. Right? And I think those are the first transposons that were discovered. And then, you know, people, people just looking at, like, melting and annealing of DNA strands realized that there were some weird things going on, and it couldn't all be random and that there were repeats.
[Greg Cost] [09:07] And so that was that work was done in the seventies. The first DNA sequencing is probably the eighties, really the late seventies, early eighties. And, these things were they're extremely common, and so they were discovered relatively early on. Probably about the one I studied is probably about 17 or 18 percent of the total human genome by sequence.
[Bryan Cantrill] [09:28] It is is 17 or 18%.
[Greg Cost] [09:31] Yeah. And it's probably actually caused the synthesis of about 4, 5%, close to 50% of our genome.
[Bryan Cantrill] [09:40] Wow. So this is significant.
[Greg Cost] [09:42] Yeah. And and, you know, the the the bizarre thing is at the time, I was the most academic possible thing you could imagine studying. Right? But now, actually, the company I work at called Addition Therapeutics, we're actually using very related retrotransposons in order to try to do gene gene engineering and try to to cure human disease. I should say, by the way, that I'm I'm here in my personal capacity, not in my employer.
[Greg Cost] [10:06] But, yeah. Oh, I
[Bryan Cantrill] [10:08] was gonna reveal that Addiction Therapeutics is our first sponsor of oxide. We're trying to sorry. Okay. I got some misunderstandings here about the, 8 okay. And then when you say reverse transposons, what's the reverse in there?
[Greg Cost] [10:22] So some, some some transposons are what are called DNA transpo bonds. And that's sort of the, well, the normal type of transpo. So a segment of DNA will make a protein. That protein will cut out that DNA and then plop it down somewhere else. The type of transposon
[Bryan Cantrill] [10:41] But these are not genes. Right? Oh, sorry. Is everything complicated?
[Greg Cost] [10:45] People call them elements because they have their own agenda. But strictly speaking, they are they are they are have all the things that genes have. Right. So I think of them as genes, but a very odd class of
[Bryan Cantrill] [10:59] Okay.
[Greg Cost] [11:00] They're they're not commonly thought of as benefiting us, let's put it that way. So they're sort of like interlopers. That's that's that's the language that's used. It's fine.
[Bryan Cantrill] [11:11] But it feels like a only a small upgrade from junk, frankly. It's like, hey, good news. You're no longer junk. You're an interloper. It's like, hey, listen, pal.
[Bryan Cantrill] [11:18] Like, I, feels like a okay. So
[Greg Cost] [11:21] And actually, in in, recent discoveries, like, a lot of these transposons, they may actually have a role in aging and disease. Like, they end up causing a, a sterile inflammation. Like, our our immune system gets kind of turned up and up and up as we age. Nothing good comes from that.
[Bryan Cantrill] [11:39] Interesting. Yeah.
[Greg Cost] [11:39] Yeah. Anyway, sorry to answer your question, retrotransposons are, kind of the weird category in that, they make an RNA, like, coming from the DNA, and that's something that like like in a normal gene. Right? Instead of that RNA, being so sorry. The RNA is turned into a protein in the same as the the normal equation.
[Greg Cost] [11:59] But then, what's and then what's replicated actually doesn't stem from DNA being replicated, but rather the RNA, gets is the substrate for the replication. So there's Oh, interesting. Transcriptase that turns out RNA back into DNA, and in the process, actually, integrates it into.
[Bryan Cantrill] [12:19] Okay.
[Greg Cost] [12:19] It has to do with just the mechanism.
[Bryan Cantrill] [12:21] The the mechanism. Okay. So the reverse bit is the is is just a an indicator of the mechanism. Okay. So okay.
[Bryan Cantrill] [12:29] So given the backdrop of all that, and so you're obviously you're a practitioner. You're you've been doing this for 30 years. You've been very much involved in what we know from a science perspective and how we can use that to benefit humanity. So maybe that's a good segue to the actual to the book. Yeah.
[Bryan Cantrill] [12:48] The actual book. Yeah. Yeah. The actual book. So, with alright.
[Bryan Cantrill] [12:51] So what did you make of the book?
[Greg Cost] [12:54] Yeah. Great question. So I have I because of that background, I think I have a third perspective on the book. Right? A lot of the biology wasn't new to me.
[Greg Cost] [13:05] And so I had to think about, you know, I think that I was called upon to take the perspective of someone who didn't actually already know some of the details going in. Right? Which, of course, most people don't. Right? And I think the book is definitely written from the perspective of someone who, you know, has a good, say, college level education in biology.
[Greg Cost] [13:27] And, you know, you learn that there's DNA, the DNA makes makes RNA. The RNA makes proteins. Proteins catalyze chemical reactions. And then all that complicated chemistry, like, you might see these big wall charts cycle. Right.
[Greg Cost] [13:43] All that stuff happens in some big symphony and, you know, life. Life.
[Bryan Cantrill] [13:52] You know, I think
[Greg Cost] [13:54] a lot is is detailed in the book. A lot of what has been discovered in let's say that's a that's a very, I would say, big fifties, sixties model. Right. Right. And a lot of well, science has progressed since then.
[Greg Cost] [14:09] Right. And so I think a lot of what's discovered is that, you know, it's a little bit more complicated than that. Right. There are notably, I think, alternate forms of information that are inherited, not just and A. Yeah.
[Greg Cost] [14:23] That's a very and I'd say a very surprising discovery. It's that was the big one for me. Is, the big thing I think is notable for an outside person. Right? I think, you know, I think he makes a point very, very clearly in the book.
[Greg Cost] [14:40] Like, if if you just had the genome and you put it in a bunch of soup, you wouldn't suddenly have life. Right? Life is more than the the DNA. Right? So it has to exist in a context of information and organization that allows an energy, that allows the plans in that DNA to be brought forth.
[Greg Cost] [15:00] Right? And, so, you know, the book goes through many different interesting examples of how things are a little bit more counterintuitive than we might expect. You know, so I have some more more critical thoughts.
[Bryan Cantrill] [15:15] You're right. Yeah. Yeah. Definitely hear those. I think that the yeah.
[Bryan Cantrill] [15:19] I mean I I think I mean part of what is so interesting about this book is I mean this book ultimately is about metaphor to me and about the, you know, the the effectiveness of metaphor and especially the metaphor of computation. And, you know, do we and certainly, I mean, god, we've I feel well, Ball does it repeatedly in the book himself even though he tries, I think, not to about using a it's so tempting to use a program text as a metaphor for DNA and vice versa that, like, oh, this is like a stored program computer. And, like, look, I've got this instruction sequence, and the instruction sequence happens to be nucleotide base pairs. And it's just like software. And I I think it's like, I I that metaphor is super tempting and understandable and also really misleading in a bunch of very kind of deep ways.
[Bryan Cantrill] [16:14] Because it's the I mean, my like, one of my major takeaways of this the gamut. Now this is like in the not deep thought department. But the the machines that we engineer are absolutely nothing like biological life. They are at Yeah. That they are at the opposite end of every conceivable spectrum.
[Bryan Cantrill] [16:38] And, you know, I loved that, you know, Michael Olsen, Adam, sent me a line that I loved was as he was getting into the book. And he's like, these are like programs that only operate on side effects. So Interesting. Which I thought was a really interesting way for a software engineer to think about it. So Yeah.
[Bryan Cantrill] [16:55] Like, we are spoiled stupid in software because the instructions that a computer executes are very deterministic.
[Greg Cost] [17:06] And They were written by a human who They are written by a human. Assumption. Yeah. That makes sense.
[Bryan Cantrill] [17:11] A 100%. And we love to, like, treat them as, like, biological because they're they represent complexity that we don't understand and and so on. And we love to kinda complain about the level of complexity and, like, look, like, for, like, decent reason, it is it is remarkably complicated that you've got, you know, got a laptop here that is executing billions of instructions per second. They're ultimately are all synthetic, but it would be actually a pretty complicated exercise to describe every single instruction that the thing is executing as part of being in this discord. And it's all adding up to like, but as complicated as that is, it is like nothing.
[Bryan Cantrill] [17:51] Absolutely nothing. I was just like, I don't matter. You must have felt the same way. I'm just like, where you're just like getting just the humility that you feel on the complexity of life. It's just not again, it's like the and it's the kind of the open question is, like, does the metaphor serve us well or not?
[Adam Leventhal] [18:14] And You're talking about fishing in the pool of mechanical metaphor to explain biology. Yeah.
[Bryan Cantrill] [18:20] That's right. That's right.
[Adam Leventhal] [18:21] Agreed. It's a it's a weird misfit for sure. And I think I was steeped still in the, like, the late nineties human genome project hype, and had not even kind of, taken up biology to understand the distinction, the the fact that the genotype had many different phenotypes that it could produce. And, I mean, I think sort of vaguely aware of that, but not the degree to which that was the case. That even things that we view as, complications or or errors in, development.
[Adam Leventhal] [18:56] Yeah. That's just like one of the potential expressions and uncommon, but not necessarily something that something that literally is written in the DNA, in the genome.
[Greg Cost] [19:07] I I think everything is
[Adam Leventhal] [19:09] sorry. No. Please go ahead, Greg.
[Greg Cost] [19:11] No. It's because I think, the the instructions are probabilistic. Right? And that's that's how things work, especially at the molecular level. Right?
[Greg Cost] [19:19] The machines are all the machines, but they're they have to operate via very different rules, and they have to account for noise and all sorts of stochastic effects. And, I mean yeah. Absolutely. Developmental biology is it's it's a landscape, and, like, things are guided towards one outcome. But, you know, obviously, it's not it's not a sure thing.
[Greg Cost] [19:42] Right? Yeah. I mean, we've all seen identical twins in our lifetime. Yeah. Totally.
[Greg Cost] [19:46] And I don't necessarily look They're
[Bryan Cantrill] [19:48] not identical. They're not identical. No. I know. We and we had we've got identical twins live across the street.
[Bryan Cantrill] [19:52] And when they were much younger, I could not tell them apart. And then as time went on, like, they are and one is an inch taller than the other. Yeah. You know? And I I did I you know, I mean, I feel like my my brain blew up many times in this book.
[Bryan Cantrill] [20:07] And again, I'm this is all common knowledge for you, Greg, but the, one of the lines early was that, you know, of the single nucleotide polymer polymorphism, SNPs, so seen in the human population, 62% are associated with height. And you're like, okay. Okay. So okay. Height is more complicated.
[Bryan Cantrill] [20:26] I even height, which is like Right. Which like, pretty clearly is like it it just feels like everything was complicated.
[Greg Cost] [20:34] I think height is something that is is very easy to measure, but it's not something that the organism really cares about. Right? It's like Interesting. Yeah. Yeah.
[Greg Cost] [20:43] Like, we're not programmed to grow to a certain height. We're programmed to, like, metabolize nutrients. And if you do that a little bit better, then Yeah. Really? It's interesting.
[Greg Cost] [20:52] Just grow a little bit more. Right.
[Bryan Cantrill] [20:54] Right.
[Greg Cost] [20:54] It's like, you know, you've been on you've been on these old houses for like 300 years ago and the doorways are about 5 feet tall. Right. And it's because people who are very poorly nourished back then. Right. And so they were just shorter.
[Bryan Cantrill] [21:07] So you've got yourself a bunch of things
[Greg Cost] [21:08] in the DNA. Right. Right. But and I think what goes into the genetics of height is like the same thing that goes into it's like a 1000000 different pathways, right? Like anything that makes the cell grow happy or our bodies grow and be happy will make you, like, fractionally taller.
[Greg Cost] [21:25] Right? Right. And so it's not, you know, everyone can stand up against the wall at the doctor's office and like, oh, I'm growing. Right.
[Bryan Cantrill] [21:33] Well, as you say, it's very easy to measure. So it's very kind of like tempting to oversimplify.
[Greg Cost] [21:36] Yeah. Yeah. There's not a gene for height.
[Bryan Cantrill] [21:38] There's not a gene for hype. Yeah. No. Yeah. As you said, it's like a whole bunch of things that are yeah.
[Bryan Cantrill] [21:42] That that that's that's really interesting. I mean, I also feel that, like, the another thing that was super surprising to me in the book well, actually, I do I wanna talk about the things that troll I can talk about the things that troll us in a little bit. I was all I also found myself trolled at least once in the book. Yes. I'm doing I'm sure.
[Bryan Cantrill] [22:00] I I I I can
[Adam Leventhal] [22:01] I can I'm sure I can guess it? But, before you depart
[Bryan Cantrill] [22:04] either you
[Adam Leventhal] [22:05] you were talking about, about metaphor and about, you know, sort of the humbling nature of this to computer science. I don't maybe this is too far giving, us too much, of a pat on the back, but some some of these emergent behaviors, you know, you think about the complex, you know, systems that we create. And I think that you look at look at some of the performance we're doing around, like, you know, our storage facility, for example. I don't know that we could just read the code and infer the properties of it. And obviously, that's like a
[Bryan Cantrill] [22:37] That's true. Yeah. For sure.
[Adam Leventhal] [22:38] 1,000,000,000,000,000,000 times simpler than what we're looking at in terms of gene expression or whatever. But but still, like, I I think, it it was interesting to me reading it, seeing that in any complex system, you have a lot of these same properties where it's not necessarily predictable just from the raw material even when that raw material is as simple as things that we've crafted with our own two hands.
[Bryan Cantrill] [23:03] Totally. And actually, Adam, you know, I think that I felt myself reflecting on is in terms of like you got this computation metaphor that breaks down for all these reasons. But, you know, the other thing we actually spend a lot of time thinking about and talking about here is, the way we organize people and organizations. And I'm, like, actually a better metaphor, you know, for, like like, what I mean, we we did because we've talked about, like, the culture of oxide, you know, and some of the things that we do as a as a as a company culture, which something we think about and have thought about a lot of, but has a bunch of these, like, amorphous, ambiguous kind of qualities to it where it's not completely deterministic. And yet it also is like also ultimately, like, we have height as an organization.
[Bryan Cantrill] [23:43] You know what I mean? It's like Yeah. I I don't know. I don't know. Let's say about it occurred to you though.
[Bryan Cantrill] [23:46] I'm like, that's actually, in some ways, a it's it's easier for me because I have a really hard time with the ambiguity. We are, again, spoiled in computer science, where these things ultimately execute a single instruction at a time. And we the systems we make are really brittle. Like, you can't just you know, Adam, were you in the office when we had what is a typical dumbass idea of corrupting program text and seeing how many instructions we can corrupt. What are the chrono panics?
[Bryan Cantrill] [24:20] Do we This is like a classic dumbass lunch discussion that we had or like so we because we we've got a running operating system. Right? And so there are a bunch of instructions and it's like let's start corrupting instructions. How long does it last? And do you remember this, Adam?
[Adam Leventhal] [24:39] Not that specific. When I did once, like, replace all locks with no ops because how long would that last? And it was, like, not long. Not long.
[Bryan Cantrill] [24:46] Not long. Yeah. So that's another actually, it's an even better example. So the the, we synchronize different threads of control operating often on different CPU elements in a system operating on a shared memory. And the way you make you the way we reason about them is we say no.
[Bryan Cantrill] [25:01] No. No. No. Only one of you can access this at a time. Like, you have the lock.
[Bryan Cantrill] [25:05] And so what Adam the experiment he's talking about is, like, I'm gonna just gonna, like, make those no operations. So, like, you want the lock?
[Adam Leventhal] [25:12] Everyone wins. Everyone gets Everyone wins.
[Bryan Cantrill] [25:14] Everyone's a winner. And the system does not last long. Yeah. Like, the system blows up really quickly.
[Greg Cost] [25:20] The great thing about biology is that every organism out there has been challenged in a in a reasonably similar way. Right? We've had we're thrown into a weird environment. Right? And, you know, a 1000000 generations ago, your whatever bacterium ancestor had the same experience.
[Greg Cost] [25:36] Right? And so it was selected Yeah. Function robustly in the absence of that information or a particular nutrient. Right? And so a lot of I think one of my favorite parts of the book was when he talks about the, robustness of life to challenge or to insult.
[Greg Cost] [25:53] Right. It takes a lot to push an organism or a cell in a particular direction because it it kind of, like, knows what it wants to be, and then it it, you know, it it has it takes a little bit of a shove, like a multiple put pokes in the right direction.
[Bryan Cantrill] [26:06] So is so what did you It's
[Greg Cost] [26:08] like I mean, life, if anything, is not fragile.
[Bryan Cantrill] [26:10] Right. It's not fragile. And I so this gets to again, what it was a mind blowing point for me about the purpose of life being this kind of information preservation. Like, I'm so grateful to be a eukaryote. After you you know what I mean?
[Bryan Cantrill] [26:25] Again, I'm the only one that's, like, I think I've been taking just, like and he makes the point of, like, so sorry. Why do you think, like, eukaryotes? Like, oh, we should all be eukaryotes? Someone wanna explain all of, like, the single cell life around here? You know what I mean?
[Bryan Cantrill] [26:39] It's just like, oh, multi cell a multi cellular life. Like, oh, yeah. You're so awesome. Like, why is there so many singles? And you realize, like, wait a minute.
[Bryan Cantrill] [26:46] We don't have a right to exist. How did we how how did we kind of come out of the muck? How did we come out of, like, why are we not all in thermodynamic equilibrium? And I gotta say, like, the point that, like, really blew my brain up. And Adam, I'd be curious to know what your take on this was, like, the definition of life as systems that are out of thermodynamic equilibrium.
[Adam Leventhal] [27:08] Yeah. Sort of like entropy defying,
[Bryan Cantrill] [27:11] or like Yes.
[Adam Leventhal] [27:14] Creation of organization as, like, in in defiance of the second law of thermodynamics.
[Bryan Cantrill] [27:22] Yeah. Did that, like, I that blew my brain out. Yeah.
[Greg Cost] [27:26] So I
[Adam Leventhal] [27:27] Oh, totally. Like, put down the book. Like Put down the book. Because, you know, things kinda close my eyes
[Greg Cost] [27:33] for a minute.
[Bryan Cantrill] [27:34] I'm daddy's gonna go back to thermal dynamic equilibrium now. Yes. Yeah. What was your take
[Greg Cost] [27:40] on that, Greg? I, I so I read that book that's referenced what is life by Erwin Schrodinger Yeah. About 20 years ago or so. And, yeah, it's the same thing. I was like like, oh my god.
[Greg Cost] [27:51] That makes so much sense. Right? Just, like, a key part of life is avoiding entropy. Avoiding entropy. Localized the localized avoidance of entropy.
[Greg Cost] [28:00] Right? Like, creating order and, really, a lot of what life is is information. Yes. Like you could. Yes.
[Greg Cost] [28:06] Something living in a blender. And then at the end at the end, it's all the molecules are still there.
[Adam Leventhal] [28:10] Yeah. Yeah. And then the preservation of information.
[Bryan Cantrill] [28:13] The preservation of information.
[Adam Leventhal] [28:14] Yeah. Yeah. Because even in his point, even not from within the individual, we're we're you know, we'll decay away, but just generationally, again, kind of mind blown.
[Bryan Cantrill] [28:26] This is where I was, like, lying down in the fetal position in weeping. I feel is the the the the the whole well, the this whole, like, act of super efficient information preservation. That like we have preserved this information crazily energy with crazy energy efficiency. And like too often we obsess about the energy efficiency of like the computation of the brain which is like amazing especially when you compare it to again what I I pause it at the opposite end of every conceivable spectrum, these synthetic computing systems that we've developed that are ridiculously inefficient and I consume way more power. I mean, I and I'm sure you've had this a moment too in oxide where we and we think so much about the thermal design point of everything.
[Bryan Cantrill] [29:10] And then you're like, wait a minute. My brain is like 20 watts. Yeah. How's my brain doing? Like, does that help?
[Adam Leventhal] [29:16] And like, I turned hamburgers into like thoughts. Like, that's weird.
[Bryan Cantrill] [29:20] But in the thoughts, like, was so little energy.
[Greg Cost] [29:23] That's right. So
[Bryan Cantrill] [29:24] Like, I'm not Yeah. Yeah. I mean, I'm water cooled, I guess. But other than that, like, I you you know, I didn't like, that was really and so this idea of information preservation as being very, very, very core to life was very eye opening for me. And and and thinking of, like, DNA not merely as, like, you know, the answer to all that ails us, which is kind of the the human genome project kind of zeitgeist, but more the, like, no.
[Bryan Cantrill] [29:51] No. This is what's preserving all this information is preserved in here, and you've got a whole bunch of stuff in here. And I'd be curious to know what your take is on this in terms of, like, the the the how the thinking on evolution, and kind of this the the the neo Darwinism and kind of how that's being augmented and extended and kind of rethought, if at all.
[Greg Cost] [30:11] Yeah. It's, and that this is a point of where I thought the book was maybe a little bit contradictory. Okay. Yeah. And I started to have some difficulty with it.
[Greg Cost] [30:19] And then I read the epilogue, and he sort of walked some of it back. But, yeah, certainly, a theme for him in the book is that DNA is not the blueprint for, for life. Right? And, and then he's that it gets to the end and then and says, oh, well, it's not, it actually have I opened the book to this page.
[Bryan Cantrill] [30:39] Yeah. There you go. But I knew
[Greg Cost] [30:40] it would come out. So it's far from being some new paradigm that threatens Darwinism. It's rather a glorious extension of it. And that's what I kind of agree with. Right?
[Greg Cost] [30:51] And so I thought sometimes in the in the the main text of the book, things are a little bit overstated and maybe a little bit strident. But, at the end, I thought, well, it all he he kind of softened it. Right? And I thought that was correct. And, look, I'm a big Richard Dawkins fan.
[Bryan Cantrill] [31:10] Oh, Richard. Okay. Yeah.
[Greg Cost] [31:11] I have my my bias coming in, but, I think it it's a it's a bit like saying, you know, well, Newtonian physics versus quantum.
[Bryan Cantrill] [31:22] Right. Okay. Yeah.
[Greg Cost] [31:23] Yeah. Yeah. That might be familiar to a tech audience. Right? You know, like, counting physics isn't wrong.
[Greg Cost] [31:31] It's just right in a special case.
[Bryan Cantrill] [31:33] Right.
[Greg Cost] [31:33] Right? And so quantum mechanics or whatever is not doesn't you could see it as supplanting it, but really it extends it.
[Bryan Cantrill] [31:40] It's extensive. Yeah.
[Greg Cost] [31:41] Yeah. Tremend to build upon it. Right. Right. And so I thought, I thought that was really how I view a lot maybe most of the examples that were cited in the book.
[Greg Cost] [31:51] Right? You know, I guess, I'm saying that it's not a blueprint, not a blueprint. And I I guess I thought through a recent experience I had where I had a contractor at my house. Right? And, I gave him a drawing for I was having some steps read on a really minor thing.
[Greg Cost] [32:07] I gave him a drawing for the steps, and I said, okay. Here's what I want. Like, I'm and I walked him through it, and I'm like, this makes sense to you. It's like, yeah, yeah, yeah, yeah. And, you know, I went away for a weekend and the guys were going to come back and steps are great, but they're not always in the blueprint.
[Bryan Cantrill] [32:23] Yeah, actually.
[Greg Cost] [32:23] And I know you remodeled your house, Brian. Maybe you had a similar plan, similar experience. But so I I guess I I would say that DNA is kind of the blueprint, but, like, there's also nature's contractor that gets in the middle.
[Bryan Cantrill] [32:40] Right. Like, you might it might want to
[Greg Cost] [32:42] do something, but, what actually gets made, what actually comes out the end, the phenotype Yeah. Is, often not it bears some resemblance to the intent. But, yeah, the environment comes in. You know, other other organisms come in, random fluctuation happens, and, you some organisms get more or less lucky with how their cells happen to divide. Right?
[Greg Cost] [33:05] Right. So, yeah, reality and noise, for example, another concept in the book, always interceding.
[Bryan Cantrill] [33:12] When I thought it was interesting and at one point I asked you about, you know, the the the term genome clearly became popularized, and it feels to me like some academics realizing that like, okay, we need to end things in ohm. If we want it like that's this is where the grant money, the grant gold is is with the ohms, and so we got the proteome and then we've got the interactome and it feels like then and I asked you to, like, are there other ohms? And like you rattled off, like, 15 other ohms.
[Greg Cost] [33:42] I guess what what does it mean? It means, like, a comprehensive and definitive addition to the edifice of biologic biological understanding. Right? It's like that's what people mean when they say that. Right?
[Greg Cost] [33:54] But, I guess. But, and yeah, I'm sure it was good. It's a it is a trendy verbiage, I would say, especially maybe. The transcriptome. Transcriptome.
[Greg Cost] [34:04] Yeah.
[Bryan Cantrill] [34:05] The the epigenome, the microbiome, obviously, that we know that one. The immunome. The other thing, the other thing I don't think I really appreciated and it makes me wanna write go read a book about dedicated to the immune system in particular. But the immune system is kind of like we get a lot going on. The immune system is like kind of, it it we have a complicated relationship with the immune system.
[Bryan Cantrill] [34:26] Is that a fair statement?
[Greg Cost] [34:28] It it the immune system has to make a lot of value judgments. And it it, being wrong is not good. Yeah. And, so it it has a lot of double checks and triple checks and, parts of it. And then other parts of it kind of shoot first and ask questions later.
[Greg Cost] [34:48] Right?
[Bryan Cantrill] [34:49] Right.
[Greg Cost] [34:51] It's broken down typically into the innate immune system, which is the, sort of, like, really active defense that sort of does that shooting first and asking later, and then, the adaptive immune if there was B and T cell response.
[Bryan Cantrill] [35:07] Yeah. Right.
[Adam Leventhal] [35:08] There was a great line about the immune system that I that I want to share. It was the the immune system has so many different components doing so many things that it is, in the words of science writer, Ed Young, where intuition goes to die. Immunology, Young says, confuses even biology professors who aren't immunologists. And then the parenthetical is, I suspect that is a little too generous to immunologists. Yeah.
[Bryan Cantrill] [35:33] Yeah. Interesting.
[Adam Leventhal] [35:34] That was just delightful, like, in terms of the expression of complexity.
[Bryan Cantrill] [35:39] Yeah. I I remember reading. That was a good one.
[Greg Cost] [35:42] You know, I I it was one of, my favorite topics when I was undergrad.
[Bryan Cantrill] [35:46] Was immunology? Immunology. Yeah.
[Greg Cost] [35:48] I thought I was pretty good at it. It. And then, like, several years ago, I worked on a immunology related project. I'm reading starting to read papers in the field again. What I don't remember any of this.
[Greg Cost] [36:03] Yeah. What happened? And I finally figured it out because most
[Bryan Cantrill] [36:07] of it was discovered after I
[Greg Cost] [36:09] had last studied immunology.
[Bryan Cantrill] [36:10] Yeah. Right.
[Greg Cost] [36:11] And now it's only 10 or 15 years. It's remarkably complex. I'll tell you what, though. There's a lot of observation bias in anything we do. Right?
[Greg Cost] [36:20] Yeah. I think a lot is known about the immune system precisely because you can take a blood draw and get the cells. Right. I wouldn't be surprised if there are similar complexity in our liver, our gallbladder, pancreas, whatever. It's just that it's a lot more difficult to understand the, to to really access the cells and to have the biology.
[Greg Cost] [36:39] So the immune system is something where a lot of details are worked out, but it's also it's, you can slice the slice the onion even thinner and thinner and thinner. And, like like, how quick a great example is how many immune cell types are there? And, you know, the these are often looked at by the expression of cell surface markers because you can have an antibody that'll bind to that marker, and you can use an experiment called do do use a machine called a flow cytometer to, really subdivide all these classes of of immune cells. And, like, the more you look, the more types there are. And it's probably,
[Bryan Cantrill] [37:20] is it even just figuring out?
[Greg Cost] [37:21] It's it's it's being it's it's just dense. You know, there was a there was somewhere in the book there was a map of like, I think a term triptomic profile of different cell types. And, one of the point was that they're not separate islands, right? There were like linkages between them with cells. Yeah.
[Greg Cost] [37:37] Almost an immune cell or almost a hepatocyte or something. Right. And yeah, I just get the feeling that there's a lot of that going on in general in the body, but also especially as, sometimes the cells switch what they do. Like, you can you can be a pro pro inflammatory cell or a de inflammatory cell, if you will. I'm just based on the context, And so Uh-huh.
[Greg Cost] [38:02] It's I I I'll bore you with it.
[Bryan Cantrill] [38:04] No. That's wild. I mean, but it it also be makes it very difficult to study. I mean, this is not a deep thought. Yeah.
[Bryan Cantrill] [38:12] But it's just like I mean, I'm kind of amazed that with all of the complexity, I mean, you're talking about, like, you know, you're discovering you're studying immunology as an undergrad. You're like, alright. I can think I understand this stuff. I just feel like you get your ass handed to you all the time by how complicated this stuff is. And then I'm so amazed you don't just like walk away and like, I'm gonna go, like, be a farmer.
[Bryan Cantrill] [38:32] I'm gonna go I I'm actually gonna be the contractor that goes next steps in because, like, I just can't like, this is getting me such a, that there's so much that I thought I knew. That is actually way more complicated. Yeah. I mean, it
[Greg Cost] [38:43] it You learn humility quickly. You
[Bryan Cantrill] [38:45] wanna yeah. Yeah.
[Greg Cost] [38:45] Yeah. And, you know, like I said, another thing that was brought up in the book, I think the quote from the editor biology editor of Nature, like, the in biology, the answer is always yes. And Yep. Right. That's immunology is a great example.
[Greg Cost] [38:59] Oh, is there a immune cell that does this? Oh, yes. But but only when x, y, and z are are present. Right? And, yeah.
[Greg Cost] [39:08] Look. It it's daunting. And I'm sure, again, I'm sure it's the same in other fields. We just probably haven't appreciated it yet.
[Bryan Cantrill] [39:15] I think it's worse than biology. Oh, no.
[Greg Cost] [39:17] So I meant I meant another, subs field.
[Bryan Cantrill] [39:19] Oh, subs field biology. Yeah. Yeah. I'm like, yeah. I think I think you guys can, like, you guys can pretty much lower the complexity over basically anyone as far as I'm concerned.
[Greg Cost] [39:25] Like, really? What's going how how does life work? It's it's the world's biggest Rube or most complex Rube Goldberg machine. Right? Where it it the organization is unintuitive.
[Greg Cost] [39:36] It's crazy.
[Bryan Cantrill] [39:37] Well and so the other thing that that kind of blew my brain is the idea when of metazoans I mean, also, like like, glad to be eukaryote. Glad to be a metazoan. Like, nice breakthrough there. But the but evolving evolvability was a really interesting idea that, like, it seems like I mean, there's some really interesting action that happened. What what is it?
[Bryan Cantrill] [40:05] We're talking 100 of 1,000,000,000 of years ago. Right? I mean, we're talking the what where we've got the the the rise of karyotes, the rise of and we it feels like I mean, that that origin I mean, there's a lot that, like, all of a sudden got locked in where it could lock in a bunch of these
[Greg Cost] [40:20] proteins. I think he quotes the biologist, Mark Kirschner, a really famous guy, on this topic. And he's and it makes that what his statement made so a lot of sense to me. Like, what you get when you become a multicellular organism, you get you get you gain complexity and the ability to respond in smarter ways, isn't it? But what you lose is a fast generation time.
[Greg Cost] [40:38] Right. So your evolutionary rate
[Bryan Cantrill] [40:40] just those slows way
[Greg Cost] [40:42] down. And so you can't count on the fact that you're going to be able to, like, spot out and you have fewer offspring, obviously. Right. But we and, humans, other primates. You can't you you you you'd be brutal if you were so rigid.
[Bryan Cantrill] [41:00] Right. You have
[Greg Cost] [41:01] to be a little bit more flexible in terms of how things work. Right? Because otherwise you would never produce a baby. Right? Right.
[Greg Cost] [41:09] I mean, look. I think the most highly evolved organisms on the planet are viruses along closely by bacteria. It's not because
[Bryan Cantrill] [41:16] Or do we even are we even on podium as humans? No. No. No. No.
[Bryan Cantrill] [41:19] No. No. Okay. He's like yeah. No.
[Bryan Cantrill] [41:22] Sorry.
[Greg Cost] [41:22] That's that's just measured purely by the number of generations they've gone through. Yeah. I mean, there was another quote in the book that said some some biologist said, I would be proud to be on the committee that designed the E. Coli genome, but I would not be proud to be on the committee to design the human genome. And that is that is, like, the truest statement ever.
[Greg Cost] [41:41] Right? Right.
[Bryan Cantrill] [41:42] So because of the efficiency of it, because it was like there
[Adam Leventhal] [41:43] there's so much so so much Because it was, like, there there's so so much so so much purity in in the former
[Bryan Cantrill] [41:47] and so much noise in the latter. Well, listen. Yeah.
[Adam Leventhal] [41:47] Is like the 4th of
[Bryan Cantrill] [41:53] genomes. You know, the sorry. I'm making I I I I'm I'm going to the 4th being a computer programming language. Very a a famously simple computer programming language. So actually the the stack based language.
[Bryan Cantrill] [42:04] Another question I've got for you on that note because I think one of the things that Paul talks about is that we've kind of had this idea that, if we can just study if we completely understand e coli, like, we've got it all mailed. And it's like, well, maybe not. And like what's good for the e coli is not good for the elephant is kind of a line that he had quite a bit. I mean, what do you what do you make of that?
[Greg Cost] [42:23] Yeah. So can I can I just
[Bryan Cantrill] [42:24] Yeah? Please. One
[Greg Cost] [42:25] other thing first. Know, one thing I think is really a little bit inspiring actually about I'm just looking at the e coli genome is that more evolution has had time to work on something, the more sense it makes, the more it looks like something that was actually intelligently designed.
[Bryan Cantrill] [42:42] Yeah, interesting.
[Greg Cost] [42:43] And so I think it's it's kind of, it's really comforting to me to know that we, with our brains, when we design things, we're designing things that kind of look like a highly evolved system just by thinking about it. Right? And so I think we're on the right track.
[Bryan Cantrill] [43:00] We've designed
[Greg Cost] [43:01] things, right? Yeah. Like, you know, we haven't I think we don't understand the E. Coli genome, of course, but, like, it it it does kind of make sense as you look at it. Like, genes that are similar, have similar functions are grouped together and they're regulated together.
[Greg Cost] [43:14] And it's very efficiently organized. Right? And it's stripped down and it's fairly, really compacted, very few, but these big transposons getting in the way of everything and none of these introns sitting in the middle of genes for some reason. Right? It's, it's extremely efficiently evolved.
[Greg Cost] [43:36] And I think when we design something, we design something that kind of like has the same principle.
[Bryan Cantrill] [43:40] Right. Interesting. But much simpler. And so this is a Yeah. I mean, to your I guess, making the kind of the the the same point here about, like, what multicellular life, why multicellular life then?
[Bryan Cantrill] [43:52] I mean, multicellular life is kind of like a bit of a mixed bag that you get the complexity Yeah. But you lose some of the simplicity. You get the power. I mean, I I guess that's technological.
[Greg Cost] [44:02] But You know, I think even when you have, a bacterium, right, living in the soil, there its its unit of inheritance is itself. Right? And so it's selfish in that regard. But bacteria don't necessarily live by themselves in the soil. Right?
[Greg Cost] [44:17] I mean, they're nestled up against other bacteria. I mean, they're probably nestled up against their brothers and sisters, right, from previous generations. So if you think about a colony on a on a Petri plate of bacteria. Right? Sure.
[Greg Cost] [44:29] They're all unicellular, but is that really a unicellular organism? It's not not Oh, yes. Organism. But, I mean Yeah. Yeah.
[Greg Cost] [44:36] Yeah. The cells know that they're on the edge. They know they're at the bottom. They have less oxygen. Greater exposure to an antibiotic in the plate.
[Greg Cost] [44:44] Right? So they, you know, I think it's it's probably not too far from that to something like a slime mold where you have all these different cells that are together, but then some of the cells turn into the spore forming body. And that's how really the inherited inherited state. Right? Because because if you can guarantee that the cell next to you is actually genetically identical to you, it doesn't really matter to that gene if you're the cell that's transmitting the information or if it's your your paper.
[Bryan Cantrill] [45:16] Right.
[Greg Cost] [45:18] That's that's my my Dawkins plug there. That's how that's how you would think of the situation. Right? And so I think it's like I I think even some microorganisms that we conventionally think of as monocellular probably have characteristics that are reminiscent
[Bryan Cantrill] [45:33] of a multicellular organism. Interesting.
[Greg Cost] [45:36] Because you can avoid interacting with other organisms. Right? Right. Just the question is, is it is it the same genome as you that you have or is it a different one?
[Bryan Cantrill] [45:45] That's why
[Adam Leventhal] [45:45] I'll talk about bacterium that, you know, acted differently in the presence of other bacterium of the same sort where they would kind of flip between, kind of lone wolf mode and collective mode in terms of sharing information about the gradient of nutrients and things like that. I mean, right along the lines of what you're describing.
[Greg Cost] [46:06] Yeah. Yeah. There's this whole phenomenon called quorum sensing. Like, they kind of make, they change their behavior and they make kind of a group decision. It's I thought about studying it for a while.
[Bryan Cantrill] [46:15] Yeah. That's very interesting. Well, I then I'm I'm not sure how much I mean, another kind of line that that blew my brain a little bit was and again, I'm sure this is something that is well known to folks in the field, but that cancer is a disease of organization, not a disease of cells. I thought was really interesting. The and I really enjoyed, the Mukherjee's emperor of maladies, and just I mean, how it feels I mean, cancer is so fundamental to the way the cell is operating.
[Bryan Cantrill] [46:46] It feels, I mean, is it fair I mean, this may be, it feels like until we got cancer completely licked, there's a lot we don't understand.
[Greg Cost] [46:56] Yeah. No. It's it's, I think one of the discoveries in the past is has been most most, provocative to me is really that even in cancers that are of a specific type, they're not all the same. Right. Yeah.
[Greg Cost] [47:12] Cancer is defined as much by the secular nature of the mutations in the cancer and not the cell type that happened to originally. This I honestly, this is where I disagreed a little bit with Yeah. With the book. Philip Ball.
[Bryan Cantrill] [47:25] Yeah. Yeah.
[Greg Cost] [47:25] And, I I do think a lot of work has been done on, again, understanding how our normal cells evolve at the DNA level in order to replicate in a way that's dysregulated. And, you know, it no no doubt. It's an cancerism. It is not a single cell phenomenon. It's an organismal phenomenon.
[Greg Cost] [47:45] Right? A tumor is not a single cell, but the changes that go, in that that enable a normal cell to turn into a pathological state are are very clearly genetic changes. Oftentimes, they involve loss of different parts of the chromosome, amplification of other parts of a chromosome, and, of course, specific mutations, and, in particular genes that are beneficial to, beneficial to the tumor. Right? It's, like, perfect example of natural selection.
[Greg Cost] [48:16] Unfortunately, it's taking place in our bodies, each one of us every day. Right? We have cells that become cancerous. Our immune system, again, making And kills them off. Yeah.
[Greg Cost] [48:27] And, but, you know, some it sometimes they'll they'll slip through. Right.
[Bryan Cantrill] [48:34] And what do you think about his his comment of the, to develop in the tumors is one of the particular hazards of pluripotent stem cells? It might more pronounce it where pluripotent? I'm sorry. What's that? Pluripotent?
[Bryan Cantrill] [48:47] Am I pronouncing it?
[Greg Cost] [48:48] Pluripotent. Yeah.
[Bryan Cantrill] [48:49] Yeah. Yeah. I this is one of the things we've learned in doing a podcast is that I pronounce many things incorrectly, and I'm trying to get out in front of, like, the next, like, thing that I pronounce it correctly. But but, pluripotent is not a word that comes up very frequently in computer science, but comes up a lot in biology. Yes.
[Greg Cost] [49:04] Yeah. Yeah. Yeah. Yeah. Yeah.
[Bryan Cantrill] [49:06] And what did you what did you make of of that line? I mean, because I thought that was that was interesting that the that basically the the this is kind of part of part of the cost of having pluripotent stem cells is that, like, we love these stem cells because they have such fecund versatility. Yeah. But then this also sows the seeds for this versatility gone
[Greg Cost] [49:34] a mock. You you need you need your stem cells. You want them you want them around. Right? For example, in the immune, lineage there, what are called hematopoleg stem cells.
[Greg Cost] [49:42] And, there aren't too many of them in the body, but and they they divide very seldom. Once every 6 months in your bone marrow.
[Bryan Cantrill] [49:54] Really? Wow.
[Greg Cost] [49:55] But then the the cell that it divides into, it one one goes back to make that stem cell. The other cell very quickly, like, proliferates into what I call a progenitor cell, and it makes all the cells in the immune system on in the erythroid system hyaline system. And so you really want them around. Right? You would you would quickly have anemia and logical failure if those stem cells weren't there.
[Greg Cost] [50:20] Right? But, yeah, by the fact that they can make everything, sometimes they they make a mistake, and they do make everything and solutions where you wouldn't want. So maintaining that having that capacity is important part of maintaining our body. Right. Our body.
[Greg Cost] [50:38] But, yeah, it's it's like any it's like any tool could be used for good or evil. Right? And, you know, body tries to keep it under wraps, but sometimes things break. The genes break, and, also slip through.
[Bryan Cantrill] [50:52] Well, so the I I think that's another kind of interesting theme about, like, you have these things that that where we are just understanding some of these effects, and then realizing, like, actually the effect is also really important for has given us a lot. And so one of those for me was preons.
[Greg Cost] [51:07] Yeah. Yeah.
[Bryan Cantrill] [51:08] And, you know, I I so this kinda caused me to, like, reflect back as a bystander of biology, you know. So what are some of the things that have been and certainly the, BSE. And there was this idea that if you had had beef in the UK in, you know, whatever, 1984, that you were basically going to die of CJD. And there was a real hysteria for I would say a somewhat prolonged period of time. I mean, Bridget because Bridget had been in the UK my wife had been in the in the UK for those years.
[Bryan Cantrill] [51:37] She couldn't donate blood until, like, last year.
[Greg Cost] [51:39] Yeah.
[Bryan Cantrill] [51:40] Because they're just like, look, we just not we just don't know. We're not, you know, if you've been in the UK in these kind of these years in the eighties, you're not gonna be able to donate blood outside the UK. The end but then that didn't really that didn't manifest.
[Greg Cost] [51:53] It wasn't as bad as people thought.
[Bryan Cantrill] [51:55] But Yeah. I mean, it was like it was like by by, like, several orders of magnitude. Right? I mean, there was there's a kind of a thinking that was gonna be, like, millions of people with dives of CJD.
[Greg Cost] [52:03] I I don't remember the original estimate. It probably ended up being 100, though.
[Bryan Cantrill] [52:06] Right. It was 100. Right. Right. Right.
[Bryan Cantrill] [52:07] And and kind of and, but I the one of the interesting lines in there was that the misfolding pathology of prion proteins is the price paid for the benefits of disorder. So organized disordered proteins can increase the complexity and versatility of a regulated regulatory networks. But at the cost of increased risk of toxic aggregates formed by misfolding proteins. And I thought that was kind
[Greg Cost] [52:32] of absolutely. And interesting. Bions are it was a hypothesis that was not readily accepted
[Bryan Cantrill] [52:41] Right.
[Greg Cost] [52:42] As you can well imagine. Right? Because
[Bryan Cantrill] [52:44] The hypothesis that, like, I misfolded protein is gonna induce a misfolded protein. Yeah. Yeah. Yeah.
[Greg Cost] [52:49] Exactly. And, and even more than that, they especially in microorganisms, it's been shown that they can actually transmit genetic information that way. Crazy. Right?
[Bryan Cantrill] [52:58] Because nature doesn't need anything. Just care. Right? Right. Right.
[Bryan Cantrill] [53:05] So, you know, if
[Greg Cost] [53:07] this protein state, it means information like any other protein state. It's just one that's particularly self propagating. Right? Right. And so if 1 if a protein state can transmit information to the daughter cell and that gives a daughter cell an advantage Jackpot.
[Bryan Cantrill] [53:21] I'll use it. Right. Yeah. Absolutely. It's in the toolbox.
[Greg Cost] [53:24] The fact that it's pathological, in some cases is unfortunate. Right? But it's, yeah, I I thought it was a really, a really well made point. Yeah. Right?
[Greg Cost] [53:35] It's like you need proteins to be flexible. Yeah. And we can talk about this. And then states, which are, like, very much a new thing in biology, I'm really attuned to that. But, yeah, we need them to be flexible to do their jobs and exist in an energy landscape.
[Greg Cost] [53:53] And sometimes the energy landscape that allows them to achieve their appropriate confirmation is close enough to one that allows them to achieve a pathological confirmation as well.
[Bryan Cantrill] [54:06] I kind of came away then amazed that we don't see those pathologies more frequently.
[Greg Cost] [54:11] I suspect we have mechanisms in our body to prevent a lot of or Yeah. Yeah. Temple amyloid plaques. Like, they're we we have this machine in our cells. It's like it's used to the No.
[Bryan Cantrill] [54:21] No. You you you no. You're I I I feel like I yeah. I don't wanna be, like, anti medical.
[Greg Cost] [54:25] It's a it's a garbage disposal. It's called a proteasome. And so, you know, messed up proteins get put into this little funnel. They get chewed up, and they get spat back out and recycled. Yeah.
[Greg Cost] [54:36] And, I, you know, I suspect that there are there are many ways in our many times in our body that proteins get messed up, Right. For example, and, they have to be they they somehow the cell senses that and pulls it into
[Bryan Cantrill] [54:50] this Get out of here. Yeah.
[Greg Cost] [54:52] Undoes that. Right. But it's a buffering capacity. And you have something that causes the stimulation of the accumulation of these at a rate that's greater than the ability to remove them, you run into a problem. Right?
[Greg Cost] [55:04] There's also a disease called amyloidosis. It's a protein that's involved in, binding and trying carrying a thyroid hormone around a body. It's thyroid hormone. But it it falls into an alternate confirmation, and it deposits all over, you know Oh, interesting.
[Bryan Cantrill] [55:21] But it's rare.
[Greg Cost] [55:22] It is rare. It is rare. But it's one of these things like like Alzheimer's disease. You'll get it if you live long enough.
[Bryan Cantrill] [55:27] Right. Right. Oh, that's interesting. Right.
[Greg Cost] [55:28] Yeah. And that's why the diseases that people die from are often not genetic diseases. Makes that point in the book, right? All the common diseases that are really bad are not genetic diseases Because the genetic diseases will kill you young. Right?
[Greg Cost] [55:40] Right. The diseases that kill people, modern society, are the ones that you're you're you're the winner. Right? Yeah. You're dying of something that's, like, not obviously a genetic disease.
[Greg Cost] [55:51] Right? Right. It's an acquired state. Right? So Right.
[Greg Cost] [55:55] In your artery, you're like
[Bryan Cantrill] [55:56] Greg, you may not have a calling as a priest in the history of last rites. I I I gotta tell you. I'm not sure that that's bad. It's on Mandarin. It's like, and I'm here with another winner.
[Bryan Cantrill] [56:06] I got another winner. It is winner winner chicken dinner. And here you're back, I'm dying. I'm like, no. No.
[Bryan Cantrill] [56:11] Hey, listen. Congratulations.
[Greg Cost] [56:12] It's not a
[Bryan Cantrill] [56:13] genetic Congratulations. It's like a balloon drop. We have not a genetic disorder. You won. But I did you ever read Deadly Feasts, Adam, by Richard
[Adam Leventhal] [56:23] Rhodes? Yeah.
[Bryan Cantrill] [56:24] So this is one of the you get these books that like go around a social group and this is one of those that, like, Richard Rhodes wrote Dark Sun, and wrote this book called Deadly Feasts in, like, the late nineties. And, like, if you wanna get scared about prions, like, you can scare yourself about prions. Like, you take these things because they're not viruses or bacteria, and you can irradiate them, and you can do all sorts of, like, nasty stuff to them. You can burn them, and then you can, like, inject it inject it into a mouse brain. And, like, the other mouse, like, dies of Kuru or whatever.
[Bryan Cantrill] [56:53] Yeah. Yeah. They're just they're just, like,
[Greg Cost] [56:56] surgical instruments are now often disposable. Oh, stainless steel, posable surgical instruments. Exactly.
[Bryan Cantrill] [57:03] That for exactly that reason. That's really interesting because of
[Greg Cost] [57:05] you, you cannot eradicate it.
[Bryan Cantrill] [57:07] Oh, pretty interesting.
[Greg Cost] [57:10] You know, it's they're almost indestructible.
[Bryan Cantrill] [57:12] And so on the one hand, I remember reading that book and being like, yo, I'm definitely like scared. And but now I'm kind of in hindsight. I'm like, wait a minute. I also should have been asking myself the immediate follow-up question like, hey. Hold on.
[Bryan Cantrill] [57:23] Like, this is why are these so rare? I mean, these are super, super rare and unusual. They happen under unusual conditions. It's like, there's gotta be more to the story here, and it can't just be that we're all gonna like eye of kuru. But that said that said, do not eat the brains of the deceased.
[Bryan Cantrill] [57:39] No. Not Especially if they died, like, bonking in the wall.
[Adam Leventhal] [57:42] This is medical advice, people. Yeah.
[Bryan Cantrill] [57:45] This is medical advice. This is medical advice. Normally, we don't give that much medical advice in the show, but, like, just don't eat the brains of your disoriented enemies is what I would say. Adam, I'm really just concerned that, like, like, look, I I I have I do have blatant fear. Are you this late winter that I'm projecting on other people that, like, I'm gonna get eaten.
[Bryan Cantrill] [58:02] They say your cats will eat you 3 days after you die. And I can just feel it's pretty changed my relationship with the cats. I just feel that they are, like, I think if you're
[Greg Cost] [58:10] in this, I just feel
[Bryan Cantrill] [58:11] that they're just, like, eyeing me over. They're, like, looking and I catch kinda like, there's a lot of me that I feel is not edible, but I feel like the cats are gonna be, like, we're we're gonna be the judge of what's edible and what's not edible, pal. But, like, the brain, like, eat that at your own risk. Yeah.
[Greg Cost] [58:23] Again I I I
[Bryan Cantrill] [58:24] could have taken
[Adam Leventhal] [58:25] your thought. I
[Greg Cost] [58:27] can't recommend eating brains. And actually, there there are people who've gotten, beyond as you were beating squirrel brains
[Bryan Cantrill] [58:35] Yeah.
[Greg Cost] [58:35] Between Penn States. I don't know what it is about brains, but, you should not go for them.
[Bryan Cantrill] [58:41] You know, I the sweet breads though are also tasty. They are very good.
[Adam Leventhal] [58:46] Is this culinary advice or medical advice? No.
[Bryan Cantrill] [58:49] We're we're we're right in that gray area, aren't we? We're right in that gray.
[Greg Cost] [58:52] I'm thinking that about the pancreas. So There
[Bryan Cantrill] [58:55] we go. That would eat up. Well, the the you have first time when Adam was reading fast food nation. Most people read fast formation and became vegetarians. And Adam read fast food nation.
[Bryan Cantrill] [59:04] He's like, I gotta tell you, like, it's making me hungry. I'm like, I want a burger. I'm starving. I'm like I'm like, you that is you are not a big demographic pal. There are a lot of no.
[Bryan Cantrill] [59:13] You should read the book. Like, also, like, I want a burger, and we're gonna go to Jack in the Box, by the way, because they're the ones that have, like they had to figure all this stuff out. Like, fly the airline that just crashed. They're the one that are paying they're they're the ones that are paying attention. It's like, yeah.
[Bryan Cantrill] [59:27] Go to don't go to Wendy's. Go to Wendy's at your own risk. But, the, so yeah. This is not necessary. I don't know if this is culinary advice or medical advice.
[Bryan Cantrill] [59:36] Brains brains are delicious, but not of the not of your enemies that died of disorientation. I don't know. You know what?
[Greg Cost] [59:42] Actually, there's a second big second biggest second biggest, tissue tissue that expresses the pre owned protein outside of the brain is actually the bone marrow, oddly. So, you know, I don't eat
[Adam Leventhal] [59:52] oxtail Short ribs too. Okay. Interesting.
[Bryan Cantrill] [59:55] Okay. We did this feels mean spirited. Just Craig, you're just here to take things off the menu? This is like I I see, alright. Oxtail soup.
[Bryan Cantrill] [01:00:03] This is I'm
[Greg Cost] [01:00:03] kinda like
[Adam Leventhal] [01:00:04] Osabuco? Come on. I mean, brain's fine. Osabuco, I'm not sure. We'll see.
[Bryan Cantrill] [01:00:08] That okay. Well, yeah. What other are there other other thing what are other foods that you do not eat based on your you you know this reminds me of the start list. The well, then I had a, I I met a toxicologist once, Ed. And he's like, I gotta tell you, don't pump your own gas.
[Bryan Cantrill] [01:00:25] At the and this is in the era when gas was unshielded. He's like, benzene is such absolutely bad news. And if you are ever, especially if you are in like a dusty environment, do not pump your own gas because the benzene will bind to the dust. You'll breathe it in and you just, it will not. I think you just, you know, fresh off of a benzene bender or whatever, studying benzene.
[Bryan Cantrill] [01:00:46] I you know, don't overweight that advice, but, you know, there you go. It's like no oxtail soup. Don't pump your own gas. Like, everyone's filled with good good kit. This is a this is news you can use today on oxide and France.
[Bryan Cantrill] [01:00:56] Yeah. You thought you're gonna get a Correct. Exactly. I thought you're gonna get a dry discussion of of a a really interesting book, but no. No.
[Bryan Cantrill] [01:01:04] Hey. So Yeah. Brian, question
[Adam Leventhal] [01:01:06] for you. Did did you see in all of this Alan Turing on the horizon?
[Bryan Cantrill] [01:01:11] Okay. So I'm not sure
[Greg Cost] [01:01:12] you did.
[Adam Leventhal] [01:01:13] I was completely surprised to see him.
[Bryan Cantrill] [01:01:15] I was com completely surprised to see him. I would no. I I I knew we were gonna get to touring at some point. And the the, no. That was a huge surprise to me.
[Bryan Cantrill] [01:01:22] I had no idea. So Alan Turing is the rightfully thought of as the father of computer science. I mean, there are a handful of them that are these early pioneers, but, but touring is definitely one of them. Maybe now is the time to mention the part of the book that maybe I had to take a break from. Do you know exactly what this is?
[Bryan Cantrill] [01:01:40] You know the passage, I'm sure, Adam.
[Adam Leventhal] [01:01:42] I'm sure it has to do with with artificial intelligence.
[Bryan Cantrill] [01:01:46] Close. The, the once a relatively obscure figure, Turing is now widely hailed as a visionary genius. Thanks in part to the 2014 biopic, The Imitation Game, and the decision to feature him on the British 50 pound note. I'm like, I've the the no. I I think the the book got thrown off the bat with me at that.
[Bryan Cantrill] [01:02:10] I'm like I'm like, the book, you and I need a break. Like, 2 I'm sorry. The Imitation Game. Did you see the Imitation Game? No.
[Bryan Cantrill] [01:02:15] I've never heard
[Greg Cost] [01:02:15] of it, but I've heard Alan Turing.
[Bryan Cantrill] [01:02:17] Okay. The Imitation Game, first of all, terrible. I felt Adam.
[Adam Leventhal] [01:02:23] I don't know that I watched it.
[Greg Cost] [01:02:26] It's bad. It's
[Adam Leventhal] [01:02:26] just it's like It's Benedict Cumberbatch. Right?
[Bryan Cantrill] [01:02:28] It's Benedict Cumberbatch and, like, this is, like, the story of Alan Turing and Enigma, which is an extraordinary story. Is apparently too boring for the big screen. So we're just gonna, like, fill in a bunch of stuff that we think would be more exciting and interesting, and along with some kind of ridiculous characterization of what we think a computer scientist looks like, and very much into, like, the lone madman kind of a thing. It's bad. It's bad.
[Bryan Cantrill] [01:02:54] This is one of these where my kids are like, this is why we can't go to these kinds of movies for you. Like, you are this is like, why can't you just, like, roll like, you can't just chill and watch a movie. Like, you have my that's because I can't chill and watch a movie that's garbage. But it's so the idea that, like, to so in computer science, the the the Nobel Prize equivalent. First of all, any discipline that has to say Nobel Prize equivalent just shows you that it's, like, ultimately, like, eating at the kids table from a intellectual discourse perspective.
[Bryan Cantrill] [01:03:20] But the Nobel Prize equivalent for us is the Turing award. So the the the I mean, Alan Turing very well known in computer science. I think known outside of computer science before. I don't I and but I don't think the I don't
[Adam Leventhal] [01:03:32] think You don't think the 50 pound note was the tipping point?
[Bryan Cantrill] [01:03:35] I think the 50 pound note moved the needle on Alan Turing.
[Greg Cost] [01:03:37] He's British. Yeah.
[Bryan Cantrill] [01:03:39] I did the idea. That's true. God is British. And it's like and look, like, the guy's got a lot. I mean, also, it's like, do people know Ulysses s Grant?
[Bryan Cantrill] [01:03:46] I I mean, are are they just like once a relatively obscure figure, like, people I I mean, come on.
[Adam Leventhal] [01:03:53] But then, right, you take, 50 50 units of currency and then forget about it right to
[Bryan Cantrill] [01:03:59] the
[Adam Leventhal] [01:03:59] top of the charts.
[Bryan Cantrill] [01:04:00] Right to the top of the charts. Like, who's this guy on my 50 pound note? I wanna know a lot more about him.
[Adam Leventhal] [01:04:05] Tell me more.
[Bryan Cantrill] [01:04:06] Wait a minute. It's the guy from The Imitation Game. I know him. No longer a relatively obscure figure. You, Alan Turing.
[Bryan Cantrill] [01:04:14] Alright. There you go. Ran it off. I then I go retrieve the book from the balcony that I've thrown it off of and it'll be retrieve it out of the yard. But I did not know Adam at all.
[Bryan Cantrill] [01:04:24] And so is this well known in biology that Alan Turing how much is this is like someone who has got a computer science background in terms of Alan Turing's role in, in some of these the and what was the exact the exact term? But I was very surprising to me. I didn't know idea that Alan Turing had it. It's like
[Adam Leventhal] [01:04:41] the the Turing patterning, like
[Bryan Cantrill] [01:04:43] the describing. Yeah.
[Greg Cost] [01:04:44] Yeah. Not
[Adam Leventhal] [01:04:44] everything from zebra strikes to, like, you know, having 5 fingers.
[Greg Cost] [01:04:50] I guess I I knew that there was mass behind that and that those patterns can emerge. I I wasn't aware that he did that.
[Bryan Cantrill] [01:04:56] I had no idea. I had, I had no idea. And it was really, really interesting. And Gaurav actually put me on to another computer science computer scientist, Leslie Valiant. I'm not sure.
[Bryan Cantrill] [01:05:09] Won the Turing Award in 2011. And his Turing Award lecture is really interesting because this is one of the ones that he talks about. One One of the things that he's grappling with is that the that it feels like Darwin alone eo Darwinism can't explain all of the richness that we've selected. Natural selection alone is kinda like not enough. And that is like it's too much has happened.
[Bryan Cantrill] [01:05:33] It's too fast, which I thought was, and I'm sorry. I'm butchering. I'm sure his his work and and his Turing Award lecture. But I thought it was interesting where because he gets into this kind of, like, information preservation role
[Greg Cost] [01:05:46] Uh-huh.
[Bryan Cantrill] [01:05:47] That we have in biology, which I this is what we're talking about earlier in terms of, like, the the ultimate role being to kind of and touring viewing it as an information problem I thought was super interesting.
[Greg Cost] [01:05:56] Yeah yeah yeah I think actually there are a few instances in the book where, Philip Paul says, oh how could it possibly be DNA that's encoding all this? And it's sort of I know I find that a little bit of a weak argument. Right? Because, well, I I think it must be because that's what there is. Right?
[Greg Cost] [01:06:13] Right. It's, can I
[Bryan Cantrill] [01:06:16] ask Yeah? I like a super dumb question that the so one of the things that I grappled with as a kid and I'm not sure Adam if you ever grappled with this, but, like, when you first learn about a compiler. Right? And you've got this, like, okay. A compiler is something that takes a programming language and generates, like, assembly code.
[Bryan Cantrill] [01:06:34] You can run. It's an oversimplification. But, like, what do you write the compiler in? And people talk about, like, no. Like, we wrote the compiler in in the language that we developed the compiler for.
[Bryan Cantrill] [01:06:45] And I remember, like, before kind of learning about how these systems are bootstrapped, you're like, what? It does not make any like you need to have an existing compiler. How do you compile the compiler? How do you compile the compiler? Right?
[Bryan Cantrill] [01:06:56] It's like, how do you have the first compiler? And, like, the reality is right now, if you wanna build a new compiler, you don't have to do it in assembly. Right? You get to write a compiler in a higher level language because that compiler already exists. But you are very much implicitly dependent on that compiler.
[Bryan Cantrill] [01:07:16] It that and that is implicitly dependent on the compiler that creates
[Greg Cost] [01:07:19] a Totally.
[Bryan Cantrill] [01:07:19] And is the it it feels like with DNA, like, you've got DNA, but you also have, like, the computer that is the it it feels like with DNA, like, you've got DNA, but you also have, like, the computer that is the, like, the computer that is the, like, the like, you've got DNA but you also have, like, the computer. That is the thing. I mean, again, to go with the torture metaphor. But like, that's the, like, you need that as well. And that's the thing that's also, I mean, that's not being passed through only in DNA when the cell is replicating.
[Bryan Cantrill] [01:07:42] It's not just the DNA. It's also like replicating a bunch of this other goop. It I mean, like, we so in other words, like, we can't just start from DNA from scratch. Is that
[Greg Cost] [01:07:56] Yeah. No. Absolutely. I I think chicken and egg go way back. Right.
[Greg Cost] [01:08:05] I mean, like, you know, people speculate, like, what's the origin of life? Right. Like, I guess, the or in taking this RNA was actually the original self replicating model. Right? And, you know, somehow this started making proteins and, so I think RNA is thought to be the
[Bryan Cantrill] [01:08:27] chicken. RNA is the chicken. Yeah. Okay. Yeah.
[Bryan Cantrill] [01:08:30] Are you having us weighed in on one side of the is there gonna be some other like, oh, I can't of course, he said RNA is the chicken. That's what the RNA chicken people say. Yeah. I I don't have this drugs.
[Greg Cost] [01:08:40] I don't have a horse that was raised really. But, yeah. No. Or chicken. Yeah.
[Greg Cost] [01:08:45] Or chicken.
[Bryan Cantrill] [01:08:47] So RNA predates DNA is kind of the thinking. Yeah.
[Greg Cost] [01:08:51] I think so.
[Bryan Cantrill] [01:08:52] Yeah. Interesting. Yeah. It feels like the order I mean, I definitely found myself, like, way more interested in that origin of life question, I feel. I mean, again, not a deep thought.
[Greg Cost] [01:09:03] Yeah. No. Wait. It's fascinating. In a way, like, he makes this point in the book.
[Greg Cost] [01:09:07] And I've I've when I've taught for junior people, I'm like, no, you got to like, sure, you know this, but like, why does it have to be right? Why why can't why do we need RNA at all? Right. Right. Why why can't DNA just be opened up and be translated directly?
[Greg Cost] [01:09:21] Yes. There's actually nothing stopping that from being true, but it is not true. Right? And, you know, there are there are reasons, like, okay. Maybe you, you wanna amplify a signal, and if you have translating directly off the DNA, you can only make as much as that one copy will get you.
[Greg Cost] [01:09:38] Right? So in fair enough. And then, obviously, you have to replicate your DNA. Maybe it would expose it to double damage and breaks. So there there are certainly, like, reasons.
[Greg Cost] [01:09:45] Right? But, like, there's not it's a little bit of an a priori. It's a little bit of an ugly way to design it. Right?
[Bryan Cantrill] [01:09:53] Yeah. I understand.
[Greg Cost] [01:09:53] Like with tRNA's as well. Right? So these are the the RNAs that have amino acids stuck to them. And they're they're they're what actually decodes the mRNA. Right?
[Greg Cost] [01:10:03] And the ribosomes, this machine that, that, puts our proteins together by grabbing the right tRNA and making sure that the 3 base pairs at the end match, the RNA. Right? I'd say, like, couldn't there have been some, like, more elegant way to do that? It's a little bit. Right.
[Greg Cost] [01:10:22] But, I think it doesn't make sense and exactly if you think that, you know, maybe the RNAs were doing it first and then the proteins kind of came along and ended up helping out. Right? And then DNA was like some sort of cold storage, if you will. Yeah.
[Bryan Cantrill] [01:10:39] Right. I'm talking
[Greg Cost] [01:10:39] about AWS earlier. Yeah. Right. There's, like, the what's it called? Ice cube or something?
[Greg Cost] [01:10:44] Glacier. Glacier, they call it. Yeah. Yeah. Yeah.
[Greg Cost] [01:10:46] That's, like, Dina's glacier. Right? Right. Alright.
[Bryan Cantrill] [01:10:48] Yeah. I didn't realize that the okay. Yeah. DNA is on that that that deep storage. Interesting.
[Greg Cost] [01:10:54] In fact, if you, you know, if, people thought, well, how did how did it's the same chicken egg question. Right? Like, making proteins where you need a ribosome to make proteins, but the ribosome is made out of. It. So how did that
[Bryan Cantrill] [01:11:07] How did that get going?
[Greg Cost] [01:11:08] And and really, it's it's actually that's pretty clear because people solve the structure of the ribosome. It is mostly RNA. Interesting. The RNA is doing all the the chemistry and the heavy lifting. Right?
[Greg Cost] [01:11:19] The proteins are just kind of there to tweak it in the right direction. So it's pretty easy to understand.
[Bryan Cantrill] [01:11:24] To see what the origin of that might be.
[Greg Cost] [01:11:26] Unwind the tape. Right? Like, Yarni could probably do it, just not very well. Right? So Right.
[Greg Cost] [01:11:31] It makes a protein that helps it do a little bit better and then do this selective drive.
[Bryan Cantrill] [01:11:36] The selective drive. And then that is happening in prokaryotes as well as eukaryotes. Yeah. Right. So
[Greg Cost] [01:11:41] this is We have different ribosome, but, yeah, it's
[Bryan Cantrill] [01:11:44] so this is going back to our common ancestor. Oh, yeah. Whatever this is, this mechanism is is and and there's a like again I mean not there's a lot going on in that era that like extended you know again what that's like a 1,000,000,000 years the first 1,000,000,000 years is like a big deal right
[Greg Cost] [01:12:03] yeah I you know any any low probability event times infinite time times a 1000000000 years yeah you'll get something right you'll
[Bryan Cantrill] [01:12:08] get something
[Greg Cost] [01:12:09] you know I that's like maybe a good theme for me in general is like before we had the ability to to study the human genome or whatever or to study a complex organism, people said, okay, I'm going to study e coli or I'm going to study yeast, which is a fruit fly or a nematode. That's going to be a model for how humans work or.
[Bryan Cantrill] [01:12:30] Right. Right. Right. Right.
[Greg Cost] [01:12:31] Yeah. That's what that's what taxpayers want. They want. That's what
[Bryan Cantrill] [01:12:34] taxpayers want. They want.
[Greg Cost] [01:12:35] They want to understand humans and disease and Right. Yeah.
[Bryan Cantrill] [01:12:38] Right, right,
[Greg Cost] [01:12:39] right, right. And so people said or study phages. That was the one of the first ones. Right. Like bacteriophages, right?
[Greg Cost] [01:12:44] The small. And so that was a really a way to study things that were tractable, permanently tractable. Yeah. Reduced complexity. But the amazing thing is to me is one of the big themes in biology, I think, for the past 34 years.
[Greg Cost] [01:12:58] The amazing thing is that really the guts of how organisms work is let's say eukaryotic eukaryotic organisms work.
[Bryan Cantrill] [01:13:07] It's really
[Greg Cost] [01:13:08] kind of the same.
[Bryan Cantrill] [01:13:09] Yeah. Interesting. But there is a lot of value.
[Greg Cost] [01:13:11] Yeah. A lot of that. Just like how the cell decides to stop and go. How that's the internal parts of the cell work. Obviously, there are a lot of differences, but there are a lot of similarities.
[Greg Cost] [01:13:23] Yeah, interesting. From yeast to us. Right. And that didn't have to be true. And I think we just kind of lucked out at a lot of the knowledge that we're able to discover by studying those microorganisms and smaller organisms like flies and worms.
[Greg Cost] [01:13:39] Really, it actually did play out and give a not so indirect understanding of Interesting. A few Yeah. Yeah. Island. Right.
[Bryan Cantrill] [01:13:47] And then when someone comes along with our Kia, you're like, get this out of here. No one wants to see this. What are you doing here?
[Greg Cost] [01:13:55] No. Carl Woesey was a guy who discovered our Kia. Like, definitely under recognized, man. He died a few years ago. Remarkable guy.
[Bryan Cantrill] [01:14:03] Yeah. He
[Greg Cost] [01:14:04] used any insane techniques in a time when, really, people shouldn't have been able to discover what he discovered, and he persisted in don't believe him for a while. It's one of these stories where no one believe for Wildman.
[Bryan Cantrill] [01:14:17] Oh, sweetie. It is a bit of a grand claim.
[Greg Cost] [01:14:19] Oh my god.
[Bryan Cantrill] [01:14:21] It's like, I think I've got a new branch of life. And you're like, okay.
[Greg Cost] [01:14:24] Easy. Yeah. I know. But it was it was looking at different ribosomal RNAs as I recall.
[Bryan Cantrill] [01:14:29] Is how he got it. Using paper electrophoresis.
[Greg Cost] [01:14:32] He was, like, putting them on a big sheet of paper coated in saltwater and putting extremely high voltages across this piece of paper. They probably caught it on fire half of the time. Yeah. And making it radioactive and then spreading out across this piece of paper and then trying to discern patterns from it. Heroic back in the heroic age of technology.
[Bryan Cantrill] [01:14:53] Yeah. That's really interesting. And and then and I think this is also, like, a common theme in the book. You've got a bunch of folks that are ahead of where other people are. It's kind of a lonely spot.
[Bryan Cantrill] [01:15:05] I mean, you've got whether it's Preons or or you kind of, like, ahead of some of this stuff, and it takes a long time for people to catch up and realize, like, yeah. Okay. You you were you were on to something. Yeah.
[Greg Cost] [01:15:16] It's it's just like it's just like natural selection. Like, most mutations are bad. And without being a pessimist, maybe most ideas New ideas are wrong.
[Bryan Cantrill] [01:15:24] Right. But but the ones that are right,
[Greg Cost] [01:15:28] yeah, sometimes they take a while to get accepted because they are so unconventional. Right. And maybe even there's a correlation between the meaningfulness and how the novelty of an idea and how how long it takes to catch on. Because as, you know, Carl Sagan said, extraordinary claims require extraordinary.
[Bryan Cantrill] [01:15:43] Evidence. Right. Right. Yeah. That's right.
[Bryan Cantrill] [01:15:45] That that yeah. I I I wasn't sure if you're gonna go that or you're gonna go with Thomas Kuhn? Scientists, science advances 1 funeral at a time. You know, that's kind of the the the the other side of that. Yeah.
[Bryan Cantrill] [01:15:56] That's really interesting. And then so what do you make of, you know, the actually, can I just ask you about conjoined twins? No. Maybe person. But okay.
[Bryan Cantrill] [01:16:05] No. No. No. I know. I I I this is listen.
[Bryan Cantrill] [01:16:08] If I got legal advice, I'm gonna ask Adam and he's gonna dispense legal advice or accounting advice or medical advice. So I I I want you to be so because one of the things he actually mentions in here is that conjoined twins are the result of an incomplete separation. I don't think that's that's right. I already so the the I read a very interesting book a couple years ago called Mutants that talks about conjoined twins are actually it's like, no. No.
[Bryan Cantrill] [01:16:33] It's you've got you've got these different morphogens that are actually you're it's not an incomplete separation or an incomplete fusion, which is kind of like the conventional idea. But that you are actually have got morphogens in 2 different spots. And so you're actually, like, getting cell differentiation going where it shouldn't be going because you're getting is that
[Greg Cost] [01:16:54] that's an interesting I I so I don't know. Okay.
[Bryan Cantrill] [01:16:56] I'm
[Greg Cost] [01:16:56] not going to try to profess on something I don't really know about. I think, clearly, we do see identical twins happen. Right? So that there must be a process by which there can be separation.
[Bryan Cantrill] [01:17:08] For sure.
[Greg Cost] [01:17:08] And so, is it true that coin twins are a failure of that kind of weird process? Or is it or is it something that's never fated to split? And like you're saying, it's a it's a different type of, unlikely outcome from a development biology because that I don't know.
[Bryan Cantrill] [01:17:30] Because one of the things and and Ball kind of goes into a bunch of these examples in the book where how these very early groups of cells get orientation, get, like, left versus right, and get some of their asymmetry. It kinda got, like, the cilia, and and you've got this turbulent flow that helped to, okay. For the record, you're rolling your eyes a little bit. You're just, like, so you're skeptical on that one that that one's just, like
[Greg Cost] [01:17:53] I don't I I guess with all due respect to the biologist who figured it out, I don't see symmetry breaking as hard just because It's right. The environment out there. Right? And Inching. Yeah.
[Greg Cost] [01:18:03] Yeah. No. What's the first thing that happens to, fertilizer? It travels down the fallopian tube and then implants in the uterus. There's asymmetry right there.
[Greg Cost] [01:18:13] Right? So I I I don't but and I I'm speaking a little bit of ignorance here, so I don't wanna
[Bryan Cantrill] [01:18:18] No. No. That's alright. I will we'll we'll go through our mailbag as we get some of the the I'm sure the well, and and this week, it's, like, a gastrulation, which is definitely a I'd, that's Adam, is that I mean, it's not exactly a scrabble word. That one
[Adam Leventhal] [01:18:31] Not not one that I'd come across for. No. Points. Yeah.
[Bryan Cantrill] [01:18:33] Yeah. The the the I mean, if it's basically if it's a first of all, it's a 2 letter word just like Adam flat out knows that it doesn't even in fact, even if it's not a 2 letter word, but it's in the Scrabble dictionary. Adam definitely knows it. And and if if it's if he he can use it on a rack, he will definitely know it. Once you hit 7 letters though, you begin to get so I when I saw gas relational, Adam, I wondered it.
[Bryan Cantrill] [01:18:52] And you I'd not heard that word. That was definitely Yeah. Yeah. Okay. That was a new one to you too.
[Bryan Cantrill] [01:18:56] Yeah. But interesting about the the the kind of the whole, gastrulation being this kind of development, where you actually get this kind of cell differentiation early, early, early cell differentiation. Or is that my butchering Oh, no.
[Greg Cost] [01:19:12] No. Absolutely. It's, I think the earlier you go back in development, it's we're necessarily in a game where things are very finely tuned. Things can't break in that process. Right?
[Greg Cost] [01:19:28] Or you'll have a miscarriage, for example. Right? So right there's extremely strong selective pressure to get it right. Right. And,
[Bryan Cantrill] [01:19:37] when it's there's gotta be because because this is something that also I've had a hard time squaring with respect to just, like because our pace of evolution is extremely slow, like, very slow.
[Greg Cost] [01:19:48] 20 years versus 20 minutes.
[Bryan Cantrill] [01:19:49] 20 years versus 20 minutes, you got, like, we can't reproduce very much. We don't have very many shots at it. Like, if you're gonna, like, miscarry a bunch, like, you only got, like, the the you do not have many shots at that. Like, you have gotta get it right, basically. Yeah.
[Bryan Cantrill] [01:20:02] It's amazing to me how it gets it right.
[Greg Cost] [01:20:06] Yeah. It's it's, it's pretty stunning. Right? It's pretty yeah. Yeah.
[Bryan Cantrill] [01:20:13] Yeah. So the another thing I want I wanted to ask you about because I the the synthetic biology stuff
[Adam Leventhal] [01:20:22] and the xenobots The last oh, xenobots.
[Bryan Cantrill] [01:20:24] Yeah. Yeah. The xenobots.
[Adam Leventhal] [01:20:26] Yeah. Did this did any of this kinda turn your guys' stomachs at all? Like, I I it it was interesting to me. Like, it was it it was not a little
[Bryan Cantrill] [01:20:36] I don't know where you're going with that one. Did it make you wonder where you know where it is? No. No. No.
[Bryan Cantrill] [01:20:39] No. No. Like, god. I could go some first some frog embryo right now and be so god, like a little cracker?
[Greg Cost] [01:20:45] Like good with a way to make fake frog legs.
[Bryan Cantrill] [01:20:47] It's good. Oh. He was
[Adam Leventhal] [01:20:48] a little he was a little terrifying.
[Bryan Cantrill] [01:20:50] The xenobots.
[Greg Cost] [01:20:51] You should see the frogs. So the frogs they come from Xenopus laevis are big. They have claws. They're aggressive. They thrash around in the tanks.
[Greg Cost] [01:21:02] Most people study the eggs from them. They have to actually inject them to make them hyperopulate. They inject them with exactly like IVF medicine. Right? And you have to squeeze the eggs out like it's big thrashing pincushion.
[Greg Cost] [01:21:14] There's big fossil frog.
[Bryan Cantrill] [01:21:15] You have to squeeze the eggs out. It's like this. So, okay. Why? Why is this like this this frog?
[Bryan Cantrill] [01:21:22] Why? What is it about this frog that
[Greg Cost] [01:21:24] is really big eggs. Big eggs. Big eggs. So it's like
[Adam Leventhal] [01:21:28] Also, they hate them. They just hate these frogs.
[Bryan Cantrill] [01:21:31] They also hate these frogs. I feeling sounds mutual. They're they're,
[Greg Cost] [01:21:36] they're not cute and they're not fairly friendly. But I think,
[Bryan Cantrill] [01:21:41] they've got physically large eggs. Slowly.
[Greg Cost] [01:21:43] And and one of the weird things about these eggs is that, cell division happens in a very strange manner, and that this size of the total mass of the cell and organism doesn't change, but it gets subdivided over and over and over. So it starts out with a huge abnormally large cell.
[Bryan Cantrill] [01:22:04] This is this frog. Yeah. Yeah.
[Greg Cost] [01:22:06] This is
[Bryan Cantrill] [01:22:07] not just like everything. Right?
[Greg Cost] [01:22:08] Or is
[Bryan Cantrill] [01:22:08] it not this is unusual?
[Greg Cost] [01:22:11] Yeah. More so than most. Right?
[Bryan Cantrill] [01:22:13] Okay.
[Greg Cost] [01:22:14] And so you can see these single cell. They're they're big. Right? And Wow. And the first, you know, 8 16 divisions of the of the embryo doesn't the size the total size doesn't change.
[Greg Cost] [01:22:29] It just gets DNA replicated and gets subdivided.
[Bryan Cantrill] [01:22:31] Wow.
[Greg Cost] [01:22:31] So it goes very quickly, and you so you can you can study that process. I think that I I believe that was the intent between studying these frogs, but then, obviously, I guess, Mike Levin, one of the
[Bryan Cantrill] [01:22:44] Yeah.
[Greg Cost] [01:22:44] Pulled off some of these cells and, you know, kind of probably as a stunt. Or, like, I just I think of it as a nice hack. Right?
[Bryan Cantrill] [01:22:52] Right. Right. Right.
[Greg Cost] [01:22:52] Right. Right. Yeah. Pulled off the cells. So I wonder what happens if I break it in this way.
[Greg Cost] [01:22:56] And he, like, dripped some cells off and they kept growing. And then, you know, the cells have their programing like they want to they want to say their blueprint again. Right. Not that I'm calling it that's not in the spirit of the book, I suppose. But, you know, they have their programming and they want to be next to other selves and they want their silia to go in a certain way.
[Greg Cost] [01:23:15] And, you know, for whatever reason, that helps make a normal frog. Right? But when you take it out of that context, it you get these, like, amusing weird like They're called xenobots?
[Bryan Cantrill] [01:23:28] Xenobots. Yeah. And I mean, I thought this is, like, a very interesting question about, like, are these things life or not? They gotta be. Yeah.
[Bryan Cantrill] [01:23:37] I think they're Right?
[Greg Cost] [01:23:38] Right. Sure.
[Bryan Cantrill] [01:23:39] Yeah. The Wikipedia page is, like, a controversy about whether these things are life. Are these robots? Like, I think this is, like no. This is especially guarded with my new brain blowing up about the entropy defying nature of life.
[Bryan Cantrill] [01:23:53] Like, dissatisfied. I think this checks that box.
[Greg Cost] [01:23:56] You know what is life? Right? I I don't know. I mean, there's nature doesn't doesn't divide itself such along such clean lines.
[Bryan Cantrill] [01:24:04] Yeah. Right. Some people, their
[Greg Cost] [01:24:05] viruses aren't alive. I don't know. I'm more like, this man had a biological macromolecules and it can replicate itself and it's alive. So in that case, xenobots are not alive. Right?
[Greg Cost] [01:24:16] Because they clearly are alive because they're out there and doing something in their environment.
[Bryan Cantrill] [01:24:21] And so what do you think about the thermodynamic kind of definition of life? Thermodynamic disequilibrium basically being the definition of life, which is more or less what Phil what Ball was saying.
[Greg Cost] [01:24:29] I think it includes all the things we currently think of life, but it would include some weird things like crystals or something. Right? Which are Right. Probably we don't wanna put in that category, but, you know, on the or or artificial intelligence. Right?
[Greg Cost] [01:24:42] I mean,
[Bryan Cantrill] [01:24:42] Oh, boy. Here we are. Okay. Look. Hey.
[Bryan Cantrill] [01:24:44] Hey. I didn't even bring it up. I didn't even bring it up, Adam. So I you got, like, flip it over. Flip it over.
[Bryan Cantrill] [01:24:49] Did you have an hour and 25 on your card? Because I managed to get through this whole goddamn thing without even mentioning this. I got lots of stuff. You're right. Exactly.
[Bryan Cantrill] [01:24:58] I know and I know you thought that I would not summon the self control. Who knew that it would be our guest who would actually, like, crack the seal? Completely unprompted. Completely believe, brother, I've got this sign that I've had up for for an hour and a half now. This is I'm tapping the sign over and over and over again.
[Bryan Cantrill] [01:25:16] Greg's just giving me weird looks and I'm, like, say the words. Yeah. Well, so I think that, like, that I've I've got I've got a fit I've got opinions about that because I feel that in reading this, Adam Peterson got opinions as well. I think that, like, we just in general, we've done ourselves an enormous disservice by anthropomorphizing these things we've built. And I think that that metaphor so just as, like, I think the machine metaphor is can be powerful but is dangerous and can be overly reductive.
[Bryan Cantrill] [01:25:50] I think the life metaphor for the machines that we've built is also in fact, I think is even worse. And I think is like, no, like this looks nothing like that, by the way. Nothing. Nothing like that. Nothing.
[Bryan Cantrill] [01:26:05] I like this. So this is like these are not the same at all. They look nothing like one another. And, like, go have some frogs hyper ovulate on you that some ornery frogs like, if you wanna go, like, learn what life is, go extract some of these eggs from these hyper ovulating frogs with, like, a bad attitude. Like, that's life.
[Bryan Cantrill] [01:26:24] Like, go go do that. Like, this idea of these kind of, like, of these, you know, stochastic parrots, and our gibber's line. But the this is not these don't look at all like these systems. And, I mean, we can't even be, like, just to be random. Randomness is really important.
[Bryan Cantrill] [01:26:44] Like, these are stochastic systems that these physical systems, it's really hard to be random. Really, really hard to be random. And in fact, it's like to be truly random because cryptography depends on it. We have to be like, it's actually pretty hard to be really, really random. So we can
[Greg Cost] [01:27:02] It was like radioactive decay or
[Bryan Cantrill] [01:27:03] So you they use or like SRAM actually sells can be if you did you can get you have to get the randomness in nature, basically. Okay. And but it's it's really hard. And then everything else is kind of pseudo random from that. Right?
[Bryan Cantrill] [01:27:14] The but these systems don't look any and I think we do ourselves an enormous disservice when we we we because when we conflate them, we kind of think that, like, oh, we've done this thing over here, so it allows us to understand these systems so that the the the synthetic system is gonna allow us to have kinda convey under and I'm just like, no. I don't I I I especially after I didn't buy it going into this book, but coming out of it, I'm like, no way. These things are not at all the same. And there's there's little I don't know, Adam. What'd you do you have a Yeah.
[Bryan Cantrill] [01:27:46] I mean,
[Adam Leventhal] [01:27:46] I guess I guess I had a, you know, looking at, like, neural networks, I, you know, I I think that maybe to your point, this is modeled on our deeply imprecise understanding of the brain. Like, profound and then a simplification of that and simplification of that. The thing I did see in common is sort of like the this is a complex system whose inner operations we don't actually fully understand from first principles. Sure. Right?
[Adam Leventhal] [01:28:14] That Yeah. It's like I'm gonna run this neural network. It's gonna come out some results, and I can't tell you why this weighting is it has its particular value. But, what comes out seems to do what I was hoping it to it would do, and then some other surprising things.
[Bryan Cantrill] [01:28:29] When it's not being racist?
[Adam Leventhal] [01:28:31] What well, I mean, that part is sort of least surprising,
[Bryan Cantrill] [01:28:34] I guess. Right. I guess.
[Adam Leventhal] [01:28:36] Right. Garbage in, garbage out. But I but I guess, I don't know. I mean, I I think that in I I definitely agreed that any analysis that's, like, let's take this imprecise model of our half understood system and then use that as a proxy to understand the original system is full of problems.
[Bryan Cantrill] [01:28:57] Fraught with peril. For sure.
[Adam Leventhal] [01:28:59] Totally agree.
[Bryan Cantrill] [01:29:01] And, Adam has dropped in into the chat, has dropped in an image of one of these frogs. I gotta say, like, I do not wanna pick this. I'd like, no you get its eggs. Yeah. It's a hell of that guy right.
[Bryan Cantrill] [01:29:11] Hell of that guy. That frog too. The and and do you think that the the xenobots because it's an interesting kinda hack. Yeah. Is there anything there that is are are you know, as we kinda look to the future of what's gonna be possible?
[Bryan Cantrill] [01:29:26] Because, again, I feel like with the systems that we engineer look nothing like these biological systems, and we are a long, long, long, long, long way away from making an engineered system that operates like life operates.
[Greg Cost] [01:29:43] Yeah. You know, I remember seeing the xenobots when they came out some years ago. Yeah. Honestly, I kind of forgot about it till I read the book. Yeah.
[Greg Cost] [01:29:50] I don't know. I think it's fairly early. If you talk about trying to, like, sculpt cells or engineer with cells, in a multicellular context, very little is being done with that, to my knowledge. Yeah. Interesting.
[Greg Cost] [01:30:01] There are people who are doing, like, making artificial skin, for example, and that's wonderful, but that's not I don't really view that as related to this. Right? I I don't know. Not my field. Honestly, I haven't followed it, but Yeah.
[Greg Cost] [01:30:15] It seems more like an interesting
[Bryan Cantrill] [01:30:17] trick
[Greg Cost] [01:30:18] to me than
[Bryan Cantrill] [01:30:19] Than than a than a fundamental. Right. Fundamental man. Okay. So what what is your what what are your kind of takeaways from the book then kind of writ large in terms of like you've got the this is, what is the new biology to you?
[Greg Cost] [01:30:36] Yeah. I you know, I don't know. I think I'm a bit of a reductionist. Right? Okay.
[Greg Cost] [01:30:42] In the beginning of the book, he there's a diagram. It's like it has a picture of DNA, and there's a big literally a big black box. And then there's, like, an arrow connecting that. And there's another arrow, and it goes to, like, life. Right?
[Greg Cost] [01:30:52] Right. And so, you know, what's in the black box? Right? And I think that's what the book attempts to explain. I think there are a lot of things that have been covered that really add some depth, some complexity, some richness to that picture.
[Greg Cost] [01:31:06] And it is really complicated. And it's it's more than just a straight linear correlation between the DNA and the output. The environment largely intervenes. Random noise intervene. Molecular fluctuation intervenes.
[Greg Cost] [01:31:22] Absolutely. He's right. That some of the, the metaphor we used to talk about things wrong. Yeah. I don't know.
[Greg Cost] [01:31:31] I think I think clients that he's railing against in some ways got a lot right too, however. Right? For example, there was, we were talking about if you knew everything about the state of information in protein organization in the cell, could you model life? Right? And, this famous biologist, his name is Sydney Brenner, and discovered a good bit of the genetic code and, the nature of the genetic code back in the in the days of the early sixties.
[Greg Cost] [01:32:05] We founded something up in Berkeley probably about 20 years ago now. I don't think it exists anymore. It's called the Molecular Sciences Institute.
[Bryan Cantrill] [01:32:12] Okay.
[Greg Cost] [01:32:13] The premise of the institute was like, okay, damn it. We're gonna we're actually gonna, like, figure out all these all the the numbers and the, over time of, and over the stage of development of of, of all the different proteins and RNAs in a yeast cell. That was their model.
[Bryan Cantrill] [01:32:30] We're gonna simulate a yeast cell.
[Greg Cost] [01:32:32] They're gonna they're gonna understand as a function of, like, the cell going through the like s like replication Right. Or, how how proteins fluctuate against one another. And I think, unfortunately, you'd have to look at all the interactions between the proteins and the muscle. It gets it gets insurmountable very quickly, unfortunately. Right.
[Greg Cost] [01:32:52] But I think that level of detail is where life is happening. Right? It's like, you have a 100000 different molecules of every protein in the cell, and each one interacts with 5 other proteins at some affinity, unless one of them has a phosphate group on it or, you know, and it's it's contextual or unless some RNA comes and binds it. And it's it's it's somewhat unfathomable. I mean, the way we can study this problem is to change the DNA.
[Greg Cost] [01:33:25] Right? Right. So and we can see how that changes those the output of that process. But sometimes it's a lot of hard work and with techniques that are less well developed to understand what happens in between. Right.
[Greg Cost] [01:33:38] To understand, like, you change the affinity of one molecule for another by a factor of 10%. So it's very difficult to measure that, but maybe that's enough. Right. Change to to throw the cell down a new developmental pathway or to have it separating cleave into a new embryo or not. Right?
[Greg Cost] [01:33:57] These things are very subtle. And, you know, I I think I don't know if it'll ever be possible, honestly, to really understand things at that level. But look, a lot of a lot of what he a lot of the new things he's mentioning in the book really add to the picture. Right? I think in particular, no one understood the role that RNA played in the cell.
[Greg Cost] [01:34:23] People thought for sure that it was just mRNA and then tRNA with this decoding RNA. And I think certainly in the past 10 or 20 years, people maybe 20, 30 years, people started to understand RNA is everywhere. Yeah. Interesting. Everywhere.
[Greg Cost] [01:34:37] And, in particular and also, I think one of the other things he brought up was, like, disordered proteins. And and, you know, sometimes disorder is under easily understood. Right? You have pick up you determine the structure of a protein. You see, well, some parts aren't in the structure.
[Greg Cost] [01:34:57] And it's because they're moving around and they don't diffract x-ray as well or even in a, there's a new technique or newer technique called cryo electron microscopy. They you can exist in alternate confirmations hard to resolve. You can understand that pretty easily. It's like a taking a picture of someone playing sports and they're throwing a ball and their hand is blurry. Right.
[Greg Cost] [01:35:17] Because you'd say, oh, well, it's disordered. Yes, because it's if it's doing something.
[Bryan Cantrill] [01:35:22] Right. Right. Right. Right.
[Greg Cost] [01:35:23] Right. That's easy to understand. But what's harder to understand, and I think, very a very almost a foreign concept is something that was discovered in the past, maybe, 10 years about how proteins can exist really almost in their own different phase of matter. Right? Certainly, the conventional way to think about is a protein exists in solution.
[Greg Cost] [01:35:44] There's water around or some salt. The salt is making some of the amino acids and the proteins happy. But the cell's really, really, really crowded place. And there are it's so crowded that I think there's not really enough almost not enough water to go around. Like, the proteins, things things like to be with things that are like themselves.
[Greg Cost] [01:36:07] And that's why proteins fold up on themselves. Right? Because that's the energetics typically energetics minimum.
[Bryan Cantrill] [01:36:12] Yeah. Right. Interesting.
[Greg Cost] [01:36:13] But if you have enough of these proteins that don't have and necessarily have an intrinsic structure, it could kind of bond together and, maybe even form a like, almost a phase that's outside of an the aqueous phase. Right? It's almost like if you have, what would be a great example here, oil and water. Right? Obviously, they form separate phases and you shake it up and then they reassort.
[Greg Cost] [01:36:34] Right? And so I think to many people's surprise, this seems to be able to happen with proteins and maybe RNAs as well. And when I honestly, when I first learned about that, I was really depressed because I knew it meant I knew it was probably true, and I knew it was it explained a lot of things, but it also means it was extremely difficult to study. Yeah. Those are true.
[Greg Cost] [01:37:02] Of our techniques rely on really things being in an aqueous environment. It's extremely Oh. It's it's it's a new area in biology, and, a lot is being discovered about it, but, it's not one that's very minimal
[Bryan Cantrill] [01:37:19] To study.
[Greg Cost] [01:37:19] Study, and I'm worried that a lot of biology is gonna depend on this type of of phenomenon.
[Bryan Cantrill] [01:37:25] And can we does that path of simulating, like, the, you know, the the the like for the project out of Berkeley to to simulate the yeast? Can we if we take this kind of does the thermodynamic approach of kind of like because it feels like so much of this is about optimizing energy and and optimizing the it's so efficient. Does that kind of guide the way we would develop simulation at all? Is that a totally naive question?
[Greg Cost] [01:37:52] No. Totally could. You know, you and your friends have got made computers amazing. Right? And, have enabled computational power to increase to such an extent that, it's now possible to do what are called molecular dynamics calculations.
[Greg Cost] [01:38:09] Now I think several over the over the span of several seconds
[Bryan Cantrill] [01:38:14] Right.
[Greg Cost] [01:38:14] Which is an insanely long time in the, like, sale. Right? But when I started graduate school, they were they were they were looking at, like, picosecond was amazing.
[Bryan Cantrill] [01:38:26] You could simulate a picosecond. Right? Yeah. Right. Wow.
[Greg Cost] [01:38:29] So Bohr's law. Thank you.
[Bryan Cantrill] [01:38:30] Yeah. Right.
[Greg Cost] [01:38:30] Yes. And, you know, that that's the time frame that biology happens on. Like like, you can a protein if it if it's not gonna find a confirmation within several seconds, it's probably not favorable. Maybe it's one of those, like, a prion confirmation, which is probably off to the side somewhere. Right?
[Greg Cost] [01:38:48] Yeah. So I don't know. Could you simulate it? Maybe. But Maybe.
[Greg Cost] [01:38:52] Yeah. Actually. You could simulate the molecule went in its by itself, but it's interacting with
[Bryan Cantrill] [01:38:58] It's a really complicated thing. Yeah. Right.
[Greg Cost] [01:39:00] And then it's complicated in a way that's really favorable for current experimentation. Yeah. Smart people out there, they'll figure it out. Right? Well, I
[Bryan Cantrill] [01:39:07] think it will
[Greg Cost] [01:39:07] be not in my lifetime.
[Bryan Cantrill] [01:39:08] Well, not in your lifetime, really.
[Greg Cost] [01:39:12] Well, more will be learned. Right? Right. But, like
[Bryan Cantrill] [01:39:15] I mean, like, listen. Like, we know you're just trying to be a winner and not die of genetic disease as long as you're like, as far as you're concerned, like, they don't you've you've already
[Greg Cost] [01:39:22] It's not hard.
[Bryan Cantrill] [01:39:24] Yeah. The, and there was a and as someone's dropping into the chat, they, a molecular dynamic machine specific machine that was developed called Anton, developed. Actually, do you know anything about this, Adam? This is David Shaw built this. From David Shaw.
[Bryan Cantrill] [01:39:39] No.
[Adam Leventhal] [01:39:39] I didn't. Yeah. I didn't know about this one.
[Bryan Cantrill] [01:39:41] Yeah. David Shaw, like, made it. It was one of the firms that basically invented high frequency trading. And Okay.
[Greg Cost] [01:39:49] Yeah.
[Bryan Cantrill] [01:39:50] And made a ton of money and then spent it all on this, like, new computational approach for to advance molecular dynamics. I thought it was really interesting. But it's really interesting that you say that this can be a hard that that it was almost depressing to learn that, like, this is probably true, and it means that this is gonna be a hard area to study because it's just hard to get into. It's hard to, like, physically work with. I mean, it's hard to hard to come up with.
[Bryan Cantrill] [01:40:15] So many of these experiments are so creative. I mean, it seems like all so much of this is kinda coming up with the experiment to be able to go explore these domains that are unseen.
[Greg Cost] [01:40:24] Yeah. No. It's it's I think a lot of biology really is a technology driven process. Like, yeah, our ability to assay things when that changes the gold rush.
[Bryan Cantrill] [01:40:36] And all of a
[Greg Cost] [01:40:37] sudden, people use the technology to explore their favorite project, and we discovered this cascade new inform.
[Bryan Cantrill] [01:40:45] Yeah. And he makes a point in there. I think it was interesting, which is, like, we're kind of always exploring the thing that we can explore.
[Greg Cost] [01:40:50] Yeah. Yeah.
[Bryan Cantrill] [01:40:51] And it was like, of course. I mean, that that it sounds technological, but it is also really important because it does mean that, like, as we improve technology and can explore a new domain, it's gonna open up. The thing I felt obviously about the book, I'd rather love to know your take on it. I felt like excited for biology. Like, I can imagine that this book in the kind of in the right 17 or 18 year old would read this be like, oh, this is like amazing.
[Bryan Cantrill] [01:41:16] I got tons of open problems here.
[Adam Leventhal] [01:41:18] Oh, yeah. Absolutely. I mean, inspiring. Right? Like, if you Inspiring.
[Adam Leventhal] [01:41:21] If you are kind of at the prep knocking on the door of biology to just know the the the breadth of problems to be solved. And, also, just, like, the the rate of innovation and, like, there are there's discoveries to be made. Right? Like, it's it there's a potential gold rush.
[Bryan Cantrill] [01:41:40] And it just feels like it's a domain that's gonna change. But that I mean, obviously, has changed a lot because you're coming back to immunology being, like, alright. So much for all that. And I guess, like, so much has changed
[Adam Leventhal] [01:41:48] lots of years. But it feels
[Bryan Cantrill] [01:41:49] like there's a lot is going to change. It feels very exciting.
[Greg Cost] [01:41:51] Yeah. No. Absolutely. It's a lot of open questions. Every organism does it a little bit differently.
[Greg Cost] [01:41:59] So, you know, if you if you're it depends on what you care about. Right? If you wanna study diversity of biology, it's it's an infinite supply. Yeah.
[Bryan Cantrill] [01:42:12] That's well, it's exciting. It felt exhilarating to me to to be and and to think about, you have there's so much information that's been preserved for so long, and that allows the the just the kind of life to do extraordinary that a lot of the versatility that life gets. I Meg it was kind of come one of the interesting points to me that that you have some of this versatility that only comes out under duress or what have you Yeah.
[Greg Cost] [01:42:42] Yeah. Yeah. I I I remember there. So I think you're citing this example in the book about, working with heat shock proteins. Yeah.
[Greg Cost] [01:42:49] I think it was towards the end of the book. And, he talks about this woman, Susan Lindquist. I actually, I almost did my postdoctoral work with Susan Lindquist.
[Bryan Cantrill] [01:42:57] Oh, nice. Okay.
[Greg Cost] [01:42:58] She was amazing scientist. Unfortunately, she passed away a number of years ago, but, it was absolutely fantastic. And, actually, that paper was the paper that really got me interested in her lab. She also studied prions extensively.
[Bryan Cantrill] [01:43:09] Oh, interesting.
[Greg Cost] [01:43:10] Yeah. And, so the concept is really remarkable, and that is, you know, we accumulate mutations all the time. Most of them are bad. But then the idea was that maybe there is a built in occasional buffer system. Yeah.
[Greg Cost] [01:43:26] Right? You can see how that'll be selected for. Right? And so just so there are these very weird proteins, which I don't know much about. They're called heat shock proteins because they're they they are induced to have more of them in the cell when you heat the cell up or when you explode.
[Greg Cost] [01:43:42] The process why they're called shock proteins. They they basically they're kind of like the fire brigade. Right? When things start to go wrong, then the cell experiences some extreme environment. These things get turned on.
[Greg Cost] [01:43:55] And, they they actually, like, help proteins fold back into, like, the, probably, the energy minimum. You're overstating the case a little bit, but they they help get things, The con the confirmation of molecules get back to where they need to be
[Bryan Cantrill] [01:44:10] During this situation of heat.
[Greg Cost] [01:44:11] If they get broken or whatever.
[Bryan Cantrill] [01:44:13] They're getting they're getting denatured because of heat or whatever.
[Greg Cost] [01:44:15] And so the idea the idea is that maybe there are mutations that would cause a protein to hold, but that heat shock protein can fix that. Right? And so, it's a way that, you can offer mutations, but also maybe that protein in their normal circumstances works fine but when you stress the cell the heat shock proteins can't quite keep up would allows that protein to have a different function or break circumstantially under that new under that new regime. And and maybe that is a way to have have what do we get? Double dip.
[Greg Cost] [01:44:53] Right. Interesting. You get the normal function of the protein, but you also get some altered function maybe when you need it. Right? So very provocative paper I'm not sure not sure if the hypothesis is true or not I'll start right it made a good made a good it made a good read when it came out
[Bryan Cantrill] [01:45:09] Yeah. That's that that's really interesting. Well, this has been, it's been great. I don't know if you got other other one thing I think people would be curious about is, like, other books you might recommend for folks that are interested in this that there are
[Greg Cost] [01:45:27] Yeah. No. We talked about, what is life? Yeah. Erwin Schrodinger.
[Greg Cost] [01:45:31] I I I I read that. And we have discussed extensively at the end of this book. That would that was really a a foundational one.
[Bryan Cantrill] [01:45:40] I did feel that there were a lot of, like, foundational biologists that I wanted to, like, learn more about. And then in the footnote, they would explain, like, oh, but also this person's a Nazi. Unfortunately, you're like, oh, okay. I'll be reading the the the the the biography of Il De Mangold anytime soon. I'm afraid the the the
[Greg Cost] [01:45:57] I found the book a bit sanctimonious.
[Bryan Cantrill] [01:45:59] It is a Okay. Okay. We got it. Right? Read the bio.
[Bryan Cantrill] [01:46:01] Alright.
[Greg Cost] [01:46:02] Not not right. I don't know. The books. One that, a lot of biologists have read, I think, is called the Microbe Hunters.
[Bryan Cantrill] [01:46:14] Yeah. Right. Yeah. Yeah.
[Greg Cost] [01:46:15] Yeah. Definitely from one from the heroic age of of biology. It was probably written about a 100 years ago. I haven't read it in a long time, but to my recollection, there are parts that maybe haven't aged, as well as they could have. But, I think captures the spirit of doing clients at the bench by candlelight and bunsen burner lights.
[Greg Cost] [01:46:38] Right. And before the light bulb and, you know, like, it was maybe getting into
[Bryan Cantrill] [01:46:43] the kind of that early history
[Greg Cost] [01:46:45] atmosphere too
[Bryan Cantrill] [01:46:46] it's an atmosphere alright well then that's a good recommendation. Well, this again, this is I I to me, this has been great. I really appreciate you walking us through, you know, you the the domain. The I I don't know if you got any other thoughts here. Were you at any other thoughts from the book?
[Adam Leventhal] [01:47:06] This is a great recommendation, Brian, and definitely a stretch, but one I really enjoyed. So thanks for for pushing me and and pushing a lot of the the folks listening out.
[Bryan Cantrill] [01:47:17] Yeah. And so I'm gonna also share my notes in the chat, so, so folks can see for whatever it's worth, like, the things that the passages that I found that were interesting. Gaurav also has got a bunch of interesting notes and pointers to a bunch of other interesting things. And, you know, his, his take is you know, he's got some, definitely some criticisms of the book or some things that that that he felt that the the book, played down, what have you, but really felt that overall, this is like he said, I was almost in tears by the end. Hard to describe how moving it is to see the fringe ideas that define my twenties put together in such a nice way for a broad audience.
[Bryan Cantrill] [01:47:56] So, there we go. And the bringing fringe ideas to the mainstream here, Greg. Yeah. Yeah.
[Greg Cost] [01:48:01] That was it was super looking. And and, Brian, thank you again for the opportunity to be on here and to talk science. Yeah. That's great. Hopefully not down to you, but, hopefully Yeah.
[Greg Cost] [01:48:12] No.
[Bryan Cantrill] [01:48:12] No. No. It's it's listen. We're talking about, like, eating brains around here and, you know, although I'm I'm not messing with those, the the the frogs.
[Adam Leventhal] [01:48:20] Those frogs. Yeah.
[Bryan Cantrill] [01:48:21] The the those frogs are this is and this is part of the reason why I'm ultimately a computer scientist. Like, I don't wanna deal with a hyper ovulating frog. I don't. You don't. I just like, that is or unless they're delicious.
[Greg Cost] [01:48:35] I don't know.
[Bryan Cantrill] [01:48:40] Adam Adam is, like, Adam, this is, like, the lab the biology lab that that you and I have. You're, like, what do you mean you ate all the frogs? And they're like, no. We've gotta braze them. They will
[Adam Leventhal] [01:48:48] Here's the thing. I ate the first one just for science. Right? And then That's so good.
[Bryan Cantrill] [01:48:52] And then, oh my god. That was good.
[Greg Cost] [01:48:54] You know, my brother, long time ago, he worked, at a mouse facility doing biology in biology. Right? To people doing experiments with mice. And oftentimes, you're making a transgenic mouse. And, so those it's it could be 5050 whether it's inherited or not.
[Bryan Cantrill] [01:49:10] We we do what does a transgenic mouse mean?
[Greg Cost] [01:49:12] You can add a gene to the mouse.
[Bryan Cantrill] [01:49:13] Oh, got you. Okay. Yeah.
[Greg Cost] [01:49:14] So sometimes that happens out of only 1 or 2 copies. And, let's say for your experiment, let's say you want the mouse when you breed the mice. That's like a 1 in 4 chance that a mouse will end up having both copies. Right?
[Adam Leventhal] [01:49:25] Those are
[Greg Cost] [01:49:25] the ones you want to study. Right? Probably. Right? But he would take the ones that were the losers, and he would actually feed them to his snake.
[Greg Cost] [01:49:34] And their life had meaning instead of going into the carbon dioxide
[Bryan Cantrill] [01:49:39] bin. And the snake developed language. No. And also is now a venture capitalist. Jenny.
[Bryan Cantrill] [01:49:45] Okay. Oh, no. No. That that no. Non transcent.
[Bryan Cantrill] [01:49:47] Non transcent. Alright. Well, the the, someone in the chat is saying that is against a lot of protocols.
[Greg Cost] [01:49:58] Probably. Yes.
[Bryan Cantrill] [01:50:00] You know, hey, listen. You go feed this snake then. If you wanna, like, mister mister protocol, mister abide, but it's also the nontransgenic mice. It's fine. It's fine.
[Bryan Cantrill] [01:50:10] Greg, thank you again. Really, really appreciate it. Adam, thank you. Thanks to everyone for for joining us on this one. I thought this was fun.
[Bryan Cantrill] [01:50:17] We'll see when there's the the next grassroots demand for another book club. Adam, it may be never. So
[Adam Leventhal] [01:50:22] That's right. Now that we've smoked the whole pack together. Yeah.
[Bryan Cantrill] [01:50:25] We smoked the whole pack. We really did. Alright. Thanks, everyone.