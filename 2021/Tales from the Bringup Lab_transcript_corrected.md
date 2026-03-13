[Speaker 1] [00:00] Yeah. Well, yeah. This is the fun stuff where, you know, when the CAD doesn't work. Right? Because, you know, we did something wrong, and then you get to figure out what, you know, what happened and how you fix it.
[Speaker 1] [00:11] So
[Speaker 2] [00:12] Oh, yeah. Absolutely. I've I've heard, some stories of smoke plumes, but, I don't know the details. Somehow, I'm hoping to hear some smoke plume details.
[Speaker 1] [00:20] Yeah. We've had relatively little smoke, so that's been exciting.
[Speaker 3] [00:24] That's good. Very few
[Speaker 4] [00:25] smoke. Literally I literally thought the white smoke was just a figure of speech, like, not a real thing.
[Speaker 3] [00:32] And when we
[Speaker 4] [00:33] were in Minnesota, they're the hardware team's just like, oh, no. No, Steve. Like, its actual smoke will come up if something goes wrong.
[Speaker 2] [00:39] You thought it was like choosing the pope?
[Speaker 4] [00:41] Yeah. I thought it was sort of like, ah, you know, the old magic smoke.
[Speaker 3] [00:44] So, Steve, did you want to kick us off maybe? Because you, you may have, obviously, this is, this is a first bring up for you and a lot of education. What was your perception going in? And you want to lead us off here?
[Speaker 4] [01:02] Yeah. Sure. Maybe just very briefly because I think, I, like Adam, and, like everyone, is very, very excited to hear kind of from Nathaniel's perspective, that coming into this and the stages and where things have ended up so far. But, yeah. Definitely my first bring up.
[Speaker 4] [01:21] My second real foray into being close this close to the hardware. The first being, the hardware hacking course that we took, I don't know, December 2019. And the mean, I think what what I came away so we went out to our manufacturing facility in Minnesota when we got the first boards off the line, and, Nathaniel and Eric and Aaron and Ari and RFK and a bunch of folks were there. And I was there basically just to make sure everyone had coffee and, get, you know, water refilled, smuggle water into the lab and, was expecting that I mean, sadly, I expected that bring up of a board, if things went well, would all take place within, like, a day?
[Speaker 3] [02:18] And I mean, I didn't get that from me, did you? Did I say that? I mean
[Speaker 5] [02:24] I may have contributed to this a little bit of, like, telling stories about bring ups that actually happened in a day, but also with the caveat of that was with an experienced team on, like, the 4th generation of the product.
[Speaker 3] [02:37] Well and, also, Rick, we did have a protoboard that we are the protoboard for the service processor, running Hubris, which we brought up about a year ago, which went which was a day. I mean, that was the way we just brought that thing up. And at the time, Rick was telling anyone who would listen, like, do not infer anything from this experience. Like, this is not supposed to go this smoothly. And when we have bigger boards, it will get rockier.
[Speaker 3] [03:03] But maybe you missed the memo on that one, Steve.
[Speaker 4] [03:05] Definitely. I mean, I honestly, when I was thinking day, I was I in my head was, like, even maybe a couple of hours. And so, I mean, there was one moment that will be burned into my memory forever, which was, you know, the whole team is kinda standing over and sorry. I'll after this, like, I think we want to go back to the beginning and walk through this, but, we were at the point of applying 54 volt load and, like, testing whether the, you know, obviously, the first stage of power would come on. And in my mind, I think with all the buildup and all time going back from the design and the actually having a real physical artifact in our hands, and then applying power, I kind of felt like it was this big milestone moment.
[Speaker 4] [03:48] And when that was applied, and no magic smoke showed up, I remember, like, raising my hands, and, like, maybe yelling. Like, very, very excited. And everyone turned their heads, like, what are you what are you doing? Like, this is, like, the first of 24th. Right.
[Speaker 4] [04:06] It's going to take, like, weeks.
[Speaker 3] [04:07] This is, like, the first pitch of the game. And and and you, and you have just exploded in the jubilation that a strike has been thrown. Basically.
[Speaker 1] [04:17] Now, Steven, do you remember what day that was? Because it's all kind of blur to me.
[Speaker 4] [04:22] That was day 3.
[Speaker 3] [04:25] Okay.
[Speaker 4] [04:26] But we got there at night on Monday, so I think it was Wednesday.
[Speaker 1] [04:29] Okay. Yeah. So yeah. So we had spent, like, a probably parts of 2 days, going through and just doing power checkout and making sure that, you know, the resistors we intended to put on were there and the resistors we didn't intend to put on were not there. You know, those kinds of things.
[Speaker 1] [04:45] Right?
[Speaker 3] [04:46] Well, in the video, this is actually an important point because you also in doing that, in checking the all the resistors and checking all the caps, you got the issues that you found in that.
[Speaker 1] [04:57] Sure. Yeah. I mean, you know, there were a couple of parts that, you know, we intended to know stuff, which means, you know, not don't install. And, we messed up the property or messed up the bomb when we shipped it to our vendor. And so those parts got installed.
[Speaker 1] [05:12] And, you know, you also do standard things like power plane checkouts. You want to make sure your power and ground planes aren't short together. And so we found a couple of, surprisingly low resistance values between some of the planes. And so there was a little bit of a freak-out about that. And we, you know, sent one of the boards back for x-ray to make sure that, you know, the part that, you know, interacted with those 2 planes wasn't shorted and it wasn't.
[Speaker 1] [05:37] And we had some help from, Cliff and Rick, you know, back in other parts of the country, beeping out some of their, their test hardware, which had the same kinds of chips on there to prove that, yeah, some of these chips really just have low powered off resistance. And I mean, powered off stuff is, like, there's no data sheet for powered off parts. So you kinda don't know what you're getting.
[Speaker 2] [05:58] And the thing is, is it worth can you step back a minute and maybe talk about this board and what's on it and what you know, the like, what we're talking about here?
[Speaker 1] [06:06] Yeah. So this is our server board. So we've got, an AMD. It's we're targeting an s p three socket family part. So we're going to go with the Milan silicon.
[Speaker 1] [06:16] It's got a bunch of, it's got 10, PCIe, by 4 some connectors, which will go to the front for our u dot 2 hard drives. It's got, you know, a bunch of dims on it. So I think, we can set 16 dims on there. And then we have, you know, our control plane stuff. So, like, our totally not a BMC, as Steve likes to say.
[Speaker 1] [06:40] And so that's our, you know, h seven arm processor and our root of trust. And we have a 100 gig, NIC chip down there on the board. So this is all on one monolithic board, and then all the power supplies and everything that goes with that. So
[Speaker 3] [06:59] And then one, I think, important property for this is that there's not an an a traditional power supply on this board. So this is plugging directly into a DC bus bar at 54 volts.
[Speaker 1] [07:10] Right. No AC.
[Speaker 3] [07:13] Alright. So, yeah, yeah, you want to take it for so we spend, basically, more or less 2 days not powering just doing all of your pre power checkout.
[Speaker 1] [07:22] Yep. Yeah. So, Aaron and, Robert Keith did a lot of the beeping out, but, you know, there's your there's only so much you can kinda do. And then, you know, as we go through that, we're doing some schematic comparisons too and catching there were a few, like, already known bugs with the board. So we already knew some parts had to be swapped.
[Speaker 1] [07:41] And so we're trying to coordinate rework with our manufacturing partner, to get some of the parts that, like, we don't wanna necessarily have to solder on the bench replaced, especially, like, these multiphase power supplies have huge inductors. And the inductors are really not fun to do on in a bench setup. So you'd rather have them go, you know, use some of their big equipment and take care of that. And so we knew those values were wrong going out there. So we had reels of new parts, but we had to have those swapped over.
[Speaker 1] [08:11] Our manufacturer noticed that, you know, there were some same tech connectors that, don't have a clear pin one indication, and so they had been installed backwards. So, you know, we had a bunch of stuff that we had to kinda coordinate with them to get flipped back around before we did power up.
[Speaker 3] [08:27] And when you're saying beeping out, just to I the the're referring to that very reassuring beep that one gets from the digital multimeter when you are testing for resistance, and you have connectivity, I assume.
[Speaker 1] [08:38] Yes. Yeah. If you turn that feature on. Right? Yeah.
[Speaker 1] [08:41] So, I mean, sometimes we might talk about beeping it out even without the beep because sometimes the beeps get annoying. But, yeah, we're we're looking at, you know, resistance between, you know, whatever 2 conductors you're looking at that point. And you when where you expect to hear the beep is where you expect to have low resistance.
[Speaker 3] [08:58] So then you get to the moment that Steve has led us up to, that Steve believes is going to be, we're going to turn on 54 volts and walk away with this thing. Yep. And so you take us through that. Take us through that initial power.
[Speaker 1] [09:10] Okay. So, so we, you know, we had a Chrome event supply there. Eric, who's on the call, had, you know, had a lot of that set up. And, you know, we hit the power button on the bench supply, and it currently faults. And so, like, that's, you know, probably expected.
[Speaker 1] [09:27] We were pretty conservative with our, current settings. But, you know, when you're bringing up a new board, you always want to have a power supply that's current limited because, you know, something might go wrong and you don't want to melt things. And so, you use a current limit limited supply. It turned out, you know, after we went through, a little more troubleshooting, the current limit on the Chromebook was just way too low. And so, you know, you slowly increase that until you can get over, you know, a lot of times on a blank board, you've got a lot of in rush as the capacitors charge up, and we have a bunch of capacitors on the 54 volt side.
[Speaker 1] [10:00] So, you get the 54 volts up. And so at that point, we wanna check, you know, all of the 54 volt supply. We want to make sure that, what we call our IBC. So that's our 54 to 12. The big converter that kind of deals with most of the rest of the stuff is off at that point.
[Speaker 1] [10:17] We want to make sure he's he's off and happy. We want to look at any derived power from the 54 volts and make sure that those are all, solid. And so the know, that stuff all checked out really well.
[Speaker 2] [10:30] And Nathaniel, just on the current limiter, just to make sure as a dumb software guy, I understand. Basically, you're saying if something is shorted, and you don't have the current limiter, then the board is just a smoking pile. Is that right?
[Speaker 1] [10:41] I mean, the board becomes the fuse. And so whenever the trace is small, right, you will, you'll either heat it up or it will blow as a fuse. And then now you've broken something you didn't intend to break.
[Speaker 2] [10:56] Got it. Cool.
[Speaker 3] [10:58] And then so and I, Matt, SAI, I saw you're here. I know you were, diligently asking us for our, our bring up updates, and I was kinda deferring you to next week for a while. So, I'm glad that you're here. You can get the, the get it lives here.
[Speaker 6] [11:14] Oh, yeah. Brian, thanks for letting me in on this. I am really curious. I was looking at the photos posted by Nathaniel earlier today here. There's this big no man's land Yes.
[Speaker 6] [11:26] Between the front and back half of the board.
[Speaker 3] [11:28] Yes. What goes in the no man's land, Daniel?
[Speaker 1] [11:31] Yeah. So we have a double stack of fans that sit right there.
[Speaker 3] [11:36] Oh, that's So the
[Speaker 1] [11:37] the fans are connected to the chassis. Those are also important to keep, you know, the server cool and everything. It from a like, electrical design perspective, they're kind of annoying because they're, like, right in the middle of where you might like to put stuff. And they take up most of the vertical space in the chassis. So, we have basically nothing on top stuffed in that area so that the whole chassis there's so there are 3 sets of double I think 3 sets of double stack fans.
[Speaker 3] [12:04] Yeah. Three sets of dual rotor.
[Speaker 1] [12:05] It's in there.
[Speaker 3] [12:06] Yeah. It is So Eighty millimetre fans. Those things can move a lot of air.
[Speaker 1] [12:10] And they are very loud. Yeah. And then we have a shroud that goes over the CPU heat sync and the DDR, you know, slots and all of that and blows air. So Yeah.
[Speaker 3] [12:22] So Yep. Sorry, Eric. Go ahead.
[Speaker 7] [12:24] No. More conventionally, like, they'd be in the back, but then because we're using a cable backplate, those connectors take up some vertical space. So we'd have to use smaller fans if we went in the back of the chassis. And so the trade-off of board space versus available, like, cross-sectional area of a fan and the bigger your fans are, the easier it is to run them a little slower and still get plenty of air moving through them.
[Speaker 3] [12:49] Yeah. In fact, actually, the big change we had to make with these fans is they actually default to their lowest PWM, being 5,000 RPM, which is super loud still. So we actually had them modify the fans down to 2,000 RPM so they can run a little quieter. Little quieter.
[Speaker 7] [13:05] Yeah. And hopefully last a little longer. Because if you're not running them at the utter hairy edge, hopefully, they'll not smoke their bearings too quickly.
[Speaker 6] [13:15] And so being in the middle of the chassis, does that present replaceability issues? Or
[Speaker 1] [13:23] so, I mean, for better or worse, those are actually the easiest things to get out. So when you're when you're in a chassis, the fans kinda drop from the top, and they, and then there are connectors on the board. And so you have to pop 3 connectors kind of back near that black heat sink in the picture. And then, the chat the whole chassis that holds all the fans together just essentially lifts out after you take a couple of screws out the side.
[Speaker 3] [13:50] It so we as you may infer, we made the deliberate design decision to not make those fans hot pluggable for a bunch of reasons that we can get into. But the the you've got to pull the sled out to replace the fans. And we got what we call the 3 up design where that whole fan apparatus comes out as 1 piece, and you replace it with a new one. So the with the logic being if one of those fans has failed, the other 2 are going to be due. Alright.
[Speaker 3] [14:17] So, Nathaniel, you want to take us so you so we've got this thing. We don't have smoke pouring out. Steve has
[Speaker 1] [14:24] Yeah. No smoke.
[Speaker 3] [14:24] Steve has done a jersey slide, strangely, way, through the bring up lab. Everyone looking at him awkwardly now.
[Speaker 1] [14:32] Yeah. So we have a tiny ice 40 FPGA in that power domain. And so, you know, it has some derivative supplies that deals with some of the very low level like presence detect and link management stuff. And so that guy had to be programmed. Of course, that's where you start running into some of our first problems where, you know, we had a schematic issue where these, you know, spy signals are swapped around.
[Speaker 1] [14:54] And so, you know, then that means we have to hop in there and pull some resistors off and, you know, put some wires on and that kind of thing, to get the dongle talking to or to get it to so that it could talk to Flash and configure itself.
[Speaker 3] [15:07] And that was as I recall, like, that was a very quick issue to debug.
[Speaker 1] [15:12] Oh, yeah. Yeah. That one was that was pretty easy because, the have a header there to talk, and so we could talk to the flash part or we think in reality, we could talk to the FPGA and not the flash part. And so that was it was pretty clear to figure out what direction was swapped. And then once you have that, you program the flash part and off you go.
[Speaker 3] [15:31] And this is one of 2 FPGAs with that we've got. Correct. And so Yeah. So
[Speaker 1] [15:36] yep. That's a little tiny ice 40, that, you know, it's a 1000 a 1000 LE part, basically. And then we have, an 8 k ice 40 that does a lot of our power sequencing, which we'll probably talk about a little
[Speaker 8] [15:50] bit later.
[Speaker 3] [15:51] Yeah. We'll get to them later. Alright. So we get so we figured that out pretty quickly and get the ignition, I took, got programmed pretty quickly.
[Speaker 1] [15:59] Yeah. Yeah. Once yeah. Once the dongle was talking, then it was up and, you know, Ariane had, a design kinda ready to go so that we could, you know, turn the thing on and off, you know, on the bench, which is what we wanted to do. And yeah.
[Speaker 1] [16:12] So that that was all good. And so then, then you move to, that that controls the IBC. Right? So the IBC is our 54 to 12 volt converter. And that becomes, like, the like, the power for basically everything else on the board.
[Speaker 1] [16:28] At that point, they all derive off of that 12 volts from the IBC. And so, prove that the IBC works, you know, I think we had to add a pull down or something because he was a little unhappy when the FPGA was configuring, little, you know, issues like that. But then 12 volts is up. And so then we start looking at all the supply rails again that are on by default when 12 volts are up. And so, you know, you kinda, like, rinse, slide, and repeat on the voltage you bring up and go through your schematic and check all the things.
[Speaker 1] [16:56] So, no, no big issues there that I remember. And then you're a kind kind of at a point where it's like, okay. We're ready to start messing with our embedded control plane. Right? So it's time to program the service processor.
[Speaker 1] [17:11] And that went super smoothly. That was I mean, like, you connect the dongle and, like, we had a target built for that. You know, you and Cliff had worked on that, and it was very smooth. And, you know, we had our Hubris OS running there just kinda like snap your fingers.
[Speaker 3] [17:28] It was great. And now I I I confess maybe I was doing the Jersey slide at this point because we are now only a couple of days in, and things are going really smooth. This is great.
[Speaker 1] [17:36] Like, we've
[Speaker 3] [17:37] got Yeah. Yeah. It's like we've got we've got the SP up. We've got, and now we're beginning with the service processor up now and us being able we've now from a software perspective, like, we're in business. Now we can begin doing all of our checkouts on all of our I squared z buses and everything else.
[Speaker 1] [17:54] Right. And, you know, as a hardware guy, it was awesome to be able to have, like an embedded target and an OS and a bunch of code that we had already proved out on various dev boards. And, you know, maybe just needed a little bit of a different pin configuration day after getting the SP program going through and doing I squared c bus scans and PM bus scans and that kind of thing to make sure that all the devices that we, you know, do we think we can talk to are all, like, sitting on the network at the addresses that we intended. That turned out to not be the case generally. And so there's a rework to, you know, there was a late maybe not a late breaking change, but there was a spec change at some point in the project that never made it into the schematics.
[Speaker 1] [18:47] And so a bunch of the addresses hadn't actually been updated resistor straps, and you just change them and off you go.
[Speaker 3] [19:02] Well, so this I thought was actually an interesting little though a little design intersection that, where we deliberately did the rework required to bring the board in line with the spec rather than changing the spec. Yeah. Which I thought was I mean, I thought that was an interesting I mean, I guess maybe that wasn't even a from your perspective, but, I guess I I I thought it was interesting that that was the that was a clear direction to go.
[Speaker 1] [19:28] Yeah. I mean, I guess I didn't really consider it an option to not.
[Speaker 3] [19:34] Yeah, there was a Good for you. There was a lot of there was a lot of
[Speaker 1] [19:37] thought put into the addresses that we had chosen. And so and then I know, certainly, I think philosophically, our team doesn't like, implementation driving specification, and just the for the convenience of it. And so, you know, flipping things around to match the spec really made sense. In general, I would say there was one somewhere in the, you know, craziness of getting this stuff swapped around. We did interchange 2 of the power supplies' addresses.
[Speaker 1] [20:07] And by the time we figured that out, we already had a number of boards reworked. And so that one was a spec revision because, but that it was a little different from picking, you know, just a new device out of thin air. It was just 2 parts that had, you know, swapped their addresses.
[Speaker 3] [20:22] And then importantly, changing that changing the specification in that case and making sure that we're we don't wanna what we don't want to have is a bunch of different snowflakes that have got different parts of different addresses.
[Speaker 1] [20:33] Right. Yeah. And so, like, Eric and I, you know, worked at a different company, you know, for a lot of our career. And, like, this was one of
[Speaker 3] [20:40] the is one of the
[Speaker 1] [20:41] key things as you bring up multiple units is to make sure that, they all have a clear life cycle and a clear indication of what they are, and they should all match in general. And so, you know, that's something we both feel really strongly about. And so we had, you know, written an RFD on that process before bring up to make sure we call them model change notices. But, essentially, you build an atomic change and then document changes to it. Yeah.
[Speaker 1] [21:18] This is the
[Speaker 3] [21:19] Wait. No. It's such a great process. And then the other thing that I thought you guys also brought in terms of, like, bringing engineering culture is just the documentation of
[Speaker 1] [21:33] worked out better than I think any of us could have imagined. I mean, we invited Aaron to come, and he kind of lived, less as, like, the guy with the soldering iron and more as the guy with the keyboard. And so he sat there and just took, copious amounts of documentation and notes and of all the changes. And, I mean, really, this that was more documentation probably than even we had ever experienced anywhere else, as part of bring up just because we were able to, like, put a person in the seat to and that was his job. And that Aaron did an awesome job of that.
[Speaker 3] [22:05] That's funny. You know, I could have assumed that you guys had always done it that way because I it just seemed it felt so natural. It seems like such a good idea.
[Speaker 1] [22:12] It is really does. And I mean, after having done it, you know, I'm I'm sure we'll get to more of it, but, like, that really has paid dividends.
[Speaker 8] [22:18] Yeah.
[Speaker 1] [22:19] And so I like, I don't see us not doing that ever again. I think, you know, it's totally worth one more, you know, one more person sitting there just focused on, you know, documenting. And then I think that's helpful too as a company where, like, the whole team can't really come down to the lab because not everybody was on-site and, like, really, not everyone is ever on-site, you know, for any bring up since we have people kinda spread all across the country. Being able to, like, clearly document that stuff in a way where the rest of the team can follow along and be, you know, appraised of the changes and understand what's going on and ask questions, I think, has been really valuable.
[Speaker 3] [23:00] It's been really valuable. And I think, you know, what an up a point that you know, we are not And really, it'll let yes. No. You're totally right. Okay.
[Speaker 3] [23:15] So we've got the the SPs up. We're going through these I squared c buses, making some minor mods, but things are looking pretty good.
[Speaker 1] [23:23] Things are. Yeah. And we're starting to, like, approach the period where, like, things that we have previously integrated, like all the software and everything, we're sort of running out of the like, things that we know work. Right? And so, you know, at a certain point, you and Cliff, you know, hop on a plane to head out, because and we've we've been trying to get the, the FPGA, you know, that's sitting there, involved.
[Speaker 1] [23:49] So that, like, I'm responsible for some of that and, like, getting the SP to program that. And, you know, so I think, Cliff was hacking that that driver on the plane as he flew out to Minnesota for us. But, and, you know, we had found a couple more schematic problems there where we had multiple things sharing a spy bus and so there are some bus contention. So we had to have some parts ripped off. And so managing that with our, manufacturing partner.
[Speaker 3] [24:14] Yeah. And I think that speaking from my perspective, and I think Cliff's too. I mean, I indeed, the entire company. Like, you really just don't want the code that you're me that we're blocked on. So we're just trying to, like, how can I just need to stay, like, a block ahead of the parade here?
[Speaker 3] [24:36] And, we were doing that a bunch.
[Speaker 1] [24:41] Yeah. I mean, I think there were a lot of jokes about the eye of Sauron and, you know, who it was pointing at anyone. That's
[Speaker 3] [24:46] right. I know. I know. And I think it's to a certain degree, like, on it, like, we are such a team oriented team that nobody wants to let the team down. So it's like the eye of Sauron ends up being, like, much worse, I feel.
[Speaker 1] [25:00] Right. Yeah. So, you know, we had a few other things to do and then, you know, you guys had landed, and we made it there, and we're tried and, you know, Cliff had done a lot of awesome work to get the FPGA loaded. So, you know, we've got FPGA loading. We got, you know, spy traffic kinda running back and forth between them.
[Speaker 1] [25:18] We can communicate some, you know, new drivers, and that kind of thing, you know, all hacked out. And, and, you know, then it's like, okay. We're ready to, like, start exercising the sequencer. And so that's you know, this is all stuff that we have now really not been able to test up until this point. Right?
[Speaker 1] [25:36] We haven't had the hardware. We don't have things that handshake like the sequence
[Speaker 3] [25:43] sequencer is. Like, what what what is sequencing? Why is this a problem?
[Speaker 1] [25:47] So, generally, AMD has a fairly complicated power on sequence, you know. So there are, I don't know, somewhere around 12 or 13 rails that go into the AMD chip, and they kind of all want to be brought up in a certain order. And then, you know, as you look at, like, take a step back, the Simms have, you know, 3 or 4 rails coming into them, and they want to be powered on and off in a certain order. And you want that stuff to be sort of deterministic. And so, you know, a decision that was made a while back was to push a lot of that FPGA and then the sequent the FPGA logic runs off and turns a bunch of things on.
[Speaker 1] [26:32] And there are some checkpoints with the software at various, you know, spots along that way to make sure that things are working. And you bring up all the rails for the Simms and the AMD processor.
[Speaker 3] [26:44] And where does the sequencer get into the stream from?
[Speaker 1] [26:47] So the sequencer, well, you know, at the very beginning, we put it in an in a flash, and then we realized the flash and the SP and the sequencer were all contending on the same bus. And so Cliff did some cool work, and we pushed that into the SP's flash image, and we just ripped the flash parts off the board. So we had our, manufacturing partner run around and pop off a couple of the BGA flash parts. And we did one there on the bench with the hot air gun, which, this board, you know, it's an 18 layer board and, every other layer is ground. And so getting this thing warm enough to pull stuff off easily when you're trying to pull, like, a BGA off is a real pain.
[Speaker 3] [27:29] Yeah. So tell me about that board heater because the board heater I unfortunately, I didn't get a chance to watch that thing run, but everyone was just marvelling at the board heater.
[Speaker 1] [27:37] Yeah. So our manufacturing partner had a little pace, you know, maybe kilowatt heater or kilowatt and a half maybe. And, you put that underneath, and you put the board in a rack on top and you let that guy run. And so he heats up the bottom of the board. And you know what?
[Speaker 1] [27:53] You're you're trying to get the thermal mass of the board to get up close to reflow temperature so that then when you hit it with a hot air gun, you're you just kinda like slowly crest across the, you know, the temperature that makes the solder turn go from solid to liquid.
[Speaker 7] [28:09] Yeah. For And For, like, non hardware people, imagine a toaster oven with a convection feature, and you literally flip it on its back, open the door, and then put a board on top of it. That's basically what the board preview is.
[Speaker 1] [28:22] It's like a little space heater almost.
[Speaker 7] [28:23] Yeah. It's convection of it with a hole in it.
[Speaker 3] [28:26] And if I and reflow temperature, this is the temperature of the solder at which point the solder is effectively liquid.
[Speaker 1] [28:33] Right. Yeah. So it's somewhere up in the like, 250 c range. You know, it kinda depends on what kind of solder you're using, but for lead free stuff up around 2 to DC. And so but you wanna kinda heat the board up to, like, you know, a 150, maybe.
[Speaker 1] [28:47] You don't want to melt all your plastic, but, you want to make it so that your hot air gun just has to do a little bit of a push to get across and turn everything liquid. And so we did one of those, there on the bench with, you know, and that was, you know, as much fun as that was. We didn't want to do the other 12 like that. So we are the other 11. So we set the other 11 back to, you know, we had, you know, our manufacturing partner who's who we were at.
[Speaker 1] [29:14] They could run them through their big BGA rework station and pull all those off pretty easy. So we had them go do that for us.
[Speaker 3] [29:21] And I think this is a is a really neat little change of the bit stream being in the SP image itself because it means the attestation of the SP image automatically attests this bit stream that we're gonna dynamically load onto the FPGA.
[Speaker 1] [29:33] Right. Yeah. And you also avoid a whole class of errors where, like, one thing got updated and not the other, and you have to figure that out.
[Speaker 7] [29:41] You also avoid manufacturing issues with the flash part goes obsolete, and you have to qualify another one. There's limited parts that work. And
[Speaker 1] [29:49] Yeah. And, I mean, finding flash has not been a problem this year. Right?
[Speaker 3] [29:53] So Yeah. Right. There's no supply chain issues.
[Speaker 1] [29:57] So, I mean, the cool thing is we freed up that part. So we have a bunch more flash parts. We use that part in a couple other places on the board. So we have a bunch more, inventory than we maybe intended to have.
[Speaker 3] [30:06] I thought we're we're just we sell those parts in lieu of doing our next raise. I assume we were just Right.
[Speaker 1] [30:11] There you go.
[Speaker 3] [30:13] Some, some flash gray marketing activity. Right.
[Speaker 1] [30:16] Right. Yeah.
[Speaker 3] [30:17] No. As far as you know.
[Speaker 1] [30:21] And yeah. And I mean, since then, Cliff has done some cool work to, you know, to compress the bit stream even nicer on that thing and then decompress it on the fly. So it takes even less flash, than it did while we were there in Minnesota, 2 months ago.
[Speaker 3] [30:36] Can we stop for a moment just from a software perspective to praise include bytes? This is what, Adam, the include byte. Have you used include bytes or includes STR, the macro? I've used include STR, but I haven't used include bytes. So include bytes is just the logical equivalent.
[Speaker 3] [30:50] So those of you I mean, this is like a religious experience I feel with Rust to discover include bytes and include STR, take a file off the file system and drop it in effectively into your file as a string or as bytes, which is great for an FPGA bit string. Right? So pretty neat. Yeah. Very cool.
[Speaker 6] [31:09] So I am curious. How are you guys planning to attest the FPGA image before doing this?
[Speaker 3] [31:15] Well, so we will the in terms of, like, how do we attest that the blue spec that we are generating is that the that bit stream has not been tampered with? Or what do you mean?
[Speaker 6] [31:26] Right. So, I mean, I can see how you can attest to the software image that then loads the SP, which then loads the FPGA. How are you planning to do that before you made it load in that sequence? Or were you just not attesting the FPGA?
[Speaker 1] [31:43] So do I mean, we're not currently attesting the FPGA for development, but the plan always, I think, was to do this. But we had the flash part on there kind
[Speaker 8] [31:56] of as a fallback in case, you
[Speaker 1] [31:56] know, we didn't have the software there in time, or we didn't want to deal with that right now.
[Speaker 3] [32:01] Okay. So this
[Speaker 6] [32:02] is just brought up magic.
[Speaker 8] [32:03] Yeah.
[Speaker 1] [32:03] This is just brought up magic. Okay. I mean, it's its always cooler when you get what you hope your product solution is as kind of the earliest thing too. But, you know, when you're like throwing hardware, down in the schematic, you're just never sure where you're going to land. And and and like I said, like, that driver was, you know, essentially written on the plane as Cliff flew out.
[Speaker 1] [32:24] And so, you know, it worked pretty well for plain code.
[Speaker 3] [32:28] Right? For plain yeah. Cliff writes great plain code, I have to say. I've been into I mean, certainly much better than my own aircraft code. Like, the plain code's pretty great.
[Speaker 3] [32:36] Alright. So we now have the sequencer. So now we're going through because I'm trying to think of the things we're trying to do before we powered on s p 3, which is the the actual AMD socket.
[Speaker 1] [32:48] Right. So as we went through sequencing, you know, we found, a few different problems. I mean, sometimes the, you know, net names, maybe were called out active low and the parts were actually active high. And so, like, the FPGA bit stream had to be kinda flipped around a little bit. So we did, you know, kind of bunch of that.
[Speaker 1] [33:08] And then, like, as we're going through this, we get to the level translator issue. Do you remember that?
[Speaker 3] [33:15] Are we gonna talk about the blown inductor first? I feel like that we've I feel like the thing that that wait. I have to think we can talk about zombie board.
[Speaker 8] [33:22] Eric, are
[Speaker 3] [33:22] you gonna talk about zombie board or the balloon eductor.
[Speaker 1] [33:25] So, yeah, somewhere along the way as after we got the embedded stuff up and running, we sort of had enough of the board risk retired where we were, willing to, like, risk more boards. And so, you know, we started bringing on a second and third board. Right? And so once we had a second and third board, we could pass the second one of the boards off to Eric who does a lot of our power stuff. And so he started looking at, you know, with the AMD has a fake processor load called DS CLE.
[Speaker 1] [33:55] And so he started looking at some of that and some of the other power supply designs. So maybe he wants to talk a little bit about how zombie board was created.
[Speaker 2] [34:01] Well, hold on. That thing, just to see if I understood that correctly. So early on, you only have a limited number of bullets here. So we're we conserve them and move very slowly, it
[Speaker 7] [34:10] sounds like.
[Speaker 2] [34:11] But then when we gain a little bit of confidence, then we're able
[Speaker 1] [34:13] to parallelize. Is that right? Yeah. So, you know, it's kinda like the know if you have a bent socket, you don't want to stick a bunch of pins in there. And then every, you know, like, every you know, back in the days when processors actually had pins, you know, if you had a damaged socket, you wouldn't want to run all your processors through there because you could accidentally damage all of them.
[Speaker 1] [34:31] And so, you know, until we got to a certain point, we really were single threaded on a single piece of hardware, doing all the rework on that guy to make him happy and to prove that like, you know, we didn't have some major oops that was, you know, going to melt parts or ruin other things. And so by the time we got to, like, the SP up and running, it's kinda like, okay. We have enough stuff here. We have the power supplies up. Everything's being controlled.
[Speaker 1] [34:57] You know, the we have varying amounts of rework on, you know, certain things, but we kind of understand all of that. So let's go execute that rework on a board 2 and a board 3, which were kind of coming off the line hot from our manufacturing partner to,
[Speaker 2] [35:13] they
[Speaker 1] [35:13] should they had done flying probe. So which requires some development once you have hardware. And so we got our first unit, but without having gone through flying probe.
[Speaker 3] [35:25] And then they just a little plug for flying pro flying probe is so cool for those who
[Speaker 1] [35:29] It is cool.
[Speaker 3] [35:30] Yeah. Who it's a maybe just a little explanation of flying probe.
[Speaker 1] [35:33] Yeah. So it's, it's an automated, DMM, basically. And,
[Speaker 3] [35:39] DMM digital multimeter. Sorry. Yes.
[Speaker 1] [35:41] Right. Yes. So, it is has robotic arms that move, you know, on the top and the bottom, and it has, spring pins. And so it is moves down and touches electrical contacts on your board. It moves up from the bottom, and you can test continuity.
[Speaker 1] [36:07] So they take your net list in, which is cut you know, like, all the electrical nodes on your schematic, and they figure out what they can hit with those probes. And then they program the machine up to go through, and it uses your CAD. And it goes through and checks continuity, you know, in those areas. And it can do some limited, like, resistor measurements and capacitor measurements and that kind of thing.
[Speaker 3] [36:27] And videos of this are mesmerizing. So definitely go watch videos of this.
[Speaker 1] [36:32] Yeah. And it has, you know, they have a limited number of probes. So it's not like a bed of nails where everything gets tested concurrently. And so it just moves around and it yeah. They're they're fun.
[Speaker 1] [36:42] There are a lot of good YouTube videos about that.
[Speaker 3] [36:44] Okay. So you've got these boards that go off hot. Sorry. Yeah.
[Speaker 4] [36:47] No, Nathaniel. Sorry. Just one other thing that I wanted to mention is we that we skipped ahead of. But to the uninitiated, one of the things that was fascinating for me was in that first stage to bring up, I think it was, like, a FLIR camera app that Arian had Oh, yeah. That we were using to detect when parts were starting to warm up, which indicated life.
[Speaker 4] [37:10] And,
[Speaker 3] [37:11] Or death.
[Speaker 4] [37:12] Or death. And that was, again, back to the those in the, in the bleachers with popcorn, that was pretty fascinating to watch, the test and being able to see parts kinda come up live on that thermal camera.
[Speaker 1] [37:26] Yeah. Especially when you mean, that's a that's a common trick, you know, as you bring parts up, you know, put a thermal camera on there. You know, maybe some people have seen resistors get really hot in certain power circuits, not on this board, but it, you know, in other boards, and it can teach you a lot about what you messed up, in your design for essentially free. And so, yeah, I have a seek thermal that connects to my camera and Ari and had a flare. And so, you know, putting those on, and you could watch especially when you start bringing, the power stages on which as we get to zombie board.
[Speaker 1] [38:00] We'll
[Speaker 3] [38:10] zombie board?
[Speaker 7] [38:12] Yeah. So before we put the AMD load simulator, the SALE in there, we wanted to get I wanted to get these processor power supplies up and running even without that just in case it sent 12 volts at them because I don't want to blow up our one load pod because they're hard to get. And so I hardwired the feedback, back to the controllers and turned things on, and it is seemed to be kinda working. But there was a there was a bug in the schematic where there was a recommendation that wasn't followed on one of the current sense signals going to the power stages. And to give you an idea, like, the core of this power supply when you're doing this testing can pull north of 250 amps at, you know, a volt or so, during testing.
[Speaker 7] [39:00] I mean, they don't do that in normal life usually unless it's a surge, but that's what they that's what we test to. And so this particular error caused the current feedback from these power stages to be bad, and that caused the controller to kinda lose its mind. And this is an 8 phase power supply.
[Speaker 3] [39:20] So 8
[Speaker 7] [39:20] of these stages, the 8 of these switching supplies, each of which can theoretically put on 90 amps. You never use them that high, but it caused one of them to, go bonkers, and it, sent 12 volts right at the output. And one of the things that you do on these low voltage power supplies is you never really put high voltage rated parts on there. So the first big capacitor that it hits after it goes through this power stage is a 4 volt rated, aluminum polymer cap. And at 12 volts, that thing becomes a lovely resistor.
[Speaker 7] [39:56] And it, it got a little toasty, which I found out by accidentally touching it after the thing started going through the thing like that.
[Speaker 3] [40:03] So I
[Speaker 7] [40:03] touched it. Yeah. I think
[Speaker 3] [40:04] it's the hell. So we
[Speaker 7] [40:06] bring some turn it off, bring the thermal camera over, turn it back on, and there's this glowing red death right at the bottom. It's like, oh, that that's that's not good. So
[Speaker 1] [40:17] I do find that's usually the sign to bring the thermal camera out is when somebody burns themselves on something.
[Speaker 7] [40:24] Yeah. That's
[Speaker 3] [40:25] God's own thermal camera.
[Speaker 7] [40:27] Nathaniel's comment on a resistor is there's another board that we had designed that had a random resistor on an FPGA that was just smoking hot and barely not resoldering itself. We found that using a thermal camera. Little tiny o four zero two thing that was, like, a 150 c. But yeah. So zombie board basically committed a side at that point.
[Speaker 7] [40:48] But luckily, our rework person was awesome, and she was able to pull that power stage off, put another one on. And I tried firing it back up, but the 12 volts had damaged all the caps. I was hoping it hadn't, but I had to rip off all those caps and replace them. And once that happened and we, we got that one problem with the current sent fixed, then it, it fired up much, much nicer after that.
[Speaker 3] [41:16] Yeah. And I just want to make clear because, Adam, I the Nathaniel and, Ed and Eric both mentioned this, but they may have gone past it quickly. The the SALE that we're using is this really important piece of equipment that AMD makes that is a load generator. So go ahead, Eric. Yeah.
[Speaker 3] [41:35] Describe Save because Save is really pretty cool.
[Speaker 7] [41:38] Yeah. So instead of, you know, retail high-end Milan processor being, like, 5 grand or whatever, instead of just throwing Milan in there and, you know, praying to whatever god he wants to that it doesn't immolate, into a ball of fire. You put this fancy load pod on there, and basically what it is a bunch of electronic resistors. We, you know, use Moses. And it abuses your power supplies in a controlled manner and watches how they respond, and there are limits to what it can what it will allow.
[Speaker 7] [42:11] So, like, it'll do a load step from, let's say, 50 amps to 200 amps, and the voltage that it does that to can't change by more than, you know, a couple of percents of its voltage. So if you have, like, a one volt rail, and you do a 150 amp load step, it can't change by more than, let's say, 10 millivolts or 20 millivolts, And that's, like, 1 or 2%.
[Speaker 2] [42:36] And does this thing give you some readout or diagnostic or or or some report card of how you did?
[Speaker 7] [42:41] Yes. It's pretty slick. Like, they built it in mat in, not Matlab. It's a Simulink. No.
[Speaker 7] [42:48] God damn it. What is it? Lab view. Live view. Thank
[Speaker 3] [42:50] you. View.
[Speaker 7] [42:50] So they built it in Lab view, and it's, you know, executable, and it connects to this thing. And it's its pretty fancy, but it spits out basically a giant CSV, and they have some x Excel spreadsheets with macros in them that digest that and spit out some nice graphs that show you, like, your minimum maximum voltages, the, you know, voltage versus frequency. And this load step it does, it doesn't just do it once. It does it repeatedly for, like, a second at a time, and it does it anywhere from, like, a kilohertz up to, like, 300 kilohertz. And so it'll just slam this thing, and you can actually if you're in a quiet room, you can hear it go through the different frequencies in their audio range because the magnetics, start humming.
[Speaker 3] [43:33] And That
[Speaker 7] [43:33] sounds really cool.
[Speaker 8] [43:34] It is
[Speaker 3] [43:34] really cool. And so and also, this thing is speaking so AMD has a protocol between the the actual CPU and the controller. And so this thing called s v I 2. So this thing is speaking over that protocol and verifying, that it's getting the right answer back. So which is really, really neat because it allows you to actually completely check this out before actually loading up a real CPU on there.
[Speaker 7] [43:59] Yeah. So they're it's completely invaluable. Intel has the same thing for their stuff, and there are commercial companies that make independent ones that are, like, load slammer, and Intel has their own version of load swimmers. And it's kinda standard a lot with, like, ASIC bring up because, you know, you only have a few revs, you know, rev 0 ASICs. So you want to make sure your power supplies are very well-behaved before you put that, you know, very first silicon into a board.
[Speaker 2] [44:33] This sounds a little bit, Brian, like what we talked about last week with the switch and the at the Torino 2, like, physical sample part for testing Yep. Kind of physical characteristics.
[Speaker 3] [44:45] Yeah. Absolutely. And in fact, Eric, one of the the mean, Eric actually mentioned load slammer. We have for Toughing too, we one of the first things we did is got a load slammer for that part. So we're going to be able to do the same thing when we do the sidecar ramp.
[Speaker 7] [45:00] Cool. Yeah. That that thing makes AMD's power requirements look trivial.
[Speaker 3] [45:06] Yeah. So alright. So, state so we've got actually, the point, we didn't think it was zombie board. We thought it was dead board. And then when it came back, we realized that it was going to
[Speaker 7] [45:15] be again?
[Speaker 3] [45:16] It was alive again?
[Speaker 7] [45:17] Yep. It couldn't, Yeah.
[Speaker 1] [45:18] We that was, like we're sitting at dinner that night. So this is a Saturday, I believe. And we're sitting there at dinner. And so I texted our manufacturing partner and just asked, you know, what are the chances that we could have a rework person come in on Sunday? Because we're going to be back doing this, and this
[Speaker 3] [45:35] is one of the 2
[Speaker 1] [45:36] or 3 boards that we have access to at this point. And so they managed to get, their high-end reworks person back in there on a Sunday morning and, and did the work for us. So and then we were able to get this board back in our hands and it is still functioned albeit with some quirks, which are fine.
[Speaker 8] [45:55] Yeah.
[Speaker 7] [45:55] We superglued the socket cover back onto that one, so nobody accidentally puts the process in it. But the nice thing is once so once we got that one problem figured out, like, the 2 biggest power supplies, the core power supply for the AMD and the SOC, which is, like, the hidden processor power supply, both of those passed the SALE testing with flying colours. Both those are just fan freaking tactic. It was great.
[Speaker 1] [46:21] And we may come back to those later.
[Speaker 7] [46:23] And those yeah. The other rails had some quirks and whatever. But at least the 2 big ones, power wise, they worked fabulously.
[Speaker 3] [46:39] Alright. So, we're, so we are now getting ready. We got zombie here, and it's now, I think we are now getting ready to to to actually attempt our first SP 3 power on, I think, at this point. Right?
[Speaker 1] [46:53] Yes. Yeah. So we this is probably now Thursday of the 2nd week. Right? And, we're we've got a processor loaded in there, and we're we're going to try to power this thing up.
[Speaker 1] [47:10] In fact, I did we have done we actually put a processor? We must have.
[Speaker 3] [47:14] Yeah. I don't
[Speaker 7] [47:15] think we put them a lot on them or a Rome.
[Speaker 1] [47:17] Or Rome. We had a Rome processor in there.
[Speaker 3] [47:19] Okay. And then because it was the level shipping issue on when we first attempted the should describe the level shipping issue because that was still definitely another major hiccup.
[Speaker 1] [47:29] Yeah. I'm trying to remember if SALE was connected or not, but regardless, we had, we so there's a level shifter. There well, we have a lot of level shifters. There's an ice squared c level shifter on there. And the mean, to, I guess, give the answer before the walk-up, that that guy was misbehaving.
[Speaker 1] [47:55] But we didn't know that at the time. And so what we saw as we're going through some of this stuff is we're seeing, like, I squared c transfers not work and a bunch of really strange things. And so we've got our to the bus, and we're looking at your know, this is like the ISR on then points back at Brian because, his I squared c thing is, or it's its PM bus thing is pulling bus reset, like, on loop. And, you know, we're, like, what in the world, you know. And so, you know, like, anyway, we're all looking around.
[Speaker 3] [48:32] The eye of Sauron is going googly eyed at this point. The eye of Sauron just seems to be going everywhere.
[Speaker 1] [48:37] Because we mean, we thought, like, we'd load a different FPGA, and we get different behaviour even though the FPGA doesn't even sit on that I squared c bus. And so we're building FPGAs with, like, all the pins restated and all the pins high and all the pins low, trying to figure out what is causing this. And the FPGA is somehow related to this problem. And so, you know, as we got through it, we started, you know, binary searching basically on the FPGA pins, you know, turning them all high and all low.
[Speaker 3] [49:06] Well, in the video, I think it's also a very important detail that led us down the wrong path on this. This appears to only be happening on one of the boards Right. Which it turns out was a total accident. Like, as it turns out, both boards would we and we were basically in undefined behaviour effectively. And maybe you want to define a little bit what a level shifter is and why they're so problematic.
[Speaker 1] [49:28] Well, so, so level shifters, especially on a bidirectional bus like I squared c, are especially tricky. Right? So a a level shifter bus, it has the circuit has to be able to do high to low and low to high and figure out which direction it needs to do and kinda like, these things end up all being kind of magic. And really, they're not. I mean, you know, you can go in and figure out how these parts work.
[Speaker 1] [50:02] But it turns out that the part that we had chosen here did not have defined behaviour on both sides of it when one side was powered down. And so one board worked a certain way and the other board worked a different way when they were both in the same state where one of the two sides and that's the side that is powered and things are working. And the SP is sitting on the other side of the bus, which is the side that wasn't or maybe vice versa. But like what we were looking at on the analyzer was not actually what our processor was seeing because this, level translator was, you know, kind of acting like, a mirror, basically, and you couldn't actually see what was going on behind the mirror.
[Speaker 3] [50:54] I think the eye of Sauron was burning a hole in my brain at that particular moment because that definitely looked like this is a like, the SP is doing something is misbehaving with respect to I squared c is what that looked like. Right. And in certain
[Speaker 5] [51:08] And this was also where this was also where we were digging through data sheets trying to understand how does this level shifter actually work. Like, what are we missing detail wise? And the level shifter is offered by 2 manufacturers. They make the same device, but, you know, they offer compatible parts. And one of the data sheets tells you absolutely nothing about how it works.
[Speaker 5] [51:29] The other one tells you just enough that implies that you understand how it works. But until you notice that they actually have links to YouTube videos illustrating how it operates, that's the only place that they actually describe how the part works.
[Speaker 1] [51:43] Well and we mean, it turns out that with these same level shifters, we had a different level shifter problem once we got back home as well. And, like, it all hinges around these things don't really have defined behaviour when they're powered off.
[Speaker 7] [52:00] The one the ones we picked. There are
[Speaker 1] [52:02] devices that we picked. There are ones that do. Yes.
[Speaker 7] [52:04] But, you know, with Fast Dash, they make it makes it a more of a pain
[Speaker 3] [52:08] to find nice supply, nice, mobile
[Speaker 1] [52:11] They may have been the ones that were available.
[Speaker 3] [52:14] They may have been. But it was I mean, if it was interesting object lesson in a lot of different ways. I mean, one, I feel like, you these kinds of I score c level shifters.
[Speaker 2] [52:29] Brian, we lost you.
[Speaker 1] [52:34] Yep. We did.
[Speaker 6] [52:35] The little shifters got them.
[Speaker 1] [52:37] Yeah. Yeah. Pretty much. Powered off. Yeah.
[Speaker 1] [52:39] I mean, those things, they're for things that should be I mean, seemingly are very simple in your circuit, they end up being a very complicated, in practice. And you really do have to go through and, may not you know, make sure that you understand how these things work.
[Speaker 7] [52:58] 1 And it also depends.
[Speaker 1] [53:00] And as Rick said, like, some of the data sheets are not helpful. Like, you read the every page of the data sheet, and you have no idea how the thing actually works. So And we picked this particular component because we could source
[Speaker 2] [53:15] it or because it was compatible with different things?
[Speaker 1] [53:17] Yes. Yeah. I mean, yes. And I mean, you like, every one of the insiders has some quirk, and so you're just, like, we were using this in other places, and, you know, its specs are good enough for the data rates we're looking at, and we could source it. And so that's how we kinda ended up with these.
[Speaker 1] [53:35] And if you pick a different family, then you just get a different set of issues.
[Speaker 3] [53:40] Gotcha.
[Speaker 2] [53:40] So you just fire up those YouTube videos and learn about spec.
[Speaker 1] [53:43] That's right. Yeah. Oh, gotcha. Yeah. I mean, shout out to TI.
[Speaker 1] [53:46] TI has Yeah. A much better datasheet on these parts. Yeah.
[Speaker 8] [53:50] I mean
[Speaker 6] [53:50] So, of course, it's t I.
[Speaker 7] [53:52] But,
[Speaker 3] [53:53] this is the most
[Speaker 6] [53:54] t I think I've ever heard.
[Speaker 1] [53:55] Right. Well, their datasheets are much better than YouTube videos. Experian. Hesperia.
[Speaker 7] [54:02] Yeah. Hesperia is
[Speaker 6] [54:03] Yes. But they're also notorious for putting that one footnote that you really cared about, like, on page 364 behind the door marked beware of Jaguar.
[Speaker 8] [54:12] Yeah.
[Speaker 2] [54:13] Because
[Speaker 1] [54:14] right. And actually is there.
[Speaker 3] [54:18] This issue was clear in retrospect, but at the moment and in some regards, like, the scariest moment for me was when you, Cliff, Eric, and RFK all had a look of total what the fuck is going on. Like Right. Fear. Like, actual fear in all four of your eyes. And I'm like, okay.
[Speaker 3] [54:39] I am terrified. If these 4 are scared, I'm wetting my pants because,
[Speaker 8] [54:45] I've just
[Speaker 3] [54:45] you know, you got engineers who've got are pretty few of us engineers with different perspectives on things, and when everybody has no fucking idea.
[Speaker 1] [54:52] Well and yeah. Because we discovered it while I'm playing with the FPGA, but the FPGA doesn't sit on the bus. That was the part I think that, like so, like, you can, we could pretty conclusively prove it was the f like, the FPGA was doing something, but how that interacted with us? And I mean, it turns out the FPGA was controlling the power to the thing. Right.
[Speaker 1] [55:12] And so, you know, once you figure that out, it, it becomes a lot more obvious. And, but yeah, up until that point, we're, like, the FPGA is not even sitting on that bus. How can it be messing up that I squared c bomb?
[Speaker 3] [55:24] I mean, it literally is like, I'm turning on and off lights in Houston, and Atlanta is bursting into flames. And I do not understand how these things could possibly be related. But so we get we get through that, which is that was a good moment. And now it feels like, let's go power this thing on. Right.
[Speaker 3] [55:41] Let's go Yeah. Then what?
[Speaker 1] [55:45] Well, let's see. I'm trying to remember
[Speaker 3] [55:47] We did the next morning. What happened? It was because that that that was late. So we broke up late that night. We're going to come back the next morning.
[Speaker 3] [55:54] Cliff and I have got flights out the day after. We're gonna power on s p 3. It's all going to work. It's going to be amazing. And it does not work.
[Speaker 3] [56:05] We come back out, and, we roll s we actually populate the s p 3 sockets. I think Friday morning I want to say Friday morning was the first time we tried to do that once we had that issue resolved, but maybe that's I've got the timing wrong.
[Speaker 7] [56:17] I think, like, we were getting ready to head out.
[Speaker 3] [56:20] Yes.
[Speaker 7] [56:21] Yeah. Packing up the mobile lab back into the minivan.
[Speaker 3] [56:26] And we and it is it And
[Speaker 1] [56:30] and it is just like, nothing really happened. Right?
[Speaker 3] [56:32] Nothing really happened. And so the so the and what are we looking for is kind of the first thing of first sign of life out of the CPU.
[Speaker 1] [56:41] If
[Speaker 3] [56:41] anyone want to describe that.
[Speaker 1] [56:43] Yeah. We're looking for spy wiggles. Right? So the mean, the way these processors boot, you do some handshaking and then kinda, like, they boot out of, like, an on chip ROM, basically, and execute some code. Their PSP does.
[Speaker 1] [56:58] And then, you know, in fairly short order, they're going to go out the spy interface the way we have this strapped and attempt to fetch code. And, and so we did we had wires tacked onto that spy interface and, like, nothing is going on. Nothing's dumping out that you are and, like, we're, and we're running out of time, really, there in Minnesota.
[Speaker 3] [57:21] Running out of time and alright. Can't get it working. You and Eric are going to take the boards back to Wisconsin. The and we also decide to send you with all the Melan's and a bunch of DRAM. I we just the cargo of the minivan was worth much, much more than the minivan.
[Speaker 1] [57:40] Oh, oh, yeah. Because this is a rental town and country. Rent all. Exactly. Expensive.
[Speaker 3] [57:45] Right. Right. And, and then you've also got the Sales. The SALE being the the the load. Irreplaceable.
[Speaker 3] [57:53] Irreplaceable. Right. And, and we
[Speaker 1] [57:56] You had instructions for us.
[Speaker 3] [57:58] I did. Right. If carjacked, give them the DRAM and the Milan CPUs
[Speaker 7] [58:03] You're like, here you
[Speaker 3] [58:03] not part with the SALE.
[Speaker 7] [58:04] You can hack these you can hack these easy on eBay. They're unlocked. Like, you have no problem unloading them. Just connect for the love of God. Don't touch these 4 boxes.
[Speaker 3] [58:13] They are worth nothing
[Speaker 7] [58:14] to you. You can't sell them, and they are they're they're worth everything, please.
[Speaker 3] [58:18] They're they're they're priceless. Right. We only have one SDA. Fortunately, no carjacking. Problems.
[Speaker 3] [58:25] Right.
[Speaker 2] [58:25] No pirates.
[Speaker 3] [58:26] Gotcha. No pirates. No piracy. You're right.
[Speaker 1] [58:29] Safe and at home. Safe and
[Speaker 3] [58:31] at home.
[Speaker 1] [58:32] All the equipment.
[Speaker 3] [58:33] But So, so Yeah. Go ahead. No. I'm sorry. Yeah.
[Speaker 1] [58:37] I was just going to say, so then we start the like, okay. Now now now what? Right? Like and so, you know, we have a board. And so it's, like, well, we must have done something wrong sequencing.
[Speaker 1] [58:49] And so let's go let's go read AMD's documents and, you know, so we get, a board set up here on my bench, and I rework a bunch of wires onto it. And, I mean, Eric and I spent a couple of weeks in my home lab here, you know, doing various testing. I mean, like, lots and lots of testing. You know, check power supplies. We wire out all the sequencing stuff.
[Speaker 1] [59:11] We know, the first time we try it, we, you know, get every like, the whole team on a call late at night one night and watch nothing happen
[Speaker 3] [59:20] Nothing happened. Essentially. And then At this point, like, Steve has been wounded so many times that he's just like, alright. But Steve is so enthusiastically joining. It was like, no.
[Speaker 3] [59:31] No. No. Nothing's happened. Right.
[Speaker 1] [59:33] And so then I feel like, you know, another few days go by, and we find some more things, and we fix some more things and, you know, it's like, then, then we do another call and a bunch of people, you know, from the team join. We get on there and we show it. And this time, not it's not nothing that happens, but, like, we're playing with power navigator, which is MMM. The software that's that's driving, that's driving the power controllers. And so I've got that.
[Speaker 1] [01:00:01] That's like a sideband in addition to our SP control.
[Speaker 7] [01:00:04] Sitting on the same I squared c bus DSP is.
[Speaker 1] [01:00:07] Yeah. Yeah. And it's so it's got a dongle, like USB dongle. It's mastering I squared c, but it's pulling and doing a lot of traffic. And, you know, as we're talking through it, I think, the suggestion comes out to do an squared c bus scan.
[Speaker 3] [01:00:20] God. Who made that suggestion? I that that is negligent. I mean, that is odd obviously the wrong thing to do. Furthermore, I mean, boy.
[Speaker 3] [01:00:30] You know, blameless post-mortem, but I need some names.
[Speaker 1] [01:00:33] Right.
[Speaker 3] [01:00:34] Okay. That would be Yeah.
[Speaker 1] [01:00:35] So Brian suggests we do an squared c scan, And and and so we do. And, like, the instant I execute that command, like, everything in Power Navigator goes from green to red and errors just fly up and, you know, it's like
[Speaker 7] [01:00:51] Power Navigator turns out gets really, really unhappy if it can't scan things.
[Speaker 3] [01:00:57] It did, it was very, very upset.
[Speaker 1] [01:01:00] And probably, like, there was probably some bus resetting going on because, like, the s p, you know, thought it should be the master
[Speaker 7] [01:01:07] And the s p is accessing every single address on the squared c bus, And so that may or may not have caused things that are undefined in power navigator land to go bonkers. It was bad. Yeah.
[Speaker 1] [01:01:19] It was not great. And so, like, at this point, we're like, oh, we probably killed the processor. You know, lot lots of things.
[Speaker 7] [01:01:25] Oh, and at this point, the think one of the rail set was reporting out at like 80 amps on the Right. S o d rail.
[Speaker 1] [01:01:32] It shouldn't. Yeah. Oh, this is one of the DRAM controllers.
[Speaker 7] [01:01:35] Oh, the d yeah. Well, the Yeah, man. That one.
[Speaker 3] [01:01:38] Yeah. It's not it's not it doesn't take it. It doesn't try to use
[Speaker 7] [01:01:41] Oh, yeah. That's the 1 d controller with no dims on that side. Yep. That's it.
[Speaker 1] [01:01:44] Yeah. I think you know, and I think Keith's telling us, like, what the data sheet spec is, and it's, like, spec to pull, like, 20 amps or something. And, you know, we're seeing 84, you know, in the diagnostics, and it's like, oh, this is really not great.
[Speaker 3] [01:01:57] This is bad. This is bad. So I so just like a quick aside though, because this is actually an interesting artifact of the kind of new way of working with everyone remote. We recorded every one of this kind of, like, these rolling out of the to the pad of s p 3, we recorded. And it was actually really helpful to go back and replay just rewatch what we did and be able to see exactly what we did when.
[Speaker 1] [01:02:22] Yeah. Yeah. And you can get time correlation there too. Right? So it's like you can see when I hit enter and, you know, like, within the next, like, quarter second, everything went bad.
[Speaker 1] [01:02:32] Right?
[Speaker 3] [01:02:34] It was bad. Anyway, you could see
[Speaker 4] [01:02:36] rewatch that moment again and again. Hey.
[Speaker 3] [01:02:39] Try this.
[Speaker 4] [01:02:40] Hey, try this.
[Speaker 1] [01:02:41] I am happy to report that that processor is actually fine. So Which is amazing.
[Speaker 3] [01:02:47] Yeah. We thought we we we thought we had killed the processor. Yeah.
[Speaker 7] [01:02:50] And Super convinced.
[Speaker 1] [01:02:52] And certainly, that thing had experienced some abuse. I mean, you know, that's the first one. And so, like, some of the sequencing wasn't perfect and, you know, mistakes were made all along the way, but that that guy does seem fine. So So so what did you guys actually do when like,
[Speaker 6] [01:03:07] what did you guys actually do when you scanned it? Was that, like, set all voltage rails to minimum or turn them off?
[Speaker 8] [01:03:13] Or
[Speaker 3] [01:03:13] No. No. No. We did not know which when no. No.
[Speaker 3] [01:03:16] We were when we were scanning it, the and, honestly, like, it's actually still a little bit unclear why. What is more likely, honestly, is that we were initiating bus transactions at the same time the power navigator was initiating bus transactions, and it was just getting back nonsense because it was seen it was seeing our traffic and wasn't handling it very well. I mean, I squared c is definitely not a multi master bus. Right? So it is they are,
[Speaker 1] [01:03:41] it was same time. Yeah.
[Speaker 3] [01:03:42] Yeah. Definitely not the same time. Exactly.
[Speaker 7] [01:03:44] Well, in Power Navigator, when it doesn't get, like, responses, it starts reinitiating the power supplies. And it'll start reloading their entire config over I squared and trying to restart them again because if it's lost synchronization, I think it calls it. And so at that point, you're, like, trying to burst traffic across I squared c while this the SP is trying to scan things, and the god knows what's happening on the power controllers. But the power navigator likes reinitializing everything because it assumes it's on a dev board or something, and it can do that.
[Speaker 6] [01:04:20] As all good dev board software does.
[Speaker 7] [01:04:22] Yeah.
[Speaker 3] [01:04:22] Yeah. Right. Right. Exactly.
[Speaker 6] [01:04:24] And, of course, this is running, you know, some Windows 95 looking all
[Speaker 3] [01:04:28] the way Yeah. Yeah. Take I mean, that's
[Speaker 7] [01:04:31] figure out how to talk to something on I squared. Yes.
[Speaker 6] [01:04:35] That's that's the renaissance one.
[Speaker 7] [01:04:36] Yeah. But Yeah. To its credit, it has some really nice features that we are trying to
[Speaker 3] [01:04:44] it's trying to do it.
[Speaker 1] [01:04:45] In this in the grand scheme of, like, vendor software.
[Speaker 7] [01:04:49] It's pretty good.
[Speaker 1] [01:04:49] That one's that one's actually pretty nice. It looks decent and it is sort of works. I mean, there's certainly some other vendor software we have
[Speaker 3] [01:04:59] said what it is.
[Speaker 1] [01:05:00] Yeah. It doesn't work.
[Speaker 7] [01:05:01] Every vendor's PLL software, like, to interface to their PLLs, is just a complete shit show.
[Speaker 6] [01:05:08] Oh, come on. ADI is not that bad.
[Speaker 7] [01:05:10] ADI, TI, they're all awful. Like, even if you have good like, TI power interface stuff, their fusion interface is not too bad at all. But, like, their PLL stuff is just terrible.
[Speaker 3] [01:05:21] Well, and we are trying to load the e prom in the clock generator, and we are hitting, like, what it, and it's like it's like unrecognized e prom type other. And I'm like, okay. Obviously, this is a misconfiguration. And then and you guys were all like, no. The software is this bad.
[Speaker 3] [01:05:36] I'm like, it can't be this bad. This is like this doesn't work at all. Is this bad. Yeah.
[Speaker 7] [01:05:41] You haven't been jaded enough.
[Speaker 3] [01:05:42] No. It was, like, a total, like, country mouse moment. We're, like, look, cancel, you idiot. It is this bad. Like, stop overthinking it.
[Speaker 1] [01:05:48] I mean, to be fair, in this specific instance, like, there is a button in that software that does not work. Oh, yeah. Instance, like, there is a button in that software that does not work.
[Speaker 7] [01:05:54] Oh, yeah.
[Speaker 1] [01:05:55] And Yes. But, like, we know, we're looking at it and, like, after you play with it a little bit and don't see any bus wiggles or anything. It's like, oh, well that button just doesn't work, and I guess we're like all of us harder guys are to Stockholm
[Speaker 3] [01:06:08] to, like, like, be that mad about it.
[Speaker 6] [01:06:11] It's a reason. Only 1? Right?
[Speaker 3] [01:06:13] No. That is. That is it. That is. You're right.
[Speaker 3] [01:06:15] But that's basically it. I'm like, where's the indignation? It's like, we're just exhausted, man. Can we just Right? Like, you know,
[Speaker 6] [01:06:21] I fully expect there to be, like, 4 to 5 whole tabs of features that are not implemented.
[Speaker 3] [01:06:26] Yeah. And I think, and I think this actually just does drive to our whole zeitgeist, which is about getting fully documented parts and then being able to program these things without proprietary tools. And doing that and to their credit, the vendors are not unsupportive of this approach. And I one of the things I'd like about Power Navigator is, broadly, it is using PM Bus to communicate, and we can do the things that Eric likes about that tool, we can emulate in humility and hubris, which is pretty neat.
[Speaker 1] [01:06:54] And we are on a lot of it. Right? Yeah.
[Speaker 6] [01:06:57] So PM Bus has always just terrified me insofar as you are letting software control the voltages that can explode your CPU.
[Speaker 3] [01:07:08] Yep. So the interesting.
[Speaker 7] [01:07:10] There are ways of so one of the things on, like, the the the core supplies, let's say, on these processors is you can do voltage margining where you can tweak over PM bus. You can tweak the voltage up and down. But to your point, you can tweak the voltage up to 2 volts and just completely just melt down your processor.
[Speaker 6] [01:07:34] Yeah.
[Speaker 7] [01:07:34] But you can also configure it with a way that won't allow that. So you can't actually touch it over the bus. And so on of the one of the things we're going to maybe eventually get to is being able to load things over I squared with a, you know, an intestinal image such that it won't let you even if you've got, you know, got on that thing with fly wires and a bus pirate or something, you can't over voltage the thing or under voltage it. Now if you get onto the AVS bus and start mocking with that or the, you know, the the the processor bus that tells it what to do, well, then, yeah, all bets are off. But at least from the PM bus side, that's there are ways of preventing that at least.
[Speaker 7] [01:08:17] But, yeah, you're right. It's its curious how, especially because, like, the renaissance parts are slick enough and fancy enough that you can tweak their control loop while they're running. And so you can do some very interesting things if you don't do that right.
[Speaker 6] [01:08:30] Oh, that's not terrifying at all.
[Speaker 3] [01:08:31] Yeah. Yeah. Right. Exactly.
[Speaker 7] [01:08:33] I don't think you turn them off first. The renaissance ones are like, oh, yeah. No problem. I can run that. I can do that as a running change.
[Speaker 3] [01:08:38] Yeah. Hold it here. Hold my beer while I do that.
[Speaker 1] [01:08:41] I will say though, like, I think with the like, our team's approach to software hardware co design, I feel like there's a healthy, concern on in everybody who's interacting with this stuff, to make sure that, like, we don't do dumb things like that. And so that's I mean, you know, I'm sure we'll make some mistakes, but, like, there seems to be, like, a lot of care and thought put into these things to make sure that they come out right. And so that that's been very nice, I think. And the team is all very, you know, aware of, like, the fact that, like, there's something physical also going on. It's not just bits running around in a processor.
[Speaker 3] [01:09:19] Yeah. Definitely. And if for those that are curious, we open sourced Hubris, and Humility last week, actually. So you can actually go look at the software that we're talking about and the software that does, like, PM Bus reporting and so on. And definitely find bugs.
[Speaker 3] [01:09:32] Let us know. Right. But, because it is yeah. It has consequences. If you get it wrong, you can break the thing.
[Speaker 7] [01:09:40] But if you get it right, you have a lot of built-in diagnostics and
[Speaker 3] [01:09:43] That's right.
[Speaker 7] [01:09:44] Parametric that you can get out of it, which is amazing.
[Speaker 3] [01:09:47] If it's really cool. And so alright. So we are now I feel we enter the prolonged period of
[Speaker 7] [01:09:53] Now we're in the
[Speaker 1] [01:09:54] area of despair. Eric living at my house.
[Speaker 3] [01:09:57] Eric living at your house. Valley of despair. Matt, you're asking us Twitter space. See you next week, everybody. The
[Speaker 6] [01:10:07] And here we thought Brian was just running away from me the whole time.
[Speaker 3] [01:10:10] No. Exactly. No. It's like, please don't ask, go bring up. And, you know, because we are, and we're we are double, triple, quadruple checking everything.
[Speaker 3] [01:10:20] We're going through Yeah. I I I feel like there's this moment where because understandably and AMD is being super helpful through all of this. AMD is trying to help us brainstorm it. The only real symptom we have of this thing is it resets after 1 point 2 5 seconds.
[Speaker 7] [01:10:36] Infinite reset loop.
[Speaker 3] [01:10:37] Infinite reset loop.
[Speaker 1] [01:10:39] Yeah. So it, like, it has a fancy handshake sequence. And so we go through all of that. Right? We're all the way up
[Speaker 7] [01:10:45] to And everything looks happy.
[Speaker 3] [01:10:46] Theory Everything's happy. Like,
[Speaker 1] [01:10:48] loading code out of its ROM. Everything seems happy, and it hangs out for a second and a quarter. We never see any spy wiggles, and then it just resets. And it's like reset, hang out, reset, hang out.
[Speaker 7] [01:11:02] And, like,
[Speaker 3] [01:11:02] that's
[Speaker 8] [01:11:03] how
[Speaker 3] [01:11:03] So meanwhile, we're trying to get ours to work. Rick on the other side of the country has an ethanol x that he's trying to get to break in the same way that ours is broken.
[Speaker 2] [01:11:12] What's an ethanol x? Right.
[Speaker 3] [01:11:13] A ethanol x. You
[Speaker 2] [01:11:14] That's ethanol x.
[Speaker 5] [01:11:17] Ethanol x is, a reference system from AMD. So the CPU vendors, when they release a processor, typically make an entire motherboard and, provide that to the OEMs as a this is how we expect you to build it. And this way, you have something to compare to when something doesn't work. You can at least see an example of a working system.
[Speaker 1] [01:11:37] And, I mean, like quick caveat. At this point, Rick's ethanol has already had a significant amount of surgery, because we've,
[Speaker 5] [01:11:46] like, prototype
[Speaker 1] [01:11:47] some things before we cut out, and then we've he's been instrumenting it to get sequencing samples so that we can compare against, you know, our own design?
[Speaker 5] [01:11:57] I have no shame about taking a soldering iron to a very expensive motherboard. So, yeah, there were many experiments where I was just totally willing to remove components and attach wires and do all sorts of things. So my board was in a good shape to use as this candidate for, okay, if we can't figure out why our board isn't working, can I modify my board to look as close, as possible to our board and see if I can get it to fail in the same way?
[Speaker 3] [01:12:28] Which was it being incredibly valuable because, what we discovered is, Rick no. Rick could not get this board to fail no matter what he did. And, actually, it was really important because there would be hypotheses about different signals that we don't have wired up or wired up differently than ethanol. And Rick would be able to validate, like, nope. That doesn't matter because I can hold that low, and it still boots.
[Speaker 3] [01:12:51] I can do this to that.
[Speaker 7] [01:12:52] Despite what your documentation says, this doesn't matter. Right. Right.
[Speaker 1] [01:12:56] I mean, I think we should talk a little bit about k b reset l. Uh-huh.
[Speaker 3] [01:13:00] Oh, absolutely. K b reset l. So, yeah, so explain KB reset l.
[Speaker 1] [01:13:04] So KB reset l is, you know, you know, like something that our company generally hates, right? Because it's this, like, less leftover vestige of, like, a keyboard reset. And so it's like a pin that maybe could make the processor reset. And, you know, today, that's all connected up to actual BMC's and that kind of thing in different designs.
[Speaker 8] [01:13:24] AMD suggested
[Speaker 3] [01:13:24] that, like, you know, on our
[Speaker 1] [01:13:24] like, in the documentation, it's, like, if you're not AMD suggested that, like, you know, on our like, in the documentation, it's, like, if you're not using this, it'll internally pull up high, so float it. And so that's what our design did. We floated it. You know, as we're going through the debugging, that was one of the things they suggested. Like, can you, like, confirm that k b reset hell reset l is high.
[Speaker 1] [01:13:44] And so we're like, Oh, sure, no problem. And so then, you know, as we look at our board, though, we realize since it's floating, like the via from the socket to the back of the board has been stripped off. And so the only like, this connection like, I and I don't know how people are familiar with, the s p 3 sockets, but s p 3 sockets have, like, little spring pins in them, and they reach up and touch little, like, gold dots on the bottom of a processor. And those little spring pins are kind of, like, little tiny wires, and they're wired down to balls that are soldered onto the top of the board. And then, you know, for signals that need to go elsewhere on the board, we have a via right next to that.
[Speaker 1] [01:14:24] And, you know, the signals fan out on internal layers. However, for signals that, like KB reset L that doesn't go anywhere. Oftentimes the via get removed as part of the, you know, CAD and layout process. So on this board, we have the spring pin soldered down to a ball on the top of the board that we can't really get to, and then it doesn't come out to a via in the back. And so, you know, Eric and I are sitting there trying to figure out how we might, you know, figure this out.
[Speaker 1] [01:14:55] And Eric's like, I think I can solder onto this thing. And so we have got pictures of this. It's its pretty impressive work on Eric's part, but he, he stuck a, you know, 30 gauge or, 40 gauge magnet wire down, and we tacked underneath the bottom side of the spring pin under the socket and soldered onto that, and so we could wire that pin out and look at it. And then we could tie it high or low.
[Speaker 3] [01:15:20] And you really need the dime for scale. Like, if you look at it without a dime, you're you're like, oh, yeah. I don't know what that up looks. Is that small? And then you look at, like, what is that massive star there?
[Speaker 3] [01:15:33] It's like, oh, no. That's a dime. You're like, oh, god.
[Speaker 1] [01:15:35] Yeah. I mean, the magnet wire is, thicker than, like, human hair. Right? But, it's a lot thinner than even a 30 gauge rework wire. So yeah.
[Speaker 1] [01:15:46] And is magnet wire like
[Speaker 2] [01:15:48] a standard tool in your tool belt? Like, did you have that hanging around?
[Speaker 3] [01:15:50] Yeah. Yeah.
[Speaker 6] [01:15:51] Absolutely. EV everybody's got a spool of this stuff.
[Speaker 1] [01:15:54] Yeah. And it's nice for this kind of stuff or if you need to tack to traces, like, we use a lot of 30 gauge for, like, most of the rework, but, like, for really nasty things, the magnet wire is really awesome for that. So
[Speaker 3] [01:16:09] And we'll, we'll tweet out a photo of that because that's pretty but pretty mesmerizing. And so this is, and I'm thinking, like, this is okay. I get it. Gods, I hope you've enjoyed your little playtime. You have punished us by making k b reset l, the fact that it's floating, the fact that we've got a pin in this microprocessor that's through the keyboard, which obviously this thing will never have.
[Speaker 3] [01:16:33] It's like, okay. We get it. Joke's over. Can we please boot now? Now we
[Speaker 1] [01:16:37] can boot. Nope. Nope. Nope. Nope.
[Speaker 1] [01:16:39] That was not it.
[Speaker 3] [01:16:40] That was not it.
[Speaker 5] [01:16:41] Yeah. And meanwhile, you know, we're running all these other experiments on in my, my board, I've managed to remove something like 40 components from the ethanol x. And I just have this, like, growing pile of resistors that and my board is still booting. Like, that's the amazing part. It's like it's actually still working fine.
[Speaker 3] [01:17:01] Do anything right. We can't even break a machine correctly. It's like, Jesus Christ.
[Speaker 7] [01:17:05] You have ever seen Beverly Hills cop? I think it's Beverly Hills cop 3 where Eddie Murphy is driving this car out of a chop shop and parts are just falling off of it. He's just
[Speaker 3] [01:17:13] That's right. Exactly. I just
[Speaker 7] [01:17:14] said that's Rick's ethanol.
[Speaker 3] [01:17:16] That's Rick's ethanol. And parts falling off of it. So I I I have to say if I can just take it now quick aside to, read an excerpt from this book I read on Antioch because I boy, did I feel this. When things wouldn't work, frustrated workers referred to the machine as the maniac. Another of the engineers remember joking that if they gave their drawings to the Germans, they would set back the war effort 10 years.
[Speaker 3] [01:17:42] We were young and deeply involved. We felt like the whole war program depended on us, Goldstein said. There's a real sense that we are doing something very extraordinary, which I felt like this thing is the maniac. Like, it's like, what is going on? And I also feel like we've got the total confidence that we're going to resolve it, but at the same time, total confusion about what's happening.
[Speaker 3] [01:18:01] Yeah. And an AMD is being super helpful with this. I mean, AMD is, like, making all sorts of I mean, they are, like, boy. We have not really seen anything like this. And they're making a lot of suggestions, and we're acting on all of them.
[Speaker 3] [01:18:13] This is where I think, Nathaniel, writing everything down was a real win. Yeah.
[Speaker 7] [01:18:16] We at this point, we have 136 pages of notes.
[Speaker 5] [01:18:20] Right. Yeah. And so This is also where you start to question reality, where you're like, okay. So clearly, following the documentation didn't work. Trying to break our board or break our reference design didn't work.
[Speaker 5] [01:18:36] We're not getting any answers from the vendors because, you know, they're working hard on it, but we just nobody knows what is wrong with this thing. And
[Speaker 8] [01:18:45] running out of options
[Speaker 5] [01:18:45] as to what that could possibly be wrong? And this is where we run into things like, yes. I have been on a Brine up where it turned out that somebody's multimeter was not, had not been calibrated and was in fact reading wrong.
[Speaker 8] [01:19:06] Fuck.
[Speaker 5] [01:19:07] And that takes a really long time to figure out, you know, things like that. And just asking all these mundane questions of okay. Now we just have to really check our what are we missing?
[Speaker 3] [01:19:19] We're missing something.
[Speaker 1] [01:19:20] And so Eric and I live, like, 20 minutes apart. And so every day, Eric is showing up with a trunk full of more stuff. And so it's like, you know, one day, it's the SALE. Another day, it's the ethanol x, another day it's like, you know, a Keith 2 different DMMs. There.
[Speaker 1] [01:19:35] Yeah. 2 scopes and, you know, all kinds of stuff, you know, just to try and, like, you know, 0 in on whatever is going on here. And we've we've been instrumenting we've been instrumenting our part. Of course, course, like, at some point in this process, like, we drop a probe on a powered board and it toasts the board. And so then it's, like,
[Speaker 3] [01:19:55] it's, like, it's like Right. Right. Like, this is That
[Speaker 5] [01:19:57] was a pretty
[Speaker 7] [01:19:58] good day.
[Speaker 1] [01:19:59] That was a Friday.
[Speaker 3] [01:20:00] That was a bad day.
[Speaker 1] [01:20:01] Friday at, like, 8:30 in the morning. And it's, like,
[Speaker 3] [01:20:05] oh. And we're going into the holiday week the next week, so we had a tiny window. Yeah. That was, like,
[Speaker 1] [01:20:12] all day. Like, well, okay. I mean, that board had, you know, like, days of rework on it. And so it's, like, well, you know, because we have a bunch of stuff that we don't actually ever want to see again, but it's, like, brought out right now, so we can get the scope trap captures that we need for sequencing. And so we, you know, we ship that one back to our vendor to have, BGA part replaced that that blew up.
[Speaker 1] [01:20:35] And, and so we start, you know, start round 2 on another board. And, you know, I mean, like, at a certain level, you're like, well, maybe there was just something wrong
[Speaker 3] [01:20:45] with it. Right. It'd be it is had a spell cast on it. That that makes sense.
[Speaker 1] [01:20:50] But at the other side, you're like, now I got a check everything else again because I have to, you know, get back to that same place. And so we get back to that same place, you know, over the weekend into Monday.
[Speaker 3] [01:21:01] Well and thing that's also worth mentioning on some of these theories and, Rick, I'm I'm sure you and Eric felt the same way. On some of these theories, you'd be like, okay. Well, we're going to try it with this thing set the other way. But fuck it. This is it.
[Speaker 3] [01:21:12] It's going to be very distressing because it's going to mean that, you know, this signal that's clearly documented to float or this signal that's clearly documented to be one way, It magically needs to be the other way. It was almost like, I want this thing to boot, but not at the cost of my sanity, I don't think. But then I was like, you know what? I'll give it out by sanity. Fine.
[Speaker 3] [01:21:30] Right. Which is
[Speaker 5] [01:21:31] Well, there's also there's always how much is it how painful is it going to be to fix this if we're right? Because at this point, you know, it's a significant leak board. It's got all these, you know, all this work that we're trying to do on it. If it turned out that we made a mistake on something that was an inner layer, like that starts to get into a very, very difficult to solve problem.
[Speaker 3] [01:21:56] Well, and we
[Speaker 1] [01:22:05] afternoon, we Eric and I had found that, you know, as we as the processor loaded, we could tell that was it.
[Speaker 3] [01:22:11] I thought that was a
[Speaker 1] [01:22:12] voltage fold back, and it was like, this rail has fairly tight specs on it. We're not meeting it. You go look at the layout and the layout kinda got botched, and it was like, okay.
[Speaker 3] [01:22:21] That's it.
[Speaker 1] [01:22:21] You know, this must be it. Right?
[Speaker 3] [01:22:23] That's got to be it.
[Speaker 7] [01:22:24] We're getting
[Speaker 1] [01:22:24] under voltage
[Speaker 7] [01:22:25] and so we're dropping everybody. A 100 millivolts on a freaking 0.9 volt rail.
[Speaker 1] [01:22:30] Right. And so but so, you know, we chatted with people, and it was like, okay. This is it. And so, like, a lot of good ideas, you know, like, we could steal voltage from some other supply on here. And Eric's like, no.
[Speaker 1] [01:22:43] I think I can just copper tape a new plane onto the bottom and fix it. And so he That was amazing, by the way. Yeah.
[Speaker 3] [01:22:51] I mean, as a software guy seeing that,
[Speaker 2] [01:22:53] I'm like, really? That's that's what we're doing now? Okay.
[Speaker 3] [01:22:55] No. No. It was amazing because also, I felt like I was I felt like this fits all the evidence that we've got. This must be it. And, Steve, you remember when you had us talking at the office, I'm like, the good news is this is it.
[Speaker 3] [01:23:08] The bad news is it's going to be it's its not going to be reworkable. As it turns out, like, both of us were wrong. It's like, it is reworkable, and it's not it.
[Speaker 1] [01:23:16] And, I mean, to be fair, like, it only requires one layer of copper tape. Like, we didn't have to put Tapton on and add a second layer or anything, you know? So, like, in the grand scheme of rework, the SP pins were probably worse rework than this. But so Eric lays down a new copper plane and, you know, we try it again. And, of course, it's the now the supply is rock solid and the board still reset loops.
[Speaker 3] [01:23:42] And, actually, it should be said that, like, the SALE, like, report card, Adam, that you're asking about earlier, we have gone from, like, you know, like, a's and b's to, like, a pluses. I mean, we are now, like, the margin on this thing is now to the point where Andy's like, probably, I've never actually seen power this good. This is amazingly good power. Like, the margin
[Speaker 8] [01:24:01] there is incredible.
[Speaker 3] [01:24:01] Great. Thanks for nothing. Right. Right. Very impressive.
[Speaker 3] [01:24:04] It's like, okay. Can you boot now? Like, please? Please? Please?
[Speaker 3] [01:24:08] Please? And then in and then, I but, Erica, you'll walk you through the the the walk you up to your big breakthrough. But it was in part of those conversations with AMD where they're just, like, just throwing a bunch of stuff out about, you know, check this, check this, check this. And they they they mentioned the SPI 2 traffic. And looking at just make like, go back and kind of, and we'd already looked at that stuff, and it hadn't been an issue.
[Speaker 3] [01:24:34] Well, and s p and
[Speaker 7] [01:24:35] Power Spy is responding to the commands from the process.
[Speaker 1] [01:24:38] And s p I 2 is required to pass SALE. And so, like, it's clearly working.
[Speaker 3] [01:24:44] It's clearly working. And so it's like, we're not like, okay. But we know the SBI 2 is working. And so, Eric, maybe you can walk us through your thought process based on that. I mean, because that clearly, like, got you just digging deeper on that.
[Speaker 3] [01:24:54] Yeah. I mean, we were desperate.
[Speaker 7] [01:24:56] Yeah. That's very desperate. But, like, one of the one of the AMD folks just casually mentions, like, oh, yeah. I saw, you know, some support ticket or somebody mentioned that, like, oh, if you don't see a VOTE in the right amount of time, that could, you know, that could cause a reset loop. And I'm like, the hell is VOTE?
[Speaker 7] [01:25:13] And so I go look at the s v I two spec, and I look at VOTE as a special it's a special packet that gets sent by the power controller when, like, let's say, a processor chain requests a voltage change. So, like, let's say the, you know, the load, you know, the app load on the processor has really gone up, and it really wants to, you know, get tons of power really quick, it'll tell the voltage regulator, hey. I want, you know, instead of 1.0 volts, I want 1.1 volts because I really
[Speaker 3] [01:25:40] And this is a and VOTE is v in on the fly. Right? I think it's the Yeah. It's what it does. It's the
[Speaker 7] [01:25:47] fly and then the c is complete. Right. So it's an on the fly voltage change request from the processor. Could be up, could be down, whatever.
[Speaker 3] [01:25:57] And that is sent successfully.
[Speaker 7] [01:25:59] Yep. That's well, no. It's so And
[Speaker 8] [01:26:01] The process that says
[Speaker 1] [01:26:01] The the the command is
[Speaker 7] [01:26:04] Go to 1.1 volts. I see the slew up to 1.1 volts. It's well controlled. There's no overshoot. There's no ringing.
[Speaker 7] [01:26:09] There's no nothing. It looks beautiful. And then I'm like, okay, well, what the hell? Like, is there anything in this tool that the SCALE runs on that measures something in here. It's like, oh, okay.
[Speaker 7] [01:26:21] I see 2 measurements. Whatever. I'm like, you know, what the hell does this packet even say? And so I'd zoom in because it has a little it even has a utility to capture s v I 2 packets, like, with that transition. You can tell it to transition.
[Speaker 7] [01:26:34] It'll capture the traffic right after it. And I realized that it doesn't seem to be sending a VOTE packet. It just sends normal like, there 's's 2 single direct it's like a spy bus at, like, 3 megahertz or something. And so there's a data bus that comes from the processor to the controller, and then there's a telemetry bus that goes from the controller to the processor where the processor is told, hey. Your rail 1 is at, you know, 1.1 volts and your current is, you know, 38.7 amps and temperature is blah blah blah, and the processor uses that for something.
[Speaker 7] [01:27:10] And I realized that it's just sending normal, like, telemetry back. It's not sending the VOTE packet when it's supposed to be.
[Speaker 3] [01:27:16] It's not sending the complete packet.
[Speaker 7] [01:27:18] It's not
[Speaker 3] [01:27:18] saying I it's not it's not responding with I've done this.
[Speaker 7] [01:27:21] Yeah. It's not responding with the, hey. I finished even though it finished. And it was responding and sending telemetry and otherwise behaving normally.
[Speaker 3] [01:27:30] Literally half the protocol. It is implementing the half of the protocol that changes the voltage Yeah. But not the half the protocol that said I did it.
[Speaker 7] [01:27:37] Yes. And so I sent to an e for Genesis, FAE who is awesome and responds very quickly with a yeah. So if you try this different software and you know, there's a little button that should be pressed in the GUI. And it's like, okay. I push that button.
[Speaker 7] [01:28:02] Alright. Fine. Yeah. I'll get this newer version and install it. And then, ding, there's the VOTE complete.
[Speaker 7] [01:28:10] I'm like, what?
[Speaker 3] [01:28:12] So in the end, there was a there was a arguably, I mean, our from our perspective, a bug and actually maybe this perspective a bug too. In that the SALE was not was actually looking at the telemetry packets, but didn't actually note whether the complete packet had been sent or not.
[Speaker 7] [01:28:33] Even though it easily has
[Speaker 3] [01:28:34] the same idea
[Speaker 7] [01:28:35] looking at that and really should be Should
[Speaker 3] [01:28:37] be checking that.
[Speaker 1] [01:28:40] And a bug in the power tools that when you turn this feature on, it only turned half of it on.
[Speaker 3] [01:28:46] It turned half of it on. We set that bit to 0.5. So
[Speaker 6] [01:28:51] so in the true spirit of oxide, this turns out to be a firmware bug.
[Speaker 3] [01:28:57] Yeah.
[Speaker 7] [01:28:57] I hate to I hate
[Speaker 8] [01:28:59] to be
[Speaker 3] [01:28:59] a firmware bug. It is. I kinda hate to say I hate to be so on brand, but, yes, it is. Yeah. And I mean but to be clear, like, everybody honestly in this, this is one of these things that, like, I the all of these folks were incredibly, incredibly helpful in helping us get this problem resolved, and we're really grateful to Renaissance and AMD.
[Speaker 3] [01:29:16] And then importantly, like, we get all of this, they are these FAE at Renaissance is just terrific and got us everything that we needed. So I was worried that, like, we're going to have to, like, get a new part. Right.
[Speaker 7] [01:29:29] Or we're going to have to, like, navigate some huge bureaucracy within Renaissance to find an answer to why this is happening. And they won't know. I want to be like, oh, god. Now what? It's like we should've used this other part.
[Speaker 7] [01:29:39] This wasn't the part they use in the reference design.
[Speaker 3] [01:29:43] None of that happened for the Oh, no.
[Speaker 8] [01:29:45] Here's the thing.
[Speaker 7] [01:29:45] Yeah. And No worries.
[Speaker 1] [01:29:47] We get the new things programmed and boom, spy wiggles.
[Speaker 3] [01:29:52] We get Spy Wiggles. And then we get
[Speaker 1] [01:29:55] We noticed that the Spy Wiggles' pins aren't quite right.
[Speaker 3] [01:29:59] And we have
[Speaker 1] [01:30:00] another Right. Another little swap. But we
[Speaker 3] [01:30:05] have Yeah. I do. It's kinda like it's kinda like the action movie that's like you think I get like the villain is dead. The movie's over. It's like, oh, no.
[Speaker 3] [01:30:11] Nope. Not quite over. We have to do we have to do one more little rework. Monty Python. Noted.
[Speaker 3] [01:30:17] Exactly.
[Speaker 7] [01:30:18] Just a second.
[Speaker 1] [01:30:18] That was real clear. Like, we had you know, that board was ready with Heather's instrumented on the spy and everything. And so as soon as we saw spy wiggles, it was, like, super clear that, like, you know, d zero and d one are swapped.
[Speaker 7] [01:30:31] My god. And Damn it. We swapped s I r
[Speaker 3] [01:30:33] s o. Oops.
[Speaker 1] [01:30:35] And so, you know, a little trace cut and a little jumper and
[Speaker 7] [01:30:40] A magnet wire layer and
[Speaker 3] [01:30:42] So And then we,
[Speaker 1] [01:30:44] the end of that day. I mean, so, like Yes. Because I got that home and had to do I had to do some UART rework or, like, so we didn't bring the UART. We need to bring UARTs out to a header so we could see them and some other stuff. And so that was that and then the next day, we had a demo.
[Speaker 3] [01:31:03] We had a demo. And it well, we had a demo that was, talking about the eye of Sauron whipping to me where so the first thing that's going to happen are these spy wiggles where the PSP, which is this bot this proprietary, security core inside the AMD part, it downloads its firmware, and then it's gonna start booting the processor. And then the first thing we're going to see out of this thing is it attempting to train DRAM by asking where the DRAM is. And this is where it actually is going to hit our code. And Daniel gets everyone out.
[Speaker 3] [01:31:39] Let's get a demo. And then
[Speaker 1] [01:31:41] And so, I mean, so we lay so, I mean and to be fair, like, I knew we were going to land there because I had gotten there that night Yeah. The night before. But it was, like, this is good because, like, we have characters coming out the u r from the s p 3. In our design, our service processor sits as a proxy for the SPD EPROM's that are on all the Simms because we want access to those in our control plane. And so that's the code that Brian's talking about where the AMD processor is going to go out and talk to our service processor and think he's talking to Simms, and we proxy all of that.
[Speaker 1] [01:32:15] And so it just it kinda zipped through and said none of the dims are present.
[Speaker 3] [01:32:21] Which, of course, like, could be lots of different things. Fortunately, this is where I think the tooling and all the the the stuff we've done, we were very quickly able to determine that I had fucked up. And I had a cut-and-paste error from I actually was looking at my I don't like, I'm looking at my own code being like, how is this fucked up? And Rick has realized, like, you cut pasted it from, again, what, not from CentOS.
[Speaker 1] [01:32:39] It's a pin it was just a pin out problem. It wasn't even a logic problem.
[Speaker 3] [01:32:42] No. It was a lot of problems. So there's a pin problem, super easy fix. And then we came all the way up, except then we ended up with, like, Keith had left you an image that had a very traumatic hello world message. But now we had a Windows terminal problem, such you could not give you the actual, like, glorified image properly.
[Speaker 3] [01:33:00] And now we're into, like, new unsolved problems on how to get Putty configured correctly with respect to line frames.
[Speaker 1] [01:33:05] Yeah. So there yeah. We had the know, you need the implicit, carriage to turn online feed or whatever. And, so we got that done and, you know, kinda cycled the whole thing over and get all the way up, and we see Hello World and Oxide's, you know, NATO bootloader that Keith's been working on.
[Speaker 3] [01:33:22] And it was glorious. So we got all the way
[Speaker 1] [01:33:24] through running Yep. Yeah. That's running our x86 code. Right? Which is kinda the important part of that.
[Speaker 1] [01:33:30] Because everything up until that point is kind of running AMD's blob of stuff that does all the DRAM. Like, we don't get to control that. And so then, ta the, we're running our code.
[Speaker 3] [01:33:41] And it means the dims trained and everything else. So we well, always long way to go, but, definitely, wind at the back. And, you know, Steve, you had said that you had had a line relatively early in this. Like, going to have a good story around the campfire when all this is done. I think you've just been at the campfire.
[Speaker 5] [01:33:59] Well, Brian, you're you're getting you're forgetting that last little bit of the story. So we get to this wonderful point. You can see
[Speaker 8] [01:34:05] the output.
[Speaker 5] [01:34:06] It shows that we booted,
[Speaker 7] [01:34:08] and then you can't hide anything.
[Speaker 3] [01:34:09] The last part of the story. Oh my god. How can I forget this? Yes. Good.
[Speaker 1] [01:34:13] I will never forget this.
[Speaker 3] [01:34:15] Right. And so and because, like, we are who we are, everyone's mind is immediately running to the absolute worst case scenario. So Right. The key is like, you know, we are hitting you know, it's a thumb trip or, you know, we're we like, the CPU is shutting down or, you know, we're stock. Yeah.
[Speaker 3] [01:34:32] Stock.
[Speaker 1] [01:34:33] So because so we get a get a terminal, basically, right, with key stuff. And so I should be able to issue characters and no characters occur. And so, you know, it's like, okay, we kinda shut the demo down at this point, and I'm like, look, we'll go figure out what's wrong with the serial port, you know, and they're, you know, they're only 3 or 4 wires here. It can't be that hard. Right?
[Speaker 1] [01:34:54] And, you know, so looking into it, and it's like, it's the pin that our TDI dongle should, you know, should set low to or, sorry, the pin, he should see the processor have set it low so that he can issue characters. It's high. It's floating high and we can't issue characters. And so, you know, we go through and, you know, if you've ever dug through TDI data sheets, you know, they're TX and RX and like, you know, every I feel like every hardware and embedded guy in the world has had to deal with like who's TX and who's Rx and like which direction does all of these things go through all of that. Everything's fine.
[Speaker 1] [01:35:37] So I spent, you know, the rest of the afternoon kinda chasing that. And I get to a spot where, like, I finally probe the board in such a way that I realized like, oh, my dongle isn't working. You My FCI chip is not doing what I'm expecting. And, you know, at that point, I'm kind of like, okay, I'm putting the computer down. I'm going away.
[Speaker 1] [01:35:56] Like, this has been too much today.
[Speaker 3] [01:35:59] Which does I have to say, Nathaniel, you've got I mean, you have such a high threshold for pain. When Nathaniel had the message in the channel be like, I am walking away from the computer for the day, you're like, okay. It's, it's grim over there. Now
[Speaker 1] [01:36:12] the sad part is, of course, I go upstairs to watch TV or whatever, and all I can think about
[Speaker 3] [01:36:17] is why is that just working. The computer is like, you'll be back.
[Speaker 1] [01:36:22] So I come back down, and I'm like, I'm gonna, like and, you know, I had tried, like, 2 other TDI, you know, mini modules and, like, I was getting different behaviour on each one, which is never inspiring confidence both in like how you're testing it and like the product itself. And, but, you know, like, and it's like, well, it's got to be something I'm doing. So I come back down and, you know, I'm looking at this pin, and it's an input, and it's kinda floating high. And so I'm like, I'm just going to ground the pin with a little DuPont wire. And so I grab one of the DuPont wires, and I just, like connect that pin to ground.
[Speaker 1] [01:37:00] And I measure it with my DMM. And one side is ground and the other side is floating. And I'm like, wait a minute. Like, this I mean, this is not, like, electrically possible. Right.
[Speaker 1] [01:37:15] So so so then I pulled the DuPont wire off, and I owe them it out, and it's an open circuit.
[Speaker 3] [01:37:22] Womb. Womb. Womb. Womb. Womb.
[Speaker 3] [01:37:24] And it's like right.
[Speaker 1] [01:37:25] And so then I'm like, okay. So that explains, you know, part of what's going on here. But I'm like, but I have this other DuPont wire over here that, and so I own that one out, and it is also an open circuit.
[Speaker 3] [01:37:37] And you could so DuPont wired, we're talking these are like the the jumper wire that you have in, like, a breadboard, a maker breadboard. This is like stuff that can't fail.
[Speaker 1] [01:37:50] Well, mostly. I mean, it's so of the 7 DuPont wires that I had involved in this setup, 2 of them were open circuits, and 2 of them were open circuits, and, like, I'm like, they were broken or something because or maybe, like, heavily oxidized because, like, I pulled the plastic off to look, and it's, like, the copper is still crimped in the crimp and they're open. And so that it happened to be that was the pin, you know, the RTS CTS pin was an open circuit.
[Speaker 3] [01:38:22] And so as soon as I
[Speaker 1] [01:38:23] got an actual wire there, like
[Speaker 3] [01:38:27] I know we said that talk about a VoIP whizzing over the year. It so that only because that that implied that flow control is constantly on, we couldn't TX. If that had been on another pin, it wouldn't, we wouldn't have seen anything.
[Speaker 1] [01:38:41] Yeah. We right. We would have ended up back into, like, Sale land putting some
[Speaker 3] [01:38:46] Yes.
[Speaker 1] [01:38:46] On things.
[Speaker 3] [01:38:47] Yeah. Right. Exactly.
[Speaker 7] [01:38:49] We would have figured it out.
[Speaker 3] [01:38:50] We would have figured it out.
[Speaker 1] [01:38:51] Figured that out pretty quick because, like, we would have seen it wiggle. But it, like, it depends because it depends on where you put the salvia. Because if you put it
[Speaker 8] [01:38:58] at the
[Speaker 1] [01:38:59] end of your broken wire, you know, you're not going to see what you expect.
[Speaker 3] [01:39:04] So, yes, Rick. Thank you very much for remembering me. The end of that is just I mean, a broken DuPont wire at the end. So it's like busted firmware, broken DuPont wire, can't be reset l. Are gods, are you happy yet?
[Speaker 3] [01:39:16] Are the gods content at this point? Can we Jesus Christ?
[Speaker 5] [01:39:19] Well, like I said, we had already gotten to the point where we're questioning reality. We just we did it a little too early.
[Speaker 3] [01:39:25] It was
[Speaker 1] [01:39:25] So I can confirm that all the entire set of DuPont wires has been scrapped. So we're not gonna mess with those anymore.
[Speaker 3] [01:39:34] There you go. Done with those. Well, it was a and, Adam, I'm sorry. I know you've got you've
[Speaker 8] [01:39:40] got Josh
[Speaker 2] [01:39:41] on this. This has been the killer. This has been killer.
[Speaker 3] [01:39:44] But I feel like this is a story that had to be told. And, yeah, I feel like also these are the stories that are frequently not told, honestly, because they kind of are they're told to kind of, you know, among, you know, engineers at a company or what have you, but they're not often told publicly. But, this one was obviously well, also, Matt, you've Matt had been asking every week, so it's like we had to your know? Gotta
[Speaker 2] [01:40:05] tell him something.
[Speaker 3] [01:40:06] I have to tell him something. Exactly. That's right. So, but if it was this is a hell of an odyssey. On the one hand, we were confident the entire time.
[Speaker 3] [01:40:15] On the other hand, we were also terrified the entire time. Or I was terrified. Steve, sorry. Maybe you don't want to hear this right now. The, but it is because it is I mean, the problem what makes this kind of work exciting and terrifying is if you don't get through this, you don't have anything.
[Speaker 3] [01:40:34] Like, I remember us joking about, like, hey. How much could we run on the service processor anyway? Maybe customers want to run their workloads there. Maybe they don't want a CPU. But it's We'll
[Speaker 1] [01:40:45] call it our ARM data centre.
[Speaker 3] [01:40:46] That's our ARM data centre. And this is the challenge of this kinda, but it also makes it super exciting and so validating when we actually get all the way through it. So it was it was a hell of a ride. And I'm sure there are more rides in our future, but that one, I think, is always going to be special. Alright.
[Speaker 3] [01:41:07] And, Daniel, I saw that you and I don't know if you or anyone else want to chime in here if you want to be mindful of Adam's time and, and also especially Nathaniel and Eric in central time. I know it's late for you both. But
[Speaker 1] [01:41:18] Oh, this has been fun.
[Speaker 3] [01:41:19] This has been it is it's its been fun because it booted. That's why it's been fun.
[Speaker 2] [01:41:25] Yeah. It was. Yeah. It was a lot
[Speaker 1] [01:41:26] less fun last week.
[Speaker 3] [01:41:27] A lot less fun last week. And I assume everyone knew that the ending must have been good because we would not be so chipper about talking what a disaster everything was. But it it definitely has been fun to, to relay this. And, yeah, onto the next. Onto ETV.
[Speaker 3] [01:41:50] Alright. Adam, anything I ray radar
[Speaker 2] [01:41:55] killer. No. Nathaniel, Eric, this has been awesome. Rick, thank you for this. You know, I, for folks outside of oxide, even inside oxide, I get a couple of these pieces often without the explanation to really appreciate it.
[Speaker 2] [01:42:09] So this has been awesome. And, for future generations of oxide employees like this, this recording is going to be a great thing to put in the time capsule.
[Speaker 3] [01:42:19] Absolutely. Alright. Thanks everyone. See you next week. Thanks.
[Speaker 3] [01:42:23] Yep.
[Speaker 1] [01:42:24] Thank you.