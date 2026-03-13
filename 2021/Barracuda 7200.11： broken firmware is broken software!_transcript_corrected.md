[0.00 → 1.76] Bill, thanks for the segue.
[2.22 → 4.80] So Adam and I were chatting this morning.
[4.92 → 6.42] We're like, hey, what should we talk about in the space today?
[6.52 → 8.12] And I'm like, I don't know, kind of what's in the news?
[8.30 → 10.62] And headed over to Hacker News.
[10.92 → 11.86] And I'm like, that's strange.
[11.96 → 17.10] Like, why is there a Seagate just like skew in as a Hacker News story?
[17.44 → 19.10] And Adam, did you know about this Wikipedia page?
[19.20 → 20.36] I don't think I did.
[20.72 → 22.84] No, totally news to me.
[22.92 → 27.18] And it's always one of those funny ones when it's just like a bare Wikipedia page on Hacker News.
[27.28 → 28.70] So I also picked my interest.
[28.70 → 29.78] Right, which I actually like.
[29.78 → 34.88] I mean, I think it's because, you know, it's like, okay, this thing is so interesting that we're just going to drop it as a noun.
[35.02 → 35.84] Like, there's no headline.
[35.94 → 36.82] This is just a thing.
[37.50 → 37.90] That's right.
[38.40 → 41.16] This fact that is unknown needs to be known.
[41.36 → 42.02] Yes, excellent.
[42.28 → 47.70] And so this is the ST3000DM001.
[48.10 → 50.68] This is what we knew as the 7200.10.
[50.92 → 56.26] We actually never, we used the successor to this drive, the 7200.11,
[56.26 → 63.68] which, the codename Moose, was an absolute disaster for us.
[63.86 → 65.38] And I definitely want to tell our stories.
[65.62 → 67.74] I'm hoping other people will tell their stories as well.
[67.82 → 74.14] So if you've had stories with this very, very bad class of drives,
[74.36 → 76.86] it's because, Adam, the one thing I learned, so I mean, among other things,
[76.86 → 82.60] first, this is a drive that has a class action suit section in the Wikipedia page entry.
[82.68 → 83.32] How great is that?
[84.04 → 87.88] I mean, it's got to be a unique or a very small number.
[88.22 → 89.50] Interesting to know the stats on that.
[89.60 → 90.68] Interesting to know the stats.
[91.00 → 95.54] And I feel like it should be every company and product's aspiration to avoid the class action section.
[95.54 → 98.98] It doesn't have a Wikipedia page entry that does title class action section.
[99.96 → 103.50] Did you go through some of the firmware bugs that this thing had?
[104.34 → 104.94] I don't know.
[104.98 → 106.58] Yeah, I looked into some of them.
[106.70 → 106.84] Yeah.
[107.52 → 111.78] We did not see the worst ones is what I can't believe.
[111.96 → 115.46] I mean, so the and Adam, actually, do you want to give the
[117.04 → 120.20] because I do feel like memory, it can become fuzzy here.
[120.96 → 123.60] I think we should tell the story that we had with our drives,
[123.60 → 125.16] and then we can use that as a segue.
[125.76 → 127.82] You know, I think you lived it much more indelibly.
[128.06 → 128.86] You should do this one.
[129.94 → 130.44] All right.
[130.52 → 134.26] So we were, so Adam and I, along with a bunch of other folks,
[134.48 → 137.42] were together at Sun back in the day building a storage product.
[137.54 → 139.00] This is in, we started in 2006.
[139.16 → 140.12] We shipped in 2008.
[140.76 → 143.46] And we had several different storage products.
[144.28 → 148.32] One was based on Hitachi drives, HGST.
[148.54 → 152.28] And this is all going to get confusing because HGST and Western Digital later merged
[152.28 → 154.06] and took the name Western Digital.
[154.72 → 158.02] So I know that Rick Alter, I know, has got some WD stories that I want to get to, too.
[158.12 → 162.38] And you have to figure out if that's the WD post-haste merger or pre-test merger.
[163.14 → 168.02] But we were using Seagate drives in one product and HGST drives in another product.
[168.02 → 172.32] And the I mean, Adam, you obviously remember the firmware rev.
[174.06 → 174.78] You know what?
[175.16 → 177.26] I'm embarrassed that I don't have that off the top.
[177.26 → 178.16] Are you serious?
[178.16 → 180.20] How many years the therapy worked?
[180.52 → 181.64] I know, I know.
[181.72 → 183.28] I know that you still have the tattoo.
[183.46 → 184.98] I can't forget it.
[185.38 → 189.42] So SU0D is the drive firmware rev.
[190.98 → 192.96] So this thing damn near ruined our lives.
[193.42 → 196.62] So what would happen, and this happened to a couple of customers,
[197.28 → 199.90] they'd buy our product, and it would be great.
[200.68 → 202.10] And they're like, oh, this is great.
[202.18 → 203.00] And it seems great.
[203.00 → 205.14] And so they put more and more load on it.
[205.52 → 208.10] And then sadness would start.
[208.36 → 209.88] And there'd be a first raindrop.
[210.42 → 212.72] And then it would be like four more raindrops.
[212.86 → 217.58] And then it was all fucking hailstones as the product just came to its knees.
[217.78 → 223.64] And in particular, what would happen is we started seeing these outliers, latency outliers.
[223.90 → 229.52] It's like 560 millisecond latency outliers, which is like it's spinning media.
[229.52 → 232.38] These are 700 RPM drives, but that's a long-ass time.
[232.46 → 233.46] That's fucking half a second.
[234.60 → 238.82] And what you would see is one drive would start seeing them,
[238.90 → 240.66] and then another drive would start seeing them,
[240.70 → 242.54] and then three more drives would start seeing them.
[243.16 → 245.24] And do you remember MIT Broad was a customer?
[245.58 → 246.36] Adam, did you ever deal with them?
[246.44 → 246.72] Yes.
[246.92 → 247.76] Yes, I remember the Broad.
[247.84 → 247.96] Yeah.
[248.42 → 248.60] Yeah.
[248.68 → 252.04] So I mean, the admin from MIT Broad was crying on the phone with me.
[252.24 → 253.18] He and I were both crying.
[253.18 → 253.94] This is clear.
[254.64 → 257.42] But he was actually crying.
[257.42 → 260.26] And I mean, crying maybe a bit strong.
[260.34 → 261.88] I don't think it was too strong.
[262.18 → 265.86] He said in a way that barely had control of his emotions.
[265.98 → 267.28] And again, I did not have control of my own emotions,
[267.28 → 268.36] so this is all very reasonable.
[269.00 → 271.54] It's a reflection on Seagate, not on him.
[271.78 → 275.56] He's like, I just want the system to be back to what it was.
[275.66 → 277.62] And I'm like, that's what we all want.
[277.76 → 278.66] We all want that.
[278.66 → 283.62] And what was happening, we were getting a huge runaround from Seagate.
[284.26 → 285.78] And they were being very cagey.
[285.78 → 287.94] And what we understood to be happening, but I would love,
[288.06 → 290.62] if anyone has got kind of supporting detail about this, I would love it.
[290.66 → 293.98] Because the firmware is all proprietary, and it's very hard to reason about.
[294.38 → 298.36] But according to what we received from them,
[298.74 → 304.94] there was a firmware bug whereby the head would be mis programmed due to a polarity error.
[305.32 → 309.72] And instead of being programmed to decelerate at high Las,
[309.78 → 312.60] it would be programmed to accelerate at high Las,
[312.60 → 315.34] which would destroy the drive if it allowed to do that.
[315.76 → 317.98] So the drive would actually reset itself.
[318.44 → 322.02] And what we were seeing, those 560 millisecond outliers,
[322.38 → 326.36] was the time it took for the drive to reset itself.
[327.76 → 332.96] And now, Brent, sometimes I feel like some of this was like in a dream.
[333.06 → 334.70] So I'm not sure if I remember this correctly.
[334.70 → 339.38] But one of the reasons we tried to see this pathology in our lab,
[339.50 → 342.26] and as I recall, one of the reasons we didn't see this
[342.26 → 345.14] was that in well climate-controlled labs,
[345.44 → 349.80] you would encounter this problem because it had to do with the ambient temperature.
[350.30 → 357.32] Whereas our lab at Fish works averaged around like 95 to 105 degrees, as I recall.
[357.86 → 360.62] And so in this like super baking hot lab,
[360.62 → 363.74] we like wouldn't encounter this pathology.
[363.82 → 364.72] We were less like a sit.
[364.88 → 365.60] I don't know.
[365.74 → 367.94] Is that, I mean, I definitely,
[368.06 → 370.32] I'm not sure if I ever knew that detail, if that were the case.
[370.66 → 373.92] I mean, honestly, we were so,
[374.30 → 378.44] what we knew from Seagate is that upgrading from SU-0D to SU-0E
[378.44 → 380.30] was going to solve this problem, and it did.
[380.30 → 384.48] And at that point, I think I was just,
[384.64 → 387.84] at that point, the desire to understand this problem ended,
[387.98 → 390.34] and the desire to forget it began.
[391.24 → 396.58] And now was this also the one that would cause the G-list to grow incorrectly?
[396.82 → 398.76] Or was that, am I conflating firmware bugs?
[399.48 → 400.58] That, so this is where,
[400.72 → 403.66] when I was going through all the firmware bugs on this piece of garbage,
[403.88 → 405.80] this is where I realized like, man, there were a lot,
[405.86 → 409.28] I mean, of course, of course there were a lot of firmware bugs in this thing.
[409.28 → 413.90] And so, no, that I think is a second disjoint firmware bug, I believe.
[414.48 → 415.22] Okay, okay.
[415.46 → 417.40] Because I remember we would see problems like this
[417.40 → 421.60] where these drives would incorrectly report sectors as bad,
[422.08 → 424.16] and then the G-list would grow and grow
[424.16 → 426.86] and incur nasty performance pathologies,
[427.58 → 431.96] and then all of a sudden start reporting the smart, you know, predict fail,
[432.50 → 434.20] and we'd get these drives back in hordes.
[435.06 → 437.56] Well, and the right,
[437.56 → 442.00] and there were apparently also firmware bugs where, I mean, again, like,
[442.12 → 445.02] so if you go to the Wikipedia page on Seagate Barracuda,
[445.42 → 447.30] not on the SKU I mentioned,
[447.50 → 450.84] but the Seagate Barracuda on both the
[450.92 → 454.70] both the 7200.10 and 7200.11 entries
[454.70 → 458.96] have got extensive firmware bug descriptions.
[458.96 → 464.54] And I feel that, I mean, you should take a look at that, Adam,
[464.60 → 467.82] because, like, that, apparently there was a bug, by the way,
[467.86 → 473.66] where this thing could forget where its effectively metadata was on the spindle,
[473.82 → 475.38] and the drive would just never boot again.
[476.66 → 477.06] Wow.
[477.78 → 480.66] It's, all right, so with that, those are our stories.
[480.78 → 483.02] We upgraded this thing from SU0D to SU0E.
[483.02 → 485.42] Those problems went away.
[485.50 → 487.28] There were a bunch of other problems that we had.
[488.54 → 493.10] And then, before I kind of throw it over to others for their stories,
[493.24 → 498.26] the other thing I would add is Seagate themselves were a giant customer of ours.
[498.50 → 499.12] Do you remember this, Adam?
[499.92 → 500.68] Yes, yes.
[501.36 → 504.16] And they were dicks as customers, which is fine.
[504.38 → 507.16] Like, when people are dicks as customers, it's like, all right, I get it.
[507.26 → 508.54] Like, you want it to work.
[508.70 → 509.66] Like, we want it to work.
[509.72 → 510.18] You want it to work.
[510.18 → 510.96] We all want it to work.
[511.48 → 513.56] You feel so strongly that we should record that.
[513.64 → 513.88] Yes.
[514.18 → 517.18] Yeah, but no, I do feel that, like, when a customer is, like, really, like,
[517.52 → 519.30] abusing you because the thing doesn't work,
[519.40 → 522.70] a part of you has to be, like, you're abusing me because you want this to work,
[522.76 → 524.06] and I want this to work, too.
[524.26 → 526.70] And this might not be the way I would conduct myself,
[526.70 → 528.24] but I have to forgive you for it, right?
[528.38 → 528.86] I mean, I...
[528.86 → 531.44] There's a lot of empathy there, but that's great, yeah.
[531.48 → 532.56] That year was a tough fucking year.
[532.80 → 535.60] So we had a bunch of different firmware problems.
[536.22 → 539.62] And so you recall we had the SU0D problems, very acute.
[539.62 → 540.84] We had...
[540.84 → 542.12] And I can't believe you've forgotten.
[542.34 → 546.36] The expander, SAS expanders, had the 3R20 problem.
[547.36 → 548.76] Do you remember what we called that one?
[548.78 → 549.56] That was a blue light special.
[550.34 → 550.64] Oh, yeah.
[550.84 → 553.68] This is where the lanes would, like, go out to lunch, right?
[554.62 → 555.34] That one...
[555.34 → 556.06] There was that one, too.
[556.78 → 561.04] In this one, the service light would come on, but there was no other problem.
[563.08 → 563.44] Right.
[563.96 → 564.08] Right.
[564.22 → 565.60] This is why we called it the blue light special.
[565.60 → 569.74] So the service light would come on, and then all of humanity would spend its precious resources
[569.74 → 571.84] trying to figure out what was wrong with the system.
[572.16 → 574.62] As it turns out, what was wrong with the system was that the service light was on.
[575.18 → 577.28] I mean, it was very, like, meta in some ways.
[577.54 → 579.70] So what you actually needed to do was reseed it.
[579.72 → 581.80] If you reseeded it, the service light would go out, and then everything would be fun.
[582.64 → 583.14] That's right.
[583.44 → 583.64] Man.
[583.92 → 586.36] And then we upgraded to 3R22 to get out of that one.
[586.40 → 587.36] That was on the SAS expander.
[587.92 → 589.54] But then we had the LSI...
[589.54 → 590.60] The LSI HBA.
[591.38 → 592.04] That's what I was thinking.
[592.08 → 592.22] Right.
[592.24 → 593.44] The HBA, the Firelock problem.
[593.44 → 595.16] Yeah, FI lock, right.
[595.66 → 599.40] Where a FI would lock up and then be like, I'm just done.
[599.54 → 600.10] Like, I've locked.
[600.32 → 600.82] Like, nothing.
[600.94 → 601.78] You can never talk to me again.
[601.78 → 603.12] And you had four of them.
[603.16 → 603.68] You had four of them.
[603.88 → 607.44] And, like, one would go, and you'd lose 25% of your bandwidth.
[607.54 → 607.64] Right.
[607.64 → 609.04] And then two would go, and you'd be halfway.
[609.28 → 611.60] And then a year later, they'd all be gone.
[611.62 → 611.78] Right.
[611.86 → 612.94] And there's no recovery.
[613.06 → 613.34] That's right.
[613.42 → 615.40] And it turns out losing that last FI is particularly painful.
[615.40 → 617.10] This is the...
[617.10 → 621.50] I mean, Adam, we've talked about the title of your forthcoming best-selling book from one to zero.
[621.50 → 622.50] So...
[622.50 → 623.46] That's right.
[624.00 → 626.38] I feel this is another chapter of from one to zero.
[626.76 → 628.96] Because from one to zero, for the...
[630.92 → 633.62] For those that don't know, Adam is not necessarily a fan.
[633.74 → 634.50] I think it's fair to say.
[635.12 → 635.50] Yeah, that's fair.
[635.62 → 636.24] We can record that.
[636.32 → 636.48] Yeah.
[636.64 → 643.04] Of zero to one, Peter Thiel's, like, how-to book on cargo cultism.
[643.04 → 643.52] And...
[643.52 → 644.04] And...
[644.04 → 645.04] And...
[645.04 → 650.52] I like that Josh unmutes himself for the laughter.
[651.46 → 653.38] I was going to make a comment, but I couldn't.
[654.84 → 656.30] Well, okay, and didn't...
[656.30 → 659.84] Am I making up the fact that you, like, interviewed with Peter Thiel or something?
[660.18 → 662.18] No, no, that part you're making up.
[662.22 → 665.60] But Peter Thiel, in his book, and now we're wandering far afield.
[665.60 → 672.02] But Peter Thiel says the way he interviews people is by asking something that they believe
[672.02 → 673.72] that other people don't generally believe.
[673.86 → 676.60] Which I think would be an entertaining interview question.
[676.98 → 681.08] But I'm not sure any of the results, like, would correlate with them doing a good job.
[681.16 → 682.32] It is a weird signal.
[683.20 → 683.52] I got it.
[683.52 → 684.72] It's a weird signal, right?
[684.94 → 685.44] And...
[685.44 → 689.00] And so I thought that was a terrible interview question.
[689.00 → 692.38] And someone asked me that as an interview question.
[693.30 → 697.38] And I said, well, you know, a lot of people think Zero to One is a good book.
[697.54 → 699.68] And I don't think it's a very good book at all.
[699.84 → 702.80] And that was not the right answer to that interview.
[703.02 → 703.70] That is awesome.
[703.82 → 704.36] That's an email.
[704.72 → 706.92] How long had you been sitting on that one?
[708.52 → 710.98] Actually, I never thought it would come up.
[711.50 → 712.32] But then...
[712.32 → 712.54] Okay.
[712.60 → 718.00] Because I'm a good New Englander, I tried to pull up from that nosedive that I'd put in.
[718.00 → 720.86] And I said, oh, well, what's your answer to that question?
[721.00 → 724.76] And the person with whom I was interviewing said, uh-huh, I've never thought about it.
[725.46 → 728.68] At which point, obviously, I should have left.
[728.90 → 729.70] But I stayed.
[730.20 → 730.32] Okay.
[730.38 → 731.54] So I've got a lot of follow-up questions.
[731.74 → 734.48] One, have you ever used the phrase good New Englander in conversation?
[734.62 → 736.24] You've been using that for years, and I've just missed it.
[736.28 → 737.68] I've never heard you say good New Englander.
[738.50 → 738.80] I mean...
[738.80 → 742.52] I mean, like, you know, like, you know, don't...
[742.52 → 743.26] Like, we don't hug.
[743.34 → 744.38] We're not a hugging people.
[744.88 → 747.90] You know, there are a lot of characteristics of New Englanders.
[748.36 → 751.36] Listen, the guy's a Red Sox fan, all right?
[751.54 → 752.58] That's all you need to know.
[752.96 → 753.30] Yeah, yeah.
[753.88 → 754.32] It is.
[754.90 → 755.42] It is.
[755.48 → 757.06] In fact, the guy is such a Red Sox fan.
[757.62 → 757.86] No, no.
[757.86 → 758.48] We're getting far out of the field.
[758.58 → 759.92] We're going to get back to Seagate, I promise.
[760.06 → 765.68] He is such a Red Sox fan that Adam and I were together for an historic game.
[765.80 → 767.98] Oh, great, beautiful, delicious game.
[768.36 → 770.76] Sean Mania's no-hitter against the Red Sox.
[770.76 → 772.24] No, Dan escorted us in.
[772.80 → 773.22] No-hitter against the Red Sox.
[773.22 → 774.00] No, this is...
[774.00 → 775.66] Dude, this speaks to what a Red Sox fan you are.
[776.02 → 776.58] We are...
[776.58 → 778.52] You had never seen a no-hitter in person.
[779.30 → 779.52] Yeah.
[780.64 → 782.18] This is the first no-hitter you've ever seen in person.
[782.46 → 783.40] It is...
[783.40 → 785.96] We are in the ninth inning and there are two outs.
[786.36 → 786.68] Yeah.
[786.88 → 791.52] And I asked you, does any part of you want to see a no-hitter?
[791.66 → 793.04] And you're like, no part of me.
[793.10 → 794.10] I want to see a base hit right now.
[794.46 → 795.10] I remember...
[795.10 → 796.82] The ball doesn't hit the wicket.
[797.32 → 798.38] That's when the ball doesn't hit the wicket.
[798.60 → 802.84] And Adam wanted the wicket-keeper to score a try.
[802.84 → 805.58] I mean, and you were so excited that your hand...
[805.58 → 807.60] You couldn't videotape because your hand was shaking.
[808.38 → 810.94] And I remember Hanley Ramirez was the last at-bat.
[811.12 → 813.18] And I said, knock it out of the park, Hanley.
[813.40 → 816.60] And you turned to me and explained that I was a terrible person.
[817.26 → 819.86] I feel like no explanation was really needed in that situation.
[820.20 → 821.22] That's like obvious...
[821.22 → 823.36] It's self-evident that we are in Oakland watching a no-hitter.
[823.94 → 824.10] All right.
[824.14 → 824.32] Sorry.
[824.56 → 824.70] Anyway.
[825.04 → 825.76] We digress.
[826.00 → 827.34] And they completed the no-hitter.
[827.56 → 827.88] But yes.
[828.68 → 830.20] Back to Seagate as a customer, though.
[830.64 → 831.58] Copping the stack off.
[832.86 → 834.92] So Seagate is a customer.
[835.56 → 836.58] And they are...
[836.58 → 837.62] This thing is not working for them.
[837.76 → 838.80] And they are furious.
[839.66 → 841.70] And they're like furious.
[841.70 → 843.72] They're furious, and they've been kind of tough to deal with.
[843.78 → 844.18] Tough customers.
[844.52 → 845.00] So...
[845.00 → 851.04] And I am thinking, please, God, let them be seeing the SU0D problem.
[851.50 → 851.94] Please.
[852.74 → 853.14] Please.
[853.34 → 853.66] I would...
[853.66 → 855.04] Because this is a different division of Seagate.
[855.04 → 862.60] And I would so love to explain to them that the problem that they are so upset about is their own company's problem.
[862.72 → 863.46] I'm like...
[863.46 → 865.84] But, of course, that was not to be in the...
[865.84 → 866.72] They were seeing Shylock.
[867.08 → 868.22] So it's like, oh, come on!
[868.68 → 869.24] Can't...
[869.24 → 869.58] That's right.
[869.60 → 873.58] I've only wished the SU0D pathologies on one customer in that.
[873.72 → 873.96] Yes.
[873.98 → 876.36] If only LSI had been seeing the CBO problem.
[876.60 → 876.70] If only LSI.
[876.70 → 877.12] I know exactly.
[877.12 → 877.72] Some sort of...
[877.72 → 879.62] Some, like, gift of the Magi kind of...
[879.62 → 880.32] That's right.
[880.88 → 881.44] That's right.
[882.50 → 884.68] So those were our experiences, I think.
[884.84 → 887.04] We did notice that we saw so many problems.
[887.08 → 889.34] Because there was the Aspersion issue, which I think that...
[889.34 → 891.26] I wonder if that was the issue you were referring to in terms of temp.
[891.32 → 894.02] Maybe the LBA issue was temp related as well.
[894.02 → 895.74] I thought the LBA was...
[895.74 → 900.32] I thought that the Seagate issue was related to temperature because that's what was...
[900.32 → 905.90] The firmware was making a decision about the fly height in part based on the ambient temperature.
[906.00 → 906.68] That would make sense.
[906.68 → 906.76] Anyway.
[906.94 → 907.08] Yeah.
[907.16 → 907.46] No, no, no.
[907.46 → 907.92] That would make sense.
[907.98 → 909.60] I just don't think I ever got that detail.
[909.86 → 911.36] And again, I think part...
[911.36 → 914.22] Again, I don't remember how hot our lab was at Fish works.
[915.14 → 920.86] One of my big interviewing mistakes is I had some interns come in to make some Ethernet cables
[920.86 → 922.94] and I parked them in the lab, not realizing it.
[922.94 → 925.08] It was 110 degrees in the lab that day.
[925.58 → 926.88] And the fact that any of them...
[926.88 → 928.66] Their fingers were sweating.
[929.06 → 934.46] It was the worst interview, most abusive interview I've ever given by accident.
[934.86 → 938.12] And it should be said that these were high schoolers who...
[938.12 → 938.28] Yeah.
[938.42 → 939.86] I mean, these were children.
[940.80 → 941.64] This is child abuse.
[941.78 → 942.42] I mean, these were children.
[942.58 → 943.04] This is child abuse.
[943.04 → 945.16] Doesn't this violate some sort of child labour law?
[945.16 → 945.66] Oh, absolutely.
[945.92 → 946.82] Without question.
[947.28 → 947.92] Without question.
[948.82 → 949.62] Oh, man.
[949.62 → 953.00] It was like seven years ago or whatever.
[953.32 → 954.04] So, not trouble.
[954.38 → 955.20] I mean, that's...
[955.20 → 955.54] That's right.
[955.76 → 956.48] There you go.
[956.72 → 958.08] It was seven years ago.
[958.18 → 960.42] Oscar, if you're listening now, like, lawyer up, kid.
[960.44 → 961.02] It's not too late.
[961.26 → 963.82] You may be in your mid-30s, but you can...
[963.82 → 964.18] That's right.
[965.46 → 967.74] I'm like LinkedIn buddies with those guys still.
[968.22 → 969.14] They were great.
[969.26 → 969.56] Good character.
[970.18 → 970.76] It definitely...
[970.76 → 971.40] They were...
[971.40 → 973.28] Actually, I really liked both of those two.
[973.38 → 975.12] And they endured a lot.
[975.12 → 975.60] Yeah.
[976.88 → 977.24] Yeah.
[978.68 → 979.12] All right.
[979.14 → 980.24] So, I would like to hear...
[980.24 → 983.44] Because I know other people have experiences with this...
[983.44 → 984.68] Actually, not only do I...
[984.68 → 986.08] Well, I should say I now know.
[986.20 → 988.36] I mean, I think it's like watching that Hacker News...
[988.36 → 989.58] Did you read any of those comments on there?
[990.28 → 990.82] Yeah, crazy.
[991.14 → 993.24] But it also felt like...
[993.24 → 994.28] It felt very vindicating.
[994.94 → 995.70] And hold on.
[995.72 → 996.94] I'm trying to get...
[996.94 → 997.16] Oh, Bill.
[997.26 → 997.64] Yeah, there you are.
[997.72 → 999.54] Bill, you just asked to be a speaker.
[999.76 → 1001.12] Do you have some...
[1001.96 → 1002.30] Yes.
[1002.30 → 1009.22] I worked in the federal space dealing with that particular variant of Seagate Drive.
[1009.66 → 1020.70] I had a lab with 50 HP Z620 workstations that we had fully pimped out with 192 gigs of RAM, which was sweet.
[1021.14 → 1024.24] We had the OS on a solid state drive and whatnot.
[1024.24 → 1033.22] But for bulk storage of local data, we had two of those Seagate drives in each machine in RAID 1.
[1034.44 → 1034.90] Uh-oh.
[1035.18 → 1039.24] And that was the longest...
[1039.94 → 1043.10] You know, they can't all possibly...
[1043.10 → 1047.46] You know, we can't lose a third of them in a 24-hour period, can we?
[1047.76 → 1048.48] Oh, no.
[1048.48 → 1049.48] Oh, wait.
[1050.48 → 1050.92] Oh, wait.
[1051.10 → 1063.48] Yeah, but it was all local transient storage, so all the gold reference copies of the data were stored on a tape robot, which has its own set of problems, which...
[1064.12 → 1064.60] Yeah.
[1065.34 → 1066.12] But yeah, no.
[1066.54 → 1069.00] That's my single longest shift as a government employee.
[1070.22 → 1076.02] Over two days, it was 15 and a half hours each day, me and one other person.
[1076.02 → 1079.02] And were you trying to reconstruct...
[1080.04 → 1082.32] I mean, first, which pathology...
[1082.32 → 1084.16] Were you seeing one of these firmware pathologies?
[1084.38 → 1085.64] What were you seeing?
[1086.86 → 1089.44] We weren't that far down the rabbit hole.
[1089.56 → 1090.02] We were just seeing...
[1090.62 → 1093.60] We went from, oh, that's weird.
[1094.24 → 1097.66] Why is it taking so long to access a drive that's in the kit?
[1098.20 → 1099.02] Why is this...
[1099.54 → 1101.48] Why is it lying about block status?
[1102.74 → 1103.40] What it...
[1103.40 → 1109.78] I mean, I didn't really have an adjective to describe it until somebody introduced me to James Dickens.
[1110.40 → 1122.90] So, myself and the lieutenant colonel who were swapping drives out for Western Digitals, we referred to it as the Dickensian dystopia.
[1123.60 → 1123.78] Yeah.
[1123.78 → 1127.28] So, but yeah, that was fun.
[1127.54 → 1127.78] It was...
[1128.60 → 1135.10] And then the tape robot started having problems the following month, but I don't work there anymore.
[1135.36 → 1136.58] It's all better now.
[1137.52 → 1139.92] You have a lieutenant colonel swapping out hard drives.
[1140.02 → 1141.44] You've got some real serious problems.
[1142.78 → 1144.92] Things have not gone according to plan.
[1145.18 → 1146.66] If the lieutenant colonel's in there swapping drives.
[1146.70 → 1147.54] I think is that fair to say, Dan?
[1147.54 → 1149.86] Oh, yeah.
[1150.04 → 1150.22] Yeah.
[1150.78 → 1155.82] I mean, if that had happened in the Marine Corps, like, it would have been...
[1155.82 → 1157.26] I mean, that's the apocalypse right there.
[1157.44 → 1157.88] Right.
[1158.00 → 1158.46] Exactly.
[1160.42 → 1160.86] All right, Rick.
[1162.52 → 1168.14] Moose was slightly before I ran Google's hard drive team.
[1168.14 → 1180.28] So, I only heard about the after effects of it, but it definitely was one of those things where we learned a lot about how hard drive vendors manage their firmware development.
[1182.38 → 1186.54] Specifically, things like they don't use source control.
[1188.00 → 1189.56] Yeah, this is where I can...
[1189.56 → 1191.72] Is there a WTF emoji that I can, like, launch?
[1191.78 → 1193.20] I mean, this is just amazing to me.
[1193.20 → 1196.02] And so, Rick, how did you have insight?
[1196.10 → 1200.34] Because I feel like we never got that insight, even though we were a huge customer of Seagate.
[1200.50 → 1203.00] Like, we did not have the throwaway to get that kind of insight.
[1203.74 → 1205.06] You weren't that big of a customer.
[1205.18 → 1205.64] Yeah, fair enough.
[1205.72 → 1206.22] Right, exactly.
[1206.32 → 1206.62] There you go.
[1206.68 → 1206.98] That's it.
[1207.38 → 1208.42] That's what they kept telling us.
[1208.98 → 1218.26] When you're a big enough customer for hard drive vendors where you're ordering directly from them in sufficient volume, you also get to start making your own firmware changes.
[1218.26 → 1226.98] And so, you end up with your own firmware builds, which is its own complete set of disasters.
[1227.34 → 1242.86] Because the mainline firmware that ships to the commercial boxed units or even to the OEMs for system integration, the bug fixes that go into that train, someone has to manually put them into your train.
[1243.72 → 1245.08] That doesn't sound error-prone at all.
[1246.70 → 1247.14] Yeah.
[1247.14 → 1250.16] So, you know, there were many issues.
[1250.86 → 1254.30] That's how we figured out how to deploy hard drive firmware at scale.
[1256.50 → 1261.92] And, yeah, the Western Digital Sparta was the one that I spent a lot more time on.
[1262.16 → 1264.10] So, that was a two terabyte from Western Digital.
[1264.82 → 1274.20] And that drive, the short version of the story is they had copied a previous drive design specs.
[1274.20 → 1279.92] They changed the fly height to be closer because they needed to increase the aerial density.
[1280.36 → 1287.44] They did not realize that the error on the flight height was expressed as a percentage.
[1287.92 → 1291.94] And they did not change the percentage when they reduced the fly height.
[1291.94 → 1292.34] No.
[1292.34 → 1301.46] So, the drive was built so that the fly height would never be able to be within a safe margin.
[1301.46 → 1307.96] And it was basically during writes impacting imperfections on the disk.
[1307.96 → 1320.78] So, it was a very early case where, you know, the number of hours of consecutive writes or the numbers of amount of data written was a good indicator of how quickly the drive was going to die.
[1320.78 → 1330.68] So, that's when I got to see things like scanning electron microscope images of drive heads where they had a crater in the front of them.
[1332.34 → 1336.64] And, yeah, figuring out is it even possible to fix this with a firmware bug?
[1336.74 → 1338.10] And how do you run a screen?
[1338.50 → 1345.58] Because now you actually have to deploy firmware to these drives that let you run a test that you can do to figure out how many drives are even affected.
[1346.34 → 1349.56] And at Google scale, that's all quite a big challenge.
[1349.56 → 1350.20] Wow.
[1351.82 → 1361.40] Hey, Rick, when you're making custom firmware updates in your, you know, mega warehouse of disks, what kinds of functionality are you sneaking in there?
[1363.06 → 1367.90] Oftentimes, people are just asking for pretty basic things like adjusting the number of read retries.
[1368.22 → 1374.08] Because you may not want the drive to be trying really hard if you're running a cluster file system that has replicas elsewhere.
[1374.50 → 1376.52] You actually want it to stop early.
[1376.72 → 1377.02] Yeah, fail fast.
[1377.14 → 1377.64] Yeah, for sure.
[1377.82 → 1378.10] Makes sense.
[1378.10 → 1382.04] There are other tweaks to, like, you know, scheduling behaviours.
[1382.32 → 1383.60] Do you want background scrubbing?
[1383.74 → 1385.44] How intensive do you want that to be?
[1386.20 → 1388.08] You know, fairly benign things.
[1388.98 → 1393.44] But it's enough that if they tweak those things, you end up with your own fork of the firmware.
[1393.70 → 1400.62] And then, you know, you have to stay on top of what's happening everywhere to make sure that your firmware builds get appropriate fixes.
[1401.08 → 1401.20] Right.
[1401.28 → 1401.50] Gotcha.
[1401.50 → 1408.02] And is this, so WD's Sparta, is this an HGST drive or is this a WD drive?
[1408.02 → 1410.20] Yeah, this is pre-merger.
[1410.52 → 1410.74] Right.
[1410.78 → 1410.92] Okay.
[1410.92 → 1413.42] So this is on the WD side, not the HGST side.
[1413.42 → 1419.96] In fact, the merger, I think, happened not too soon after they had finished all the Sparta mop-up.
[1419.96 → 1422.08] Yeah, interesting.
[1422.08 → 1427.18] Because I was with a – I mean, it is amazing the fly height.
[1427.40 → 1431.86] I mean, you talk about the fly height is so important to these things from just reliability and performance and so on.
[1431.86 → 1440.26] And I know that I've said this before, but I just kind of found this number mind-bending when we were with the VP of quality for HGST.
[1441.14 → 1446.08] And he was asking us a bunch of questions around temp because apparently temp really affects fly height.
[1447.36 → 1450.14] Or rather, temp affects the performance of the drives.
[1450.80 → 1452.02] And we were talking about fly height.
[1453.30 → 1458.12] And the – Adam, do you know that we talked about fly height during a White for a drive?
[1458.12 → 1463.26] Oh, all I know is I need to take my best guess and then, like, divide it by a factor of 1,000.
[1463.40 → 1464.28] Yeah, that's basically it.
[1464.42 → 1469.06] I mean, my guess was going to be – I think, like, a reasonable guess on this would have been my guess.
[1469.44 → 1473.42] Would have been, like, I don't know, like, a micron seems small.
[1473.82 → 1474.54] Like, is it a micron?
[1475.32 → 1480.30] And it is – the fly height during a White is 0.8 nanometres.
[1480.30 → 1484.14] And I fell out of my chair.
[1485.00 → 1489.04] And I said, do you mean 800 picometres?
[1489.96 → 1491.56] And he's like, yeah, I guess I do.
[1491.74 → 1492.38] I never thought about it that way.
[1492.42 → 1493.18] But, yeah, 800 picometres.
[1493.62 → 1494.28] Yeah, that is what it is.
[1494.30 → 1494.86] It's 800 picometres.
[1495.50 → 1499.70] It's like, okay, if I had to deal in picometres, like, I would make – I would inflict picometres on everybody.
[1499.84 → 1501.72] I would be using picometres all the time.
[1501.72 → 1504.34] Like, and I saw that, Rick.
[1504.54 → 1507.24] Those spaces may have dropped, dropped Rick.
[1507.94 → 1512.40] But the – yeah, that is – that is wild.
[1512.40 → 1513.38] That's astounding, yeah.
[1514.74 → 1519.88] And just in terms of how sophisticated these things are mechanically, I mean, it's easy to bag on them.
[1519.88 → 1527.50] Although, that said, I feel like I spent too long apologizing for Gate's firmware because of the endemic difficulty of the problem.
[1527.60 → 1530.06] And then you learn, you think that they're not using source code control and all this other stuff.
[1530.16 → 1531.54] You're like, okay, now this feels a lot less sympathetic.
[1531.72 → 1534.72] This is a hard problem, but –
[1534.72 → 1535.32] Right.
[1535.44 → 1538.34] You don't need to create additional obstacles here.
[1538.78 → 1539.18] You don't.
[1539.26 → 1541.56] And, I mean, I think this is where I feel – I mean, I don't know.
[1541.66 → 1558.50] I feel that that kind of whole experience, and not just SC0D, the Gate experience, but the Gate experience, the LSI experience, the SAS expander, the Quanta experience, the – I mean, effectively every piece of firmware on that box really failed us.
[1558.50 → 1563.28] I feel it really radicalized me with respect to the need for open source firmware.
[1563.50 → 1571.32] Because I do feel that, like, a lot of these problems would be – at least making them visible to us would have made a big difference.
[1571.32 → 1572.32] Absolutely.
[1572.32 → 1572.46] Absolutely.
[1572.64 → 1579.46] Being able to go through – I mean, just – we've all seen this in other fields of software where you're asking yourself, am I crazy?
[1579.70 → 1579.80] Right?
[1579.88 → 1591.16] Like, and then to be able to actually correlate the phenomena you're seeing with the software that, as you can understand it, is so important, especially in these production environments.
[1591.42 → 1591.72] Yeah.
[1591.72 → 1592.58] I'm totally with you.
[1592.58 → 1594.20] When you're asking yourself, like, am I crazy?
[1594.32 → 1598.60] By the way, the vendor is, like, helping you out with their hypothesis, namely, like, you're crazy.
[1600.04 → 1600.98] It's like, oh, okay.
[1601.46 → 1601.60] Right.
[1601.60 → 1602.22] Well, thank you.
[1602.22 → 1603.30] It's everybody except us.
[1603.36 → 1603.88] Are you kidding me?
[1604.28 → 1604.48] Right.
[1605.24 → 1612.54] The – like, we're not – I mean, and, like, no one else is seeing that problem is something that I – I mean, how often have you heard that from a vendor?
[1612.54 → 1615.32] Like, we've never heard of anyone else having this problem.
[1615.84 → 1617.44] You're the only one who's seeing this.
[1617.88 → 1619.74] That's – I mean, it feels like language from a lawyer.
[1619.74 → 1626.44] I think Dell have put that as a low-numbered item in one of their support scripts.
[1626.86 → 1627.46] Oh, I –
[1627.46 → 1632.58] Like, the support technician is just supposed to read that line out, regardless of whether it's true.
[1632.88 → 1633.02] Right.
[1633.04 → 1634.48] That person's not even a Dell employee.
[1634.60 → 1637.02] That's just off a script from some generic call centre.
[1637.10 → 1637.50] Exactly.
[1637.64 → 1639.08] It's right under, dude, you're getting a Dell.
[1639.70 → 1641.14] We've never heard of that problem before.
[1641.34 → 1642.16] You're just like, oh, wow.
[1642.28 → 1645.10] No customer other than you is experiencing this problem.
[1645.22 → 1645.80] It's like, really?
[1645.92 → 1647.72] Okay, but it looks to me like the website's broken.
[1647.72 → 1651.54] Now, reboot the computer and update the BIOS and get back to me.
[1653.96 → 1656.00] Tom, I saw you unmuting yourself.
[1657.62 → 1658.30] Oh, you did?
[1658.54 → 1659.32] Am I on?
[1659.40 → 1659.76] You are.
[1660.80 → 1661.20] Amazing.
[1661.46 → 1664.96] I'm on a Twitter beta app, and it's a little flaky.
[1664.96 → 1671.34] But, yeah, I was going to say about the custom firmware that Dell and HP do.
[1672.20 → 1674.76] Back in the day, there were actually reasons for it.
[1674.78 → 1683.68] But now, the main thing is to put their names in the vendor field so that their RAID software can check that you're actually using their own drives.
[1683.68 → 1685.92] Oh, that's great value.
[1685.92 → 1688.60] I mean, it's just a lot more.
[1689.10 → 1690.34] It's just rent-seeking.
[1690.60 → 1691.30] Sun did this, too.
[1691.82 → 1691.94] Yeah.
[1692.20 → 1692.34] Yeah.
[1692.78 → 1694.12] It's such a bad thing.
[1694.12 → 1701.14] We tried to buy a BOD from Sun once, and they were like, well, you've got to buy a disk in all 24 slots.
[1701.54 → 1703.62] I'm like, well, but we've got lots of disks.
[1703.82 → 1704.54] Oh, no, you don't.
[1704.62 → 1704.88] Can we?
[1706.42 → 1707.30] Not yet you don't.
[1707.30 → 1710.74] And, yeah, it was just like, well, we're not going to sell you the sleds.
[1711.10 → 1711.66] How about that?
[1711.98 → 1713.98] I'm like, but the sleds are a small piece of plastic.
[1714.14 → 1715.26] Can we have the sleds, please?
[1715.66 → 1716.06] Like, no.
[1716.46 → 1717.64] One million dollars each.
[1717.64 → 1720.80] The sleds are the cost of a drive, plus 10%, because you're annoying.
[1722.50 → 1725.42] So there is the opposite extreme of that, though.
[1726.40 → 1729.06] We dealt with Bods a lot at Drive Scale.
[1729.20 → 1737.18] But WD was selling these populated Bods that were so cheap that people would buy the Bods, take the drives out, resell the drives,
[1737.30 → 1741.44] and then sell the MAJOR on eBay for like 500 bucks.
[1742.48 → 1742.62] Yeah.
[1742.72 → 1742.88] Yeah.
[1743.08 → 1749.50] Basically, we had a galactic pile of 250 gig spindles that no one was ever going to use, basically.
[1749.50 → 1751.50] Because in the end, that was just easier than...
[1752.68 → 1758.88] Because we could replace them with two terabyte spindles at a huge decrease in price.
[1760.44 → 1763.86] Tom, when you were at Drive Scale, you were obviously dealing with a bunch of different kinds of storage.
[1763.98 → 1766.48] So you must have seen all manner of drive firmware problems.
[1767.30 → 1767.84] Yeah.
[1767.94 → 1774.90] One of my favourites was Seagate was that just to query the smart status, you know, tell me a few counters.
[1775.60 → 1778.44] It was a 200 millisecond overhead.
[1779.52 → 1781.80] Nothing else would happen on the drive.
[1783.50 → 1786.28] And this is like, you're like, what is going on for 200 milliseconds?
[1787.08 → 1787.66] What are you doing?
[1787.94 → 1790.72] How many head seeks is it to ask your smart status?
[1791.60 → 1791.88] Yeah.
[1792.00 → 1793.98] I was like, what could they possibly be doing?
[1793.98 → 1796.16] Busy dumping core.
[1797.08 → 1798.88] Or maybe like, or rebooting.
[1799.00 → 1802.46] I mean, you're just like, not being able to kind of see into what's actually going on.
[1802.52 → 1808.90] I think like smart is another good example where, I mean, smart, what does the even acronym stand for?
[1809.36 → 1811.04] Sadly, it's an acronym.
[1811.04 → 1820.00] But this is for the giving you drive health statistics that are infamously always zero because the vendor doesn't want the drive to come back.
[1820.10 → 1821.26] So, of course, like the vendor's like, no, no.
[1821.42 → 1824.78] If I'm telling you I'm going to sick, I'm going to do it on a hidden mode page.
[1824.84 → 1826.76] I'm not actually going to do it in the smart data.
[1829.40 → 1829.96] I've got it.
[1829.96 → 1830.74] I've got it up, Brian.
[1830.80 → 1832.40] Do you want to guess what smart stands for?
[1832.40 → 1835.66] Does the S stand for smart, first?
[1836.30 → 1838.50] It's got to be simple or something, right?
[1839.14 → 1840.66] So, it's self-monitoring.
[1840.74 → 1841.56] Oh, self-monitoring.
[1843.10 → 1845.90] Self-monitoring and?
[1848.10 → 1851.12] Analysis and reporting technology.
[1851.78 → 1852.26] Technology.
[1852.64 → 1852.86] Yeah.
[1853.22 → 1854.10] That's, no.
[1854.22 → 1854.70] It's right there.
[1854.76 → 1854.96] Bad.
[1855.04 → 1855.14] Yeah.
[1855.14 → 1856.86] It's bad.
[1857.26 → 1857.98] It's all bad.
[1858.16 → 1863.40] It's like, one, I think like, and I say this as the company that worked for it, we had a product called like Smart Everything.
[1863.70 → 1864.78] I think Smart is a terrible name.
[1864.90 → 1865.78] I didn't know any of those products.
[1865.94 → 1868.46] I think Smart is, Smart just sounds smarmy.
[1868.80 → 1870.08] Like, don't call yourself smart.
[1871.88 → 1873.06] You're just inviting disaster.
[1873.06 → 1874.88] I think you're just inviting disaster by calling yourself smart.
[1875.22 → 1875.54] Exactly.
[1875.78 → 1876.44] Don't call yourself smart.
[1877.66 → 1879.96] I like the products that call themselves dumb.
[1880.64 → 1884.80] And the ADM 3A, they actually marketed it as a dumb terminal.
[1884.80 → 1885.52] That was awesome.
[1885.64 → 1886.38] There you go.
[1886.58 → 1886.94] That's right.
[1887.02 → 1887.42] Well, that's it.
[1887.48 → 1890.18] You know, we call that simple, where I'm coming from.
[1890.36 → 1891.36] I guess simple is good.
[1891.44 → 1891.94] We like simple.
[1893.18 → 1894.20] Simple is definitely good.
[1895.54 → 1910.88] When I did, you know, Rick made an interesting point, and unfortunately, before I'm going to assume the Twitter spaces ran out of memory and dropped it, but made an interesting point, and I think, Adam, this is true for us as well, that the one upside of having terrible dry firmware is it really requires you to get the firmware upgrade story right.
[1912.52 → 1912.90] Oh, yeah.
[1913.66 → 1914.74] Which we definitely did.
[1914.80 → 1928.10] I mean, we did spend a lot of time and energy allowing you to upgrade your disk firmware and getting that all correct, and that can all happen, fortunately, without actually, I mean, it can happen while the machine is up, which is gratifying.
[1928.10 → 1935.46] Yeah, and Brian, with regard, I'm getting more firmware, like horror story flashbacks.
[1935.46 → 1948.12] And tell me if this is, like, just, I've talked myself into this, if this is an embedded memory or a real one, but, like, with the LSI Flock problem, do I recall correctly that it was insufficient to, like, reboot the box?
[1948.12 → 1949.12] Yes.
[1949.12 → 1951.12] Because that HPA actually stayed powered.
[1951.12 → 1952.12] Yes, right.
[1952.12 → 1961.74] So the support procedure for that was put down the phone, walk over to the system, yank out the power cables, and put them back in.
[1961.96 → 1962.68] Am I making that up?
[1962.68 → 1963.54] No, I don't think you're making that up.
[1963.54 → 1963.76] Okay.
[1964.10 → 1966.04] Yeah, no, you're not making that up.
[1966.04 → 1966.22] Yeah.
[1966.22 → 1967.74] Because, because...
[1967.74 → 1970.58] Make sure you wait 30 seconds for the capacitors to drain through, right?
[1970.58 → 1970.90] Right.
[1971.52 → 1972.02] That's right.
[1972.32 → 1972.98] Count to 30.
[1973.26 → 1973.48] Right.
[1973.48 → 1984.50] And part of the problem was that an oversight of that system was that, like, the LOM couldn't actually do a full power reset of all those components.
[1985.72 → 1995.70] Yeah, and speaking of the LOM, we were not spared the most cruelly ironic firmware bug that we actually had on that system, I felt, was an actual Sun firmware bug.
[1996.22 → 1996.86] That's right.
[1996.96 → 2003.82] Where the service processor was a Java program, of course, because what else would you write a service processor in?
[2003.92 → 2005.14] Like, let's make sure we're writing it in.
[2005.38 → 2008.10] Just check your stock ticker and write it in that.
[2008.12 → 2008.92] Oh, stop.
[2009.60 → 2010.88] Oh, that's so cutting.
[2011.62 → 2013.10] God, that's so cutting.
[2013.90 → 2014.72] Oh, man.
[2016.08 → 2017.34] Now I'm just sad.
[2017.44 → 2017.60] All right.
[2017.66 → 2018.24] Yeah, so fine.
[2018.64 → 2019.60] Yeah, check your stock ticker.
[2019.72 → 2024.98] Write it in whatever application is reflected, whatever language is reflected in the stock ticker, in this case, Java.
[2026.22 → 2028.34] And which is, again, also, like, fine, perhaps.
[2028.42 → 2042.62] But this thing would do what many Java programs would do is it would actually grow without bounds and get to the point where GC is running all the time and not finding any garbage because the heap has effectively grown without bounds.
[2042.62 → 2056.08] And then it would somewhat amusingly, the service processor would, in this, now, like, allocations are failing.
[2056.08 → 2059.94] And it now doesn't know about itself from the CLI.
[2060.06 → 2064.30] So you would say, I want to reset slash, what?
[2064.70 → 2066.34] Reset slash Says slash SP, right?
[2066.42 → 2067.18] Something I thought I'm trying to remember.
[2067.18 → 2067.36] Right.
[2067.36 → 2067.58] Exactly.
[2067.68 → 2067.78] Right.
[2068.10 → 2071.48] And it would tell you, like, no such object SP.
[2072.50 → 2074.04] It's like, you are the SP.
[2074.40 → 2076.00] And we're having a good thing I'm talking to.
[2076.00 → 2081.54] Like, we're having a very metaphorical, like, a very metaphysical kind of solipsistic conversation here.
[2081.62 → 2083.46] But, like, do you not exist?
[2083.52 → 2084.06] Do I not exist?
[2084.20 → 2085.86] Are we in the simulation?
[2086.06 → 2086.88] Is none of this real?
[2087.58 → 2089.32] Are we all filled with existential dread?
[2090.98 → 2094.00] Which is, that was very, so that was very frustrating.
[2094.12 → 2098.74] But when that would happen, we would now neglect to control the fans properly.
[2098.74 → 2101.70] And the fans would, yeah.
[2101.76 → 2105.50] Well, the other way around, the fans would say, what the fuck happened to the SP?
[2105.96 → 2106.16] Right.
[2106.38 → 2110.14] Like, full power to the torpedoes.
[2110.14 → 2116.72] Full power to the torpedoes, which feels like a sensual, like, that feels like a fail-safe kind of thing, is to run the fans full speed.
[2116.72 → 2128.56] It's like, well, it might be if we didn't have these little Hitachi Bronco KS in there that were very vibe sensitive and a chassis that was maybe not really, maybe had some vibe issues.
[2130.04 → 2130.38] That's right.
[2130.58 → 2143.00] And I don't remember this part, but we had chosen the processor on these systems to be a little cooler and then capped the fan speed at, like, 80%, knowing that that was safe.
[2143.00 → 2150.14] But this fail-safe mechanism blew through that 80% cap to go at full 100%.
[2150.14 → 2154.84] Full 100%, and then the drives themselves started getting ridiculous IO latency outliers.
[2155.02 → 2164.54] So then you start saying, like, thousands of milliseconds because it's getting what are called non-repeated run outs, which, where the head is, the whole chassis is vibing itself to death.
[2165.04 → 2168.78] So the head is having a very hard time tracking and is constantly having, you know,
[2168.78 → 2182.20] Rick made this interesting point, too, about just changing the number of retries on a drive, where the drive has no other way of telling you, like, I am in tremendous pain and there are many problems here, and I need attention.
[2182.20 → 2187.28] So all it has, really, is read and write and tell me how you're feeling.
[2187.40 → 2190.56] And, like, by the way, I can never tell you that I'm feeling sick because otherwise you'll replace me.
[2190.80 → 2191.58] So I don't want that.
[2191.58 → 2194.04] So I need to, like – I'm always, like, by the way, I'm feeling great.
[2194.94 → 2200.54] And on the reads and writes, it's like I'm just going to keep trying, like, what else am I going to do?
[2200.62 → 2201.38] It's like, well, fuck.
[2201.46 → 2202.48] You could, like – I don't know.
[2203.18 → 2203.98] Like –
[2203.98 → 2205.16] Like, the data is here somewhere.
[2205.30 → 2205.98] The data is here somewhere.
[2206.10 → 2207.54] I'll have it for you in two weeks.
[2207.66 → 2208.54] Like, I swear on you.
[2208.54 → 2208.86] Totally.
[2209.38 → 2209.70] Totally.
[2210.06 → 2210.34] Totally.
[2210.40 → 2214.46] It's like someone who's made, like, a cascade of bad life choices and, like, it's all coming due.
[2214.56 → 2215.62] Like, the debt's all coming due.
[2215.62 → 2220.10] Like, you're not – no, it's like you're not – I paid off the visa with the MasterCard bill.
[2220.10 → 2222.26] And I got a payday loan for the MasterCard.
[2222.34 → 2224.22] And now it's, like – now they're redoing everything.
[2224.28 → 2225.46] It's just, like, the whole thing's coming.
[2225.60 → 2226.60] Like, the ads.
[2228.62 → 2235.68] Retry forever failure is also one way in which they've created artificial differentiation between consumer and Newline drives.
[2236.60 → 2237.08] Oh, that's right.
[2237.08 → 2246.20] Like, consumer drives will retry forever, basically, which is not terribly good for a rate array that could say, well, I'm, like, you know, just fail and I'll figure it out, right?
[2246.20 → 2247.92] Oh, that's so wrong.
[2247.92 → 2255.52] So that they can charge, you know, 80 extra bucks a drive or 150 or something for slightly better –
[2255.52 → 2256.82] Oh, you want me to break out of that loop?
[2257.00 → 2258.10] That's – I mean, I can do it.
[2258.16 → 2258.74] It's going to cost you.
[2258.78 → 2259.28] But it's not free.
[2259.62 → 2260.98] It's going to cost you.
[2261.00 → 2262.50] It's not free for me to do less work.
[2263.12 → 2264.64] You're like, what's going on?
[2264.70 → 2264.88] Right.
[2265.04 → 2267.30] Why are you – yeah, that's brutal.
[2267.30 → 2276.62] This is in line with other products where the consumer product is cheap and full of features and the professional product just does one thing well.
[2277.38 → 2278.58] Or does one thing anyway.
[2282.30 → 2282.66] Yeah.
[2284.20 → 2286.62] And certainly after – I came out of that.
[2286.68 → 2292.50] I don't know, Adam, if you ended up – so we – after Sun, you went to Delphi.
[2292.50 → 2293.22] We were enjoying it.
[2293.70 → 2299.34] Well, I mean, when I went out of Sun, I mean, the lesson I learned from that was different from the lesson you learned.
[2299.42 → 2302.16] The lesson I learned was stay the hell away from hardware.
[2302.70 → 2304.72] I mean, obviously, I've unlearned that fast.
[2304.82 → 2304.94] Right.
[2304.98 → 2305.24] There you go.
[2305.26 → 2306.02] You've forgotten that lesson.
[2306.18 → 2306.30] Right.
[2306.32 → 2307.36] We're trying to remind you that lesson.
[2307.40 → 2310.26] That's why I coasted into like virtual.
[2311.54 → 2316.00] So you – well, this is not an uncommon lesson that people learn when dealing with hardware.
[2316.12 → 2317.56] It's like I never want to deal with hardware again.
[2317.68 → 2319.44] Like this is actually – hardware is hard.
[2319.44 → 2320.02] I mean, it's painful.
[2320.18 → 2322.60] It's awful when these things –
[2322.60 → 2328.36] Well, I think in particular at the time, you know, people were asking why did we not do Phish works as a startup?
[2329.30 → 2344.64] And I think our analysis, at least that I recall it, was accurate, which was it being hard enough for us, Sun, to get the attention of all of these component vendors to please fix these – what would have been business-ending bugs.
[2344.64 → 2349.20] And for like an insignificant startup to get that good attention would have been untenable.
[2349.94 → 2351.96] And I think the world has changed a lot since then.
[2352.36 → 2352.62] Yeah.
[2352.70 → 2353.34] No, I think you're right.
[2353.46 → 2369.06] And I think that the – I think also in a world of all closed firmware, all proprietary firmware, it is actually – I mean, this is part of why we need an open firmware ecosystem is to allow for more innovation and more companies to be able to do things more cheaply.
[2369.06 → 2375.36] Because we – you could not – you're exactly right that like we could not have done it simply because we could not have gotten the attention that we needed.
[2375.52 → 2385.94] I mean, hell, at Oxide, it's hard to get the attention that we – I mean, we're very good at making a racket, but it is hard to get what – you know, we've got – and we've got very little proprietary firmware in the stack.
[2385.94 → 2392.98] But as Laura can attest, like the proprietary firmware we do have is making its proprietaries well-known, unfortunately.
[2395.42 → 2404.26] So I'm curious with this group of people who've been tortured by hard drives and have tortured them in return, what do you actually want from the hard drive API?
[2404.82 → 2414.18] Like, do you want to be able to say on every request, hey, give me a fast read or give me a reliable read or give me a really absolutely try as hard as you can to give me a read?
[2414.18 → 2414.74] Read.
[2415.92 → 2417.16] So I –
[2417.16 → 2422.88] Like, it feels weird to change the firmware on the drive rather than having a different kind of request for that request.
[2423.98 → 2429.68] So in all honesty, and I know this is just very on-brand for me to say this, I actually want an open ecosystem.
[2430.20 → 2433.18] I want – I don't think one size fits all.
[2433.18 → 2446.16] And I think that different people may want different behaviour, and we should have – just as we are able to programmatically change our behaviour elsewhere in the stack, we should be able to programmatically change our behaviour with respect to drive firmware.
[2446.88 → 2447.18] So –
[2447.18 → 2448.64] Software-defined hard drive.
[2448.64 → 2452.26] Well, the thing is we already have a software-defined hard drive.
[2452.38 → 2455.08] It is just that it's a proprietary-defined hard drive right now.
[2455.60 → 2457.14] And so we –
[2457.14 → 2468.32] There's a major philosophical thing too, which it all comes from the school of thought that nothing is ever going to fail except in very rare situations as opposed to the networking point of view.
[2468.48 → 2469.86] It's like you're lucky if anything works.
[2469.86 → 2477.38] And if you are protecting the whole stack to be – if you feel lucky, then things work a lot better.
[2477.80 → 2479.30] Tom, it's interesting you say that.
[2479.30 → 2484.30] And I think the Apple WDG conference was today.
[2484.64 → 2492.84] And I bring that up because like in 2016 or something, they were rolling out their APFS, their new file system from scratch.
[2492.88 → 2494.26] And I went and talked to some of those folks.
[2494.26 → 2508.24] And to your point, Tom, they actually claimed that they did not see bit errors, that bit rot was a – was like the product of mass hysteria.
[2509.46 → 2518.54] And to which I said, well, with HFS, you're – you know, the file system you've been monitoring for years, you just wouldn't know because you'd just have things change, and you'd have no way of identifying that.
[2518.54 → 2548.52] And –
[2548.52 → 2550.30] You're the only one asking that question.
[2550.42 → 2551.42] We've never heard that question before.
[2551.70 → 2552.52] We've never –
[2552.52 → 2554.08] That's right.
[2555.36 → 2559.84] Yeah, that's – I mean, so that's interesting with the kind of the APFS analog.
[2560.06 → 2568.78] And just in terms of like the – and Tom, that's a very good point too about this kind of the storage thinking versus networking thinking because I feel we saw this too.
[2568.82 → 2571.52] I feel like we were helping to perpetuate this, Adam.
[2571.54 → 2576.06] I feel like we – because we were captained in 2006, I feel.
[2576.06 → 2584.06] Like we had – we were trying to sell highly available, highly reliable storage by pretending that a partition couldn't possibly happen.
[2585.36 → 2586.44] Yeah, yeah.
[2586.58 → 2592.22] And I don't know the degree to which we were pretending with well-knowing or pretending well not knowing.
[2592.84 → 2593.16] Right.
[2593.16 → 2596.10] You can't just go around declaring that the network is the computer.
[2596.20 → 2596.82] That's right.
[2597.78 → 2598.82] Not unless you're Cloudflare.
[2599.34 → 2601.30] I – yeah.
[2601.38 → 2611.00] And I think that the – so I think part of the problem is that just as Tom said that there has been this – the way you deal with failure.
[2611.00 → 2616.46] Because the other problem, I think, is that like if a packet is dropped, the NIC does not get returned.
[2617.48 → 2623.00] So it is – there's obviously so much that can fail in the network that that's not necessarily on the component.
[2623.16 → 2627.88] I think that the drive feels that like if I report an error, like I'm going to be returned.
[2628.12 → 2629.46] It's like, well, yes, probably.
[2629.56 → 2630.72] But you still need to report the error.
[2630.92 → 2632.00] It doesn't mean that you –
[2632.00 → 2634.84] And then the whole ecosystem.
[2635.16 → 2643.24] So if there's a link error talking to the drive, and it gets recorded, everyone goes completely batshit insane all the way up to the application.
[2644.22 → 2646.16] You know, as opposed to saying, oh, there was a glitch.
[2646.26 → 2646.78] Let's try again.
[2647.00 → 2647.40] Right.
[2647.80 → 2648.28] That's right.
[2648.54 → 2653.90] I mean – and also, I mean, I think there is a degree to which like it is actual – you know, it's persistent.
[2653.90 → 2666.96] So if you do have these failure modes, like this crazy failure mode that we didn't see where the drive would lose its metadata, and they'd never be able to boot again, you do have these pathologies that are arguably much more acute.
[2668.74 → 2671.16] But still, it's like, oh, man, we can do better than this, though.
[2671.34 → 2671.86] So, Aaron, I don't know.
[2671.92 → 2673.64] How is that as an answer to your question?
[2676.76 → 2677.56] Sounds good to me.
[2679.12 → 2679.44] Yeah.
[2679.62 → 2681.34] I think – well, and it sounds good to a lot of people.
[2681.34 → 2688.02] I mean, I think that, you know, we've obviously got a bunch of kind of core beliefs at Oxide, but open firmware is a pretty deeply held one.
[2688.80 → 2696.90] Yeah, and I wonder how, you know, behind a lot of the firmware that we're talking about here is this real complex engineering and science and physics.
[2698.06 → 2703.42] And that, while complex, is often tending towards commoditization.
[2703.42 → 2716.58] So, you know, one of the questions I have is how we break this idea that firmware is the path to greater revenue and margin and differentiation.
[2717.16 → 2718.76] Yeah, this is a good point, Adam.
[2718.84 → 2723.34] And, like, that firmware is your path to preservation of that innovation.
[2724.00 → 2724.54] That's right.
[2724.54 → 2735.44] And it is, like, super tragic, especially when you get into the physics of these drives, which are the – and we are not using rotating media at Oxide, not yet anyway, not in our first product.
[2735.88 → 2740.20] We presumably will at some point just because the density advantages are so great.
[2740.40 → 2742.88] But the – do you think about Hammer versus Mammal, Adam?
[2743.02 → 2744.94] Have you ramped up on any of this stuff?
[2745.66 → 2746.32] Or have you been –
[2746.32 → 2746.54] No.
[2746.54 → 2746.94] Yeah, right.
[2747.00 → 2749.28] You would love this stuff.
[2749.60 → 2753.32] So, Hammer is heat-assisted magnetic recording.
[2753.58 → 2756.98] Mammal is microwave-assisted magnetic recording.
[2757.74 → 2769.48] And they are effectively – so, with Hammer, you are superheating for periods of femtoseconds, literally, in tiny areas.
[2769.48 → 2773.36] So, you can write higher-density bits.
[2773.36 → 2776.80] And it's, like, crazy interesting.
[2777.04 → 2782.16] And you're, like, wow, how is the physics this, like, off the charts nuts?
[2782.48 → 2785.28] And then you're, like, not using source code control for your firmware.
[2785.64 → 2789.70] I feel like – I mean, it makes me feel bad as a software engineer.
[2790.52 → 2790.96] Right?
[2791.36 → 2791.64] Yeah.
[2791.78 → 2796.24] I think the trouble is these companies don't admit that firmware is software.
[2797.80 → 2799.86] It's just, like, something the hardware guys all do.
[2799.86 → 2801.88] Or that it's as critical a component.
[2801.88 → 2806.14] I mean, to your point, Tom, that, you know, this becomes the weak link in so many devices.
[2806.76 → 2806.96] Right.
[2807.08 → 2808.72] I mean, software is eating the world.
[2808.88 → 2811.94] And these guys are software companies, but they won't admit it.
[2812.54 → 2815.52] Yeah, that's interesting, actually, that you said that.
[2815.58 → 2824.18] Because we definitely – we've got one colleague in particular who is very – he is fighting the lone fight against the term firmware.
[2824.28 → 2825.34] It's like, firmware is software.
[2825.34 → 2827.98] Like, to not – like, we are – it is software.
[2828.14 → 2830.12] It is a software – it is very low-level software.
[2832.04 → 2832.72] And it is.
[2832.78 → 2833.38] Like, he's not wrong.
[2833.48 → 2834.14] It is software.
[2834.70 → 2838.00] Well, and it's not even necessarily very low-level anymore.
[2838.20 → 2840.54] I mean, look at – like, we talk about hard drives.
[2840.60 → 2846.34] But look at SSDs, which are taking a totally different technology and then pretending to be hard drives out the other side.
[2846.34 → 2846.74] Right.
[2848.08 → 2853.56] Masquerading is this interface that made sense for spinning media to a degree and just really doesn't for those.
[2853.66 → 2856.70] So the complexity of the software in there is enormous.
[2857.22 → 2859.52] And hybrid storage devices.
[2859.72 → 2863.18] I mean, how many of these things are running, like, a badly patched copy of the Linux kernel?
[2863.46 → 2863.90] Right.
[2863.90 → 2864.72] That's my question.
[2865.20 → 2865.60] Totally.
[2867.10 → 2867.54] Right.
[2867.90 → 2868.30] Right.
[2868.38 → 2868.72] Exactly.
[2868.94 → 2874.30] Well, and then you – see, you run – what's really troubling is that you run strings on these binaries that you're getting from the vendor.
[2874.30 → 2876.46] You're like, why is there a URL in this firmware?
[2876.62 → 2878.00] I'm like, what's going on exactly?
[2879.12 → 2884.34] Dan, to your question about, like, how much unpatched Linux kernels or what have you are around here.
[2884.36 → 2884.92] No, it's very troubling.
[2885.16 → 2896.14] And Adam, the point about, like, these SSDs being these very complicated little worlds in there that have got their own – tons of their own complexity that we don't have this ability into because it's trying to pretend its something else.
[2898.48 → 2903.32] Is there any – because actually, you know, it is funny is that there is – speaking of SSDs,
[2903.32 → 2908.14] the only firmware that did not give us really acute pain.
[2908.26 → 2910.46] I feel like we did not have a Godzilla problem.
[2910.66 → 2911.46] Am I wrong, Adam?
[2911.52 → 2911.70] Yeah.
[2911.98 → 2913.98] No, I think that's right with Ester.
[2914.16 → 2914.66] With Ester.
[2914.66 → 2918.58] Which got acquired by WD or where did they get bought?
[2918.88 → 2919.22] No.
[2919.40 → 2920.88] Yeah, they went to WD eventually.
[2921.06 → 2921.16] Yeah.
[2921.28 → 2924.08] But, I mean, the – I mean, are you going to tell the Ester story?
[2924.08 → 2925.38] The Ester story is pretty great.
[2926.94 → 2927.18] So –
[2927.18 → 2928.82] I mean – yeah, go ahead, please.
[2928.82 → 2942.06] Well, you know that – so we were dealing – so Ester was a company – I mean, Adam was, I dare say, the first person to really look – I mean, other people were making this observation at the same time.
[2942.10 → 2947.74] But, Adam, you were very early on making the observation that Flash could be used in an enterprise storage product.
[2947.74 → 2950.12] Yeah, we were really at the right place at the right time there.
[2950.38 → 2957.20] But because with the advent of the iPhone, the economics on Flash changed really, really quickly.
[2957.28 → 2958.32] I mean, right out from under us.
[2958.38 → 2966.74] We're at the point where the early Flash drives that we got were intended for use in, like, helicopters and high-vibe environments.
[2966.74 → 2979.90] And then a month later, the samples we got were – they had figured out, like, high-performance Flash could be more economical than just shoving a bunch of drams and a battery into a three-and-a-half-inch enclosure.
[2980.76 → 2983.50] And we – which is what we wanted to avoid.
[2983.64 → 2985.70] We wanted to avoid the battery in particular.
[2985.90 → 2990.98] We were using Flash first and foremost for non-volatile store that we could write too quickly.
[2990.98 → 2995.50] And we found this company called Ester that was the leader of the space, really.
[2995.62 → 2996.86] I mean, they were the pioneer in the space.
[2998.16 → 3001.86] Well, you know, they bought this company, Gnu Tech, to buy them a way in.
[3002.26 → 3010.34] Ester had this whole consumer brand of, like, rebranded hard drives and rebranded memory, which later they divested.
[3010.50 → 3012.22] They bought this company, Gnu Tech, out of England.
[3012.40 → 3013.20] So I don't know if you remember this brand.
[3013.20 → 3013.94] I've forgotten that, yeah.
[3013.94 → 3016.32] When you say Gnu –
[3016.32 → 3019.02] I'd like to interject for a moment.
[3019.02 → 3019.82] Yeah, yeah, no.
[3019.98 → 3021.26] That Gnu is not Linux.
[3021.48 → 3021.82] Yeah, right.
[3022.62 → 3022.98] Right.
[3023.30 → 3026.82] I don't know if you remember this part, Brian, but the first samples we got of those Ester drives,
[3026.92 → 3035.58] we couldn't plug in until I had gone down to the Kohl hardware to get metric screws because they wouldn't –
[3035.58 → 3038.66] the screws we had would not fit into these components.
[3039.06 → 3045.66] Adam, you'd be happy to know that Googling Gnu Tech Ester yields your blog on –
[3045.66 → 3050.32] I was trying to corroborate what you were saying, but I'm like, oh, this person seems to agree.
[3050.36 → 3050.80] Hey, wait a minute.
[3050.96 → 3051.70] It's past that.
[3051.76 → 3052.44] Wait a minute.
[3052.48 → 3053.20] Wait a minute.
[3054.60 → 3059.18] But so we were – I mean an early customer for that.
[3059.18 → 3065.86] So Mark Machete, one of these two brothers that were running the company, the Machete brothers,
[3066.86 → 3069.18] and Mark was spending a lot of time with Fish works.
[3070.06 → 3070.84] Yeah, yeah, yeah.
[3070.88 → 3075.36] And you know that – I mean you know that Mark came within a hair's width of going to jail.
[3076.64 → 3077.54] I do know that.
[3077.62 → 3078.10] I do know.
[3078.24 → 3079.78] I followed that with great interest.
[3079.78 → 3087.98] So they, as it turns out, were crooked as all get out in a – and actually, Tom, I would love to know how classic this scam is.
[3088.22 → 3089.12] They were stuffing the channel.
[3089.78 → 3091.28] So they were a public company.
[3091.94 → 3099.38] They were stuffing the channel, which is where you basically are marking a bunch of sales that you haven't necessarily made
[3099.38 → 3101.48] because you filled the channel with your product.
[3102.28 → 3107.12] But as a – so your sales will go way, way up, and then they'll come way, way down because people now have your product.
[3107.20 → 3110.12] They're not going to need it for a long time because they've stockpiled a bunch of it effectively.
[3111.34 → 3114.42] And as memory serves, they were stuffing the channel with EMC, I think.
[3114.78 → 3120.52] Yeah, I think – actually, I think one of the problems that they ran into is that they had sold a bunch of the EMC,
[3120.68 → 3123.38] but EMC was not able to move them quickly enough.
[3123.38 → 3128.22] And I remember this, but EMC priced them just ludicrously.
[3128.22 → 3133.82] These parts that we were selling for $5,000, $10,000, $20,000, they were selling for like $100,000.
[3134.30 → 3141.54] And when we did the math, we determined that they were using spinning disks to get a price per IOP
[3141.54 → 3145.94] and then just multiplying that based on what these SSDs could do.
[3146.62 → 3148.66] So they were ludicrously expensive.
[3148.88 → 3151.66] So then they had bought a bunch of them and then weren't selling them.
[3152.92 → 3155.28] And Ester was a public company at this point.
[3155.28 → 3158.62] They communicated to Ester that they weren't going to be buying anymore for a while.
[3159.48 → 3168.28] Ester then, in their earnings call, in their 10K or 10Q or whatever, made no mention of this.
[3169.40 → 3174.94] And then some insiders traded on that non-public information.
[3174.96 → 3176.00] Yeah, as it turns out, they sold high.
[3176.16 → 3177.82] As it turns out, they had some insider information.
[3177.94 → 3179.44] Namely, we've stuffed the channel.
[3179.72 → 3182.12] So we're just going to sell it all.
[3182.12 → 3186.66] As it turns out, the SEC is like, yeah, actually, you're not the first person to think of this crime.
[3186.82 → 3190.56] This crime is not the master crime that you might think it is.
[3190.68 → 3191.40] This is actually –
[3191.40 → 3192.50] We have a whole name for that one.
[3192.52 → 3193.88] We have a whole name for that one, actually.
[3194.12 → 3195.08] And it's like, you're going to jail.
[3195.28 → 3199.56] But he – I feel like he walked on a technicality.
[3199.56 → 3208.74] I think they were able to clear it up somehow in some, like, arrested development type scheme.
[3209.26 → 3210.74] I don't know the details.
[3211.52 → 3219.12] But kind of pulling out of this particular nosedive, to your point, yes, I don't think their firmware ever screwed with us the way that other firms are.
[3219.12 → 3220.28] Well, this is like the irony.
[3220.46 → 3222.88] Is this what we need to do to get, like, correct firmware?
[3223.02 → 3224.94] We need to go to, like, crooked people?
[3224.94 → 3231.60] Like, can we – come on, world, don't make us go – I do have the – I mean, God bless the SEC.
[3231.78 → 3240.54] I do actually have the full SEC complaint featuring the Zeus IOPS, which is the product that we had that we called Godzilla, very prominently.
[3240.86 → 3243.52] So it's all a statement of fact on the record.
[3243.52 → 3246.54] I seem to remember the stack drive.
[3246.64 → 3250.24] I don't know if it's the same one, but it had no firmware at all.
[3250.34 → 3252.16] It was an actual hardware device.
[3252.16 → 3255.74] No, you know what?
[3255.76 → 3257.46] They did have an FPGA on there.
[3258.78 → 3264.16] So I don't know what – I don't know how we're going to want to classify that as firmware, software, or none of the above.
[3265.12 → 3270.64] But I do remember that the FPGA was doing a lot of work there.
[3271.10 → 3275.60] And one of their – the big piece of their milestones was going to an ASIC version of their product.
[3275.70 → 3277.60] I mean, again, this is ancient history now.
[3277.60 → 3279.56] But that's actually fascinating, though.
[3279.56 → 3282.64] It's when microprocessors show up that all the trouble starts.
[3284.00 → 3285.24] No, yeah, that's right.
[3285.30 → 3286.36] I think that's fascinating.
[3286.60 → 3292.24] That, like, actually the fact that it – I did not realize that, Tom, but that makes sense, actually.
[3293.10 → 3301.04] That we – that you – because it is – FPGAs don't tend to have the same pathologies as firmware.
[3301.04 → 3305.16] And that is fascinating.
[3305.52 → 3308.46] Yeah, when the microcontrollers show up, that's when the trouble starts.
[3308.60 → 3309.72] That's definitely true.
[3312.36 → 3315.20] Yeah, that is – that is sad.
[3315.40 → 3316.86] I mean, we've got to do better than that, though, right?
[3316.86 → 3319.64] So, I mean, so what we need – so, Tom, how do we counter that?
[3319.94 → 3320.68] Because I think you're right.
[3320.78 → 3322.50] Like, that does seem to be a problem.
[3322.50 → 3326.28] Obviously, I think open source is a big part of the answer.
[3326.46 → 3327.24] What's your take?
[3328.08 → 3334.72] Yeah, I mean, a clear boundary between hardware and software and admitting that software is never correct.
[3335.02 → 3338.30] So, there has to be a way to improve rapidly.
[3340.34 → 3345.22] But managing firmware like it's just another hardware component is a disaster.
[3345.22 → 3348.46] That is it.
[3348.88 → 3351.76] Yeah, managing – I think that – think of – you've got to think of firmware.
[3351.86 → 3352.90] Firmware is software.
[3353.08 → 3354.04] It is actually not hardware.
[3354.44 → 3360.38] And thinking of it as a hardware component is the way you end up delivering things out of home directories and having –
[3360.38 → 3362.48] And software is clearly never done.
[3363.18 → 3364.14] It's never correct.
[3364.96 → 3367.46] It can only get better, but it usually gets worse.
[3370.60 → 3372.64] I thought you were going to leave us on such an optimistic note.
[3372.64 → 3376.10] But then I got to drag us right back down.
[3378.02 → 3378.46] All right.
[3378.50 → 3380.40] Well, we've been looking to keep these to about an hour.
[3380.96 → 3385.26] I think that's as good a note to wrap up on as any.
[3385.40 → 3386.86] Thank you very much, everyone.
[3387.00 → 3391.24] Definitely let us know things you want to talk about, other feedback you might have for us.
[3391.32 → 3393.44] I know, Adam, I'm continuing to have fun doing this.
[3393.56 → 3394.96] I'm not – how you feel, Tom?
[3395.00 → 3395.94] Thank you so much for joining us.
[3399.00 → 3399.76] Yeah, thanks, Tom.
[3399.76 → 3401.58] Thanks, everyone who chimed in with their stories.
[3401.68 → 3402.28] Really appreciate it.
[3402.28 → 3402.72] Good fun.
[3403.80 → 3404.12] Awesome.
[3404.22 → 3406.90] And I think we're going to take – at least I am out next week.
[3406.98 → 3409.12] We may be taking next week off, but I don't know.
[3409.20 → 3414.58] Adam, we've got to figure out our summer vacation schedules and get a schedule for our Twitter space.
[3415.68 → 3416.70] We'll keep you posted, folks.
[3416.72 → 3416.94] Awesome.
[3417.10 → 3417.56] Thanks, everyone.
[3417.68 → 3417.94] Take care.
[3418.66 → 3419.08] Thank you.
[3419.34 → 3419.72] Thank you.
[3419.72 → 3419.74] Thank you.
[3419.74 → 3419.78] Thank you.
[3419.78 → 3419.80] Thank you.
[3419.80 → 3421.84] Thank you.
[3421.84 → 3423.74] Thank you.
[3423.74 → 3423.84] Thank you.
[3423.84 → 3424.74] Thank you.
[3424.74 → 3425.74] Thank you.
[3425.74 → 3425.84] Thank you.
[3425.84 → 3427.80] Thank you.
[3427.80 → 3427.84] Thank you.
[3427.84 → 3427.90] Thank you.
[3427.90 → 3428.84] Thank you.
[3428.84 → 3429.84] Thank you.
[3429.84 → 3429.90] Thank you.
[3429.90 → 3430.90] Thank you.
[3430.90 → 3431.84] Thank you.
