[0.00 --> 2.90]  We've got a good crew here, so let's go ahead and get going.
[5.06 --> 13.38]  The origin of this, Arden, I thought you might kick us off because I think the origin of this is your tweet, which I loved.
[13.38 --> 19.72]  A measurement two years in the making, which really gets to the odyssey we've gone on here.
[20.54 --> 26.94]  Do you want to describe at the outset what we've actually built and what some of the challenges were?
[26.94 --> 36.12]  So in the beginning, what did we build?
[36.12 --> 38.84]  Well, so super quick.
[39.26 --> 46.88]  What I showed in the tweet was a measurement of the backplane cabling that we're using between our switch and our compute sled.
[46.88 --> 59.74]  And in particular, what it shows is a TDR measuring the full channel of the cable connected to two circuit boards through the connectors.
[59.74 --> 67.22]  We're using probes that are touching the printed circuit boards on like both printed circuit boards each on one side.
[67.22 --> 69.98]  So you can measure through the entire stack, like everything.
[69.98 --> 83.22]  And what that lets us do is it will let us extract some performance data about how well a signal will travel through the PCB, through the connectors, into the cables, through the cables, out the connectors, and then into the PCB.
[83.22 --> 89.58]  And then ultimately through the pads and then where the chips then would be that then are connected to each other.
[89.58 --> 92.40]  So that's pretty exciting.
[92.54 --> 98.00]  So I'm going to apologize in advance for starting with a bunch of questions.
[98.34 --> 99.66]  You mentioned a TDR measurement.
[99.78 --> 101.40]  You want to describe what that is briefly?
[103.08 --> 105.80]  How about Eric describes a TDR measurement?
[106.30 --> 106.50]  Sure.
[107.16 --> 109.04]  I'll basically back away from you.
[109.04 --> 109.64]  Exactly.
[110.88 --> 111.50]  Back for names.
[112.34 --> 115.64]  There's two ways of measuring a channel.
[115.64 --> 124.68]  A channel is basically just defined as a set of wires that goes from some source to some destination in a high-speed link in our case.
[124.68 --> 137.72]  So the two main ways of doing a measurement of how good or bad that link is are an S-parameter measurement using a VNA, which is a vector network analyzer,
[137.72 --> 151.54]  and a measurement using a TDR, which is a time domain reflectometer that we were using from LaCroix, Teledyne LaCroix, that's known as a wave pulser.
[151.54 --> 161.72]  So a VNA basically sends out a sine wave, and it looks at how much of the sine wave gets through and how much of the sine wave gets reflected back.
[161.72 --> 174.76]  Because some of it, you know, like a wave hitting a rock in a pool or something tends to send a wave backwards because it's a discontinuity.
[175.24 --> 185.34]  So the machines measure that reflection and the transmission and how much of that sine wave gets through, and that tells you how good or bad the channel is.
[185.34 --> 188.14]  A TDR sends a pulse.
[188.70 --> 204.46]  So it's, you know, for those of us who remember math, and I remember just enough to be dangerous, if you send an impulse function, so a delta function, which is an infinitely narrow unit pulse down a transmission line,
[204.46 --> 207.52]  the FFT of that is basically all frequencies.
[207.52 --> 220.64]  And so a TDR tries to approximate that using a known pulse, and it sends that pulse down, and it looks at how much of that pulse is reflected back, and what the shape is, and how much of the pulse gets through.
[220.64 --> 232.16]  And so there's benefits in detractions either way, but the way we're using is a TDR method from Teledyne-Acroix using a wave pulsar.
[232.16 --> 240.56]  And that thing is good up to 40 gigahertz or so, but our probes we limited to 26 gigahertz because of probing limitations.
[240.92 --> 250.58]  But basically it's a way of measuring how good a channel is using a little voltage wiggle that we send down the line and see how it can.
[250.64 --> 253.42]  See how it returns and see how much of it gets through.
[254.66 --> 262.06]  So obviously a lot of meat on that phone, and I want us to kind of work up to that measurement.
[262.70 --> 265.20]  But in doing so, maybe it's worth backing up a little bit.
[265.94 --> 268.64]  And this is a 100 gigabit backplane.
[268.64 --> 275.84]  And lest anyone, I mean, I think most folks may be coming to this kind of from higher up in the stack.
[276.50 --> 290.76]  And it is, this is really high-speed stuff, and it is really physically challenging to get a cable backplane to operate at 100 gigabit or 28 gig NRZ in this case.
[290.76 --> 299.58]  But Arjen, do you want to talk about some of the challenges that we had in the earliest ways we were kind of thinking about this?
[301.52 --> 305.32]  Yeah, so I want to put a little asterisk.
[305.32 --> 313.26]  So when someone hears 100 gig, what we're talking about is four channels of 28 gigabit signal, the 28 gigabaut signal.
[313.26 --> 329.62]  And for our discussion here, we're talking about a roughly 14 gigahertz signal because you're measuring at half the frequency, the Nyquist frequency.
[329.62 --> 336.72]  Think back about information theory you might have encountered in a computer science undergrad.
[338.36 --> 350.74]  So what we're concerned about is a signal, let's say up to about 28 gigahertz because you want to get the fundamental frequency plus then the first harmonic potentially, maybe even the second.
[350.92 --> 354.76]  But by the time you get through a little bit of the channel, all that is gone already.
[354.76 --> 364.92]  Because maybe we can get to that later, but there's some interesting stuff around what Eric was saying earlier with the reflections of the ripples in a pond.
[365.70 --> 374.08]  Basically, a signal through a channel like this, every little disturbance in the impedance profile causes a little ripple and a reflection.
[374.44 --> 378.76]  And so you can see all those in the pictures that are in the thread.
[379.52 --> 380.68]  You can see all those reflections.
[380.68 --> 385.32]  But you were asking about the challenges of getting this done.
[387.42 --> 404.90]  Well, the major challenge, if I understand the question you're asking correct, is that the receiver on a chip has a noise floor up to which it can measure this signal coming in.
[404.90 --> 411.16]  And you basically want to send a signal down a cable, but it's more than that.
[411.22 --> 413.10]  It's a cable plus the connectors plus the PCB.
[415.26 --> 422.66]  And you need to keep that signal above that noise floor because otherwise the receiver can't receive that signal anymore.
[422.66 --> 426.32]  And it can't make up whether you send a zero or a one.
[426.42 --> 427.46]  Let's keep it simple for now.
[427.46 --> 435.14]  And then it does a bunch of signal processing even to artificially lower that noise floor even further.
[435.32 --> 439.74]  So there's a full-on signal processing chain at the receiver end.
[439.74 --> 448.62]  But the manufacturer of these chips give you a specification that you need to live within.
[448.72 --> 456.00]  And in our case, for a 28 gig NRC signal, they say a ball-to-ball measurement.
[456.00 --> 467.42]  So meaning where the two devices that you're transmitting between are soldered to the circuit board, that needs to be – you can tolerate up to 20 dB of loss.
[467.96 --> 475.08]  Meaning that most – like a lot of the signal at the Nyquist frequency that we're interested in, that's roughly 14 gigahertz.
[475.08 --> 480.06]  So you can absorb at that frequency.
[480.74 --> 497.64]  You can – if you are less – if your signal that is received is above that 28 dB noise or 28 dB level, the receiver will still receive at least something.
[497.74 --> 503.94]  Whether or not you can get a completely valid link out of that, that will be – it's a little up in the air.
[503.94 --> 518.28]  And, Arian, at each level – I mean, the term for this that I had not heard before, Oxide, as I've said many times, but I'll say it again many times in this conversation, that I definitely – every day I think I know how computers work.
[518.94 --> 521.96]  You know, the next day I learned I actually did not know how computers work.
[522.44 --> 526.26]  And I definitely learned a lot at Oxide, have learned a lot at Oxide.
[526.74 --> 533.14]  The term that is used for the loss that is induced at each of these steps is called insertion loss, right?
[533.14 --> 533.70]  Yes.
[534.50 --> 536.76]  Which is kind of a – I don't know, Adam, have you ever heard of the term insertion loss?
[537.40 --> 537.68]  Never.
[538.30 --> 538.44]  No.
[539.52 --> 546.78]  And I guess – I mean, like, okay, look, a lot of things are poorly named, but it feels like insertion just feels like – I don't know, I feel like you're inserting something.
[547.26 --> 555.06]  And the insertion is kind of the – and, Eric, maybe you can kind of explain the origins of the term to those of us who are new to it.
[555.06 --> 555.50]  Yeah.
[555.50 --> 556.06]  Yeah.
[556.32 --> 561.08]  Insertion loss and return loss are the two main parameters that you look at.
[561.18 --> 565.46]  So you want insertion loss to be low, and you want return loss to be high.
[565.80 --> 575.12]  What that means is your – insertion loss means I stuck a signal into some channel, and a lot of it got through.
[575.12 --> 579.74]  So the loss to me inserting a signal into a channel is low.
[580.46 --> 589.46]  And my return loss is high because I want all of the signal I insert into it to go somewhere else and not reflect back at me.
[589.58 --> 596.50]  So I have a lot of – I don't have a low return, like, you know, a bad return loss, and I have a lot of that signal returned back to me.
[596.50 --> 605.56]  And that comes from impedance mismatch, and that's the, like, you know, 50,000-foot RF guys rolling in their chairs.
[607.86 --> 609.18]  I know what we're doing.
[609.64 --> 618.58]  All these terms and the techniques and the methods used for high-speed signal integrity all come from RF because they did it way before any of the high-speed guys did.
[619.60 --> 621.56]  So this is all based on RF stuff.
[621.56 --> 628.04]  So, like, a VNA is fundamentally a measurement system intended for RF.
[628.18 --> 632.56]  So if you're measuring, you know, radios, that's what you use a VNA.
[632.72 --> 635.68]  You'd never use a TDR because it doesn't have nearly the range.
[636.08 --> 638.92]  We can tolerate, like, 20 dB of loss.
[639.52 --> 646.02]  You know, your typical wireless channel will tolerate, like, 80 or 100 or 120 dB of loss without flinching.
[646.02 --> 660.28]  But in circuit board land, because our receivers are much lower power per bit, peak of joules per bit or whatever, versus a wireless modem, we have much lower tolerance for loss.
[661.08 --> 663.90]  Yeah, insertion loss and return loss are both RF terms.
[665.48 --> 668.60]  Looking at how much signal gets through and how much gets kicked back at you.
[668.60 --> 675.72]  Well, you would use that, too, if you're talking about any reflections, though, like in any, you know, channel.
[675.94 --> 678.70]  So, I mean, it's technically correct no matter what.
[679.84 --> 680.20]  Right.
[680.38 --> 688.08]  You know, I think it's – and, Eric, I guess that I was – so the insertion – the thing that's being inserted is the signal itself that's being inserted.
[688.26 --> 688.54]  Got it.
[688.60 --> 689.82]  Okay, that makes a lot more sense.
[689.82 --> 695.64]  And, Adam, have you been hit by impedance mismatch and reflections of you?
[695.84 --> 699.54]  This is, like, our – I feel like Adventures with Spy involved.
[699.54 --> 699.66]  No.
[700.08 --> 705.70]  So, when you – so there is – one of the ways – I saw Matt Keeter here.
[705.84 --> 714.58]  One of the ways that in software you get burned by this is you can set the speed of a pin, which is how fast it will transition.
[714.58 --> 722.04]  And the speeds you can set are, like, very slow, like, ridiculously slow, slow, and all the way up to, like, super fast.
[722.14 --> 723.12]  And you're like, I'm a software engineer.
[723.26 --> 724.60]  I want to set it super fast.
[724.90 --> 725.00]  Right.
[725.10 --> 725.30]  Exactly.
[725.60 --> 730.32]  I did – I fell for that same trap, and Matt told me how that was wrong.
[730.60 --> 730.82]  Yeah.
[731.56 --> 732.70]  It is wrong.
[732.82 --> 733.04]  Bad.
[733.44 --> 733.92]  Bad.
[734.10 --> 734.42]  Go slow.
[734.96 --> 736.80]  Go slow because –
[736.80 --> 737.80]  Work with slow users.
[737.80 --> 747.56]  And you end up with a signal coming back at you that you think is the other end sending to you, but it's like, no, no, that's you sending to you.
[747.64 --> 748.64]  And it gets very confusing.
[749.46 --> 749.68]  Yeah.
[749.80 --> 758.08]  So, a random and a story is when I – my previous company, we had a 20 megahertz clock that was getting sent to a bunch of places.
[758.54 --> 763.84]  And we needed a lot of those clocks sent, and they had to be aligned with each other because of various reasons.
[763.84 --> 777.34]  But the only chip that would do that in a reasonable, you know, amount of chips was a – like, a 1 to 28 or something fan-out buffer that could drive, like, 1.6 gigahertz signals.
[778.26 --> 780.42]  Which are, you know, absurdly fast.
[780.58 --> 780.86]  Right.
[780.86 --> 782.06]  And we had a 20 megahertz clock.
[782.16 --> 783.16]  And we're like, okay, fine.
[783.20 --> 783.56]  It'll be fine.
[783.62 --> 784.18]  20 megahertz.
[784.26 --> 784.68]  It'll handle that.
[784.70 --> 785.02]  No problem.
[785.42 --> 785.58]  Right.
[785.64 --> 786.26]  Yes, it will.
[786.36 --> 792.28]  But it'll send that out with a, like, 6 gigahertz edge rate, you know, edge bandwidth.
[792.28 --> 796.92]  So, we were sending a 20 megahertz clock of the sharpest edges known to existence.
[798.06 --> 806.04]  And amazingly, that caused us problems because, you know, when you're sending a 20 megahertz clock, you don't need 1.6 gigahertz harmonics coming in.
[806.26 --> 806.68]  Right.
[807.04 --> 808.16]  In fact, they're confusing.
[808.16 --> 808.88]  They're actually bad.
[809.42 --> 809.64]  Right.
[810.06 --> 816.48]  So, who we are on the space has a good explanation for what impedance actually means.
[816.48 --> 819.86]  Because I've, it's a term that I use daily.
[820.08 --> 824.24]  And I have some amount of intuition for what it means.
[824.24 --> 826.32]  But it's actually kind of fuzzy to describe.
[826.82 --> 829.62]  There's a mathematical term for it, but that's not intuitive.
[831.40 --> 833.54]  I mean, yeah, go for it.
[833.68 --> 833.78]  Okay.
[835.62 --> 845.58]  Impedance in a non-math way, you can think about it as the amount of information that travels from one place to the next.
[845.58 --> 850.94]  In terms of, like, how much you send in and you're analyzing the amount that you get out.
[852.02 --> 853.70]  So, it can be a voltage.
[854.22 --> 856.62]  So, I send in something at 5 volts.
[857.16 --> 860.88]  And over the course of whatever the period that I'm sending it through, it comes out a little bit lower.
[862.04 --> 865.92]  Or you're sending, I'm trying to talk to you and it's noisy.
[866.16 --> 869.06]  And I say, you know, 5 words and you get 3.
[869.06 --> 875.72]  Or, you know, so it's any characterization of the amount lost.
[875.72 --> 876.72]  Yeah.
[879.00 --> 886.76]  So, the way I sort of try to grasp it is you insert a certain amount of energy into a channel.
[887.56 --> 893.80]  And that is characterized by a voltage and an amount of current.
[894.76 --> 899.82]  But these are just sort of ways in which we can measure impedance.
[899.82 --> 901.88]  But they're not the actual thing.
[902.00 --> 904.14]  It's a measure of energy going into that channel.
[904.26 --> 911.40]  And when we talk about this edge rate being too fast, you're basically inserting energy at a really small time delta.
[911.58 --> 913.52]  You're pushing a lot of energy into that channel.
[913.64 --> 922.96]  And if that channel is not able to absorb that energy at that exact rate, then it is going to immediately reflect that back at you.
[922.96 --> 928.00]  So, that's where you talk about an impedance mismatch or an impedance discontinuity.
[928.18 --> 937.86]  It's where basically the amount of energy that the channel can absorb or push forward, like transmit for you, is different from one place to the next.
[937.94 --> 939.02]  And that's like at an instant.
[939.26 --> 941.60]  There's like a sharp edge where that is.
[942.26 --> 951.14]  And then at that point where these two things are, where the channel is not matched, where basically there are two different impedance values, so to speak,
[951.14 --> 954.24]  you're going to get a reflection that is going to come back to you.
[954.26 --> 955.76]  Because that energy needs to go somewhere.
[955.86 --> 960.18]  Because it can only absorb some amount of energy that it can handle.
[960.40 --> 963.02]  And then the rest needs to, it is preserved.
[963.16 --> 964.14]  It needs to go somewhere.
[964.26 --> 965.30]  So, it will come back to you.
[965.34 --> 966.52]  That's the only place it can go.
[967.20 --> 972.02]  Well, you can be a jerk about it and just say it's entropy and then be right at the time.
[972.34 --> 973.00]  Oh, that guy.
[973.22 --> 973.84]  Oh, that guy.
[975.00 --> 981.12]  Yeah, I mean, the Wikipedia definition of characteristic impedance is the ratio of voltage to current.
[981.14 --> 988.94]  You know, in a wave propagating through a channel, which is great and probably, you know, mathematically correct on everything.
[989.04 --> 991.74]  But it gives you basically zero intuition about what the hell you're trying to do.
[991.74 --> 1011.14]  And so, the only way I can think of it is, okay, the impedance is the, you know, whatever that trace width and trace spacing to the ground plane, we have to hit so that the impedance and ohms matches both the transmitter source impedance and the destination receiver impedance.
[1011.14 --> 1013.58]  And that varies based on the standards.
[1013.76 --> 1016.62]  Like PCIe is like 85 ohms or something.
[1017.08 --> 1019.48]  A lot of the newer stuff is 92 ohms.
[1020.06 --> 1025.46]  Single-ended stuff is always generally 50 ohms or 75 ohms if you're talking broadcast.
[1026.20 --> 1028.12]  And there are reasons for those impedances.
[1028.12 --> 1039.04]  But basically, you have to match whatever you need to based on whatever the transmission protocol you're using is.
[1039.56 --> 1046.64]  And in our case, we're using somewhere in the 90 ohms-ish, 92 ohms, something like that range.
[1047.20 --> 1049.06]  But those are all conventions.
[1049.06 --> 1055.40]  So, we all built our receivers around this idea of like, okay, let's everyone try and build a receiver that can take a chance.
[1055.76 --> 1057.96]  There's a reason that 50 ohms was chosen.
[1058.24 --> 1061.56]  I don't remember enough of it to go into the explanation for it.
[1061.60 --> 1062.92]  But there is a reason for that.
[1063.84 --> 1066.38]  The interested reader can look up.
[1066.64 --> 1066.86]  Yeah.
[1067.42 --> 1072.76]  So, I guess the point I'm trying to make is that the 50 ohm, it's not a totally arbitrary number.
[1072.92 --> 1074.70]  But it is a number we chose.
[1074.70 --> 1079.98]  There's nothing necessarily fundamental about why it couldn't be, say, 40 or 60 or whatever.
[1080.10 --> 1086.44]  It's just that we started to all use 50 because otherwise, you need to match all these devices.
[1086.88 --> 1092.76]  You need to match all the pieces in the channel to ideally all be that 50 ohm so that you have no reflections.
[1092.92 --> 1104.32]  You can make this perfect channel that has no discontinuities and is impedent so that you can, like, you basically, as the energy travels through this, there is nothing that will get reflected back.
[1104.70 --> 1109.02]  And, Arian, when you say we chose 50 ohms, do you mean a totally naive question?
[1109.18 --> 1110.74]  Do you mean we oxide or we human?
[1110.86 --> 1112.02]  No, we humanity.
[1112.26 --> 1112.48]  Okay.
[1112.68 --> 1118.64]  We electrical engineering humanity back in, I don't know, the 30s, 40s, or ever when they started doing.
[1119.68 --> 1122.56]  But in this case, the broadcast industry picked 75.
[1122.56 --> 1127.66]  So a lot of broadcast equipment is at 75.
[1128.16 --> 1128.92]  I mean, of course.
[1129.88 --> 1130.18]  Sure.
[1131.68 --> 1132.76]  I mean, of course.
[1132.84 --> 1138.84]  I just, like, I feel like there's certain truisms that transcend every engineering domain and the fact that two different bodies picked it.
[1139.10 --> 1144.22]  If there's an arbitrary number to be picked, you know that two different groups picked different numbers and then beat it about it.
[1144.22 --> 1149.60]  But this whole concept of impedance, and, like, Eric is absolutely right.
[1149.62 --> 1153.20]  When you're building a system, all you think about is this impedance number.
[1153.40 --> 1157.88]  It's expressed in ohms, and you do your best to try and match it everywhere.
[1158.08 --> 1163.84]  And you get a – there's a bunch of equations that you're using, and some of them are, you know, more detailed or complex.
[1163.96 --> 1166.94]  And then there's some shorthands that you use to get to those numbers.
[1166.94 --> 1181.24]  And then – but as a person writing software for, you know, like, pretty much forever, and then transitioning into electrical engineering, this was – a couple years ago, this was a very tough concept for me to grasp.
[1181.32 --> 1186.42]  Because I struggled with the math or the physical – I struggled with the mathematical perspective of this.
[1186.42 --> 1192.68]  And I had to sort of transition a little bit in the physical aspect because you can look at this from two different directions.
[1192.88 --> 1202.14]  And you can look at it from a hardcore, like, equations perspective, and it will tell you absolutely nothing, or at least it didn't do anything for me until I started reading some books that had a different perspective.
[1202.38 --> 1205.40]  And then I, like, oh, okay, there's – I started to build some intuition.
[1205.62 --> 1208.92]  Although, like I said, the reason I was asking this question early, can we define it?
[1208.94 --> 1209.86]  Is because it's so fuzzy.
[1209.86 --> 1216.30]  No one seems to really be able to, like, intuitively tell us what it is.
[1217.04 --> 1219.34]  It's just frustrating to a degree.
[1220.42 --> 1238.56]  Well, I mean, it feels like it is – and it's so great to hear you kind of ask these super basic questions because it does feel like some of these things are – like, I'm just having a very hard time with the intuition around a 28 gigahertz – or 14, I guess – gigahertz signal.
[1238.56 --> 1247.28]  It's just – I mean, I'm so accustomed to that being so much faster than anything we can run a clock on in an IC, in an ASIC.
[1247.90 --> 1251.72]  To think that, like, we've got anything at 14 gigahertz.
[1251.72 --> 1257.52]  It's just – and I guess this gets to your point earlier, Eric, about, like, this is all RF.
[1257.74 --> 1263.72]  And when you're at that point, like, it's a radio that's in a channel, basically, is maybe the better way to think about it.
[1263.72 --> 1263.84]  Yeah.
[1263.84 --> 1269.16]  High-speed serial links are crappy radios that only do two levels.
[1269.42 --> 1270.84]  I mean, they're really just crappy radios.
[1270.84 --> 1270.98]  Yeah.
[1271.28 --> 1275.10]  And they're crappy radios because they can have idealistic channels.
[1275.26 --> 1278.78]  There's no external interference from, you know, your neighbor's Wi-Fi.
[1278.78 --> 1283.12]  There's no – there's no crap from the local airport blasting.
[1284.16 --> 1290.68]  All of this is very, you know – high-speed serial links are fundamentally an RF channel in a very, very controlled environment.
[1291.44 --> 1299.12]  Well, and we want to make some crappy radios because we don't want to spend all that silicon real estate on expensive, like, analog front lines for this.
[1299.12 --> 1301.84]  Like, power and chip space is very expensive.
[1302.12 --> 1304.44]  We want to make this as simple as we can make it.
[1304.44 --> 1318.20]  And that's why, for example, with every stepping technology generation, say, for PCI Express, these receivers become more complex because we need to go to faster speeds, which means that that noise floor needs to go down, et cetera.
[1318.36 --> 1323.50]  So we're starting to – those receivers borrow more and more and more out of, like, actual radio receivers.
[1323.70 --> 1326.78]  And as a result, they become more complex, more power-hungry.
[1327.10 --> 1333.48]  Yeah, like 100 gig and 400 gig start using things like tech and, you know, forward error correction because they know they're going to get bit error.
[1333.48 --> 1340.78]  Back in the 10 gig lane, like, bit errors, like, no, you just – they're so rare that you just handle them at a higher level.
[1340.90 --> 1341.42]  No worries.
[1342.04 --> 1347.28]  But when you get up to 28 gig, you know, the famous quote is like, oh, no, you're going to see errors.
[1347.48 --> 1348.88]  It's just how many.
[1349.74 --> 1358.66]  And you just want to make sure that rate's not so high that your forward error correction or your, you know, CTLE or DFE and all that stuff can't correct them.
[1358.66 --> 1377.62]  And your radio – the radio protocols that we use for, let's say, your cellular network or whatever, use really – or relatively complicated encoding schemes exactly for that because they have to – you want – you don't want to retransmit in that channel ever because that's expensive.
[1377.62 --> 1380.08]  So you want to recover as much of that signal as you can.
[1380.24 --> 1386.26]  So they – the radio world has been doing forward error correction for a long, long time because they were forced to.
[1386.98 --> 1395.46]  But slowly, more and more of that shows up in these serial receivers for, you know, wired Ethernet and PCI Express and whatnot.
[1395.46 --> 1397.92]  Yeah, I mean, they're crazily sophisticated.
[1398.28 --> 1400.76]  And I mean, like – and maybe this is a good segue, Tom, to you.
[1400.94 --> 1416.10]  And I want to get – so we get some folks from Ancestry as well to talk about, like, how do you think about the system in advance to know that, like, when we build it, we are going to have any chance of having something that actually works?
[1416.60 --> 1421.12]  I mean, how do you – and maybe, Ari, and you want to kind of serve as the intro to that.
[1421.18 --> 1422.54]  Like, how did we model the system?
[1422.54 --> 1428.74]  Well, we paid Anc's money to get software.
[1429.46 --> 1431.46]  And Tom spent many, many hours.
[1431.78 --> 1432.08]  Yeah.
[1432.48 --> 1436.68]  Well, it would – but also, like, fundamentally, it serves with, like, the piece of paper.
[1436.92 --> 1446.64]  You know you need to go – let's say you're going over some length of coax and you know how much loss there is in a, you know, coax per meter.
[1446.64 --> 1448.88]  And so you start building it up.
[1448.96 --> 1454.28]  You know that the chip vendors told you you've got this many dB of insertion loss for your margin.
[1454.56 --> 1456.58]  And then you start sort of, like, papering it out.
[1456.64 --> 1458.22]  Can this architecturally work?
[1458.66 --> 1469.14]  For instance, if you decided early on that there's no way you could meet that insertion loss spec with the amount of PCB that you had to go across and the cable length,
[1469.14 --> 1475.48]  then we'd be, you know, looking at, like, re-timers somewhere and then the re-timer would have to fit in there, right?
[1475.56 --> 1481.60]  So, I mean, fundamentally, it starts with a piece of paper and just, like, looking at the specs and making sure the specs sort of work out.
[1481.86 --> 1488.08]  And then you could delve into it and, like, actually put it to the test and look at the physics, you know, make sure it actually works.
[1488.08 --> 1494.08]  Yeah, because the back of the napkin gives you sort of the rough estimate for, like, is this even worth trying, which we did.
[1494.34 --> 1500.32]  So we went to, you know, the cable manufacturer, in this case, we've been working with Semtech.
[1501.04 --> 1505.22]  And they gave us an estimate for, like, hey, this is what our cable system can do.
[1505.46 --> 1506.26]  This is modeled.
[1506.36 --> 1506.96]  This is implemented.
[1507.20 --> 1508.20]  We've tested that.
[1508.82 --> 1510.94]  And then, yes, but that assumes that you're doing everything right.
[1511.00 --> 1518.02]  That assumes that all your, you know, everything on your PCB is correct, that you're not basically losing more of that signal than you absolutely have to.
[1518.36 --> 1519.84]  And that's where ANSYS comes in.
[1519.98 --> 1521.04]  And that's where, exactly.
[1521.64 --> 1521.84]  Yeah.
[1522.04 --> 1533.68]  That's where we start to really dial that in so that we build simulations of the actual PCB, the actual traces on the PCB, the dielectric material between all the copper pieces, the vias, all that.
[1533.68 --> 1546.42]  And then you start to run simulations and you start to carefully tweak all these pieces so that you improve that, or you basically reduce that loss until you are as close to that optimal that you can hit.
[1548.08 --> 1552.30]  And then hopefully you, by then, have met the specifications and your link actually works.
[1553.04 --> 1553.26]  Yeah.
[1553.38 --> 1557.82]  So speaking of vias, like, we've spent a lot of time looking at vias.
[1558.82 --> 1561.62]  Like, every, can you give a little bit of an overview?
[1561.62 --> 1561.90]  Yeah.
[1561.90 --> 1562.50]  Yeah.
[1562.50 --> 1582.30]  So, well, every time, you know, if you were to look at a cross section of a PCB trace, for this sake, there's two classes of traces you could run on a PCB, what they call microstrip, which is any external routed traces, which are half referenced to air.
[1582.30 --> 1592.34]  And the other half is, well, not exactly 50%, but, but it's a, it's not a uniform dielectric part of its air, part of its, whatever your PCB FR-4 is.
[1592.56 --> 1605.26]  And so strip line are where you're totally embedded within two, let's say two shielded ground planes and your signals have, they're, they're a uniform dielectric.
[1605.98 --> 1608.34]  So Tom, are those two different kinds of vias?
[1608.34 --> 1610.76]  Um, well, I'm getting to that.
[1610.94 --> 1619.72]  The, uh, the idea is that as we're routing across a PCB, the, the, the cross section of the fields are really well behaved.
[1619.88 --> 1622.64]  We can understand them even like with a 2D field solver.
[1622.80 --> 1627.84]  But as soon as you approach a via, the via is basically a drill going from one layer to the next.
[1627.84 --> 1634.24]  Um, and all of a sudden where your return currents were really nice and uniform on your ground plane.
[1634.62 --> 1640.34]  Now they, they go into another ground via connecting the two ground planes together.
[1640.48 --> 1642.40]  The problem becomes really complicated.
[1642.40 --> 1645.66]  You've got, um, physics that are not simple.
[1645.66 --> 1653.76]  And that's why we need 3D field solver to actually like put the geometry together and actually investigate what is going on.
[1653.76 --> 1666.12]  And what are the, in other words, you know, you can look at the different inductances and capacitances, um, through, you know, as the, the signal transitions from a TEM mode in the strip line.
[1666.12 --> 1676.46]  And then you're going to be able to do a little bit of a PCP to this via, which is like a really funky, you're trying to make like a coax in the Z axis of your board going from the top to the bottom, for instance.
[1677.40 --> 1692.00]  So you're going for something that is like nice 2D math that you can sort of still approach with your high school math to having to solve like full on differential equations for a 3D art, like not an arbitrary 3D structure, but a very complicated 3D structure.
[1692.00 --> 1697.06]  And, and that's quickly like surpasses what you can do by.
[1697.06 --> 1701.94]  By the way, I'll say this is a very hard discussion to have without like showing diagrams.
[1702.24 --> 1705.96]  You know, like pictures are really helpful here.
[1706.54 --> 1706.72]  Yeah.
[1707.58 --> 1708.76]  Well, and I, yeah.
[1708.86 --> 1713.58]  And Adam, I don't, in terms of like, I mean, first of all, Adam, don't you just feel just like listening to this?
[1714.12 --> 1718.94]  Like we've entrusted all of this, like rocket science to the pile of idiots at the top.
[1719.02 --> 1720.08]  We're actually driving this with software.
[1720.08 --> 1729.82]  I mean, I'm just like, I, I, I, I mean, I, I just feel like about all of these software that I've seen or written that has just like abused the network or behaved terribly.
[1730.02 --> 1731.02]  You're like, don't.
[1731.34 --> 1734.46]  We're creating this beautiful thing, this, this physical piece of art.
[1734.64 --> 1736.44]  And then, and then, and then we hand it to you.
[1736.52 --> 1741.52]  And then we hand it, I know for, for some dumb ass timeout that was like specified in like, in like seconds.
[1741.62 --> 1743.00]  I'm supposed to be milliseconds or whatever.
[1743.14 --> 1744.04]  It's like, oh my God.
[1744.20 --> 1744.68]  That's right.
[1744.68 --> 1750.06]  You know, back, back in the day in Solaris, if you unplugged the cable, it would say link down cable problem.
[1750.54 --> 1757.38]  And I feel like, I mean, even then it felt like a, a pretty unsophisticated diagnosis of what might be going on.
[1757.66 --> 1757.82]  Yeah.
[1757.86 --> 1763.46]  And now it's just like, what, why did we think cable problem was, I mean, there's so many problems that could, that could arise.
[1763.46 --> 1774.52]  I know it's just amazing that like, and, and Tom, just to go to like what you're, when you are kind of visualizing these vias where you are, because unfortunately these are not, our circuit boards have multiple layers.
[1774.74 --> 1777.16]  Unfortunately, reality is a real pain in the ass.
[1777.70 --> 1777.86]  Yeah.
[1777.96 --> 1778.18]  Yeah.
[1778.18 --> 1786.94]  The challenge is like in two areas, basically you have to get from the BGA, which is like, there's, you know, everyone's probably familiar with a BGA.
[1786.94 --> 1792.66]  There's a bump and it has to have a circular pad on the top side of the PCB or the bottom in our case, the top.
[1793.00 --> 1797.98]  And you've got to basically get from that to one of the inner layers.
[1798.32 --> 1805.72]  And then you go across your board to the next connector of this, in this case, the Samtech Air of six connector we're using.
[1806.16 --> 1809.28]  And you've got to have another via there to be able to go to the connector.
[1809.28 --> 1818.76]  So that's what the vias are really, as long as you can like only have the two vias, the via transition areas in the BGA and then at the connector.
[1819.38 --> 1822.30]  And so those are the two areas we focus on the most.
[1822.62 --> 1831.04]  And in fact, you know, like it gets really complicated because as you put a lot of vias through in tight proximity to one another inside of the BGA,
[1831.04 --> 1837.54]  and you have traces routed through next to those and the voids and there's back drill clearances and all this stuff,
[1837.80 --> 1848.60]  you actually can have some of the RX layers coupling to the TX layers that are, you know, maybe half a millimeter away.
[1848.74 --> 1854.44]  You can actually have some coupling through the void, which again, this would be great to have a picture.
[1854.44 --> 1861.20]  But there's like this really complicated way of seeing the way the coupling modes can happen.
[1861.44 --> 1865.46]  And unfortunately, that isn't really clear until you can visualize it in 3D.
[1865.56 --> 1871.12]  The 2D CAD programs, you know, they give you like a 2D down view of like polygons.
[1871.36 --> 1875.94]  But there's a lot more to it because you need to really understand what is going on in the Z axis,
[1876.14 --> 1879.72]  how much space is between this and that and the other thing.
[1879.72 --> 1887.04]  And that's where once you can extract a 3D geometry and then look at it in that world or you get good at it after you do it enough,
[1887.12 --> 1890.78]  you start to like have a 3D view just as looking at a 2D.
[1891.54 --> 1893.48]  And this might be getting ahead of ourselves.
[1893.68 --> 1899.88]  But as we look at, as we do the math and do the simulation, do we just get back yep or nope?
[1900.00 --> 1901.94]  I mean, how do you debug this thing?
[1902.06 --> 1908.54]  Like how do you figure out where back and you get back an inscrutable waveform that has a bunch of little spikes all over it.
[1908.54 --> 1912.18]  And you have to assess whether or not that is good enough.
[1912.82 --> 1914.76]  And it's even trickier.
[1915.02 --> 1915.40]  Absolutely.
[1916.02 --> 1922.44]  You have to know, you have to sort of test whether or not your simulation was valid.
[1922.62 --> 1924.56]  Like did you actually set it up correctly?
[1924.68 --> 1926.14]  Because there's an art to this as well.
[1926.66 --> 1929.80]  When you have to like put a, you put what they're called are ports.
[1929.80 --> 1932.90]  When you have a 3D geometry, you assign a port.
[1934.08 --> 1941.68]  Then when it solves for those ports, it'll basically look at energy in one port and see how it comes out on all the other ports.
[1941.78 --> 1945.12]  And then it solves that whole set of equations.
[1945.12 --> 1949.02]  So you have a set of your S parameters that tells you what happened.
[1949.68 --> 1951.78]  If you only have four ports, that's one thing.
[1951.78 --> 1961.64]  But like we did an extraction on a larger chunk of the chip that literally took two or three weeks on a 512 gig machine and had 48 ports.
[1962.02 --> 1971.72]  So I think similarly when we were doing the Samtech extraction, which Samtech did for us because they have their connector model.
[1972.06 --> 1975.06]  I think that similarly took like a week or something like that.
[1975.06 --> 1983.96]  So these are non-trivial things and you got to really know how to set it up correctly and make sure that like the answer you're going to get back is the right one.
[1983.96 --> 1990.56]  Because unfortunately, you've spent all this time and it could be, oops, my port was, you know, put to the wrong reference.
[1990.76 --> 1992.38]  And now the data is invalid, right?
[1992.94 --> 1993.22]  Right.
[1993.30 --> 1995.36]  I mean, that must be very nerve wracking.
[1995.60 --> 2004.44]  I mean, because and obviously in any simulation, you are trying to find as many ways as possible to check your model against reality.
[2004.44 --> 2009.64]  But these are, Thomas, you mentioned these things are run for a really long period of time, super sophisticated software.
[2010.24 --> 2019.18]  This is not, I mean, Adam, I feel like like the kind of simulation we do in software generally is done with like an aux script, usually of like two or three lines.
[2019.34 --> 2026.78]  I feel like, I mean, I think the modeling we do is so unsophisticated by comparison to where we've got this actually like physical thing.
[2027.78 --> 2030.30]  And these electrons just don't behave very well.
[2030.30 --> 2034.46]  I mean, it's like we kind of have this idea of like, oh, these two wires are connected logically.
[2034.76 --> 2037.94]  So clearly it's going to like travel along this path.
[2037.98 --> 2039.88]  And it's like, no, no, no.
[2039.88 --> 2042.84]  I was in a meeting earlier today where we were doing some performance benchmarks.
[2043.06 --> 2044.78]  Were we using the right SSD?
[2045.10 --> 2046.76]  Well, we were using an SSD.
[2047.76 --> 2052.14]  So, I mean, it's like a pretty gross by comparison.
[2052.58 --> 2052.88]  I know.
[2053.18 --> 2053.42]  I know.
[2053.42 --> 2060.96]  So, I know we've got Larry and Robert who joined us from ANSYS.
[2061.14 --> 2061.74]  Maybe, I don't know.
[2061.92 --> 2064.36]  And you're getting your first like real exposure inside the oxide.
[2064.54 --> 2066.28]  You may just be like, oh, my God, these guys are turkeys.
[2066.52 --> 2066.90]  We need to.
[2071.14 --> 2075.24]  Well, just don't ask us to create a network switch because we can't do that.
[2075.74 --> 2076.42]  There we go.
[2076.54 --> 2077.16]  Okay, fair enough.
[2077.16 --> 2091.92]  So, I mean, first of all, is oxide's use case, is this like a common use case for folks that are, I assume that everyone has to do these kinds of simulations before they actually build this up, right?
[2091.92 --> 2094.06]  Because it's so high consequence to get it wrong.
[2094.96 --> 2101.30]  Well, back in the old days, if you're moving, you know, something at one gigabit per second, not so much.
[2101.30 --> 2108.84]  But now, today, you know, every little discontinuity on the line, as you've mentioned, conspires against you.
[2109.68 --> 2122.38]  And having something that solves for the physics, what are those options and how are they going to compile on top of one another using our simulators really makes a big difference.
[2123.24 --> 2123.38]  Yeah.
[2125.60 --> 2131.06]  Well, I think there's a really good point here that is, and Eric, I know you mentioned this to me as well, Tom, you've said this as well.
[2131.30 --> 2135.58]  That, like, when you have loss, like, you're never going to get it back.
[2135.80 --> 2139.26]  So, every little bit in this, like, what of it matters?
[2139.44 --> 2140.26]  All of it matters.
[2140.30 --> 2143.28]  Like, all of the details matter enormously in this.
[2144.66 --> 2146.00]  Especially at these frequencies.
[2146.54 --> 2154.66]  So, you know, the interconnect, like, you look up on the data sheet, the semiconductor vendor tells you you can stand 20 dB of loss or whatever it is.
[2155.08 --> 2157.82]  If they're actually, in fact, it's frequency-dependent loss.
[2157.82 --> 2162.70]  But the network, the interconnect, looks like a low-pass filter.
[2163.44 --> 2167.90]  So, DC, you said earlier, right, a simple, hey, these are just connected together.
[2168.00 --> 2170.24]  So, DC, sure, it marches right through.
[2170.70 --> 2178.50]  But the higher frequencies, 14 gigahertz, 28 gigahertz, is diminished a lot more than the lower frequencies are.
[2178.68 --> 2179.56]  It's a low-pass filter.
[2179.56 --> 2187.36]  So, any sharp edge that you'd like to send, like transitioning that NRZ signal from zero to one, gets rolled over.
[2187.78 --> 2189.06]  It gets smeared out.
[2189.74 --> 2191.82]  And how much does it get smeared out?
[2192.14 --> 2193.06]  And then it gets worse.
[2193.48 --> 2196.06]  You stick a via structure in between or an IC package.
[2196.60 --> 2200.32]  Some of the energy goes forward towards the receiver.
[2200.76 --> 2202.20]  Some of it bounces back.
[2202.20 --> 2207.30]  Some of it bounces back to the transmitter and then bounces forward yet again to the transmitter.
[2207.60 --> 2209.02]  They start holding upon one another.
[2209.02 --> 2209.16]  Yeah.
[2209.32 --> 2217.00]  So, the bounce back and forth thing can have some interesting effects because, you know, like let's say your fundamental is 14 gigahertz.
[2217.16 --> 2225.18]  And let's say you have two structures that have imbeensis discontinuities that are spaced just far enough apart that you get a standing wave at 28 gigahertz.
[2225.18 --> 2230.82]  And now you have this massive energy suck out at 28 gigahertz and it basically looks like a notch over.
[2231.22 --> 2235.74]  And it just sucks out any possible information there and gives you the middle finger on your signal.
[2237.02 --> 2239.64]  I mean, a standing wave at 20 gigahertz.
[2239.78 --> 2241.40]  I'm just trying to like wrap my brain around that.
[2241.44 --> 2242.44]  Like that feels bad.
[2243.40 --> 2247.38]  Well, and if you move those vias like five millimeters apart, it's gone.
[2247.64 --> 2248.68]  And you won't even see it.
[2249.34 --> 2253.08]  So, if you have those at just the wrong spacing, it just screws you so bad.
[2253.08 --> 2264.30]  And I think this you're exactly right in the sense that one of the things that's important to that I've always found in my flow of simulation is that like you start by looking at it in the frequency domain.
[2264.44 --> 2267.92]  So, you can at least get an idea of like at what frequency with the losses.
[2267.92 --> 2284.84]  But then because there are all these time-dependent dependencies to a particular channel where the via actually lives within your data rate, that's yet another level of simulation that's really helpful to look at this in time domain to see what the I actually is.
[2284.94 --> 2286.86]  Because you might find some of the discontinuities.
[2286.86 --> 2300.16]  Like this is where via backthrilling comes in and you can really see it clearly where there are some frequencies that that little structure resonates and the wrong data rate at the wrong stub, you know, it could actually, you know, kill your line.
[2300.64 --> 2304.06]  So, Tom, can you just describe the I because that's something that does come up with.
[2304.06 --> 2312.54]  Oh, it's just taking like taking any data transmission and all you do is you take like if one UI is one bit symbol.
[2312.78 --> 2316.20]  So, at 20, it's a 25 gig that we're running at.
[2316.62 --> 2318.12]  It's 40 picoseconds roughly.
[2318.12 --> 2328.56]  So, basically, you overlay every 40 picosecond chunk on top of one another so you can actually get the aggregate of what does every single up-down transition look like over one another.
[2328.70 --> 2335.02]  So, it ends up creating this nice diagram that shows that looks like an I, whether it's open or closed is the terminology.
[2335.60 --> 2341.32]  And it gives you an idea of like how much margin you have for your receiver thresholds, right?
[2341.34 --> 2345.28]  So, you just get to like weigh everything over on one simple view over one.
[2345.28 --> 2352.28]  And to drive on the point, the open eye meaning there's a large difference between what is considered a zero and a one.
[2352.36 --> 2355.56]  So, that's easier for the receiver to make out.
[2355.80 --> 2358.66]  And then PAM 4, you've got now 44 levels.
[2358.94 --> 2359.96]  So, you know, it just gets worse.
[2360.36 --> 2360.64]  Yeah.
[2362.24 --> 2362.52]  Yeah.
[2362.66 --> 2364.52]  Adam, have you seen the PAM 4 eye diagrams?
[2364.88 --> 2365.20]  No.
[2365.54 --> 2365.78]  All right.
[2365.80 --> 2367.00]  So, you look at an eye diagram.
[2367.10 --> 2368.30]  You're like, okay, like I can appreciate that.
[2368.34 --> 2369.14]  That's like a clean eye.
[2369.22 --> 2369.92]  That's an open eye.
[2370.20 --> 2371.14]  It's like, but what happened over here?
[2371.14 --> 2372.18]  This one looks totally wrong.
[2372.26 --> 2373.60]  It's like, no, no, that's a PAM 4 signal.
[2374.22 --> 2375.08]  That looks really good.
[2375.52 --> 2375.88]  Yeah.
[2375.96 --> 2376.96]  It's like, oh, and that looks great.
[2377.10 --> 2379.42]  Because as Eric mentioned, it's a cyclops effectively.
[2380.12 --> 2384.74]  And you have, because you are, you are laying on multiple voltage levels.
[2385.56 --> 2386.88]  Apparently, we're giving up on digital.
[2386.96 --> 2389.76]  Digital is like, has taken us as far as digital is going to take us.
[2390.10 --> 2391.38]  So, we're at least binary.
[2391.38 --> 2396.92]  If you look at like Ethernet, it's I think a 5-level, something like that, signaling.
[2397.28 --> 2399.58]  And there's either these attacks, but.
[2399.58 --> 2405.64]  Gigabit Ethernet Base-T is still using PAM 5.
[2406.02 --> 2412.34]  And then I think 10 gig over Twisted Pair jumped up to, I think it's PAM 16.
[2413.26 --> 2413.48]  Yeah.
[2413.68 --> 2414.08]  What?
[2414.08 --> 2414.24]  What?
[2414.64 --> 2415.02]  Yeah.
[2415.08 --> 2417.40]  I did a 10G, 10G Base-T 5.
[2418.60 --> 2420.92]  And it's 16 different voltage levels?
[2422.06 --> 2422.42]  Yeah.
[2422.54 --> 2423.24]  Four bits per single.
[2424.44 --> 2424.76]  Holy.
[2424.76 --> 2425.16]  Man.
[2427.44 --> 2429.54]  I feel like it's like everything's a lie.
[2429.72 --> 2430.88]  Like, what's not a lie right now?
[2430.88 --> 2432.48]  It's lower frequency, though.
[2432.58 --> 2433.94]  So, you have that going for you.
[2434.38 --> 2434.40]  Yeah.
[2434.44 --> 2436.04]  Even those eyes are a lie.
[2436.12 --> 2438.40]  Because what you're looking at is something that's already been equalized.
[2438.46 --> 2439.78]  So, really, what's going on in the receiver?
[2439.92 --> 2440.94]  You don't even know what it looks.
[2441.04 --> 2441.98]  It doesn't even look like an eye.
[2442.64 --> 2442.78]  Yeah.
[2442.92 --> 2444.82]  If you broke it, it just looks like magic.
[2445.12 --> 2445.56]  Oh, it goes.
[2445.64 --> 2446.28]  This is garbage.
[2446.52 --> 2446.92]  Yeah, absolutely.
[2447.28 --> 2448.72]  We couldn't look at that on a scope.
[2448.72 --> 2455.34]  Because it's so encoded, we had to rely on DSP and the slicer to basically tell us how good we did.
[2455.58 --> 2461.72]  That instrumentation of this is all another part of the problem, which is...
[2462.38 --> 2462.56]  Yeah.
[2463.46 --> 2466.72]  So, before we get off the simulation piece, because, Larry, I've got a question for you.
[2466.80 --> 2472.72]  When you got the input into the simulation, which consists of things that you're getting out of these vendors,
[2474.44 --> 2477.16]  presumably there's obviously materials consequences, I assume.
[2477.16 --> 2478.60]  Are you getting...
[2478.60 --> 2481.62]  And how do you validate that that information...
[2481.62 --> 2482.16]  I mean, surely...
[2483.10 --> 2487.12]  Just based on the number of errors that I have found in data sheets, we have found in data sheets,
[2487.26 --> 2489.18]  surely that information is not always correct.
[2489.74 --> 2492.68]  How does one validate that that information is correct?
[2493.54 --> 2496.26]  Well, we start with the ground-based physics.
[2496.68 --> 2498.62]  So, what we do is we go from the bottom up.
[2499.68 --> 2502.20]  I should explain to the listeners what we do.
[2502.20 --> 2508.18]  We have these remarkable electromagnetic field simulators, like this thing called the high-frequency structure simulator,
[2508.36 --> 2509.70]  which does finite elements.
[2510.46 --> 2512.38]  So, you mentioned differential via structures.
[2512.88 --> 2514.76]  Well, what happens when the signal approaches it?
[2514.84 --> 2516.72]  We look at a differential via.
[2516.84 --> 2518.02]  We input the geometry.
[2518.64 --> 2520.18]  You bring it in from your layout.
[2520.18 --> 2527.90]  You specify material properties, like copper traces and whatever material you're using for the printed circuit board,
[2528.18 --> 2532.56]  what dielectric permittivity it is, what loss tangent.
[2533.26 --> 2536.16]  And then from first principles, we solve all those wave equations.
[2536.16 --> 2542.26]  And again, we were talking earlier about, you know, if you were to do this analytically on pencil and paper,
[2542.50 --> 2547.88]  it would take you six pages of math and a PhD degree in electromagnetic field theory to do it.
[2548.08 --> 2549.52]  But we do it on the computer.
[2550.24 --> 2552.00]  And so, we're solving for the field.
[2552.18 --> 2555.98]  If a signal approaches that differential via, it can bounce off it and go back.
[2555.98 --> 2561.58]  If the impedance is not correct, or some of the energy can go forward with the direction you want it to go,
[2562.22 --> 2564.68]  and we can, you know, take a look at how those happen.
[2564.82 --> 2570.14]  So, we can do that for an IC package, for the escape routing from the IC package.
[2570.26 --> 2573.56]  We can do it for vias, connectors, the cables that you have.
[2574.00 --> 2577.06]  And then we cascade all of those together into a circuit model.
[2577.18 --> 2580.18]  So, we can look at frequency domain, as you mentioned before.
[2580.32 --> 2582.12]  What does it look like versus frequency?
[2582.60 --> 2583.56]  Low versus high?
[2583.86 --> 2584.84]  How much signal can get in?
[2584.84 --> 2588.18]  What is the so-called insertion loss versus frequency?
[2589.14 --> 2592.36]  And then we can also look at a TDR, a time domain reflectometry.
[2592.56 --> 2596.24]  So, you can say, well, where are the discontinuities down the line, right?
[2596.34 --> 2602.12]  TDR is really cool because you send in a pulse and you wait for the signal to come back.
[2602.94 --> 2609.04]  Whatever it bounces off of, you can determine what is the impedance of that discontinuity
[2609.04 --> 2610.40]  and how much energy is coming back.
[2610.40 --> 2615.60]  And so, TDR, if we can do it in simulation also, just as you can do it in the lab.
[2617.14 --> 2618.06]  Yeah, that's really neat.
[2618.12 --> 2624.06]  It actually has given me a flashback to my algorithms prof who taught the class an FFT.
[2624.56 --> 2625.96]  This is a computer science class.
[2625.96 --> 2630.42]  And I remember a lot of math and an FFT.
[2631.46 --> 2635.04]  And this guy was a pure computer scientist.
[2635.84 --> 2637.64]  Adam, we may have had the same prof.
[2637.80 --> 2638.04]  You may know.
[2638.40 --> 2638.90]  This is...
[2638.90 --> 2639.50]  I know, exactly.
[2639.50 --> 2643.84]  Phil Klein, God bless you, but you are a pure...
[2643.84 --> 2645.62]  Not an engineer at all.
[2645.84 --> 2646.86]  Not overly pragmatic.
[2647.62 --> 2650.92]  And someone in the class asked, like, what is an FFT for anyway?
[2651.14 --> 2653.34]  And he's like, I don't know.
[2653.56 --> 2654.76]  I don't know that they're that useful.
[2655.40 --> 2657.34]  And I was talking to what...
[2657.34 --> 2661.52]  Of course, we went over to the engineering department and they just about declared war on the computer science department.
[2661.52 --> 2665.36]  I think the engineers are actually going to march on the computer science building and just porch it.
[2665.76 --> 2669.52]  Because it's like, no, an FFT is only the most important thing in humanity.
[2669.68 --> 2671.06]  All humanity rests on FFT.
[2671.14 --> 2671.36]  No, no.
[2671.44 --> 2675.88]  I mean, his specialty is planar graphs, which is pretty far from FFTs.
[2676.02 --> 2679.72]  Or it's understandable why he would not be that interested.
[2680.50 --> 2681.06]  That's right.
[2681.20 --> 2682.50]  And he was forced to teach his class.
[2682.66 --> 2687.72]  So they forced him to give back all the tech that relied on FFTs and then he had to walk home?
[2687.90 --> 2688.54]  No, that's it.
[2688.64 --> 2689.14]  That's it.
[2689.14 --> 2694.14]  I believe, Arian, there were several similar kinds of suggestions that he needed to be as punishment.
[2694.28 --> 2697.26]  He needed to be deprived of all innovations that relied on an FFT.
[2698.54 --> 2705.34]  But, Larry, it sounds like when you're sending that pulse back, part of the reason you can figure out where it's coming from is because of the frequencies you're getting back.
[2705.46 --> 2706.94]  Is that correct?
[2707.64 --> 2710.20]  Certainly, you can perform processing on it like that.
[2710.28 --> 2713.14]  But a PDR method is actually really old.
[2713.80 --> 2715.64]  It was used with phone lines.
[2716.38 --> 2717.00]  And it was used...
[2717.00 --> 2718.32]  Phone lines, telephone lines.
[2718.32 --> 2720.18]  And cable TV.
[2720.44 --> 2724.02]  The guy with the cable TV truck that shows up at your house has a TDR device.
[2724.56 --> 2729.44]  And what they used to do is it would literally just send a voltage that goes from low to high quickly.
[2730.28 --> 2731.24]  And that's going to...
[2731.24 --> 2736.16]  It's going to basically, you know, sort of crack the whip and send that energy down the line.
[2736.16 --> 2744.28]  And however long it takes to get down the line and back, that round trip distance, you can divide by two and say, oh, that's where the discontinuity in the line is.
[2744.28 --> 2750.12]  And they send a service technician down there to figure out where the broken in the line.
[2750.12 --> 2755.38]  Because you know how fast a speed of light is in that line.
[2755.82 --> 2757.50]  So you can calculate the distance.
[2758.10 --> 2762.88]  So like TDR sometimes will say, like, I have a distance resolution of five millimeters.
[2762.88 --> 2764.88]  And that's based on how much...
[2764.88 --> 2772.06]  How, you know, how fine of a time you can resolve in the propagation velocity of light in that medium.
[2772.58 --> 2773.56]  That is so cool.
[2774.20 --> 2775.42]  Of course, that makes sense.
[2775.52 --> 2775.88]  That's how it came about.
[2776.38 --> 2780.94]  So you're like the cable guy being like, there's somewhere around here, there's a discontinuity.
[2780.94 --> 2786.54]  So do I just start there and start counting five Mississippi until I get to the discontinuity?
[2786.88 --> 2788.00]  Yeah, just really fast.
[2788.12 --> 2789.78]  Five Mississippi is five nanoseconds.
[2790.20 --> 2794.42]  And then send the guys with a shovel to dig at that location and they dig up the cable and fix it.
[2794.82 --> 2795.66]  That's how they use it.
[2795.96 --> 2798.76]  And they still use that for, like, underground power lines.
[2798.88 --> 2800.06]  Do you want to know where a fault is?
[2800.62 --> 2800.86]  Yeah.
[2801.14 --> 2805.36]  You send a thumper out there and you thump the power line and you measure how long it takes to come back.
[2806.22 --> 2808.76]  So that's what we do with, you know, high speed interconnect also.
[2808.76 --> 2810.54]  But you can get a lot more information, right?
[2810.54 --> 2815.62]  You use a time domain measurement to develop the understanding of what's down the line.
[2815.74 --> 2818.32]  And you can back calculate with simple mathematics.
[2818.48 --> 2819.20]  You can back calculate.
[2819.32 --> 2827.00]  If you know the transmission line impedance and you see what voltages are coming back, you can calculate, well, what must be the impedance at that location?
[2827.42 --> 2836.90]  So say you send a signal down your differential transmission line on your print circuit board and you hit that via the amount of energy that the signal comes back,
[2836.90 --> 2840.12]  you can use that to calculate what must be the impedance at that location.
[2840.54 --> 2842.68]  And, Larry, are you doing that in simulation?
[2842.88 --> 2843.70]  That's happening in simulation.
[2844.06 --> 2844.96]  Oh, that is really cool.
[2845.44 --> 2849.60]  And then, Tom, are you using that information to kind of like, all right, we need to change the layout here?
[2849.84 --> 2850.38]  Every day.
[2850.92 --> 2852.66]  No, mostly it's the way.
[2852.76 --> 2855.28]  The way I use it are, like, a couple of different ways.
[2855.28 --> 2861.32]  When I'm doing a via structure, if I'm looking for matching, one way to do that is to look in return loss.
[2861.76 --> 2865.06]  And another is to do it in the time domain.
[2865.24 --> 2868.42]  So you can look at the time domain and do a TDR on your via transition.
[2868.42 --> 2886.90]  And, you know, it's a little tricky to do that because you've got to make sure that you mesh your structure to a good enough frequency that your time domain edge can, you know, so that the data is well formed for the speed at which you're going to ping it at.
[2887.26 --> 2890.08]  And, you know, so there's like, but the tools help you with that.
[2890.08 --> 2894.22]  You can actually set up meshing based on what you plan the TDR with, which is really cool.
[2895.02 --> 2895.68]  I like that feature.
[2896.02 --> 2905.10]  And, yeah, so basically it's a really helpful diagnostic when you're trying to just kind of like learn a little bit more about your circuit and you're trying to look for a way to tune it.
[2905.74 --> 2906.20]  Yeah, interesting.
[2906.42 --> 2911.08]  So, Tom, I was going to ask you, like, how you are acting on the simulation data you're getting back.
[2911.28 --> 2913.00]  And it sounds like you were doing that a lot.
[2914.56 --> 2916.34]  It's a very iterative process.
[2916.54 --> 2917.04]  You have to.
[2917.48 --> 2918.86]  Yeah, it's very iterative.
[2918.86 --> 2919.68]  We'll run through.
[2920.28 --> 2931.58]  I mean, and that's part of why, for instance, before we ran that two-week simulation, we had spent a lot of time looking at little things and getting everything dialed in, you know, on quicker sims.
[2931.64 --> 2933.04]  And then you kind of build up to it.
[2933.34 --> 2933.44]  Right.
[2933.56 --> 2933.74]  Okay.
[2933.82 --> 2935.00]  So then, which makes sense.
[2935.08 --> 2935.88]  It's like, okay, now we're ready.
[2935.96 --> 2938.00]  We think that this thing is basically where we want it.
[2938.06 --> 2938.50]  We don't need it.
[2938.54 --> 2946.58]  We're not going to use the simulation data to iterate, but we are going to, we want to validate effectively with our kind of final simulation run and get an idea.
[2946.58 --> 2960.34]  And so based on that, did we, I mean, it was, I know we were optimistic going in to actually getting this thing physically in hand, but there must always be some apprehension about something that has been forgotten in the simulation.
[2960.48 --> 2962.48]  Something we've neglected to account for and so on.
[2963.94 --> 2964.84]  No, we're perfect.
[2964.94 --> 2965.98]  And we never make mistakes.
[2966.62 --> 2967.02]  Nice.
[2967.12 --> 2967.56]  That's awesome.
[2967.68 --> 2968.58]  I was scared as hell.
[2969.80 --> 2970.24]  Totally.
[2970.24 --> 2970.36]  Totally.
[2971.56 --> 2988.42]  So then we, so we actually get the, Eric, I definitely want to, we got to tell the actual story of getting this backplane actually up because our, what we, we, we get our RevB sleds, Gimlet RevB sleds.
[2988.42 --> 2998.86]  And we, those of you who listened to our tales in the BringUp Lab, remember our tales of getting the Chelsea O'NIC brought up and the 499 ohm resistor.
[2999.46 --> 3003.46]  And the Gimlet sleds are, that's our compute sled into which the NIC is being plugged.
[3003.46 --> 3003.54]  Right.
[3003.64 --> 3003.72]  Yeah.
[3004.74 --> 3011.12]  And definitely an odyssey for a bunch of folks on that one.
[3011.16 --> 3013.36]  So go listen to that, that recounting there.
[3013.36 --> 3019.78]  But so we get the NIC up and it is, we're talking at, we're at 40 gigs.
[3019.96 --> 3025.46]  So which is to say, I think 10 gigabits per channel, but we can't get it to 28.
[3025.94 --> 3026.44]  Yeah.
[3026.56 --> 3031.30]  It bombs when it tries to go to 25 per lane, which is 100 gigs.
[3032.72 --> 3040.28]  And this is a tale of like data sheets and stuff screwing us up yet again.
[3040.28 --> 3044.32]  Well, no, because they were like, don't do this.
[3044.44 --> 3049.16]  And we said, okay, because you said, don't do this, we won't do it.
[3050.70 --> 3051.28]  All right.
[3051.32 --> 3052.80]  So we, yeah, go ahead.
[3052.86 --> 3053.52]  Tell the story, Eric.
[3055.20 --> 3066.06]  It turns out it, there was a lot of jitter coming out of it and we can measure that jitter using the very nice lab master scope.
[3066.06 --> 3072.54]  We had from Teledyne and we saw this just horrific jitter on the, like way more than we expected.
[3073.62 --> 3074.10]  And we're like, okay.
[3074.22 --> 3081.84]  And jitter, jitter is essentially the, the difference between when we expect an edge to show up, you know, a transition and when it actually shows up.
[3081.88 --> 3083.32]  And that's measured in seconds.
[3083.70 --> 3088.92]  And that's, you know, usually pico seconds if it's bad and femtoseconds if it's pretty good.
[3088.92 --> 3090.08]  So femtoseconds.
[3090.68 --> 3091.64]  Femtoseconds, yeah.
[3091.68 --> 3091.84]  Yeah.
[3092.12 --> 3093.40]  E-m-i-f-15.
[3093.40 --> 3093.68]  Yeah.
[3094.58 --> 3100.22]  So if you think this is an expensive device to measure this, by the way, you're right.
[3100.78 --> 3101.34]  It is.
[3101.82 --> 3104.38]  If you want to mortgage your house, you could probably get a down payment.
[3105.38 --> 3105.62]  Yeah.
[3105.62 --> 3110.70]  So the, and so this is a Teledyne, Teledyne LaCroix scope, right?
[3110.84 --> 3111.82]  If I remember correctly.
[3112.24 --> 3116.48]  And this is a lab master, 36 gig lab master, I think.
[3117.16 --> 3120.86]  And, and these are like half a million bucks plus basically.
[3120.96 --> 3121.24]  Oh yeah.
[3121.74 --> 3122.54]  They're gorgeous.
[3124.54 --> 3127.18]  They're the cat's meow high speed scopes.
[3127.18 --> 3132.60]  And these are things that you, that, I mean, we're, I think we're still, we're saving up
[3132.60 --> 3137.42]  our allowance to buy, but you, you rent, or in this case, I think Teledyne LaCroix was
[3137.42 --> 3141.10]  very, that was very helpful in terms of, of letting us eat our unit.
[3141.42 --> 3144.12]  And we, this was, this was the first hit of crack they gave us.
[3144.22 --> 3145.06]  And now, now we're hooked.
[3146.02 --> 3146.30]  Exactly.
[3146.46 --> 3147.12]  Well, they did a good job.
[3147.24 --> 3148.32]  No, they did this deliberate.
[3149.90 --> 3151.60]  But these things are super, super expensive.
[3151.70 --> 3153.90]  I mean, these things are, this is the kind of equipment.
[3153.90 --> 3154.40]  They're super good.
[3154.62 --> 3157.16]  I mean, that's what you have to have to look at a signal like.
[3157.18 --> 3157.94]  This in real time.
[3158.68 --> 3161.14]  And so we looked at this and saw a bunch of jitter.
[3161.26 --> 3162.72]  We're like, okay, where the hell is the jitter coming from?
[3162.82 --> 3163.32]  Is it power?
[3163.44 --> 3164.94]  Because of course everybody goes to power first.
[3165.40 --> 3166.28]  You know, of course it's power.
[3166.74 --> 3171.38]  So we looked at power and it's like, well, it's not really showing us anything that's
[3171.38 --> 3172.16]  really that bad.
[3172.28 --> 3173.56]  And it's like, okay, what the hell?
[3173.64 --> 3174.78]  Let's look at the input clock.
[3174.84 --> 3176.32]  And we thought the input clock was pretty good.
[3176.44 --> 3179.60]  And we measured it and it's not really that great either.
[3179.78 --> 3180.94]  Like, what the hell?
[3181.18 --> 3182.94]  Like, I thought we fixed this the last one.
[3184.30 --> 3187.06]  And so we're looking at the clock source and we're looking at the power.
[3187.06 --> 3187.76]  The clock source.
[3187.86 --> 3189.20]  We're looking at the power again.
[3189.98 --> 3192.94]  And it was looking fine.
[3193.20 --> 3196.18]  Like, there's some non-idealities which we're improving on the next one.
[3196.30 --> 3199.88]  We're like, okay, you know, this isn't, this isn't, there's like no, you know, smoking
[3199.88 --> 3200.56]  gun here.
[3200.90 --> 3201.98]  What the hell's going on?
[3201.98 --> 3206.38]  And it just like something that was always bothering me in the back of my head.
[3206.58 --> 3209.06]  Why in the hell doesn't this thing have a 100 ohm diff term?
[3209.78 --> 3215.30]  And a lot of chips have 100 ohm diff term internally for something like a clock input or even like
[3215.30 --> 3215.94]  high speed input.
[3216.10 --> 3220.26]  A lot of them just have 100 ohm terminations as part of their receiving structure, your
[3220.26 --> 3220.92]  receiver structure.
[3220.92 --> 3228.54]  But this one and the T6, if you put it into LVDS mode, it did not.
[3228.70 --> 3234.52]  What it did have is 4K bias resistors, which are also needed for LVDS, to power and ground.
[3234.64 --> 3236.34]  It did not have a 100 ohm diff term.
[3236.34 --> 3243.78]  And like, it's not particularly clear in the data sheet, like when you put it in this
[3243.78 --> 3246.98]  mode, here's what the input structure looks like, because of course they never tell you
[3246.98 --> 3247.24]  that.
[3247.94 --> 3250.34]  It's probably IP from some other company and whatever.
[3250.60 --> 3253.12]  So it's not spelled out.
[3253.18 --> 3255.22]  And it's like, well, all right, screw it.
[3255.28 --> 3256.58]  I don't know what the hell else to try.
[3256.66 --> 3258.54]  So I'm just going to try putting a 100 ohm diff term on there.
[3259.20 --> 3260.64]  I put a 100 ohm diff term on there.
[3260.88 --> 3265.40]  The clock looked, well, it still didn't look great, but it looked a lot better from Jitter.
[3265.40 --> 3267.08]  I'm like, okay, let's see.
[3267.48 --> 3268.24]  I'll break up.
[3268.36 --> 3268.62]  I'm like, great.
[3269.00 --> 3270.40]  You want to try firing this thing up?
[3271.08 --> 3271.94]  So he fires up.
[3271.98 --> 3274.40]  He's like, it just blinked.
[3275.16 --> 3275.88]  Like, what?
[3277.86 --> 3279.28]  It drained.
[3279.48 --> 3281.20]  I'm like, shit.
[3281.88 --> 3282.44]  That's right.
[3284.04 --> 3289.00]  So, I mean, the 499 ohm resistor that was the difference between life and death has now
[3289.00 --> 3293.04]  been trumped by the 100 ohm resistor between life and death.
[3293.04 --> 3298.36]  And the thing is, like, if you look at the dev board, their NIC that they have does not
[3298.36 --> 3300.66]  have a 100 ohm diff term on their LVDS clock.
[3301.70 --> 3308.32]  And my hypothesis for this, and this gets into transmission lines again, is the clock source
[3308.32 --> 3316.70]  on their NIC, on their physical, you know, like PCIe by 16 NIC is about a half an inch
[3316.70 --> 3318.30]  from their chip.
[3319.02 --> 3321.58]  Not even, maybe like a centimeter from their chip.
[3321.58 --> 3330.60]  And that, I think, is close enough that the edge rate of their source clock is not fast
[3330.60 --> 3332.42]  enough for that to be electrically long.
[3333.16 --> 3333.28]  Right.
[3333.38 --> 3337.84]  So even though they don't have termination, they never actually see the reflection because
[3337.84 --> 3342.76]  they don't actually have enough length to get a reflection developing.
[3342.76 --> 3345.04]  It's a poor explanation.
[3345.26 --> 3348.18]  They're basically coming short enough and, you know, electrically short.
[3348.30 --> 3352.18]  Like, if you put two completely mismatched things right next to each other, like, not
[3352.18 --> 3357.14]  all the energy will get there, but the signal will still look okay-ish.
[3357.78 --> 3357.92]  Yeah.
[3358.40 --> 3360.70]  And so, to be clear, this is on the clock, correct?
[3361.06 --> 3361.28]  Yes.
[3361.34 --> 3364.68]  This is on the clock input to the Ethernet NIC chip.
[3365.18 --> 3365.44]  Right.
[3365.44 --> 3369.16]  So this is what, and so the clock, and so Adam, I'm not sure if you got what the actual
[3369.16 --> 3373.50]  issue was, in terms that the clock was missing a terminating resistor.
[3374.18 --> 3377.66]  So it was, which I kind of view as a kind of an off-ramp.
[3378.00 --> 3382.54]  I mean, this is a bad way of thinking about it, but an off-ramp for the signal, as opposed
[3382.54 --> 3383.98]  to just kind of bonking in.
[3385.16 --> 3388.50]  And so we were getting, effectively, reflection on the line.
[3389.26 --> 3395.36]  And the spec sheet said specifically not to put a resistor?
[3396.44 --> 3397.22]  They said.
[3397.70 --> 3398.82]  They said.
[3399.04 --> 3400.12]  Oh, no, you don't need that.
[3400.68 --> 3400.90]  Yeah.
[3401.38 --> 3405.92]  So, I mean, this is one of the things where it's like, you don't need that because it's
[3405.92 --> 3406.32]  so short.
[3408.02 --> 3411.38]  Well, and this is where you get to something that I feel we've learned again and again
[3411.38 --> 3411.72]  and again.
[3412.02 --> 3416.36]  When you don't necessarily build from first principles and you have a reference design,
[3416.66 --> 3420.24]  you don't really know what's working by accident there.
[3420.24 --> 3426.40]  And in this case, they were speaking kind of their truth, which is, hey, in the designs
[3426.40 --> 3430.86]  that we have built where the clock is super close to the part, we haven't needed it.
[3431.40 --> 3434.34]  What they don't know is like, well, actually, you may have needed it.
[3434.38 --> 3435.92]  You just were kind of getting away with it.
[3436.12 --> 3437.34]  It was kind of working by accident.
[3437.34 --> 3438.44]  Well, not just that.
[3438.56 --> 3444.24]  If they actually added it on their nick, their input clock might have less jitter, meaning
[3444.24 --> 3447.92]  their PLL does better, their certies will do better, and therefore, actually, you can
[3447.92 --> 3452.80]  extend your cable a little bit more because you're eating less into the budget of your
[3452.80 --> 3453.76]  bid periods.
[3453.76 --> 3457.24]  So I feel like this is kind of a punchline we've got to work up to.
[3457.34 --> 3459.88]  And then, Andrew, I want to get you in here as well because I know you've been looking
[3459.88 --> 3463.94]  at some of the scope output that we've been able to get you.
[3465.80 --> 3467.84]  So, yeah, what did it look like?
[3467.90 --> 3469.62]  Once we got that, we've done all the simulate.
[3469.74 --> 3472.34]  We've done the paperwork to roughly verify it.
[3472.38 --> 3477.26]  We've done the simulation, the iteration with the simulation on the layout, the big simulation
[3477.26 --> 3480.46]  multi-week to verify that it's going to be, we think this is plausible.
[3480.46 --> 3483.38]  We find the missing 100-ohm resistor on the clock.
[3483.50 --> 3484.86]  We get that resolved.
[3485.66 --> 3488.70]  And what does it look like end-to-end?
[3490.28 --> 3491.36]  It's gorgeous.
[3495.70 --> 3497.78]  It's still better from Tofino.
[3498.12 --> 3501.06]  That chip is still putting out gorgeous, gorgeous signals.
[3501.90 --> 3510.14]  But even from the T6 going out and some 9-indiality, you don't expect the CNI.
[3510.46 --> 3517.02]  Honestly, looking at these things, because the signal is usually so degraded and so crappy
[3517.02 --> 3523.58]  that the only prayer you have seeing anything reasonable is by enabling every equalization
[3523.58 --> 3525.46]  method known to man on your receiver.
[3527.42 --> 3528.54]  Sorry to ask.
[3528.96 --> 3530.34]  What is equalization?
[3530.60 --> 3530.88]  I'm sorry.
[3531.02 --> 3531.80]  Equalization is...
[3531.80 --> 3532.20]  What's that mean?
[3532.20 --> 3539.32]  There's a couple of mathematical things that they can do to boost the high frequencies,
[3539.52 --> 3542.62]  essentially, in a very poor man's description.
[3544.00 --> 3547.02]  Like they were saying, the channel is a low-cast filter.
[3547.20 --> 3552.64]  So you send a nice high-frequency signal out, and you send it to a channel that ends up with
[3552.64 --> 3558.14]  a low-cast filter, and you get a much more attenuated signal coming out of the receiver.
[3558.30 --> 3562.86]  Well, the receiver knows that there's generally some characteristic of that, and there's mathematical
[3562.86 --> 3568.76]  ways of boosting that lost high-frequency information.
[3569.24 --> 3569.64]  Got it.
[3569.64 --> 3571.52]  Again, that's one of the methods.
[3571.76 --> 3574.86]  There's DFE, which is decision feedback equalization.
[3575.36 --> 3578.00]  There's FFE, which is forward equalization.
[3578.24 --> 3579.48]  I think that might be on the channel better.
[3579.96 --> 3583.04]  But that's not my area of expertise.
[3583.04 --> 3589.68]  You basically try to amplify specific frequencies again that you care about that are in relation
[3589.68 --> 3599.24]  to your fundamental frequency in the hopes that you can, by basically artificially making
[3599.24 --> 3605.18]  these values bigger by amplifying this, you can recover more of the original signal.
[3605.18 --> 3614.18]  Yeah, that's part of that really fancy scope is having things like CTLE, DFE, et cetera, that
[3614.18 --> 3616.18]  can do those kinds of equalizations.
[3616.98 --> 3617.58]  Right.
[3618.06 --> 3621.00]  Like the chip does, because you can't actually probe.
[3621.36 --> 3624.18]  Well, it's impractical to probe on the die.
[3624.66 --> 3625.02]  Right.
[3625.12 --> 3632.22]  You have to probe somewhere else and then figure out what it looks like at the die based on
[3632.22 --> 3632.70]  that measurement.
[3632.70 --> 3640.34]  And Eric, maybe now is a good time to mention the probe station that you built, which I think
[3640.34 --> 3640.90]  is pretty neat.
[3641.86 --> 3642.20]  Sure.
[3642.36 --> 3642.50]  Yeah.
[3642.98 --> 3647.60]  The probe station is just, it's a collection of off-the-shelf parts from either Thor Labs
[3647.60 --> 3650.76]  or Misumi or Mastercar.
[3651.72 --> 3658.50]  And its entire purpose in life is to hold microwave probes, which are basically coax, pieces of
[3658.50 --> 3664.86]  coax that are very, very small, that have very pointy tips that are bolt-plated, that touch
[3664.86 --> 3668.68]  down on a circuit board to try and measure the channel.
[3668.68 --> 3671.36]  And they're absurdly delicate.
[3671.76 --> 3678.62]  They're very, very sensitive to movements and vibration and things because they are very,
[3678.72 --> 3679.18]  very delicate.
[3679.66 --> 3684.04]  And they're basically designed for probing wafers that are perfectly flat and, you know,
[3684.56 --> 3684.86]  perfect.
[3685.60 --> 3686.08]  Right.
[3686.08 --> 3691.48]  But we're using them to probe this, like, horrific, like, mountainous landscape and
[3691.48 --> 3691.94]  PCB.
[3693.54 --> 3699.42]  And so you need some sort of mechanism to hold the board steady, support it, and then hold
[3699.42 --> 3704.78]  the probe steady and get them into whatever position you need them to interface with your
[3704.78 --> 3708.54]  BGA pattern or your connector pattern or whatever it is.
[3708.54 --> 3717.30]  And hold them very still for extended periods of time while the system does its thing and
[3717.30 --> 3718.20]  does all of its measurements.
[3719.02 --> 3719.14]  Right.
[3720.02 --> 3725.08]  And this is the actual literal probe effect that we are, I mean, right.
[3725.74 --> 3728.80]  Not distorting the system while we probe it is really, really challenging.
[3729.46 --> 3733.62]  And also getting a good, like, connection between the probe and the system is really damn difficult.
[3734.94 --> 3737.58]  And so, you know, there's all sorts of stuff you have to deal with that.
[3737.58 --> 3741.58]  But basically, the systems that we looked at that were commercial were either...
[3742.44 --> 3744.56]  Expensive or expensive?
[3744.76 --> 3746.70]  Well, expensive or expensive.
[3747.52 --> 3753.62]  Even if they were really expensive, they were only able to do, like, one board at a time
[3753.62 --> 3754.36]  and we needed two.
[3754.90 --> 3755.20]  Right.
[3755.76 --> 3758.18]  And so I'm like, screw this.
[3758.22 --> 3758.82]  This is stupid.
[3759.44 --> 3761.10]  Like, somebody should just make one of these things.
[3761.34 --> 3762.22]  So I just made one.
[3762.36 --> 3765.04]  And in my previous job, I was in the verge of making one anyway.
[3765.04 --> 3767.10]  So I kind of had a little plan in my mind.
[3767.58 --> 3769.50]  And there's certainly things to improve upon it.
[3769.84 --> 3773.40]  And it's, you know, not great, not perfect.
[3773.82 --> 3777.82]  But eventually, I get a free moment, which is in short supply lately.
[3777.96 --> 3781.84]  But when I get a free moment, I will publish the design and open source it.
[3782.08 --> 3783.60]  And people can do with it what they will.
[3783.60 --> 3789.84]  But there's some feedback that Tom has given in such to make it better that I haven't
[3789.84 --> 3791.18]  getting anything for it yet either.
[3791.18 --> 3798.10]  And I think this is a very common oxide theme that I was on the verge of making one in my
[3798.10 --> 3798.88]  previous job.
[3798.88 --> 3803.20]  I think is, like, true for many different kinds of one in many different kinds of jobs.
[3803.30 --> 3806.48]  I feel like, Ari, do you think that that's kind of a common theme across the company is
[3806.48 --> 3810.08]  that everyone has kind of come here with a tip on their shoulder about the kinds of things
[3810.08 --> 3813.64]  that they are either sick of paying too much for or want to do on their own?
[3813.64 --> 3816.26]  That is definitely a theme.
[3816.44 --> 3818.62]  I sort of was guilty of that, too.
[3819.16 --> 3819.76]  Oh, no.
[3820.04 --> 3821.80]  Oh, I mean, I'm not speaking mechanistically.
[3822.02 --> 3824.74]  I mean, this is true of, you know, that we've done our own operating system.
[3824.84 --> 3826.34]  We've done our own, like, lots of things.
[3826.60 --> 3831.42]  I think almost to a person, and often when it comes to stuff like this, where it's like
[3831.42 --> 3837.64]  tooling, where it's like, at no other company, in no other position, could I make the justification
[3837.64 --> 3841.18]  of, like, we'll spend too much and get the wrong thing.
[3841.18 --> 3846.60]  And this is a great example where now we're building this thing that is totally fit to
[3846.60 --> 3850.86]  purpose, and in places where it's not, you know, it's our design, and we can fix it.
[3851.28 --> 3855.16]  Yeah, I got to say, like, if I had, like, one piece of technology leadership advice, if
[3855.16 --> 3858.68]  anyone on your team wants to build their own tooling, you should always let them.
[3858.82 --> 3864.50]  I mean, I just, like, because in general, the people who want to build their own tooling
[3864.50 --> 3869.10]  have already kind of thought through the problem well enough that it is almost certainly not
[3869.10 --> 3870.96]  ill-advised just because they're asking the question.
[3870.96 --> 3873.52]  I mean, we know the things that we're not going to build on our own, right?
[3873.56 --> 3876.76]  We know the things that are, that, you know, that does exist.
[3876.88 --> 3879.14]  There are things that we're not going to build on our own, but...
[3879.14 --> 3879.64]  Not yet.
[3879.92 --> 3880.82]  Not yet, exactly.
[3882.60 --> 3883.20]  Larry, don't worry.
[3883.26 --> 3883.68]  Not simulation.
[3883.90 --> 3885.16]  Simulation software is not on the list.
[3885.34 --> 3885.94]  No, no, no.
[3885.94 --> 3887.82]  The simulation software is safe.
[3889.50 --> 3890.96]  But the...
[3891.62 --> 3895.70]  And so, and Eric, so with this, with the probe station, we are able to actually...
[3895.70 --> 3898.80]  Because the thing I love about the probe station is it is strictly mechanical.
[3898.80 --> 3902.32]  There's no kind of a fancy robot arm here.
[3902.48 --> 3903.80]  This is like...
[3903.80 --> 3905.62]  No, that's not cost too much.
[3906.10 --> 3906.40]  Right.
[3907.00 --> 3907.40]  Right.
[3908.54 --> 3913.24]  It's a mechanical system, and there's a little, like, you know, a little microscope that plugs
[3913.24 --> 3919.04]  into a TV that I use, and you can lower it down and use knobs on three-axis things.
[3919.04 --> 3923.46]  And there's one feature on it that is, like, the one unique feature of the entire system
[3923.46 --> 3928.12]  in the fact that you can adjust the plenarity of the probe, which is basically that you have
[3928.12 --> 3932.56]  these four very sharp, delicate points that have to touch down at the exact same time.
[3932.88 --> 3936.60]  And inevitably, like, nothing is in the same plane.
[3936.60 --> 3942.56]  So you have to adjust those four probes to be the right angle to touch down your board
[3942.56 --> 3943.64]  all at the same time.
[3944.58 --> 3951.54]  And the method I use adjusts that plenarity or that angular mismatch and adjusts that
[3951.54 --> 3953.02]  without actually moving the tip.
[3953.50 --> 3955.02]  It is not very common.
[3955.76 --> 3959.34]  And I haven't been able to find it in any other probe station that I've worked at.
[3960.44 --> 3960.92]  Yeah.
[3961.14 --> 3963.38]  The one salient feature, which...
[3963.38 --> 3963.58]  Yeah.
[3963.96 --> 3964.92]  Well, that is cool.
[3965.02 --> 3966.16]  And I'm looking forward to getting the...
[3966.16 --> 3968.98]  I mean, it's going to be fun to get kind of your plans out there,
[3969.18 --> 3973.58]  and it's an open source or whatever, and I'll let people go wild.
[3974.76 --> 3977.58]  So we're gathering the data, and it's looking good.
[3977.70 --> 3981.56]  And Andrew, I know we were feeding a bunch of this data that was coming off the Teledon
[3981.56 --> 3986.14]  and LaCroix scope to you for some of the stuff that you've done on your GLScope client.
[3986.22 --> 3987.86]  Do you want to describe some of that work?
[3987.92 --> 3989.02]  Because it's really interesting stuff.
[3990.62 --> 3991.02]  Yes.
[3991.02 --> 3997.22]  So speaking of let your engineers build tools, that's a policy I firmly subscribe to as well.
[3997.88 --> 4003.02]  So for those of you who aren't familiar with GLScope client, it's an open source application
[4003.02 --> 4010.42]  that is essentially a user interface and front end for oscilloscopes and now starting to branch
[4010.42 --> 4013.18]  out into more content heads with multimeters, network analyzers, and so on.
[4013.22 --> 4014.80]  But for the most part, oscilloscopes.
[4014.80 --> 4021.80]  And it consists of an object-oriented library LibScope how that provides an API to oscilloscopes,
[4021.96 --> 4024.40]  and then oscilloscopes on itself is the UI in front of it.
[4024.68 --> 4027.80]  So I can connect to a Rigel.
[4027.88 --> 4029.30]  I can connect to a LaCroix.
[4029.38 --> 4033.82]  I can connect to a Siglin and have the same user interface in front of it, the same C++ API in front of it.
[4033.82 --> 4036.80]  I can load waveform data from a file coming from any of these scopes.
[4036.80 --> 4045.84]  And so that's how Eric and company were sending me the data from the lab master is they were taking the files off of the scope,
[4045.96 --> 4051.66]  exporting it to LaCroix's waveform format, sending them over to me, and then I would load the .trc file
[4051.66 --> 4056.04]  and then process that waveform in exactly the same user interface as if I was sitting in front of a scope.
[4056.04 --> 4061.96]  So just to repeat this, to kind of say this back to you, I think this is pretty amazing.
[4062.48 --> 4066.98]  You have implemented effectively the front end on this thing, so you can take data from our scope
[4066.98 --> 4069.62]  and pull it up on your own virtual scope and manipulate.
[4069.88 --> 4071.48]  Is that a fair summary?
[4072.98 --> 4075.48]  I can acquire data from any source node.
[4075.58 --> 4077.62]  So it's built around a filter graph architecture.
[4077.62 --> 4082.38]  If you're used to GNU radio or any kind of like audio processing pipelines and stuff like that.
[4082.38 --> 4089.28]  So the source node can be a physical instrument or it can be a block that loads data from a file.
[4089.40 --> 4091.28]  It can be a block that creates synthetic data.
[4091.68 --> 4093.78]  So we were talking about simulations earlier, for example.
[4094.28 --> 4103.04]  So a very common use case is to create a synthetic step waveform and then import channel response data as S parameters.
[4103.04 --> 4109.62]  And then you could apply channel emulation to that in order to see what either the more word time domain transmission response
[4109.62 --> 4117.72]  or the reflected time domain reflectometer response would look like given channel data from, say, an S prep, sorry, from a touchstone file.
[4117.86 --> 4121.06]  But you could also do the same thing with, say, live data coming off the VNA.
[4121.28 --> 4121.86]  You can have that.
[4121.86 --> 4123.68]  The system just cares.
[4123.80 --> 4127.18]  The input to this filter block is a magnitude channel and an angle channel.
[4127.26 --> 4133.86]  And it doesn't care whether that channel came from a file or whether it came from VNA or whether you generated it from some arbitrary simulation.
[4134.14 --> 4136.62]  It's just data flowing into blocks and flowing out of blocks.
[4137.24 --> 4137.82]  That is really cool.
[4138.00 --> 4143.00]  And I gather that are these formats always open?
[4143.36 --> 4149.94]  Or I mean, it feels like there would be some temptation for bad vendor behavior in here that you must have sidestepped.
[4149.94 --> 4159.84]  So vendors in general have been incentivized to provide APIs for equipment because production test automation and things like that are, you know,
[4159.90 --> 4165.86]  so many people buy scopes to tool up production lines in factories and test some product.
[4165.96 --> 4168.82]  And you just need to go trigger on the same event over and over again.
[4168.86 --> 4172.92]  You know, once every five seconds, a new thing comes down the assembly line, goes down to a bunch of pogo pins.
[4173.14 --> 4174.30]  You run a bunch of waveforms.
[4174.32 --> 4176.50]  You make sure it meets spec, comes off, you do the next one.
[4176.54 --> 4177.50]  You have to be able to script that.
[4177.50 --> 4184.56]  The problem is the previous state of the art had been using ASCII text commands that were all instrument specific in order to be able to script.
[4185.90 --> 4188.62]  So Libscope Howell does away with all of that.
[4188.70 --> 4191.66]  It is still using that same API under the hood to connect to the instrument.
[4192.02 --> 4199.46]  But it presents a unified vendor agnostic C++ API to you as the end user.
[4199.46 --> 4210.48]  So you can write code against an abstract oscilloscope that has four channels and a sample rate of at least 20 giga samples per second and a bandwidth of at least two gigahertz and supports a positive edge trigger.
[4210.74 --> 4214.28]  You can write your test case against that minimum set of requirements.
[4214.28 --> 4219.48]  And then any oscilloscope object that you are given will work with it and you don't care what it is.
[4219.88 --> 4220.42]  That's very cool.
[4220.76 --> 4221.46]  That is very cool.
[4221.54 --> 4221.70]  Yes.
[4221.94 --> 4231.92]  You can connect to several scopes and it's got a feature that allows you to probe a common test point with one channel from scope A and one channel from scope B.
[4231.92 --> 4235.60]  And then look at the delta between them.
[4235.64 --> 4237.96]  It will calibrate out the phase shift in your trigger cable.
[4237.96 --> 4243.84]  So now you can view the same, say, eight channels, four from one scope and four from another scope in one user interface.
[4244.44 --> 4247.82]  And then can you describe some of the data that Arian and Eric got to you?
[4247.90 --> 4251.56]  Because I was really – I loved what you were doing with it, but I didn't understand it.
[4253.58 --> 4255.78]  So, again, we're talking about the filter graph.
[4255.88 --> 4258.94]  And so the entire architecture application is built around this.
[4258.94 --> 4267.54]  You take a series of data sources, you apply a transformation to them, and you visualize the output of that transformation or use it as the input to other blocks.
[4267.70 --> 4272.78]  And you don't necessarily have to be seeing plots of every intermediate result, although you can if you want to.
[4273.36 --> 4282.34]  And so in this case, the main data set that I was looking at a lot was a QSIGMI link, so quad serial gigabit media independent interface.
[4282.34 --> 4289.46]  It is four lanes of up to gigabit that are timeshared on a single physical bus.
[4289.88 --> 4302.04]  So the individual lanes are running at 1.25 gigabit per second, and it's pretty much just round robin send one 10-bit symbol from lane zero, send one symbol from lane one, send one symbol from lane two.
[4302.12 --> 4303.34]  And then they just all take turns.
[4303.34 --> 4310.92]  And then there's a few little tweaks to the encoding because, you know, you need to know those four lanes corresponds to which physical port and so on.
[4310.98 --> 4317.40]  So they change the idle character in lane zero in order to let you know this is lane zero so you can keep them synced.
[4318.08 --> 4322.68]  And, Matt, this was – because folks may be confused where this particular network was coming from.
[4322.74 --> 4328.32]  That was using this high-speed scope that we used for the high-speed back lane, but that's on the management network, right, Matt?
[4328.32 --> 4331.62]  Yes, this is actually taking a couple steps down in speed.
[4331.76 --> 4336.00]  So this is a six-gibb link, the 28-gibb link that's the main back lane.
[4336.36 --> 4340.02]  This is running between all of the servers, all of the service processors.
[4341.20 --> 4356.34]  Yeah, so what's actually going on is there are 400 megabit, I believe, at the far end, but they are multiplied up to one gigabit because the link actually has a minimum data rate it can run at.
[4356.34 --> 4362.46]  And so the way that serial gimme works is if you have data going at one gig, you send each byte in sequence.
[4362.72 --> 4365.68]  If you have data going at 100 meg, you send each byte 10 times.
[4365.76 --> 4367.98]  If you have data going at 10 meg, you send each byte 100 times.
[4368.36 --> 4374.00]  And so you always end up having the same data rate over the link just because some of this hardware doesn't like running too slow.
[4374.56 --> 4383.86]  Anyway, so once you have these streams of bytes coming from each of these four links, again, you just interleave them, send them four times as fast, and the bytes take turns and so on.
[4383.86 --> 4398.22]  Anyway, so the nice thing is that the signaling within each of these lanes is, again, serial gimme, which is essentially regular gigabit Ethernet, 1000 base KX or base SX and so on, same line code, other than the support for 10 hundred.
[4398.70 --> 4410.42]  And so we were able to write a – we had an existing filter block in Jellscope Client that recovers the clock from the link, another one that takes the analog waveform and thresholds it to give you a digital waveform.
[4410.42 --> 4423.12]  Then you feed the recovered clock and the digital data into another filter block that decodes 8B10B, and then that gives you a sequence of control characters or data bytes.
[4423.54 --> 4434.38]  And then you can feed that into the new block that I wrote to work with this data, which just takes in a stream of 8B10B symbols and outputs four additional streams of 8B10B symbols at one quarter of a rate.
[4434.38 --> 4441.36]  So it determines which lane is lane 0 because that one has the K28.1 instead of K28.5 as the idle character.
[4442.70 --> 4450.34]  And then it – so once it's recovered the sync and it knows which lane is lane 0, then it just takes all the incoming data.
[4450.74 --> 4452.16]  Again, round robins it.
[4452.28 --> 4454.10]  Okay, you're lane 0, you go out this port.
[4454.26 --> 4455.34]  You're lane 1, you go out this port.
[4455.50 --> 4457.88]  And it creates four streams of data at one quarter of a rate.
[4458.12 --> 4459.66]  Then you can take those data streams.
[4459.66 --> 4463.00]  You can feed them to individual protocol decoders for a serial gimme, for example.
[4463.40 --> 4465.14]  And that will then decode up to Ethernet frames.
[4465.22 --> 4468.66]  You can then apply another decode on the end of that that decodes, say, IP before headers.
[4468.82 --> 4473.20]  Or you can add a sync node that outputs to a PCAP file and look at a Wireshark.
[4473.20 --> 4485.76]  So you can cascade all these different filter blocks independently in any order you want, depending on what kind of application you have.
[4486.44 --> 4486.84]  Exactly.
[4486.98 --> 4488.50]  They are wrongly typed.
[4488.68 --> 4496.46]  So, for example, and this does confuse some new users, and it's something that we'd like to work on as far as making the GUI kind of infer type conversions a little bit.
[4496.46 --> 4505.60]  So, for example, it is illegal to apply a RS-232 protocol decode to an analog signal because RS-232 is a digital protocol that expects a digital input.
[4506.06 --> 4511.78]  And so you first have to apply a threshold filter to convert your analog NRZ signal into a digital signal.
[4512.10 --> 4518.04]  And once you have a waveform of type bool rather than of type float, you can then apply the RS-232 decode to that and so on.
[4518.62 --> 4523.94]  But, yes, so as long as your input is legal for the data type that the filter block expects, you can cascade them arbitrarily.
[4523.94 --> 4531.60]  You can basically make an arbitrary decoder for any kind of data you want based on the data that you have.
[4531.76 --> 4534.56]  Like, okay, I have some arbitrary AP10B thing.
[4534.72 --> 4536.52]  So I'm going to put a CDR block in there.
[4537.00 --> 4538.94]  And then I'm going to put a, you know, threshold ring.
[4539.14 --> 4540.78]  All those kinds of blocks in series.
[4540.94 --> 4547.44]  And I can basically have a pretty good start to a custom protocol decode for anything you want.
[4547.44 --> 4550.62]  The underlying libraries are all open source.
[4550.94 --> 4552.44]  There is a plug-in model.
[4552.44 --> 4560.70]  So if you make your own decoder that you don't want to release, it is completely impossible to make a binary blob protocol decode that fits into this API.
[4560.96 --> 4565.46]  Now, right now, since this is still kind of a work in progress, there's no binary stability.
[4565.64 --> 4570.02]  So releasing a blob would be ill-advised because five commits later probably won't run anymore.
[4570.38 --> 4572.32]  But architecturally, it is possible.
[4572.32 --> 4579.96]  Anyway, so you can write your decode as a plug-in or compile it into the main code base and, you know, submit a power request for it as upstream and so on.
[4580.30 --> 4587.98]  But now your decode, so let's just say hypothetically, you could make a decode for, say, gigabit ethernet, which we have already.
[4588.06 --> 4589.14]  But say you're writing a new one.
[4589.36 --> 4594.74]  You could write a decode that would take in AP10B objects and spit out ethernet frame objects.
[4594.74 --> 4596.30]  And then you could take your new decode.
[4596.36 --> 4597.46]  This is what we did here, actually.
[4597.84 --> 4600.14]  So I've written the decode for serial gimme.
[4600.48 --> 4607.62]  And then since that output of ethernet frame objects, I could take the output of that block and feed it into, say, the IPv4 decode that I already had.
[4607.66 --> 4607.84]  Yeah.
[4608.12 --> 4613.98]  Because as long as that data type, the next stage doesn't care that this is a filter I just wrote.
[4614.16 --> 4615.28]  It just sees ethernet frames.
[4615.32 --> 4616.22]  And it's like, oh, ethernet frames.
[4616.28 --> 4616.92]  I know what to do with those.
[4616.92 --> 4619.70]  Yeah, that is really cool.
[4619.96 --> 4625.64]  And I think Matt has got a great blog entry from, Matt, what was that?
[4625.70 --> 4626.28]  Two weeks ago?
[4626.64 --> 4627.12]  A week ago?
[4627.12 --> 4627.82]  I can't even remember.
[4628.00 --> 4629.28]  All the time is blowing together.
[4630.62 --> 4633.16]  Yeah, it looks like it was two weeks ago or something like that.
[4633.34 --> 4639.48]  But a great blog entry on going from the scope to the actual Wireshark output.
[4639.82 --> 4644.20]  Yeah, Larry, I'm not sure if you realize this, but we're actually doing, we're not actually just building one switch.
[4644.20 --> 4646.86]  We're building, well, at least two, arguably three.
[4647.96 --> 4654.14]  We've got our main switch has got a lower speed switch on it for the management network.
[4654.26 --> 4658.22]  So we were actually doing a bring up of two switches, not just one.
[4658.34 --> 4660.64]  So it's been exciting times around here.
[4662.60 --> 4670.82]  So one of the, Eric, I want to get back to one of the things you were saying about, you know, get this whole thing up and it looks pretty glorious.
[4670.82 --> 4674.36]  And Larry, in particular, a question for you.
[4674.46 --> 4679.12]  How often do you kind of go back to like, okay, we've simulated this.
[4679.54 --> 4681.12]  Let's go to the actual built artifact.
[4681.64 --> 4684.84]  And how did it work out?
[4687.04 --> 4687.90]  Well, that's interesting.
[4688.06 --> 4696.50]  I mean, well, maybe my colleague, Robert, who's also on the line, could tell you a bit more war stories out of the trenches of doing these things themselves at Microsoft.
[4696.50 --> 4707.10]  But, yeah, usually it's as I'm hearing on this call is it's you keep working at it until you make it work.
[4708.38 --> 4711.84]  You know, there's a lot of that happens and things come up, right?
[4711.90 --> 4714.82]  Oh, I didn't terminate a particular transmission line.
[4714.90 --> 4716.08]  I need to add a different resistor.
[4717.04 --> 4718.82]  You know, and the vendor didn't tell me to do that.
[4718.82 --> 4723.56]  You know, there's a lot of physics going on and they're not going to cover all those cases.
[4723.74 --> 4726.56]  And that's why simulation comes around and is useful.
[4727.04 --> 4732.88]  Going back and doing the sort of postmortem, I suppose, is what you're asking.
[4733.36 --> 4737.24]  I think that there are, you know, a lot of our longtime customers that have been doing this.
[4737.24 --> 4742.90]  They they've come to rely on the software and get good at it if you're doing it all the time.
[4742.90 --> 4750.68]  And then you then, you know, you you you get that faith in what what the software can do and what you're doing.
[4750.74 --> 4755.30]  The software will tell you exactly the answer precisely for what you said to it.
[4755.38 --> 4760.40]  But whether or not that matches the network that you're designing in reality is another story.
[4760.52 --> 4763.76]  If you fended a pile of crap, it'll give you an answer based on that pile of crap.
[4764.22 --> 4765.20]  And it'll be right.
[4765.40 --> 4765.54]  Right.
[4765.66 --> 4766.02]  Exactly.
[4766.02 --> 4766.64]  It'll be right.
[4766.64 --> 4767.90]  But you fended a pile of crap.
[4767.90 --> 4769.72]  And that's why a lot of people spend a lot.
[4770.60 --> 4771.34]  Yeah, go ahead, Robert.
[4772.66 --> 4777.22]  I was just going to say that's why a lot of people do spend a lot of time doing simulation measurement correlation,
[4777.22 --> 4784.06]  because a lot of times you might need to tune some of the parameters of your simulation model to get to match where you're seeing in reality.
[4784.06 --> 4784.26]  Right.
[4784.60 --> 4787.20]  You know, you might get a certain dielectric constant from a vendor,
[4787.36 --> 4793.62]  but that might not actually be the actual value you need to use in the simulation to get everything to nicely align.
[4794.26 --> 4794.48]  Yeah.
[4794.48 --> 4801.44]  Or you're getting weave effect, which you didn't necessarily model, because that requires a whole hell of a lot more simulation time.
[4801.44 --> 4803.98]  Yeah.
[4803.98 --> 4807.36]  And even if you have surface roughness, how do you account for that?
[4807.44 --> 4809.64]  Are you accounting for too much of it or not enough?
[4809.68 --> 4809.80]  Yeah.
[4809.88 --> 4810.44]  I was just going to say...
[4810.44 --> 4811.58]  There's a lot of different factors.
[4812.06 --> 4823.46]  Surface roughness is like one of the most poorly specified things from the vendor and requires really everybody to characterize it for themselves, pretty much, as far as I know.
[4823.46 --> 4823.70]  Okay.
[4823.70 --> 4824.02]  Okay.
[4824.14 --> 4825.32]  So surface roughness.
[4825.42 --> 4826.92]  I mean, this feels like...
[4826.92 --> 4828.42]  Zoom so...
[4828.42 --> 4829.40]  So my copper happens.
[4829.84 --> 4830.10]  Yeah.
[4830.20 --> 4838.50]  The issue is that, for one, there's a thing called skin effect, which is the higher and higher frequency you're transmitting across copper,
[4839.00 --> 4842.50]  the electrons skate across closer and closer and closer to the surface.
[4842.50 --> 4848.88]  And at the frequencies we're talking about, the skin depth is microns, microns deep on the surface of the copper.
[4849.08 --> 4860.32]  So that means the resistance loss in the transmission line that you're calculating or losing across the entire transmission line depends on what that surface looks like.
[4860.40 --> 4863.32]  It's not a nice, polished, perfect piece of copper.
[4863.32 --> 4871.40]  It's actually intentionally rough on one side in order to improve adhesion to the epoxy layer.
[4871.82 --> 4872.48]  Oh, man.
[4873.18 --> 4873.36]  Right.
[4873.54 --> 4876.50]  So they make it rough on purpose on one side.
[4876.62 --> 4877.98]  They polish on another.
[4877.98 --> 4888.80]  So that is also why you want to create your stack up in a way that you want to more closely bias the polished side so that most of your losses are sitting there.
[4888.80 --> 4895.04]  It's all these details that you've got to dig into and understand and how you're constructing the whole shebang.
[4895.60 --> 4895.72]  Yeah.
[4895.84 --> 4903.58]  And like your idealized notion of a trace being the perfect little rectangle that sits above and below infinite ground length is also a part.
[4903.94 --> 4904.28]  Oh, yeah.
[4904.56 --> 4905.14]  Your trace is actually a trapezoid.
[4905.14 --> 4906.20]  Trapezoidal effects.
[4906.50 --> 4907.08]  Yeah, exactly.
[4907.36 --> 4911.38]  Or if it's on the surface, it's a trapezoid with maybe an inverted trapezoid on top of that.
[4912.40 --> 4912.80]  Plating.
[4913.00 --> 4913.36]  Exactly.
[4913.58 --> 4914.26]  Yeah, there's a lot.
[4914.26 --> 4918.44]  And then you get the skin effect and you get the fact that you use Enig.
[4918.68 --> 4918.98]  Right.
[4919.54 --> 4921.78]  Nickel is actually pretty crappy for RF.
[4922.08 --> 4923.08]  And it's magnetic.
[4923.52 --> 4924.54]  And it's magnetic.
[4924.86 --> 4925.04]  Yeah.
[4925.40 --> 4932.42]  More other problems, which is why we don't use microstrip or externally on any of these high-speed traces.
[4933.70 --> 4936.26]  Nickel has a really shallow skin depth compared to copper.
[4936.46 --> 4938.46]  And so not only is – well, it's not even pure nickel.
[4938.58 --> 4940.02]  It's nickel, phosphorus, alloy.
[4940.02 --> 4945.34]  They have to add phosphorus to it so it will plate better, and I think it affects the mechanical properties a little bit too.
[4945.82 --> 4949.44]  And so you've got your nickel phosphorus plating on top of your copper.
[4949.66 --> 4952.22]  So now it's got a shallower skin depth.
[4952.36 --> 4955.38]  So your signal is traveling in less material than it would if it was pure copper.
[4955.70 --> 4958.30]  And the resistivity is about four times higher than copper.
[4959.42 --> 4961.46]  Which is why we do microstrip only.
[4961.82 --> 4962.68]  Sorry, strip only.
[4962.68 --> 4964.58]  Sorry, other way around.
[4965.46 --> 4969.96]  So where do we use kind of the phosphorus-doped nickel?
[4970.16 --> 4971.00]  Where does that be?
[4971.30 --> 4973.14]  Everywhere you see copper on our board is gold.
[4973.14 --> 4973.84]  External layers.
[4974.96 --> 4975.18]  Yeah.
[4975.18 --> 4978.28]  That has – that layer of gold is angstrom stick.
[4979.40 --> 4986.06]  And what's underneath in between the gold and the copper is actually a nickel-phosphorus alloy, like Andrew was saying.
[4986.44 --> 4986.86]  Damn it.
[4986.86 --> 4989.64]  It's ENIG, Electroless Nickel Immersion Gold.
[4989.82 --> 4993.78]  So like Electroless Nickel is a type of plating method for putting nickel onto copper.
[4994.42 --> 5006.38]  And then Immersion Gold is basically like this gold flash plating that makes the solderability a lot better, but also doesn't put so much gold on there that it's expensive and you don't have gold embrittlement of your solder joints.
[5007.26 --> 5008.82]  Too much gold is also a bad thing.
[5010.90 --> 5012.12]  Computers are really complicated.
[5012.22 --> 5013.68]  How does any of this stuff ever work?
[5013.76 --> 5014.78]  It's just amazing to me.
[5014.78 --> 5018.96]  There are all these memes going around about like we don't have enough electrical engineers.
[5019.22 --> 5021.16]  It's like, well, I mean, yeah.
[5021.30 --> 5023.88]  We don't have – I mean, geez, who can keep this in their heads?
[5024.92 --> 5025.14]  Yeah.
[5025.22 --> 5026.40]  It's just remarkable.
[5026.60 --> 5032.86]  And it's interesting to get that – so surface roughness, Tom, is like one area that is particularly tough to navigate.
[5033.18 --> 5034.80]  And it sounds like it has a real effect.
[5034.80 --> 5048.46]  And in fact, somewhere around like around 10 gig days, the resistive losses became on par with dielectric losses just based on – and again, this kind of gets into what is your impedance.
[5048.46 --> 5059.60]  For instance, in order to create an impedance of, let's say, 50 ohms, your geometry has to be a certain width and a certain distance from the dielectric, right?
[5059.60 --> 5068.06]  And so in general, this is all yet another complexity that you're trying to like fit your PCB into a certain overall thickness.
[5068.34 --> 5070.14]  And I have to get so many layers into that.
[5070.32 --> 5078.62]  So then that – you know, all of these things cascade to say in order to route the board to make it work, you have to do this geometry and then that geometry.
[5078.62 --> 5086.58]  You go and look at the losses of it and it's like generally speaking, about 50-50 is what I found on the boards I was designing.
[5087.22 --> 5089.44]  And so resistance is huge.
[5089.82 --> 5090.48]  50-50, what do you mean?
[5090.48 --> 5103.14]  So the resistive – so there's two types of primary loss in most of – PCB, we'll just talk about like resistive loss, i.e. literally LRC, so the R part.
[5103.14 --> 5110.80]  And then your dielectric has losses due to – well, there's lots of fun physics there.
[5110.90 --> 5116.58]  But nevertheless, like your dielectric loss constant is what sort of dictates that primarily.
[5116.90 --> 5127.76]  So we can pay for less loss in the dielectric by buying better and better dielectrics that have lower and lower DF or the dissipation factor.
[5127.76 --> 5129.54]  And so we do that.
[5129.68 --> 5135.26]  We pay for a really good – a really good, very low loss material.
[5135.72 --> 5140.04]  But you still can't get very – you can't get that good on copper.
[5140.24 --> 5144.64]  So resistance losses are still dominating in most cases.
[5144.98 --> 5149.36]  You can improve that by making your trace wider because literally you add more copper.
[5149.36 --> 5160.30]  But that is yet another problem because if you make the trace wide, that means you have to make the dielectric thicker, which means you have only so many layers you can fit in the overall thickness of the board you're trying to achieve.
[5160.54 --> 5161.56]  So all of these things.
[5161.78 --> 5163.68]  So resistance is bad.
[5164.64 --> 5164.78]  Right.
[5166.84 --> 5169.90]  And if you make your copper tooth, maybe your board falls apart.
[5170.46 --> 5170.98]  Right, exactly.
[5171.14 --> 5172.36]  I mean, clearly there's a reason for the R part.
[5172.36 --> 5177.70]  But for the adhesion, your board will literally delaminate if you make this thing –
[5177.70 --> 5178.06]  Yeah, boy.
[5179.38 --> 5182.46]  You know, I've said this before.
[5182.70 --> 5183.72]  I'm sure I'm going to say it again.
[5183.84 --> 5186.56]  I feel like the PCB is missing a definitive history.
[5186.70 --> 5187.84]  I mean, there's so much stuff.
[5187.92 --> 5200.12]  And I feel like I'm always learning something that is extremely important, like the adhesion and the surface roughness, which I had never heard of, and is yet clearly a very important factor and trade-off.
[5200.12 --> 5202.80]  And Eric mentioned fiberweave effect.
[5202.90 --> 5210.94]  That's another fun thing, you know, because the fiberglass is literally woven in and then cured in a layer of epoxy.
[5211.72 --> 5219.36]  And so you get these little micro dips of dielectric constant across the board depending on which axis you're on.
[5219.46 --> 5227.30]  And so one of the mitigations of that is to rotate all of your artwork by, you know, ideally it would be 45 degree and then 22 degree.
[5227.30 --> 5229.18]  But, like, that costs a lot.
[5229.36 --> 5233.70]  So 11 degrees sort of state-of-the-art where everyone, like, you know, manages that.
[5233.82 --> 5239.42]  So you're trying to route it some odd angle to this orthogonal weave, which has little dips and valleys.
[5239.70 --> 5242.96]  And then, you know, you have more fun things to deal with.
[5243.34 --> 5245.58]  Is that something that, like, we are able to capture in simulation?
[5245.80 --> 5246.26]  Do we have to discover that?
[5246.26 --> 5246.64]  Yeah, yeah.
[5246.84 --> 5248.74]  Not by – simulation is difficult.
[5248.74 --> 5251.82]  But for measurement, we can capture it.
[5252.06 --> 5261.04]  And that's one of the things that – one of the bits of work we will do in order to determine – like, there's lots of different ways of mitigating it.
[5261.04 --> 5268.18]  But the impact is that if you had a differential pair and you're routing along a board, you think they're well phased matched.
[5268.18 --> 5275.98]  But lo and behold, one of them might be sitting, you know, under, like, a slightly higher dielectric constant than the other one.
[5276.08 --> 5282.64]  It will go slightly faster and they will then be off by a picosecond or two picoseconds or whatever.
[5282.84 --> 5286.04]  And it – you know, at a 40 picosecond die, this stuff really matters.
[5286.04 --> 5286.64]  Right.
[5287.64 --> 5288.16]  Man.
[5289.18 --> 5290.42]  And, Brian, maybe just to add to that –
[5290.42 --> 5292.28]  Machesic ferocious noise in 150 minutes.
[5292.62 --> 5297.30]  We're trying to beat 350 seconds of jitter on clocks.
[5297.50 --> 5301.48]  And so one picosecond that we get skew out of a PNN, that's a lot.
[5302.06 --> 5302.52]  It is.
[5302.74 --> 5305.32]  You just undid all the work that you did in the other place.
[5305.32 --> 5305.56]  Totally.
[5306.22 --> 5306.44]  Yeah.
[5306.90 --> 5308.46]  Robert, sorry, you were going to say?
[5309.52 --> 5310.26]  Oh, no problem.
[5310.26 --> 5318.88]  I was just going to say, I've actually seen people define small sections of a design and analyze the fiber weave in simulation.
[5319.06 --> 5330.92]  They'll actually draw in the fiber weave as well as the epoxy to see how different angles of rotating are going to affect, you know, how much loss you might have or any problems you might have from that fiber weave effect.
[5331.68 --> 5332.68]  Yeah, that is really cool.
[5333.08 --> 5334.52]  Did they ever write any papers on that?
[5334.58 --> 5335.48]  That would be fun to watch.
[5335.82 --> 5336.28]  Go ahead and read.
[5338.44 --> 5339.62]  I believe so.
[5339.62 --> 5342.68]  I don't remember off the top of my head, but I have seen it done before.
[5344.06 --> 5344.90]  That's really neat.
[5345.90 --> 5353.22]  And I mean, the upshot is, you know, and this has been, you know, from piece of paper through simulation all the way through.
[5353.46 --> 5360.12]  I mean, we've got a – then this is the advantage of doing this thing kind of from first principles and simulation intensive and so on.
[5360.36 --> 5363.20]  We've got a backplane that seems to be doing pretty well.
[5363.20 --> 5371.28]  I mean, it's – Ariadne, it must feel very satisfying to have taken this thing from its initial conception to, as you say, it's a measurement two years in the making.
[5371.28 --> 5374.46]  Yes, absolutely very satisfying.
[5374.46 --> 5381.22]  And also, like I said in the tweet, a little unique because we know the two systems that will be connected.
[5381.22 --> 5393.88]  Whereas if you are building a switch that you sell in the market as a – just as a standalone device, now you need to live within the specification that the IEEE standard dictates to you.
[5393.88 --> 5407.62]  So you're using, you know, some of these ballpark figures that they put in these standards and then, you know, if everyone adheres to them, then you're going to most likely end up with a system that works.
[5407.74 --> 5418.36]  But it might mean that, for example, with a particular switch and NIC configuration at these higher speeds that the DAC cable that you used to use that is two meter might not actually be working anymore.
[5418.46 --> 5422.76]  So now you need the one and a half meter DAC cable might be the longest you can get.
[5422.76 --> 5442.48]  But in our case, because we control both sides of this link and we very precisely control what the link itself looks like because we're sourcing all of these individual pieces and we're carefully selecting them and matching them and making sure that we ring out all the little bits of performance that we can get, we're able to build a backplane that is actually fairly complex.
[5442.48 --> 5448.30]  There's multiple connectors in there, pretty long piece of copper to go from one board to the next.
[5448.30 --> 5455.90]  But we're able to measure that and build some confidence that by the time we're done, this thing will actually work because we've seen the worst case.
[5456.00 --> 5459.40]  We understand which cable lengths we'll be observing.
[5459.72 --> 5464.84]  We can do some checks on the quality of these cables and these are built to very, very tight tolerances.
[5464.84 --> 5471.86]  And then we can measure that and we can characterize that and then, you know, we build a little bit of buffer and a little bit of margin in there.
[5472.00 --> 5481.06]  But it basically gives us a very good overall picture of what the system will be used, like the context in which the system will be operating, which is pretty cool.
[5481.58 --> 5482.44]  It is really cool.
[5482.62 --> 5487.68]  And it's unquestionably, this is a hard path to go build all of this from first principles.
[5487.68 --> 5507.48]  I also think, so Eric, so real talk, when this thing was not working, when we were not able to drive this to 100 gigs, what was the, to what degree were you kind of vomiting in a trash can or wondering if we, have we screwed something major up or do you have confidence we're going to nail it?
[5508.18 --> 5510.88]  Yeah, there's a reason that I travel with lots of antacids.
[5511.90 --> 5512.78]  There you go, right?
[5512.78 --> 5519.90]  I got a lot of indigestion from this and I didn't realize like how much this was weighing on me until we got it working and I slept really, really well.
[5520.04 --> 5522.72]  I'm like, oh, yeah, okay.
[5523.54 --> 5540.58]  But the satisfaction that you get after working on this for so long and not even nearly as long as Aria and you and everybody, but the time that I've been working on it and seeing it come and getting it connected with our longest cable
[5540.58 --> 5546.08]  and have it have basically zero FEC corrections.
[5546.80 --> 5549.70]  Because as I said before, you kind of expect FEC corrections.
[5549.70 --> 5550.52]  Right, right.
[5550.78 --> 5552.64]  This would be forward error correction.
[5553.08 --> 5553.38]  Yeah.
[5554.42 --> 5561.80]  Like you assume there's going to be bit errors and we have FEC enabled to correct the notes and base this on none.
[5564.06 --> 5565.36]  That is really great.
[5565.44 --> 5566.08]  That's just amazing.
[5566.52 --> 5566.64]  Yeah.
[5566.64 --> 5569.72]  This warm fuzzy feeling like it's Christmas morning or something.
[5571.72 --> 5575.52]  Well, that I think is a great note to end on.
[5576.38 --> 5579.52]  You know, this has been a huge team effort.
[5579.68 --> 5588.54]  I mean, I think part of what I love about this problem is that it requires every single link in the chain needs to work.
[5588.54 --> 5594.26]  And anything can actually introduce, you know, insertion loss that you don't want or what have you.
[5594.52 --> 5598.64]  And I think it was really fun to watch all this come together.
[5599.46 --> 5602.44]  And Larry, Robert, thank you for joining us as well.
[5602.60 --> 5606.20]  It was obviously fun to put your software to work.
[5606.20 --> 5611.76]  And hopefully you've enjoyed getting with it, getting with a team that's actually using it in anger.
[5612.90 --> 5615.64]  And we appreciate it.
[5616.36 --> 5616.72]  Absolutely.
[5616.84 --> 5617.66]  Thank you for having us.
[5618.06 --> 5618.94]  Yeah, you bet.
[5619.08 --> 5620.88]  And thank you, everyone.
[5621.08 --> 5622.08]  This has been a lot of fun.
[5622.14 --> 5625.14]  Andrew, thank you for your work on Geoscope client.
[5625.14 --> 5628.78]  I mean, the open source work is really, really important.
[5628.92 --> 5630.34]  And we're very excited to see it.
[5631.10 --> 5632.26]  And the domains that you're making.
[5632.88 --> 5633.96]  And the, absolutely.
[5634.50 --> 5634.80]  Yes.
[5635.06 --> 5639.74]  So bringing open source software to a domain that's early needs it.
[5640.92 --> 5641.48]  All right.
[5641.52 --> 5643.90]  Well, Arian, thank you very much for kicking this off with this tweet.
[5644.06 --> 5645.72]  It was a measurement two years in the making.
[5646.58 --> 5652.12]  Adam, I assume I can speak for both of us when I say it's been extraordinarily educational, as always.
[5652.52 --> 5652.92]  Absolutely.
[5652.92 --> 5655.82]  It is amazing that anything works at all.
[5656.08 --> 5660.18]  And now can we please those lunkheads like us in software?
[5660.68 --> 5667.14]  It is our responsibility to get our software to run correctly on this unbelievable fabric.
[5667.42 --> 5671.42]  So we really need to, let's try not to be such cool.
[5671.74 --> 5673.46]  Yeah, don't waste any bits, please.
[5673.62 --> 5674.54]  I don't waste any bits.
[5674.98 --> 5675.94]  So we work hard for it.
[5675.96 --> 5676.98]  Together over here, right?
[5677.32 --> 5677.80]  Exactly.
[5678.04 --> 5679.16]  We got to clean it up.
[5679.60 --> 5679.98]  All right.
[5680.02 --> 5680.66]  Thanks, everyone.
[5680.66 --> 5684.38]  Next time, it's going to be Kate talking about supply chain.
[5684.62 --> 5685.98]  That's going to be a great discussion.
[5686.16 --> 5687.20]  That's going to be next week.
[5687.34 --> 5688.58]  So really looking forward to that one.
[5689.76 --> 5691.80]  And Robert, Larry, thanks again.
[5691.92 --> 5692.60]  Thank you, everyone.
[5692.94 --> 5693.82]  And see you next time.
[5693.82 --> 5694.98]  We'll see you next time.
[5695.08 --> 5695.62]  Bye.
[5695.62 --> 5696.76]  Okay.
[5696.76 --> 5696.98]  Bye.
[5697.00 --> 5697.12]  Bye.
[5697.26 --> 5697.30]  Bye.
[5697.32 --> 5697.60]  Bye.
[5697.78 --> 5698.20]  Bye.
[5698.70 --> 5699.54]  Bye.
[5699.60 --> 5700.30]  Bye.
[5700.82 --> 5701.66]  Bye.
[5701.86 --> 5702.56]  Bye.
[5703.18 --> 5717.96]  All right.
[5718.18 --> 5719.22]  Bye.
[5719.68 --> 5720.16]  Bye.
[5720.58 --> 5720.94]  Bye.
[5720.98 --> 5721.76]  Bye.
[5721.76 --> 5722.18]  Bye.
