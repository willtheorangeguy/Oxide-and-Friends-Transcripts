[Speaker 1] [00:00] Alright. So should we get going, Adam? I think we we've got a
[Speaker 2] [00:02] Let's do it.
[Speaker 1] [00:03] I I know we've got another couple of folks that will that will come in. So, as you see, our colleagues arrive, let's definitely get them up on stage. But the so just to to, now, Adam, when had you heard about compliance as a thing? EMC, the the the the electronic data compliance.
[Speaker 3] [00:25] Yeah. So early, but I admit I didn't know what all was involved. I knew that, you know, we we were building this product to this rack scale computer. We were gonna stick it in a thing and we were gonna hope it didn't turn into an antenna. This is the term that I kept on hearing the EEs tell us over and over again.
[Speaker 3] [00:44] Like, that it was gonna interfere with their AM reception or what, but, that was the that was as deep as I understood it, and that was quite a while ago, maybe 2 years ago, if not more.
[Speaker 1] [00:56] And then at the end of it, at
[Speaker 4] [00:58] the end of it, we
[Speaker 3] [00:59] were gonna get something that said it was fine and that we could sell
[Speaker 1] [01:05] it. The executive summary. Yes. Yeah. And I so I think that this is one of these problems.
[Speaker 1] [01:11] I mean, obviously, you know, we're starting a computer company. We we know and you talk to certainly any of the double e's we talked to early on would kind of shutter when they mentioned so EMC electromagnetic compatibility, the EMC compliance, they would kind of shutter, but with without real it was kind of nonspecific angst. And I remember hearing that from a bunch of folks. Do you remember what we did on the metal early on? And we, we had some of the early folks that, worked at Facebook in particular, had described the way they kinda circumvented compliance and the way they avoided dealing with this problem.
[Speaker 3] [01:49] I don't remember that. How how did they how did they circumvent that?
[Speaker 1] [01:54] Did we was that not on the record? Was it Now I'm wondering if that was one evil. Yeah. We're we're comfort.
[Speaker 4] [02:04] Did you did you just unseal?
[Speaker 2] [02:08] Well, good job, Brian.
[Speaker 1] [02:09] Yeah. Well, you know, maybe we weren't supposed to talk about that. But so what they did the story about Sweden's ringing any bells? No? So Amir and Michael sorry, Amir.
[Speaker 1] [02:18] Okay. So if we well, the b sides. Here we are. On the metal b sides. So Amir described how in or they, Facebook needed to they did not wanna to do this compatibility testing.
[Speaker 1] [02:32] I mean, for somewhat for reasonable reasons. This is not nefarious in that we control the data centers. We're not like, this is not a product. We control kind of both sides of this, and so we shouldn't need to like, these regulations don't apply to us. And they did some things that were to make sure the regulations didn't apply to them.
[Speaker 3] [02:50] It's like the motto of Facebook. Right? We control both sides of it, and the regulations don't apply to us.
[Speaker 1] [02:55] I'm pretty sure it is.
[Speaker 5] [02:56] There are some things you can't measure, and so the the it is allowed in the standard that you can do what's called site testing or, you know, basically, you bring an antenna out there and you measure your building to make sure your building is not turning into a megawatt transmitter.
[Speaker 2] [03:11] Right. Did you measure your meter? Big steel box, and you put all the things in the big steel box. You know, it's fine.
[Speaker 5] [03:16] Concrete's very effective as well. But Right. It turns out that if you have a concrete building with windows only up high, you're not gonna measure anything because there won't be any.
[Speaker 1] [03:24] Right. And then they it's like their model is kinda like, hey. This is the data center size computer. Like, the data center is the product. So, like, the the building's the only
[Speaker 5] [03:31] their product. They're not even selling it.
[Speaker 1] [03:33] Right. So, yeah, this all this kind of this makes sense. I that this is understandable.
[Speaker 5] [03:38] Oh, these are gray areas that are well defined. Right. But, you
[Speaker 1] [03:41] know, one of the things that I think I think, Eric, you and Ari in particular gave me real appreciation for is, like, I mean, there are kind of 2 ways to view this. Like, you can view this as, like, oh, this is this kind of regulatory body, and we gotta adhere to all these regulations. And that's that's certainly true. But the spirit of it actually is really, really important. And, Eric, I think it I can't remember if it's you or Arian who had the line of, like, if we did not have this regulatory compliance, if we did not if people did not need to make sure that their emissions fell within these guidelines, nobody would do it because it's kind of it's unseen effectively and nothing would work.
[Speaker 1] [04:18] You would walk into a room and you would have so much bizarre behavior in your life of like, oh, wow. Like, this appliance only works in this room and doesn't work in that room. And if you move this and we already have enough of that with Wi Fi, but it would be much, much worse if we if everyone were just left to their own devices. Is that a fair
[Speaker 5] [04:38] summary, Eric? Absolutely. And what's interesting is the difference between the US and Europe, for instance. The US does not require immunity testing for a lot of things. And immunity testing is we're gonna blast your product with a lot of RF and see if it does anything bad, with bad meaning causes a hazard.
[Speaker 5] [04:58] And one of those things could be like, I make a I make an oven, and the oven turns on when I get a phone call, which is something that you can find videos of. Somebody had a phone on their stove, and it turned on when they Oh. When they got a phone call. I was like, oh, that's terrifying. Okay.
[Speaker 5] [05:18] All all this goes back to, like, you know, back in the days of early radio and TV, you had a lot of interference from random stuff. Like, you turn on your blender and your TV would go on a fritz. And then you have the the more famous incident on the the USS Forrestal, I believe, where some basically, some unmitigated immunity sensitivity caused some rockets to fire, and, the ship nearly sunk, and a lot of people died. And that's all because of the fact that things were not hardened against transients and shocks. And, you know, if you've ever been anywhere that has actual winter and gets cold and dry, you just you know that you need to just be touching something inductive all the time.
[Speaker 5] [06:03] Otherwise, you're just gonna shock the hell out of yourself every time you
[Speaker 1] [06:06] move. Oh my god. That is such a visceral. I you know, Eric, I grew up in Denver and but have basically lived in a in a more humid climate for but just the way you describe it, I immediately recall. Because Adam, I'm not sure you've ever lived in an arid climate like that, where I mean, I used to you get so zapped.
[Speaker 1] [06:23] I mean, you would walk across carpet and if you didn't, if you weren't careful, I mean, yes, you would get absolutely zapped. So yeah, I mean, all this stuff is, is really important and. You know, again, you can kind of view it as, as unfortunate, but it really is the wrong way to view it. It's really necessary, and it's part of of, you know, an engineer's responsibility to our kind of broader societies that make sure that we I I and I try to remind myself of that whenever whenever we are having authority issue that we need to resolve as part of this. So and, Ariane, when you first joined the company too, I mean, obviously, one of our earliest engineers that I I I just remember, you know, as you, you know, because you you're someone who kind of has been on both the software and the hardware side, and just your descriptions of, you know, the these these fields kind of traveling from 1 in in they're kind of, traveling under advisement.
[Speaker 1] [07:22] Like, they're not actually with these things that we view as, like, wires. That's just kind of, like, advice. That's not necessarily where these things are gonna travel, where these fields are actually gonna be. And these things are just super, super, super complicated. So I remember getting so we, as we were kinda growing the team, and Eric, you, and Nathaniel, and we had a couple of folks that had come from, from the the the GE side and had done CTs.
[Speaker 1] [07:52] And you had done compliance a lot on very big high current, high voltage kind of things. And I think your line early on was, we will absolutely find things. They will be resolvable, but we will find things. And, I I maybe the the place to pick it up is with the pre compliance that we did. It all blurs together, but I think that that was in I mean, was that was that June?
[Speaker 1] [08:18] I think it was June of 2020.
[Speaker 6] [08:20] 2nd 2nd week of June or 1st week of June.
[Speaker 5] [08:23] That was June in Texas.
[Speaker 1] [08:25] In Texas. So, the
[Speaker 4] [08:28] So hot.
[Speaker 1] [08:29] It it was. And the so what's the I I maybe describe some of what we do. Like, why do what what does even pre compliance even mean? What what what were we trying to to because the the the I mean, the RAC space could come together for the very first time. So what are we trying to find down there?
[Speaker 5] [08:47] So, basically, like, there's all these theories and books and whatever you can read on how to design things to not, you know, become big violators of EMC, but the proof's in the pudding. And all those books and examples are usually based on small devices that have fairly simple interconnects. And whenever you get into the real world and have to do large system integration, all that stuff just kinda goes out the window and everything conflicts each other, and you have to kinda make your best your best guess of what's you're supposed to do. That'll work well.
[Speaker 1] [09:18] Yeah. So this is a really important point because a question that I think has come up that came up certainly something I had, I think, other people have had is, like, wow. Can we really can we can't simulate this. And the answer is basically, like, no.
[Speaker 4] [09:29] We can't we can't.
[Speaker 5] [09:31] The the software companies want you to believe that they they can simulate it, and they're like, well, look at this, you know, f 35 simulation and this radome. It's like, you can simulate all the emissions off this thing. It's like, well, sure. If you have an army of a 1000 people, and all you do for, like, 7 years is put every possible detail of your system into this tool and then spend, you know, $1,000,000 computing it. Sure.
[Speaker 5] [09:53] You can simulate some things. It's still not gonna be right. Like this
[Speaker 1] [09:59] And in any kind of errant component, can any I mean, you get one of those details
[Speaker 5] [10:04] component. It could be a setting in your component. It could be a batch, a lot, an undefined behavior. I saw one where there were 2 equivalent parts that could be on a a bill of materials for a board. And one of them, when you debt short it, behaved fairly benignly and just kinda turned its output off.
[Speaker 5] [10:21] The other one kept retrying, and that retrying happened to excite a resonance in the cable that was about 20 meters long. And it just screamed an EMC. And so then some porpoise and had to go and rework, like, 300 of these boards to swap out the part because that part had an undefined short circuit behavior, which was safe, but, you know, it wasn't defined in terms of EMC performance. And so we found that randomly on a on a visit to the chamber. We're like, oh, no.
[Speaker 5] [10:54] What's that? That's awful.
[Speaker 1] [10:57] Okay. So in what is the It
[Speaker 6] [10:58] can be even worse. Like, you you if your if your supplier go comes up with a mic with a if you basically get a a an an process node change where you go from a larger silicon process to a smaller silicon process, your edge rate of all your transistors is gonna go up. And that by itself may just mean that, stuff is gonna start radiating because Right. Yeah.
[Speaker 5] [11:21] You'll you'll start getting worse effects from the same board.
[Speaker 1] [11:25] Well, and it's it's just the whole idea that, like, oh, yeah. Your your edges get sharper. And as a result, you actually are now resonating with this component that you weren't resonating with before. Now this now you have this holy cascading failure that is actually there's much more energy involved than just the energy of the part, which is crazy just because the system is so complicated. So what is the chamber?
[Speaker 1] [11:46] What let's describe the the chamber a little bit.
[Speaker 5] [11:49] For for any Star Trek fans out there, the chamber looks like a holodeck, and that's that's a side effect of something inside of it. But, basically, it's a giant steel box, and then it has ferrite, which is a material that conducts RF energy fairly well, but is absorbent. It it turns it into heat. And then you have this foam on top of that. So it's a steel box, and then it's lined with these ferrite tiles, which are, you know, maybe a 100 millimeters aside.
[Speaker 5] [12:18] Those are all glued to the entire inside surface of this thing. And then inside of that, you have these, like, pointy or wedge shaped or some other funky shape carbonized foam. And the carbonized foam is also an EMI, you know, EMC, EMI, RF, whatever term you want, absorber, where radio frequencies will go into it, and they will turn into heat. So the whole point of this is to create what's called an anechoic chamber or a semianechoic chamber, so a SAC. So the SAC is sometimes an an acronym that you'll hear, EMC chambers called, and SAC just means semianechoic chamber.
[Speaker 5] [12:54] So that means 5 walls of the box are lined with this ferrite foam stuff. And then the bottom is just straight steel, and the steel can reflect, radio waves. And so, basically, the whole point of this chamber is to simulate the conditions of this device that they're testing being out in the middle of space and not having anything around it. So it shields both your device from all external fields, so, like, the the radio transmitter tower that's right down the road or the FM station or the cell tower, and also shields your noise that you're creating, from getting out of the room. And so the whole point of this is to measure your device in isolation in a perfectly quiet, quote, unquote, electrically quiet room, and then measure the very small signals that come off of your device against a a standard using an antenna and a turntable, essentially.
[Speaker 1] [13:52] Yeah. And so that how it's a I mean, a bunch of things. So one is that this is so on the one hand, this is simulating. We're trying to keep it quiet around this device so we can understand what this device is actually emitting. It does mean that in principle, you could have 2 devices that you could combine in ways that could kind of positively reinforce one another.
[Speaker 1] [14:11] But it's part of the the the purpose I mean, currently, I'm wrong here, but it's like the the purpose of the standard is, like, to minimize the odds of that, not to make that impossible. It's not gonna be you you can't make that impossible.
[Speaker 5] [14:23] But we're Yeah. It's a game of statistics. Basically, the the whole standard is trying to make it statistically improbable that a combination of arbitrary things in some space is going to cause a problem to something else.
[Speaker 1] [14:36] Right. And, Adam, if you ever go into one of these chambers, as as people will tell you as you walk in, do not bring your cell phone in, because your phone will search for signal and it will not find anything. So your phone will begin to actually drain a lot of battery as it's aggressively not finding it thinks that you're in space. And It'll turn up
[Speaker 5] [14:56] its output power until it's maxed out, and it'll just sit there and happily drain your battery in an hour.
[Speaker 3] [15:01] Fantastic. And in this picture, Arne, that you posted, was that from the pre compliance or that that was from the actual,
[Speaker 6] [15:09] real deal compliance? Yeah. That is the run from, what is it, 2 weeks ago?
[Speaker 5] [15:14] Okay.
[Speaker 1] [15:15] Yeah. That's a real deal compliance.
[Speaker 6] [15:17] Actual chamber that we were in for the past couple of weeks.
[Speaker 1] [15:20] And so what did
[Speaker 3] [15:21] the what did the Texas yeah. What did would the Texas experiment
[Speaker 5] [15:24] show us?
[Speaker 4] [15:24] What what did it look like?
[Speaker 1] [15:26] It was a little rawer.
[Speaker 3] [15:29] Like, cowboy chamber? What do we how raw are we talking?
[Speaker 5] [15:33] Yes. No chamber. Wild Wild West. No chamber. It was an open air.
[Speaker 5] [15:38] Basically, we were in a back room, which is like the loading dock because the chamber was too small. Yeah. These these are the things you deal with when you have short time and, you know, just need to get in there. And so we had, basically, our rack sitting in a loading dock with, you know, nobody quote around it, and then we just manually moved an antenna around it.
[Speaker 3] [16:03] Yeah. Was this useful? Did did
[Speaker 1] [16:05] we did we learn stuff from it? Yes. This was extremely useful. Yeah. I was just gonna say, so this is a a this was extremely useful.
[Speaker 1] [16:13] And I mean, for so many different reasons. 1, I felt it was just, like, useful for people like me to just to get education about what this whole thing is and what's involved here. And but for us, it was extremely useful. One, we wanted some very concrete things we wanna get into. And then, but we also, you know, we're also having to bring the whole thing together.
[Speaker 1] [16:35] And just the process of I mean, in many ways, like, our first customer was in this loading dock in Texas, and we learned a lot. I I think we learned Eric, I RFK, Arian, I think it's fair to say that we learned that we did not wanna have to bore holes in the actual product in order to be able to communicate with it. I feel that that was one of our our big takeaways.
[Speaker 5] [16:57] That was a that was a good takeaway. It it's funny because wherever I've been, you know, early EMC testing was always, like, a very big rally point for software integration because that was kind of generally the first time where, like, everything had to be working together and be in the hands of nonexperts.
[Speaker 1] [17:18] Yeah. Yeah. And it's it's it Lot
[Speaker 5] [17:23] of lot of lot of stuff gets figured out. Real quick.
[Speaker 1] [17:26] Gets figured out. And, I mean, in in in pre compliance, it was great because we figured out a lot of stuff that we had to go do and a bunch of stuff that we knew about and a bunch of stuff that we you know, there's also the stuff that you know about, but the priority becomes much higher in your mind after and, you know, we had designed this thing with the the technician port and the ability to access this thing via the technician port, it was going to be a lot of work to be able to go do that. But coming out of that compliance, like, we gotta, you know, obviously prioritize that work and and a bunch of folks, Matt Keeter and and Aaron and Arin, you had a bunch of folks that did terrific work, Ben Nacker on getting all that, that that kind of that whole connection made and being able to we it was just we learned a lot in pre compliance just from a product perspective, software perspective. But then, Eric, we learned something actually really important from an admissions perspective as well.
[Speaker 5] [18:16] Yeah. So we initially found that we were doing both radiated and conducted, and radiated is basically put an antenna nearby and see what you measure. Conducted is put a clamp around, basically, a current transformer around your power cables or any other cables that come off your device and see if there's electromagnetic energy on those. And so we saw some on conducted emissions, and we were using, an off the shelf power shelf, essentially, with rectifiers that was that was basically unmodified by us, and we're like, this is weird. What's happening?
[Speaker 5] [18:53] And so we asked the the vendor who makes that, like, hey. Do you have some test reports you could send us? Because we saw something that would cause us to fail. And if you have to do conducted emissions mitigations, radiate emissions is not as nasty because, generally, the the the physical modifications are small. Conducted emissions means you have to put some, you know, basically cinder block sized thing of filtering on your power cable, and it gets very scary.
[Speaker 1] [19:29] Just remind, you know, lead time. Our lead time so these are rectifiers, the Murata rectifiers. We had, had had actually some supply chain issues, and I, and I don't know if I can remember if I if I if I told you this or not, but we there was a moment where we're like, oh, god. It's gonna be the lead time and rectifiers is so long. Like, how hard can it be to do our own rectifier?
[Speaker 1] [19:54] And, Eric, I just remember you being like, listen. I would like everyone who would like to build their own rectifier to to come over here, please. Oh, god. We're gonna learn how to build our own rectifier. And you were just like, I am now gonna sit you down and explain why you will never again say we should build our own rectifier.
[Speaker 1] [20:08] I'm gonna explain to you how complicated a rectifier is. Because the question of, like, how complicated can a rectifier be? I felt you gave some good answers to that. The answer is exceedingly extremely complicated. And I mean, you think it's like, you know, the, the, the most basic elements are still so fiendishly complicated, and I think we decided that it was a lot easier to help them get the FET that they needed or whatever it was.
[Speaker 5] [20:36] Yeah. Yeah. It was a, like, a a rectifier like, a a world class server rectifier is basically like a three-dimensional puzzle filled with complex hand, you know, handmade hand designed, like, custom components. And all those components are made by a bunch of different suppliers, and they're all very manual and that there's, like, wires wound, and there's special shapes of ferrites, and there's always, like, mechanical and magnetic bits that fit together like this big puzzle. And then you have to also make it, EMC compliant, so there's filtering inside of them.
[Speaker 5] [21:12] And then you also have to make them cheap. And yeah. Oh, wow. Right.
[Speaker 1] [21:16] And and efficiency too. Right? I mean, efficiency is super important.
[Speaker 5] [21:18] Yes. Extremely efficient. So these things are, like, insanely efficient. And it I I hopefully drove the point home that we will not be making our own rectifier anytime soon.
[Speaker 1] [21:30] Oh, you drove that. You definitely made us smoke the whole pack. I mean, I definitely was like,
[Speaker 5] [21:34] you're Yeah. You're you're gonna light all these cigarettes, and you're gonna just start dragging on them. Right. No. Keep waiting for call them.
[Speaker 5] [21:40] Keep sucking. Let's go. Right.
[Speaker 1] [21:42] Well, and
[Speaker 5] [21:44] Yeah. So we so we called Murata. We're like, okay. What what are we doing wrong here? Like, you you obviously they have to pass their own emissions, so they're certified independently, whatever.
[Speaker 5] [21:55] And so they sent us a bunch of test reports from, you know, a bunch of different test houses, TUV and Intertek and UL and all these other places. And so I've I've been on the receiving end of a lot of these reports from subtier, you know, vendors, at my time at GE, and many of them are just kinda like, oh, yeah. That's how you tested it. Yeah. Okay.
[Speaker 5] [22:17] That's gonna make you look a lot better. Oh, okay. Yeah. So I've I've been on the receiving end of really crappy reports where they, quote, tested it, and it's like, yeah. Sure.
[Speaker 5] [22:27] If it's, like, this perfect ideal setup, yes, And you have tiny, tiny cables or whatever. And just poor measurement techniques or whatever where it's technically compliant, but they weren't exactly doing their due diligence. The reports I saw from Arata were just phenomenal. Like, everything was beautifully set up as it would be in a rack. The thing was in a, like, rack style chassis that was sitting on the floor like a rack.
[Speaker 5] [22:52] It wasn't just, you know, sitting on some foam and, you know, perfectly, like, whatever. Now it's like, no. There's stuff on here. There's things that would radiate. There's all kinds of stuff.
[Speaker 5] [23:02] And I saw their data on it, and it's like, okay. Yeah. Their data doesn't look anything like ours. And then I started looking at the frequencies that they're showing up because you always see some stuff from the switching power supplies in these things even if you're well below the limit. And none of those frequencies lined up with any of ours.
[Speaker 5] [23:19] And so, basically, the conclusion was, yeah, there was something wrong with that test.
[Speaker 1] [23:24] Oh, interesting. Right. Because I think I mean, we we were looking at how we were grounding at the chassis at one point, but you felt that the the ultimate conclusion of that was just like the test was
[Speaker 5] [23:33] The test was garbage. It was it was a it was an it's hard to do those kinds of tests because they do pick up a lot of extraneous crap, especially in open air test chambers. And so it's it's very hard to do that, and we were I think that was late at night, and we were kinda rushing. And so I I don't particularly blame the test house on that one. It's more of just a a side effect of we weren't paying enough of attention to say this is right or wrong or otherwise.
[Speaker 1] [24:00] But very valuable for us to go in and just even getting their test results and understanding it. I mean, because that was not really something in the hindsight we should have, but was not something we were looking closely at when we were kind of evaluating the these various rectifier folks.
[Speaker 5] [24:15] But Right.
[Speaker 2] [24:16] Because they're
[Speaker 5] [24:16] they're supposed to meet the standard, but it turns out they have to meet the same standard our whole rack has to meet. So
[Speaker 1] [24:23] And this is, like, also a really important point in that. I'm not sure. This is definitely something that was, not necessarily obvious to me, but the that the EU, I mean, should be obvious, I guess, that if you take a bunch of things that are themselves FCC compliant and comply with the relevant regulation, and you put them together, the thing that you have doesn't necessarily comply. Like, it's actually pretty easy for that to happen.
[Speaker 5] [24:48] Yes. It's almost guaranteed.
[Speaker 1] [24:50] Right. Almost guaranteed.
[Speaker 5] [24:53] You you have to meet a higher standard at a system integrator level than the sub components have to meet.
[Speaker 1] [24:59] Right. Because all this stuff also adds up. So you can have something that is like, well, yeah, if you had one of these things, it's actually not a problem. But you have 6 or you have 32 or you have 4. You and because you've actually added up the actual energy that these things are emitting at this particular frequency, yes.
[Speaker 1] [25:17] Now you're no longer compliant, and sorry for you. So, definitely so, yeah, Adam, to answer your question, that I thought the pre compliance I mean, RFK, Ariane, you guys were also there. I thought it was it was hugely valuable, and we we learned just a lot about the product and a lot about what we needed to go do.
[Speaker 6] [25:35] It mostly exposed how not ready we were for it, which was, you know, the wake up call we needed. And we vowed that we wouldn't be so unprepared going into the chamber the next time. And Yeah.
[Speaker 1] [25:47] There I say, we're
[Speaker 5] [25:48] better people to that. It's hard to do that with words.
[Speaker 1] [25:50] Yeah.
[Speaker 6] [25:50] It is. We're a little bit better prepared when, like, not too like, I won't give us too much credit, but we were a little bit better prepared. Just, you know, a hair.
[Speaker 1] [26:00] Yeah. I think Before
[Speaker 3] [26:01] we move on, Brian, you said we learned not to bore a hole in the product to to wire things up. Did we learn that the hard way or the easy way?
[Speaker 1] [26:11] Oh, no. For sure. The hard way. I mean, like, sorry. I mean, it obviously
[Speaker 3] [26:14] Why do we who who? Okay.
[Speaker 4] [26:16] Because we have to run with all the
[Speaker 6] [26:18] dongles in. We we had We had to Yeah. Okay. We had no No.
[Speaker 5] [26:20] We had to have those adapters.
[Speaker 6] [26:21] Control the thing. We had all the debug adapters attached to all the systems, So we had to drill holes into the chassis so you can get these cables out.
[Speaker 2] [26:29] We gotta turn it on now.
[Speaker 3] [26:30] That makes sense.
[Speaker 1] [26:33] I mean, you have to you like, when we put the sleds into the rack, there's a a degree to which we've launched this thing into space, you know, and we the the things that we are used to dealing with on a bench, we don't have anymore, unless you wanna drill a hole in the front of the, of the sidecar, which is what we had to do because we and we thought that we hadn't thought about this problem. It's just that, to Ariane's point about, like, with the stuff that we still had to build, there was a and the the the connection from the technician port into a into a or a sidecar, new compute slider, or a network switch. I mean, it is a crazily complicated path that involve I mean, like, it's not like we were close to having networking. There was a lot of stuff that had to be built. Now we
[Speaker 5] [27:13] Yeah.
[Speaker 1] [27:13] We did a terrific job building it over the next, you know, whatever it was, 6 weeks. Right? It was a lot of stuff that needed
[Speaker 3] [27:18] to be built.
[Speaker 4] [27:19] And for folks
[Speaker 3] [27:19] who haven't seen the sled, there's no, like, USB or KVM or any of this baloney. Right. It's like u dot twos out the front and out the back is blind mated power and in, like, in Ethernet, like, 200 gigabit Ethernet. And that is it. So there's no there's no none of the Goober ports that you have on your standard server.
[Speaker 6] [27:41] And and Ethernet is in a non standard form factor, so it's really not usable in any way, shape, or form other than connecting to our execs our, like, exact switch.
[Speaker 5] [27:51] And your laptop doesn't have a 100 gig Ethernet port.
[Speaker 2] [27:54] Yeah. And this is all plugged into, like, a fully integrated backplane. So, like, you you you've got anything on the front, and there's nothing on the front, and that's it.
[Speaker 5] [28:03] Yeah. And it now that we built up the infrastructure, it's like, that's not really a problem. But back then, that was a problem.
[Speaker 1] [28:09] What was a problem that could be solved with a drill? And that's what we ended up doing. And the and just I get I just remember, I mean, just learning a lot. RFK, you know, I said, I just we're sitting in that, like, the the kind of the pulled up table in this garage, basically, learning, like, we've got a lot of work we need to go do to make this thing, actually.
[Speaker 2] [28:30] Oh, yeah.
[Speaker 4] [28:31] And I mean, the other thing that thing
[Speaker 2] [28:33] in it last to boot was, like, a real real grinding, you know, very visceral, like, I'm sitting here waiting, watching watching it boot, and it's just taking forever. You mess up once? Oh, well, here you go. Take a lap.
[Speaker 5] [28:45] Aren't we weren't we loading, like, the boot ROM out over, like, a 115 k bot?
[Speaker 2] [28:50] That you are This was well, this is where we figured out that the actual image could be changed, and that was great. That changed a lot. That that, you know, we went from, like, 30 minutes to, like, you know, 15
[Speaker 1] [29:03] Yeah. Which
[Speaker 5] [29:04] is a big deal. So the the the one thing I will say for pre compliance testing is it showed us that we weren't screaming our heads off. So the the real thing that I wanted to check, like, going into that was that we didn't have anything that was basically visible or off the charts in pre compliance because if it's off the charts in pre compliance with 1 sled or 2 sleds or even 3 sleds and one sidecar, which is our network switch, it isn't gonna get any better when we have 32 SLEDS and 2 sidecars. Right.
[Speaker 1] [29:34] Yeah.
[Speaker 5] [29:34] And so what that did is it told us that, hey. Okay. We aren't completely out of, like, out of bed in terms of being able to get this done, and we don't have, like, major redesign to do before we get this. There there are some things we found that we wanna improve, obviously, but it's those were found later because they're basically so hard to see at that point that, you know, they were not visible in the noise.
[Speaker 1] [30:03] Right. And and I think, you know, this is whenever you're solving a kind of big, hard systems level problem, you do wanna get to that things that are potentially unbounded risk you wanna get to as quickly as you can. I don't and I don't think I don't think we could've done pre compliance any earlier than we did. I think there was plenty of blood on the floor as there was. But I thought so it was really valuable for that to and to understand, like, okay.
[Speaker 1] [30:28] We don't we're we've got a lot of work to do, but we're it's there there is nothing that we have got that is obviously a disqualifying from a compliance perspective. I think it's the conclusion coming out of that. So As we thought. It that's what we thought. Right.
[Speaker 1] [30:45] Exactly. Well, and then so but it was also just also just very educational and interesting. I mean, Adam, watching this debugging process is super interesting and, you know, RFK, you know, you've come you you, you know, kind of came up as an RF engineer. So this is I I kinda felt like you were just, like, welcome to, like, this is my land. Like, I know I did this is They should feel all good.
[Speaker 2] [31:05] And, you know, you're all warm and fuzzy for a little bit, and then they're, like, go back to designing, you know, differential signaling, and they're, like, oh.
[Speaker 5] [31:11] Feel feel my pain.
[Speaker 1] [31:13] Right. Go back I know. I I think you we get, you know, send you back to, you know, I squared c translators or whatever. You're just like, no. Actually, like, this is this is right.
[Speaker 1] [31:20] Like, to be, like, the with the antennas in this chamber kinda figuring out what's emitting what. So It's fun. It it was really neat. And it's like these also out of new, like, these these test facilities, particularly that one, which was definitely felt like a like, a haunted test facility. I mean, there's just like all of these kind of cadavers of various large equipment kinda lying around.
[Speaker 1] [31:40] I mean, it's definitely, I feel like a Scooby Doo mystery should be had in in a in the chamber for sure.
[Speaker 4] [31:47] Was the control room also isolated like a Faraday cage?
[Speaker 5] [31:52] So it depends on the chamber. So one of the chambers we were in, it does not. The the chamber that I used to work in was not. It doesn't have to it doesn't have to be because everything's shielded and pretty well quiet anyway. So it's just the you have big filters to get stuff in and out of the chamber.
[Speaker 5] [32:11] But, the one that we were most recently at does have the the control room in it, like, a little antechamber that is also a Faraday cage, which makes it more obnoxious to
[Speaker 4] [32:21] be able to test convenient.
[Speaker 5] [32:23] Fair. I can't take notes on this because all my stuff is disconnected. Great.
[Speaker 2] [32:28] And, I mean, it has, like I mean, sometimes it's important for that kind of thing, like, where you do get some, like, stray signaling. But, like, you kinda don't need that. No. It Especially if you got customers
[Speaker 5] [32:41] that are crappy cables.
[Speaker 2] [32:43] Yeah. That that's, like, that's where you would get stuff that would come through. Like, we were running there's, you know, Ethernet that runs all the way into the floor of the first chamber, and it comes out of a certain port in the second chamber. And the barrier for that port had been dislodged from the floor, so it was rendered, but it was basically useless. And so the okay.
[Speaker 2] [33:00] Well, now, like, anything could, like, potentially come through there, and so, like, alright. Well, we got the second chamber, and you close that door, and you're like, okay. Well, we'll really stall it now. Nothing's gonna just sorta get in. And we there were some random things that we saw, like, once or twice when we didn't shut that door, but, generally, you don't need to do that.
[Speaker 5] [33:19] Yeah. For terms of generation, I need that.
[Speaker 1] [33:22] And I do think and as some folks are saying in the chat, before leaving Austin, we we really do need to mention the barbecue. So CJ Mendez is on the Oxide team, who's played an instrumental role in a lot of the the the logistics and operations of this compliance. CJ, lives in Austin, and, boy, did he hook us up with the Franklin's is kind of the canonical barbecue in in Austin, Adam. And, boy, it's, it's canonical for a reason. That that that brisket was just absolutely something else that was Yeah.
[Speaker 6] [33:56] Well, it divides Austin into 2 camps because there's another place that is like, half of Austin says Franklin's and the other half says the other place.
[Speaker 1] [34:05] But And I think the I mean, I think they're both right.
[Speaker 5] [34:07] I think they're both Yeah. I don't care. They're both just
[Speaker 1] [34:09] Oh, right.
[Speaker 3] [34:09] No. I I
[Speaker 1] [34:10] I will take I will take them both. Anyway, that it was it was really, really, really good. I kind of felt like it was a little bit of like a Pepe's moment for me.
[Speaker 5] [34:18] There you go.
[Speaker 1] [34:19] Bring it back to new Haven. Yeah. Going to new Haven and be like, people have been people. Adam has been so insuffer about this pizza that I really don't want. Oh, damn it.
[Speaker 1] [34:27] This pizza's really, really good. Pizza's actually damn it. Every bit as good as Adam has been saying for the last 2 decades.
[Speaker 4] [34:33] There you
[Speaker 1] [34:34] go. But and, as it is with awesome barbecue. That was great. Barbecue was terrific. And saying we we left pre compliance with, this Murata thing to chase down, and Eric mentioned that.
[Speaker 1] [34:44] We got that kinda chase down, and then a whole bunch of work that we needed to go we knew we had to go do, not just from a compliance perspective, but just to get the whole product together. And and team really did a terrific job. And so fast forward to December, it doesn't feel feels like feels like it was several years from June to December, but I guess it was only a couple of months. It really does not feel that anyway, the time and space have been destroyed. So then we were, phonetically getting ready for a, our compliance run, trying to get in.
[Speaker 1] [35:20] And so it's worth mentioning too, Eric, that these chambers, like, you have to book them a while in advance. These things are a finite resource, and this is not like a Wendy's. You know, you've gotta actually you gotta book these things long in advance, and people do cancel, and you can kinda get last minute stuff, but it's a scramble to, do you can't kinda negotiate your date generally that much. That's that's
[Speaker 4] [35:46] that's I wonder if the chambers right? It's
[Speaker 6] [35:48] the shit
[Speaker 4] [35:49] as well.
[Speaker 5] [35:50] It's both. Yeah. The they it they don't yeah. People don't usually run 3 shifts. They'll run 3 shifts if things go long, and people are willing to stay.
[Speaker 5] [36:01] But, like, gee, when whenever the the chamber schedule would open for the next, like, quarter or 2 quarters, it would be filled within a day with people, like, staking their claim on it. And then there was all this horse trading and threatening to go to upper management to get priority because we have our own chambers. Oh, is this this whole political, like, charades and just this all this chess maneuvering to, get chamber time. But it is a very, like, precious resource, and these chambers are exceedingly expensive. And so being the you know, being that we're, like, operating on short timetables makes it a lot harder.
[Speaker 5] [36:44] But being flexible, thanks to the the folks in Emeryville and saying, listen. You tell us when to be there, and we'll get in. Gives you a lot more, a lot more leverage to get into somewhere because you can adapt to people canceling.
[Speaker 1] [37:02] Yeah. And so we were pushing hard for this December date, and, and we the team did I mean, it it Eric, you said this earlier, this is kind of a these compliance runs tend to be big rallying points, huge rallying point for us, pulling together a bunch of different hardware and software. We I feel like even though it's not related to compliance per se, I do feel that it's worth talking about one of the mishaps we had on the way where we discovered that the the shark fin, which is what connects the our our drives in the front, the u dot 2 drives have they've got a u dot 2 connector. That's connected to a PCI connector, and they're the the shark fin kinda mounts vertically in there. And, Josh, I think you're the one who initially tripped over this issue
[Speaker 4] [37:52] If if Yeah. At, like, at, like, 3 in the morning.
[Speaker 1] [37:55] Great. So what were the symptoms of this issue, as you recall?
[Speaker 4] [38:00] Didn't work at all, but the lights came on funny, and then they went off funny. Sitting there like, well, that's funny. These little don't think it should come on and then kinda fade out like that. That's not good.
[Speaker 1] [38:13] It's not good. And so
[Speaker 4] [38:14] And nothing worked at all.
[Speaker 1] [38:15] Nothing worked at all. And there, you know, Josh is the one who's kinda been pulling this together from a hardware and software perspective. You know, you kind of have, like, well, maybe I've maybe I've done something wrong. I don't know.
[Speaker 4] [38:27] It doesn't feel like
[Speaker 1] [38:28] you've done something wrong, but maybe maybe there's, hopefully, there's some pilot error to be blamed here, but as it turns out, no, You've done everything correctly. You'd just been you had encountered a, an issue that, RK, I think you debugged that next morning.
[Speaker 2] [38:41] I don't no longer remember. Oh, this is the part.
[Speaker 1] [38:44] Yes. Yeah.
[Speaker 2] [38:45] I remember now.
[Speaker 5] [38:49] So I'm looking at 2 of them under a microscope. I brought him one of the new ones, and he was looking at one of the old ones and just, like, doing the the dead stupid, like, alright. I'm just gonna look at every one of these parts and see if they look the same, and he noticed that one was different.
[Speaker 4] [39:03] Well, they just would
[Speaker 2] [39:04] yeah. They're like a SOT 6. Right? They're, you know, they're s y c 5. I can't remember.
[Speaker 2] [39:10] But, anyway, they all look the same, and they've all got very similar part numbering. And our manufacturer just, you know, decided to load the wrong reel. And a mistake.
[Speaker 4] [39:22] Right. Same same size. Hot though. Yep. Totally.
[Speaker 2] [39:26] It looks
[Speaker 4] [39:26] as identical.
[Speaker 5] [39:27] Even though it's right?
[Speaker 1] [39:29] Just the wrong
[Speaker 5] [39:30] logic function.
[Speaker 2] [39:31] And Literally, your AOI won't catch it. Your AOI won't catch it because they'll train on the bad one, and then they will look at all the the the next one they build. They're like, these are fine. No. They're not.
[Speaker 4] [39:40] That's the part that that's the part that really feels like a huge process problem to me. It's like, why don't you look at the text that you read in the
[Speaker 5] [39:48] They do. They do. They do look at the text. There's no, like, database of, like, this part has this text on it and blah blah blah. It even if they had that, they would look at it based on the real because sometimes parts are marked differently depending on the manufacturing site they come from or whatever.
[Speaker 5] [40:04] And so the the typical way of doing this is they for prototypes is it's the min for max. It's the minimum amount of effort for maximum amount of benefit as they will frame it on the first one and then check all the rest of them the same. And so the question Which,
[Speaker 4] [40:22] of course, they were.
[Speaker 5] [40:24] Which they were. Yes. Good news. Which if they had to change reels halfway through, they would have found, hey. These are different, then they would have found it.
[Speaker 5] [40:32] And in production, you would train it on it and you would see, oh, these are different, you know, because you'd have a golden board that they can train on. Because it makes it a lot lot lot less labor and test to do that.
[Speaker 1] [40:43] But our assumption was not they've stuffed the wrong part. Our I mean, the assumption is I mean, there's so much We have the wrong bomb call
[Speaker 5] [40:49] out or something. Wrong bomb.
[Speaker 1] [40:51] Wrong the layout change. This is where we talk about the eye of Sauron kinda whipping around, and everyone's, like, going to their own part of the system to understand, like, wait a minute. What what's because we knew quickly that the we determined quickly that the rev c of this particular part worked and it's the rev d that didn't but there hadn't been meaningful changes in rev d. And, anyway, it was the thing that was remarkable, to me, anyway, was and just what you we get kind of undivided attention from such a broad, diverse, and deeply talented group of folks. We got that thing debugged really, really quickly as a team.
[Speaker 1] [41:25] So that was within, like, you know, 90 minutes, we knew exactly what had happened. And, Eric, you did you say you took that that Nathaniel got these things under the microscope, actually saw, like, wait a minute. This is the wrong part. Fortunately, we got also we it should be said we got lucky. It kinda that's the part that that was that was the part of the board Nathaniel was starting on.
[Speaker 1] [41:44] So he had like the second part is like, this one's wrong. And then we had to take all of we had to disassemble all of these racks. So all of the racks had to be disassembled. All of the shark fins had to come out. They all had to go back for rework.
[Speaker 3] [42:00] And by all, it was like 500 odd, something like that?
[Speaker 1] [42:04] I think we'd I wanna say, like, 1100, wasn't it? It was
[Speaker 4] [42:07] Well, no. But we we only sent back, like, 6 something, 600 or something, I think.
[Speaker 1] [42:12] I guess that's right. Right. Okay. You're right. I guess, through the the the there were a couple but it was, it But it's still
[Speaker 4] [42:17] to be fair, it's a lot.
[Speaker 5] [42:19] It's a lot. I mean,
[Speaker 1] [42:20] it's a lot. It's a lot.
[Speaker 4] [42:23] And did not did not regret putting scannable bar codes on them. Like Okay. Yeah. So, Josh,
[Speaker 5] [42:30] this is
[Speaker 1] [42:30] actually a really good point, because this is something so every Fruh that we have in the system, every field deployable unit, we have got a barcode on there. We they're all being scanned in the manufacturer. They're all going into a database. And we had kinda Josh, you had pulled that software together, like, kind of moments before this stuff had. And I I remember us debating, like, is it worth scanning these or not?
[Speaker 1] [42:54] And, yeah, do you wanna talk through that that a little bit? Because that was a that was a huge win, I think.
[Speaker 4] [42:59] Yeah. I mean, we just so we have manufacturing workstations that sit on the line that can scan, barcode. So we we have them do that, and then they get programmed into the ROMs that sit on the cards and so on, so that the cards can be self identifying. And, just as an inventory thing, So it's like we're we're gonna send back hundreds of these things, and we have no idea. If we don't scan and log each one that we send out and also each one that we receive, then there's really no way to know, like, where most of the stock is now that they've come out of the servers that they shipped here in.
[Speaker 4] [43:41] It's just a lot of parts. And, also, we had, if you recall, 20 or 30 of them that I think were not programmed correctly.
[Speaker 1] [43:48] We wanted to
[Speaker 4] [43:49] quarantine those on the way back in for inspection. It's just much easier if you have, a barcode printed on the thing and also, like, a cheap and easy barcode reading station.
[Speaker 1] [44:02] Well, and it was the this is another one of these things where it's like, you know, I I don't think anyone, you know, has doubted at the time why this is important, but we got we're getting an early visceral visceral, expression of why this is so important. So, that was actually, I mean, I personally enjoy it was a definitely a barn raising. I know, Adam, you were in here. A bunch of folks were in here actually. Right?
[Speaker 3] [44:24] You're you're yeah. I mean, can we talk about our child labor practices?
[Speaker 1] [44:27] Absolutely. The child labor was, was load bearing here.
[Speaker 3] [44:31] Yeah. You you had the you had the whole clan in. Right?
[Speaker 1] [44:33] I had the whole clan in.
[Speaker 3] [44:34] You too.
[Speaker 1] [44:35] The the the kids were in
[Speaker 4] [44:36] there and We're your children, so it's okay. Legal Exactly.
[Speaker 1] [44:40] Yes. Thank you, Josh. Josh is Adam refuses to be my lawyer, but Josh is with.
[Speaker 3] [44:46] It's like working
[Speaker 4] [44:46] on the farm.
[Speaker 1] [44:47] It's it's like working on the farm. Actually, I I I really liked it. Actually, I I thought it was great for the kids to kinda get that physical feeling of, like, hey, this is what we're actually doing. And I they really enjoyed it. It was so anyway, that was fun, but we were all doing this to get us ready for compliance.
[Speaker 1] [45:06] Everyone is scrambling hard to get and we amazingly, when the shark fin thing happened, we're like, there's, like, compliance is off. There's just no way we can do it. But through this, like, you know, we work 16 different miracles. We pull it off. We're ready for compliance.
[Speaker 1] [45:20] We are we're we're we are or getting there, and we are ready to power on the rack for the first time. And, Josh, you were in the room, I believe, when we we threw the switch.
[Speaker 4] [45:34] Yeah. I took the video of what's it how much you're about to describe?
[Speaker 1] [45:38] Right. So yeah. What, what happened? I was I had I was traveling for a conference, but I got so I I I got the the the the immediate after action on this one. I was not in the room when it happened, but, yeah.
[Speaker 4] [45:51] I mean, we so we turn we had fully populated the rack, and we turned it on at the wall, and almost half of it did not, clear the runway. There were no lights. It was not good.
[Speaker 1] [46:05] If you say not clear the runway, you really mean a a fire at the end of the runway that includes Yeah. The Gimlets. Yes.
[Speaker 4] [46:10] They collided with the seawall. It was not good.
[Speaker 1] [46:13] It was not good. It was very bad. So we had so 14 of the gimlets, and actually, it was also one of these moments where it's like, it's, totally clarifying because there's no question about what happens next. I,
[Speaker 4] [46:27] compliance is canceled.
[Speaker 1] [46:28] Compliance is canceled. Well, no. Because I mean, it's look. I I you know, I when my now 15 year old was 4, and he was walking along a concrete planter at a store and tripped and fell backwards of how he cracked his skull. But he'd actually broken his arm very badly.
[Speaker 1] [46:45] Broke his arm very cleanly, I should say. Say. His arm was in his arm had a giant s curve in it. And as a parent, it was enormously clarifying because it was not like, oh, do I call the advice nurse? Or, you know, do I call my wife, or what do I do?
[Speaker 1] [46:59] It's like, I we get in the car, and we go to the trustee room. Here we go. That's it. And that's and I feel like this this is like, okay. That we know exactly what's going on.
[Speaker 1] [47:09] We are not going to do declines. Compliance is not gonna happen on Monday. I can't because we don't know what just happened. And, we need to figure out what happened, and we've got some hunches. We'll we'll kinda describe some of those hunches briefly, but the we, the well, I I can tell you that what we do know is that we, Eric and team, Nathaniel and Aaron and RFK, were all out here that next week.
[Speaker 1] [47:33] And, Eric, how many power cycles did you guys do for the rack? I mean, a a lot of power.
[Speaker 5] [47:39] 100 and 150. It it was a lot. And we were power cycling it as abusively as possible because there are many theories between, like, okay. What if the phase connected at first before ground? Because this is it literally you know, we saw this when somebody plugged the big, like, twist lock connector, you know, 3 phase twist lock connector into the wall in the other room because yeah.
[Speaker 1] [48:05] Yeah. Dear Karen
[Speaker 7] [48:07] and I Aaron and I personally ex executed at least 200 cycles that way.
[Speaker 5] [48:12] There you go.
[Speaker 1] [48:12] Oh, yeah. And I I mentioned it
[Speaker 7] [48:14] of time in the fridge.
[Speaker 1] [48:16] So Yeah. Of course, you're right.
[Speaker 3] [48:18] Cycles executive cycles is such a a fancy way of describing what I saw, which was one of you sitting in one room, yanking the power cord out and the other one sitting in the other room, watching it and pushing a button on your phone to update a counter like, umpire calling balls and strikes.
[Speaker 5] [48:37] The The person in the room was
[Speaker 7] [48:39] It was not interesting.
[Speaker 2] [48:40] The person
[Speaker 5] [48:40] in the room was counting in their head. Like, okay. 1, 2, 3, 4, 5. Okay. Plug it in.
[Speaker 1] [48:48] Well, and it just plug
[Speaker 5] [48:49] it in abusively.
[Speaker 1] [48:50] Well, that's it. We didn't start aggressively because we did not know what had happened. And in particular, we did not know if we power this thing down and power it up, are the other begin what's gonna blow? Are we so there was, like, the first couple of days is being super ginger trying to understand everything. RFK had very quickly determined pulled the SLUDs out and very quickly determined that we had blown the FPGA that does the initial power sequencing.
[Speaker 1] [49:13] The the the not even the sequencer, but this thing called Ignition that our end that you developed. We knew we had blown that. We did not know why, and we and this is still problem that we're we're causing. We've never seen it again. It the our current hypothesis is and we've got a bunch of we can we don't need to go into too many we can go into kinda arbitrary detail on this, but we don't we suffice it to say, we spent a lot of time with this problem.
[Speaker 1] [49:40] But our current hypothesis is that these things were actually blown on the bench. That when we programmed them on the bench, we, we they got blown out on the bench. So when we actually loaded them in, they were dead before we initially powered it. And we've, as one can imagine, we made a bunch of process changes to make sure that if this does happen again, we're gonna get a lot more information, and we're meanwhile, we're having the the chips themselves. We're having them decapped, so we can understand the actual damage to the FPGAs themselves.
[Speaker 1] [50:08] We have 14 of them. So we've got I think, actually, those just showed up today. So we've got someone who's gonna be decapping those and looking at those chips. So we got a whole bunch of stuff to get that we went to go explore there. But importantly, one, we, we haven't seen it again.
[Speaker 1] [50:22] But secondly and and Eric kinda reminds me of the Murata thing where it's like, on the one hand, there wasn't anything that that was due to to the testing environment. On the other hand, we learned a lot about Merida by going into the detail by going into their their client's information. We learned a lot about how these things power on by doing it again and again and again. And and, Adam, there I would say that there was a little bit more art than you implied trying to actually by the end of the week, they're trying to break it, and they're unable to.
[Speaker 3] [50:56] See, to the untrained eye, it looked like he was yanking the power cord.
[Speaker 5] [51:00] Yeah. Yeah. I was I would get there and, like, put the thing in just barely and as cockeyed as it would let me without bending the pins and, like, slowly wiggle it in until I started hearing arcing, and then I'd let it sit there for a second, wiggling a little more. And then I'd start moving in in a little more to power up the rest of it. It was trying to be the most abusive thing I could possibly think of, and nothing killed it.
[Speaker 5] [51:23] We even intentionally disconnected ground and cycled that a few times. I didn't do anything. It's like it's it's infuriating when you can't cause a problem to happen again, but it's also good because we power cycled the heck out of it, and it was it never had a problem. So we're like, well, okay. I guess it's not power cycling.
[Speaker 1] [51:42] Yeah. And and we we and in particular, we believe that we don't have a design issue on the actual bus bar or the rack. I mean, they they it would have been in many ways, it would have been satisfying to reproduce it. It would also have been horrifying because it could have been, really it could have been a major setbacks. Anyway, that we we get through that we the fact that that compliance had been and and this is where, just some heroic work by CJ was able to book a time for a chamber in, what, 2nd week of January.
[Speaker 1] [52:13] Right? So we were going in in, what, January 7th or something like that, which was, I it was terrific that he'd managed to to pull that off. We had everyone here to kinda there's a lot of software work that still need to be done. Josh, you were doing a ton of work to actually allow us because now, it the certainly the concern that that we all had is, 1, if we were to see this kind of problem again, we wanna have information on it. But, also, just in general, if the rack when the rack misbehaved, we wanted to make sure that we were gonna be able to actually understand what's going on.
[Speaker 1] [52:45] So we had a lot of stuff we needed to go build and get integrated, and that was a real, real load start to get all that stuff put together. And, Josh, I know you built a lot of software to to software that we will then use in the manufacturing line, and, helping to flesh out parts of the product for sure.
[Speaker 7] [53:02] And and already hours before pickup?
[Speaker 1] [53:06] Hours. Full hours. Full hours. I'll have you know. Pickup was scheduled for 6 AM on Monday, and we were I mean, that thing
[Speaker 4] [53:14] we were out of
[Speaker 1] [53:15] there by 2.
[Speaker 5] [53:16] Yeah. Exactly. Pickup was scheduled on Friday.
[Speaker 1] [53:20] Pickup was technically scheduled on Friday, and
[Speaker 5] [53:22] We may have moved it a few times.
[Speaker 1] [53:23] We may have moved it a couple times.
[Speaker 4] [53:25] We learned definitely, it was like so how about when do you think should be ready? Like, an hour or 2 hours? And I'm like, 72 hours? Like, oh, oh, dear. Monday then, I guess.
[Speaker 1] [53:38] Okay. But it's a
[Speaker 5] [53:39] car truck company.
[Speaker 1] [53:41] And and this is one of these things where it's like we have the chamber starting at, like, kind of 9. And you, so like, you know, we needed this thing to get picked up promptly at sex. CJ was out there for, it was out here in Emeryville when we were getting this thing picked up. So I I I we'd kinda left off the
[Speaker 4] [53:59] Large thing, it must be said. It's quite heavy.
[Speaker 1] [54:02] It's large.
[Speaker 4] [54:03] Not really a convenient, physical set of dimensions
[Speaker 5] [54:07] for something that heavy either. Over £2,000. 20.
[Speaker 7] [54:11] It's a cozy fit in the truck.
[Speaker 5] [54:13] Yes. Yeah. That's one way to put it.
[Speaker 1] [54:17] That's one way to put it. Another way to put it is, oh, shit. That's not gonna fit. That is absolutely not gonna when they were when they were loading that thing, I'm like, there's not a chance that fits. And, amazingly, it did fit.
[Speaker 1] [54:30] They had to pull the tore back a little bit to get that thing to fit.
[Speaker 5] [54:34] Pre pre squish the foam in the bottom a little and
[Speaker 1] [54:38] Right. So we right. We go into the chamber, and, and what do we discover, in in the chamber? We'd so we get this and this is it should be said, this is not like the kind of the garage testing facility in Austin. The the barbecue may be worse in in Fremont, but, boy, the the chamber is much better.
[Speaker 1] [54:58] So this is a a a really
[Speaker 5] [55:01] The nicest chamber I have ever been in.
[Speaker 1] [55:04] Really nice chamber down there. And the thing that was super cool is they got this panel. I wish I'd taken a photo of it. They have a panel, Eric. The thing that you pointed out to me where you can dial up any country's kind of voltage and phase, for to to test anything.
[Speaker 1] [55:20] It's like, you know, how is this thing gonna do with Japan, or how is it
[Speaker 5] [55:23] gonna do? Yeah. It's a it's a giant matrix switch of power sources, which is just amazing.
[Speaker 1] [55:27] It was it's really and so this and that's what so Arian dropped the totally. Like, what I'm sorry. Which prefecture do you need, Adam, in terms of the, the Either one. 50 Hertz, 60 Hertz, whatever. Nice.
[Speaker 5] [55:42] It I don't care.
[Speaker 1] [55:43] It really is from Rockwell, and it's it's sitting there on, and that's the photo that Arne has dropped into the chat, where we've got the, this thing is on this giant turntable. And now we need to figure out, alright, what what do we see? And what are some of the things that that we see off the bat?
[Speaker 5] [56:01] Well, so we see some we see very little on the low end, which is amazing, because usually power supplies will emit in the, like, sub 250 megahertz range. And then so we saw, like, remarkably nothing there, essentially. We saw clocks. So we saw some 100 what was it? 200, 300 megahertz clock, some 900 megahertz clock, say, 687 point something something something clock.
[Speaker 5] [56:30] So we we saw a few clocks, but nothing was too bad if you were a little over the limit. And then we went up into the high frequencies and saw some more clocks and more things like TDR or whatever. But, basically, it's it like, I've I've done EMC testing on large CT medical devices for 15 years or so, and this is the most clean system I've seen go in on a first run. Usually, the the most impressive one I I saw was one where the, the chain the chamber had to change the scale on the on the, receiver because it was too high. So they had to they had to zoom out so they could measure a higher signal than they were used to seeing.
[Speaker 5] [57:20] I think
[Speaker 1] [57:21] that's that's not great.
[Speaker 5] [57:23] 20 megahertz based comb generator from a 20 megahertz clock. That was a that was an
[Speaker 2] [57:28] impressive one.
[Speaker 1] [57:29] Yep. That is impressive.
[Speaker 5] [57:31] It and, like, that thing had some particular quirks to it. It had big power and all that stuff and a big open frame motor, but it was pretty noisy. And this was remarkably not noisy in spite of the fact that it wasn't, like, Faraday sealed or whatever. But there were still things that I mean, we failed the first time, and it we found some found some things that we needed to work on and had to go digging into those.
[Speaker 1] [57:56] Well, so I I in particular, I love the fact. So we we have the 6187.5 megahertz outlier. Everyone's trying to figure out, okay, what harmonic of what clock is is that? The, one of the things that you'd said is, like, well, listen. Let's actually, make sure we get the rear doors.
[Speaker 1] [58:14] We've got a cable back plane. It's got rear doors. Let's get the rear doors closed, and let's understand the effect of that. One of the things that that is and I we should I we showed a video of you doing this, Eric, because I think it's so fascinating to watch. I mean, Adam, this is super physical.
[Speaker 1] [58:29] So one of the things that that Eric wanted is, like, I need to be able to see the output. I I need to be able to see the kind of the frequency output while I'm manipulating the system. So I wanna know, like, if I grab this cable bundle, and if I move this cable bundle, like, what do I see with the spikes? If I grab the door this way, how does it change the spikes? I mean, it really is, Adam.
[Speaker 1] [58:49] Like, you got the old, like Antenna? It's a totally antenna. I think this is, like, a total generational thing. This was, like, it's totally my turn
[Speaker 5] [58:57] to Tuning the rabbit tuning the rabbit ears.
[Speaker 2] [58:59] Tuning the rabbit.
[Speaker 1] [59:00] You are absolutely tuning the rabbit ears. Like, no. Right there. Stand there. No.
[Speaker 1] [59:03] No. No. Go back. Exactly. Right there.
[Speaker 1] [59:05] And so, okay, we just need to ship Eric with the rack standing on one leg just like that, and then we're fine. But one of the things that was interesting was bit so if we close the rear doors, the 687 megahertz freep 0.5 frequency, like, that that goes away. That spike goes away. But now there's a new spike at 72, I believe.
[Speaker 5] [59:26] All that low frequency that was so clean before it got real nasty.
[Speaker 1] [59:30] Right. And
[Speaker 5] [59:31] And it turned out that 72 ish megahertz is about a I think it's a half wave resonator with our rear door dimensions. And so our rear door turned into a an antenna, which they are won't to do.
[Speaker 1] [59:46] They are want to do. And I think that so this is, like, one of these things. And and, Nathaniel, you'd use the the kind of the the, analogy of, you know, you've got kind of, this this ball that you're kinda squishing, the water balloon that you're kinda squishing. You can squish it over here, you're gonna get some more water. It's gonna kinda come out in a different different spot.
[Speaker 1] [01:00:04] And it this was definitely a very concrete example of that, where it's like, okay, we've done this, but now we've got this other thing that we need to go deal with. And I the other kind of thing you highlighted for me is that whenever you see an Eric, obviously, you know, you you've got an and RFK Orion. You've got much better kind of intuition for this. But anytime you see any outlier at any frequency, you gotta immediately think, like, what is that wavelength? And that wavelength is how much, and what does that correspond to?
[Speaker 1] [01:00:32] It's like, okay. That is, you know, 9 centimeters. What do we have that's 9 centimeters that this thing could be resonating with? And so in this case And is it horizontal or vertically polarized? Because that's resonating with?
[Speaker 1] [01:00:39] And so in this
[Speaker 4] [01:00:39] case And
[Speaker 6] [01:00:39] is it horizontal or vertically polarized? Because it tells you whether it's a horizontal or vertical, the opposite, the, like, opening that it might come out of or or thing that is resonating at the at the antenna. Because the antenna rotates.
[Speaker 5] [01:00:55] Yeah. There's a polarization of the wave, and that tells you something about the the source that it came from.
[Speaker 1] [01:01:01] So it's a really neat debugging process. I mean, it's it it it certainly has a lot in common with debugging that I've been a part of and seen, but it's it is also like very different. I mean, it's very, and it it's just because it is so physical, but it was so much fun to watch. So us to bug that. So we discover the, the we've got some, we know that they're the doors.
[Speaker 1] [01:01:22] And then so, Eric, you got the, coming out of that, we've like, okay. We we've got too many admissions, but you've got an idea on the doors in particular. So what was the issue with the with the doors?
[Speaker 5] [01:01:35] Yeah. The doors weren't grounded along their length intentionally. Like, there's a, you know, there's a ground strap that you have to have for safety safety testing. But other than that, there's no requirements for multiple ground points. But if you have multiple connections between the door and back to the rack, it kind of detunes your antenna, and it turns it into a higher frequency, resonator.
[Speaker 5] [01:01:58] And so the hope is that you get enough connection points such that it doesn't look like an antenna to any noise that may be in a frequency that would resonate it cause it to resonate. And, hopefully, that doesn't mean that you turned it into a big Faraday cage with, like, huge copper straps all over and whatever.
[Speaker 1] [01:02:20] Right. So
[Speaker 5] [01:02:22] you don't want to turn it into a complete EMC chamber in itself if you don't have to because that's expensive.
[Speaker 1] [01:02:28] Expensive. Yeah. And then it's it can be a little bit slightly. Yeah. Exactly.
[Speaker 1] [01:02:32] Hard to do. Right? We we ought to avoid that for much reasons, but so
[Speaker 7] [01:02:36] Yeah. It makes your customers mad too. And and your repeatability drops once you ship it in the field, And so then you're, you know like, copper tape is awesome on day 1, but, like, on day, you know, 497, it might not be so awesome. So it might not.
[Speaker 1] [01:02:51] Yeah.
[Speaker 5] [01:02:51] So you gotta find gaskets or copper fingers or whatever, to to be able to make those connections. And the the idea is like, okay. Let's go in and let's try and make those connections in as many places as we need to to get things kind of behaving as they should.
[Speaker 1] [01:03:12] And so this is where and I can't remember if we've talked about this before, but you know those when you pull a drive, and you've got those little springy things on the side of the drive that are kinda evenly spaced.
[Speaker 2] [01:03:25] Yeah. Yeah. You're talking about?
[Speaker 1] [01:03:27] Yeah. So you know that that's for that that is for EMC compliance.
[Speaker 5] [01:03:32] Oh, I didn't know that.
[Speaker 1] [01:03:33] Yeah. Yep. That is And they actually I always assumed that that was like, oh, this is to, like, make it snug.
[Speaker 5] [01:03:40] Yeah. They're exceedingly important.
[Speaker 2] [01:03:42] Yeah. They're supposed to be.
[Speaker 6] [01:03:43] It's for EMC and for for ESD protection as well. Mhmm.
[Speaker 1] [01:03:47] So that
[Speaker 6] [01:03:47] so that you have a path and you might grab it and not zap it excellently.
[Speaker 1] [01:03:52] Yeah. But is that interesting? I mean Yeah.
[Speaker 4] [01:03:54] Because I
[Speaker 1] [01:03:55] you you feel like you've you've looked at those fingers, you know. I've look. I feel like I I've seen those fingers my entire career, and I just always I just draw the wrong inference about what they're for. It's like, no. No.
[Speaker 1] [01:04:05] This is actually somebody has been in a cage with these in a in a chamber with these at some point and figured out like, oh, god damn it. It's the actual we need to go get some fingers in there. Sort of break that up. So, yeah. So the, there are definitely some workarounds to all this stuff.
[Speaker 1] [01:04:22] I love coming out of the chamber. I the the next couple of days, Eric, you were up here in Emeryville, and you were actually, grinding off the paint on these. So you were out front, I guess, was that a what what were you using for that? A power tool, obviously. Was that a sander?
[Speaker 1] [01:04:40] I'm not sure what that was.
[Speaker 5] [01:04:41] No. Yeah. I got an angle grinder. Went down. Angle
[Speaker 1] [01:04:43] grinder did
[Speaker 5] [01:04:43] it all. I'm like, but we don't have one of these, so I'll go get one and get the old angle grinder out and start grinding away all the metal. And the the idea was, like, okay. I'm gonna grind away everything so then they don't have to worry about what part of the door is ground versus what isn't. And then, you know or Robert and the the other folks in the chamber can do it, more elegantly on the on the rack itself, so that they don't have to, you know, take the thing outside and grind the whole thing with an angle grinder.
[Speaker 5] [01:05:14] They can use, like, a paint scraper or whatever to do surgical surgical modifications of the rack instead of, you know, the angry end of the angle grinder.
[Speaker 1] [01:05:25] And then meanwhile, RFK, you were back here in Emeryville just trying to figure out okay. Let me try to figure out some of the things we saw in the chamber. It's obviously noisier, but, like, let me see if I what I can figure out. And at some point, you came up to me as like, what is 2 meters high? And I'm like, what is 2 meters high?
[Speaker 1] [01:05:45] I'll just pass it a little bit.
[Speaker 3] [01:05:47] Middle of the sphinx here.
[Speaker 1] [01:05:48] Oh, no. It is. And I feel like I have spent I feel that, like, I mean, we all have. Like, I've spent a lot of time in the physical proximity of this rack, and I've spent a lot of time and I'm like, what is 2 meters high? It's too high for kind of a lot of the business in the in in the the middle of the rack.
[Speaker 1] [01:06:06] It's too high for the switches. It's too high for the rectifiers. And, RFK, what what is 2 meters high, Rach?
[Speaker 2] [01:06:13] Well, if you it turns out that the hinges on the doors are exactly about about 2 meters, and the antenna doesn't obviously go lower than a meter. So you really don't you it would presumably also be at the bottom hinge. You could probably find the signal strength, like, at very high at that point. But with doors on, really, because you're breaking it up at these three points that we had created, the easiest place for it to radiate out of is the top seam of the rack, which would obviously be right at the top of the hinges. And so the peak detection, as you can see in our data well, we didn't post for data, but in our data,
[Speaker 6] [01:06:52] it it
[Speaker 2] [01:06:53] shows at 2 meters, that is the strongest point of
[Speaker 4] [01:06:56] the signal.
[Speaker 1] [01:06:56] And, you know,
[Speaker 2] [01:06:57] it's it's a very physical problem that you get to, like, go and look at the rack and realize in your head. And you have to think about these things that are that's electromagnetic waves that are or, like, you know, going everywhere. You kinda it makes it a more realizable 3 d model when you can look at it like that.
[Speaker 1] [01:07:16] Yeah. It was really neat, And, I did not I, I I did not guess the hinges. I felt a little bit vindicated when I don't think I think Steve was guessing the hinges either. I didn't think everyone was struggling to guess the hinges, but it was, of course in hindsight makes sense. So we are, and then the other thing that we, that we knew that we had not yet done, that we wanted to go experiment with is enabling what's called spread spectrum clocking.
[Speaker 1] [01:07:46] And do you, Eric, do you want to describe a little bit what SSC is?
[Speaker 5] [01:07:52] Yeah. So spread spectrum clocking is a way of everything everything in a computer operates off of a clock, which is just a repetitive, synchronous, very controlled, oscillation, and that that determines what what everything does in a computer. So for a thing like PCI Express, there's a clock that's along with it, that is a 100 megahertz And usually that's a 100 megahertz in there blasting away at a 100 megahertz plus or minus, you know, some handful of PPMs. And that's really bad for EMC because that is a very, very sharp, sharp meaning very narrow bandwidth spike of energy, and all the energy of that clock is contained within a very narrow bandwidth. So in EMC, there's a certain there's a certain opening.
[Speaker 5] [01:08:46] It's like how how much you open your eyes on the receiver. And they open the receiver up to see about a 100 and 20 kilohertz, if I remember right, of bandwidth, and that's where they measure the entire the entire spectrum. So if you can make your clocks, if you can spread the frequency of your clocks out more than a 120 kilohertz, then the EMC chamber receiver won't measure as much energy at any one point, because, basically, the the chamber receiver is blind to it. And it sounds kinda like cheating, but it's actually, it's a it's a reasonable thing to do because a lot of RF receivers have a fairly narrow bandwidth, if they're if they're meant to operate at a specific frequency. And so spreading out the energy, not only reduces the chamber measurement, but it also reduces the likelihood that you'll interfere with something else.
[Speaker 5] [01:09:41] So you effectively spreading the energy out.
[Speaker 1] [01:09:43] And are you you're effectively introducing a little bit of jitter in the clock. Is that correct?
[Speaker 5] [01:09:48] Yeah. It's absolutely controlled jitter. Right. Usually, jitter is awful in communications.
[Speaker 1] [01:09:52] Right. But Right.
[Speaker 5] [01:09:53] More modern back in the old days, computers didn't have any of this stuff. And if you had spread spectrum, it just wouldn't work. Now computers are designed to have this because it's a a, quote, cheap and easy way for manufacturers to meet emission standards without having to do heroics on enclosures. And so, basically, you just take the energy that would have been at that one frequency, and you smear it across a bunch of frequencies. And so I mean,
[Speaker 1] [01:10:19] it to me, it's, like, it's pretty clever. I mean, honestly, because you are on the one hand, you're you're introducing something or reintroducing something that we normally try to get out of a system jitter. But by doing that, you are effective. You're not dominating this precise frequency. You can actually just move yourself just enough to avoid, emitting a bunch of energy.
[Speaker 1] [01:10:40] It's not just for the past compliance. I mean, you are you are emitting less energy at that particular spot. You are less likely to induce residents in another part or what have you because you're spreading yourself up. So, yeah, it's pretty neat. So we knew that we had, that there is, as a close followers of the company may recall, there is no bias in our system.
[Speaker 1] [01:11:00] We are doing our own lowest level system firmware, all the way up with lowest level system software, host boot software. So we are, things like spread spectrum clocking, which would normally be either a bias tunable, or would happen really, really, BIOS. I I'm being told that I'm saying bias when I should be saying BIOS. Yes. The basic input output system that dates back to CPM.
[Speaker 1] [01:11:26] The it was a BIOS tunable, but, we we're responsible for implementing that ourselves. So we, implemented, SSC. We did there's a you may have heard us talk about these kind of hidden messages, that these messages that need to be sent to other cores hidden cores in the computer, and there's a message that you can send effectively on the MD Milan that says, I want you to turn on SSC. The good news is that that that that worked great on the Gimlets. The bad news is, Josh, you discovered that when we attach that to the switch, maybe not working so much.
[Speaker 1] [01:12:05] The, it should be said that Josh, like, the SharkVid issue ended up once again being on the front lines of, like, am I doing something wrong? Like, I just integrated this. I I pulled in this change and cranked it, and now I'm running it. It's like, it seems to work everywhere, but it's not working here on what we call the scrimlets. The gimlets that are immediately attached to to the switch, to the sidecar.
[Speaker 1] [01:12:25] And, Josh, I think that, I think, everyone's like, oh, well, this is Josh. This must be. Must have done something. You must have pulled something in incorrectly, but it's like, nope. We have definitely some, a challenge there.
[Speaker 4] [01:12:37] I feel like this is a familiar feeling.
[Speaker 1] [01:12:40] Yes. Exactly. So we what we learned, and we're still, still debugging aspects of that issue, but what we did that definitely learned is that that, SSC can be enabled on all the compute SLEDs, and then we need to understand why and and how we need to not enable SSC or work on that on on these things that are attached to the switch. But, actually, this is one of these things where well, actually, if you can enable it on 30 of the 32, that actually is a that that's a that's a big difference. So that can actually, reduce our emissions quite a bit.
[Speaker 1] [01:13:16] And so we wanted to go do that. We wanted to go explore these things with the door. I think what what were some of the other things we, some of the other I think those those are the certainly the 2 big ones that we wanted to go, revalidate when we got back into the chamber. Well, yeah.
[Speaker 2] [01:13:32] There was a bunch of stuff that we did when we we looked at. I mean, there's, like, about a 7 point list of things to do. But, you know, when you go into the chamber, you kinda start off with the things that you know you should start with, like, very big changes and then kind of work as it comes from there, because you'll just find new stuff. So we ended up doing a lot of stuff. It was, like, tangentially related to the list, but not explicitly, like, we know exactly what we need to do when we go in there.
[Speaker 2] [01:14:02] That's just I've never, like, been in that situation in a chamber where it's like, oh, yeah. I do all these things, and it's perfectly fixed.
[Speaker 4] [01:14:09] It's like, no. We went
[Speaker 2] [01:14:10] in there for, like, another, you know, 72 hours.
[Speaker 1] [01:14:12] Right. And And it
[Speaker 2] [01:14:14] should be like
[Speaker 1] [01:14:15] and it should also
[Speaker 5] [01:14:16] be We
[Speaker 6] [01:14:16] want to understand how each of these things individually behaves and then how they combine. And, and some of them you have a little bit more confidence in. Some of them you have less confidence in. Some of them we needed to do some physical work. Like we needed to scrape off more paints and, like, put gasket in and you
[Speaker 5] [01:14:32] know. So
[Speaker 2] [01:14:33] Yeah. I mean The process. And also, you wanna do things. You you wanna go in there and make changes in ways that your mechanical team will be able to reproduce and also in a way that will not piss them off when you tell them what you ask want them to do. Because I reckon
[Speaker 1] [01:14:52] it didn't
[Speaker 2] [01:14:53] be a dick, and, like, make the change really difficult, and they will hate you forever.
[Speaker 1] [01:15:02] Right. So we and it's it should also be said that at the same time, we're also doing our safety compliance. And a safety on the one hand, we're little bit less concerned about, I would say, because we're not, that there's no reason to believe that we would have major redesign for safety. On the other hand, there's safety is obviously important, and we need to make sure that we we don't have, I mean, that they're gonna be testing exposed services and testing for ESD, and there's a bunch of things they're gonna be doing. They're going to
[Speaker 4] [01:15:32] We we hit the thing with a sack of doorknobs was the part that really felt like
[Speaker 5] [01:15:36] One doorknob is a calibrated doorknob.
[Speaker 1] [01:15:38] It's a calibrated doorknob.
[Speaker 4] [01:15:40] ISO standard doorknob. Is that is that really safety, or is that masochism? Like, what what's going on? The tip test was fun too.
[Speaker 1] [01:15:48] Right. They wanna do a tip test, and they're gonna, like, we're gonna do a tip test. And, yeah, Nathaniel, what were the details on that? They had to they they wanna, like, tip it over, and they wanna They they they said they said that we're gonna put
[Speaker 6] [01:16:00] Well, yeah. They were we were gonna tip it to 10 degrees and we were they said, like, oh, just put 2 people behind it to catch it if it tips over. In the process of getting
[Speaker 1] [01:16:16] this thing to market.
[Speaker 4] [01:16:18] Well, and it weighs like £23100. Right? Yes. Yes.
[Speaker 1] [01:16:23] Yeah. It it is scary. And certainly, when I think if that thing got tipped, it would get very scary. Ariane, I loved your line when I went down there to the the safety testing house, down, in Menlo Park. You're I mean, you looked at me just just looked me right in the eyes.
[Speaker 1] [01:16:38] You're like, you know, for a place dedicated to safety, you can die here. And I was kinda laughing and you're like, no, no. I'm serious. Like, watch yourself. I'm like, okay.
[Speaker 1] [01:16:47] I I can
[Speaker 3] [01:16:47] He means you specifically, Brian.
[Speaker 1] [01:16:50] What's I, I mean, Brian. Cards on them? I there were and in particular, like, the whip that they had us using was definitely, like, it
[Speaker 5] [01:16:58] I,
[Speaker 1] [01:16:59] I yeah, it was,
[Speaker 5] [01:17:01] The state safety testing is not the place where you want people who are who are, not comfortable with working with dangerous things. Which is like
[Speaker 1] [01:17:10] I mean, I guess it makes sense. I mean, it's
[Speaker 5] [01:17:12] like They're trying to induce failures at some level, and that that has inherent risk to it. Right?
[Speaker 1] [01:17:17] Yeah. But it was so I and I think that the and, Josh, I have to tell you that emotionally, it really did feel like that they were gonna drop a sack of doorknobs on it. It's just like just because we, you know, spent time here
[Speaker 4] [01:17:29] in the ministry of safety office, like Right. Exactly. Because the
[Speaker 1] [01:17:34] ministry of safety is gonna launch doorknobs against this thing. But it is, as Eric says, very it's a very precise test, and we don't anticipate it or didn't anticipate it. It it it may cause a facial laceration, but don't anticipate it. Actually inhibiting the the the operation of the rack. The and then, Arnie, do you guys were all also down there doing a bunch of, a bunch of thermal stuff?
[Speaker 1] [01:18:00] Where would you
[Speaker 6] [01:18:01] Yeah. So we had to we had to prove that if if if things get if fans get blocked, that we don't overheat in such a way that, components get so hot that you might, like burn someone in, you know, that that, bodily harm might occur. So there we have to set up some tests for thermal, testing. And I'm trying to find the pictures of that because there was some, this It was pretty funny. Well, because hilarious.
[Speaker 6] [01:18:27] Yeah.
[Speaker 1] [01:18:28] In particular, the you are trying to get this thing to overheat, which is now, like, look, you know, like, we've built a complicated system. We've got a series of trade offs. We've got a lot of thermal margin in this thing. When we like, one of the very first decisions we made was around height of the, so each of these sleds is designed to be tall is tall enough, a 100 millimeters tall to contain within it an 80 millimeter fan. It has 6 80 millimeter fans in it.
[Speaker 1] [01:18:55] Those fans move a ton of air. They at very low power, when they're only at 2,000 RPM, they are moving enough air to effectively keep the system cool, unless it's doing an obscene amount of work, in which case they may go up to 3 ks RPM. The fans themselves can go up to 12 ks RPM, but they will draw a lot more power. And when Arion was down there, like, try I mean, Arion, you you all are trying to, like, find every intake of this thing, because those fans are gonna fight you, and they're gonna find ways to get air into that thing to cool the to cool the CPU.
[Speaker 6] [01:19:30] Yeah. So there's there's 2 scenarios in particular we ran. One with the input blocked. So basically, the fan is starved from fresh air. I posted photos in the in the chat.
[Speaker 6] [01:19:43] So that's that's the first one you see with a bunch of cardboard on the front of this thing. And then, the second test was where we would block the backside of the of the the rack, and we really tried to close it up, basically, to trap hot air afterwards in the rack. And that, in particular, was kinda funny because we we put these cardboard pieces on the inside of the doors, turning the doors effectively into really, like, wing surfaces effectively. And we started off with a little bit of tape. Like, the doors are sort of closed with a bit of bit of extra tape to sort of keep them closed.
[Speaker 6] [01:20:20] And as the system starts ramping up because of the heats heat is getting trapped and the fans continue going and going and going, the doors basically get blown open. So we had to put these really, like, heavy steel plates that are used to take things in and out of the EMC chamber. So we put those against the the doors. And and then in order to keep the rest in order to keep those from further tipping and to keep them from sliding, we put a bunch of, like, heavy weights in front of it, and that that that was just enough to sort of keep the doors from closing. And then we had to find all the holes by which air was escaping, like the top and the sides.
[Speaker 6] [01:20:54] And, and the thing was definitely fighting us all the way. And in in the end, all the hot air would come out on the bottom because that that was pretty much the only, like, real opening that was left, which was allowed for us per this test standards because our rack is standing on a is expected to stand on a, you know, concrete floor or whatever Right. Not on on on soft bedding. And, therefore, we don't have to close-up the the bottom. And but if you were to hold your hand on the bottom of the rack as it was running, you know, 15 or 16 kilowatts of hot air coming out the bottom, that that was getting pretty warm.
[Speaker 6] [01:21:27] Let's put it that way.
[Speaker 1] [01:21:28] Yeah. And the the rack could be deceptive because these are these big fans. They they are able to move air without so the rack is very quiet. If you're accustomed to a data center, one of the first things you will notice physically when you're around the rack is it's much quieter, and you you think, is that thing on? And then you go to the back, and you just feel this heat just dropping off the back.
[Speaker 1] [01:21:48] You're like, okay. No. It's definitely on. There's a lot of heat back here. And, yeah, you put all that heat in one spot, Ariane.
[Speaker 1] [01:21:54] And as you said, I I kinda like the idea of the rack on soft bedding, though.
[Speaker 2] [01:21:56] I kinda feel like we need that.
[Speaker 1] [01:21:57] I guess that's gonna be disqualified by our our safety compliance. It's not gonna allow for a
[Speaker 4] [01:22:01] 2 inch shag carpet? 22 inch
[Speaker 1] [01:22:06] exactly. Yeah.
[Speaker 6] [01:22:08] Good luck rolling that thing over that shack carpet without ripping up the carpet.
[Speaker 2] [01:22:12] Do you remember when we were
[Speaker 4] [01:22:14] rolling it when we were rolling it into the rack, and the whole rack came to a shuttering stop on a, like, millimeter and a half lip on the crate?
[Speaker 1] [01:22:24] It's it's a lot of computers, it turns out. And the the the other thing it was funny is as Aron was kinda reporting back from this down to the the the safety facility. And, you know, we're kind of the the rest of oxide is kind of taking bets about, you know, this is kind of like thermal margin versus power margin. And we like, those fans, if they're all cranked, we would draw a lot more power. And indeed, we ended up, like, for one of those tests, we ended up actually, the rectifier.
[Speaker 1] [01:22:50] And this is, like, like, actually, sorry. You've reached your limit here, and and we are we've designed this thing to go maximum to, what, 19 k w, which is basically what it hit, with the the the fans absolutely cranking the cubicle. Fans doing their job. So that was, that that was fun. So safety went, I think, broadly, that was, largely vindicating, went well.
[Speaker 1] [01:23:13] The but we now we need to get back in the chamber I'm getting slightly out of order because we did the kinda finish up that safety last week, but then the, RKU and Ariane had a couple of very late late nights in there where you're figuring out, exactly how to eliminate some of these spikes.
[Speaker 6] [01:23:31] Minimal set of changes we can make in order to pass compliance and not upset our mechanical engineering team as,
[Speaker 2] [01:23:38] Well, we went minimal. That's true.
[Speaker 1] [01:23:42] What were some of the changes that we that we had to make, and and what was the the final result?
[Speaker 2] [01:23:46] So, yeah. Like, going going back a little bit. Like, we're worried about things becoming antenna. Right? And the doors, obviously, antenna, big doors.
[Speaker 2] [01:23:59] And as you cut them up, they become different types of antenna. So you can ground them in different ways, and, they radiate in different ways, but less, you know, once they're grounded. So that was one change. Like, definitely make sure these doors have good ground pump pack. Okay.
[Speaker 2] [01:24:16] But we don't always wanna, like, make people have doors. Right? That's not cool. Customers don't want that, especially the front door. And so we're like, alright.
[Speaker 2] [01:24:24] Well, you know, we can't put the front door on all the time. So let's try to just make sure we don't have to pass and, like, require our customers to do that. So we put the backdoors on. Backdoors are fine. And then you do, 30 megahertz up to 1 gigahertz.
[Speaker 2] [01:24:42] And, you know, once we had done a series of other changes like SSC, there's, like, potential for some gasketing that we can do in order to, like, further bring down this, like, broadband noise that we have. But we can pass without it. Great. Cool. Moving into higher frequency.
[Speaker 2] [01:24:57] So that's 1 gig up to 8 in our case, and they do it's 5 times the maximum clock frequency. So that leads puts us at 8 gigahertz, but we can see all the way up to 18 in our test. Which so it's like, yeah, I don't really care about the rest of this, even though like, but we have the data for it. So, you know, we can make improvements later as we like or have time for, which is probably never.
[Speaker 1] [01:25:22] And so so where does where does the kinda the standard stop? At what frequency do the standard stop?
[Speaker 2] [01:25:28] Well, it's 5 times the maximum frequency.
[Speaker 1] [01:25:30] Oh, okay. I got you. So it depends on the product. Okay.
[Speaker 2] [01:25:33] Got you. On the product entirely. So,
[Speaker 1] [01:25:36] I think Okay. So they they once you get beyond the 5th harmonic, they're like, we actually once you get beyond the 5th harmonic, like, we just assume that the amount of energy that you're that you have up there is just not gonna be material.
[Speaker 2] [01:25:49] Yeah. For that for that operating frequency that you're running at. And I mean, it changes in it's like different for different types of products too. So, I mean, obviously, there are radios that operate, like, way higher than that. And so and then it'll also be dependent upon, like, how you're transmitting time on air, like, stuff like that.
[Speaker 2] [01:26:06] But that this is like a whole other class of, like, problems that we do not have to worry about, because we do not have intentional radiators, and we're not a radio product. So, like, hey, good. This would be way worse if it was. Yeah. The, so we get in there.
[Speaker 2] [01:26:23] We're working at a 1 gig to 8 gig, and what we're gonna what we're gonna see is that the same things that we kinda saw at the low frequency range, the other components that operate with those that are errant are gonna be errant in the high frequency range. And lo and behold, all of the drives in the front of the rack scream like none other, because, of course, they do. It's PCIe, and spread spectrum does a little bit, but not enough. So what happens is you we have to try to pass. We don't have the front door on the rack.
[Speaker 2] [01:27:00] If you put the front door on the rack, it would keep all that stuff in because we grounded that, but we can't do that. So, we're just under the limit for 9 or for, like, at, 8 gigahertz. So we're like, oh, okay. Maybe we'll pass. And, you know, if these things are not exactly, they if the if the clock's shipped around, then they'll do the they'll look for peak detection after they scan once, and they'll try to find, like, the maximum of the frequency that it found first.
[Speaker 2] [01:27:32] And if the clocks move around, obviously, like, that maximum is gonna come down. But if it's something constant, like, you know, PCIe clocks, it's not gonna go anywhere. Actually, it's gonna get worse, because it's gonna go it it finds some local thing that it found, and then it'll then search around in that area for the most powerful sig instance of that signal.
[Speaker 6] [01:27:54] Yeah. It can maximize the emission of that signal.
[Speaker 2] [01:27:58] Yeah. Because it's just it's just looking around in, like, all the dimensions that it can to try to find that spot. And so, you know, we had, like, maybe 1 DB of margin, and it was, like, oh, man, I don't know if this is gonna work. We come back, we go, and we're gonna we we set out of the chamber and let it run because it takes about 5 minutes to find this. Then we come back a little bit later, and, oh, man, we we it found it.
[Speaker 2] [01:28:21] It sure did, because we are so close. I mean, just unbelievably close to the margin, but we passed, so it doesn't matter.
[Speaker 1] [01:28:30] You know, I had some courses like that in college.
[Speaker 2] [01:28:32] Right? It's like we are we are I mean, point 08 dB away from not passing, but we do. And we know the things that will mitigate this in its entirety, which is also the the better finding coming out of that. And they don't care. It's like you gotta pass, like, when you know what your solutions are, and you write that up in your report, and then you submit that to the FCC, and that's generally okay.
[Speaker 2] [01:28:58] And, you know, like, that is not uncommon for, everybody that has to go through and do
[Speaker 1] [01:29:06] this. Yeah. When
[Speaker 2] [01:29:07] products in field that they'll they'll already have sold it. And then they'll have to go back and do EMC testing, and they'll fail something.
[Speaker 1] [01:29:14] Oh, man.
[Speaker 2] [01:29:15] Oh, man. Then you gotta recall all that stuff and go fix a bunch of things. So, like, you know, even though we are getting through just barely, like, this is way better than, like and especially for the size of the system. Like, way better than
[Speaker 1] [01:29:30] the the system. Yeah. What and
[Speaker 4] [01:29:31] it's one
[Speaker 1] [01:29:31] of the things I think that that that we really appreciated, especially in all of this, is that the that when you have these when you're selling by the one you or the 2 you when you're selling kind of the traditional server, it's it's it's an easier problem, frankly. I mean, there's just it there's just a lot less that's there.
[Speaker 6] [01:29:47] Yeah. Just just running one of our machines in the chamber, we're passing actually with a pretty decent margin. But if
[Speaker 2] [01:29:52] you have Oh, absolutely.
[Speaker 6] [01:29:53] 32 of them, then then things become a lot more difficult.
[Speaker 2] [01:29:57] It's a combined effect for sure. And I mean, like, no one has to like, I mean, if you're building, like, a CT or something, sure, you're going in but, like, that's that's all one contained system. But we're talking about the rack is, like, one built up of 32 individual, but should be tested individually, things. And, like, no one no one goes and does that. Not at It's a yeah.
[Speaker 2] [01:30:18] It's a
[Speaker 6] [01:30:19] should be, but, normally, they are individually tested, and they pick their exact sort of test configurations they wanna test them in.
[Speaker 2] [01:30:27] Exactly. They'll go pick, like, they know that, like, some of these different files are, like, the worst style for this system that they're gonna test, and
[Speaker 1] [01:30:34] they'll put
[Speaker 2] [01:30:34] that together. And then they'll just say everything after that is okay, because they're like, well, this is probably the worst. And then they don't Right. They just, like, sign a DOC, and they're like, well, we conform with everybody. But they didn't actually test it.
[Speaker 2] [01:30:44] No. Like, we know everything that goes into this rack in the way that it's supposed to, and we're doing it all at once together, and it works, and we pass.
[Speaker 1] [01:30:52] Which is awesome.
[Speaker 2] [01:30:53] Yeah. Pretty great.
[Speaker 1] [01:30:54] And no one died in the tipping test, and we did Well, so
[Speaker 4] [01:30:58] my my thing is, like, when we ship this rack down there, I feel like it wheels out of the box and, like, it you know, like, 32 machines booted up to UNIX, and the switches configured themselves. And it was like it was and then you, like, hit it with these doorknobs, and then for some reason, it's, like, it's caught on fire. It's full of shag carpet. Like, how is it gonna be when it comes back?
[Speaker 5] [01:31:20] It well, it it just the the thing that's amazing is it just works. Like, there's no, oh, crap. This one didn't work this time. Reboot it. So I'm like, no.
[Speaker 5] [01:31:28] No. It just came up and it worked.
[Speaker 6] [01:31:30] Well, Josh, to answer your question, how is it gonna come back? Well, in having gone
[Speaker 4] [01:31:35] over angled ground off of it?
[Speaker 6] [01:31:37] No. There's definitely a lot of paint missing. But then, in in going in and out of the chamber many times, you had to go over ramps and things. So, yeah, the wheels are a little bit squeaky now. So, I'm sorry.
[Speaker 6] [01:31:48] We we we may have broken it a little bit.
[Speaker 2] [01:31:51] Yeah. The wheels
[Speaker 1] [01:31:52] Josh, Josh, I kinda share your, like and I think this is how you tell, like, we really truly do love computers. Because, like, why would you hurt the computer? Don't hurt the computer.
[Speaker 4] [01:32:04] And, like, the first one that we made too.
[Speaker 1] [01:32:06] Right? It's exact it's exact but it's, it adds character.
[Speaker 6] [01:32:11] That's what it does. So When it when you have it on display in some museum, it that's it will be it will add character.
[Speaker 4] [01:32:17] Rec 1, we hardly knew you.
[Speaker 1] [01:32:19] We did well, and and the but I also feel and, Nathaniel, I believe your line was, I don't know that I've ever seen software come together later for something and work as well in the chamber.
[Speaker 4] [01:32:31] Every every assignment that I did at university was finished at 2 o'clock, the morning before it was due. So that's just how we roll.
[Speaker 7] [01:32:40] I mean, we've like, I've you know, Eric and I spent a lot of time in EMC Chambers over the years, and it's not uncommon for, you to have the software issues in there or, like, you know, in in certain systems, you wanna run them in a mode that, like, stresses them. And, like, those are often the, like, hard modes to be reliable. And so, you know, you find, like, oh, you know, the yeah. We ran this test 8 months ago, but, like, this no one does this except for an EMC, and so all the bits rotted and, you know, it doesn't work again. And so it was really awesome to see the system, like, you know, show up in this in there, and it just worked.
[Speaker 7] [01:33:18] And it was it was really nice. Like, the the team could then focus on the thing they needed to do instead of going and chasing software problems.
[Speaker 5] [01:33:24] So Yeah.
[Speaker 7] [01:33:24] We we just did the whole team for that.
[Speaker 6] [01:33:26] We had to tweak it a little bit for, like, you know, when we started running things. Like, one of the things that we hadn't quite anticipated was we had built a stress test for various components, and then we tried to put a load on the on the SSDs, and we just start the stress test. And, basically, the entire machine just went out for lunch. Like, the thing was just not responsive anymore. It was running.
[Speaker 6] [01:33:47] Just it wasn't wasn't making any progress because It
[Speaker 4] [01:33:49] was very busy doing what you asked us to do. We spent
[Speaker 6] [01:33:52] we spent we spun up so many threads per SSD, and that that the system was just, like, done.
[Speaker 1] [01:33:56] So we had to
[Speaker 7] [01:33:57] That's the improved version that wasn't erasing
[Speaker 1] [01:34:00] all of its own. I was gonna say yeah. That was
[Speaker 6] [01:34:02] that was after we erased a bunch of stuff.
[Speaker 1] [01:34:05] We did have at, it wasn't 2 in the morning. Josh, when did that happen?
[Speaker 4] [01:34:08] That's that's why it took until 2 in the morning.
[Speaker 1] [01:34:11] It's why it took until
[Speaker 4] [01:34:12] 2 in the morning. Like, quarter to midnight or, like, half midnight or something. Like, the because we because we wanted to turn the lights off and do the all the lights flashing on the front thing, which
[Speaker 1] [01:34:23] Which is pretty cool.
[Speaker 4] [01:34:25] That did happen. Cool. And also it ate all the partition tables at the same time, which was very sad. Like, don't turn this off.
[Speaker 1] [01:34:33] Right.
[Speaker 5] [01:34:34] We'll turn
[Speaker 4] [01:34:35] it so we can fix it.
[Speaker 1] [01:34:37] And then Josh back in there with the Kluge dot twos that we talked about in our small boards. The, it and
[Speaker 4] [01:34:42] The jumper cables?
[Speaker 1] [01:34:43] They'd be going in with the exact include armed with, like, kludge dot twos in each hand, like, you were defibrillating the rack. The there was, like, a combination of, like, jumper cables and and a defibrillator. It was really a great look, as we're going around getting it. Unfortunately, though, we got got the rack back on its feet, and, yeah, we're not gonna plow the boot drives anymore. But it was a, honestly, great effort all around, really educational.
[Speaker 1] [01:35:07] You know, I think over and over again through this journey, we've learned why other folks, you know, because I I think the question that we get is, like, why are not other people making a rack scale computer? And the answer is, like, it's hard, but this is some real concrete detail of why it's hard, is because it is actually hard to get this whole thing together and treat it as a coherent unit. And compliance is, you know, something we had heard a lot about, about it being a challenge, and it was a challenge, but it was a challenge we were up to. And, it was a lot of fun. And I think, RK, you know, you I I love the way you said it about, like, we know the next time we go into a chamber, there are a whole bunch of mechanical changes that we're gonna be making to make sure that, like, our margin's not gonna be that tight the next time.
[Speaker 1] [01:35:51] We're gonna get gonna get much better margin. And, Ari, and I know you were you were kinda looking at some of the other engineering teams that were down there who've been teams at much more established companies and, and just admiring kind of how they go into compliance. And we've got a lot that we learned. I think we're gonna be, we're we're only gonna improve over time, but, boy, this was, this is a lot of fun and, a lot of work from a lot of folks, a lot of late nights, a lot of 3rd shifts, a lot of early mornings, and a rack that damn near didn't almost didn't fit in its truck. But, it was, great work all around and really very important because without this compliance, we cannot sell a product.
[Speaker 1] [01:36:36] So for those folks who've been asking, when are you gonna ship? Like, well, you've you've you gotta actually have the the the compliance in order to be able to ship. Out safety compliance. You gotta actually have the FCC compliance. So, we are, the runway's in sight.
[Speaker 1] [01:36:53] Still plenty of challenge ahead as always, But, the, we are looking forward to getting this thing. Exactly. Whether the folks have pointed out in the chat, we are gonna ship it as soon as we leak, we can. And now we've got the legal green light, regulatory green light, and, looking forward to getting these things out there.
[Speaker 6] [01:37:12] Technically, we don't have the green light yet. We just have the reports in hand that will get us the green light. But we still have to defend it. But Fair.
[Speaker 4] [01:37:20] What are you what are you, from the government? Jesus. What a what a buzzkill.
[Speaker 2] [01:37:23] Oh, god.
[Speaker 4] [01:37:24] If you're if you're a cop, you have to tell us.
[Speaker 1] [01:37:29] The it's a in FCC deep mole. Yes. We have got a defendant, and we we will defend it. That the the the point 0 8 d b.
[Speaker 6] [01:37:36] I Oh, yeah. We absolutely can. We just
[Speaker 4] [01:37:39] This is this is a discoverable medium.
[Speaker 2] [01:37:41] That's right. I was talking to Tom yesterday, and he was, like, you know, arguing that point away, it's like getting a d in a class and then having to go to your professor and be like, no. It is worth that one point. I get those credit hours.
[Speaker 1] [01:37:53] I I the the it's, in in the the letters s and s and c, which is satisfactory, no credit for a course you're not taking for a grade. It's the s that's important. But again, terrific work. I know that a lot of startups, really struggle with compliance for understandable reasons because it's, it's expensive and it's laborious and it's it's a lot of time and energy, but, great work all around and, looking forward to getting it out there. Adam, I'm sure this has been, I mean, very eyeopening for me.
[Speaker 1] [01:38:26] I feel I've, I am never gonna look at a consumer product the same way again.
[Speaker 3] [01:38:31] Yeah. See that little FCC sticker on it now means a whole lot more.
[Speaker 6] [01:38:34] Oh, does the fact that your TV turns on every time you ask it to? Oh, like most of time it turns on.
[Speaker 5] [01:38:39] Most of the time. Yeah.
[Speaker 4] [01:38:41] Most of
[Speaker 1] [01:38:41] the time.
[Speaker 6] [01:38:41] It's it's Yeah.
[Speaker 1] [01:38:42] When it does, it's just a small mirror. Like, how Yeah. Exactly.
[Speaker 6] [01:38:45] How well this stuff works on average.
[Speaker 1] [01:38:48] It's it's amazing. Alright. Well, hey. Average. Thanks, everyone.
[Speaker 1] [01:38:53] Thank you, Eric and and Arian, Nathaniel, RFK. Thank you all of this. And since CJ oh, I should actually would just in closing because CJ had the drop. He was listening earlier. He did have some some points of clarification that I feel are are important, that I had had pulled up a moment ago.
[Speaker 1] [01:39:13] Let me go pull those up. So on, 1st and foremost, on the, the actual barbecue. I it Ariane, he believes that the barbecue you're referring to is, nickelthwait. I'm probably mispronouncing that, but, in general, just as good, but Franklin's brisket really does live up to the hype. Just be sure to order a couple weeks ahead to skip the line, CJ says.
[Speaker 1] [01:39:39] Definitely recommend that. On the number of shark fins, it was, 1,136 sharp shark fins, total rework in 5 days. So, and as he points out, a huge shout out to Steve for finding a courier for these things who was totally sketchy. That courier was that was dodgy, but, Steve, you did it. They got there back.
[Speaker 1] [01:40:01] And then also, she just says shout out to Matt Keeter as well, for advising him to put more money on the table with EMC Chambers in the Bay Area at times, though that really has paid our butts on on the schedule. So important clarification. CJ CJ was, and join us up here on stage, but I think everyone here would agree that, CJ was absolutely essential on both pre compliance and compliance. So it really does take a village, and we got Hey, Dave. We appreciate you.
[Speaker 2] [01:40:32] Yes. CJ legend. Getting those times in the chamber. Woah. Shit.
[Speaker 2] [01:40:36] That was incredible.
[Speaker 1] [01:40:37] And the Franklins is amazing. Alright. Thanks, everyone. We'll talk to you next time.
[Speaker 5] [01:40:44] Thanks, everyone.
[Speaker 1] [01:40:45] Take care. Cheers.