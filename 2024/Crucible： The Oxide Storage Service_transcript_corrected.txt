[0.00 → 3.96] So Adam, I'm going to tell you words you don't want to hear.
[4.98 → 5.38] Namely.
[7.30 → 8.58] This could be anything.
[8.82 → 9.72] Like literally anything.
[10.24 → 10.92] In the wheel.
[11.06 → 13.62] He's like, there are so many words I don't want to hear you say.
[13.90 → 15.02] That wheel is so big.
[16.44 → 17.50] Where is this going to land?
[17.64 → 19.46] How many of the words are LLM?
[19.90 → 20.64] No, no, no, no, no.
[20.92 → 21.76] Okay, thank you.
[21.92 → 22.40] Quiet, dude.
[22.62 → 23.58] One of the words are LLM.
[24.22 → 26.56] But I have been thinking about our episode from last week.
[26.56 → 29.68] I know you're just like, no, Brian, you did the episode last week.
[30.00 → 31.82] No, we never talk about it again.
[31.98 → 34.04] You and nobody else.
[34.18 → 34.36] Yes.
[34.74 → 34.90] Right.
[34.96 → 35.34] Okay, right.
[36.08 → 40.68] And in the spirit of more answering questions that no one asked.
[42.04 → 44.74] So no, I was going to say, it actually is.
[44.90 → 53.04] This is actually on topic because I was thinking like as I was re-listening to it as I wanted to do.
[53.04 → 67.50] And I think I didn't really get to the crux of what I kind of find deeply annoying about Nate Silber's list of, you know, the top whatever, top 10 technologies from 1900 or from 2000 and comparing them.
[67.50 → 71.94] But here's my, like the fundamental issue is it's reductive.
[72.38 → 74.88] That's the problem is that it's reductive.
[75.02 → 85.54] And I actually like things that take seeming, that where you have seeming simplicity and you actually, there's, there's a world of complexity underneath it.
[85.54 → 87.64] Like that to me is actually a lot more interesting.
[88.86 → 91.46] And I'm glad you have the week to think about that.
[92.60 → 93.00] Yeah.
[93.30 → 96.44] You know, like, look, this is why it's, we're always better off.
[96.54 → 105.64] This is why like the talk that I prepare when I get trolled is actually like listenable versus like the podcast, which may not always be because it's a little too hot.
[105.64 → 107.04] But no, but I think this is the issue.
[107.12 → 109.34] Like the issue is it's, it's too reductive.
[109.46 → 125.32] And I think that it is too easy to take things for granted because we, because technologists spend a lot of time trying to make technology integrate into the into society, bluntly, in terms of like how we use it.
[125.42 → 127.64] And we don't want these things to be a giant pain in the ass.
[127.66 → 131.60] You shouldn't have to know how PCB works in order to be able to use one.
[131.60 → 135.16] And, or, and I think like that is like the fundamental issue.
[135.16 → 139.00] And as you know, I kind of think about my own interests.
[139.00 → 143.84] And I think that the interests of a lot of folks that are, are, are friends of oxide.
[145.00 → 150.98] It is the, the things that are interesting are where you, you take something that like, wow, that how hard can that be?
[151.86 → 156.10] And you take it apart, and you realize like, wow, this is actually extraordinarily complicated.
[156.10 → 161.52] And you get great reverence for like, wow, I will never think of a network switch the same way again, because wow, it is.
[161.60 → 163.46] So deeply complicated.
[163.64 → 165.42] I will never take boot for granted again.
[165.52 → 172.54] I will never, I will never take all of these, these kinds of unseen aspects of the system that are in this category of how complicated can it be?
[172.58 → 174.50] It's like, well, glad you asked because it's super complicated.
[174.50 → 182.54] And I think like, that's the thing when you just take that complexity and, and in Silver's case, he's like, doesn't know that it exists.
[182.66 → 191.78] So it's very easy for him to will it away because he doesn't, you know, not to sound, you know, well, I guess this is just going to sound terrible.
[191.78 → 197.58] But I, this is the challenge of when you have someone who doesn't, is not actually a technologist kind of weighing in on these things.
[197.58 → 204.22] It's like, you can do that, but you have to have great reverence for this hidden complexity, and you have to fight the urge to be reductive.
[205.50 → 207.72] So that brings us.
[207.86 → 207.98] With that.
[208.40 → 208.82] With that.
[208.82 → 209.86] To our simple storage service.
[210.02 → 211.02] To our simple storage service.
[211.28 → 213.28] No, actually, that's a great example, right?
[213.38 → 217.02] Because that is, I mean, that's actually, that's, that's very on point.
[217.02 → 222.64] I mean, I mean, how many people know that S3 is actually the simple storage service, and it ain't simple.
[223.12 → 231.82] I mean, it's anything but, and storage is kind of the Naples ultra of how hard can it be?
[232.46 → 233.22] And how hard can it be?
[233.34 → 235.48] Like, you're taking bits, and you're putting them over there.
[235.48 → 236.52] I got my bits.
[236.62 → 237.46] You're just moving things.
[237.52 → 238.40] Just moving things.
[238.50 → 239.88] Take the bits and store the bits.
[240.52 → 243.90] When I ask for the same bits back, give me the same bits.
[244.12 → 244.88] Like, really?
[244.98 → 245.68] Is that complicated?
[245.68 → 249.52] And Alan, I think it's, it's complicated is the answer.
[249.86 → 249.98] Yeah.
[250.62 → 250.80] Yeah.
[250.80 → 251.30] It's complicated.
[251.40 → 267.30] So we've got, so we're going to dive into storage and we, and I think we have been, Adam, you and I have been remiss to, to, we, this is a dimension of oxide that we have really, I know people rightfully think, you know, you people are such over sharers.
[267.30 → 272.66] It's like, there, anything that happens to oxide that you don't just prattle on about in 15 different podcast episodes?
[272.66 → 277.32] And the answer is like, yeah, there are still a bunch of things that we haven't really talked about.
[277.54 → 278.22] Stay tuned.
[278.54 → 279.06] Stay tuned.
[279.52 → 280.02] We will.
[281.36 → 287.12] And storage is a big one because the storage is really, really important in the rack.
[287.22 → 288.58] And we haven't really talked about storage at all.
[288.64 → 290.82] We kind of hit on it and, and it's open source.
[290.82 → 294.22] So we've had people out there that have been like, Hey, when are you guys going to talk about storage?
[294.26 → 295.14] This seems fascinating.
[295.56 → 300.26] So in the spirit of that, we've got a bunch of folks here have been working on Crucible.
[300.84 → 313.80] But Adam, I wonder if if you and Josh might kick it off with kind of the origin of this, because we were, when we started the company, we knew that we were going to have what one might call hyperconverged infrastructure.
[314.04 → 314.52] Hyperconverged infrastructure.
[314.64 → 316.40] How, how much does that term bother you, Adam?
[316.40 → 319.32] I think tremendously.
[320.88 → 323.92] I will be on the list of words you didn't want to hear from Brian.
[324.42 → 325.36] Yeah, yeah, yeah, yeah.
[325.40 → 329.10] That was, if I was writing a little note here, and I turn it over, and you finally got there.
[329.20 → 335.12] But I think because it sounds so kind of highfalutin and it is.
[335.32 → 337.20] And yet also, I don't know what it means.
[337.58 → 341.76] Yeah, I think it's, it's not, it's not well understood generally.
[342.20 → 345.26] And it really sounds magical.
[345.26 → 348.58] I mean, not just converged, but hyperconverged.
[349.86 → 349.90] Yeah.
[351.90 → 356.40] Critically, that's because we already had something that people were calling converged, right?
[356.72 → 357.46] Before that.
[358.24 → 359.04] So, yeah.
[359.22 → 360.70] And I also don't know what that means.
[361.12 → 362.14] So, yeah.
[362.68 → 364.88] You know, Adam, that dimension hadn't even occurred to me.
[365.04 → 367.92] There's like a converged is kind of like a Boolean property.
[367.92 → 369.74] And it's like, no, this is not just true.
[369.82 → 370.38] It's hyper true.
[370.94 → 371.10] It's like.
[371.52 → 373.44] You can't be hyper pregnant.
[373.88 → 374.14] Right.
[374.24 → 374.84] Hyper on.
[375.20 → 375.74] It's like, isn't it just.
[375.88 → 376.02] Right.
[376.14 → 376.64] No, it is.
[377.20 → 378.00] It's a goofy term.
[378.66 → 379.16] It's a goofy term.
[379.24 → 384.52] And people are using it to mean that, you know, sort of you get storage and memory and
[384.52 → 389.56] CPU all sort of in blocks together.
[390.12 → 390.92] Is that rough?
[391.12 → 392.48] No, isn't it meant to be.
[393.44 → 399.82] So, I vaguely remember EMC selling us a ridiculously expensive storage card that was both fibre
[399.82 → 403.52] channel and Ethernet and calling it hyperconverged in like 2005.
[404.34 → 404.66] No, no, no.
[404.70 → 405.14] That is not.
[405.22 → 405.42] No, no.
[405.48 → 405.78] That is.
[406.46 → 407.98] Well, this is an important distinction.
[408.30 → 409.82] That is merely converged.
[410.16 → 410.84] Ah, I see.
[410.96 → 411.54] That is actually.
[411.62 → 413.94] Well, I can see where my confusion would have emerged from.
[414.54 → 415.82] That is converged.
[415.82 → 423.20] That is that the converged was a kind of storage ism for converging these different
[423.20 → 423.94] storage protocols.
[424.38 → 429.30] And hyperconverged is the've always understood it to your understanding as well, where you've
[429.30 → 433.72] got compute and data at some level co-resident on the same infrastructure at some level.
[433.84 → 433.96] Yeah.
[433.96 → 434.40] Yeah.
[434.52 → 440.72] And I mean, it's so specific in some people's minds that they feel like a detractive property
[440.72 → 444.30] of hyperconverged is that it all comes in some sort of fixed ratio.
[444.50 → 450.78] And I don't know why the definition in their minds has become so specific, but it's even
[450.78 → 455.78] a term that I've shied away from when talking about oxide at all, just because it comes with
[455.78 → 456.68] so much hair on it.
[457.22 → 458.32] And it was an abbreviation.
[458.42 → 462.56] It's HCI, which is not human computer interface, which is what I always thought it was, but
[462.56 → 463.72] hyperconverged infrastructure.
[463.94 → 464.22] Yes.
[464.24 → 464.66] I'm sorry.
[464.96 → 467.74] I hate to be doing this, but it's true.
[467.74 → 471.24] Well, host controller interface with the USB spec.
[471.44 → 472.72] I mean, it's a distant dirt.
[473.42 → 475.96] Josh was already mad when he thought we were talking about fibre channel.
[476.08 → 477.10] Now imagine how it goes.
[477.64 → 479.20] I look fibre channel.
[479.46 → 487.80] It's, I mean, other than how ridiculously expensive a proprietary tree it is, like Mrs.
[487.86 → 488.78] Lincoln, I'm sure it's fine.
[488.78 → 493.48] Otherwise, I actually have complicated feelings on fibre channel because the, you know, we
[493.48 → 498.92] did a this, you know, I mean, I worked on the storage appliance and one of the protocols
[498.92 → 500.40] that we ended up offering was fibre channel.
[500.46 → 505.08] So I spent a bunch of time with FC, and I'm like, you know, I, I kind of like, like it
[505.08 → 505.82] in a strange way.
[505.84 → 508.34] It feels like, you know, Josh, you might actually like fibre channel.
[508.66 → 509.12] Have you gone?
[510.14 → 510.88] Do you know why?
[510.92 → 514.02] It's kind of that kind of that, that, that antiquarian sense to it.
[514.02 → 515.80] It's kind of, it's fine.
[515.80 → 516.66] Kind of steampunk.
[517.06 → 517.90] We have a lot of it.
[517.90 → 518.34] It's steampunk.
[518.52 → 520.04] It is definitely steampunk.
[520.50 → 522.58] But also I didn't want to suffer at its hands.
[522.70 → 523.32] That's a that's awesome.
[523.54 → 525.12] We were like, I mean, right.
[525.60 → 530.74] I, I do believe in my heart of hearts that EMC could have used any protocol to create the
[530.74 → 532.24] nightmare cathedral that they sold us.
[532.28 → 534.28] So like challenge accepted.
[534.42 → 534.76] That's right.
[534.78 → 535.02] Yeah.
[535.12 → 537.06] Like, you know, yeah.
[537.60 → 537.76] All right.
[537.76 → 539.24] So to get to it, in terms of oxide.
[539.24 → 544.00] So we do, so when we start out four years ago, we know we're going to have storage
[544.00 → 547.54] as we, we, I mean, early, early on, this is where we're, you know,
[547.54 → 550.88] students of all the other efforts in this domain.
[550.88 → 556.22] And one of the dimensions of failure was relying on third-party storage.
[556.22 → 562.66] So building compute, that would be then entirely dependent on third-party storage, because that's
[562.66 → 568.38] just a one that is a never ending quest to deliver a reliable system across two different
[568.38 → 569.10] vendors effectively.
[569.10 → 572.06] Um, and you just can't own your own fate.
[572.32 → 574.72] Because Adam, I don't know if we even seriously, we didn't seriously contemplate.
[574.78 → 575.46] I don't think we seriously.
[575.72 → 576.68] I don't, I don't think so.
[576.72 → 581.36] But in, in part, because it's not just sort of, uh, or, or maybe some of this experience
[581.36 → 584.72] came from Delphi where I worked for a bunch of years.
[585.06 → 589.46] We were, um, we dealt with lots of what, what we called externalities.
[589.46 → 594.58] So we built this software virtual appliance that plugged into any storage you happen to
[594.58 → 594.84] find.
[595.18 → 602.76] And Geez, like, man, we found like every vendor storage problem got bubbled up to us.
[602.84 → 603.10] Okay.
[603.20 → 605.10] So we were always guilty until proven innocent.
[605.40 → 608.72] I got to ask you at that time, when you kind of first come, because, you know, you and I
[608.72 → 613.98] have developed our own storage product, and we've absolutely suffered with all the ways
[613.98 → 615.66] that you suffer when you do all the storage product.
[615.84 → 617.70] Then you go to Delphi, we're like, Hey, good news.
[617.70 → 618.76] We're not developing storage product.
[618.96 → 619.12] Yeah.
[620.62 → 622.20] I want to get out of hardware.
[622.32 → 624.16] Like, please get me away from this baloney.
[624.38 → 624.56] Right.
[624.96 → 625.14] Right.
[625.26 → 626.52] And now you realize like, no, wait a minute.
[626.60 → 627.88] I haven't gotten away from the problems.
[628.18 → 630.84] I've, I've merely exported them to hostile actors.
[631.26 → 631.80] That's right.
[632.16 → 632.48] That's right.
[632.48 → 634.94] It's just everybody else's problem has become our problem.
[634.94 → 639.42] And then, you know, for example, we saw some ZFS checksum errors when people were doing
[639.42 → 641.22] an EMC storage array upgrade.
[642.34 → 642.78] Impossible.
[643.24 → 643.68] Possible.
[643.82 → 645.56] All of our Windows machines stayed up.
[645.84 → 647.10] Only you were complaining.
[647.10 → 649.34] It's like, well, we're the only ones who had checksums.
[649.48 → 649.88] Keepers.
[650.32 → 652.22] So, well, could you, if you consider turning those off?
[652.42 → 655.00] Because I feel like that would have helped.
[655.38 → 655.96] Then you'd be fine.
[656.74 → 661.16] I mean, that must be wild though, to see checksums on some, a piece of storage that people paid
[661.16 → 661.80] a lot of money for.
[661.94 → 664.84] That must've been like, on this one.
[665.56 → 666.74] Yeah, it was.
[666.96 → 667.26] Yeah.
[667.38 → 673.38] I mean, and then the fact that, you know, as you might imagine the but the vendor and
[673.38 → 676.90] the customer were unwilling to accept any evidence to the contrary.
[677.82 → 678.64] Yeah, definitely.
[678.80 → 680.24] Like, let me give you my evidence to the contrary.
[680.34 → 681.88] I paid way too much money for that.
[682.00 → 682.40] That's right.
[682.40 → 683.16] Check some errors, pal.
[683.36 → 686.04] So why don't you go reconsider whether I saw some checksum errors?
[686.04 → 694.46] There is a very, like a big, like, what's the thing where you fall in love with your captors?
[695.52 → 696.26] Stockholm syndrome.
[696.46 → 696.54] Yeah.
[696.54 → 704.84] So it's like combination, combination Stockholm syndrome and like good money after bad fallacy
[704.84 → 705.74] sort of.
[706.10 → 706.22] Yeah.
[706.62 → 707.26] Yeah.
[707.62 → 708.10] Yeah.
[708.10 → 712.70] And then, you know, all the other ways that people are, are secured into their infrastructure.
[712.80 → 712.94] Sorry.
[713.12 → 718.40] So you, you'd had that experience of having the now you're debugging every vendor's problem
[718.40 → 718.78] effectively.
[718.88 → 719.08] Yeah.
[719.12 → 719.30] Yeah.
[719.30 → 719.48] Yeah.
[719.48 → 719.76] Exactly.
[720.42 → 725.92] And as you say, I don't think we really thought that, you know, oh, maybe we'd plug into somebody
[725.92 → 727.02] else's storage or something.
[727.02 → 732.80] I think as we envisioned this thing as, you know, private cloud, one throat to choke kind
[732.80 → 738.36] of kind of product, it wasn't, nobody thought it would make sense for us to integrate with
[738.36 → 742.96] other people's storage products or, you know, drive APIs at other people's storage.
[743.04 → 743.82] It just made no sense.
[743.92 → 746.74] So we knew that we had to have storage in the box.
[747.52 → 749.88] And then there were a bunch of other constraints.
[750.72 → 756.76] One of the most, like, I mean, some very hard constraints were we needed it to be reliable.
[756.76 → 762.88] And I think having built some storage products, we had a good reverence for what it took to
[762.88 → 764.26] be, to make reliable storage.
[764.62 → 770.52] You know, we started at Sun, we started working on ZFS, I think in earnest, Brian, in like
[770.52 → 771.06] 2001.
[771.54 → 772.46] Yes, that's right.
[773.18 → 778.70] And then we shipped it, you know, in, I think 2005 as part of like the first update to Polaris
[778.70 → 778.94] 10.
[779.36 → 779.80] Right.
[779.80 → 786.50] And then we shipped it, you know, again, arguably as part of the ZFS storage appliance in 2008.
[786.76 → 792.98] I think those felt like starting lines, but I think that was the time in my career.
[793.10 → 795.64] I realized that, or pardon me, those felt like finish lines.
[795.72 → 798.36] That was the time in my career that I realized those were actually starting lines because
[798.36 → 803.10] as we roll, as you know, we had shipped this thing, it was in customers' hands.
[803.34 → 806.52] This was in 2006 when we started the Fish works group building that appliance.
[807.28 → 810.82] And yet we were tripping over all this kind of stuff just in development.
[811.00 → 815.48] Then when we shipped the thing, we found our customers very helpfully helped us find all
[815.48 → 816.42] these other kinds of problems.
[816.76 → 819.74] So which is not to say that ZFS is unreliable or less reliable.
[819.86 → 824.32] I mean, we saw, I saw this later on in, in these even, you know, longer tenure products,
[824.32 → 826.22] but it's hard to build reliable storage.
[826.72 → 832.08] It's very hard to build reliable storage because it's not merely about getting the, the, the
[832.08 → 837.24] block back that you stored, although it is certainly that, um, and that is very much
[837.24 → 837.70] a constraint.
[837.70 → 840.34] It's about getting it back in a timely manner.
[840.34 → 844.86] Because I think one of the I mean, the problems that we had with ZFS actually, I mean, in a
[844.86 → 851.94] real tribute to, to Jeff and Matt and the original ZFS team is the, the ZFS, we did not
[851.94 → 855.06] really, we did not see data corruption.
[855.06 → 862.98] We saw some very long data vacations and preventing data vacations is really, really, really hard.
[863.18 → 865.34] Um, friend data loss is obviously a constraint.
[865.34 → 874.28] So, and it, and you just realized like how much damage a single bad disc can do to a broader
[874.28 → 879.70] system in terms of, of a latency, not, not in terms of, of reliability.
[879.70 → 882.44] Um, so it's, it's really hard.
[882.52 → 886.52] And then the, the, the thing that I felt like I, Josh, you and I learned very viscerally
[886.52 → 894.22] together at, um, at Joint where we use ZFS in production, and we did not, there's a little
[894.22 → 896.92] bit of an asterisk on data corruption in ZFS.
[897.06 → 901.80] ZFS did not ever induce data corruption, but we did actually have a very, very, very bad
[901.80 → 907.90] OS bug that, um, we, uh, effectively pushed the system into a new dimension and hit some
[907.90 → 913.18] old behaviour, a hidden old bug, and it would cause rampant data corruption in the system.
[913.34 → 917.46] And if you cause rampant data corruption in the system, like you can actually corrupt
[917.46 → 919.20] metadata on its way out.
[919.28 → 919.94] That's already been checked.
[920.28 → 924.04] Critically in, in the, the memory, but the RAM of the system.
[924.36 → 924.72] Yeah.
[925.26 → 928.90] And where we just happened to be storing some data that was on its way to the disc, for
[928.90 → 929.28] instance.
[930.30 → 931.20] And that was very bad.
[931.54 → 932.52] And that was not right on the device.
[932.82 → 936.56] Um, and so you really don't want to have like, so basically world war two stressful rampant
[936.56 → 939.22] data corruption back is what I'm trying to, right.
[939.32 → 940.34] These are your life lessons.
[940.56 → 946.72] So when we, when we, um, you know, Josh and I started kicking around ideas for what storage
[946.72 → 951.14] would look like at oxide doing as little as possible was an important constraint.
[951.14 → 956.94] I think at the time, you know, I joined, um, having done some research around ZNS, you
[956.94 → 962.04] know, this is what has now become flexible, flexible data placement, but ZNS, uh, zoned, uh,
[962.04 → 963.64] namespaces on SSDs.
[964.36 → 969.54] Um, and started thinking about like, what are all the totally crazy things that we could
[969.54 → 970.80] go do from a clean sheet of paper?
[970.80 → 977.24] You know, at that point we had almost 20 years of experience from ZFS and great system, but,
[977.34 → 981.34] but really fundamentally a system that was built for spinning media.
[981.48 → 989.24] Like it was, it had a very different design basis than, uh, than what we have now than
[989.24 → 990.70] the state of the state of the world now.
[991.26 → 995.06] And I'd spent a lot of times with Matt Aaron's batting around ideas for what a next generation
[995.06 → 995.46] would look like.
[995.46 → 1000.36] So briefly fell in love with what a next generation could look like with all the whizzes new
[1000.36 → 1001.42] SSD technologies.
[1001.80 → 1006.96] But then with time constraints and knowing how long it takes to make one of these things,
[1007.16 → 1012.40] make, make a storage service actually reliable and perform well and not go on long vacations.
[1012.76 → 1016.62] We started to figure out what the simplest form we could take.
[1016.62 → 1016.98] Right.
[1018.48 → 1023.66] And we, I think also people might be a bit surprised as I guess they were with RFD26 and our Helios
[1023.66 → 1024.92] discussion a couple of weeks ago.
[1025.54 → 1027.06] ZFS was not necessarily a foregone conclusion.
[1027.26 → 1031.94] It was something that we all had a lot of experience with, but we also wanted to make
[1031.94 → 1034.14] sure we were really surveying things.
[1034.70 → 1040.12] So, um, the RFD60, which we've just put, put out there today, made public, um, folks can
[1040.12 → 1042.14] go look at some of the things that, that you looked at.
[1042.14 → 1046.92] Um, but we did, I mean, we, you know, very seriously considered things like Ref.
[1047.02 → 1052.46] Um, and, um, Adam, I remember you and I had some discussions with people who had deployed
[1052.46 → 1052.98] Ref.
[1053.36 → 1053.56] Yeah.
[1053.60 → 1058.24] Um, and they were revealing, I mean, because I mean, it, it, again, not to, not to fall into
[1058.24 → 1060.90] the kind of what I'm convincing, what I'm accusing Nate Silver of.
[1060.96 → 1061.46] I don't want to be too good.
[1061.46 → 1068.40] Practically, but I think that it was very clear that Ref needed, I mean, the most charitable
[1068.40 → 1072.58] thing you could say about Ref is that it very much requires operators.
[1072.94 → 1073.34] Yeah.
[1073.42 → 1074.22] It needs a staff.
[1074.46 → 1079.98] That's the of people who are not just like using it, but, but, but actively caring for
[1079.98 → 1084.44] it and feeding it and watering it like every day, checking to make sure that the print queues
[1084.44 → 1089.06] are not clogged up or whatever it is, you know, like you need people doing the busy work basically
[1089.06 → 1090.26] to, to keep it going.
[1091.54 → 1095.20] And it sounds like Brian, we had the same recollection of that, of like that conversation,
[1095.20 → 1101.82] which we're, uh, with some operators of Ref who were very, uh, you give a lot of praise
[1101.82 → 1102.48] to Ref.
[1102.78 → 1103.04] Yes.
[1103.04 → 1103.86] Very pros.
[1103.86 → 1104.44] For me.
[1104.90 → 1105.20] Totally.
[1105.32 → 1110.54] The kiss of death was them saying, but you know, that Ref is operated, not shipped.
[1110.94 → 1115.16] And I've since found, I've since found some people who kind of have pushed back on that
[1115.16 → 1118.90] notion, but I found at the time that very compelling.
[1119.06 → 1123.00] That this is a system that requires care and feeding, and it's great.
[1123.74 → 1128.84] And, uh, we needed something that was going to be, uh, autonomous.
[1130.32 → 1133.82] And that's been one of our core load stars, right?
[1133.86 → 1137.64] For the whole, for everything that we've designed in the product, I feel like it's like, how
[1137.64 → 1144.80] can we make this, uh, truly automatic so that it does not require a person to go log into
[1144.80 → 1149.74] a Unix shell and like kill a stuck process or delete some files or move some logs around
[1149.74 → 1150.06] or whatever.
[1150.06 → 1151.04] Like it should just work.
[1151.94 → 1153.40] Uh, yeah.
[1153.44 → 1156.68] And I think, you know, Ref has been on an interesting journey, and they did an entire
[1156.68 → 1162.50] rewrite, um, which actually paradoxically, um, kind of drained confidence I might have
[1162.50 → 1166.74] in it just because they had been kind of so confidently asserting their previous data store
[1166.74 → 1169.42] that they were then like, actually ignore what we said about the previous data store.
[1169.42 → 1170.64] Now we've got one that works.
[1170.84 → 1171.08] It's like, okay.
[1171.12 → 1174.04] This is the blue, the thing we did, we wrote the paper on.
[1174.28 → 1174.52] Yeah.
[1174.52 → 1174.66] Yeah.
[1174.66 → 1174.82] Yeah.
[1175.06 → 1175.26] Yeah.
[1175.42 → 1175.54] Yeah.
[1175.54 → 1175.86] Yeah.
[1176.06 → 1176.62] Blue store.
[1176.84 → 1177.32] Blue store.
[1177.50 → 1177.58] Yeah.
[1177.58 → 1183.40] Um, and I mean, like, I think it's great that Ref is, you know, living its best life
[1183.40 → 1186.82] and I'm perfect for it, but it was, it just was not, it can be a fit for us.
[1186.86 → 1192.72] So, and then I think we, and you kind of gone through some other things and really had
[1192.72 → 1198.42] decided like, look, what we need to go do is build something that is as simple as possible
[1198.42 → 1200.90] as robustly as possible.
[1200.90 → 1206.78] Um, and that can deliver what we're trying to deliver, which is reliable elastic storage
[1206.78 → 1209.94] to the folks that are provisioning VMs on the rack.
[1210.48 → 1216.16] Um, so do you want to kind of, I know you and Josh were beginning the noodle on getting
[1216.16 → 1219.92] like specific about like, what would this architecture going to look like?
[1219.92 → 1226.12] Because I think it's like, this was in 2020, uh, the pandemic hit by actually Adam, did
[1226.12 → 1230.34] you in the RFD, we refer to an actual meeting that we have.
[1230.34 → 1231.30] We record all meetings.
[1232.20 → 1235.90] Is this the one with, with, uh, the, the disc vendor?
[1237.22 → 1238.96] Uh, no, no, no, no.
[1238.96 → 1244.20] This is one where we are effectively, it's a it's a determination for 60 where we're figuring
[1244.20 → 1247.20] out what our approach is and oh my God, the COVID haircuts.
[1248.88 → 1250.46] That would have been in June, right?
[1250.90 → 1251.08] Yeah.
[1251.12 → 1252.40] It's in June 2020.
[1252.40 → 1256.60] And it's like, kind of like, it's like in that era when we're all getting haircuts at
[1256.60 → 1259.62] home and no one had, had yet gotten perfect at it.
[1259.62 → 1260.60] You know what I mean?
[1261.38 → 1266.20] Um, I have, I have notes from that meeting, and they finished with the words good meeting
[1266.20 → 1267.12] with an escalation.
[1268.20 → 1269.02] It was a good meeting.
[1269.26 → 1270.24] Just to tie that off.
[1270.58 → 1271.62] Just, it was a good meeting.
[1271.80 → 1272.24] It was a good meeting.
[1272.32 → 1274.12] Actually, you know what, Josh, you've got nothing.
[1274.20 → 1275.28] Maybe you were growing your hair out.
[1275.38 → 1277.38] I have to say your hair looks great.
[1277.96 → 1279.82] In that meeting, Adam, see me after class.
[1279.82 → 1280.82] Fair.
[1282.58 → 1284.62] Um, but no, this is us.
[1284.68 → 1285.64] You can see me and everyone else.
[1285.72 → 1287.20] I've got very much the same.
[1287.60 → 1288.94] My, my, my bangs were missing.
[1289.18 → 1292.36] So we had, we, uh, we, we changed it up after that haircut.
[1292.62 → 1296.94] Um, but so what were some of the kind of the approaches that you were considering when
[1296.94 → 1298.08] we were originally?
[1298.08 → 1303.96] So I think, I think we ended up saying if ZFS is going to be part of this and as much
[1303.96 → 1308.22] as possible, like we want to lean on the things that ZFS is good at.
[1308.22 → 1314.60] And I think the as I recall, the, the, the, the two kind of major architectural things
[1314.60 → 1320.52] that we considered were, so do we have ZFS and then plug in some sort of distributed
[1320.52 → 1327.72] storage layer underneath this where, you know, a particular ZFS dataset could, could
[1327.72 → 1332.78] talk to multiple, you know, backing stores, virtual volumes that were remote.
[1333.66 → 1336.58] And Delphi at the time was also doing some work along these lines.
[1336.58 → 1338.12] So it felt like not outrageous.
[1338.56 → 1344.42] And then the other approach that we, that we considered was, um, what Josh had deemed
[1344.42 → 1345.42] a mix.
[1345.42 → 1349.26] And I think this is something Josh, that you had been thinking about at Joint for a while.
[1350.72 → 1351.94] Yes, that is true.
[1353.02 → 1353.28] I was.
[1354.50 → 1356.70] Do you remember?
[1358.04 → 1361.28] Towards the, towards the end, we were like, we could do EBS.
[1362.10 → 1365.56] Like, and you're like, no, go back to bed.
[1365.56 → 1371.94] There's no one, no one that we would give it to within the organization, which we find
[1371.94 → 1372.94] ourselves would enjoy that.
[1373.40 → 1373.42] So.
[1374.06 → 1377.78] And, and just to be clear, we did not have all we had at, at Joint.
[1377.78 → 1379.36] At the time it was local storage.
[1379.54 → 1379.66] Yeah.
[1379.66 → 1386.32] Which was a, um, a hyperconverged S3, if you will, a storage service that you could run
[1386.32 → 1386.90] and compute on.
[1387.62 → 1393.52] Um, and so that was, and then we had, um, effectively local of a fair, I hate the term
[1393.52 → 1396.72] ephemeral because it wasn't ephemeral at all, but we had local storage that was local to
[1396.72 → 1400.32] an instance that obviously performed very well, but we did not have an EBS in between.
[1400.32 → 1404.02] Um, and we knew that was going to be a huge undertaking and Josh.
[1404.14 → 1407.84] And so Josh, I know you've been thinking about it and that, that kind of that first approach,
[1407.84 → 1413.76] um, that you're describing where you have ZFS on a so you've got a local compute instance
[1413.76 → 1415.60] that is talking to a Z pool.
[1415.78 → 1419.34] That Z pool is then going out over the network underneath that effectively.
[1420.16 → 1422.90] Um, that's what we call, I think the Southern volume manager approach.
[1422.90 → 1423.62] That's right.
[1423.74 → 1424.14] That's right.
[1424.74 → 1424.96] You're right.
[1425.00 → 1431.20] As opposed to what, what then became the Northern MIX where we had ZFS on those distributed
[1431.20 → 1438.40] nodes, kind of managing each of the SSDs, carving those up into what we would later call extents.
[1439.00 → 1446.18] Um, but, uh, you know, within the datasets, but having this new layer that was running close
[1446.18 → 1452.40] to the, to the VM that was in multiplex in the IO across these, uh, these downstairs
[1452.40 → 1453.14] components.
[1453.26 → 1455.20] So, or, or these Southern components.
[1455.20 → 1459.24] And that later became upstairs and downstairs for, um, for North and South.
[1459.80 → 1460.12] Right.
[1460.30 → 1464.60] And the, you know, as we're kind of considering, these are like a major fork in the road.
[1464.68 → 1466.28] I mean, these are totally different architectures really.
[1466.98 → 1471.68] Um, and you know, one of the things that I, a big believer is like, what can you go prototype
[1471.68 → 1474.30] or implement to get some, to inform a decision?
[1474.30 → 1478.20] And Josh, I think it was about at this time, you're like, I need to seem to go simulate some
[1478.20 → 1478.76] of this stuff.
[1478.98 → 1479.34] Yeah.
[1479.34 → 1486.56] In June, Adam, Adam went to start looking at, uh, like just a nominal prototype of the
[1486.56 → 1490.92] the thing with, uh, like discs underneath ZFS.
[1491.78 → 1495.02] I think we started out with iSCSI, possibly in AWS.
[1495.22 → 1495.52] That's right.
[1495.52 → 1496.32] You did some tinkering.
[1496.32 → 1501.76] I have found a note here where like a bunch of your tinkering ended with like a one line
[1501.76 → 1503.74] comment that was like garbage with a period.
[1505.54 → 1506.62] That sounds about right.
[1506.80 → 1510.98] Which I think that reflects what I remember the, the, the feelings of the tone being.
[1511.14 → 1511.34] Yeah.
[1511.42 → 1516.88] I, I do think I went in with, with more optimism that, that this was going to sort of work out.
[1516.88 → 1517.48] Right.
[1517.72 → 1524.80] Um, but it, it was, I mean, as I said, like ZFS wasn't on its, you know, initially even
[1524.80 → 1527.00] designed for SSDs.
[1527.00 → 1532.04] So it certainly wasn't designed for different volumes that were remote and might be available
[1532.04 → 1533.72] and might not and so forth.
[1533.72 → 1538.20] So yeah, I think, I think garbage was a pretty terse and accurate summary.
[1538.52 → 1543.76] I think my skepticism originally with the idea came from like the partition, like network
[1543.76 → 1546.38] storage, like iSCSI, you end up with partitions, right?
[1546.38 → 1550.16] It's just not something you really get with like a local SCSI disk.
[1550.16 → 1555.30] It's either like working or it's electrically connected, and it's not working, and you can
[1555.30 → 1557.20] decide to like to retire it.
[1558.48 → 1563.18] Well, and this is a real danger at, you know, on the one hand, there's a power of the abstraction
[1563.18 → 1565.02] where it's like, oh, you think you're talking to a local desk.
[1565.08 → 1565.56] Oh, surprise.
[1565.68 → 1566.28] You're going over the network.
[1566.42 → 1570.44] But on the other hand, it's actually introducing a bunch of new failure modes there that
[1570.44 → 1571.74] you didn't actually have.
[1572.20 → 1576.00] And things can go out to lunch for two minutes and that's terrible.
[1576.00 → 1576.90] Like, you know.
[1578.54 → 1582.66] And this, you know, things of problems that, you know, NFS addressed one way or the other
[1582.66 → 1584.02] for better and for ill.
[1584.26 → 1589.04] But what we, we're really not looking for something that has NFS semantics or really,
[1589.18 → 1592.32] you do need something that's really got block semantics, not file semantics.
[1592.68 → 1596.34] Because what you're trying to support is a guest VM that's going to do, you know,
[1596.46 → 1598.74] its interface is the machine interface effectively.
[1598.86 → 1600.88] So it really does need a block layer.
[1600.88 → 1601.88] Right.
[1602.44 → 1611.38] And so alongside that, I worked on just a simulator for how I envisaged the like,
[1612.28 → 1614.72] storage format and the protocol would work.
[1615.26 → 1622.38] Or the other approach where we would, we would have simpler, non-redundant ZFS pools
[1622.38 → 1626.96] down on every, like, every SSD in the rack has its own file system, own ZFS pool and file
[1626.96 → 1627.58] system, basically.
[1627.76 → 1630.62] And there's no mirroring or RAID or anything.
[1631.14 → 1636.56] And then we would do essentially replication from, from, from up the top.
[1637.70 → 1643.06] You know, we would write blocks of data to some number of replicas, which I think around
[1643.06 → 1644.70] then we decided would be three replicas.
[1644.70 → 1645.10] Yeah.
[1645.30 → 1645.70] Yeah.
[1645.92 → 1650.16] That's an important point too, because we decided we weren't going to do anything, any
[1650.16 → 1653.06] crazy erasure coding or RAID or anything like that.
[1653.18 → 1655.74] We decided we were going to really keep it simple.
[1655.94 → 1656.36] Right.
[1656.46 → 1659.30] And, and not just mirror it once, but mirror it.
[1659.42 → 1665.98] So have three redundant copies of every block that, that customers store within the rack.
[1666.94 → 1671.52] Because we weren't trying to make the world's most efficient storage, the world's fastest
[1671.52 → 1672.92] storage, the world's anything most.
[1672.92 → 1675.24] It was meant to just be a good everyday driver.
[1675.92 → 1676.28] Right.
[1676.34 → 1680.60] And in particular, it was meant to be like reliable above all else.
[1680.68 → 1682.22] Had to be absolutely reliable.
[1682.22 → 1683.90] Like that had to be a constraint.
[1684.12 → 1688.38] Well, and a big part of, big part of three replicas was like, if you recall really early,
[1688.46 → 1693.42] like one of the first things we decided was that if we, if we did network storage and
[1693.42 → 1701.22] we did live migration, then software update could basically be like something that people
[1701.22 → 1706.22] don't notice because you can go on update and reboot each computer in sequence.
[1706.84 → 1712.78] And if you're, if you only needed two of three replicas to be online and responsive to take
[1712.78 → 1718.60] rights basically without a durability loss, then like three replicas was the way to go.
[1718.96 → 1719.10] So.
[1719.96 → 1723.00] Well, and this is actually an important point too, because especially people who have followed
[1723.00 → 1727.02] us from company to company be like, wait a minute, didn't you guys like write a blog
[1727.02 → 1730.12] entry explaining why network storage is a problem?
[1730.12 → 1730.66] And it's like, yes.
[1730.76 → 1731.12] Well, it is.
[1731.24 → 1731.98] It is a problem.
[1732.12 → 1736.82] We spent four years like screwing around trying to make it work, and it's going well, but like,
[1736.96 → 1738.36] Geez, a lot of work.
[1738.36 → 1738.80] Yeah.
[1738.80 → 1744.24] It's a lot of work, but a part of the reason we viewed it as a constraint on what we were
[1744.24 → 1749.06] delivering is exactly what you said, Josh, is that we knew we needed to do one of the
[1749.06 → 1753.80] pain points that we had had is the, the absence of live migration.
[1754.12 → 1759.02] And when you don't have live migration, you don't want to reboot a compute node because
[1759.02 → 1759.98] you can't migrate it.
[1759.98 → 1764.16] And you are therefore like that node, you want that node to sit.
[1764.38 → 1768.66] And there are, that just has a lot of perverse incentives, and it creates a lot of problems.
[1768.66 → 1770.24] So we didn't want to have any of those problems.
[1770.34 → 1774.60] We wanted to, we wanted to have live migration built into the product as a constraint on the
[1774.68 → 1775.36] on what we were doing.
[1775.36 → 1780.14] And that meant that you have to have network storage, um, as a first class operation and
[1780.14 → 1783.60] you can do other things too, but we, we really viewed that as a constraint.
[1784.82 → 1789.36] Uh, and so Josh, your simulator begins to yield some results in terms of indicating like,
[1789.36 → 1795.40] okay, maybe like this, this path of the Northern MOX is feeling viable.
[1796.34 → 1807.28] Um, yeah, I had made myself comfortable that, that, uh, like we could build a crash safe representation
[1807.28 → 1818.28] of a disc with a reasonable performance, like target in mind, uh, without it being like incredibly
[1818.28 → 1821.28] complicated, and we'd need to build a custom file system and a bunch of other stuff.
[1821.28 → 1830.46] Like the, um, I think the and the simulator stuff I did for like two months was a big part
[1830.46 → 1831.10] of that, right?
[1831.10 → 1838.46] Like, like the discovering, like what happens if you allow an overlapping right to the same
[1838.46 → 1839.36] disk address, right?
[1839.36 → 1844.16] To, to occur, to be issued like concurrently with an like, you know, like you're writing
[1844.16 → 1847.84] to LBA five and then before that finishes, you write to LBA five again.
[1848.88 → 1855.30] Uh, you know, and there's just like, there's a it's all about ordering constraints really,
[1855.30 → 1855.64] right?
[1855.64 → 1860.72] Like this operation and this operation, like this one has to happen after that one because
[1860.72 → 1861.44] it's replicated.
[1861.44 → 1864.86] You're doing that operation on three copies.
[1865.12 → 1870.16] And so that happens after relationship has to be the same on all three.
[1870.66 → 1871.14] Right.
[1871.34 → 1875.40] And so then there's just like an issue of like dependency ordering, threading through the
[1875.40 → 1880.40] protocol and, but you don't want to make everything totally ordered because then you can't do anything
[1880.40 → 1880.88] in parallel.
[1881.18 → 1886.74] So like safely splitting up what things can occur concurrently.
[1886.74 → 1893.60] How do we make sure that each replica ends up transitioning through the same series of
[1893.60 → 1899.48] visible states, even if they end up doing things in parallel and then making it crash
[1899.48 → 1899.72] safe.
[1899.88 → 1904.84] So if you, you know, get interrupted between or during any set of operations, and indeed,
[1904.94 → 1909.76] if you get interrupted during a different point on any replica that you can still come back
[1909.76 → 1913.42] up and figure out what it is that you've promised to give back to the guest.
[1913.42 → 1922.20] And disks have a pretty specific set of promises that they make around write back caching and
[1922.20 → 1928.00] flushes and synchronization and what's considered durable and not durable with respect to asynchronous
[1928.00 → 1928.88] writes and so on.
[1929.58 → 1929.64] Right.
[1929.80 → 1935.68] So the simulator was about trying to square those promises that we had to make against how we
[1935.68 → 1937.70] might implement that on the backend with a protocol.
[1937.70 → 1943.22] Because you're essentially creating a distributed system with not many nodes, right?
[1943.34 → 1948.22] But like, like one of the simplifying assumptions, I think that we've held the whole time is that
[1948.22 → 1949.72] there is actually only one client.
[1950.46 → 1957.52] So there is no need for consensus or coordination on a block by block or request by request basis.
[1958.44 → 1962.60] And Josh, when did the nomenclature, and I think Matt pointed out in the chat, that the nomenclature
[1962.60 → 1969.16] at some point shifts from north to south, we shift from upstairs and downstairs, which I always have.
[1969.34 → 1976.30] I mean, I just get the image of an English manor in which madcap adventures happen downstairs.
[1976.54 → 1977.48] I'm not sure what's your intent or not.
[1977.48 → 1980.50] That is, that's definitely where it came from.
[1980.50 → 1988.68] I mean, the I swapped one, uh, one historically toxic, politically charged set of words for
[1988.68 → 1990.58] another, but on a different continent.
[1990.58 → 1992.10] The good news is we're not going to have a civil war.
[1992.32 → 1994.06] Um, instead we're going to have a class base.
[1994.46 → 1994.82] Right.
[1994.86 → 1996.04] It's merely about class.
[1996.30 → 1996.90] It's merely about class.
[1997.04 → 1997.42] No, no.
[1997.64 → 1998.26] That's great.
[1998.58 → 1999.42] Uh, good stuff.
[1999.58 → 2004.10] Uh, and then somewhere, so this is all kind of through 2020 and then in early, but it's
[2004.10 → 2006.52] like, it's clear that, okay, we've sketched out what we need to go do.
[2006.52 → 2010.84] So, but, and Josh, remember both you and Adam being like, by the way, I mean, we already
[2010.84 → 2016.48] have way too much to do, but like we need to add some people to go do this, pal.
[2016.64 → 2020.82] Like we cannot do, we, there, you know, we have joked that inside of Oxide, we've got
[2020.82 → 2026.16] nine different startups and this was definitely one of the startups, and it was rather understaffed.
[2026.58 → 2031.10] I have a date here, 2020, February 4th, 2020.
[2031.10 → 2036.50] So before the pandemic, we were in an all hands and Adam says the long pole will
[2036.50 → 2037.98] be storage, write it down.
[2039.20 → 2040.76] Like, and you did, and you wrote it down.
[2041.00 → 2041.62] I have it here.
[2044.14 → 2046.02] Accurate, I feel in hindsight.
[2046.42 → 2054.50] Uh, but we, we didn't start on Crucible until February 17th, I think, 2021.
[2055.06 → 2057.66] Well, and, and, which is a good segue to Alan.
[2057.74 → 2060.48] So Alan, you joined us, I think in April 2021.
[2060.66 → 2060.88] Is that what it is?
[2060.88 → 2061.16] May.
[2061.34 → 2061.80] What is that?
[2061.90 → 2062.12] May.
[2062.72 → 2062.96] Yeah.
[2062.96 → 2063.04] Yeah.
[2063.56 → 2067.96] And so Alan, you're coming, so describe your background a little bit and kind of how you're
[2067.96 → 2069.68] coming into Oxide in early 2021.
[2070.92 → 2076.58] Well, I, let's see, I had, I'd been at Sun for a while and I went to a storage startup,
[2076.78 → 2077.42] three-par data.
[2077.88 → 2081.94] I came back on, and then went to another storage startup, DSSD.
[2081.94 → 2087.48] Um, and I was, had left there and, and gone somewhere I wasn't really happy with and I
[2087.48 → 2090.86] wanted to, wanted to land somewhere working on big systems problems.
[2091.54 → 2097.02] And I was keeping an eye on Oxide, and finally I was like, I, I really want to work there.
[2098.02 → 2100.10] I want to see if I can get a job there.
[2100.70 → 2102.98] Um, but I'm sure that, I mean, there are so many storage guys there.
[2103.04 → 2105.40] There's no way they need any more storage people.
[2106.32 → 2109.46] I'm sure that work is like, they did that in the first 15 minutes.
[2109.46 → 2109.80] Oh yeah.
[2109.84 → 2110.04] Right.
[2110.16 → 2110.62] Yeah, exactly.
[2110.80 → 2111.30] In the back burner.
[2112.26 → 2112.58] Um,
[2113.06 → 2113.68] Little did you know.
[2114.06 → 2114.30] Yep.
[2114.70 → 2121.08] So then I, I show up and there wasn't much storage done yet, but there was lots of good
[2121.08 → 2121.44] ideas.
[2121.44 → 2125.64] And so Adam and Josh sat me down and said, okay, here's, here's what we were thinking.
[2125.90 → 2128.16] Here's the repository in which we've been phoning it in.
[2128.60 → 2129.82] Would you like to do the typing?
[2131.44 → 2136.98] That was sort of the beginning and, and yeah, we, we got to work and started writing code
[2136.98 → 2137.18] and.
[2138.12 → 2138.52] Yes.
[2138.52 → 2139.96] And so describe that kind of journey.
[2140.02 → 2144.54] So you are, you'd done, you had kind of come in with a background of, you've done a bunch
[2144.54 → 2145.08] of storage.
[2145.18 → 2152.20] You've been, um, at, at DSSD at sun, uh, but also been doing some rust at a at, at a startup
[2152.20 → 2152.92] if I recall correctly.
[2153.60 → 2154.06] A little bit.
[2154.10 → 2154.28] Yeah.
[2154.38 → 2155.48] Not, not a ton.
[2156.14 → 2161.44] Um, so you're coming into a, um, you know, some stuff that you, you, you've got a lot of
[2161.44 → 2166.04] experience in and getting, and understanding, um, getting ramped up on rust as well.
[2166.04 → 2169.76] Um, and so what was, what was kind of the first things you started experimenting with?
[2170.38 → 2177.00] I think it was, it was implementing the lowest part of what, what crucible is talking, talking
[2177.00 → 2177.86] to the files.
[2178.32 → 2184.64] You know, there are the extents where we actually put the data on and taking sort of Josh's and
[2184.64 → 2188.70] Adam's ideas and, and putting them into actually writing bits on disc.
[2188.70 → 2194.70] And what were, I'm trying to remember some of the early milestones when we were, I mean,
[2194.72 → 2199.96] there was so much work to be done, but when we, and I think I, you know, I, I, I pretty
[2199.96 → 2203.88] early on in there also, you're like, Hey, by the way, we, we definitely need to add, uh,
[2203.88 → 2205.22] I cannot do this by myself.
[2205.34 → 2207.12] I'm going to need additional folks.
[2207.50 → 2207.82] Yeah.
[2207.82 → 2212.22] Um, but what were some of the I mean, when did we come up with the name crucible?
[2212.38 → 2213.26] Actually, when was that?
[2213.66 → 2218.94] I thought, I thought, according to my, according to my notes, the day that I opened the repository
[2218.94 → 2224.38] and started typing the first, like 500 lines was when I decided to call it crucible.
[2225.04 → 2225.56] All right.
[2225.62 → 2227.98] Like that all happened in the space of about 30 minutes.
[2228.32 → 2228.44] So.
[2230.44 → 2231.02] All right.
[2231.10 → 2233.48] So we, so it was crucible when you, when you got here.
[2233.68 → 2234.24] Oh, I got here.
[2234.40 → 2234.90] Oh, on your side.
[2234.90 → 2235.08] Okay.
[2235.72 → 2242.08] Um, so, um, what, um, yeah, as you're, so you're proceeding with some of the, the kind
[2242.08 → 2243.40] of the earliest lowest layers.
[2243.72 → 2247.80] And I mean, you obviously are looking at kind of the thinking that had been done on this
[2247.80 → 2250.98] and kind of, is your thought these people are off the rocker or this?
[2251.64 → 2253.50] I was a little, little worried.
[2253.60 → 2258.30] There were a bit too many layers, but, um, I don't know.
[2258.30 → 2264.24] I was just so excited to be here and to start working on it and, and being able to use rust
[2264.24 → 2264.88] full-time.
[2265.06 → 2271.98] I mean, we've talked a little bit about how we'd like rust and I think that language
[2271.98 → 2275.32] enabled us to go so much faster than it would have been if we had done it in C.
[2275.60 → 2275.94] Yeah.
[2275.96 → 2276.66] That's fascinating.
[2276.78 → 2276.94] Yeah.
[2277.32 → 2282.76] Like no way would we have gotten as far as we did as quick as we did with, with any,
[2282.92 → 2284.28] certainly with C, but.
[2285.28 → 2289.36] In, and then, because I remember early on you being like, we definitely need more folks
[2289.36 → 2293.68] here and James, you joined us like a just a couple of months later in 2021, right?
[2294.96 → 2295.50] In July.
[2295.92 → 2296.62] Yeah, it was July.
[2296.76 → 2296.92] Yeah.
[2298.28 → 2304.02] Um, and I, I definitely, uh, remember in the, the conversations you were having at Oxide,
[2304.12 → 2306.80] you, you made two deadly mistakes.
[2307.28 → 2309.92] You indicated to Alan that you were interested in storage.
[2309.92 → 2314.66] Um, and then as I recall, you laughed at Alan's jokes, which is always the second, I mean,
[2314.74 → 2319.64] that Alan was, was smitten the second you, uh, the second his jokes were landing.
[2320.04 → 2323.70] Um, it was definitely, it was, it was, it was made meant to be.
[2323.82 → 2328.48] I remember the hiring huddle when we were talking about James, and I was like, I want James.
[2328.58 → 2329.78] I want James in storage.
[2331.26 → 2331.62] Oh.
[2332.32 → 2333.52] It was, it was that direct.
[2333.62 → 2337.42] I, then he also added like, also he laughed at my jokes, but the, uh, I think that James,
[2337.42 → 2338.24] it was after I.
[2338.24 → 2338.48] Right.
[2340.36 → 2342.82] Well, and he's from the Commonwealth, so I can't argue with that.
[2343.26 → 2343.62] Exactly.
[2343.86 → 2348.18] You're, you're fine with anyone who's from a constitutional monarchy, hire them.
[2348.76 → 2348.84] Right.
[2350.02 → 2356.00] And so James, you're coming aboard, and I'm not, you had, you had your, your fingers in a lot
[2356.00 → 2359.76] of parts of the system, but, but very, very much involved in Crucible.
[2360.26 → 2363.94] Um, what were some of the kind of your early memories of getting going with Crucible?
[2363.94 → 2371.82] It's funny that Alan started out, uh, at the lowest level, uh, in terms of Rust, you know,
[2371.82 → 2375.36] talking directly to the bits on, uh, I guess the downstairs at that point.
[2375.88 → 2379.56] I remember one of the first things I did is I, I came up to the top and I said, okay,
[2379.66 → 2383.44] I'd like to put a, uh, NBD crate in front of this.
[2383.50 → 2386.72] I want to treat this as an actual, like, disc.
[2386.78 → 2388.94] I remember the, uh, the demo that resulted from it.
[2388.94 → 2393.36] I said, I was very nervous, and I think I said, it's a disc like a hundred times in a row.
[2393.90 → 2398.60] Um, but I, I wanted to make that, you know, part of my development workflow.
[2398.60 → 2404.60] So starting with like, can I interact with this, you know, slash dev slash NBD zero, uh,
[2404.60 → 2405.02] for example.
[2405.02 → 2409.52] So getting it up and running like that was one of my, uh, one of my earliest memories, uh,
[2409.52 → 2410.16] in that case.
[2410.88 → 2415.26] Well, and so you mentioned the demo, because I remember those, those early demos of where
[2415.26 → 2419.54] you're actually getting this thing to do like re you're actually using it for like real
[2419.54 → 2420.32] stuff.
[2420.60 → 2427.50] And you were, uh, and there, there, nothing beats seeing a demo where people are actually
[2427.50 → 2430.04] like the stuff I've actually, we've been developing.
[2430.04 → 2433.54] I'm now actually putting to real use, um, was just outstanding.
[2433.54 → 2439.20] And I learned that you're, uh, because James has got a, um, oxide has several data centres,
[2439.20 → 2443.56] one of which in Canada, we're all named after pet food names.
[2443.56 → 2448.60] I believe are all your, we, we do believe in, in pets, not cattle for some, some machines.
[2448.78 → 2450.06] Um, good old fancy feast.
[2450.26 → 2457.32] I feel has served very honourably in the as the, uh, as my comedy partner, Greg likes
[2457.32 → 2460.94] to say, I'm one of the hyperscalers and I will take no further questions at this time.
[2461.56 → 2467.12] Uh, let me see if I could, I have a picture that actually took of this so I could drop it
[2467.12 → 2467.58] in the chat.
[2467.98 → 2468.58] Oh yeah.
[2469.68 → 2470.38] This is great.
[2470.38 → 2473.36] Because you're solving another problem for Adam, which is like,
[2473.56 → 2476.46] it's not, this is going to be my, my Northern mix diagram.
[2477.38 → 2481.84] I'll use this as the, uh, the background of the like the, the final thing.
[2482.12 → 2482.66] Uh, yeah.
[2482.68 → 2485.68] So this is, uh, affectionately called the Canada region.
[2485.98 → 2492.50] It's composed of four machines that I, uh, it's like the here's your rack bro kind of
[2492.50 → 2492.88] thing.
[2492.88 → 2498.34] It's, it's, it's all desktop hardware, but, uh, it emulates as, as faithfully as I can make
[2498.34 → 2500.72] it, uh, the oxide system.
[2500.72 → 2503.78] So you've got the four machines named after dog food there.
[2503.94 → 2510.26] That would be a dinner bone and fancy feast is the control machine at the top.
[2510.58 → 2519.00] Uh, and yeah, I, I regularly bring up and tear down all the, uh, required stuff just in the
[2519.00 → 2520.12] in the furnace room over there.
[2521.42 → 2523.58] I didn't actually present it on the thing.
[2523.68 → 2523.82] Yeah.
[2524.56 → 2524.96] There are you.
[2525.02 → 2526.24] I've never actually seen a photo of it.
[2526.78 → 2529.04] It looks so much more professional than it was.
[2529.24 → 2530.32] Not, not the take anything.
[2530.74 → 2531.56] I'm a little disappointed.
[2531.66 → 2532.48] Are you disappointed, Alan?
[2532.60 → 2533.22] You're disappointed.
[2533.36 → 2533.48] Yeah.
[2533.54 → 2533.84] Hold on.
[2533.92 → 2534.70] I'll post the back.
[2534.80 → 2535.46] I'll post the back.
[2535.56 → 2537.40] It's not, it's no longer professional when I post the back.
[2537.46 → 2538.32] There's no cable management.
[2538.80 → 2540.00] It's just everywhere.
[2540.96 → 2541.16] Yes.
[2541.20 → 2541.54] There's some.
[2541.62 → 2543.54] I mean, I thought it was literally in his bathtub.
[2543.68 → 2544.46] So I'm very impressed.
[2544.46 → 2544.82] Yeah.
[2544.94 → 2545.26] Yeah.
[2545.34 → 2546.92] I, I, that's what was my understanding too.
[2547.00 → 2551.50] I'm just, I am very, uh, I mean, and I can't get the image to go there.
[2551.58 → 2551.70] Okay.
[2551.70 → 2554.24] The back that's better, better.
[2554.50 → 2557.40] I feel, I feel, can Alan step in the right direction on that one.
[2557.58 → 2558.34] We're moving there.
[2558.34 → 2562.00] We need a little, I need to see a little more James, but yeah, this is better.
[2562.30 → 2562.40] Yeah.
[2562.48 → 2567.56] I, I, I needed, uh, you know, something like obviously Canadian, like a, you know, a, a,
[2567.56 → 2571.78] a flagrant foul after a, um, an empty net goal or something.
[2571.82 → 2572.04] I don't know.
[2572.06 → 2574.12] I need, I need something else in here, but this is good.
[2574.12 → 2576.56] This is the this is, we're moving in the right direction.
[2576.94 → 2584.04] Um, so, but, and James, you were, um, because I also know that you were able to, that, that
[2584.04 → 2588.92] kind of approach of coming from the, from the top down led you to develop some pretty
[2588.92 → 2590.86] important functionality pretty early on.
[2590.92 → 2594.38] I remember like the, the snapshot that when you're developing snapshots.
[2594.54 → 2599.58] Well, and James also, James was the first one, I think to actually boot on a crucible.
[2599.58 → 2605.34] Like I, I was testing it, but I didn't actually have it connected to a VM and James was the
[2605.34 → 2608.26] first one to actually boot a system on crucible.
[2608.90 → 2609.10] Wow.
[2609.40 → 2611.18] That was, I mean, it was exciting.
[2611.28 → 2612.08] See, when was that?
[2612.14 → 2614.50] I mean, this is where time really blurs together.
[2614.86 → 2615.12] Yeah.
[2615.12 → 2618.54] I mean, it wasn't either long after he arrived.
[2619.72 → 2625.96] Um, and so we, I mean, Alan, obviously a huge shot in the arm to get someone who you're,
[2626.00 → 2629.96] I mean, I think it's so important to be collaborating tightly with someone.
[2629.96 → 2634.48] And I mean, I don't know, I, did you find that it was, I mean, obviously it makes you
[2634.48 → 2635.96] go more than twice as fast.
[2635.96 → 2639.78] I feel when you've got someone who you can like, who, who cares about the problems that
[2639.78 → 2643.48] you've just solved or the really, I mean, obviously we're all in this together, but it's really
[2643.48 → 2647.32] helpful to have someone who's just can work through all the same problems.
[2647.54 → 2647.68] Yeah.
[2647.72 → 2652.38] And someone else, let me, Josh and Adam both had six other day jobs they were doing.
[2652.38 → 2654.42] So they were like, yeah, Alan, that looks good.
[2654.48 → 2654.76] Whatever.
[2654.76 → 2659.88] And, and when James was there, it was like somebody, we can read each other's code.
[2659.96 → 2663.98] We can like, there's more, you know, we're much, we were much tighter collaborators there
[2663.98 → 2664.34] and that.
[2664.92 → 2668.80] And then, and so when, and then that, that might lead, that kind of leads us into RFD
[2668.80 → 2672.88] one 77, which is the RFD that, that you write, which we also made public.
[2673.66 → 2679.12] Um, and that begins to get us into like, what does this implementation actually look like?
[2679.12 → 2683.08] And some of the actual implementation decisions that, that we made there.
[2683.48 → 2683.88] Details.
[2683.98 → 2684.14] Yeah.
[2684.14 → 2684.22] Yeah.
[2684.24 → 2684.48] Yeah.
[2684.48 → 2685.02] The details.
[2685.38 → 2689.28] Um, and I mean, as you were kind of getting into the details, what were some of the kind
[2689.28 → 2694.12] of the big important details or some of the, the, the important decision points in there?
[2695.08 → 2701.96] Well, I mean, I don't know if there's any, anything new, the importance about keep it simple.
[2702.24 → 2704.92] Don't, don't get crazy and make it work.
[2706.66 → 2711.04] And then of course, for everything you're doing and every time you're doing anything at any
[2711.04 → 2713.62] moment, you could lose power and you have to come back.
[2713.62 → 2715.34] Now, I mean, that's always with storage.
[2715.34 → 2719.96] You always get into those, like the fast path when everything is working is kind of the
[2719.96 → 2720.52] easy part.
[2720.62 → 2723.14] It's all the damn errors, and it's all the yeah.
[2723.44 → 2727.54] Every, when this doesn't, this message doesn't come back, and then you lose power and then you
[2727.54 → 2729.18] come back up, but that one's not there.
[2729.18 → 2732.58] And it's like, it just explodes into complexity.
[2732.58 → 2737.66] And so working through all those of like a lot of this stuff we didn't see until we sort
[2737.66 → 2739.10] of stuck our foot into it.
[2739.22 → 2740.30] And then you're not, you know.
[2740.92 → 2745.14] And so how did, I mean, you had the challenge that we all had of trying to develop this before
[2745.14 → 2745.74] we had a rack.
[2745.82 → 2747.60] So you're developing on a kind of commodity hardware.
[2747.88 → 2748.16] Yeah.
[2748.16 → 2752.54] Um, but then you're also trying to develop, to, to test many aspects of the system that
[2752.54 → 2753.40] are hard to test.
[2753.48 → 2756.28] So how did, what was your approach to testing on all this?
[2756.28 → 2762.86] Well, again, Rust, uh, makes it really easy to write this sort of unit tests that you
[2762.86 → 2767.90] can do, and you can, I mean, it's, it's, it's kind of basic programming where you just kind
[2767.90 → 2774.12] of break it down into smaller, smaller pieces and then test each little sub piece on its own
[2774.12 → 2777.98] and then build back, build back the more complicated system.
[2777.98 → 2783.66] Once you're like, okay, I, I know for sure this piece of it is, is solid and, you know.
[2783.66 → 2790.12] Um, and then be, and being able then to have kind of a robust testing also allows you to
[2790.12 → 2791.54] buy it to, to move the implementation.
[2791.72 → 2794.56] It's sort of like when I need to go make a change to the implementation, you get some
[2794.56 → 2795.10] confidence.
[2795.38 → 2795.74] Yes.
[2795.82 → 2796.08] Yeah.
[2796.28 → 2801.52] And then that's something again with, with C, like you never really know, like you hope
[2801.52 → 2808.44] you pray with, with Rust, I have a lot more confidence that I changed it.
[2808.58 → 2813.36] I mean, when you get to come, when it compiles, you're like pretty close.
[2813.66 → 2815.92] So I've got to work out the logic bugs, but like.
[2816.52 → 2822.60] It is amazing how, I mean, I think that this is where I do feel that Rust really separates
[2822.60 → 2827.82] itself from certainly everything that I've used where that compilation, just getting it
[2827.82 → 2832.40] a big refactor to compile, you know a lot about where you are.
[2832.88 → 2840.88] And I mean, so actually kind of knowing that, that, that, that ability to, for refactoring
[2840.88 → 2843.90] in the future, does that kind of guide you in the present of like, look, I know that
[2843.90 → 2849.06] like I can make decisions that are revisitable, are more readily revisitable than they may
[2849.06 → 2850.42] be in a C-based system.
[2850.42 → 2856.82] Or if we need to read or to optimize this later or what have you, like I, I, I can, I can
[2856.82 → 2859.16] afford to like to get the implementation right now.
[2859.16 → 2862.32] And then know that if we need to like to improve the abstractions from a performance perspective,
[2862.32 → 2863.04] we can do that later.
[2863.10 → 2864.16] Did that kind of guide you at all?
[2864.16 → 2865.36] Yeah, no, for sure.
[2865.52 → 2870.52] Because I, I, I knew there were things that we were doing that were slow and, and I was
[2870.52 → 2874.58] like, but I want to make sure it works, and I want to build it, build the whole thing,
[2874.68 → 2877.96] build the whole stack, and then we can start iterating the different pieces.
[2877.96 → 2883.12] But yeah, certainly knowing that we can come back and, and update it later, give you the
[2883.12 → 2887.02] freedom to just like to get the basic stuff working.
[2887.46 → 2891.98] And then how did, I mean, you've obviously got a bunch of different failure modes that you've
[2891.98 → 2893.46] got to be able to, to test.
[2893.46 → 2896.04] You've got to be able to, I mean, disks coming and going and so on.
[2896.10 → 2898.22] How did you, how do you simulate that?
[2898.30 → 2899.14] How did you test that?
[2900.76 → 2908.22] I, let's see, for me personally, I, we built some tools that, that help us that will like
[2908.22 → 2912.40] do this sort of simulation where we all on one system, we can have an upstairs and three
[2912.40 → 2916.02] downstairs, all in different processes running and talking to each other.
[2916.02 → 2921.28] And then we built like a control system that will shut down different, different parts
[2921.28 → 2924.62] of the downstairs and let it recover and see what happens.
[2924.62 → 2927.16] And so it gives us a lot of, a lot of control.
[2927.16 → 2934.00] And then we built a, a sort of fake front end where you can basically sit there as the
[2934.00 → 2936.96] upstairs and say, okay, now issue a right to this address.
[2936.96 → 2939.66] And then now read this address.
[2939.66 → 2944.90] And so you can like step your way through very specific sequences that allows us to replay
[2944.90 → 2949.02] things and to test a very specific, you know, okay, I'm going to take this one downstairs
[2949.02 → 2950.90] out, and I'm going to send a right.
[2951.18 → 2952.58] Then I'm going to turn everybody off.
[2952.98 → 2954.90] Then I'm going to turn them all back on and see what happens.
[2955.10 → 2957.24] And like do all sorts of things like that.
[2957.24 → 2961.78] And then we, and then you're able to do that in a way that it's effectively automated such
[2961.78 → 2967.98] that when, when we go to improve the system, we can kind of check that as a, as a regret.
[2967.98 → 2972.92] Did we regress this particular condition of what, where things are kind of transiently
[2972.92 → 2978.84] coming and going, which I, I mean, so important when, when you're endeavouring to do something
[2978.84 → 2984.02] like this, that you really need to, to have, and, and folks in the chat are asking, well,
[2984.02 → 2988.62] did you use, you know, prop testing, did you, formal proofs, I would say not quite formal
[2988.62 → 2989.26] proofs.
[2989.54 → 2995.40] But we, everything else is kind of in scope and we, we take kind of different approaches
[2995.40 → 2996.56] for different parts of the system.
[2997.48 → 2999.24] And we can definitely talk about TO plus.
[2999.42 → 3000.12] Someone was asking the chat.
[3000.44 → 3002.22] James, did you want to talk a bit about testing?
[3003.88 → 3004.24] Yeah.
[3004.24 → 3007.16] Somebody had said anything beyond unit tests.
[3007.28 → 3012.30] We, Alan talked a bit about the, the testing tools, which I believe have the some of the
[3012.30 → 3013.66] best names at Oxide.
[3014.54 → 3019.58] We've got CRUD, which is the crucible DD that was written to test, you know, just basic
[3019.58 → 3020.16] stuff like that.
[3020.24 → 3026.34] We've got a couple of fun names there, but just to sort of back it up a bit.
[3026.34 → 3030.98] I think it took like five minutes of, of starting to work on the storage system.
[3030.98 → 3035.66] And, and you sort of, you understand like the mission is this has to work.
[3035.66 → 3037.40] Like it has to be bulletproof.
[3037.50 → 3039.18] You can't lose customer data, stuff like that.
[3039.18 → 3044.06] So we've taken quite a lot of effort throughout the year, two years, three years I've been
[3044.06 → 3047.86] here in order to write these, you know, extensive tests.
[3047.92 → 3051.66] So we've got the, the, the tools that Alan was talking about.
[3052.04 → 3058.80] We have these, this full integration test suite where we, we have Tokyo tests that boot the
[3058.80 → 3061.58] downstairs and the upstairs and run various scenarios.
[3061.58 → 3067.98] Uh, we have the, uh, that also can boot, uh, different, uh, tools like our pantry service
[3067.98 → 3069.48] that, uh, we also boot there.
[3069.48 → 3074.80] Uh, we have the my, my favourite one of these dummy downstairs tests.
[3074.96 → 3077.92] Uh, I find that that can, uh, tease out a lot of issues.
[3077.92 → 3083.12] We have a we boot a real upstairs, but we talk to fake downstairs, and we can control,
[3083.32 → 3088.80] for example, like this downstairs receives a message and then goes away while the other
[3088.80 → 3091.20] ones receive and, and answer their messages.
[3091.20 → 3092.98] Then it gets kicked out.
[3093.10 → 3094.48] For example, it comes back.
[3094.54 → 3099.52] We make sure that the upstairs is either replaying or, or reconciling and repairing.
[3099.52 → 3105.72] Uh, you can have very, very fine-grained, uh, downstairs behaviour based testing in that
[3105.72 → 3106.02] case.
[3106.02 → 3109.26] And this is all done, uh, through the, uh, through the API.
[3109.26 → 3114.96] Uh, so yeah, I, you know, lines of code are a terrible measure for, for this kind of thing,
[3114.96 → 3119.80] but I think we've got quite, quite a few, almost, I think, parody of lines of code to
[3119.80 → 3120.92] lines of test code.
[3121.10 → 3125.30] And I know that, you know, that's, that's what it is, but, um, yeah.
[3125.46 → 3127.92] We're all measured in, you know, our progress reviews.
[3128.40 → 3128.72] Yes.
[3128.98 → 3130.58] By lines of code we do per week.
[3130.68 → 3131.62] Yeah, that's exactly right.
[3131.66 → 3133.28] I have found that that creates no perversions.
[3133.44 → 3136.18] And I really just like to stack rank the organization by lines of code per week.
[3136.28 → 3136.60] I found that.
[3136.60 → 3136.78] Exactly.
[3137.20 → 3137.32] Yeah.
[3137.36 → 3137.56] Yeah.
[3137.64 → 3140.54] Very early on, I understood that I had to game the system like this.
[3140.54 → 3144.34] So every PR has, you know, 12,000 lines of testing code, you know?
[3144.54 → 3144.94] Yeah.
[3145.34 → 3147.84] The most important measure of a software system is its mass.
[3148.48 → 3149.36] That's exactly right.
[3149.46 → 3150.88] That's what we have written up on the wall here.
[3151.46 → 3158.22] Um, in this testing, the, the testing framework became really, really important when it became,
[3158.34 → 3159.46] it's like, okay, this thing works.
[3159.72 → 3162.60] And now like we, let's make it faster.
[3163.04 → 3168.38] Um, and, um, Matt, this may be a good opportunity to get, to get you in the conversation here because
[3168.38 → 3173.00] you've been very much on the, the, the forefront of, of making it faster.
[3173.44 → 3179.60] Um, because we had, we, and we had, I mean, and I mean, to hugely to crucible's credit,
[3179.72 → 3180.40] it's been great.
[3180.46 → 3185.06] It's a it's done what it's needed to do in terms of like, you haven't, we have, haven't
[3185.06 → 3185.54] you had data?
[3185.62 → 3186.38] We'll take vacations.
[3186.52 → 3192.26] It's, it's been great, but, uh, we also need to make, I mean, there is no, I, one of
[3192.26 → 3198.02] the challenges with IO is like, there's no performance that is going to be a we always want more
[3198.02 → 3202.64] performance, and you always want to be able to do, um, the, the absolute most amount of
[3202.64 → 3203.04] work.
[3203.40 → 3209.92] Um, and, uh, Matt, maybe you can describe some of your early work and, and, uh, I think this
[3209.92 → 3213.16] is where also the, the presence of the test suite, the kind of implementation rust becomes
[3213.16 → 3217.84] super important when it comes to make it faster because you can actually make some pretty radical
[3217.84 → 3220.16] changes and get some confidence in them.
[3220.64 → 3221.48] Yeah, absolutely.
[3221.68 → 3226.04] I mean, if Alan was coming in at like from the bottom up and James was coming in from the
[3226.04 → 3228.62] top down, I guess that leaves me at the like middle out position.
[3230.30 → 3233.10] So yeah, I joined the crucible team.
[3233.10 → 3237.08] I was previously doing hubris stuff, working on embedded switch from where I was on a previous
[3237.08 → 3238.40] episode about that a while ago.
[3238.70 → 3243.74] Uh, but I joined crucible and started working in earnest, uh, August of last year and was
[3243.74 → 3247.78] kind of the mandate was basically like, look at things that are slow and see if you can make
[3247.78 → 3248.42] them faster.
[3249.14 → 3254.00] And so this was another situation where like Brian said, like using rust, having such an extensive
[3254.00 → 3257.92] test suite meant that we could do like relatively broad refactoring.
[3258.06 → 3263.42] Like one of the things that we changed, uh, relatively early on was the actual on-disc format
[3263.42 → 3268.24] that we use for data where this is going a little bit into the weeds, but we are using
[3268.24 → 3269.44] authenticated encryption.
[3269.44 → 3275.36] So we have to store both a blob of data, which is like 4k, uh, for each block and then an associated,
[3275.36 → 3278.54] uh, tag and some metadata for the encryption.
[3278.54 → 3281.48] And you can't mess that up.
[3281.48 → 3284.22] If you write the block, but don't have the metadata, then you're not going to be able
[3284.22 → 3284.86] to decrypt it.
[3284.86 → 3290.16] And so you, the implementation that we had previously been actually using SQLite to store
[3290.16 → 3294.42] the metadata, because that's something that is very good at not losing your data.
[3295.18 → 3297.78] And it would actually store like multiple rows of metadata.
[3297.78 → 3301.94] And then when it loaded, it would pick whichever row corresponded to the block on disc and use
[3301.94 → 3302.26] that.
[3302.26 → 3307.94] And so on of the things we worked out is that we didn't actually quite need that level
[3307.94 → 3308.46] of overkill.
[3308.46 → 3311.18] We can actually store the metadata within the same files.
[3311.18 → 3315.82] And we started leaning on like some ZFS behaviour where if you're writing to the same file descriptor,
[3315.82 → 3319.90] then you have certain guarantees about ordering and what's persistent on disc based on when
[3319.90 → 3320.74] you send flushes.
[3320.98 → 3328.00] So changing from ZFS or changing from SQLite to just using raw files was like a 30% speed up
[3328.00 → 3329.70] for a bunch of small writes.
[3329.70 → 3334.52] And so that's kind of example of like, there's a lot of, we're pretty far from the like raw
[3334.52 → 3339.08] speed of disk IO, and we've been slowly bringing it closer and closer through both like micro
[3339.08 → 3342.94] things like that and like bigger architecture changes and kind of refactoring large chunks
[3342.94 → 3344.84] of the system to do async more efficiently.
[3346.42 → 3351.78] I do remember when we chucked SQLite back out though, like I feel like it has to get some
[3351.78 → 3356.06] kind of special mention for being really quite a lot faster than even I expected, I think
[3356.06 → 3356.98] that it was going to go.
[3357.56 → 3359.26] It lasted quite a while.
[3359.26 → 3359.70] Yeah.
[3359.70 → 3361.38] It was pretty impressively quick.
[3361.94 → 3363.50] And we didn't have it originally.
[3363.76 → 3365.14] And then we put it in and then.
[3365.54 → 3365.80] Right.
[3365.88 → 3372.30] Because we didn't have, we didn't have, we had naively in 2020, not really thought that hard
[3372.30 → 3374.32] about encryption and what it meant.
[3374.32 → 3385.12] And the property of like the like unauthenticated encryption can be size preserving.
[3385.50 → 3389.80] So if you're going to write a 4k block and then, or an encrypted version of that block,
[3389.84 → 3391.36] it's still 4k at the end.
[3391.36 → 3396.82] But the authenticated encryption stuff, which unfortunately is necessary.
[3396.82 → 3401.10] Like when you look at all the attack models, it's like kind of difficult to argue that
[3401.10 → 3402.02] it's not necessary.
[3402.02 → 3411.58] And it is just like, it adds some number of additional, not very power of two shaped data alongside
[3411.58 → 3412.84] the 4k sector.
[3413.20 → 3417.58] It'd be like 4.1k, which doesn't fit very good into anything.
[3417.58 → 3418.76] Yeah.
[3418.92 → 3420.28] It's 48 bytes of metadata.
[3420.94 → 3421.26] Right.
[3421.38 → 3422.90] Which is like, you think, oh, that's not much.
[3422.98 → 3425.86] Like it's not, but also it's not a multiple of anything.
[3426.10 → 3435.62] And it has to go, you have to like atomically update that 48 bytes alongside the block data,
[3435.68 → 3437.70] which is nicely shaped on purpose.
[3437.96 → 3440.94] So that definitely made it a lot more complicated.
[3441.02 → 3442.58] And that's why we ended up with SQLite.
[3443.34 → 3446.74] Whereas in the original model, we didn't have any of that metadata stuff hanging off the
[3446.74 → 3446.98] side.
[3446.98 → 3449.98] We just had like a flat file, basically.
[3450.52 → 3450.72] But yeah.
[3450.90 → 3452.10] Encryption makes things challenging.
[3453.04 → 3455.60] The funny thing about SQLite is that we actually tested two versions.
[3456.02 → 3459.52] In one version, we got rid of SQLite and put everything into these raw files.
[3459.86 → 3463.42] And in the other test, we got rid of the raw files and actually put the block data into
[3463.42 → 3463.94] SQLite.
[3464.56 → 3466.38] And both of those were actually faster.
[3466.90 → 3470.44] But we decided to ditch SQLite for the sake of simplicity.
[3470.58 → 3471.50] But it was still pretty impressive.
[3472.38 → 3472.60] Yeah.
[3474.24 → 3474.64] Yeah.
[3474.64 → 3475.82] I mean, it was actually.
[3475.82 → 3478.24] I mean, SQLite is just kind of what it says on the tent.
[3478.32 → 3478.92] It's very robust.
[3479.22 → 3481.62] And it was actually pretty easy to understand what was going on.
[3482.32 → 3485.60] Relatively easy to instrument the system to understand what was going on.
[3486.64 → 3489.06] And Matt, you were kind of.
[3489.06 → 3491.80] In terms of some of the bigger refactorings.
[3491.80 → 3501.28] I mean, and we've made available RFD 444 and 445 go into some of the things that you've worked
[3501.28 → 3501.72] on there.
[3503.30 → 3508.96] What were some of the ways in which we were able to kind of refactor it to in the name
[3508.96 → 3509.58] of performance?
[3509.58 → 3516.60] So RFD 444 is a deep dive into the upstairs architecture and kind of big refactoring,
[3516.72 → 3523.24] probably too big, that switched a lot of the data ownership around, where when the software
[3523.24 → 3527.68] was growing, it was using Tokyo tasks to do a bunch of different operations in parallel.
[3527.96 → 3531.86] But those tasks were all mostly operating on the same chunk of data.
[3531.86 → 3535.84] Like we had one big lock where each task would lock it and do some work and then unlock it,
[3536.28 → 3539.20] which meant that you weren't actually running the tasks in parallel.
[3539.20 → 3541.56] Like you weren't actually getting much parallelism out.
[3542.04 → 3545.58] And there were also concerns of like, well, are you sure that you maintained your invariance
[3545.58 → 3545.96] correctly?
[3546.22 → 3549.56] And are you sure that the locks live long enough that no one else can interrupt you and stuff
[3549.56 → 3550.06] like that?
[3550.52 → 3557.46] So RFD 444 describes a relatively major refactoring where we took the system of like six or seven
[3557.46 → 3562.14] interlocking tasks and basically refactored into one big task that owned all the data.
[3562.36 → 3567.02] And then a handful of smaller tasks who were just doing serialization, deserialization and encryption
[3567.02 → 3568.08] at the edges.
[3568.08 → 3574.88] And that was, ended up being a decent speed-up because we could kind of figure out where
[3574.88 → 3579.64] is the heavy work, which was again, encryption, serialization, deserialization, and then move
[3579.64 → 3580.58] that out to the side.
[3580.78 → 3585.52] And the simple, you know, quote unquote, simple logic of just shuffling what jobs are ready
[3585.52 → 3589.14] to run and kind of throwing them over the fence to the different downstairs, that could
[3589.14 → 3591.52] all be done in one place, which owned all of its data.
[3591.94 → 3593.70] So that ended up being another nice speed up.
[3593.70 → 3597.90] And you know, Alan, you were talking earlier about not being able to imagine doing it in C.
[3598.06 → 3603.74] This refactor is one where like, I cannot imagine this is, because this is the kind
[3603.74 → 3608.26] of thing where I don't care how veteran you are with C, like we're now going to really
[3608.26 → 3611.34] kind of change the way things are paralyzed and, and, or not.
[3611.34 → 3615.74] And just like, would be very hard to get confidence in.
[3615.74 → 3620.58] And I think this was a huge, I mean, the fact that we could do this kind of refactoring at
[3620.58 → 3622.82] all, let alone get like pretty quick confidence in it.
[3624.48 → 3628.06] Another good example of that is actually like a smaller thing, which I've mentioned this to
[3628.06 → 3631.86] everyone at work, but I recently went through and just removed four mutates from the crucible
[3631.86 → 3636.32] downstairs because they were not actually protecting anything.
[3636.60 → 3639.44] And that's the kind of thing where if I was doing this or C++, I would be terrified
[3639.44 → 3643.16] to make that kind of change because like, we never know how would you stash a copy of your
[3643.16 → 3647.96] data, but because we're using rust, like I tried compiling it.
[3648.02 → 3653.32] I had to add a couple of more, I had to make a couple more ref things mutable instead of
[3653.32 → 3653.64] immutable.
[3654.28 → 3658.06] And there was one thing which actually the compiler was like, Hey, you're secretly sharing
[3658.06 → 3658.84] this between threads.
[3658.84 → 3662.94] So I had to re add one mute, but I still got rid of the other four.
[3663.60 → 3666.24] And then once it compiled, it was like, I'm pretty sure this is safe.
[3667.28 → 3671.34] In the original sketch of the whole thing, which was not more than a couple of thousand
[3671.34 → 3672.30] lines, really.
[3672.54 → 3680.30] Like I had absolutely punched on any hint of performance, like in the job tracking stuff,
[3680.50 → 3683.62] like the because my expectation was that we'd be able to fix it later.
[3683.74 → 3684.14] Basically.
[3684.14 → 3692.18] Like I had really focused on the correctness, which I had achieved through a lot of things
[3692.18 → 3694.72] that did a lot of loops, scanning over everything.
[3694.72 → 3701.14] And rather than like having a list of tasks that are in this state and a list of tasks
[3701.14 → 3704.32] that are in that state, we just put them all in one big list, and we had a state variable
[3704.32 → 3705.02] on the task.
[3706.10 → 3710.68] And I feel like one of the first performance things, maybe Brian, you worked on was like
[3710.68 → 3716.84] refactoring some of that stuff so that we weren't doing as many scans of memory to like
[3716.84 → 3720.74] once we'd figured out what shape the data structures actually needed to be in to track these things
[3720.74 → 3725.12] and what, what properties we needed to enforce as invariants across the whole thing.
[3725.12 → 3729.42] Like, I feel like it's been, there's just been a lot of constant refactorings as we've
[3729.42 → 3736.80] unpicked experiments and turned them from like a correct proof of concept into a correct
[3736.80 → 3738.86] and fast operable system.
[3739.34 → 3739.78] Yes.
[3739.92 → 3743.78] Which is, by the way, that's the same path that ZFS itself took, right?
[3743.82 → 3744.90] ZFS itself.
[3745.28 → 3749.98] But I mean, if you, the I mean, Adam, when you describe us shipping that in 2008 and that
[3749.98 → 3753.96] kind of being, even though ZFS had been in customer stance 2005, the difference between
[3753.96 → 3760.00] what we did from 2008, 2009, 2010 was really all ultimately around performance.
[3760.12 → 3763.82] And it's not performance in kind of the way you might think of just like IOPS because
[3763.82 → 3765.72] performance is a lot more than just IOPS.
[3765.96 → 3771.22] Performance is how do you behave when things begin to, to behave pathologically.
[3771.72 → 3777.28] And I feel like, you know, Josh, what you're describing where you have things that, that
[3777.28 → 3782.20] scale with the data size, in particular, like snapshot deletion was a, I mean, the one that
[3782.20 → 3788.52] definitely has some scar tissue where ZFS would do these, where a small snapshot delete
[3788.52 → 3793.96] would be fine, but a large snapshot deletion would be on the order of the you end up in,
[3794.06 → 3798.28] when you're trying to sync a transaction, you're doing random reads, which is always the kiss
[3798.28 → 3798.66] of death.
[3798.66 → 3805.50] And, you know, Matt, Aaron's some terrific work to, to get that out and be able to do
[3805.50 → 3806.52] large snapshot deletion.
[3807.28 → 3813.30] And I would also think that like one of the challenges too is that, and this is, I, frankly,
[3813.38 → 3817.42] one of the advantages that Crucible has over CFS is the ability to do these kinds of refactors
[3817.42 → 3820.78] because some of these refactors were, were really impossible in CFS.
[3820.82 → 3825.82] I mean, there's some refactors that I think would just be terrifying to do in CFS because
[3825.82 → 3828.54] of the way state is spread through the system.
[3830.40 → 3837.18] And I mean, we, like we had dedupe, for example, CFS supports deduplication, but the way it was
[3837.18 → 3844.04] done was definitely not very many lines of code, but really problematic from a performance perspective
[3844.04 → 3846.64] and not really possible to right the ship on that one.
[3847.62 → 3848.90] That one's just what it was going to be.
[3849.70 → 3853.06] I wrote the dialog box though, that you have to click when you want to enable it.
[3853.06 → 3855.78] And you're real explicit about that.
[3857.24 → 3862.46] One of the other funny things that we ran into with these cleanups is we had a lot of
[3862.46 → 3866.54] sources of what we started calling accidental back pressure, like things that scaled with
[3866.54 → 3869.92] the number of jobs in a queue or scaled with the size of rights.
[3870.56 → 3874.72] And as we started taking these down, we suddenly ran into issues like, oh, look, the upstairs is
[3874.72 → 3878.96] going to buffer 400 gigabytes of rights because there's nothing slowing it down anymore.
[3878.96 → 3880.70] And the downstairs cannot keep up.
[3882.44 → 3887.72] So let's talk a little bit about back pressure because back pressure is very, very important.
[3888.16 → 3894.22] And I mean, if you do not develop deliberate back pressure into your distributed system,
[3894.92 → 3896.42] God will develop it for you.
[3896.76 → 3900.06] And it doesn't even need to be distributed, right?
[3900.06 → 3906.92] Like, I mean, a lot of these surprise explosion bucket things were like, like between queues
[3906.92 → 3908.62] were just inside the process.
[3910.06 → 3911.58] God's own back pressure is not pretty.
[3911.70 → 3912.52] You do not want that one.
[3912.68 → 3914.02] You want the designed one.
[3915.26 → 3920.70] Well, it's worth saying, I mean, in particular, God's own back pressure becomes very inconsistent
[3920.70 → 3921.96] and unpredictable.
[3922.74 → 3926.64] So there's always going to be back pressure somewhere, but it's sort of what it looks like.
[3927.06 → 3929.76] And God's own back pressure actually manifests itself as a data vacation.
[3930.06 → 3936.24] It's like we are, this system is no longer available and will be available when it is
[3936.24 → 3937.66] chosen to become available again.
[3937.78 → 3938.80] And that's not what we want.
[3939.48 → 3944.48] We want to have a not to, not to play too much of divine intervention in storage systems,
[3944.60 → 3945.82] but it sometimes feels that way.
[3946.96 → 3952.32] Although I actually didn't, you know, Don McCaskill was an early customer of ours, Adam, at Sun.
[3953.04 → 3956.88] And every time I think of Don McCaskill, all I think about is waiting for his data to come
[3956.88 → 3959.26] back on a Z-Port that was taking like 45 minutes.
[3959.26 → 3961.10] He doesn't even remember that happening.
[3961.28 → 3961.82] God bless him.
[3962.14 → 3965.76] So, you know, sometimes he doesn't remember the vacations, but it was very painful.
[3966.86 → 3973.04] So, Matt, how did you kind of think about back pressure in the system in terms of designing
[3973.04 → 3973.68] it explicitly?
[3975.54 → 3975.66] Yeah.
[3975.66 → 3975.70] Yeah.
[3975.78 → 3981.52] So it's interesting because things like reads and flushes, we had to wait for the downstairs
[3981.52 → 3982.44] to come back, right?
[3982.48 → 3984.60] For reads, you needed at least one copy of the data to come back.
[3984.68 → 3986.86] For flushes, I think we needed two out of three to come back.
[3987.30 → 3992.40] But for writes, we had an optimization where as soon as the upstairs submits a White, we
[3992.40 → 3993.48] immediately tell it, you're good.
[3993.84 → 3997.90] Because writes don't need to be persistent until the following flush actually comes along.
[3997.90 → 4004.20] And so this is interesting because it's analogous to actually an old blog post from Adam, one
[4004.20 → 4009.16] Adam Levinthal about the ZFS write throttle, which is solving basically the same problem
[4009.16 → 4014.14] of like, we can cache a certain amount of data in RAM, but we can't cache infinite data
[4014.14 → 4014.74] in RAM, right?
[4014.74 → 4016.30] So we have to start slowing down at some point.
[4017.50 → 4020.76] So the design, I can't remember whether I came up with it before or after reading that
[4020.76 → 4024.68] blog post, but it ended up being very similar where we track a handful of things.
[4024.68 → 4028.16] We track the number of jobs that are in flight and the number of bytes that are in flight.
[4029.00 → 4033.66] And we have a quadratic equation with a bunch of tuned parameters that I made up at random.
[4034.24 → 4036.62] And that will artificially delay writes.
[4036.96 → 4042.92] So the system ends up in a kind of steady state where the delay added by the SPAC pressure
[4042.92 → 4046.24] converges to the same amount of time it actually takes for a White to go through the whole
[4046.24 → 4046.60] system.
[4047.90 → 4049.28] And that is like pretty good.
[4049.64 → 4053.14] There's still some tuning that we need to do that RFD 445 talks about a little bit.
[4053.14 → 4059.46] But this fixed the like most pathological case of the upstairs will buffer infinitely much
[4059.46 → 4062.12] write data because it's so much faster than the downstairs.
[4062.90 → 4065.88] I'm pretty sure the infinite buffering was due to me.
[4066.20 → 4067.42] Just due to me.
[4067.84 → 4069.08] And I think, is that a fair?
[4070.36 → 4071.70] You may have suggested.
[4073.22 → 4076.36] I remember you came to seek an indulgence about this, right?
[4076.42 → 4077.14] You're like, couldn't we just...
[4077.90 → 4078.64] I think I'm going to seek an indulgence about this.
[4078.64 → 4084.94] Because we used to, you know, foolishly wait for two of the writes to be acknowledged on
[4084.94 → 4088.42] the platter, basically, before we would tell the guest.
[4088.68 → 4090.82] And it's like, we don't actually need to do that.
[4091.42 → 4092.02] That's true.
[4092.60 → 4094.80] It did go quite a lot faster.
[4095.62 → 4096.90] Stop waiting for that.
[4097.96 → 4101.64] Fast enough to explode, in fact, as it turns out.
[4101.64 → 4104.86] Just to give folks a little bit more of additional context.
[4105.10 → 4109.36] So we are presenting a virtual block device up to a guest.
[4109.78 → 4114.86] And we are telling the virtual block device that, hey, by the way, we have a write cache.
[4115.12 → 4116.84] There's a write cache that's enabled on this.
[4117.82 → 4119.64] A non-volatile?
[4120.44 → 4121.78] A non-volatile write cache.
[4122.62 → 4123.90] Or a volatile one.
[4124.28 → 4124.88] Volatile one.
[4125.34 → 4126.06] Volatile one, yeah.
[4126.06 → 4133.94] So if you've not done a flush, you cannot assume that your data has been persisted.
[4134.88 → 4136.22] But we were on writes.
[4136.34 → 4139.70] We were waiting until those writes had been acknowledged by two different machines.
[4139.90 → 4142.82] Because it's like, well, I mean, what are we, nuts?
[4142.98 → 4145.72] Like, of course, we want to make sure that two different machines at least have seen this
[4145.72 → 4147.38] thing and have synced us out.
[4147.42 → 4149.48] And I'm like, hey, we can make the system go a lot faster.
[4150.78 → 4153.06] Like, we just can act it immediately, of course.
[4153.30 → 4154.36] That's what the disk is doing.
[4154.44 → 4155.36] That's what your argument was.
[4155.36 → 4157.68] It's like, the disk is doing that to us already.
[4157.94 → 4160.36] Why don't we just pass that on to the...
[4160.98 → 4162.34] And what can go wrong?
[4162.40 → 4163.72] I'm sure I said many times.
[4164.22 → 4165.48] But yes, I was thinking of indulgence.
[4165.64 → 4171.86] It turns out that created, sorry, created a lot rather explosive amount of, now we have
[4171.86 → 4176.50] now can explode the upstairs with buffer data, which is like, that's okay.
[4176.80 → 4178.64] So we've got to actually...
[4178.64 → 4182.60] And it's always kind of paradoxical to me when you actually need to make, in order to make
[4182.60 → 4186.64] the system go faster, you need to throttle the work.
[4188.10 → 4190.98] You know, but this is like, you know, these are the metering lights in traffic, right?
[4191.00 → 4194.92] I mean, it's like, in order to be able to make the aggregate system go faster, it's like,
[4194.98 → 4196.82] yes, you need to stop your car right now.
[4196.92 → 4201.46] It's like, the way to make, get you to work quickly is to be, to have you be stopped right
[4201.46 → 4202.90] now, which can be very counterintuitive.
[4202.90 → 4203.54] But...
[4203.54 → 4207.34] And the I mean, the back, we knew we would need to do the back pressure work at some
[4207.34 → 4207.76] point.
[4207.86 → 4213.12] Anyway, there were lots of like, come back and do this better next time comments.
[4213.82 → 4213.86] Oh.
[4214.26 → 4218.20] Well, and I think importantly, I mean, because you were constantly picking and choosing
[4218.20 → 4222.36] about like, what is the stuff that has to be exactly right out of the gate versus what
[4222.36 → 4225.66] are some implementation, implement, implementation artifacts we can improve.
[4225.78 → 4229.12] And I mean, we had to get the reliability, obviously had to be correct, Alan.
[4229.12 → 4230.06] What were some of the other things?
[4230.18 → 4232.90] Because we, we, encryption was an important constraint.
[4233.34 → 4233.46] Yeah.
[4235.10 → 4239.16] Making sure, I think Josh talked about this earlier, that the order of things happens
[4239.16 → 4242.10] on all three of the all the downstairs in the same way.
[4242.20 → 4245.00] So whenever the IO is laying, they all got to land in the same way.
[4245.76 → 4249.78] That's another piece that's sort of fundamental to the whole, the whole thing working when you
[4249.78 → 4251.42] come back up after a power loss.
[4255.50 → 4258.94] And then, and those are the things that, that absolutely, and then there's,
[4259.12 → 4261.40] a bunch of functionality that you also like absolutely need.
[4261.48 → 4265.06] Like snapshots are not really, I mean, are rather important for us.
[4265.22 → 4265.40] Yeah.
[4266.60 → 4270.74] James, you talk about the development of that in particular, because as I recall, you know,
[4270.80 → 4276.82] in software, most things take longer than you think to do.
[4277.76 → 4282.46] And every once in a while you have something that is actually faster than you thought it
[4282.46 → 4282.76] would be.
[4282.76 → 4287.78] I feel like Matt, this giant refactoring that you, I feel like that's an example, even
[4287.78 → 4291.98] though as big as that was, the fact that that was possible at all, let alone the speed
[4291.98 → 4293.70] at which you're able to do that and get that integrated.
[4294.04 → 4296.98] I think it was actually faster than one would expect.
[4298.56 → 4302.20] And James, it felt like that way for some of the snapshot work you did as well.
[4302.26 → 4303.16] Am I recalling that correctly?
[4303.28 → 4307.48] There was some, I just recall you like, when James did the volume layer, I think that
[4307.48 → 4312.50] opened up a bunch of doors and solved a bunch of problems that we were like, I don't
[4312.50 → 4313.98] know, we'll get to that later, hopefully.
[4315.44 → 4317.98] So James, do you want to elaborate a little bit on that, on the volume layer?
[4320.40 → 4321.08] Sure, yeah.
[4321.52 → 4322.66] I had to look this up.
[4322.86 → 4324.44] I'm not great with dates.
[4324.44 → 4330.88] So early 2022, we had a storage huddle where we talked about kind of what Alan had said.
[4331.10 → 4335.14] So like, hey, there's all these things that customers are going to expect from our cloud.
[4335.70 → 4338.56] We should probably start thinking about that.
[4338.98 → 4340.20] So that was Monday, right?
[4340.76 → 4341.82] And I think that's what I'm saying.
[4342.50 → 4345.08] So we came out of that, we started thinking about it.
[4345.24 → 4352.34] At that point, we had Propolis with its NVMe device emulation that would, underneath that,
[4352.44 → 4354.70] talk to what we called the guest.
[4354.70 → 4359.60] Now, this would be the object that communicates with the upstairs through channels.
[4359.96 → 4365.52] So when there's an NVMe read that comes in, this gets turned into a crucible read, sent
[4365.52 → 4370.40] over this channel to the upstairs, the upstairs sends it to all three downstairs, so on and
[4370.40 → 4371.46] so forth, does its stuff.
[4371.46 → 4373.20] This read comes back.
[4373.20 → 4380.60] It then gets written into the guest memory, and then the NVMe doorbell gets wrong, stuff
[4380.60 → 4381.00] like that.
[4381.70 → 4386.88] But the structure of it was this guest object, and that was implementing all the things you
[4386.88 → 4388.24] would expect, read, write, and flush.
[4388.24 → 4392.58] So we had Propolis.
[4392.82 → 4399.06] So I started thinking about what that product had to support based on what was in that meeting.
[4399.22 → 4401.88] So booting from an image of some sort.
[4401.88 → 4407.44] Everybody shares the same Ubuntu server image, for example, and you would have to spin up
[4407.44 → 4408.32] a VM from that.
[4409.16 → 4413.42] Snapshots, taking that from the disk, and then booting from those snapshots, stuff like that.
[4413.90 → 4419.00] But then some of the more elastic properties, I expect, like growing a disk, for example,
[4419.12 → 4421.74] at runtime, stuff like that.
[4421.74 → 4427.88] So take booting from an image as an example.
[4428.02 → 4430.38] Say a user wants to boot a VM.
[4431.06 → 4434.84] They create a 32-gig disk backed by an image.
[4434.90 → 4436.98] Let's take that Ubuntu server image.
[4437.36 → 4438.20] They click Start VM.
[4438.20 → 4444.54] We didn't want to have customers wait for us to copy all the blocks from an image into
[4444.54 → 4449.56] this freshly allocated 32-gig blank region and then boot the VM.
[4449.84 → 4452.04] That would be not a great experience.
[4452.92 → 4459.36] So out of that, you think, well, now blocks have to optionally come from different sources.
[4459.56 → 4464.02] And this was never in the design of the southern mix.
[4464.10 → 4466.14] It was never in the design of the upstairs and the downstairs.
[4466.14 → 4469.12] There's this optional location.
[4471.02 → 4474.86] So breaking it down for an image base, you're booting off of an image.
[4475.36 → 4479.18] The image blocks have to come from somewhere immutable, right?
[4479.22 → 4481.34] You don't want the guest to be able to alter those.
[4481.86 → 4486.12] But any write should go to this freshly allocated 32-gig region.
[4486.70 → 4491.74] And then you have to make sure that subsequent reads of those written blocks would come from there.
[4491.74 → 4501.96] I think at that point, yeah, at that point, we could tell if a block had been written to based on the existence of this block context.
[4501.96 → 4511.92] So if you've got either the encryption context or the integrity hash that we store alongside the encrypted block data, you know that a White had occurred.
[4512.48 → 4521.02] So we could use that at least to say, you know, the allocated freshly 32-gig region had a White there.
[4521.34 → 4521.90] Serve that.
[4521.98 → 4523.30] Else serve the image block.
[4523.30 → 4526.82] But then you have to think about layering, right?
[4526.92 → 4536.08] So you could teach an upstairs to pick from two sources optionally, like depending on, you know, which writes shadow each other or not.
[4536.70 → 4540.72] But say a user has a disk, and then they say, okay, I'm going to take a snapshot of that disk.
[4540.78 → 4543.02] And then I'm going to boot a disk based on that snapshot.
[4543.22 → 4545.30] And then I'm going to, you know, take a snapshot, blah, blah, blah.
[4545.42 → 4546.64] You say they do this 100 times.
[4546.64 → 4550.80] Because now your blocks have to come from an arbitrary number of places.
[4552.30 → 4556.46] I didn't want to, you know, muck with the upstairs that much, right?
[4556.48 → 4560.74] It's doing a lot of complicated things, wrangling the three downstairs.
[4561.98 → 4565.94] And I didn't want to have an arbitrarily large list of these block sources, right?
[4565.96 → 4567.38] You only want to deal with the three mirrors.
[4567.56 → 4572.66] We know up until that point, all the code that we had written was doing that assumption of three mirrors.
[4572.66 → 4574.24] That was something we were comfortable with.
[4574.24 → 4584.20] And importantly, from Propolis's perspective, whatever we came up with, it still had to just have that interface of read, write, flush.
[4584.96 → 4587.02] Propolis shouldn't have to do any special work here.
[4587.12 → 4591.10] They just, you know, talk to the block dev layer, as it were.
[4592.60 → 4599.86] So in thinking about this layering problem, and at the same time thinking about how Propolis shouldn't have to care,
[4599.86 → 4605.30] I came up with the idea for the at the same time you come up with the idea for the volume hierarchy,
[4605.42 → 4608.30] you come up with the block I.O. trait.
[4608.66 → 4616.06] So I took what the guest was already doing and turned that into a trait that we call the block I.O. trait.
[4616.32 → 4616.60] So read.
[4616.60 → 4618.78] A trait in the Rust sense, just to be clear.
[4618.80 → 4619.74] In the Rust sense, yeah.
[4620.22 → 4623.36] I was very much inspired by how awesome Rust is, yeah.
[4623.36 → 4627.32] Which was also referenced in the demo, which, get to that in a sec.
[4629.40 → 4633.90] Yeah, so read, write, and flush, get block size, you know, stuff like that.
[4634.80 → 4636.80] Guest already implemented all of this.
[4637.28 → 4642.32] So then this volume implementation, so the volume object came about.
[4642.84 → 4646.94] So this is a struct that itself implements block I.O.
[4646.94 → 4654.08] It has an optional read-only parent, and then a list of what are called sub-volumes,
[4654.30 → 4660.60] which have, which themselves implement block I.O., but also store LBA-related information,
[4660.76 → 4663.50] so logical block address, so a range of some sort.
[4664.56 → 4670.32] And from this, you have that sort of model where writes go to the sub-volumes,
[4670.32 → 4674.96] and reads can come from either the sub-volumes or the read-only parent,
[4675.52 → 4677.80] depending on if a block was written to or not.
[4678.84 → 4684.88] And then you have this immutability by saying that writes only ever go to the sub-volume.
[4685.90 → 4691.08] And the volume layer takes care of all the, you know, you have to split a read and send,
[4691.32 → 4694.08] you know, certain block reads go here, certain block reads go there,
[4694.74 → 4696.40] splitting the writes also accordingly.
[4696.40 → 4700.36] Flushes go everywhere because, you know, you have to flush everything.
[4703.48 → 4707.68] So after that, you think, how do we solve this layering problem?
[4707.84 → 4713.12] Well, the volume object implements block I.O., so it can itself be a read-only parent,
[4713.28 → 4715.88] and then that gives us that layering right away.
[4716.72 → 4722.42] So in the case of a take a snapshot, for example, you have a read-only parent,
[4722.42 → 4728.34] which is an image source of some sort, and then the freshly allocated 32-gig region.
[4729.12 → 4736.40] To take a snapshot is to, first, perform a ZFS snapshot on that 32-gig region.
[4736.98 → 4743.66] This gives you places where you can boot read-only downstairs out of the .ZFS slash snapshot directory.
[4744.28 → 4748.20] And you know, based on ZFS's guarantee, that this data will never change.
[4748.20 → 4751.76] So this is actually an important point, James, and I just, because, you know,
[4751.84 → 4754.62] we didn't really belabour it, Adam, when we were talking earlier,
[4754.86 → 4757.08] but someone might reasonably be like, wait a minute,
[4757.22 → 4759.80] you're going to have a Pool that consists of a single SSD?
[4760.02 → 4763.02] You're going to have all these, you know, 10 NVMe SSDs?
[4763.20 → 4765.08] Like, why are you putting a Pool on them?
[4765.12 → 4767.12] Like, just use the device directly.
[4767.82 → 4771.50] And there, I mean, there was a bunch, or there were a bunch of reasons for it,
[4771.50 → 4775.26] but we wanted to be able to leverage a bunch of the semantics that ZFS was offering,
[4775.26 → 4777.70] even though we weren't using erasure encoding or mirroring.
[4778.74 → 4780.92] You wanted the copy-on-write snapshooting stuff.
[4781.32 → 4782.66] You wanted the copy-on-write snapshooting stuff.
[4782.86 → 4783.38] And you want to check some of this.
[4783.38 → 4785.96] It makes certain things, like, really a lot easier.
[4786.26 → 4792.88] You don't have to invent or contort your data format into something that does its own native copy-on-write stuff.
[4793.08 → 4797.76] Like, you can just write the files and take a snapshot at the time that you need it,
[4798.06 → 4800.70] and then access it as a read-only thing off to the side.
[4800.88 → 4801.44] It's pretty good.
[4802.04 → 4802.24] Right.
[4802.24 → 4806.66] So really, sorry, James, just to briefly interject in terms of, like, why that,
[4807.20 → 4810.26] because when you're developing the snapshooting mechanism, you're able to leverage,
[4810.70 → 4815.76] you're able to at least solve some fraction of the problem by using ZFS snapshots.
[4817.04 → 4823.58] We ended up relying on a few of those ZFS-based things for at least sort of the DOG stent work
[4823.58 → 4829.86] and some of the guarantees that we get about the downstairs will only ever return, for example,
[4830.10 → 4835.20] okay if all the checksums from ZFS say that they're okay, for example.
[4836.30 → 4837.08] Stuff like that.
[4837.20 → 4837.34] Yeah.
[4837.40 → 4838.54] We end up relying on it.
[4839.26 → 4841.20] Copy-on-write and the transaction group stuff.
[4841.20 → 4841.44] Yeah.
[4844.44 → 4844.80] Yeah.
[4844.90 → 4845.32] So...
[4845.32 → 4845.96] Sorry.
[4846.12 → 4846.16] Yeah.
[4846.16 → 4847.16] So, yeah.
[4847.28 → 4848.72] All the problems that...
[4848.72 → 4849.98] I think I was there.
[4850.04 → 4853.16] All the problems that we had talked about in that storage huddle.
[4853.54 → 4860.44] Growing a disk, well, that's just adding to the subvolume, like the DEC of subvolumes.
[4860.98 → 4863.22] You can even talk about re-encryption.
[4863.22 → 4872.22] So you make the existing volume a read-only parent, and then you boot an equivalently sized region with a different encryption key.
[4872.88 → 4878.06] Importantly, you need this operation called a scrub that is done by Propolis,
[4878.30 → 4882.64] where blocks are read from the read-only parent and written to the subvolume,
[4883.20 → 4885.36] but only if they had never been written before.
[4885.36 → 4889.86] So this is not going to overwrite whatever guest activity had occurred.
[4891.04 → 4894.10] Once something like that is done, you can drop the read-only parent
[4894.10 → 4898.10] and then issue all of your reads and writes directly to the subvolumes.
[4899.14 → 4902.02] You could even do a crucible upgrade, right?
[4902.06 → 4907.28] Like an upstairs V2 or something like that, because this is all hidden behind that trait.
[4908.02 → 4915.32] It ends up being a hammer where everything that we wanted to solve would be the nail, I guess, in this case.
[4916.34 → 4917.46] So Brian, you're not wrong.
[4917.50 → 4919.28] It did come together very, very quickly.
[4919.44 → 4923.20] Monday was sort of the genesis of it, and then Friday was the demo.
[4923.62 → 4927.80] I remember talking to Alan for feedback during the week,
[4927.88 → 4932.04] but there was a particular meeting on Thursday where it's like,
[4932.06 → 4935.04] oh yeah, this came together, but is this good?
[4935.38 → 4936.06] What do you think?
[4936.08 → 4937.76] I had it with Josh and Alan.
[4937.88 → 4938.80] It was like, hey, what do you think?
[4938.86 → 4939.78] Did I miss something?
[4940.64 → 4943.64] Did I overlook something that will bite us later kind of thing?
[4943.64 → 4945.46] I was pretty excited.
[4945.56 → 4949.80] I wanted to sort of demo it and sort of start building on top of it,
[4949.80 → 4953.56] because it enabled us to move in that direction pretty quickly.
[4954.02 → 4959.40] I think that the stuff that you put together with that abstraction really
[4959.40 → 4965.30] was like a good concrete rendition of a bunch of hand-waving
[4965.30 → 4968.64] that we'd been doing for probably two years at that point.
[4968.68 → 4975.48] Because we had talked a lot about the Fish works appliance had had a feature called
[4975.48 → 4977.38] shadow migration, I believe.
[4978.02 → 4978.28] Yeah, yeah.
[4978.28 → 4986.16] In which, like, you would say, all right, you've got this existing file server
[4986.16 → 4990.36] with, you know, 100 gigabytes of crap in it or whatever, or a terabyte or something.
[4990.64 → 4994.96] It's going to take a while to copy that over to this new Shiny file server.
[4995.32 → 4999.92] So instead of just everybody has to unmount everything and go away for eight hours or something,
[5000.02 → 5003.86] we would, you would just mount the new thing directly.
[5003.86 → 5009.44] And the new thing would be smart enough to fish old files out on demand from the back end
[5009.44 → 5013.86] and copy them into the front end before serving them up.
[5014.58 → 5017.60] And then it's almost a little bit like hierarchical storage management.
[5018.76 → 5024.24] Like, I think we had talked at some length about how that was going to be the thing
[5024.24 → 5028.90] that we were going to do for all kinds of things we didn't want to solve at the time.
[5028.90 → 5036.66] Like, rekeying, migrating data format to data format, upgrading software, stuff like that.
[5038.10 → 5042.74] And then when James put this thing together, it was immediately apparent that it was going
[5042.74 → 5045.86] to be useful for all sorts of stuff.
[5046.14 → 5046.90] All sorts of stuff.
[5047.02 → 5051.04] And then, like, pretty concretely demonstratable in a very short order.
[5051.22 → 5052.90] It was a big win for us.
[5053.40 → 5056.14] I mean, there have been a couple of demos that have blown me away over the history of the
[5056.14 → 5059.22] company, but that is definitely, that is among them, where it's just like, James,
[5059.26 → 5062.24] it just felt like that demo was like, but wait, there's more, but wait, there's more,
[5062.32 → 5063.00] but wait, there's more.
[5063.14 → 5066.16] That was the NFTs involved in that demo, I believe.
[5066.96 → 5067.84] Is that the word?
[5068.42 → 5074.92] The I definitely remember, well, I learned that, like, part of the problem is that there
[5074.92 → 5079.94] is, there's an inner performance artist, apparently, in every oxide engineer.
[5079.94 → 5085.28] And, James, your demo with Greg that you alluded to earlier, the two of you were playing Minecraft
[5085.28 → 5087.50] using the oxide rack.
[5088.12 → 5093.74] I learned that I could never trust again, because you two were, there was so, so much
[5093.74 → 5094.48] was part of the bit.
[5094.58 → 5097.92] And, like, whenever Matt's giving a demo, like, you'll then feel at the end that, like,
[5097.94 → 5101.38] you're actually all in my demo right now, which I feel happened at least once, Matt.
[5102.24 → 5105.74] Well, that was the time that I was demoing the network switch and actually running my demo
[5105.74 → 5106.58] internet through it.
[5106.58 → 5110.76] But the problem with this is that now, whenever anything goes wrong during a demo, everyone
[5110.76 → 5111.82] is like, is this a bit?
[5112.02 → 5112.52] Is this a bit?
[5112.56 → 5113.46] I think this is a bit.
[5114.18 → 5114.28] Right.
[5116.22 → 5118.08] And it often is, I feel.
[5118.24 → 5122.02] I feel like it's, I, it was, James, it was, that, that demo was amazing.
[5122.12 → 5125.24] It's just how much came together, how quickly.
[5125.74 → 5130.26] And, I mean, it's, you know, I always tell people, like, whenever that happens, man, just
[5130.26 → 5135.32] make sure you bottle it up so you can spray it on yourself later when something seemingly
[5135.32 → 5139.52] simple is taking you, like, this is taking me much longer than I thought it would take,
[5139.56 → 5141.24] which feels like it's much more common in software.
[5141.42 → 5144.06] But that, that must have been, James, that must have been a great feeling to have that
[5144.06 → 5144.84] come together so quickly.
[5145.34 → 5146.62] That, that was a fun demo.
[5146.92 → 5147.44] Uh, yeah.
[5147.62 → 5152.92] I, I, so I actually, I had remembered something and I don't know if any of you also remember
[5152.92 → 5153.12] this.
[5153.12 → 5158.26] So I looked at that demo again, because, uh, at one point I had a slide with, with the
[5158.32 → 5159.74] sort of the volume struct.
[5159.86 → 5162.28] And it was like, here it is, you know, it's just a couple of fields, blah, blah, blah.
[5162.80 → 5167.58] Uh, but I, I didn't mention this during the time, but it didn't say, you know, like read
[5167.58 → 5170.30] only parent colon arc guest, right?
[5170.32 → 5171.44] It said Dan block IO.
[5171.90 → 5176.54] I didn't mention at the time, but later on as a slide, I, I referenced back to it after
[5176.54 → 5177.60] the first part of the demo.
[5177.60 → 5181.72] Uh, and I said, you know, eagle-eyed readers would have noticed that it didn't say guest,
[5181.82 → 5183.16] it said, uh, block IO.
[5183.70 → 5188.54] And Matt in, in the chat said, actually, yes, I, I did notice this.
[5188.78 → 5190.90] Um, which, uh, which is kind of funny.
[5191.08 → 5195.02] He, before the, the days when he had joined the team and sort of done the work, he was
[5195.02 → 5197.16] already saying like, ah, this is, yeah.
[5198.30 → 5198.70] Anyway.
[5199.28 → 5201.04] Eagle eyed in the, in the demo.
[5201.40 → 5202.38] Uh, early in eagle eyed.
[5202.52 → 5205.98] Well, that was, I said it was, that was great to, great to see.
[5205.98 → 5208.12] And I also felt like it was one of those.
[5208.12 → 5211.44] And I think there've been, again, a couple of these where whenever you're doing something
[5211.44 → 5216.40] hard and long, you're kind of looking for good omens of like, okay, we've got like,
[5216.48 → 5219.02] we're like, we're seeing a seabird.
[5219.08 → 5220.16] We're headed towards land.
[5220.42 → 5222.30] You know, we're not going to be out here forever.
[5222.80 → 5225.46] Uh, and I, I don't know, James, I felt like that was one of those good omens.
[5225.46 → 5229.20] Like, okay, we've got, we're, we've got some things that are actually going in the right
[5229.20 → 5229.68] direction here.
[5229.70 → 5232.14] We've got some things that are structured the right way where you can make a change like this
[5232.14 → 5233.20] and have some stuff coming together.
[5233.28 → 5234.52] I mean, Alan, it must've felt that way to you.
[5234.52 → 5235.00] Yeah.
[5235.04 → 5237.88] Well, it was like this, maybe this thing really is going to work.
[5240.08 → 5241.66] Might actually pull this off.
[5241.98 → 5244.10] Uh, yeah, that was, it was great.
[5244.34 → 5247.00] Um, and we've been able to build a lot of functionality on that.
[5247.04 → 5251.34] I mean, that is, that feels like that has been a James that has stayed a good abstraction
[5251.34 → 5255.54] and really important because as you say, like when you're spinning up guests, it's like
[5255.54 → 5261.02] snapshots, writeable snapshots become actually not some esoteric feature that's nice to have,
[5261.02 → 5265.62] but like actually wired or any real use of the rack.
[5267.46 → 5267.76] Yeah.
[5267.76 → 5268.98] It's one of the yeah.
[5269.02 → 5273.22] One of the things, killer features I would say, like of, of cloud-based infrastructure,
[5273.22 → 5278.10] like snapshot, um, you know, we don't have it yet, but like snapshot restore, for example,
[5278.58 → 5280.72] uh, exporting, importing, stuff like that.
[5280.72 → 5286.64] Like these, this sort of virtual storage things that you would expect, um, yet because we're
[5286.64 → 5291.50] using ZFS snapshots, for example, we can do this very, very quickly, uh, and, and sort
[5291.50 → 5295.88] of build on top of that by booting another disc and, and, uh, you know, our control plane
[5295.88 → 5300.46] takes care of all the reference counting and, uh, cleaning up the objects when, when done,
[5300.62 → 5305.80] uh, if there's no longer, you know, dangling, you know, volume layer that points to it.
[5305.80 → 5307.88] Uh, it's been, it's been pretty good.
[5308.20 → 5308.36] Yeah.
[5309.58 → 5315.10] So, Alan, what would have been some of the surprises along the way in terms of the, um,
[5315.22 → 5320.18] I mean, are, are there things that have been surprisingly hard, surprisingly easy?
[5320.22 → 5326.78] I mean, I, I think you always, um, with, with storage, it's always at the margins and in
[5326.78 → 5333.82] terms of like the degree that misbehaviour deep in the stack can cause, um, kind of outsized
[5333.82 → 5337.76] to fax up the stack, but what, what are being some of the things that stick out to you?
[5339.64 → 5340.68] Hey, I know.
[5346.06 → 5350.32] I know that I had a lot of trouble with the live repair, figuring out how that was going
[5350.32 → 5353.14] to fit into the whole big picture.
[5353.22 → 5356.72] That took me a while to sort of get that sorted.
[5357.36 → 5359.80] Um, it's a describe the constraints a bit on live repair.
[5359.80 → 5359.84] Sure.
[5360.58 → 5366.42] Well, that's when you're, you're taking IO from the guest from a VM, but one of your
[5366.42 → 5369.92] downstairs has failed, and you have to, you have to fix it.
[5369.94 → 5374.30] You have to make it consistent with the other two, but you can't just take a long vacation.
[5374.30 → 5377.38] You have to do this while new IO is a streaming game.
[5377.38 → 5381.56] I mean, it's not a, not a new problem.
[5381.92 → 5387.80] Anyone who's been raid and resilvering has figured it out, but it just in the scope of
[5387.80 → 5391.72] our distributed it at any moment, anything can disappear.
[5392.38 → 5393.34] Everything can disappear.
[5393.34 → 5395.42] And then the power can go out and all that.
[5397.34 → 5400.44] That was certainly a challenging piece of work.
[5400.44 → 5403.66] And, and that was, I mean, that was something that came together like relative, I mean,
[5403.68 → 5406.64] that was, that came together in come together.
[5406.72 → 5409.18] I think I said that early 23, early last year.
[5409.26 → 5410.44] Am I, am I remembering that correctly?
[5410.50 → 5411.34] Maybe it was late 2022.
[5412.36 → 5413.74] Yeah, I think it was early 2023.
[5413.74 → 5421.76] But one of those things that was required to ship that we, and I mean, so much was required.
[5421.92 → 5425.72] We had to run the table on, on so many things because this is the kind of thing.
[5425.76 → 5429.40] I mean, we say this about like all sorts of aspects of the system, but if this doesn't
[5429.40 → 5430.80] work, you don't have a product.
[5431.62 → 5431.98] Yeah.
[5431.98 → 5437.16] Like, like you need this startup to actually, this startup within the startup has to actually
[5437.16 → 5437.66] nail it.
[5438.20 → 5440.84] Like every other startup within the startup.
[5441.18 → 5442.34] Oh, I mean, I don't know.
[5442.34 → 5446.92] I think pretty much everybody is working on some piece that is completely, totally required.
[5447.40 → 5451.14] But it's not like anybody else wasn't working on something that was also critical.
[5451.24 → 5455.58] But yeah, this was another of the 55 pieces that had to absolutely work.
[5455.66 → 5456.48] This was one of them.
[5457.32 → 5460.44] I was like, as I told people to shift the rack, like if you, if you have the feeling like,
[5460.58 → 5462.24] boy, what were they going to do without me?
[5463.24 → 5464.26] They would have been screwed.
[5464.34 → 5465.32] It's like, yes, we would have been screwed.
[5465.58 → 5471.46] And we definitely would have been screwed without, without all of you, without, and all of the
[5471.46 → 5473.94] the hard work that went into all aspects of this.
[5474.80 → 5480.04] And it's been, I actually described also, when did we open up a crucible?
[5480.22 → 5481.14] When did that happen?
[5482.76 → 5484.38] Because this is all open source, which should be said.
[5484.50 → 5484.62] Yeah.
[5484.86 → 5486.02] So folks can go to kind of check out the repo.
[5486.26 → 5491.46] And it might, I may be misremembering, but I think this is one of those that we open
[5491.46 → 5492.68] sourced out of convenience.
[5493.88 → 5495.50] Like it was, I don't know.
[5495.68 → 5496.28] It was sort of a pain in the neck.
[5496.90 → 5499.42] Well, can you, can you, it might have been a pain in the neck.
[5499.62 → 5504.46] We open source propolis because Patrick was interviewing a candidate and wanted to be
[5504.46 → 5505.22] able to talk about it.
[5505.24 → 5507.98] It's like, I want to be able to talk about propolis in 45 minutes.
[5508.04 → 5508.82] So can we open it?
[5508.94 → 5510.56] I'm like, sure.
[5510.56 → 5514.02] We open source crucible because we use it as a dependency in propolis.
[5514.18 → 5514.50] That's right.
[5514.50 → 5515.68] And it's easier to use a Git dependency.
[5516.62 → 5516.92] That's right.
[5516.92 → 5519.64] It was, it was purely the convenience of Git dependencies.
[5520.70 → 5521.02] Yeah.
[5521.48 → 5522.72] 75% of it at least.
[5522.88 → 5523.10] Yeah.
[5523.12 → 5526.44] It is a real pain in the butt to have things that are like, some things are public and some
[5526.44 → 5526.98] things that are private.
[5527.10 → 5531.20] So yeah, I think we, that is, that is plenty of the things we've opened up in because of
[5531.20 → 5531.44] that.
[5531.92 → 5532.16] Yeah.
[5533.60 → 5539.30] And so we, so we got that out there, I guess a while ago, but folks can go check that out
[5539.30 → 5539.70] as well.
[5540.34 → 5545.36] I'm not, I'm not sure how readily deployable it will be.
[5545.36 → 5549.00] There are like plenty of, of dependent, but honestly it's a it's a pretty well contained
[5549.00 → 5549.76] unit too.
[5549.92 → 5550.74] So it does, actually.
[5551.30 → 5551.42] Yeah.
[5551.42 → 5557.56] I mean, I, I develop on a Mac and I run it locally on my Mac just for itself and it, you
[5557.56 → 5558.50] know, it compiles there.
[5559.60 → 5563.74] Um, and I know like Artemis and I have been doing a bunch, I mean, we were both going in
[5563.74 → 5568.06] to do, um, some of that early performance work and kind of going into a foreign source
[5568.06 → 5568.36] space.
[5568.36 → 5573.22] And it was, it was good to be able to, uh, I mean, the source space itself was very approachable.
[5573.22 → 5578.54] I got to say very, it did not feel, you know, complicated systems can be very complicated,
[5578.54 → 5583.14] but, um, you know, it was always pretty clean to figure out what was going on here.
[5583.14 → 5589.84] And, and I think clean before and after the big, the, the great refactor, um, uh, which
[5589.84 → 5594.02] is, um, made it easy to add, to kind of add people to the source space as well.
[5594.28 → 5594.60] Right.
[5594.60 → 5598.58] Um, so what's the future?
[5598.76 → 5600.38] I mean, we got, I think it's done, right?
[5600.44 → 5601.68] We're on the, on the things.
[5601.88 → 5602.20] I'm sure.
[5603.50 → 5606.54] I mean, you're the you're the boss.
[5606.86 → 5609.96] So I, I noticed you like practically muted yourself.
[5610.06 → 5612.64] I actually fell forward.
[5613.04 → 5614.40] Did you fall forward laughing?
[5614.68 → 5616.98] You, you, you meant you replied when you said that Josh.
[5616.98 → 5618.58] I'm trying to contain myself and apologize.
[5618.58 → 5619.02] Right.
[5620.64 → 5621.00] Right.
[5621.08 → 5626.86] Well, uh, I mean, we still, I mean, there is, uh, and James, I know you alluded to some
[5626.86 → 5630.22] of the future work, but there is, there is always so much to be done.
[5630.24 → 5633.56] I mean, I think we've got, we, we, we have what we needed certainly to ship, and we've got
[5633.56 → 5633.66] it.
[5634.12 → 5638.78] Thanks to Matt, your work we've got, uh, and everyone's really, we've got a, a system that
[5638.78 → 5640.38] is kind of performing better every day.
[5640.38 → 5644.92] Um, and it's been fun to deliver upgrades to customers and just like, Hey, your short performance
[5644.92 → 5645.86] is just getting better.
[5645.86 → 5648.34] Um, it's, it's pretty exhilarating.
[5648.72 → 5650.18] Um, and you still get your data.
[5652.50 → 5652.86] Yeah.
[5653.08 → 5653.48] Yeah.
[5654.18 → 5654.96] What a bonus.
[5655.10 → 5655.96] Your data is still here.
[5656.68 → 5662.28] Um, so I think it's been really, I broadly, I feel it's been really successful.
[5662.28 → 5664.34] We've been able to do exactly what we wanted to go do.
[5664.94 → 5668.28] Um, and I think we've got a great foundation to go, to go build upon because we're going
[5668.28 → 5672.88] to have, we're going to be building upon this foundation in crucible or ever effectively.
[5672.88 → 5679.18] Um, and we, this, this is going to be the way, you know, when, when our VMs are deployed,
[5679.24 → 5682.36] like this is where the root file system is going to come from, and it's got to be exactly
[5682.36 → 5682.80] correct.
[5682.88 → 5685.64] And I think I'm really terrific job on it.
[5685.72 → 5686.32] It's been fun.
[5687.40 → 5691.94] No, I'd say it's, I think storage is one of these things like there will be no end,
[5691.94 → 5697.42] but there's always, not just on the current iteration, but like there's, you know, every
[5697.42 → 5704.34] new customer requirement, every new workload creates like some whole new, uh, sub-branch
[5704.34 → 5707.96] of either how we're thinking about the current system or plans for the next system.
[5707.96 → 5714.82] So, um, I mean, James, Alan, Matt, this is not to say you're last to the mass forever,
[5714.82 → 5716.26] but just as long as you want to be.
[5718.40 → 5720.16] Um, you got plenty of work to do.
[5720.24 → 5720.80] That's for sure.
[5720.80 → 5721.06] Yeah.
[5721.44 → 5721.64] Yeah.
[5721.70 → 5721.88] Yeah.
[5722.48 → 5727.52] Uh, Alan, any, uh, any, any closing thoughts on James, Matt?
[5728.28 → 5733.22] It's been a great, it's been a great whole team to work with and the company, you know,
[5734.04 → 5734.78] having a blast.
[5735.80 → 5736.20] Yeah.
[5736.20 → 5741.30] I could not have picked a better, you know, multi, many thousand lines of code base to be
[5741.30 → 5742.64] plunged into on short notice.
[5742.72 → 5743.18] It was great.
[5744.52 → 5747.44] You all sound like you're speaking under duress.
[5747.90 → 5748.50] You know, I'd like to.
[5748.50 → 5752.10] Josh, do you have anything you'd like to say now that you've heard that?
[5752.10 → 5753.50] I'm actually blinking.
[5754.08 → 5754.56] Exactly.
[5754.82 → 5757.00] A prime number of times now to communicate.
[5757.30 → 5759.36] Could you please read your prepared statement that I've asked you to give?
[5760.18 → 5760.36] Yeah.
[5760.62 → 5762.40] This team is the no.
[5763.08 → 5763.52] Exactly.
[5764.38 → 5764.66] And fun.
[5765.72 → 5767.40] It's been fun getting better every day.
[5767.66 → 5772.26] Um, and I definitely welcome folks to check out the RFDs, learn more about.
[5772.44 → 5778.34] I will, I will say that it, it, uh, I think like if you think about crucible as a narrative
[5778.34 → 5782.06] arc, like really one of the most important things we did was hiring.
[5783.06 → 5783.46] Yes.
[5783.48 → 5787.92] Which I think is like always the most important thing we did, but like, but like it really,
[5787.92 → 5792.98] I think needs to be emphasized that like, you know, when, when Alan came on and then
[5792.98 → 5798.84] James, like we, as Alan noted, we're doing six other things, and it was really not the
[5798.84 → 5804.40] focus and was not going to happen without some people for whom it was more a dedicated
[5804.40 → 5804.82] focus.
[5804.82 → 5811.54] And, and we did extremely well pick, uh, we were very fortunate to have Alan and James
[5811.54 → 5813.66] lash themselves to the mast.
[5814.20 → 5816.50] Well, I think a testament to that.
[5816.68 → 5820.22] And I also do think, and you kind of have heard it kind of heard us weave it in here,
[5820.22 → 5821.88] but it's been a big testament to Russ too.
[5821.88 → 5826.64] Because I think it's been the fact that we've been able, I mean, to have Matt join the code
[5826.64 → 5830.34] base, you know, relatively late in its life after we, after we deployed it to our first
[5830.34 → 5835.42] customers and be able to like really, uh, do some pretty serious robocaller.
[5836.00 → 5840.40] Some of our early shenanigans, he was able to come in and clean up a lot.
[5840.44 → 5843.54] It's like an adult showed up and put everything in order.
[5843.80 → 5847.94] And like, well, I think, but also where you can, you know, have someone come in with,
[5847.94 → 5853.58] with, you know, a coming from a kind of different, uh, different code base and be
[5853.58 → 5858.24] able to bring like a bunch of greats, I mean, we, our ability to, to, to leverage rust across
[5858.24 → 5862.60] many different systems, across propolis, across Omicron, across crucible.
[5862.96 → 5866.38] I mean, it has been, I think really across hubris for that matter.
[5866.70 → 5869.96] And we all talk to each other, and we're all like, oh, wait a minute, I'm doing this.
[5869.96 → 5873.12] And this is, this is working perfect, or it's not working perfect.
[5873.52 → 5875.68] Then everyone else is like, oh, I'm going to do that.
[5875.68 → 5879.64] Or I'm not going to do that or like that, I could share it all around.
[5879.86 → 5884.44] So it's been, it's been a really important element, I think of crucible success.
[5886.38 → 5887.38] The great work, everyone.
[5887.48 → 5888.04] It's been fun.
[5888.54 → 5892.30] Um, and, and thanks folks for, for prodding us to do this episode with us.
[5892.30 → 5895.18] It's been, it's been, uh, way too long in coming.
[5895.50 → 5900.54] Um, so, um, thank you very much for, for encouraging us.
[5900.58 → 5902.22] We got, we're going to have a lot more of these.
[5902.22 → 5905.82] I think we'll probably have, I have to do some crucible follow-ons at some point as well.
[5905.98 → 5912.48] But, um, Alan, James, Matt, Josh, of course, and Adam, I guess, Adam, I do have to thank you for joining us.
[5912.54 → 5913.28] I mean, you kind of did.
[5913.48 → 5914.62] Nah, I would have been here anyway.
[5914.88 → 5915.32] Yeah, thanks.
[5915.46 → 5916.68] So, all right.
[5916.80 → 5917.42] Thanks everyone.
[5917.60 → 5918.90] I will talk to you next time.
[5918.90 → 5918.94] Bye.
[5918.94 → 5918.98] Bye.
[5918.98 → 5919.02] Bye.
[5919.02 → 5919.06] Bye.
[5919.06 → 5919.10] Bye.
[5919.10 → 5919.14] Bye.
[5919.14 → 5919.18] Bye.
[5919.18 → 5919.20] Bye.
[5919.20 → 5919.24] Bye.
[5919.24 → 5919.26] Bye.
[5919.26 → 5919.28] Bye.
[5919.28 → 5919.30] Bye.
[5919.30 → 5919.34] Bye.
[5919.34 → 5919.44] Bye.
[5919.44 → 5919.46] Bye.
[5919.46 → 5919.50] Bye.
[5919.50 → 5919.54] Bye.
[5919.54 → 5919.56] Bye.
[5919.56 → 5919.60] Bye.
[5919.60 → 5920.10] Bye.
[5920.10 → 5920.14] Bye.
[5920.14 → 5920.16] Bye.
[5920.16 → 5920.18] Bye.
[5920.18 → 5921.18] Bye.
[5921.18 → 5922.18] Bye.
[5922.18 → 5922.24] Bye.
[5922.24 → 5922.26] Bye.
[5922.26 → 5923.18] Bye.
