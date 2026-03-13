[0.00 → 4.90] So I am really excited to have Jonathan Dinesh here from Sam tech.
[5.30 → 15.68] And kind of before we get into this, I want to give kind of a somewhat long intro to kind of how we got to Sam tech and a little bit of Oxide's approach.
[15.76 → 19.20] We talked about this in other episodes, I know.
[19.28 → 21.78] I know we talked about this when we had Kate on.
[21.92 → 24.06] We certainly talked about this when we had Doug on from Benchmark.
[24.06 → 33.92] But our kind of view about the way we build this stuff is, to us, makes a lot of sense, but it is a little bit idiosyncratic.
[34.10 → 38.78] So we know that we're building a large machine, much larger than we can build alone.
[39.62 → 48.96] And we are not really looking for, I mean, obviously we need suppliers, but we're really looking for folks that are going to partner with us more deeply.
[48.96 → 54.76] And so on of the things that we do at Oxide is we really differentiate between partners and vendors.
[55.08 → 58.08] And a vendor for us is just selling kind of undifferentiated things.
[59.56 → 62.62] And, you know, the shipping is kind of the classic example of this.
[62.66 → 65.84] Like we do not have a dedicated shipping partner.
[66.70 → 67.88] We just kind of ship on.
[68.14 → 72.28] Oh, actually, maybe like, what is the one that, is it Pirate Bay?
[72.50 → 73.16] What's the name?
[73.32 → 73.82] Pirate Ship.
[74.36 → 74.92] Pirate Ship.
[75.08 → 76.92] Yeah, Pirate Bay is the other one.
[77.38 → 78.12] Pirate Bay is the other one.
[78.12 → 78.32] Whoops.
[78.96 → 79.66] Yeah, Pirate Bay.
[79.74 → 79.94] No, no.
[80.00 → 80.56] We don't do anything with Pirate Bay.
[80.76 → 81.32] But we do.
[82.06 → 83.04] And so maybe, I don't know.
[83.42 → 85.08] Nathaniel, do you use Pirate Ship a lot?
[85.20 → 86.10] Maybe that is our preferred.
[86.74 → 91.18] I mean, I don't know, like for dollars spent, how much we spend there.
[91.28 → 97.38] But certainly a lot of us remote people use that a lot to ship because it's convenient, and you just print the postage and go.
[97.98 → 101.26] Well, it's kind of heartbreaking if this is going to be a really special relationship that we have with Pirate Ship.
[101.26 → 104.96] Because we're going to have to find another example for something that is purely a vendor for us.
[105.16 → 108.42] But where we are really not differentiating.
[108.42 → 117.68] But for a lot of other things where we are really looking to go innovate with another company, we are really looking for a partner.
[117.68 → 126.04] And we're really looking for someone who's going to understand what we're going to go build it with us and go take responsibility with us with this thing.
[126.04 → 131.74] And, you know, I'd like to believe that some of this comes from our own shared history at Sun.
[132.30 → 141.04] Where one of the I think the real strengths of Sun was the way that Sun viewed its supplier relations and then also its customer relationships.
[141.30 → 144.86] And really valuing very deep relationships on both sides there.
[144.86 → 150.56] And we have lived where those relationships are not necessarily valued.
[151.52 → 155.56] And where the suppliers are constantly being pitted against one another.
[156.00 → 157.32] And it's not good.
[157.56 → 160.46] So this is kind of our disposition for kind of how we built this thing.
[160.52 → 162.24] It's really looking for the right folks.
[162.24 → 175.76] And our intro to Sam tech was, Arian, I think it was when we were really starting to figure out what the switch was going to look like.
[175.84 → 178.70] This is in like the summer of 2020, fall of 2020.
[178.70 → 186.96] And this is how hard can it be switched, which we are learning is like, damn it, this thing is really hard.
[187.78 → 196.36] And somewhere along the line, Arian, you were beginning to look at how we do that SI from the actual switching silicon.
[196.52 → 198.40] We decided on Torino at that point.
[198.90 → 208.00] But the actual signal integrity from the switching silicon to the actual QSFPs was actually going to be a real challenge.
[208.00 → 208.84] Am I remembering that correctly?
[208.94 → 211.32] That that's kind of where we kind of start on this journey?
[213.16 → 213.52] Yeah.
[214.24 → 225.92] So the thing I was trying to figure out was how do we push the ASIC as far back in a chassis as we can so that we get it as close to the sort of the back.
[226.00 → 228.92] So that the cables in the back can be as short as we can make them.
[228.92 → 235.60] While still having fans on the back of the chassis.
[235.76 → 238.44] So the board needs to be at a certain height in the chassis.
[239.62 → 242.20] And then you have these QSFPs in the front.
[242.28 → 243.82] And I was like, how are we going to resolve that?
[243.88 → 248.06] Because that is going to be an enormous slab of PCB that sits in this chassis.
[248.54 → 250.04] If you do that, all PCB.
[250.04 → 258.26] And so the idea formed to, or rather I started looking at what sort of solutions is available.
[258.86 → 264.00] And I stumbled upon the flyover cable system that Seek has developed.
[264.00 → 269.96] Which is a set of connectors and then Twin cabling that goes from a QSFP interface.
[269.96 → 272.66] Or it can be like several different connectors and interfaces.
[273.32 → 276.34] To a connector using cabling.
[276.34 → 279.40] And then you can suddenly go, A, a little bit further.
[279.64 → 286.40] Because you, like cabling has, these types of Twin cables have far less loss.
[286.48 → 288.36] Much better performance than a PCB has.
[289.04 → 294.34] But more importantly, I could place, I could basically split the board into two.
[294.54 → 298.18] And I could place one board at a particular height in the chassis.
[298.44 → 300.46] That was accommodating for the fans.
[300.50 → 303.96] And then the other board could be exactly in the centre of the chassis.
[303.96 → 306.82] And then you could have QSFP ports on both sides of the board.
[306.88 → 309.30] So you can make them belly to belly, as it's called.
[310.00 → 314.40] And then you would use these flyover cables to then fly back to the main board.
[314.40 → 315.82] And land near the ASIC.
[315.98 → 317.08] And then connect the two.
[317.86 → 319.06] So that's where we start.
[319.20 → 323.08] So that was a solution that Seek had developed.
[323.18 → 326.02] It was already made, like visible on their website.
[326.02 → 332.78] So we reached out and started talking with that as a starting point.
[332.98 → 336.22] And then things went from there.
[336.66 → 336.76] Okay.
[336.88 → 340.52] So, Arden, had you heard of Seek before kind of discovering this?
[341.10 → 342.30] I certainly had not.
[342.44 → 343.48] My introduction to Seek.
[343.74 → 344.34] Yes, I have.
[344.34 → 351.68] Because of the sort of quintessential SWD connector.
[351.86 → 353.50] That's a very prominent Seek part.
[353.76 → 355.16] So I'd heard of them before.
[355.32 → 360.80] And I'd seen some of their higher-end cable systems out of sort of curiosity in the past.
[360.92 → 363.06] But never had a reason to design with it.
[363.08 → 367.48] Because, you know, I never had anything that would go that fast until then.
[368.02 → 371.22] And so you discovered this kind of flyover design.
[371.22 → 375.42] And I just remember you sending me, like, a pointer to this video.
[375.74 → 376.26] And I was like, really?
[376.40 → 377.86] It's like, oh, man, this is great.
[377.94 → 378.88] What a great idea.
[379.38 → 380.14] And obviously this is how everyone was going to.
[380.14 → 381.48] There was a picture on the website.
[381.76 → 384.22] And it turned out later that we learned that it was Bigness's work.
[384.36 → 394.36] There's a picture on the website that splits a switch into two pieces with flyover cabling from the front to the ASIC more located in the back for cooling purposes.
[394.36 → 399.52] And we wanted to do that both for cooling purposes and to keep the backside backplate shorter.
[401.22 → 407.02] And so it was like, oh, hey, this is clearly an idea that someone has tried.
[407.20 → 410.60] Because if it is on their website, it must work.
[412.50 → 415.24] That may have been a leap of faith.
[415.30 → 415.72] I don't know.
[415.86 → 417.50] But, you know, it turns out it does work.
[417.96 → 419.58] But, yeah, that's how we got started.
[419.58 → 422.14] And so then you reached out to Sam tech.
[422.76 → 427.98] And, again, this is not a company that I – we're obviously talking to a lot of folks.
[428.24 → 430.98] And I just didn't really have any exposure to them.
[431.24 → 433.68] But then something, like, very different happened.
[434.82 → 438.40] Namely, I don't know if it was Nate or whoever you got a hold of at Sam tech.
[438.40 → 441.70] But Sam tech told you, like, we're going to ship a cable to you, like, today.
[443.26 → 448.34] And all I remember is that the next day, you're like, they sent me this cable.
[448.52 → 449.36] Like, I've got it.
[449.42 → 450.46] Like, they sent it to my house.
[450.98 → 451.70] Like, I'm holding it.
[451.70 → 455.14] Yeah, I don't know if it was quite the next day, but it was pretty fast.
[455.30 → 455.86] It was pretty fast.
[455.86 → 460.90] It was – well, can I say, like, we were having a hard time, like, getting – like, everyone else we're talking with.
[460.90 → 464.52] Like, we are – it's, like, getting bogged down with NDAs and all this other crap.
[464.62 → 468.72] And all of a sudden, you actually have a company that's like, oh, hey, yeah, you want to build this, like, crazy thing?
[468.76 → 470.02] Like, let's just send you some samples.
[470.54 → 473.66] And you're like, are you – did I, like, pass out?
[473.72 → 474.42] Is this actually happening?
[474.48 → 475.20] Are you an apparition?
[475.32 → 476.12] Are you a friendly ghost?
[477.24 → 480.04] They are known for sudden samples, right?
[480.90 → 481.50] They are.
[481.50 → 490.28] And so, and Bigness and Jonathan, so maybe this is a good time to get you involved here because, obviously, this is something that we learned is not an accident.
[490.90 → 496.44] And this is something that is a very kind of deliberate approach that Sam tech has to really support engineers.
[497.32 → 500.52] And, boy, does it pay off because you generate some real fans.
[500.62 → 502.40] I actually got a photo that I'm going to drop in the chat.
[502.50 → 505.22] I know, Adam, you love having annotating podcasts with photos.
[505.34 → 506.06] I know it's your favourite thing.
[506.18 → 506.64] Oh, the best, yeah.
[506.94 → 510.00] So I've got a photo of Arian.
[510.38 → 515.06] This is, like, one of the great things with the pandemic is it made it kind of easy to take just, like, screenshots of me.
[515.06 → 518.06] And this is, like, Arian showing me this cable.
[518.06 → 521.24] And just, like, this thing is, like, I've got it in my hand now.
[521.32 → 522.64] And, like, this is what it would look like.
[522.76 → 526.16] And it was really, really exciting and energizing.
[526.58 → 529.44] So, Bigness, I mean, this is not an accident, right?
[529.48 → 535.00] This is the – you kind of take a very deliberate approach to kind of engineer – getting engineers samples in hand.
[536.42 → 537.86] Yes, absolutely.
[537.86 → 542.72] So, first, thank you for having Jonathan and me on the podcast.
[542.96 → 543.80] Really appreciate that.
[544.56 → 547.28] So, yes, so Sam tech's a unique company.
[548.00 → 551.06] We don't go after just the Me Too products.
[551.16 → 556.92] We want to go after unique products that solve a customer's problems.
[557.42 → 562.86] And in order to solve customer's problems, first, you have to get customers to understand their problems and get them the parts that they need.
[563.16 → 564.44] So that's the philosophy.
[564.44 → 568.28] And, you know, you talked about sudden service or sudden samples.
[568.44 → 579.04] That's how the company got started, where, you know, even for the low-speed and power connectors and all these to send it just overnight to customers.
[579.04 → 580.94] And we still do that as free samples.
[580.94 → 590.82] But over the years, as our products became, you know, on the higher-speed side or even, you know, very low-small-profile power connectors and things like that,
[591.32 → 601.60] the service has gone beyond just sending samples to also providing complementary services and signal integrity for the full channel for the customers
[601.60 → 610.90] or doing cable management mock-ups for the customers or doing first-order thermal analysis of fluid flow analysis for the customers.
[610.90 → 620.30] So we've taken that service, sudden service, to the next level now because we understand that in order for customers to use products that we make,
[620.36 → 627.20] which are not Me Too, they're a unique kind of products in the industry, there's a certain learning curve that the customers will have to go through.
[627.86 → 637.78] And who better than us to help them because we have quite a bit of experience because of all the – we work with a huge variety of customers in different industries.
[637.78 → 646.62] Before we dig deeper, I want to stress that for anyone listening who thinks, well, it's a cable.
[646.74 → 647.92] How difficult can this be?
[649.38 → 661.98] Let me absolutely stress that a cable – anytime you add a cable to a system, you now added a – think of it as a third – the complexity of a third printed circuit board or beyond that in terms of complexity.
[661.98 → 671.48] Cables are incredibly complex because cables cause all sorts of effects that you have to account for in terms of signal integrity, power integrity.
[671.74 → 679.38] You have to think about your emissions and because signals are going to leave your board, and they're going to go to some other system or another board.
[680.08 → 684.12] And then you have to take care of that signal that rides on this cable.
[684.12 → 691.80] I've now been privy to the design of two cable systems, and it is absolutely some of the hardest things you can do.
[692.14 → 707.00] So when Bigness talks about providing services like signal integrity and channel modelling and even some fluid dynamics and things around temperature and heating and all that, that's absolutely necessary.
[707.00 → 715.20] And it is very much appreciated when this is done by someone who actually understands what they're doing because it can make or break your system.
[715.42 → 719.12] And when it breaks your system, you're done.
[719.76 → 724.14] It's costly to fix that and get it in a working state.
[725.72 → 725.88] Yeah.
[725.88 → 738.68] Just one way I'd like to, and Arden, you talked about earlier, but in traditional systems, the conventional way of making designs was on the printed circuit board.
[739.42 → 742.78] And the way I think is you're designing in flat land.
[743.22 → 745.00] A PCB is just 2D space.
[745.16 → 748.36] Maybe you have a mezzanine board, but basically you're designing in flat land.
[748.36 → 754.28] But what cables allow, and as you mentioned, it allows you to design in 3D space.
[755.06 → 757.38] And all the boards don't have to be at the same level.
[757.52 → 758.60] You can make it modular.
[760.08 → 764.16] And you can even rotate the boards 90 degrees if your architecture allows it.
[764.56 → 769.26] So they don't have to be in the same even plane or direction.
[769.26 → 781.16] And for that to happen and to take the advantage of that, traditional conventional architecture used to be where the electrical engineer, electrical designer was the chief architect,
[781.16 → 785.04] and all the mechanical guys and the manufacturing guys just had to adapt after that.
[785.82 → 793.58] I think as the data rates go up, the electrical architect, the mechanical, the thermal, the manufacturing architect all need to sit together,
[793.82 → 798.56] and they need to compromise together for a system to be successful.
[799.26 → 800.42] Just like yours.
[801.16 → 802.22] Yeah, that's fascinating.
[802.46 → 803.70] That is definitely true.
[803.94 → 820.60] It has been a balancing act between making it work, just getting a cable system to work with low enough loss so that you have enough signal left over on the other side to use it and recover it and actually drive the link.
[821.50 → 826.12] But then how to fit that in your chassis and how that runs and how it is manufactured.
[826.12 → 829.62] And I'm sure we'll touch on this in this conversation.
[830.22 → 832.02] And we touched on it with Doug.
[832.56 → 838.36] Manufacturing a cable system of complexity like this is its own whole different thing.
[838.56 → 843.14] You can have all these mock-ups and I can have all these pinouts and spreadsheets.
[843.14 → 849.64] And what these spreadsheets don't really convey is that because you're only taking like a small slice of a pinout out of that back plane.
[850.08 → 854.68] But that's thousands of signals that all land on these connectors.
[854.90 → 858.80] So you're looking at tens of connectors, hundreds of connectors sometimes.
[858.80 → 868.16] And then, you know, it's quite the juggling act to – it's a high-wire act to make it all fit ultimately.
[868.56 → 871.56] And then make it manufacturable and repeatable.
[871.56 → 873.42] Well, that's it.
[873.52 → 892.10] And I think it is really helpful in terms of Sam Tax's general approach to really be walking with you through all of these phases and kind of exploring these various trade-offs and not being left to merely do it on your own, which has been – I mean, it's been huge for us.
[892.10 → 903.10] And, Jan ash, I thought it was very funny because when you came out to Oxide and saw the switch and saw what we'd done with the flyover cables, you're like, God, you know, you were telling us, you're just like, I love this design.
[903.22 → 909.04] We're like, well, it's honestly like we're just doing what you – this is your guidance basically, Sam Tax guidance.
[909.58 → 910.78] And we kind of assumed that every –
[910.78 → 912.36] You just built what was on the website.
[912.68 → 913.68] It was on the website.
[913.92 → 916.68] And we just like assumed that like isn't everybody doing it this way?
[916.74 → 919.10] And you were like, no, no, no one else is doing it this way.
[919.22 → 920.92] We tell everybody to do it this way.
[920.92 → 922.14] This is the right way to do it.
[922.20 → 922.84] But no, no, no.
[922.90 → 928.46] This is not a – so, yeah, I guess we just felt it was a great idea.
[928.56 → 929.48] It's obviously a great idea.
[929.58 → 930.50] Everyone should do it this way.
[930.62 → 934.60] We preach the concept and the philosophy all the time, obviously.
[935.42 → 940.76] And, you know, some people get it and some people say, oh, okay, yeah, that's nice.
[940.76 → 943.36] But we're going to go back to doing it the way we've been doing it.
[943.70 → 946.58] But there's – you know, obviously you guys saw the benefits.
[946.96 → 949.76] You can put things on your boards.
[949.76 → 951.62] You can split boards, different levels.
[953.38 → 956.10] You don't have to – like you guys have a full cable backplate.
[956.28 → 966.26] So that is – to not have a backplate PCB, I mean, that's a ton of design effort, board spins.
[966.54 → 975.60] I mean, that's just incredible savings, just that one component in of itself, not to mention everything else that we've already talked about.
[975.60 → 980.58] But anyway, we talk to people about this concept all the time.
[980.88 → 990.60] And we've had like – you know, we've had some customers that are building smaller chassis or smaller cabinets, you know, not full-size cabinets like you guys did.
[990.66 → 997.64] So when we saw your cabinets, full-size all the way up and down, full rack size, and it was, you know, completely cabled.
[997.64 → 1002.68] It was, you know, not just the cabled backplate, but all the sleds were cabled.
[1002.84 → 1004.56] And it's just like, oh, my gosh, they did it.
[1005.28 → 1007.58] Well, and truthfully, we had an unfair advantage.
[1008.00 → 1015.34] And Adam, I remember you and I talked about this very early on in Oxide's life, that we knew that we were going to have an unfair advantage just by taking a clean sheet of paper.
[1015.34 → 1040.74] And Adam, I can't remember if we talked about this explicitly or not, but when Adam and I started a startup inside of Sun in 2008, we – just by – or 2006 when we started it, we – just by taking a clean sheet of paper, we were actually able to deploy Flash more or less early than any other enterprise storage unit just because we were walking up to it with a clean sheet of paper at the right time, effectively.
[1040.74 → 1050.76] And Adam, I can't remember if we talked about it or not explicitly, but I remember thinking, like, there's going to be some equivalent to that where we are just going to have the benefit of having the clean sheet of paper at the right moment.
[1050.92 → 1056.26] And everybody knows that, like, hey, there's this way to do it over there that is the better way to do it, but no one has a clean sheet of paper right now.
[1056.88 → 1057.68] That's exactly right.
[1057.70 → 1063.96] And this is a perfect analogy for, you know, Flash in 2008 was just changing, and we were at the right place at the right time.
[1063.96 → 1065.96] And this is a similar example.
[1066.12 → 1072.56] And actually, we've bumped into a bunch of other ones for just not having to pull along this long chain of legacy.
[1072.82 → 1075.02] So let us do a lot less, actually.
[1075.88 → 1076.24] Totally.
[1076.58 → 1084.32] And being able to do – I mean, Arian, you've been able to do exactly what you described of actually being able to innovate with respect to the switch.
[1084.36 → 1086.16] The switch is actually not one board.
[1086.54 → 1086.94] It's two.
[1086.94 → 1093.46] You've got this QSFP IO board that is then actually separated by an air gap, effectively, with these flyover cables.
[1094.10 → 1097.38] And the distance, actually, to the QSFP board doesn't hugely matter, right?
[1097.46 → 1104.02] I mean, we could – because once you're on the kind of the cable superhighway, it's – the loss is all going to be at the –
[1104.02 → 1106.10] Yeah, it's all pretty minimal.
[1106.90 → 1109.42] Like, it doesn't matter what you're going to – well, yeah.
[1109.52 → 1111.28] Like, over those distances, it doesn't matter.
[1111.28 → 1114.32] It starts to add up when you go, you know, three, four feet.
[1114.84 → 1119.10] But in this case, we're going, I don't know, 20-some inches.
[1119.44 → 1120.34] So it's not so bad.
[1123.06 → 1127.06] But – so what's interesting, though, is that we started this because I saw that picture.
[1127.54 → 1134.28] And I was like, oh, so Bigness pitched it because of – I think the main draw was, like, a thermal –
[1134.28 → 1134.92] Oh, sorry, the thermal.
[1135.04 → 1135.60] Yeah, yeah, that's correct.
[1135.60 → 1140.62] Because in a traditional switch, you have these QSFP interfaces that sit in the front.
[1140.70 → 1148.44] And then you need to put your ASIC, like, right there next to them because you want to keep those PCB traces as short as you can in order to stay within the loss parameters.
[1148.56 → 1149.56] And this is a real thing.
[1150.38 → 1156.58] You know, 100 gig, 28 gig NRZ, it's – you know, you don't have much.
[1156.58 → 1163.92] But then when you go to 56 gig PAM4 for, you know, 200 gig links and 400 gig links and beyond, the PCB is just eating so much of your budget.
[1165.26 → 1167.80] You have to be super close.
[1168.20 → 1175.24] But the problem is that all of these QSFP interfaces, all these transceivers, all have a pretty significant heat load.
[1175.50 → 1178.66] They're – you know, they start at, like, three, four watts.
[1178.66 → 1182.54] And some of them run up to, like, six, seven, eight watts.
[1183.82 → 1185.82] But you have to design for up to 10.
[1185.92 → 1191.80] So you have to accommodate potential, like, long-range modules that can go all the way to, like, nine or ten watts.
[1192.38 → 1203.60] And so if you have this 300, 400, 500-watt ASIC that sits right behind a load of QSFP interfaces that is also, you know, 100, 200, 300 watts of power,
[1203.76 → 1206.86] you have a very large amount of heat, like, in a tiny space.
[1206.86 → 1217.36] So the thing they gave us was, like, oh, you can put the ASIC much further in the back so it's closer to your fan so it's easier to evacuate the hot air that your ASIC produces.
[1217.50 → 1219.34] And I was, well, that's a really nice feature.
[1219.58 → 1223.42] But I was more interested in keeping the signal path to the back plane short.
[1224.82 → 1232.76] But the thing that fell out of this was that because we now cut the board into two pieces, we actually defined an interface between these two boards.
[1232.76 → 1235.98] And these two boards were actually designed sequentially.
[1235.98 → 1237.60] They weren't even designed so much in tandem.
[1237.78 → 1245.08] I designed the interface alongside sort of the first board, and I had a pretty reasonable idea what I wanted to do between these two boards.
[1245.32 → 1249.88] So there's flyover cabling for the high-speed interfaces back to the ASIC.
[1249.94 → 1256.10] And then there's a bunch of low-speed signalling between the two boards to manage the power on that front AO board.
[1256.10 → 1262.32] And there are a couple other components like LED drivers, and there's another five or copper ports on the front.
[1262.50 → 1266.86] And so there are some management pieces that are there.
[1266.86 → 1273.48] But what it let us do is it basically let us focus on the main board and get that interface done.
[1273.90 → 1281.80] And then once the main board was already fabled out, so that was already in production, the PCB was on its way, and assembly was on its way.
[1281.88 → 1285.92] That's when I turned around, and then we built the QSFP board that would attach to it.
[1285.92 → 1289.52] And we already started bring up of the main board.
[1291.46 → 1297.88] We started that in January, and I don't think we've had the QSFP board in hand until February or early March.
[1298.02 → 1300.98] But that was fine because we had plenty of work to do on that main board.
[1301.08 → 1310.34] So we could sequence these things in a pace that sort of made sense for us without having to design all of it up front.
[1310.34 → 1320.38] Because if we had had to design all the QSFP pieces in that main board, that main board would have taken another month or so to get done.
[1320.48 → 1324.92] Because the QSFP board was actually far more complex than I thought.
[1325.28 → 1326.34] Well, because there's...
[1327.08 → 1329.92] Definitely, like, you don't say, I was like, well, the QSFP board, like, how hard can that be?
[1330.04 → 1331.10] You're like, oh, Jesus Christ.
[1331.10 → 1334.78] Oh, yeah, but that's still 2,500 components on a PCB.
[1335.18 → 1339.76] And it's a really thick PCB because you have to, like, mount these things.
[1339.76 → 1340.46] It's belly to belly.
[1340.64 → 1344.98] But because you want all these interfaces, all these ports, you want power control over them.
[1345.00 → 1346.50] And you want fault protection.
[1346.70 → 1353.48] So if your QSFP module shorts, you don't want that to take out, you know, four other modules associated, like, next to it.
[1353.86 → 1357.68] So because of a power, like, irregularity or whatever.
[1357.76 → 1366.10] So each of these ports has a power, has a little e-fuse that we can use, A, measure power, but also to control power.
[1366.10 → 1374.34] We can turn it on and off, and it makes sure that if a module faults, it immediately shuts the module down without rippling through all the other modules in the system.
[1374.86 → 1377.28] So there's that, which adds all this stuff.
[1377.36 → 1384.22] There's all these ESD protection diodes that we need to put on there for various, like, because these are exposed interfaces on the front.
[1384.28 → 1385.20] So you need all this protection.
[1385.20 → 1388.12] So, yeah, that would have added easily.
[1389.02 → 1394.30] Like, it took us a month or so, month and a half, to get that design all done, like, all buttoned up.
[1394.34 → 1395.76] Before it was all done, set and done.
[1396.20 → 1396.58] And so...
[1396.58 → 1399.04] And the flyover cables were just huge to allow that to kind of be...
[1399.04 → 1401.54] Yeah, because you can cleanly cut that off.
[1401.76 → 1407.80] You can cut the interface between these two boards, and then you can sort of delay the...
[1407.80 → 1410.26] We were able to push the QSFP board out.
[1410.58 → 1413.04] But now the kicker is that we designed the QSFP...
[1413.70 → 1420.20] So the flyover, the pinout and the flyover cables, we designed such that we can actually re-spin this QSFP board in a different configuration.
[1420.20 → 1434.76] So today, we easily support 32 ports on the front, 32 200-gig ports, but we can reconfigure this board with actually very minimal effort into 16 400-gig ports.
[1435.18 → 1444.70] And then we can use the same connectors on the main board to then fly these 400-gig ports to the main board and make those work without having to redesign the main board at all.
[1444.78 → 1446.16] That same interface would work.
[1447.14 → 1447.82] That's right.
[1447.82 → 1455.96] We basically would do half the QSFP board, but then with the SFPD interfaces so that we can accommodate SFPD modules.
[1456.20 → 1461.04] Or if there's another standard that comes out at some point, we can do a different form factor altogether.
[1461.82 → 1469.28] I have this idea of maybe at some point we'll build a QSFP board that has a GPS receiver on it so that you can do very precise timing for...
[1469.28 → 1469.76] Right, right, right, yeah.
[1469.76 → 1475.84] So not all switches in your network need to have that, but you want to have a couple that might have that, you know, a couple per data centre.
[1475.84 → 1485.94] And so we can have a special flavour of the QSFP board that has a GPS module built in so that you can connect an antenna to it, and you can run GPS and you can have an accurate time source in your network.
[1486.44 → 1491.42] And so all these different variations of that board we can build without having to redo the main board.
[1491.56 → 1504.98] So it becomes a compartmentalized problem and will allow us to build several different variations of a switch chassis with relatively minimal and relatively low-risk engineering effort.
[1504.98 → 1505.30] Yeah.
[1505.84 → 1509.54] And so we were hugely sold on the flyover cables.
[1509.62 → 1510.40] That was going really well.
[1510.72 → 1512.26] And then we were...
[1512.26 → 1514.02] Initially, we...
[1514.02 → 1516.56] And, you know, hopefully I'm in a safe space where I can confess this.
[1516.62 → 1518.18] We were not actually considering Sam tech.
[1518.64 → 1524.72] I mean, Sam tech for us was kind of like, all right, we're going to use it for the flyover cables, but we're going to look for another vendor for the cable backplate.
[1525.60 → 1525.94] And...
[1525.94 → 1526.78] But as we were...
[1526.78 → 1528.98] Because we were already in progress with that other vendor.
[1528.98 → 1530.82] We were already in progress with that other vendor.
[1531.20 → 1534.54] And to be clear, we were trying to get them from being a vendor to being a partner.
[1534.54 → 1535.54] But they...
[1535.54 → 1536.82] It's not really working.
[1537.32 → 1538.42] Yeah, we couldn't get them there.
[1538.42 → 1542.42] But I heard that then Jonathan happened.
[1542.98 → 1543.44] Is that true?
[1543.44 → 1543.90] Jonathan happened.
[1544.30 → 1544.68] Yes.
[1544.94 → 1547.88] I mean, so the problem was that we were...
[1547.88 → 1552.00] I was trying to get drawings for these backplate cables using XMX connectors.
[1552.00 → 1555.24] And we were promised drawings.
[1555.44 → 1558.16] And, you know, the date passed and there were no drawings.
[1558.40 → 1562.66] And then we were tried again, and they would be there next week and the week after.
[1563.86 → 1566.00] To the point where we...
[1567.40 → 1568.00] And so out of some...
[1569.00 → 1571.10] There was some reluctance for me to get started.
[1571.28 → 1575.82] Because I had already figured out, like, oh, you are a second source of these XMX connectors.
[1575.82 → 1578.04] So we might be able to make this work.
[1578.68 → 1581.82] Now, there's a big difference between...
[1582.40 → 1586.20] There is a difference between what is advertised in the catalogue.
[1586.42 → 1592.52] Because the catalogue of connector and cable manufacturers is vast.
[1592.70 → 1595.02] But what is actually tooled up is a different story.
[1595.16 → 1596.42] So there's always going to be...
[1596.42 → 1598.86] You may not have the exact same thing.
[1599.06 → 1599.76] But let's...
[1599.76 → 1601.02] You know, fortunately you did.
[1601.02 → 1605.76] But I was initially a little bit reluctant to immediately jump ship.
[1605.96 → 1606.52] Because I did...
[1606.52 → 1608.92] That was a big gamble, I felt.
[1609.22 → 1612.58] And I didn't want to pit necessarily two companies against each other.
[1613.68 → 1618.18] Because also that would have been splitting my attention.
[1618.58 → 1620.60] And I did not have much time to go.
[1620.80 → 1623.10] And because I was spending an awful amount of time...
[1623.10 → 1626.66] I was spending a lot of time with the other company trying to get this to work.
[1626.66 → 1633.28] And so I was worried that I might have to spend similar amounts of time to get it to work with you.
[1634.50 → 1636.76] And I was not really in favour of that.
[1636.86 → 1643.24] So I was actually the one who had to be pushed and pulled, kicking and screaming a little bit.
[1643.34 → 1645.70] Because I didn't want to do that immediately.
[1645.90 → 1648.16] But then, yes, we started talking.
[1648.26 → 1649.20] Then Jonathan happened.
[1649.20 → 1652.20] And we actually...
[1652.20 → 1653.24] You managed to lap.
[1653.38 → 1657.20] Even though you started probably six or eight weeks behind.
[1658.08 → 1664.10] Managed to get the drawings in hand before the other partner, vendor, managed to do that.
[1665.42 → 1669.00] And at that point, you had to tell them, like, you're just late.
[1669.32 → 1669.98] I'm sorry.
[1670.10 → 1671.56] But you're just late.
[1671.56 → 1676.14] I remember some of those initial conversations.
[1676.14 → 1678.00] And they were very interesting to me.
[1678.08 → 1682.50] Because I was actually surprised that the other company was kind of being slow.
[1682.76 → 1685.10] Or slower than what you were hoping they would be.
[1686.00 → 1688.46] We actually have a good relationship with them.
[1688.82 → 1690.68] So I'm not going to talk bad about them.
[1691.52 → 1693.48] But Sam Tucks does try to do...
[1693.48 → 1696.60] Obviously, sudden service is something that we try to provide.
[1697.30 → 1699.32] And I could tell that you guys were frustrated.
[1699.32 → 1710.34] And, you know, it was from the very first call, you know, you kind of made it clear that you were kind of behind schedule from where you wanted to be.
[1710.70 → 1718.58] And so I just wanted to take that as an opportunity to run with it and get stuff to you as fast as I could.
[1718.88 → 1720.38] Well, the problem was...
[1720.38 → 1723.58] Again, I also don't want to speak ill of them.
[1723.72 → 1727.78] But the problem was that there were just too many people involved in the process.
[1727.78 → 1737.10] And what has been incredibly helpful working with you and Sam Tuck in general is that there's a very small number of people that we work with.
[1737.26 → 1740.76] And you bring in additional individuals when needed.
[1740.92 → 1745.54] And that really helps in terms of getting these things done.
[1745.94 → 1752.20] Because it means that there's just not a lot of overhead in the way that things need to be communicated.
[1752.20 → 1759.92] Well, you know, my mom has an adage that I'm sure is the time immemorial that nobody cares about your money like you do.
[1760.18 → 1765.20] I think she was telling me this shortly after she just lost a bunch of money to a financial analyst who...
[1765.20 → 1769.66] And, you know, I've always taken that to heart.
[1770.48 → 1779.56] And part of the problem that we were having, part of the frustration is like we just were not getting someone on the other side to treat this like their system.
[1779.74 → 1780.62] It was our system.
[1780.62 → 1783.54] And they were kind of...
[1783.54 → 1784.62] It was just...
[1784.62 → 1787.08] They felt very reluctant to actually...
[1787.08 → 1791.64] And Jonathan, when you kind of jumped in, you treated it like a system we were building together.
[1792.02 → 1794.44] And that was really, really important.
[1794.54 → 1801.76] Just like that level of attention to detail and empathy and let's go kind of figure this stuff out.
[1801.76 → 1802.30] And that's...
[1802.30 → 1803.32] I mean, you started out...
[1803.32 → 1807.28] Yeah, it was like eight weeks behind or more on something that was really time-critical for us.
[1808.12 → 1813.16] And, you know, within no time had basically passed and was in much better shape.
[1813.24 → 1815.58] And we were in a position to really be like...
[1815.58 → 1817.00] I mean, it was a no-brainer ultimately.
[1818.38 → 1826.82] And a no-brainer because just the degree to which you cared about our problems being shared with the two of us.
[1826.88 → 1830.32] That like we are going to take responsibility for building this system together.
[1830.32 → 1833.06] And I just can't tell you how meaningful that is.
[1833.16 → 1839.88] I mean, especially when you're us doing things that are a little bit odd.
[1840.78 → 1842.32] You know, the...
[1842.32 → 1843.78] That's perfect, Brian.
[1844.04 → 1844.26] Nice.
[1844.58 → 1845.62] Thank you for the kind words.
[1846.16 → 1850.20] Let me know the address where I can send you a gift certificate for saying such good things.
[1850.66 → 1851.46] Yeah, exactly.
[1851.58 → 1851.92] That's right.
[1852.02 → 1853.32] If you could just make that the cast, please.
[1854.42 → 1855.18] No, no, no.
[1855.18 → 1870.88] And actually, the thing that is so interesting to me is when we look around the industry and as we were kind of adding folks to the company that had been, you know, with a lot of experience, like they came in with very strong relationships because you have helped them.
[1871.10 → 1874.04] Sam tech, the larger Sam tech has helped them in past gigs.
[1874.04 → 1877.36] I mean, RFK, Robert Keith really wanted to be here today.
[1877.64 → 1882.18] And he is, as you know, is a huge Sam tech fan.
[1882.84 → 1886.64] The only reason he's actually at a graduation like right now.
[1887.38 → 1888.82] And even then he was like...
[1888.82 → 1890.32] So I made this at the worst possible time.
[1890.40 → 1890.94] Sorry, RFK.
[1891.00 → 1891.80] You're going to catch the recording.
[1891.80 → 1895.80] Even then, he was like, let's see, when does the graduation start?
[1895.92 → 1899.64] I mean, there is a non-zero chance that RFK is at a...
[1899.64 → 1900.78] Is literally they are...
[1900.78 → 1905.68] They've got like pomp and circumstance, and he's on his earbuds right now trying to unmute himself to contribute to this conversation.
[1906.22 → 1907.20] Because that...
[1907.20 → 1913.52] And that is not like a normal feeling for engineers to have about...
[1913.52 → 1915.06] But it really shows the partnership.
[1915.06 → 1917.06] And I also love, by the way, that we had...
[1917.66 → 1920.26] You have now like to set the bar for our expectation.
[1920.52 → 1928.40] And we had, well, let's just say a DRAM vendor that was trying to impress Oxide by coming by, bringing gifts.
[1928.62 → 1930.46] The problem is the gifts they brought were alcohol.
[1930.74 → 1931.94] We're like, we don't want any of this.
[1932.18 → 1933.60] RFK is like, I want samples.
[1933.78 → 1934.14] That's it.
[1934.26 → 1934.74] Like take...
[1934.74 → 1935.04] I don't know.
[1935.92 → 1936.70] Bringing booze.
[1936.86 → 1937.90] Like, I don't know.
[1938.12 → 1939.32] Go take that home or something.
[1939.48 → 1940.22] I want a sample.
[1940.76 → 1941.38] Give me samples.
[1941.56 → 1943.30] Give me technical data.
[1943.30 → 1944.88] We need to get this done.
[1945.76 → 1946.78] Then we can drink.
[1947.86 → 1948.70] Yeah, there you go.
[1949.08 → 1949.48] Contraption.
[1950.10 → 1953.52] So what I wanted to say, though, is we've really enjoyed working with you guys.
[1953.58 → 1955.92] You guys are a very good partner for us as well.
[1956.42 → 1965.70] And, you know, for all the folks listening, I think that it's important to understand that Oxide does a good job and how they do a good job for us.
[1965.84 → 1967.28] You know, they're buying cables from us.
[1967.28 → 1970.72] But they didn't just say, hey, we want this cable.
[1970.80 → 1971.44] Here's a signal map.
[1971.52 → 1972.22] Give us this length.
[1973.14 → 1973.82] Give it to us.
[1974.32 → 1974.96] Go, go, go.
[1975.06 → 1977.08] You know, it was an open discussion.
[1977.20 → 1981.42] There was a lot of talk about, hey, what's the optimized signal map for how you make...
[1981.42 → 1983.52] How do you make these cables in your production facility?
[1983.80 → 1989.08] You know, is there an optimized way that you would lay out the cables from a signal map standpoint?
[1989.08 → 1994.06] Because we're early enough in our design process that we can accommodate that.
[1994.26 → 1997.88] And then we talked about cable links and sleeving, how things go together.
[1999.74 → 2009.66] And just really listen to, you know, what we had to say about how we were making the cables and accommodated that on the design side in your system.
[2009.66 → 2018.02] And that's really, you know, that helps facilitate a lot of...
[2018.02 → 2019.72] ...with your vendors like this.
[2020.18 → 2020.42] Yeah.
[2020.52 → 2024.34] Could you elaborate specifically on good bends versus bad bends?
[2024.42 → 2030.24] Because I think this is a very concrete example of what you're talking about, about like, not all bends in cables are the same.
[2030.24 → 2032.38] Yeah, certainly.
[2032.60 → 2034.36] I know we've talked about it a little bit before.
[2034.52 → 2039.42] You guys have talked a little bit about it before with Doug specifically when he came on from Benchmark.
[2039.96 → 2044.34] But the Twin cable itself is, you know, you can picture it.
[2044.46 → 2047.06] It's two solid centre conductors.
[2047.46 → 2050.06] And that's surrounded by a dielectric.
[2050.06 → 2067.06] And so, in essence, if you're going to bend that Twin cable, a good bend would be if you can picture both of those centre conductors bending at the same time with the same bend radius.
[2067.90 → 2076.78] A bad bend would be, you know, one of those being on the inside and then the other one coming over top of it with a larger bend radius.
[2076.78 → 2084.84] Because in that case, the bend is pulling and pushing on those centre conductors relative to each other.
[2084.92 → 2088.46] Because one of those radiuses is smaller than the other.
[2090.00 → 2091.16] Is that a mechanical issue?
[2091.26 → 2092.78] We call that a...
[2092.78 → 2093.86] It's both.
[2094.38 → 2094.82] Okay, yeah.
[2094.82 → 2105.08] What can happen is it will push and pull on the centre conductors a little bit, which will put stress on the cable endpoints, whatever it's connected to.
[2105.08 → 2117.36] And then from a signal integrity standpoint, yes, it's also potentially bad because now your signal paths may have different links, especially relative to each other.
[2117.90 → 2126.38] And with the differential pairs, you know, it's all about optimizing and keeping those channel links as close to being exactly the same as you can possibly get.
[2126.38 → 2133.66] Yeah, you're going to get a little bit of P and N skew, which means that you're going to have some potential inner symbol interference.
[2134.32 → 2137.78] Because at those speeds and the lengths, that stuff sort of adds up.
[2138.86 → 2139.26] Yeah.
[2139.26 → 2144.48] I mean, in the grand scheme of things, it's, you know, it's very, very small.
[2145.42 → 2150.88] And because of the construction and how we make our cable, it's, I'd say it's minimized.
[2151.44 → 2158.34] But, you know, just like Arian said, I mean, you're getting to speeds where every little bitty thing is starting to count.
[2158.34 → 2170.06] So, yeah, it's doing, it's doing, it's doing the little things that are setting you up for success, as opposed to finding the needle in the haystack when something goes wrong.
[2170.62 → 2170.94] Totally.
[2171.10 → 2175.50] And you, I mean, one of the things I feel I've learned on this is like, you just want to be nowhere near your margin.
[2175.60 → 2178.88] I mean, you want to make sure you've given yourself lots and lots of margins, kind of like the visa bill.
[2179.10 → 2181.34] Any little loss in signal is going to add up.
[2181.34 → 2186.08] And all of a sudden, its lads up to a total loss of signal, and you've got no way to kind of get that back.
[2186.66 → 2187.64] It's really hard to get it back.
[2188.66 → 2190.96] So, Jonathan, do you want to elaborate?
[2191.06 → 2203.58] And I know we talked a bit when we had Doug from Benchmark talking about cabling back when we talked about this episode that we had at Benchmark where we were getting some dropout rates in our cabling.
[2203.58 → 2206.38] And could you talk about that from the Sam tech side?
[2206.54 → 2219.28] Because I was actually, even, you know, being, loving our relationship and being super positive about Sam tech, I was actually taken aback by just how quickly you all jumped in on that.
[2219.48 → 2224.96] So, could you describe a little bit that problem from Sam tech's perspective and kind of your approach on that?
[2224.96 → 2236.74] So, I think this, is this the you're asking about the cable that, where you were having signal integrity issues in Arian, and we were in Oakland?
[2237.18 → 2243.20] We found these cables that had, we had some damage in these cables where, like you said, because of stresses, the solder joints had cracked.
[2244.40 → 2246.58] Because of the way that we'd assembled the rack.
[2246.66 → 2253.38] And we didn't know yet how to treat these cables properly to make sure that you don't get that.
[2253.38 → 2264.38] And so, unfortunately, I wasn't able to make it, but you joined Doug and Robert at Benchmark in Minnesota to think this through and figure out how to do this better.
[2265.60 → 2268.14] Yeah, I was out in the Bay Area.
[2270.04 → 2272.26] Oh, man, was that Design Con?
[2273.44 → 2275.12] Yeah, that was a Design Con time.
[2275.12 → 2283.40] Yeah, and I was able to go out and visit some customers and Oxide was high on my list of people that I wanted to come see.
[2283.64 → 2295.96] And it just so happened that, you know, I think leading up until that point, there was a cable or two that was, you know, showing signs of signal integrity issues.
[2295.96 → 2308.30] And so, when I got there, you know, I started talking about, you know, just like we were talking about, this bending cables in the right direction, making sure other things like you have generous bend radii.
[2308.30 → 2323.74] You know, not putting wire ties on until the very end of the process so that you're not trying to connect a cable that's wire tied somewhere, and you're pulling, you know, you're pulling the end of it while its wire tied tight somewhere else.
[2323.74 → 2325.90] These types of things.
[2326.00 → 2344.92] And so, I remember I had been travelling for quite a bit, and I was sitting there talking with the team and in Oakland and everybody like, yeah, we got to get the benchmark, and we need to, you know, just take a look at a whole unit and look at how it's wired up.
[2345.14 → 2348.84] And I'm like, yeah, I said, I agree 100%.
[2348.84 → 2353.50] You know, we got to go, and we need to get in front of a rack and just take it apart.
[2353.74 → 2356.54] And we started talking, you know, spitballing different ideas.
[2356.96 → 2360.34] And I remember Steve coming over, and he's like, yeah, let's make it happen.
[2360.40 → 2362.10] He goes, let's do it next week.
[2362.18 → 2365.40] And I'm like, man, next week, my wife's going to kill me.
[2366.40 → 2368.38] He says, all right, no, how about two weeks?
[2368.42 → 2369.22] We'll do it in two weeks.
[2369.26 → 2370.76] I'm like, my wife's still going to kill me.
[2370.80 → 2373.92] But okay, I'm like, if I'm not there, I'll get somebody to be there.
[2373.98 → 2376.20] And Steve just looks at me and goes, no, we really want you there.
[2376.26 → 2379.14] I was like, okay, I'll be there.
[2380.74 → 2383.60] And of course, I think it got...
[2383.74 → 2387.08] I think it got pushed out a week from there.
[2387.16 → 2389.24] So I think it ended up being three or four weeks later.
[2389.66 → 2392.64] And so the timing worked out just fine.
[2392.84 → 2394.28] I didn't have any personal issues.
[2394.58 → 2396.76] But once we got into the benchmark...
[2396.76 → 2397.32] Oh, sorry, go ahead.
[2397.72 → 2402.04] Jonathan, it is worth just a quick aside because your base had a New Albany, right?
[2402.44 → 2403.58] I mean, Sam tech is in New Albany.
[2404.04 → 2404.20] Yeah.
[2404.38 → 2405.14] And we're in Indiana.
[2405.14 → 2405.70] Right.
[2405.70 → 2406.02] Right.
[2406.16 → 2408.76] And our manufacturing facilities is in...
[2408.76 → 2411.40] We're at Benchmark in Rochester, Minnesota and Winona, Minnesota.
[2412.06 → 2418.30] And one thing I've definitely appreciated is that the Big Ten Engineering, we got a lot
[2418.30 → 2421.74] of Big Ten alums at Oxide.
[2421.74 → 2425.74] And there is a lot of terrific capability in...
[2426.24 → 2429.74] When people talk about kind of on shoring manufacturing, I mean, we...
[2430.74 → 2433.88] That wasn't a kind of policy position for us.
[2433.94 → 2438.00] That was much more of us being pragmatic and finding real partners.
[2438.08 → 2439.68] And those partners just happened to be onshore.
[2439.68 → 2443.04] But in this case, it was a huge one.
[2443.12 → 2443.76] I mean, if...
[2443.76 → 2449.84] You know, I think if you had to go on a, you know, a 12-hour trans-specific flight, that
[2449.84 → 2452.80] probably would have been a lot less appealing to go to a manufacturing facility.
[2453.22 → 2453.32] So...
[2453.32 → 2456.22] No, but that was exactly the reason why we are doing onshore manufacturing.
[2456.66 → 2459.94] Because we just didn't want to spend all this time travelling back and forth between
[2459.94 → 2463.64] the U.S. West Coast, the U.S. East Coast, and Asia.
[2463.98 → 2464.66] Because it's just...
[2464.66 → 2465.86] And how many times...
[2465.86 → 2469.40] It's time-consuming to debug systems and debug your processes.
[2469.40 → 2470.36] When you have nothing.
[2470.52 → 2471.70] Because we have nothing yet.
[2471.90 → 2473.88] So everything is being built from scratch.
[2473.88 → 2478.28] From our product to our processes to our tools to our manufacturing capability.
[2478.42 → 2480.00] All of that had to be stood up.
[2480.36 → 2485.18] And so when COVID hit, we did deliberately say we want to do this in the U.S.
[2485.18 → 2487.62] Because it'll be just so much easier.
[2488.04 → 2492.26] It'll be so much harder to travel to Taiwan or to China every time we need to do something.
[2492.76 → 2498.52] And again, Robert, our RFK, spent so much time in China that he was like,
[2498.52 → 2499.50] I don't want to do this again.
[2499.50 → 2500.50] Like, it's...
[2500.50 → 2500.64] Yeah.
[2502.20 → 2504.98] Which I'm really glad we did because...
[2504.98 → 2505.94] Oh, really glad we did.
[2506.02 → 2506.40] Oh, my God.
[2506.42 → 2506.90] Can you imagine?
[2507.32 → 2510.50] I actually think that...
[2511.12 → 2512.40] A little bit of a side thing.
[2512.50 → 2514.74] That in our case, onshore...
[2514.74 → 2517.88] Like, manufacturing in the U.S. is actually cheaper than doing it overseas.
[2518.20 → 2519.50] Because of...
[2519.50 → 2523.80] Because not losing all this time and not having to spend all this back and forth and travelling.
[2523.80 → 2528.54] And all of it, basically, to make this happen.
[2531.08 → 2532.74] That has saved us time and money.
[2533.06 → 2535.04] And therefore, I think it is a more efficient solution.
[2535.22 → 2540.56] Whether that's still true in the long run, when you start shipping, you know, many more units, we'll see.
[2540.74 → 2543.08] But at least for now, it is very well.
[2543.74 → 2545.42] That works for us very well.
[2545.42 → 2546.10] So...
[2546.10 → 2549.70] Arjun, it's so good to hear that.
[2549.84 → 2561.90] I think if it's a very labour-heavy, anything that's extremely labour-heavy, then, of course, you know, you want to be in the lowest cost place as far as manual labour is concerned.
[2561.90 → 2570.90] But when you design things in a modular fashion where things can be reused, where the whole assembly process is optimized from...
[2572.00 → 2584.94] When it starts from scratch, as a piece of paper, as Brian mentioned, I think things can be designed in a way where you could easily manufacture this very competitively in the U.S., especially in the Midwest.
[2586.04 → 2586.44] Well, totally.
[2586.56 → 2588.50] And you think, Nathaniel, I mean, how much time have you spent?
[2588.74 → 2590.50] I mean, obviously, okay, too much time in Rochester.
[2590.50 → 2593.90] But, like, that sort of answer is too much time.
[2594.46 → 2595.26] No, we've had...
[2595.26 → 2599.46] I mean, we've had an engineering presence there almost continuous for the last six weeks.
[2600.14 → 2603.22] And, like, you just probably couldn't pull that off overseas.
[2604.32 → 2608.90] And, you know, and, like, with a few of us who live in the Midwest, it's, you know, a few hours over there.
[2608.98 → 2611.22] So in an emergency, you know, it's...
[2611.22 → 2612.88] You know, you can get over there for a couple of days.
[2612.88 → 2618.42] And, I mean, if you're going to spend a couple of days travelling, you know, to get somewhere else, it's not really an option to go for just a couple of days.
[2618.42 → 2620.62] So, yes.
[2620.82 → 2622.22] And I still have larger firms.
[2622.34 → 2625.34] Like, for example, I was working on Oculus products before.
[2625.42 → 2627.98] We had engineering presence at the factory in China.
[2628.32 → 2632.34] But it meant that those were individuals we hired in China, were located in China.
[2633.00 → 2637.66] And still a significant portion of our team was travelling for every build to be present there.
[2637.66 → 2644.60] It was a huge, like, amount of extra, like, overhead is the wrong word.
[2644.70 → 2647.00] It's like it puts a real strain on the team.
[2647.08 → 2649.54] And for a team this size, it's just not feasible.
[2650.90 → 2651.46] So, yeah.
[2651.50 → 2655.58] Anyway, Jonathan, a long way of saying we were really appreciative at that moment of having...
[2655.58 → 2666.58] It was easy for you to really get to the manufacturing facility and look to see, okay, let's sit down, you know, with production engineers and with our mechanical engineer, with Doug, with...
[2666.58 → 2671.72] And really kind of figure out, like, what's going on here to figure out how is this damage occurring?
[2673.32 → 2674.28] Yeah, absolutely.
[2674.28 → 2683.94] Yeah, and, you know, I didn't finish, but we took the cables back that were suspect and basically tore them down, looked at them.
[2684.70 → 2698.64] And, yeah, the solder joint, you could tell, had been cracked, which is evidence of pushing and pulling on those centre conductors and just overbending or putting too much stress on them somehow.
[2698.64 → 2705.10] I mean, there's no real telltale sign, but other than just, you know, too much handling, if you will.
[2706.14 → 2706.56] Yeah, interesting.
[2706.56 → 2707.56] That's what we had kind of come to.
[2708.58 → 2710.64] And so that was, you know...
[2711.16 → 2712.64] Well, your latency...
[2712.64 → 2718.44] We thought it was so important to get up there and go through a system with you guys.
[2719.12 → 2724.76] And your latency from actually taking those damaged cables and actually getting them...
[2724.76 → 2726.00] I think you were getting them imaged.
[2726.12 → 2728.22] I can't even x-ray them or not, but you could get them imaged.
[2728.22 → 2730.22] And inspecting them and...
[2730.96 → 2732.56] I mean, how frustrating...
[2732.56 → 2734.84] I mean, for so many things that I've had...
[2734.84 → 2739.88] Adam, how many things have we had in our career that gets sent back to a manufacturer only to be told that there's no fault found?
[2740.38 → 2740.76] I mean...
[2740.76 → 2741.50] Yeah, exactly.
[2742.16 → 2745.70] And it gets so frustrating to hear over and over again that there's no fault found.
[2746.18 → 2746.72] So the...
[2746.72 → 2749.60] And it just feels like, are you actually, like, trying to find a fault in this thing?
[2749.68 → 2750.22] Or are you...
[2751.22 → 2752.22] And the...
[2752.86 → 2754.90] So for you all to not just...
[2754.90 → 2757.52] Not only, like, actually, yes, find damage,
[2757.52 → 2758.90] but find it quickly.
[2758.90 → 2760.14] And I think this is, like...
[2760.14 → 2761.30] It just goes to the disposition.
[2761.52 → 2763.62] Like, your disposition was not...
[2763.62 → 2765.60] How can we exonerate Sam tech here?
[2765.88 → 2768.78] Which honestly feels like the disposition often in the industry.
[2768.78 → 2771.22] It's like, you've sent me this failing component.
[2771.48 → 2773.92] My job is to prove to you that this was not my fault.
[2774.64 → 2776.78] And it's like, that's really not your job.
[2776.98 → 2777.42] It's your job.
[2777.42 → 2782.48] It's like, we, us together, we have something that has failed.
[2782.84 → 2787.00] And we need to understand why that has failed so that we together...
[2787.00 → 2788.88] And it's like, just a lot of people don't have that disposition.
[2789.18 → 2793.34] And you very much did in terms of, like, getting understanding, where's this damage coming from?
[2793.38 → 2794.68] And then where could it be coming from?
[2794.72 → 2797.32] It's like, no, this is not, like, Sam tech's fault.
[2797.82 → 2799.74] But it's like, this thing is busted.
[2799.74 → 2801.16] How did it get there?
[2801.34 → 2807.82] And how can we help brainstorm different ways to handle this thing, manufacture it, such that we don't break it?
[2807.90 → 2809.28] It's like, that is so refreshing.
[2809.42 → 2810.72] It's a very refreshing disposition.
[2811.24 → 2816.48] I think, luckily, the physics we use is the same as the physics you use and everybody else uses.
[2818.10 → 2819.72] You know, that's not always the case, though.
[2819.84 → 2823.14] I feel like I'm alternating in a different physical reality than a lot of these vendors.
[2824.70 → 2827.66] So, yeah, thankfully, the same physics, for sure.
[2827.66 → 2831.04] And I would say, I was there on site when Jonathan was up.
[2831.20 → 2837.78] And it was just really awesome to see Jonathan and Doug and Eric and RFK, like, everybody roll up their sleeves.
[2837.92 → 2850.08] And they're all, you know, elbows deep in the rack, pulling cables out and re-bundling things and, you know, talking through how we might change the way our design mechanicals are to facilitate, you know, these nicer bends.
[2850.26 → 2857.10] And so it was just, it really felt like a whole team kind of all standing there working together, even though, you know, it's like three different companies.
[2857.10 → 2857.92] Three different companies.
[2858.22 → 2858.40] Yeah.
[2858.70 → 2865.88] And that is, and Jonathan, I mean, I'm not sure if this is par for the course for you or not, but I think it's, that's really special from our perspective.
[2865.88 → 2876.26] When you're able to really have that kind of collaboration across a bunch of different folks who are outside their own self-interest and really looking at, like, what is the how do we kind of build this thing and get it working together?
[2876.26 → 2883.54] Yeah, I think it comes back to what you, you know, what you've said a couple of times is we're, we're building this thing together.
[2883.54 → 2893.48] And, you know, it's, we certainly have some customers that are just, oh, just, you know, give us the spec, give us this, you know, just throw it over the wall to us.
[2893.48 → 2905.02] But when, when we have customers like Oxide that take the time, want to fully understand, want, want and ask additional questions, looking for that support, we're going to give it to you.
[2905.02 → 2911.96] And, and you guys do the same thing with other vendors and, you know, even with your customers, and we do it with our vendors.
[2912.52 → 2915.34] So I think we're all the same, same mindset.
[2916.24 → 2917.26] A hundred percent.
[2917.46 → 2931.06] And you're exactly right that, I mean, we have very much that model with our own customers because it's very important that like, you know, like your, your customers, like Oxide, we're a technical customer and Oxide's customers are technical.
[2931.06 → 2934.70] And, you know, we are building something together.
[2934.86 → 2946.76] And in our case, we are helping them to deliver a service to their customers who are, they are often in the walls of a company, sometimes outside the walls of the company, but ultimately we are helping them deliver something.
[2947.64 → 2955.80] And we want to be sure that if, if that, if that's not working for them, that we have all the right people in the room together to figure out how do we fix this for you?
[2955.84 → 2956.74] How do we write that for you?
[2956.74 → 2960.42] And Adam, just to say to the top, I feel like that's something we really inherited from Sun.
[2960.42 → 2968.56] And I do think that that is something that Sun got really right is we always felt empowered to do the right thing by our customers.
[2968.56 → 2972.82] And I never felt like we had to justify doing the right thing by a customer.
[2973.72 → 2973.92] That's right.
[2974.04 → 2981.82] And that's how we spent a bunch of our early careers with customers making things right or fixing things or making things right.
[2981.82 → 2988.40] Even when, just as in this case, you know, irrespective of where the blame, as it were, lay.
[2989.08 → 2993.22] But how do we make them successful with our product, whether it's our bug or their bug?
[2993.22 → 3001.30] And, you know, honestly, like we're so used to this that it was kind of foreign to me that any company wouldn't, like, why wouldn't you not do this, right?
[3001.30 → 3003.70] Obviously, this is the only way to do business as far as I'm concerned.
[3004.34 → 3006.72] That you, of course, you're always invested in your customer success.
[3006.72 → 3009.40] And it was a little bit jarring.
[3009.54 → 3021.60] I got so, I don't know, I don't get the same disposition, but I think I got, like, so used to that, that when I first kind of encountered companies in the wild that didn't have that disposition, it was, like, pretty shocking.
[3021.60 → 3040.22] And I remember in particular, we had a company, I was demonstrating D-Trace, which Jonathan and Bigness, this is a technology that Adam and I developed together to allow you to dynamically understand what a software system is doing to basically answer the question, like, why is the software system not performing?
[3041.02 → 3046.68] And generally, this is very positively received because who wouldn't want to know what their software system is doing?
[3046.68 → 3050.24] But this particular customer received it very, very poorly.
[3050.68 → 3059.46] And in particular, they didn't want their customers to be able to run this on their software to understand how bad their software was.
[3060.78 → 3064.04] So the and I can review it in this meeting or not, this meeting did not go well.
[3064.20 → 3066.88] I was not really braced for a customer.
[3067.08 → 3070.26] In particular, the customer was like, you have to disable D-Trace on my software.
[3070.26 → 3075.90] Like, I will not support my software on your platform until it cannot be instrumented with D-Trace.
[3075.90 → 3077.80] Which was not something that I...
[3077.80 → 3079.44] I'm sure that was a good opening salvo.
[3079.54 → 3081.32] I'm sure you toned that down afterwards.
[3082.46 → 3088.24] Yeah, I don't think I've ever had to be escorted out of a meeting by the sales folks who, it just did not go well.
[3088.34 → 3089.64] It went really, really poorly.
[3090.08 → 3096.80] In part because we had spent the first half of the meeting where they were trying to understand why their software is performing so badly on us.
[3096.80 → 3100.32] And it's because they were shipping debug binary with debug symbols.
[3100.32 → 3105.70] And it was when I ended up, but they told me like, sorry, like we can't rebuild it.
[3105.76 → 3106.54] We can't optimize it.
[3106.64 → 3116.84] And it was when they told me that they wouldn't certify D-Trace that I volunteered that I was going to write a tool to allow their customers to extract their source code from the binary because it had all the stabs' information.
[3116.98 → 3118.10] Like the source code was all in there.
[3118.80 → 3118.90] Yeah.
[3119.62 → 3121.80] That sounds like the right time to escort you from the room.
[3121.80 → 3122.80] Yeah.
[3124.80 → 3126.52] It clearly learned a little bit.
[3126.72 → 3129.42] So to do bring that back, though.
[3129.52 → 3129.72] Yes.
[3129.90 → 3135.86] I think that a lot of companies don't necessarily do this on purpose.
[3136.06 → 3137.74] It's not that they don't want to help their customer.
[3137.74 → 3156.30] I think that for some reason in a lot of places, the people don't have the ability to do it because either the information or the knowledge is spread so wide and so, but not positively that it's difficult to actually find the people who can and bring them together to solve a problem.
[3156.66 → 3159.88] Let alone if you have to do this with three, two or three companies.
[3159.88 → 3167.28] And then there's a bunch of politics involved with all that, which makes it usually like adds a whole nother dimension to it.
[3167.72 → 3172.30] And so, the only response that a company can then have is like, this is not a problem.
[3172.36 → 3175.22] This can't be our problem because, of course, we designed it properly.
[3175.60 → 3188.20] Because if it was not, like if there is a problem, then they don't have the ability to figure out what is wrong and how to fix it, which is a pretty bad place to be in, obviously.
[3188.20 → 3193.08] But I'm willing for a lot of places to not have it be on purpose.
[3193.28 → 3195.06] I think this is just sort of like what happens.
[3195.62 → 3200.84] This comes back a little bit to the other cable manufacturer that we were trying to work with.
[3200.90 → 3205.64] It wasn't that they didn't want us to succeed in that sense.
[3205.72 → 3215.14] It's just that they were in their way of having too many people involved to even get a set of drawings out and to give us feedback on a pinout and on how this mechanically was going to fit.
[3215.14 → 3220.52] It was not that they didn't want it because they clearly wanted our business, I think, or at least I hope so.
[3221.34 → 3224.66] But they just couldn't figure it out between all of them.
[3225.20 → 3225.78] Yeah, totally.
[3226.48 → 3226.64] Yeah.
[3226.86 → 3234.46] And what's unique about Symptom in that case is, you know, say Jonathan is actually the product manager for all backplate products.
[3234.46 → 3239.28] And I'm a technologist for multiple of the high-speed products.
[3239.84 → 3245.44] We don't only give internal direction on what the next generation architecture should look like.
[3246.04 → 3253.12] We're also involved with customer issues on existing, because if you understand the problems that you have on existing products,
[3253.12 → 3259.08] and we can't deal with all the customers, but at least leading customers, then we can design next generation better.
[3259.66 → 3264.72] And usually in the other companies, it's not the same person doing both.
[3265.22 → 3265.98] And that's the issue.
[3266.72 → 3268.58] Yeah, that's a critical piece.
[3268.74 → 3269.90] That's an important point, Dinesh.
[3269.98 → 3274.92] You need to be subjected to your own decisions and the consequences of your own decisions.
[3275.06 → 3280.26] Only then will you learn how to improve, like how to make your product better.
[3280.26 → 3290.98] Well, and this is something that I believe very, very strongly in, that you should take responsibility for your ideas all the way from that initial ideation all the way to actually running in production.
[3291.40 → 3302.28] And it is really important to do that because you then, I mean, it cannot underscore enough what you're saying in terms of like, you should not view it kind of pejoratively.
[3302.52 → 3308.26] Those things that are running in production, those systems have a lot to teach you about your next generation designs.
[3308.26 → 3310.08] But you have to go listen to them.
[3310.18 → 3320.80] You have to like, and the other thing that, you know, the thing that you hate to hear but happens way too frequently is folks being told that you're the only one seeing this problem.
[3321.02 → 3330.80] This is another thing that like, and it happens way too frequently in the industry that, you know, you all never do because it's like, it doesn't matter to somebody if they're the only one seeing the problem.
[3330.90 → 3332.02] It doesn't even matter if it's true.
[3332.02 → 3335.34] It's almost always false, but like, it doesn't even matter if it's true.
[3335.46 → 3343.38] Like never tell somebody you're the only one seeing this problem because what you're effectively saying is that like the rest of the customer base has somehow outvoted you.
[3343.38 → 3343.78] More important.
[3344.48 → 3345.14] More important.
[3345.14 → 3346.14] Yeah.
[3346.14 → 3346.16] Right.
[3346.16 → 3346.66] Yeah.
[3346.66 → 3353.60] And it's like the and you know, there are other, if, if what you're trying to phrase is like, wow, this is really unusual.
[3353.60 → 3359.88] Like say that, you know, it's like, or I play, you know, I need to understand like what is in this environment.
[3359.88 → 3363.08] What makes it, I need to understand why we're seeing this here.
[3363.08 → 3363.80] That's fine.
[3363.80 → 3365.64] But like when you're telling me, you're the only one seeing this problem.
[3365.64 → 3366.94] It's like, oh God, so frustrating.
[3366.94 → 3376.98] And it just shows how many, how few companies take your approach of actually having folks that are coming both from the design side, going all the way into the customer base and actually understanding this thing.
[3378.48 → 3378.88] Yeah.
[3381.72 → 3389.80] And I feel like Adam, this is the, the kind of it's dovetailing into our, our cackle bladder episode, which I can't even remember the better title of.
[3389.80 → 3393.30] I was able to use crackle bladder and catch a conversation.
[3393.44 → 3395.20] That's all I remember that we were talking about.
[3395.26 → 3404.94] I think this is the I know this, this is UNC episode, but we talked about customer support and why, and how important it is to actually be, to, to really walk with your customer with their problem.
[3406.22 → 3407.52] I think it was interesting.
[3407.52 → 3417.02] Like some of the very early conversations with Oxide, I had a couple like one-on-one calls with Arden after I'd sent him some samples.
[3417.02 → 3421.68] And I think they were just like mechanical samples that like even down to the component level.
[3422.44 → 3427.88] And I remember talking with Arden, like, I don't know, I'm on East coast, he's on West coast.
[3428.00 → 3437.50] So I think it was like Friday at five o'clock and, and we're, he's asking me questions about all this just mickey.
[3437.52 → 3443.22] I knew level detailed questions about the components, not just, not like, like overall cable assembly.
[3443.22 → 3447.24] It's, it's like down to the, the copper that we use.
[3447.76 → 3452.66] And I was just blown away because I think at one point I told him, and this is still true.
[3453.06 → 3459.38] I don't think I've had any other customer ask me the level of detailed questions that Arden has asked me about our cables.
[3459.94 → 3460.42] Really?
[3460.70 → 3461.18] Oh, interesting.
[3461.44 → 3461.68] Wow.
[3461.68 → 3467.50] I mean, I don't get involved at some of the Bigness is like more of a technologist.
[3467.50 → 3469.12] Have you heard him say that in his title?
[3469.28 → 3473.88] So he's, he gets involved in like some of the super far out conversations.
[3473.88 → 3483.16] I'm, I'm just a lonely old product manager, but still I talked to, I talked to customers all the time and I still have not had that level of detail.
[3483.16 → 3490.38] And I guess where I was going with that is that it's just the level of, you know, the, the level of detail that Oxide goes into.
[3490.62 → 3493.88] And I'm sure you do this, and I know you do this with other vendors too.
[3494.16 → 3498.98] And that's helping out that partner relationship kind of closing back up to that loop.
[3498.98 → 3501.56] Um, and that's just so important.
[3502.70 → 3509.54] Well, it has a very specific reason why I, why I asked those questions because so I took all your samples and took them apart.
[3509.54 → 3510.72] I cut things open.
[3510.72 → 3520.10] I, I, I pried out those little, like little metal tabs that go in the side of the connectors and then took all the wafers out and looked at the wafers and scraped some of the wafers off and besotted some pieces.
[3520.10 → 3527.06] Because one of the things I really don't want to have happened is us designing a cabled backplate.
[3527.30 → 3533.22] And at some point a customer coming back and be like, Hey, this, we don't trust this cable backplate because we see failures.
[3533.22 → 3538.38] Or we've had some of these conversations already with some of our customers or prospective customers.
[3538.38 → 3546.14] And the first thing they, they hear when they hear we're doing a cabled backplate, they have in mind these connectors with straight pins.
[3546.14 → 3550.64] And they think about bend pins and how one, one unit goes from one slot into the next.
[3550.64 → 3558.32] And, you know, as a virus goes through your rack, and you bend out, you bend everything, your cables, your connectors, your chassis, like all of it is at some point broken.
[3558.86 → 3568.76] And so I really want to make sure that I understand how this thing mechanic works mechanically, electrically, so that we make these decisions appropriately.
[3568.76 → 3578.42] And that I can ultimately stand behind this design because I don't, I just don't want to be called out of bed at three in the morning because these cable systems have failed.
[3579.58 → 3581.68] I've done enough pager duty at this point.
[3581.86 → 3584.74] And so I don't want you to either because you'll probably call me.
[3585.26 → 3594.76] No, but that's been really helpful because, because for example, there, there, there is, there was a particular engineer or a particular person at a particular prospective customer we're talking with.
[3594.76 → 3597.24] And then this person kept on pushing back on his cable backplate.
[3597.28 → 3609.36] And I made a short presentation for it specifically for him explaining how these, how, how the XMX connectors work and how you have these counter, like these counter opposing fingers that then, that, that, that insert.
[3609.36 → 3611.78] And that basically get pushed away from each other.
[3611.88 → 3613.42] And that's how you get tension between them.
[3613.42 → 3625.88] And that it is very difficult to, if used appropriately to get these connectors to be bent or these fingers to be bent and cause problems in other connectors that like where they aren't made it.
[3625.98 → 3634.94] You may not have a connection when these things, if you bend these fingers far enough, then sure, your connection won't work, but it won't damage other connectors that you're inserting these into.
[3634.94 → 3639.42] And so being able to explain that and being able to, like, I took these things apart.
[3639.82 → 3641.78] I've, I've, I've looked at this, this is how it works.
[3641.78 → 3653.64] And then we worked with Doug to make sure that our mechanical solution has enough float in all the directions so that, you know, when these things made that they made appropriately, not, not too fast, not, and that, that we, they made far enough, all that, all that good stuff.
[3653.64 → 3661.60] Because I wanted, I just wanted to make sure that we, we really dotted our I's and crossed our T's here because we're, we're, we're, we're betting the farm on this.
[3662.22 → 3662.70] Yep.
[3662.70 → 3662.82] Yep.
[3663.82 → 3665.38] There's no going back at this point.
[3665.50 → 3666.10] We can't.
[3666.40 → 3669.62] And then you were talking, you were talking about a backplate not made up PCB material.
[3670.00 → 3671.86] We just can't, there's not enough signal integrity.
[3672.00 → 3676.28] Like there's not enough, uh, insertion loss budget to do this out of a PCB.
[3676.58 → 3678.18] It is, it is going to be this or bust.
[3678.86 → 3680.30] I think now you're hooked.
[3680.50 → 3680.74] Right.
[3680.80 → 3683.04] As in, once you design with cable, you're never going back.
[3685.68 → 3687.44] Well, actually now I want the next thing.
[3687.44 → 3692.56] I want, I want a fibre optic link because then I, because I can't push, I can't push copper much further.
[3692.56 → 3693.86] Than what we were going today.
[3693.86 → 3696.68] Uh, I, I will disagree with you on that.
[3696.68 → 3699.48] And we can talk about it some other time, but yes.
[3700.28 → 3700.54] Yeah.
[3700.90 → 3701.86] Uh, copper.
[3701.86 → 3707.78] Every time people say copper has every, at every data rate, people say that's the end of copper.
[3707.78 → 3708.42] Now it's five.
[3709.24 → 3709.68] Optics.
[3710.18 → 3712.92] And so let me, let me put the asterisk here.
[3712.92 → 3718.48] Unless we can move the connector closer or even onto the package of the ASIC itself.
[3718.48 → 3723.80] If you can do that, then suddenly we have seven, eight DB extra, extra loss budget.
[3723.98 → 3724.22] And yeah.
[3724.22 → 3726.18] Then we can push copper again further.
[3726.42 → 3733.38] And, and, and Sam tech already has one that we, we got our first ending samples now.
[3733.38 → 3740.36] Where the density of that connector is better than even any silicon photonics engine that is available in the market.
[3741.32 → 3745.70] So just to give you a perspective, it's, it is 64 differential pairs.
[3745.96 → 3751.26] So think of it as 32 TX and 32 R in half inch by half inch footprint.
[3751.26 → 3755.48] So can you elaborate a little bit, Bigness?
[3755.58 → 3758.32] Because I think this is something, it's a question that we do get from time to time.
[3758.46 → 3760.36] People are like, well, isn't, aren't optics the right way to do this?
[3760.44 → 3760.50] Right.
[3760.58 → 3762.84] Actually like not, it's certainly not right now.
[3762.94 → 3763.96] It's, it's copper.
[3764.34 → 3771.94] And I think that, that you're saying that like people really underestimate copper and that, you know, everyone says that kind of copper is going to disappear.
[3771.94 → 3775.08] But actually I could, could you elaborate on that a little bit?
[3775.08 → 3780.92] Like why is copper still like the, the, the right way to build these kinds of systems?
[3781.26 → 3781.86] Okay.
[3781.96 → 3792.16] I think it's good to look at, not just from the signal integrity point of view, but just overall system and your customer point of view and your, our customer and your customer point of view.
[3792.32 → 3806.48] If you have a switch, what the current front panel, you know, like QSFPs and DDs and OS FPs allow is for you to ship a switch without optics in it, for example, or for people to, without optics.
[3806.48 → 3809.26] And then the customers can put whatever optics they wanted.
[3809.26 → 3809.48] Right.
[3809.48 → 3814.90] So customers will always prefer to have front panel optics if possible.
[3815.42 → 3815.94] That is one.
[3816.54 → 3816.64] Yep.
[3816.76 → 3829.06] The second one is what Arden talked about earlier with the current things where you don't want to keep your temperature sensitive optics very close to a high-powered heater, AKA the chip.
[3829.06 → 3835.90] So if you can separate the two, the light of the and the reliability of the optics is significantly higher.
[3836.38 → 3845.78] There is an Arden's law, which says, you know, as the temperature increases by 10 degrees Celsius, the lasers' reliability decreases by two X.
[3846.44 → 3849.80] So you want to keep, you want to keep the optics as low temperature.
[3849.80 → 3856.08] So there is a, there are, there are reasons why you want to stay up, keep optics away from the chip.
[3856.08 → 3856.52] Right.
[3857.06 → 3862.36] And, and so, and copper is just a dumb passive, copper cable is a dumb passive.
[3862.66 → 3866.42] They, they are, they can withstand the same temperature if not higher than what the silicon can.
[3866.42 → 3879.10] And so if you can do that, I think people will always will try to, if there's some technology that allows you to do that, to still have front panel optics, they will still go for that.
[3879.70 → 3881.42] So, so there's, there's that.
[3881.52 → 3890.26] Then the other part, the big part for me is power consumption, because the reason you don't do optics is that your chip inherently has copper signals coming out of it.
[3890.26 → 3899.46] Because that's like, there's, there's, there's, there's wire bar, there are bumps under your, under your, like, if you go like all, like the dye itself has pads.
[3900.20 → 3901.56] There are bumps on those pads.
[3901.66 → 3902.94] You go onto a package, whatever.
[3904.22 → 3905.98] That is copper by definition.
[3906.80 → 3913.54] The so if you go to an optical engine that is off chip or even on package, but still off dye.
[3913.54 → 3922.24] Now you, you're spending, you're spending power to go from one interface through a little bit of substrate or whatever that is into an optical engine and then optical.
[3922.48 → 3926.04] That optical conversion process obviously costs power and then you, you go out.
[3926.60 → 3938.92] So, so that, that is, that, that usually, that, because that will lose against any, if you have a passive copper solution, then yes, that will always be more power efficient because you don't do that conversion.
[3938.92 → 3946.22] Now, that might change a little bit once you start talking about these integrated photonics that go on the chaplet on the package.
[3946.84 → 3949.40] I've got, Adam, I have silicon photonics on my mango card.
[3949.52 → 3950.54] I assume you do as well.
[3950.90 → 3951.26] I'm not sure.
[3951.34 → 3951.74] Do you have a mango?
[3951.96 → 3952.82] You have a mango for me, for sure.
[3952.84 → 3954.10] Okay, yeah, very, exactly.
[3954.90 → 3962.74] So this, yeah, this is where you would integrate the photonics into an actual chip piece that then goes into your, onto the same package as your ASIC.
[3962.74 → 3971.54] And now some of these, these, these equations change a little bit because you can use the lower, the lower power interfaces between the two chaplets.
[3971.74 → 3978.08] So you're, you're talking now stuff like what you see AMD do with their chaplet designs for their CPUs and their GPUs.
[3978.22 → 3988.74] And I, I, I don't know whether that changes enough because you could now potentially shave off the studies and not, not do this conversion twice.
[3988.74 → 3991.74] And now you, you could, you could do it in sort of one step.
[3994.08 → 3995.16] And so, I don't know.
[3995.24 → 3999.34] So at some point there is an there is a crossover point where that starts to make sense.
[3999.34 → 4006.62] But then we, we would have to start thinking about how to blind mate optical links, which is, you know, I think doable.
[4007.06 → 4012.60] Just, it's all a sweat and tears to get it done and money.
[4012.72 → 4012.82] Right.
[4012.94 → 4018.78] But the PowerPoint is also a perfect one because it's like, and I know this is a concern that Eric had when we were going to compliance,
[4018.78 → 4024.38] that we are not going to have thermal monitoring on those QSFP ports, and we're going to burn the thing down.
[4024.50 → 4027.84] And you look at like the potential power consumption of those things is really high.
[4028.46 → 4035.46] So this is actually, I mean, you know, as you said already at the top, we got, you know, potentially like 300 watts out there in, in ports.
[4035.46 → 4041.18] So it's, it's, it's a good point about that.
[4041.42 → 4044.24] Lasers are actually, as it turns out, pretty power hungry.
[4045.18 → 4049.42] And there's, there's a real power argument to be made once you're, you're already in copper.
[4049.56 → 4056.88] So staying in copper, if you possibly can, is going to have a bunch of wins in terms of thermally and mechanically and so on.
[4057.44 → 4057.88] Yep.
[4057.88 → 4064.50] And to your point, right, if you can convert directly from the package itself, that saves a lot of loss.
[4064.50 → 4070.80] And the other is, can the, can the copper cable, the Twin itself be made lower loss?
[4070.92 → 4071.94] And the answer is yes.
[4072.04 → 4076.68] Our next generation cable, you know, Jonathan talked about that.
[4076.78 → 4079.18] It has a dielectric around the two copper conductors.
[4079.26 → 4080.80] It's a solid dielectric right now.
[4081.78 → 4085.98] And, and so what we are working, what we're calling it Twin air,
[4085.98 → 4092.18] but basically what we're doing is we are putting air voids in that solid dielectric
[4092.18 → 4095.14] so that the net dielectric is significantly lower.
[4095.28 → 4099.16] So the loss in these cables will be around 20% lower than the current cables.
[4099.90 → 4100.04] Wow.
[4100.04 → 4103.70] So as you, as you go to the next data rate of 224 gig,
[4104.26 → 4109.78] that's where the next generation cables will start becoming more.
[4109.78 → 4115.16] So, so we're, so we're basically trying to recreate the, the ideal physical model
[4115.16 → 4118.40] that we're all being taught in school or that you're being taught in school.
[4118.40 → 4124.96] And then, or like suspend two copper conductors in absolute like space in,
[4124.96 → 4131.18] in like low, low temperature, low temperature vacuum, uh, speed of light.
[4131.18 → 4131.20] That's right.
[4131.26 → 4131.88] That's what you modelled.
[4131.88 → 4133.02] Yes.
[4133.92 → 4134.16] Yeah.
[4134.40 → 4134.96] Nice.
[4134.96 → 4136.64] We finally have that frictionless surface.
[4137.42 → 4137.78] Yes.
[4139.40 → 4139.88] Yeah.
[4139.88 → 4145.74] And so we have, uh, like, uh, our first engineering samples of those type of cables
[4145.74 → 4146.64] already available.
[4148.12 → 4149.26] And just very on brand.
[4149.44 → 4152.60] It's like the and, and actually if everyone looks under the chair right now,
[4152.66 → 4155.04] you'll see the sandwich has already left a sample for you.
[4156.40 → 4158.66] You get a sample, and you get a sample.
[4158.66 → 4168.56] So that is honestly amazing that there's another 20%.
[4168.56 → 4174.32] I mean, that's a huge difference in, uh, in, you know, kind of, you,
[4174.50 → 4177.40] again, Alien, you made this point earlier, but like, you know, cabling,
[4177.50 → 4178.82] like how complicated can it be?
[4178.86 → 4181.96] It's like actually really, really complicated and really, really,
[4181.96 → 4182.58] really important.
[4183.22 → 4183.40] Yeah.
[4183.64 → 4185.98] And really important because it's like, boy, you think of that,
[4185.98 → 4190.52] that 20% loss that has a 20% improvement and loss has got ramifications for
[4190.52 → 4191.36] power.
[4191.50 → 4192.48] It's got ramifications for SI.
[4192.56 → 4194.80] It's got all these ramifications up and down the system.
[4195.46 → 4195.78] Um,
[4195.78 → 4199.38] because the 20% is, is, is combined with,
[4199.52 → 4204.52] because every generation of these systems, the receivers get better,
[4204.52 → 4208.24] meaning the receivers turn more and more into radios,
[4208.24 → 4213.24] meaning they're bigger because you need more silicon to more,
[4213.46 → 4213.84] uh,
[4213.84 → 4218.32] and you're actually using analog circuitry a lot to make these receivers more,
[4218.42 → 4219.16] more sensitive.
[4219.96 → 4220.48] Um,
[4221.54 → 4224.04] meaning you're spending more and more of your silicon area to,
[4224.16 → 4224.64] to do this.
[4224.66 → 4227.46] So this is another reason why chaplets at some point become such an
[4227.46 → 4230.74] interesting thing is because these analog front ends that you want in these
[4230.74 → 4232.78] 30s have very different, uh, uh,
[4232.78 → 4235.46] silicon properties than your digital logic,
[4235.46 → 4238.04] which is like tiny, and you want the latest node,
[4238.14 → 4239.28] but for your analog circuitry,
[4239.28 → 4240.92] that doesn't really work that all that well.
[4241.00 → 4242.80] So there's a different trade-off that you need to make.
[4242.86 → 4245.14] So at some point cutting these in different pieces and making them,
[4245.60 → 4246.48] jabbing this on different,
[4246.48 → 4250.18] different nodes in order to basically get the best out of each of these
[4250.18 → 4250.66] interfaces,
[4250.66 → 4252.28] it will become important.
[4252.54 → 4254.26] But as these interfaces become,
[4254.42 → 4255.86] as these receivers become better,
[4256.06 → 4256.62] you know,
[4256.82 → 4257.20] another,
[4257.36 → 4257.56] if you,
[4257.64 → 4259.70] if you can eke out another 20% on the interface,
[4259.82 → 4261.46] on the receiver or 25%,
[4262.04 → 4262.46] uh,
[4262.46 → 4264.62] then all these things stack up and that,
[4264.62 → 4264.82] that,
[4264.82 → 4265.04] that,
[4265.04 → 4269.62] that does mean that you can suddenly do these higher data rates at these
[4269.62 → 4272.40] longer lengths of cable that we want to run them at because our,
[4272.40 → 4272.68] our,
[4272.68 → 4273.26] our channel,
[4273.62 → 4274.68] our total channel length is,
[4274.68 → 4275.08] is,
[4275.08 → 4275.94] is the
[4276.00 → 4276.96] the cable is about,
[4276.96 → 4278.50] uh,
[4279.06 → 4279.88] uh,
[4280.10 → 4280.90] about six feet,
[4281.14 → 4282.08] six,
[4282.20 → 4282.62] seven,
[4282.88 → 4283.52] six feet.
[4284.30 → 4284.80] Um,
[4284.80 → 4286.30] that's the longest channel that we have.
[4286.30 → 4290.52] And we play some games with making sure that the longest cables are paired with
[4290.52 → 4296.36] the shortest traces on the print circuit board so that we borrow basically some margin out of the printed circuit board and put it back in cable.
[4296.36 → 4297.20] And likewise,
[4297.20 → 4298.00] so,
[4298.00 → 4298.86] uh,
[4298.88 → 4299.10] yeah,
[4299.86 → 4302.40] although these are all games that we play in order to make that work.
[4302.40 → 4303.02] And so,
[4303.20 → 4303.78] but yes,
[4303.88 → 4309.30] I'm a little bit hesitant to start thinking about 112 gig link,
[4309.30 → 4309.92] uh,
[4309.92 → 4310.40] because that,
[4310.46 → 4310.90] that's,
[4310.90 → 4311.48] uh,
[4312.04 → 4313.28] yeah,
[4313.42 → 4313.68] well,
[4313.84 → 4315.52] because we just have to do more modelling.
[4315.64 → 4315.84] That's,
[4315.90 → 4316.20] that's what,
[4316.32 → 4317.26] that's what it comes down to.
[4317.26 → 4321.18] And these blind mate interfaces become more important.
[4321.32 → 4323.12] Like the consistency of blind mating,
[4323.12 → 4325.00] these will become that,
[4325.08 → 4325.22] that,
[4325.32 → 4325.82] that's where the
[4325.88 → 4326.72] where this goes,
[4326.76 → 4332.32] because you need to be able to make them consistently every time the same way within the specification of the connector.
[4332.84 → 4333.20] Um,
[4333.52 → 4334.52] so I don't know,
[4334.58 → 4335.18] fun challenges.
[4335.68 → 4339.70] So Nathaniel is saying that Silicon Photonics has been one year away from mainstream for quite a few years.
[4339.78 → 4342.32] I would like to thank you for acknowledging that it's been 18 months away,
[4342.46 → 4343.18] which is the
[4343.28 → 4343.48] you know,
[4343.54 → 4346.04] when someone is saying something's a year away,
[4346.04 → 4347.36] that's just a little too tangibly close.
[4347.42 → 4347.54] It's,
[4347.62 → 4348.08] it's when it's,
[4348.14 → 4349.72] they're talking like 18 to 24 months.
[4349.72 → 4349.98] It's like,
[4350.00 → 4350.16] all right,
[4350.16 → 4352.64] that's just far enough away to not be verifiable.
[4353.28 → 4353.60] And I,
[4353.64 → 4353.82] yeah,
[4353.82 → 4354.32] I joke,
[4354.40 → 4355.06] but you know,
[4355.10 → 4362.18] I've been doing this for 16 years and I feel like Silicon Photonics has been one year away from mainstream for most of that,
[4362.18 → 4362.68] you know,
[4362.68 → 4363.74] depending on who you talk to.
[4364.00 → 4364.84] And so,
[4365.00 → 4365.36] you know,
[4365.54 → 4365.86] I mean,
[4365.86 → 4366.08] there's,
[4366.14 → 4367.28] there's interesting stuff there.
[4367.36 → 4367.70] And I mean,
[4367.70 → 4371.20] certainly the like things like chaplets and stuff give that more legs.
[4371.20 → 4375.18] Because you do have that problem where it's like your new ASICs want to be on,
[4375.18 → 4375.56] you know,
[4375.56 → 4376.36] super high end,
[4376.48 → 4377.58] tiny little transistors.
[4377.58 → 4380.56] And then your photonics maybe want some different technology there.
[4380.84 → 4381.56] So anyway,
[4382.36 → 4383.12] but I do think that.
[4383.68 → 4385.32] Photonics are going to be this one thing in my career.
[4386.12 → 4388.92] All these different manufacturers are going to hold this in front of me.
[4388.94 → 4391.86] They're going to dangle this carrot every time we're designing something.
[4392.02 → 4394.12] And I'm going to get hopeful every time.
[4394.34 → 4394.58] And I,
[4394.58 → 4395.24] and I,
[4395.24 → 4395.60] I'm,
[4395.60 → 4396.14] I'm already,
[4397.60 → 4397.78] well,
[4397.84 → 4399.14] I'm just going to go out and say it.
[4399.14 → 4401.38] Intel has already stomped on my heart twice now.
[4401.38 → 4402.54] And so it's,
[4402.54 → 4403.48] it's painful.
[4403.48 → 4404.30] Intel are you listening?
[4404.86 → 4404.96] Right.
[4405.16 → 4411.74] Should we tell him that we have a pre-meeting mailing list that we tell all the vendors to dangle Silicon Photonics out in front of him?
[4412.16 → 4412.56] Nathaniel,
[4412.60 → 4413.00] I told you,
[4413.06 → 4414.26] you're not the only thing about that.
[4414.36 → 4414.58] It's a
[4414.66 → 4415.58] it is important that,
[4415.72 → 4416.62] that we know that,
[4416.76 → 4416.86] listen,
[4416.98 → 4417.68] Arian's easy.
[4417.82 → 4418.38] He's a
[4418.84 → 4419.18] but Arian,
[4419.32 → 4419.86] I'd actually,
[4419.98 → 4420.10] you know,
[4420.12 → 4420.20] we,
[4420.30 → 4421.30] we kind of tease you about it,
[4421.32 → 4422.50] but I love the
[4422.60 → 4422.98] you know,
[4423.44 → 4426.82] like constantly like looking forward and kind of getting creative is,
[4426.82 → 4428.48] is so important.
[4429.04 → 4432.66] It just feels like Silicon Photonics is destined to be a heartbreaker for a long time.
[4433.52 → 4433.60] And,
[4433.60 → 4433.86] uh,
[4433.86 → 4435.38] We weren't going to tell you this,
[4435.44 → 4437.56] but we have a Silicon Photonics sample.
[4437.68 → 4438.30] We'll send it to you,
[4438.34 → 4438.46] Arian.
[4438.86 → 4439.50] I know,
[4439.50 → 4440.52] I know you do.
[4440.66 → 4440.88] I mean,
[4440.98 → 4441.28] I,
[4441.28 → 4441.64] I,
[4441.64 → 4441.88] I,
[4442.08 → 4443.08] you,
[4443.08 → 4444.42] you even gave me the
[4444.44 → 4444.68] uh,
[4444.68 → 4446.40] the 20 gig NRZ one that,
[4446.48 → 4446.80] the
[4446.80 → 4446.92] the
[4446.92 → 4447.34] what is it?
[4447.34 → 4448.26] The Firefly cable.
[4448.26 → 4448.62] And I'm,
[4448.70 → 4450.52] I'm sure that tech has developed further.
[4451.28 → 4451.56] Um,
[4451.58 → 4452.64] but ultimately the
[4452.64 → 4452.82] the
[4452.82 → 4454.62] the important bit for that,
[4454.68 → 4454.88] it's like,
[4454.90 → 4455.34] honestly,
[4455.34 → 4456.72] for Silicon Photonics,
[4456.72 → 4458.54] to really work and to go somewhere,
[4458.54 → 4460.40] it needs to go on package.
[4460.40 → 4463.20] It needs to be paired with the die on package,
[4463.20 → 4464.34] not as a septic,
[4464.44 → 4467.10] separate optical engine that you still need to get through,
[4467.18 → 4467.84] through the PCB,
[4468.02 → 4468.66] because that just,
[4469.14 → 4469.88] that by itself,
[4469.88 → 4472.50] you're going through the BGA package,
[4472.58 → 4473.78] the balls into your PCB,
[4473.94 → 4474.92] back into your optical engine.
[4475.04 → 4476.54] You've already lost like the game,
[4476.54 → 4477.32] like at this point,
[4477.44 → 4478.58] like why bother?
[4479.00 → 4479.12] So,
[4479.34 → 4483.26] which means that the only way this will happen is if we can figure out how to get
[4483.26 → 4483.92] this on package,
[4483.96 → 4486.14] which means that we need to get,
[4486.22 → 4486.54] uh,
[4486.72 → 4487.08] you know,
[4487.08 → 4487.26] the
[4487.26 → 4487.48] the
[4487.48 → 4487.64] the
[4487.64 → 4488.18] the switch,
[4489.04 → 4489.80] AC.
[4490.94 → 4491.34] Yeah,
[4491.34 → 4491.66] exactly.
[4491.82 → 4492.08] Santa.
[4492.12 → 4493.70] We need to get Santa to make switching silicon.
[4493.88 → 4497.42] Or we need to do our own switching silicon and then invite Santa to go put,
[4497.42 → 4497.94] uh,
[4498.00 → 4498.14] Oh,
[4498.18 → 4498.64] there we go.
[4498.90 → 4499.26] Yeah.
[4499.80 → 4502.82] So maybe we did drink that booze after all,
[4502.88 → 4503.00] you know,
[4503.00 → 4503.86] I thought we gave it back.
[4506.26 → 4507.02] First,
[4507.02 → 4508.66] I think oxide is the
[4508.66 → 4509.32] would be a
[4509.42 → 4511.34] is the perfect partner for Santa.
[4511.34 → 4512.34] I think,
[4512.34 → 4513.34] uh,
[4513.34 → 4513.60] the
[4513.60 → 4516.44] the DNA of both companies are very similar.
[4516.76 → 4517.54] So that's,
[4517.60 → 4519.10] I think that we are great partnership.
[4519.10 → 4522.12] And also for the two 24 gig,
[4522.16 → 4524.02] I'm not even talking 112 gigs and the
[4524.02 → 4524.52] uh,
[4524.52 → 4525.86] five fly connected.
[4526.02 → 4528.10] I'll talk about that course is co-packaged.
[4528.10 → 4531.64] We are partnered with quite a few,
[4531.64 → 4532.12] uh,
[4532.12 → 4533.90] of the major chipmakers,
[4533.90 → 4534.96] uh,
[4535.08 → 4537.22] and a custom of this,
[4537.30 → 4538.78] because it requires all three,
[4538.90 → 4539.58] a system vendor,
[4539.72 → 4540.16] chip vendor,
[4540.26 → 4542.16] and connected vendor to work together.
[4543.54 → 4545.42] And that is happening right now,
[4545.48 → 4545.94] but you know,
[4546.20 → 4546.58] there are,
[4546.88 → 4547.16] it's,
[4547.16 → 4547.24] it's,
[4547.28 → 4547.58] it's,
[4547.64 → 4549.58] it's a struggle also at the same time,
[4549.58 → 4553.34] because I'm getting three companies to talk to each other,
[4553.40 → 4554.92] especially if they're very large companies,
[4555.02 → 4555.48] some of them,
[4555.62 → 4556.16] it's difficult.
[4556.16 → 4556.20] Well,
[4556.24 → 4557.38] not just very large companies,
[4557.38 → 4559.94] they all have three different roles.
[4560.30 → 4562.40] They've played three different roles in the industry,
[4562.40 → 4566.40] and they've never had to cooperate in this manner until now,
[4566.40 → 4568.00] because the ASICs,
[4568.12 → 4570.52] the ASIC development has always happened a little bit in isolation.
[4570.52 → 4571.16] And then,
[4571.20 → 4571.42] you know,
[4571.44 → 4574.72] you just get the data sheet, and you get a device, and you make it work on
[4574.72 → 4574.86] your,
[4574.98 → 4575.68] on your board.
[4575.84 → 4576.90] And then similarly,
[4577.26 → 4577.58] the
[4577.58 → 4577.76] the
[4577.76 → 4577.86] the
[4577.86 → 4578.08] the
[4578.08 → 4578.50] you know,
[4578.50 → 4580.70] the system integrator builds out of pieces that they,
[4580.82 → 4581.14] that they,
[4581.24 → 4582.44] that they find and,
[4582.44 → 4584.18] and sometimes commission.
[4584.18 → 4586.38] But in order to now,
[4586.38 → 4587.40] you need to,
[4587.58 → 4587.98] yeah,
[4588.06 → 4588.38] you're right.
[4588.44 → 4592.14] You need to think about the ASIC design designers and,
[4592.26 → 4592.46] and,
[4592.46 → 4593.04] and the
[4593.04 → 4596.72] or rather the package designers that need to be planned.
[4596.72 → 4597.26] And that,
[4597.26 → 4600.90] but that means that you're now subject to these like five or six or even 10
[4600.90 → 4603.50] year cycles that these ASICs are on.
[4603.60 → 4605.38] And now you need to intercept that.
[4605.38 → 4607.48] And your system integrator needs to intercept that.
[4607.48 → 4607.78] It's,
[4607.78 → 4608.08] it's,
[4608.08 → 4609.78] this is going to be fascinating how,
[4609.78 → 4610.22] how,
[4610.22 → 4611.40] and,
[4611.40 → 4614.38] and I wonder if this is actually going to be caused to,
[4614.60 → 4617.04] for some of this stuff to slow down because some of the
[4617.18 → 4618.46] like some of these partnerships,
[4618.46 → 4620.74] I don't know if they will be able to get,
[4620.88 → 4622.92] to get done to be quiet.
[4623.46 → 4625.58] So I think that's where the customer,
[4625.84 → 4627.26] a company like yours,
[4627.48 → 4633.56] I actually have an advantage because you have not constrained yourself by the
[4633.56 → 4635.80] form factor of a one RU switch,
[4635.94 → 4636.36] actually.
[4636.88 → 4637.04] Right.
[4637.46 → 4638.96] You call it right.
[4639.08 → 4640.12] You have it as a
[4640.12 → 4641.34] or you and a half,
[4641.44 → 4642.38] like half width.
[4642.38 → 4647.18] And so you're defining your oxide unit,
[4647.30 → 4653.04] you defining your own form factor so that the overall architecture makes sense.
[4653.04 → 4656.52] And I think that's the approach that needs to be taken overall.
[4657.20 → 4661.82] And so you already are one step ahead of most of the system vendors in that
[4661.82 → 4662.20] case.
[4662.78 → 4663.44] I got to say,
[4663.48 → 4666.42] this just warms my heart because we are so used to people being like,
[4667.00 → 4670.22] and I feel like you're almost like when you're talking about oxide doing its own
[4670.22 → 4670.74] form factor,
[4670.74 → 4673.96] or this is where other folks would be like looking for a euphemism to explain
[4673.96 → 4674.24] like,
[4674.36 → 4675.46] we're basically nuts.
[4675.46 → 4675.92] Or it's like,
[4675.98 → 4676.48] as you know,
[4676.56 → 4679.64] oxide does not feel constrained.
[4680.08 → 4680.28] It's like,
[4680.32 → 4680.42] yeah,
[4680.50 → 4681.92] are you saying that we're weird?
[4682.52 → 4685.34] But we definitely have done things our own way.
[4685.44 → 4686.60] We think for very good reason.
[4686.98 → 4687.60] And I,
[4687.72 → 4687.84] you know,
[4687.86 → 4690.60] it's been terrific that Sam tech has,
[4690.70 → 4696.72] has always just dug into the problems and understood why we've done it this
[4696.72 → 4697.12] way.
[4697.12 → 4698.52] It's been such a great,
[4698.66 → 4699.10] as you said earlier,
[4699.36 → 4699.48] a
[4699.64 → 4700.12] we really,
[4700.12 → 4701.62] perfect partnership.
[4701.62 → 4703.80] It's a model partnership for us.
[4703.90 → 4706.06] We definitely point other people to the
[4706.06 → 4707.82] the Sam tech oxide partnership is,
[4707.92 → 4710.44] as really one in which we're innovating together.
[4711.44 → 4713.18] And for those of you out there,
[4713.20 → 4713.84] if you haven't,
[4713.96 → 4716.62] if you're hearing about Sam tech for the first time,
[4716.66 → 4717.46] as you may well be,
[4717.62 → 4719.58] it's a fun website to disappear on.
[4719.58 → 4720.02] And,
[4720.02 → 4722.22] and there's a lot of great content out there.
[4723.34 → 4723.50] And,
[4723.50 → 4723.52] and,
[4723.52 → 4725.04] and Jonathan,
[4725.14 → 4725.52] Jonathan,
[4725.52 → 4726.02] Jonathan,
[4726.02 → 4727.46] thank you very much for joining us.
[4727.68 → 4728.08] Really,
[4728.34 → 4729.72] really appreciate it.
[4729.72 → 4730.72] and,
[4730.72 → 4730.74] and,
[4730.74 → 4731.60] and,
[4731.60 → 4731.80] Arden,
[4731.90 → 4732.50] thank you for,
[4732.50 → 4735.98] thank you for finding them.
[4736.06 → 4736.56] Thank you for,
[4736.56 → 4737.24] you know,
[4737.24 → 4738.56] taking the approach that you did.
[4738.56 → 4739.06] And,
[4739.06 → 4740.32] and it's,
[4740.32 → 4740.94] it's been,
[4741.28 → 4744.68] it's been a lot of fun, and it's been a lot of fun to go actually,
[4744.68 → 4746.54] go build this thing together.
[4747.68 → 4748.52] I honestly,
[4748.52 → 4751.20] I don't know how we would have built it otherwise.
[4752.40 → 4752.92] Exactly.
[4753.14 → 4753.62] We would not,
[4753.72 → 4754.38] we would have been,
[4754.58 → 4755.58] we would not have built it.
[4755.94 → 4756.04] So,
[4756.28 → 4756.44] yeah.
[4757.10 → 4758.14] Thank you very much.
[4758.30 → 4764.42] And I'm based in Santa Clara, and we have a lovely demo room that shows how all of these different architectures can happen.
[4764.42 → 4766.16] And if anyone wants to just stop by,
[4766.24 → 4768.22] we can do a quick lunch and learn for anyone.
[4768.74 → 4770.92] Just reach out to Jonathan or me.
[4771.56 → 4772.40] There you go.
[4772.60 → 4773.04] Awesome.
[4773.56 → 4773.76] Well,
[4773.76 → 4774.32] and I,
[4774.42 → 4774.54] yeah,
[4774.62 → 4777.74] I would encourage folks to take you up on the offer because it's definitely on us.
[4778.60 → 4779.26] All right.
[4779.44 → 4779.68] Well,
[4779.76 → 4779.96] Hey,
[4780.00 → 4780.72] we're not going to be,
[4780.82 → 4782.30] we're going to be off next week.
[4782.40 → 4782.88] Adam,
[4782.96 → 4786.02] I'm actually giving a talk on social audio next week,
[4786.02 → 4787.60] which I'm,
[4787.68 → 4787.96] yeah.
[4788.24 → 4790.22] So we should have us all there live.
[4790.40 → 4790.58] Comment.
[4790.84 → 4791.38] We should.
[4791.46 → 4791.70] We should.
[4791.92 → 4792.58] We actually.
[4792.58 → 4794.48] It's almost,
[4794.62 → 4794.94] unfortunately,
[4795.02 → 4795.12] my,
[4795.18 → 4796.66] I think my position is slightly earlier in the day.
[4796.74 → 4797.08] This is a good,
[4797.26 → 4798.06] go to Chicago.
[4798.84 → 4799.20] Um,
[4799.26 → 4799.64] but,
[4799.80 → 4800.00] uh,
[4800.00 → 4800.68] really looking forward.
[4800.74 → 4803.60] I'll be talking about what we've done here with oxide and friends.
[4803.78 → 4804.14] So,
[4804.36 → 4804.64] uh,
[4805.16 → 4806.82] if there are particular things you want me to hit on,
[4806.86 → 4807.16] definitely,
[4807.16 → 4807.58] uh,
[4807.58 → 4808.44] hit me up in the DMS.
[4808.80 → 4809.56] So it's been,
[4809.74 → 4811.64] this has been so much fun to do.
[4811.68 → 4812.14] And in part,
[4812.14 → 4812.68] because of,
[4812.78 → 4812.92] uh,
[4812.92 → 4814.16] just like this discussion today,
[4814.16 → 4815.22] it's been a lot of fun.
[4815.22 → 4816.48] So thank you,
[4816.56 → 4816.82] Jonathan,
[4817.06 → 4817.48] Jonathan,
[4817.48 → 4817.74] Jonathan,
[4818.00 → 4818.12] and,
[4818.12 → 4819.54] and Ariane and Nathaniel.
[4819.82 → 4820.16] Um,
[4820.34 → 4820.66] and,
[4820.90 → 4821.18] uh,
[4821.18 → 4822.20] we'll see you in two weeks.
[4823.44 → 4824.08] Bye.
[4825.08 → 4825.20] Bye.
[4847.34 → 4848.72] Bye.
[4848.84 → 4848.88] Bye.
[4849.40 → 4849.80] Bye.
[4850.38 → 4851.24] Bye.
[4851.34 → 4851.68] Bye.
