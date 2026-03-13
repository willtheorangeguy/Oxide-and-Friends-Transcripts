[0.00 → 0.62] Dave's here.
[1.18 → 1.66] Dave's here.
[2.32 → 2.60] Hello.
[3.22 → 3.72] I'm back.
[4.38 → 5.02] You're back.
[5.90 → 9.40] Back to back on the podcast here, Dave.
[9.76 → 10.38] It's exciting.
[10.58 → 11.04] It's an honour.
[12.28 → 14.56] The honour is all ours, Brent.
[16.50 → 18.98] Although this one, I think it's fair to say this one,
[19.82 → 23.14] we said we'd been talking about our episode on sagas.
[23.22 → 25.42] We've been thinking about it for a long time, Adam.
[25.96 → 26.50] Yes, true.
[26.50 → 31.58] This one, a little more getting back into our groove.
[32.30 → 34.88] Not planning more than a week in advance, for sure.
[34.88 → 35.22] That's right.
[35.50 → 36.78] This is the hurry-up offence.
[37.50 → 39.04] This is the no huddle.
[39.30 → 42.16] This is the run and gun that Oxide and Friends is famous for.
[44.08 → 46.64] I also loved the comment.
[46.92 → 48.74] There was a comment from last week's episode.
[48.88 → 50.98] It's like, hey, I'm really glad to see that Oxide and Friends
[50.98 → 54.56] is back into the groove of not telling me what this thing is about
[54.56 → 55.74] for the first 17 minutes.
[55.74 → 59.34] That was just building suspense.
[59.54 → 63.60] We did mention what it was about.
[63.86 → 64.26] We did.
[65.28 → 67.40] In honour of re-listen, I definitely had some,
[67.54 → 70.86] hey, read the tweet, fellas, got vibes on that one.
[70.96 → 72.66] I felt like, hey, could someone define where the saga is?
[72.70 → 73.64] Fortunately, we did, but it was good.
[73.64 → 75.42] We're building to it.
[75.54 → 77.32] You got a sense of storytelling.
[78.32 → 78.76] Exactly.
[78.90 → 81.10] You can't just rush in and say what we're talking about.
[81.10 → 83.52] That would be far too orienting.
[83.52 → 90.82] So on this, to give the context,
[91.82 → 93.92] we are users of Cockroach TV.
[93.92 → 104.36] So one of the first things that we did early on in the company is we knew we were obviously
[104.36 → 105.12] building a control plate.
[105.24 → 107.10] We wanted to have a data repository for that.
[107.76 → 109.66] And we embarked on an entire process.
[109.78 → 114.66] Dave embarked on our process, led the charge on evaluating different options for that.
[114.66 → 118.32] And we decided on Cockroach TV, and for a bunch of reasons.
[119.68 → 123.84] And we haven't really talked about it much, I don't think.
[124.50 → 127.96] I mean, I think the most we've talked about it, and correct me if I'm wrong, but I think,
[128.08 → 131.76] Dave, the most we've talked about it is in your Debugging Odyssey episode.
[133.10 → 134.36] Yeah, I think that's probably right.
[134.36 → 139.24] And I don't know that we've talked about it publicly very much, because just based on the
[139.24 → 142.20] number of RFDs we made public for this.
[142.46 → 145.48] So we hadn't talked about it very much, but not deliberately.
[145.66 → 148.28] I mean, it's not that we were, you know, we had mentioned it, obviously.
[148.28 → 156.88] And, but then fate kind of forced our hand, because Cockroach Labs, which famously or
[156.88 → 164.52] infamously had taken an open source project and started to relicense aspects of it under
[164.52 → 170.04] the BASIL, the business source license, decided that they were going to go all proprietary
[170.04 → 173.68] on Thursday morning, right, Dave?
[173.76 → 174.36] I think it was.
[175.30 → 176.20] Yeah, that's great.
[176.20 → 189.46] So, we, obviously, this is an issue of great interest for us, and I had a conversation about
[189.46 → 196.70] it, obviously, on Thursday morning, and then I wrote up an RFD that we made public on Friday
[196.70 → 202.46] morning, and included in that, Dave, we made public all the RFDs that you've done, 53,
[202.46 → 207.92] 1.10, and then your Cockroach Evaluation repo.
[208.88 → 212.88] That kind of took people through the entire process of why we decided what we decided, and
[212.88 → 220.50] then also what we were deciding to do with the move to a strictly proprietary Cockroach DB
[220.50 → 222.38] in RFD 508.
[222.38 → 231.76] And I mean, obviously, it's like, you know, we are a podcasting company that LARP's as
[231.76 → 232.40] a computer company.
[232.50 → 234.06] Did you see that Hacker News comment over the weekend?
[234.40 → 235.38] I did, actually.
[236.18 → 236.72] Good for them.
[236.98 → 239.64] I mean, it is our show, but like...
[239.64 → 241.30] First, I lulled at that.
[241.48 → 242.68] I thought that was a funny comment.
[243.18 → 244.72] I thought that was a very funny comment.
[244.84 → 247.22] It was on the Hacker News thread about this.
[247.84 → 250.50] Or maybe it was on the Hacker News thread, actually, about the RFD.
[250.62 → 251.92] Anyway, I thought it was very funny.
[252.70 → 255.62] One of our defenders was...
[255.62 → 260.24] Which I totally admire, was calling him out on it, but whatever it's worth, I lulled.
[260.38 → 260.76] I thought it was funny.
[263.60 → 264.34] But that's it.
[264.40 → 267.08] I think that our defenders probably, right?
[267.22 → 268.44] This is someone...
[268.44 → 269.94] It's probably one of our detractors.
[270.18 → 271.48] One of the members of the Hacker's Club.
[271.56 → 271.76] Who knows?
[272.98 → 275.64] But we got the RFD out there.
[275.64 → 278.44] But the RFD got more attention than I actually thought it was going to.
[279.24 → 280.34] Is that naive?
[281.62 → 281.98] No.
[282.14 → 289.14] I mean, assisted in no small part by friend of the pod, Kelsey Hightower, who had just such
[289.14 → 292.82] a delightful repost of what you had done.
[293.28 → 297.28] Like, you know, quote, tweet, you know, with just keeping praise.
[297.36 → 298.26] Like, almost too much praise.
[298.38 → 298.96] Like, suspicious.
[300.00 → 301.34] I feel that you were suspicious.
[301.34 → 305.36] I feel like your first thought was, Brian has hacked Kelsey's account.
[305.64 → 308.62] I'd like to expand it to see if it was like a place to have a pest.
[308.62 → 310.18] Logged in around the Oxide office.
[310.70 → 318.40] And that little mischief-maker has gone in and tweeted out that it was very fulsome praise
[318.40 → 318.80] from Kelsey.
[318.90 → 321.24] Really, I mean, honestly, it's like...
[321.24 → 324.24] And obviously, you know, you always are...
[324.24 → 327.88] It's always very meaningful to get earnest praise from people that you hold in high regard.
[327.88 → 329.76] And obviously, we hold the Kelsey in the highest regard.
[329.76 → 332.06] And that was really...
[332.06 → 333.20] It was really unexpected.
[333.44 → 336.68] It was delightful, but very unexpected to get.
[337.00 → 340.76] And I think also, I mean, it...
[340.76 → 343.04] RFT 508 is...
[343.04 → 346.22] You know, I think it did a good job of kind of explaining our options there and our decision.
[346.22 → 350.56] But I actually think that the bigger piece of this...
[350.56 → 356.24] I mean, obviously, the bigger piece of this is, Dave, the work that you had done in 53,
[356.64 → 362.20] RFT 53 to define the rubric, and RFT 110 to describe why we selected Cockroach DB.
[363.34 → 365.56] So I do want to hit on all of that.
[365.56 → 368.56] I feel that...
[369.28 → 374.84] I mean, I don't want to, like, overly fixate on the action of Cockroach Labs here, but
[374.84 → 378.64] I also feel that I would be not being true to myself.
[378.78 → 379.36] I actually...
[379.36 → 380.68] And Adam, there was one comment online.
[380.72 → 383.94] It's like, oh, I love this RFT because, like, you know, there's no, like...
[383.94 → 385.06] You know, there...
[385.06 → 385.82] What was the line?
[385.90 → 388.04] There was, you know, no tearing of the garments.
[388.38 → 389.28] The rending of the garments.
[389.52 → 389.90] That's right.
[389.98 → 392.02] And you're like, yeah, well, tune into the podcast.
[392.02 → 399.08] Yeah, I mean, but does it make sense to sort of go into the time machine and, like, dial
[399.08 → 401.42] it back to whenever it was 2020?
[401.96 → 403.22] I do want to go into the time machine.
[403.34 → 405.92] I think before we go into the time machine, we...
[405.92 → 407.94] I just want to get it out a little bit.
[409.56 → 410.98] I know this is where...
[410.98 → 414.40] It's like, this is Odysseus being asked to be tied to the mast here.
[414.52 → 415.86] Or you're like, okay, now untie me.
[415.92 → 417.58] I know all those things I said about the mast.
[417.66 → 418.22] Now untie me.
[420.22 → 421.22] Just so...
[421.22 → 423.84] Because I do think that, I mean...
[423.84 → 428.60] And I described this, you know, and I had a P99 Cone talk that we then had a podcast
[428.60 → 433.22] episode on of the kind of the update to corporate open source antipatterns.
[433.68 → 437.84] And, you know, I re-listened to that talk over the weekend just to kind of remind myself
[437.84 → 442.92] what I had said because we did call out cockroach there positively for the business source
[442.92 → 447.02] license, the way that they defined it being relatively crisp.
[447.16 → 448.60] Or crisp, actually, not even relatively crisp.
[448.84 → 449.40] Like, crisp.
[449.40 → 458.86] I do think that the concern on all of these re-licensing, and this one also, is not the...
[458.86 → 461.48] Cockroach has the indisputable right to do it.
[461.96 → 466.12] And, you know, certainly we want them to have a thriving business, and they've got a right
[466.12 → 466.30] to do it.
[466.72 → 467.86] So I definitely understand that.
[468.24 → 470.48] I think that you always have to be mindful of social contracts.
[470.62 → 473.40] So that's kind of the question is like, where are the social contracts here?
[473.40 → 476.02] And I don't think they've got much of a social contract with Oxide.
[476.14 → 476.86] I think they've got...
[476.86 → 477.60] Because...
[477.60 → 481.00] And Dave, you've talked about this a lot just internally.
[481.24 → 482.86] But like, they delivered a...
[483.62 → 487.24] They have developed an engineering artifact, a software artifact.
[487.66 → 488.84] It's been perfect.
[489.18 → 491.84] And they definitely don't owe us things.
[491.98 → 494.86] So I think that the social contract with Oxide and with other...
[494.86 → 496.66] Is pretty minimal.
[497.10 → 502.30] I think there's some other social contracts here that are probably more important that I
[502.30 → 503.08] can't really speak to.
[503.30 → 504.56] So, I mean, it's like...
[504.56 → 507.58] In particular, I do think like the most important social contract.
[507.74 → 512.14] And maybe the answer is just like, there's no one in this category but are contributors
[512.14 → 514.38] to Cockroach DB.
[514.98 → 515.66] Those are...
[515.66 → 520.50] Outside contributors, Cockroach DB is in many ways the most important social constituency here
[520.50 → 527.08] because their work was made available under one set of terms, and now it's being made
[527.08 → 527.84] strictly by Jerry.
[528.30 → 528.38] Yeah.
[528.38 → 533.42] I think there's another question it raises about what the direction of the company is.
[533.48 → 534.22] Like, who is the company?
[534.92 → 540.48] And this is not to answer for other people with regard to Cockroach Labs.
[540.62 → 544.16] But what does it say to us, and how does it affect our use of it?
[544.88 → 550.96] And in particular, in this case for us, some of the terms around it like unlocking at 10
[550.96 → 557.04] million ARR and some stuff like that just was signalling in such a way that, to me at least,
[557.10 → 563.70] indicated a potential of future greater incompatibility between values or between our use case and
[563.70 → 564.32] what they intended.
[565.32 → 565.38] Yeah.
[565.50 → 566.36] That's a good point, Adam.
[566.42 → 567.06] And I do think...
[567.06 → 570.36] So, something to elaborate on before we step into the time machine because we talked about
[570.36 → 571.62] like, you know, would we...
[571.62 → 574.80] Let's take a look at, you know, what's kind of available.
[574.80 → 581.24] And they do have a source available Cockroach DB that is not licensed.
[581.56 → 588.00] But there are two requirements on there that you mentioned the $10 million of annual revenue
[588.00 → 590.74] that you have to be less than $10 million of annual revenue.
[590.90 → 593.96] And then also you have to have mandatory enabled telemetry.
[593.96 → 597.64] And that's an absolute non-starter for us.
[597.96 → 604.58] Like, 100% non-starter because we, our customers are deploying in potentially air-gapped secure
[604.58 → 605.08] facilities.
[605.30 → 607.14] It's like, that's a hard nope.
[607.88 → 609.80] Like, we don't even get telemetry from our customers.
[609.84 → 611.10] We don't get telemetry from our customers.
[611.22 → 611.44] Exactly.
[611.70 → 615.06] So, like, you definitely don't get telemetry.
[615.14 → 615.34] Sorry.
[617.02 → 619.10] So, it's like, okay, then why not license it?
[619.24 → 622.14] And I think that, you know, a question that came up online is like, all right, so just like
[622.14 → 622.84] license the thing.
[622.84 → 628.42] And we cannot encumber this product at all from a software perspective.
[629.38 → 638.12] So, every bit of software that we have in this product, we have to have a perpetual royalty-free
[638.12 → 638.70] license for.
[639.90 → 646.20] And it's not impossible that you can negotiate that with Cockroach Labs, but it's, yeah, I
[646.20 → 650.62] would say it's, it would get them, I would say, out of their sweet spot and probably out
[650.62 → 651.34] of where they want to be.
[651.34 → 652.84] I think it's impossible.
[653.02 → 657.04] I think it's impossible in terms of like, there's just too big of a gap between what
[657.04 → 661.62] we would conceivably pay and what would make sense for them to bother doing.
[661.80 → 665.80] Like, and we just, like, I don't think it's a use case that they particularly care about,
[665.84 → 665.98] right?
[665.98 → 667.64] It's not what they're trying to preclude.
[667.74 → 668.98] It's not what they're trying to enable.
[669.34 → 670.34] It's not big bucks for them.
[670.34 → 671.08] Or should care about.
[671.30 → 675.66] Like, this is like, don't, like, please let us be in our own filth here.
[675.74 → 676.42] You do not want to.
[677.08 → 678.96] Well, we've got other, like, aspects of the problem.
[679.14 → 683.82] Like, so we are, I mean, our software is going to go out to a customer, and it's going to run
[683.82 → 685.02] for potentially a long time.
[685.22 → 687.92] And we can't make real guarantees.
[688.10 → 691.80] Like, that can be pretty down rev with respect to Cockroach TV.
[691.80 → 697.28] Um, and so you can't really tell us like, oh, by the way, this is out of the support
[697.28 → 697.60] window.
[697.60 → 699.30] It's like, uh, sorry.
[699.68 → 700.66] Bad news on that.
[701.42 → 704.66] Um, like the and so just a bunch of other things, like we're going to take you out of
[704.66 → 705.14] your sweet spot.
[705.24 → 710.04] So, um, we're not, um, almost, it does not make sense, but we, it's, it's very important
[710.04 → 715.66] for us because we need to make sure that one, we take the responsibility for being able to,
[715.66 → 719.24] uh, understand any misbehaviour on the rack.
[719.24 → 724.36] Um, but then also it's really important because we need to have control over our own pricing
[724.36 → 728.28] and we need to make sure that we are a big part of the oxide value is all the software
[728.28 → 728.78] that's built in.
[728.94 → 735.50] So that's why all that, that's kind of why that's a, a non-starter, um, kind of where
[735.50 → 736.64] we, where we landed on that.
[736.96 → 740.32] Um, but, uh, so that, I think we can step into the time machine.
[740.32 → 740.84] There we go.
[741.56 → 742.92] I think, yeah, exactly.
[743.08 → 747.52] Now I've been, I've been coaxed in a lot, like the April off, I've been drugged into the
[747.52 → 747.84] plane.
[747.98 → 748.46] Yeah, right.
[748.46 → 748.90] Exactly.
[749.02 → 749.60] We ran into the garments.
[750.20 → 759.58] Um, so Dave, um, when you, so we, I think it is worth, so there are a couple of reactions
[759.58 → 760.00] online.
[760.08 → 761.76] I don't know, Dave, how much you were looking at this.
[762.50 → 766.86] Um, there is definitely a why didn't they just use Postgres?
[768.08 → 769.04] Uh, really?
[769.14 → 770.48] I hadn't quite seen that.
[770.84 → 771.24] Yeah.
[771.24 → 772.20] I kind of figured you hadn't.
[773.44 → 777.74] You're like blind siding with this is, this is, no, no, no.
[777.74 → 782.00] It dovetails into a question that Dave had asked the two of us, Adam, which is like,
[782.00 → 784.70] may I spend the first 45 minutes talking about Postgres?
[784.98 → 786.16] I think I said 90 minutes.
[786.24 → 787.70] You said 90 minutes for sure.
[787.70 → 788.08] Right.
[788.18 → 789.18] You said 90 minutes.
[789.18 → 791.58] Uh, yeah.
[791.62 → 795.62] And Adam's like, of course, because Brian thinks that 90 minutes is 45 minutes.
[795.62 → 799.96] This is why I've got so many domestic problems because I've got, this is why it's all like
[799.96 → 801.38] I promise everyone it's right.
[801.44 → 802.24] It's all making sense.
[802.56 → 804.56] Brian thinks this podcast is 45 minutes long.
[804.72 → 805.60] That's the problem.
[805.80 → 806.80] I think we actually found it.
[807.42 → 816.30] Um, so I mean, Dave, I think it is worth talking about, um, why our experiences with Postgres,
[816.30 → 823.58] um, and you've got, I mean, a line in RFD 53 that is, uh, well, you've got the there are
[823.58 → 828.70] some, whatever a subtweet is when it exists as a line in an RFD, um, about Postgres, but
[828.70 → 833.22] you want to talk about our experience with Postgres a little bit, um, and, uh, positives and,
[833.22 → 834.60] uh, findings.
[836.82 → 837.22] Yeah.
[837.22 → 839.38] This is your experience at joint.
[839.94 → 840.56] That's right.
[840.56 → 841.20] Yeah.
[841.20 → 841.52] Yeah.
[841.64 → 847.84] And so how far back in the time machine we want to go, but I want to give at least a
[847.84 → 848.62] little bit of context.
[848.62 → 853.10] So certainly the whole process of figuring out what we were going to use for the database
[853.10 → 860.12] here was heavily informed by having just previously come off of several years fighting, spent most
[860.12 → 864.88] of that time fighting issues, productionizing Postgres databases.
[865.10 → 869.92] If I get interactive, like every time I would go over to your office.
[869.92 → 872.56] For lunch with Brian, no joke.
[872.80 → 875.12] You'd be in some Postgres firefight.
[876.22 → 879.30] And it just, that's every time I would come to lunch every day.
[879.44 → 880.30] It would have been, I mean, yeah.
[880.94 → 881.30] Okay.
[881.44 → 881.62] Yeah.
[881.66 → 881.78] Good.
[881.86 → 884.88] I just, every time I visited you guys in your office, you were in your office.
[885.02 → 885.74] Like, uh, yes.
[886.12 → 886.40] Yeah.
[886.58 → 886.74] It was.
[886.96 → 887.22] Yeah.
[887.22 → 887.60] Yes.
[887.60 → 889.52] We were doing the work that we do every day.
[889.58 → 890.32] That's what, anyway.
[890.36 → 890.52] Yeah.
[890.52 → 891.32] That's what we were doing.
[891.48 → 893.68] I mean, yeah, there was a lot of that.
[893.94 → 894.60] So, okay.
[894.60 → 899.86] So this started, you know, at back at joint, we built a system called Manta, which,
[900.08 → 904.98] um, the sort of short version of it is it's very similar to Amazon S3 in spirit.
[905.16 → 909.60] It's an HTTP object store, you know, put, get, delete of large blobs.
[910.06 → 913.74] And, um, some things that were different that are, that turned out to be pretty relevant
[913.74 → 917.66] for many reasons are that it was strongly consistent at a time when S3 wasn't.
[918.08 → 921.68] So if you put something into Manta, you would get it back out, which required a strongly
[921.68 → 923.82] consistent metadata tier that we'll get to in a second.
[923.82 → 929.86] And it also imposed a directory structure so that you could list the contents of things
[929.86 → 931.34] efficiently, essentially.
[931.98 → 935.46] And so this thing, you know, implement, I'm going superfast, but the implementation is
[935.46 → 937.96] basically divided into storage and metadata, right?
[938.00 → 942.60] The storage is durably storing these large blobs of data, which you would not use something
[942.60 → 943.40] like Postgres for.
[943.40 → 949.36] And then metadata is this gigantic database mapping user facing names to the underlying
[949.36 → 952.62] storage objects that, uh, that contain that data.
[952.62 → 953.00] Right.
[953.24 → 954.98] And of course it's a cloud service.
[954.98 → 956.08] So we need high availability.
[956.30 → 957.74] How do we build high availability?
[958.10 → 960.32] Um, well, let me get back to that.
[960.36 → 962.24] The other thing we need is horizontal scalability.
[962.24 → 968.36] And so we ended up going with Postgres largely on the strength of its reputation around data
[968.36 → 971.14] integrity and performance and just general rigour, right?
[971.24 → 973.24] Is this that your recollection, Brian?
[974.16 → 974.44] Yeah.
[975.24 → 976.64] Uh, do I need my lawyer present?
[976.74 → 978.64] It feels like I need help just a little bit pointed.
[978.90 → 983.62] I, I, unfortunately I fired Adam as my postmortem lawyer after the last postmortem in which I
[983.62 → 984.14] was hung out.
[984.46 → 986.42] So I'm actually, I need a lawyer here.
[986.58 → 988.52] I'm going to have to go with the public defender.
[988.68 → 989.28] Actually, wait a minute.
[989.40 → 990.10] You're the public defender.
[990.60 → 991.76] I think that's right though.
[991.76 → 996.98] I mean, I think we didn't do a lot of like testing or like, I don't know how much we
[996.98 → 1000.08] did like a serious survey of alternatives, but it seemed like the thing to beat.
[1000.08 → 1003.92] I was like, well, what, what else would we use?
[1004.56 → 1006.48] It was what we did it on vibes.
[1006.98 → 1007.38] Absolutely.
[1008.22 → 1011.48] It kills me to say it, but we did it on vibes and reputation.
[1011.96 → 1015.16] Um, and we did not dig into that reputation at all.
[1015.52 → 1019.40] And I would say that's how most people make technology decisions though.
[1019.40 → 1025.74] Like it's, it's expensive or perceived as expensive to do it like a, a rigorous analysis and going
[1025.74 → 1030.84] with the consensus approach makes sense in a lot of, or in a lot of cases.
[1030.84 → 1032.26] And I mean, until it doesn't.
[1033.08 → 1033.30] Yes.
[1033.48 → 1039.10] And I feel that like, if you had frozen time and said, Hey, wait a minute, you guys are doing
[1039.10 → 1039.64] it is the wrong way.
[1039.64 → 1041.70] Like, don't you want to do something more rigorous here?
[1042.34 → 1043.10] I don't know, Dave.
[1043.54 → 1045.92] I mean, I, you, I've got way more faith in you than me.
[1046.08 → 1049.38] I, I think I would have been like, no, but like, we know all these people that are using
[1049.38 → 1049.64] it.
[1049.64 → 1052.84] Like we, and of course our kind of like, do you know it?
[1053.24 → 1053.98] Do you know it?
[1054.04 → 1054.42] Know it?
[1054.50 → 1055.92] Like, what do you know?
[1056.14 → 1057.02] What do you think you know?
[1057.44 → 1058.44] Well, what do you think you know?
[1058.50 → 1064.54] Have you, because you know, and I, I, so I think that you're right at them that this is
[1064.54 → 1067.28] the way like lots of people make, make decisions.
[1067.28 → 1073.36] And I don't know that we thought it to be as flawed as we now know it to be.
[1074.48 → 1077.38] You know, even in the end, it's, it's kind of a mixed bag.
[1077.52 → 1081.94] I mean, we made it pretty far on those, on that decision and those vibes.
[1082.32 → 1082.68] Right.
[1083.68 → 1084.34] I don't know.
[1084.48 → 1085.04] I feel like.
[1085.30 → 1087.56] I think we know.
[1087.64 → 1088.44] And I think you're right.
[1088.48 → 1092.22] And I think, I mean, I don't know that we would have come out with a different decision
[1092.22 → 1094.36] necessarily, but I think we would have been.
[1094.54 → 1097.64] Eyes much wider open about some of the perils.
[1098.38 → 1103.34] I mean, it's nice to say that when we did this again, almost 10 years later, we made a
[1103.34 → 1106.96] different, we went about the decision-making process differently, which is why we're here
[1106.96 → 1107.88] today talking about it.
[1107.94 → 1108.04] Right.
[1109.32 → 1109.84] Yes.
[1110.02 → 1118.64] And so if, if in RFD 53, you have an explicit non-requirements, so this is, people were wondering,
[1118.76 → 1122.64] it's like, well, this is kind of a loaded paragraph based on experience, the reputation of a
[1122.64 → 1127.20] system or stories about it being used by other organizations are weak data points.
[1127.64 → 1130.56] We will want to independently verify any properties we care about.
[1130.56 → 1133.62] That is a Postgres subtweet, such as it is.
[1134.72 → 1136.38] And that's more criticism of us, not Postgres.
[1136.48 → 1140.24] It's not Postgres's fault that we did not evaluate it rigorously.
[1140.24 → 1142.80] So Dave, what did we find?
[1143.00 → 1149.92] Just to give a, I mean, and you linked to the postmortem, one of the postmortems.
[1149.92 → 1150.68] Yeah.
[1151.20 → 1151.64] Yeah.
[1151.78 → 1156.36] So just to be a little tiny bit more context, you know, what we ended up doing for this
[1156.36 → 1160.44] metadata tier for high availability and horizontal scalability is sharded Postgres.
[1160.70 → 1161.02] Sharded.
[1161.50 → 1168.16] So we had in our initial production deployment, we had like three shards of Postgres and each
[1168.16 → 1171.08] of them was using synchronous replication with an async peer.
[1171.08 → 1174.18] So it was a primary, a synchronous peer, and an asynchronous peer.
[1174.76 → 1178.76] And so for the high availability part, you are using the synchronous replication and then
[1178.76 → 1181.84] you do a failover and now the former sync is now the primary.
[1182.10 → 1186.64] And then for horizontal scalability, we built this whole consistent hashing system on top
[1186.64 → 1191.90] of it that would figure out for a given user key, what shard its metadata should be on.
[1192.60 → 1196.74] But it's important to say that like that was a lot of engineering effort, like a lot.
[1196.74 → 1202.94] And we spent on Manatee, which is the component for managing the high availability and electric
[1202.94 → 1206.74] moray was the consistent hashing thing and all the stuff around setting up synchronous
[1206.74 → 1212.28] replication, which is relevant because you don't have to do, well, as we'll get to with
[1212.28 → 1216.50] Cockroach DB, like this is sort of a solved problem in more modern distributed databases.
[1216.86 → 1218.58] And that is kind of, that was an important factor.
[1219.36 → 1221.16] We didn't really want to go redo all that work.
[1222.42 → 1223.30] That's definitely right.
[1223.30 → 1227.52] I also think that, I mean, my conclusion was like Postgres is just built in an era when
[1227.52 → 1234.32] people go home at night and when, and there are lots of design decisions have been made
[1234.32 → 1238.30] in Postgres that are relying on the database, getting some breathing room at some point and
[1238.30 → 1239.20] being able to catch up.
[1239.80 → 1245.02] And we, which was fine for years for us.
[1245.20 → 1246.30] And then it was not fine.
[1246.30 → 1246.74] Yeah.
[1246.74 → 1247.18] Yeah.
[1247.18 → 1252.90] So we were in production for several years and had, we had some minor outages that were
[1252.90 → 1256.48] basically due to insufficient auto vacuum in the compute tier, which we didn't really
[1256.48 → 1259.94] talk about, but we were also using the same primitives for the compute tier.
[1260.10 → 1263.66] And we would run into these weird cases where like pathological performance, like queries
[1263.66 → 1269.92] over like literally a 10 row table would take like 70 seconds because it had all this trash
[1269.92 → 1274.46] in it that the auto vacuum hadn't cleaned up, which is like, you know, that's a whole complicated
[1274.46 → 1274.82] thing.
[1275.30 → 1277.76] And then we ended up having this six hour outage.
[1278.02 → 1280.20] I want to say July 27th.
[1280.28 → 1281.80] I don't know if I'm going to get the year right.
[1282.98 → 1283.26] Oh God.
[1283.36 → 1283.46] Yeah.
[1283.46 → 1283.82] You're right.
[1283.90 → 1284.84] It's July 27th.
[1285.08 → 1285.48] 2014.
[1286.08 → 1286.40] 2015.
[1286.58 → 1287.44] You nailed that.
[1287.60 → 1290.94] I mean, obviously this is a date, you know, it's not a good date.
[1291.46 → 1291.78] Yeah.
[1291.78 → 1292.64] It's a bad one.
[1293.14 → 1295.34] I did not have a child born on this one though.
[1296.52 → 1297.84] That one was kind of crazy.
[1297.84 → 1303.68] So this was wraparound to auto vacuum for people who may already be familiar with it, but what
[1303.68 → 1309.00] it boiled down to is it was a sort of latent bug in, I don't know, the configuration or
[1309.00 → 1314.18] the setup of the system or something that would only, you'd only experience on the 200 millionth
[1314.18 → 1316.12] transaction of the database.
[1317.04 → 1322.74] Like let that sink in for a second, because every time you hear about people debugging outages,
[1322.74 → 1324.86] it's always like, well, what changed in the last hour?
[1324.86 → 1329.68] And this is always my canonical example of like, yeah, the thing that changed was we ran a 200
[1329.68 → 1331.82] millionth transaction since we had more.
[1332.30 → 1334.80] It's like confetti dropped from the ceiling.
[1335.20 → 1337.36] Balloons, balloons all made of explosives.
[1338.08 → 1343.28] And the behaviour, the behaviour was hard hanged for six hours.
[1343.28 → 1348.20] Uh, and, and like, we, we don't have to go into the whole thing, but basically we had
[1348.20 → 1354.78] a, a, a, a combination of things that were taking a combination of locks that was basically
[1354.78 → 1358.82] fine most of the time, but the wraparound auto vacuum takes a particular type of lock
[1358.82 → 1361.72] and holds it for six hours, or at least in this case, it was six hours.
[1362.18 → 1366.56] And that prevented all the read locks from being tameable by anything in the system.
[1366.56 → 1368.52] And so the whole thing was basically stuck behind that.
[1368.52 → 1369.72] But, okay.
[1369.72 → 1372.90] So this was like, these were the kinds of problems we had in the early years, but they
[1372.90 → 1375.90] weren't like, I don't think they called into question, like, are we doing the wrong thing?
[1375.90 → 1379.68] They were exactly, we were kind of like, all right, these are kind of big things, but like,
[1380.30 → 1383.44] let's go spend some time understanding them and figure out how to fix that.
[1384.16 → 1384.72] I don't know.
[1384.80 → 1389.20] They weren't, this was, this is a small compared to the stuff that we ended up hitting later.
[1389.20 → 1392.62] So I was going to dive into the Samsung era.
[1393.34 → 1393.58] Yes.
[1393.58 → 1401.94] Um, so then Samsung buys joint and in part to be able to deploy several much, much larger
[1401.94 → 1407.06] mantas, they were about, um, you know, two orders of magnitude larger than our production
[1407.06 → 1409.12] one was the was sort of what we were going for.
[1409.36 → 1414.20] And unlike our production when there really were like a hundred percent duty cycle, like,
[1414.20 → 1417.50] I mean, it was like that in our production one, but it was less latency sensitive.
[1417.50 → 1424.98] Whereas, um, with what we were trying to do afterwards, it was, we are trying to do tons
[1424.98 → 1429.36] and tons of writes constantly for, you know, days, weeks, months on end.
[1429.52 → 1429.98] Yeah.
[1430.06 → 1432.98] And that's where we started running into a lot of problems.
[1432.98 → 1438.10] And we got hammered on so many fronts in terms of, um, especially synchronous replication,
[1438.10 → 1439.28] more auto vacuum.
[1439.74 → 1444.14] Uh, you know, and, and like, this is where, like, do we want to go in for 90 minutes?
[1444.14 → 1451.18] Cause like there's, we found a lot of behaviour around synchronous replication that was either
[1451.18 → 1455.92] undocumented or like very poorly documented, maybe not widely understood.
[1456.84 → 1461.44] And it just, it contributed to feeling like this thing is really hard to operationalize.
[1461.44 → 1466.04] And even though, even if you know about these things, they're very hard to work around or
[1466.04 → 1466.38] fix.
[1466.82 → 1471.64] When you have this moment where you realize like, oh God, we are pushing this harder than
[1471.64 → 1472.30] anyone else.
[1473.14 → 1473.50] Yeah.
[1473.68 → 1478.72] We, and, and be there, and to give you kind of very concrete example, I mean, Postgres
[1478.72 → 1482.80] had this idea that like, I understand where they came from, but it, you know, it feels
[1482.80 → 1487.36] like an elegant idea of like, you know, what is replication if not crash recovery?
[1487.84 → 1490.32] Like, where are we going with this exactly?
[1490.92 → 1495.52] It's like, well, it's the same logic to recover from a crash as it is to like replay a log that
[1495.52 → 1496.22] you've just been shipped.
[1496.48 → 1498.18] So let's use the same logic for that.
[1498.18 → 1502.98] And the problem is that the, the wall replay logic on the secondary is single threaded
[1502.98 → 1506.44] and the database is massively multithreaded, multi-processed.
[1506.44 → 1510.10] And it's like, okay, so if you're throwing as much work as you can at this thing, it's
[1510.10 → 1511.84] like, you obviously can't keep up.
[1511.84 → 1512.24] Right.
[1513.00 → 1519.60] And we would have replication would be like, I mean, days behind the secondary is days
[1519.60 → 1520.36] behind the primary.
[1520.36 → 1525.08] And there's no real like a blistering alarm telling you like, by the way, you think you
[1525.08 → 1530.34] have a replicated database and that is true in the most academic sense, maybe only the
[1530.34 → 1531.02] academic sense.
[1532.10 → 1536.92] Because if you lose your primary, your database is going to be down for hours and hours and
[1536.92 → 1537.52] hours and hours.
[1537.78 → 1542.78] Well, we, well, we did have takeovers that took days, days, days.
[1542.78 → 1548.26] And the thing that was really frustrating is that we, and I think this is, this is the
[1548.26 → 1553.86] part that like broke me a little bit on vibes as, as engineering methodology.
[1555.14 → 1559.88] When we talked to folks who deployed a lot of Postgres, they'd be like, oh yeah.
[1560.70 → 1561.08] What do you mean?
[1561.18 → 1561.56] Oh yeah.
[1561.60 → 1562.30] And we're like, what do you mean?
[1562.38 → 1562.76] Oh yeah.
[1562.84 → 1563.52] Like, oh yeah.
[1563.58 → 1563.74] Yeah.
[1563.74 → 1564.92] No, like this is, yeah, this is a thing.
[1565.24 → 1567.86] It's like, okay, I guess validating, but what do you mean?
[1567.92 → 1568.14] Okay.
[1568.32 → 1571.20] But, but when we talked to you before you're like, Postgres is great.
[1571.20 → 1575.90] Like I didn't hear any of these experiences, like where, you know, there's just such a
[1575.90 → 1579.38] it felt like, and I, and maybe this is overly critical, but it kind of felt like it's an
[1579.38 → 1585.54] open secret in Postgres that like, there are these ridiculously sharp edges and steep cliffs
[1585.54 → 1592.02] and they, you know, they kind of undermine the narrative of Postgres being so reliable
[1592.02 → 1593.06] so people don't talk about it.
[1593.06 → 1598.62] And then, I mean, I do remember, and you know who you are out there in the world, so I'm not
[1598.62 → 1603.78] going to name you when we were, we had someone, you know where I'm going with this, Dave, we
[1603.78 → 1607.72] had someone really pinned on this, and it's like, well, look, if you really want that,
[1607.78 → 1608.60] you need to play Oracle.
[1608.94 → 1612.64] It's like, no, that's not, no, sorry.
[1612.82 → 1616.32] That's like, no, that's not the right answer.
[1616.32 → 1624.62] Like you can't both say that this is a this is kind of a, I mean, there's this like major
[1624.62 → 1627.56] gap in, and like, I'm all for major gaps.
[1627.60 → 1629.22] It's just like, we need to be upfront about it.
[1629.26 → 1630.24] And, but that's, again, it's on us.
[1630.38 → 1631.66] We didn't do the testing.
[1631.88 → 1636.02] We didn't find those gaps until it was too late.
[1636.02 → 1637.82] Do you think those are found findable?
[1637.82 → 1641.06] So I had this sort of surreal moment.
[1641.78 → 1642.68] Yeah, go ahead, Dave.
[1643.00 → 1647.56] I had this surreal moment at one of the Postgres cones that was in San Francisco.
[1648.24 → 1653.16] I think I went with Jan and there was a talk about, about wall replication, or maybe it
[1653.16 → 1655.46] was about all the, all the different supporter kinds of replication.
[1655.78 → 1659.36] And I asked about this problem at the end, which we haven't really gone into the technical
[1659.36 → 1663.54] details of it, but it's basically, you know, you have the synchronous replication apply
[1663.54 → 1666.64] lag that just builds up, and it can't catch up because it's on, it's single threaded.
[1666.64 → 1674.38] And the speaker, like, agreed and referred me to the thing that we had built to work around
[1674.38 → 1674.98] this problem.
[1675.38 → 1678.48] Like, you should check out what the joint folks had done with the PG3 ball pit.
[1679.10 → 1681.10] You're like, I am the joint folks.
[1681.38 → 1682.04] I built that.
[1682.90 → 1686.92] I mean, I appreciate, I mean, obviously appreciate that, like, that was known and like people
[1686.92 → 1690.62] were now starting to talk about it, but it was also like, how, what?
[1691.26 → 1691.86] How is this?
[1691.86 → 1697.04] The I mean, I do think it is worth a little more texture on this problem.
[1697.16 → 1701.58] So if you set up, this was wall replication in Postgres.
[1702.30 → 1706.32] It's basically shipping the write ahead log from the primary to the secondary.
[1706.58 → 1708.02] And there are two steps there.
[1708.10 → 1712.38] One is, well, three, there's one is sending the data and there's writing it durably to
[1712.38 → 1713.16] disk and F-sync.
[1713.16 → 1716.58] And then there's actually applying that to the live database that's on the sink.
[1717.32 → 1722.48] And it's synchronous with respect to the sending and writing to disk, but not with respect to
[1722.48 → 1723.04] the application.
[1723.88 → 1728.12] And so what would happen is you would be, you would think you were synchronously replicating
[1728.12 → 1731.40] and you would be like, you would, all the data would be there technically.
[1731.40 → 1735.92] But the apply lag would, or you have what's called apply lag, which is this lag between
[1735.92 → 1739.30] what you have actually written to disk and what you've actually applied to the live database.
[1739.52 → 1742.94] But in order for that thing to become the primary, it has to have finished applying all those
[1742.94 → 1743.22] changes.
[1743.88 → 1747.12] And so when you would do a takeover, you'd be like, oh, by the way, I actually have three
[1747.12 → 1752.60] days worth of stuff to take, to catch up on that, that like, it's very easy to not know,
[1752.64 → 1754.14] like you were doing synchronous replication.
[1754.28 → 1756.04] Like, how can you have a bunch more work to do?
[1756.04 → 1759.28] And it was just accumulating it for a long time.
[1759.48 → 1765.28] We called that secret lag and then discovered many months later, something that we call double
[1765.28 → 1771.42] secret lag, which is that there's a separate process called check pointing where it takes
[1771.42 → 1776.22] whatever has been applied via the wall and like kind of serializes a snapshot of all of
[1776.22 → 1778.44] the state to disk so that it doesn't have to replay the wall again.
[1779.58 → 1783.28] But our check pointer also would start falling behind because it is also single threaded.
[1783.28 → 1789.72] And so you could be fully up-to-date on the apply lag and then restart as part of a takeover,
[1789.88 → 1791.64] but you hadn't check pointed in two days.
[1791.70 → 1793.46] And again, you have to go reapply all that stuff.
[1793.68 → 1796.76] And that, I mean, these were real gut punches each time we discovered this.
[1796.84 → 1799.20] And that one, like, there's not even a way to really monitor that.
[1799.58 → 1804.52] There's no, at least at the time, there wasn't a way to ask Postgres, how far behind were
[1804.52 → 1804.96] you on this?
[1805.02 → 1807.60] You could get it, but you had to like to run a command line thing.
[1807.66 → 1810.68] It wasn't built into any of the other monitoring tables that they have built in.
[1810.68 → 1815.50] And so it definitely felt like, I mean, I guess it felt like a couple of things.
[1815.68 → 1818.30] There weren't, there wasn't a lot of documentation around this.
[1818.54 → 1823.82] And maybe we were the first people to hit it seriously or to hit it this hard and hit these
[1823.82 → 1824.90] problems in the ways that we did.
[1825.34 → 1831.08] But the takeaway for us was certainly that it's not, I mean, you have to test it.
[1831.32 → 1832.38] That's what it boils down to.
[1832.78 → 1837.52] And you have to test it at high load, at high rate throughput, whatever it is you're trying
[1837.52 → 1841.42] to do, you have to do the fault testing under those conditions and see what happens.
[1842.56 → 1843.54] There's no substitute.
[1845.16 → 1845.98] That's exactly right.
[1846.18 → 1848.40] Like no one cares about your workload the way you do.
[1849.20 → 1850.52] And yeah, that's a better way to say it.
[1852.14 → 1859.90] We, and this is why, like, I just don't care about anecdotal information on people running
[1859.90 → 1860.22] software.
[1860.36 → 1862.14] I mean, it's like, you can kind of point you in the right direction.
[1862.14 → 1865.26] Like, okay, I'll go, you know, I'll add that to the list of things to evaluate, or I'll
[1865.26 → 1866.18] go decide that for myself.
[1866.34 → 1872.32] But even like people's good experience, I, I, I, and I know Davey and I are both scarred
[1872.32 → 1872.74] in the same way.
[1872.74 → 1874.88] Like good experiences with software.
[1875.04 → 1876.70] Don't really tell me anything bad experiences.
[1876.70 → 1879.28] I'm curious about like, that's interesting because that actually happened.
[1879.78 → 1884.08] The bad experiences are great because they give you a better sense of, of how far people
[1884.08 → 1885.54] probed and where they found the limits.
[1886.00 → 1889.02] And so, you know, if you're like, well, you hit that problem, then that means you didn't
[1889.02 → 1890.08] hit these other problems or something.
[1890.08 → 1893.44] It gives you a better sense of what was working and also obviously what wasn't.
[1894.40 → 1898.32] But yeah, when people have a good experience, it's very hard to draw conclusions about that.
[1899.24 → 1899.26] Yeah.
[1899.36 → 1902.20] And on the one hand, it felt like, you know, and you know, we got, we got Adam in the
[1902.20 → 1902.46] chat.
[1902.62 → 1906.06] He's basically blaming us for having deployed postcards and not having realized that
[1906.06 → 1907.42] that replication, AJ or Ontario.
[1907.62 → 1909.26] And it's like, don't worry, you're not the first.
[1909.36 → 1910.08] Don't be the last.
[1910.26 → 1910.52] We know.
[1911.26 → 1913.00] Could be their other Adam, not Adam, not this Adam.
[1913.46 → 1916.22] I just want to absolve myself of victim blaming you.
[1916.22 → 1918.68] I thought it was more interesting to kind of leave is open-ended.
[1919.10 → 1921.26] Or like, is Brian referring to Adam in the third person?
[1921.36 → 1921.46] No.
[1922.46 → 1926.48] The I did ask my friends at Velocity, Adam, other Adam.
[1926.98 → 1928.72] I did ask my friends at Velocity.
[1928.84 → 1930.56] I asked all of my friends at Velocity.
[1930.92 → 1933.64] And the so that I did do.
[1933.70 → 1934.86] And no, it's like, no, that's wrong.
[1935.02 → 1938.08] Actually, the conclusion I'm like, oh, you should have asked more people.
[1938.14 → 1939.28] No, wrong, wrong.
[1939.58 → 1941.04] What we should have done is tested it ourselves.
[1941.04 → 1942.60] That's what we should have done.
[1943.10 → 1949.50] And like the what my friends say at Velocity is only interested in as much as it's pointing
[1949.50 → 1954.22] us to things that, that, that actually to go verify ourselves.
[1954.48 → 1956.36] And I do not care about vibes.
[1956.56 → 1958.02] I care only about.
[1958.50 → 1965.70] So that's, I would say that, that was our disposition, Dave, coming into this of like,
[1965.70 → 1971.20] we, cause this was the other thing that there was also a little bit, I mean, this was, this
[1971.20 → 1977.90] is the, the only time I've been screamed at in my life by a, by a colleague, not a joint
[1977.90 → 1979.14] was over this issue.
[1979.74 → 1983.44] The like stress levels were like through the roof.
[1983.44 → 1986.30] People were extremely upset about this thing.
[1986.86 → 1992.94] And, you know, being told like, well, you should have done, you know, it's, it was, it
[1992.94 → 1994.82] would felt very frustrating, and it left a mark.
[1994.82 → 1997.66] Like, it's like definitely not going to do it that way.
[1997.96 → 2001.20] Um, very educational, um, in, in that regard.
[2002.36 → 2002.76] Yeah.
[2002.94 → 2007.72] So on the specific question of like, would, what about using Postgres again for something
[2007.72 → 2008.20] like this?
[2008.20 → 2013.38] I mean, it's true that a lot of this stuff has been improved and there, there's like a
[2013.50 → 2016.16] I mean, I haven't followed all the stuff in the Postgres world.
[2016.32 → 2021.26] There's logical replication now and all kinds of other stuff, but there were so many other
[2021.26 → 2028.22] ways that the, the thing, I mean, it just, it was built from an era, like you said, where
[2028.22 → 2031.12] you have downtime, where you can go do a bunch of these maintenance operations.
[2031.12 → 2036.02] And you also got like a team of DBA's that are basically monitoring this thing, or at least
[2036.02 → 2037.44] making sure that it seems healthy.
[2037.44 → 2040.60] Most of the time there's, there's vacuum.
[2040.78 → 2044.26] I mean, upgrades are offline, for example, that's not a thing you can do online.
[2044.26 → 2047.74] If you're doing replication synchronously, you couldn't, you have to update all of them
[2047.74 → 2049.54] atomically, which you can't do.
[2049.64 → 2050.68] So you have to take that down.
[2050.90 → 2055.56] The protocol is not guaranteed to be backwards compatible across major revisions.
[2055.64 → 2059.94] I mean, there's all these, and it's not to criticize Postgres for what it is.
[2059.94 → 2063.26] It's, it's, it was built in an era in which those things were a lot less important, I
[2063.26 → 2063.52] think.
[2063.76 → 2064.62] And the that's right.
[2064.90 → 2069.86] The zero downtime, you know, easy, horizontal scalability, high availability, all this stuff
[2069.86 → 2075.02] just wasn't as much of a thing, but more modern databases have been built in, you know, with
[2075.02 → 2075.94] those constraints in mind.
[2075.94 → 2078.24] And that's kind of why we started looking around more broadly.
[2079.58 → 2079.94] Yeah.
[2080.02 → 2084.00] And again, I, I'm, I think we're very happy for Postgres and we want all the success in
[2084.00 → 2084.92] the world for Postgres.
[2084.92 → 2090.34] Um, but like what I have said about C++ where it's like, I want all the success in the world
[2090.34 → 2094.36] for C++, but C++ dragged my shit into the street and lit it on fire.
[2094.36 → 2095.92] And I don't care that it was 20 years ago.
[2096.10 → 2098.50] Like I'm happy that C++ 25 years ago.
[2098.56 → 2103.28] I'm glad that C++ is like, got its, you know, has managed to straighten its life out.
[2103.36 → 2105.22] Maybe like we're not dating.
[2105.38 → 2105.74] Sorry.
[2106.42 → 2108.74] Um, so I feel the same way about Postgres.
[2108.86 → 2111.70] It's like, yeah, I'm happy for your Postgres, but nope.
[2112.06 → 2114.90] Um, we're just not, well, or, or it would be like,
[2114.92 → 2118.28] be under very, very limited conditions where I knew exactly what we're getting ourselves
[2118.28 → 2118.50] into.
[2120.14 → 2120.50] So.
[2120.86 → 2124.58] One thing that, um, I can't remember if I've like, actually, if I even talked to you about
[2124.58 → 2127.88] this, Brian, but I talked to other peers in the industry about stuff like this.
[2128.36 → 2132.20] I mean, I kind of needed to, while we were going through this is like therapy sessions,
[2132.20 → 2136.70] but people were telling me too, that like they'd used other things like Cassandra and other
[2136.70 → 2141.22] databases that also, and they were never nearly as bad as what we'd experienced, but they would
[2141.22 → 2144.86] totally start kicking off some background operation and then like go to
[2144.86 → 2146.50] hell and all kinds of horrible things would happen.
[2147.22 → 2152.80] And so that was another reason for me to feel like, okay, maybe all these databases have
[2152.80 → 2154.04] this potential in this problem.
[2154.26 → 2157.30] And then the trick is going to be figuring out where that is before it's a problem for
[2157.30 → 2157.58] us.
[2158.58 → 2159.92] And we had our own nightmare.
[2161.22 → 2168.04] We're like the, uh, so we had a wholly separate nightmare, which ultimately ended up being a
[2168.04 → 2169.00] configuration problem.
[2169.36 → 2173.28] Um, with Elijah's batch, like debugged, extraordinary.
[2173.50 → 2177.84] We, Elijah and I worked on this for a long time together, and I learned a lot about Cassandra.
[2177.98 → 2184.44] And one of the things that, you know, we had the preeminent, uh, Cassandra, uh, tuner consultant
[2184.44 → 2191.44] in, and we're looking at GC times and are, we had like GC times, freeze the world GC times
[2191.44 → 2192.62] of like 110 milliseconds.
[2192.62 → 2194.52] I'm like, well, that's got to be, I feel like that's a problem.
[2194.56 → 2195.60] He's like, actually, that's pretty good.
[2195.90 → 2197.96] I'm like, that's pretty good.
[2198.42 → 2199.48] And he's like, I know, right?
[2199.88 → 2201.56] Who would think of writing a database in Java?
[2202.42 → 2203.88] And I'm like, okay, yeah.
[2204.16 → 2204.32] Okay.
[2204.92 → 2206.34] You know, right.
[2206.66 → 2211.46] Uh, but yes, I think that there's, I just, you just realized that like the things that
[2211.46 → 2216.64] you care about in something may or may not be what the other people who are running it
[2216.64 → 2217.04] care about.
[2217.16 → 2220.02] It may not be what the people who wrote it care about.
[2220.02 → 2224.82] And that's the kind of like, you want to find that values match as much as possible.
[2227.14 → 2227.54] Totally.
[2228.82 → 2230.96] And so we get to Oxide.
[2231.36 → 2231.54] Yeah.
[2231.90 → 2236.58] We get to Oxide, and it's a new world at Oxide, and we've got a control plane that we need
[2236.58 → 2237.02] to go build.
[2237.88 → 2241.54] And it's, it's several years later in terms of like the industry development of distributed
[2241.54 → 2242.66] databases, right?
[2242.92 → 2248.68] There's this whole group of databases called New SQL based on Spanner, basically that are
[2248.68 → 2253.74] like born in the cloud era, at least some of them with hands-off operability in mind.
[2254.26 → 2261.48] And they have things like, uh, high availability, online schema changes, rolling upgrades, automatic
[2261.48 → 2266.46] sharding, online Cons, contraction and expansion, just like built in.
[2267.04 → 2267.48] Yeah.
[2267.48 → 2268.92] And it's like, that sounds pretty good.
[2268.92 → 2273.04] Let's not go rebuild all the all those things that we had to go build on top of primitives
[2273.04 → 2275.12] that weren't really intended to be able to support that.
[2275.12 → 2281.14] So, uh, we looked around at a bunch of those, uh, and I don't know how much we want to go
[2281.14 → 2286.66] into that, but cockroach CB was basically, I would say the most appealing of those, um,
[2286.66 → 2287.46] for various reasons.
[2287.46 → 2289.92] The big one was that it had a really strong Jensen report.
[2290.26 → 2295.56] So for folks that don't know, Jensen is, uh, well, it was originally a project.
[2295.56 → 2300.68] I think it's now a consulting company that will basically stress test.
[2300.84 → 2301.18] Yeah.
[2301.24 → 2307.44] Kyle Kingsbury, it was stress test all kinds of distributed database like things to verify
[2307.44 → 2311.34] their cap properties, their properties with respect to the cap through, uh, consistency
[2311.34 → 2313.06] and availability in the face of a partition.
[2313.66 → 2316.58] And a lot, I mean, a lot of them are horror stories.
[2316.70 → 2320.18] A lot of the reports around like all the terrible things that went wrong.
[2320.18 → 2325.92] And for some of the databases we looked at, some of these new SQL ones, not only was the
[2326.02 → 2330.60] were there terrible inconsistencies in the data, but like the thing would keel over part
[2330.60 → 2333.04] way through the test and like not be able to be recovered.
[2333.76 → 2335.92] And that, those were obviously pretty worrisome.
[2336.06 → 2338.06] And cockroach CB's report was really strong here.
[2338.52 → 2340.22] So that was a big reason.
[2340.38 → 2342.48] I think we were like, okay, that sounds pretty plausible.
[2342.48 → 2347.80] But then it also had a bunch of these features that just felt like it was actually pretty well
[2347.80 → 2351.00] aligned technically with what we wanted in terms of hands-off operability.
[2351.86 → 2356.88] So like with cockroach, you basically just like run cockroach run, and then you pointed
[2356.88 → 2359.52] at the other nodes of the cluster and it just kind of figures it out.
[2360.16 → 2363.78] Whereas with some of the other ones, you would have to go deploy like four or five different
[2363.78 → 2367.54] components in a bunch of different places and get everything pointed at each other,
[2367.76 → 2368.58] which is fine.
[2368.58 → 2372.30] But like, that's just a bunch more software you have to go build to make sure that
[2372.30 → 2374.06] all gets set up correctly.
[2374.82 → 2377.48] And you just kind of didn't, we didn't have to worry about that with cockroach CB.
[2377.48 → 2378.80] So that was pretty appealing too.
[2379.34 → 2379.68] Yes.
[2379.70 → 2384.80] This is a really, really, really important point because I mean, we're not sure if we're
[2384.80 → 2389.64] not the first to do it, obviously, but I think it is unusual to ship a distributed system
[2389.64 → 2390.38] as a product.
[2391.38 → 2394.62] And it's also unusual to ship a distributed system as a product that works.
[2396.08 → 2402.64] So we are, we are shipping a distributed system as a product that's going to exist over an air
[2402.64 → 2403.80] gap where we can't get.
[2403.86 → 2407.38] Critically, no remote maintenance, no remote hands, right?
[2407.38 → 2409.90] Like this is, it's got to just work.
[2410.00 → 2411.04] We're sending it into space.
[2411.24 → 2412.12] It's got to just work.
[2412.50 → 2412.82] Yes.
[2413.46 → 2418.40] Which feels like, it doesn't feel like you're splitting the atom with that requirement, but
[2418.40 → 2423.18] you, but as you take it apart, it's like actually really, really hard because you're taking a lot
[2423.18 → 2423.78] of these systems.
[2424.22 → 2428.30] A lot of these systems have an implicit dependency on an operator.
[2428.30 → 2432.78] And I think in the cloud SaaS era, that's more, that's kind of more true than ever, honestly.
[2433.98 → 2440.48] And that is something that, I mean, Dave, that, that was very, very, very important that, that
[2440.48 → 2446.46] the ability for these things to, to operate autonomously and automatically, and for us to be able to
[2446.46 → 2450.40] through software control their actions and not rely on an operator.
[2451.62 → 2452.06] Yeah.
[2452.48 → 2452.88] Yeah.
[2453.24 → 2453.68] Yes.
[2453.96 → 2454.36] Huge.
[2455.32 → 2456.00] Very huge.
[2456.00 → 2458.18] And I'd say that has worked out pretty well.
[2458.30 → 2459.84] For us.
[2459.84 → 2460.12] Yes.
[2460.28 → 2464.20] Well, I think it's just, that, that is also where a lot of these other things fell down.
[2465.08 → 2465.32] Yeah.
[2465.78 → 2471.44] Where we, and, you know, I think that it's because folks have been asking, well, you know, what
[2471.44 → 2471.90] about this?
[2471.94 → 2472.32] What about that?
[2472.40 → 2476.24] You know what about, you know, and there were folks were asking about Yuga Byte and, you
[2476.24 → 2479.06] know, Yuga Byte has some strengths for sure.
[2479.06 → 2483.60] And that it is, it was definitely, it's purely open source, completely open source.
[2483.72 → 2484.06] It's great.
[2484.06 → 2487.72] Um, and we, we kind of like the Postgres compatibility seems nice.
[2488.22 → 2491.10] Um, but the, the Jensen report was a problem for Yuga Byte.
[2491.10 → 2495.60] Um, and we were concerned about some of the operability of it.
[2495.86 → 2501.10] Um, the yeah, I think that was one of the ones where it crashed during the tests and
[2501.10 → 2503.92] required intervention to bring it back up if I'm remembering right.
[2504.38 → 2505.90] And they fixed a bunch of those issues too.
[2506.08 → 2510.28] So it's not, it's not like these are just like permanent problems, but it was, it was
[2510.28 → 2510.64] worrisome.
[2510.64 → 2512.58] It was worrisome.
[2512.82 → 2516.74] And, um, we looked at, um, TIKI and TIDE.
[2516.88 → 2519.32] We had some similar kind of, uh, problems there.
[2520.12 → 2527.82] Um, the, um, so, I mean, with, with, we had, uh, and then I, we looked at Foundation DB.
[2527.98 → 2529.58] People were asking about Foundation DB as well.
[2530.24 → 2536.66] Um, and I think, um, you know, Foundation DB, we didn't dig into too, too deeply because I
[2536.66 → 2540.16] think we concluded that it was going to require us to build quite a bit.
[2540.16 → 2540.92] Is that right, Dave?
[2541.36 → 2541.98] Yeah, that's right.
[2542.06 → 2545.68] So at that point, I don't think it even supported secondary indexes out of the box.
[2545.78 → 2548.48] That was something that people would build on top of it, which was fine.
[2548.58 → 2553.16] I mean, yeah, the takeaway was that it seemed like people had really great experiences and
[2553.80 → 2558.04] could build the thing that they needed and had to invest quite a lot of engineering to,
[2558.14 → 2562.36] to take it from what it ships with in the box to what they needed.
[2563.04 → 2565.08] It really seemed like what the name says.
[2565.12 → 2566.68] It's a foundation for your database.
[2566.78 → 2568.18] It's not a complete thing.
[2568.18 → 2572.96] And our constraint on this was that it was open source.
[2573.86 → 2575.38] Um, so we-
[2575.38 → 2576.28] I saw that.
[2577.02 → 2578.16] I mean, I saw that.
[2578.52 → 2583.18] I mean, I, I saw that again today for the first time since reading this RFD, you know,
[2583.20 → 2584.80] writing this RFD like four years ago.
[2585.18 → 2585.58] Yeah.
[2585.58 → 2589.28] And I'm, I'm like a little bit like, I mean, it was BSL, right?
[2589.28 → 2590.46] I mean, it's not-
[2590.46 → 2591.28] Not open source, right?
[2591.30 → 2591.48] Right?
[2592.04 → 2592.64] Not open source.
[2592.64 → 2593.18] Yeah, right.
[2593.26 → 2593.76] It's close enough.
[2593.84 → 2594.42] It's close enough.
[2594.50 → 2597.40] It was just interesting to me rereading that, that like, oh, yeah.
[2597.86 → 2600.42] Oh, rereading 110 in terms of your, yeah.
[2600.46 → 2601.56] I mean, it's, it's prescient.
[2602.34 → 2602.70] Yeah.
[2602.70 → 2607.50] Um, so yeah, well, we'll talk about how, kind of how Cockroach did on like its strengths
[2607.50 → 2611.20] and this is, you know, it's outlined in 110, and then what were some of the weaknesses
[2611.20 → 2612.16] that we saw out of Cockroach?
[2613.56 → 2613.92] Yeah.
[2614.02 → 2620.32] So I pulled this up to remind myself, but basically, you know, we did, we did a bunch of testing.
[2620.32 → 2621.46] We did online expansion.
[2621.60 → 2622.58] We did online contraction.
[2622.58 → 2624.08] We did an online schema change.
[2624.60 → 2630.70] Um, I did like, you know, basic sort of P kill, like send it a six SEG me, rebooted the
[2630.70 → 2632.14] operating system out from under it.
[2632.14 → 2636.32] I also panicked the operating system, which a lot of people don't realize is different
[2636.32 → 2639.78] than rebooting the operating system because TCP connections don't get cleaned up.
[2639.88 → 2641.70] So it looks more like a partition for a little while.
[2642.72 → 2648.78] And, um, in all of these cases, we, I mean, not a high bar, but there was no data loss.
[2648.92 → 2649.78] That's pretty huge.
[2650.68 → 2653.36] Um, not a high bar, but like pretty critical.
[2654.42 → 2656.46] Um, I wrote no unexpected crashes.
[2656.60 → 2660.26] Um, Cockroach DB does like to crash when the clocks get out of sync.
[2660.26 → 2665.76] And this was the thing that I ran into a lot at first because our, our stock NTPD was
[2665.76 → 2667.16] not very good at keeping them in sync.
[2667.82 → 2670.88] Um, and I gather that this has been a pain point for other folks, but since we started
[2670.88 → 2673.94] using crony, that's just like a complete non problem, non problem for us.
[2674.24 → 2677.86] Crony keeps them well enough in sync that I don't think I've seen a single one of those
[2677.86 → 2681.32] crashes and knock on wood since, uh, we started doing that.
[2681.32 → 2686.30] So no unexpected crashes, uh, you know, in this testing, go see.
[2686.38 → 2691.90] And Dave, I'd like to point out that, I mean, I mean, you're such a model for us all in terms
[2691.90 → 2693.00] of the way you conduct your engineering.
[2693.00 → 2696.82] And one of the things that I loved about the way you did this, I mean, so much rigour with
[2696.82 → 2703.32] respect to not just the RFDs, but then the software you wrote or the evaluation you got
[2703.32 → 2708.60] like, you know, in a repo in a, in a repo that we, that has been closed and that actually you
[2708.60 → 2709.34] had archived it.
[2709.62 → 2714.06] Um, and we opened it up as part of opening up one 10 and 53.
[2714.96 → 2719.00] Um, and I, I mean, this, I, this is delightful.
[2719.48 → 2724.30] And, you know, the three of us were physically in the office together, and I was going into
[2724.30 → 2728.14] this repo and I, I mean, I'd been in there, you know, four years ago, but definitely not
[2728.14 → 2728.46] recently.
[2728.46 → 2733.58] And, uh, Adam was kind of roasting me for being so surprised about how complete it is.
[2734.30 → 2738.80] And, uh, you know, Adam is basically like, how dare you insult Dave by being surprised
[2738.80 → 2744.12] by, by the depth of, and the polish on this evaluation repo.
[2744.46 → 2748.36] And then Dave, you walked over, and you were looking at it, and then it actually gave me
[2748.36 → 2752.82] great solace that you yourself were surprised at your own level of rigour in this work.
[2753.62 → 2757.30] Well, yeah, in the write-up, I was, I was like, Oh, there are a lot of graphs here.
[2757.30 → 2761.48] Like those take a little while to like to do, you know, to get that data out.
[2761.62 → 2763.02] But, you know, I thought it was really important.
[2763.02 → 2764.68] This is before ChatGPT was doing that for us.
[2765.26 → 2765.62] Exactly.
[2766.02 → 2766.44] That's right.
[2766.52 → 2771.06] This is, this is all a handcrafted human generated analysis.
[2772.18 → 2773.14] Yeah, man.
[2773.62 → 2775.52] I wonder how ChatGPT would have changed that.
[2775.96 → 2778.24] Draw the draw graphs of this random data.
[2779.20 → 2781.98] Go parse this, figure out how to parse this data and draw me some graphs.
[2781.98 → 2782.98] Yeah.
[2784.74 → 2785.06] Yeah.
[2785.16 → 2788.04] I mean, so the report was very detailed, and it's like, yeah, it hasn't a lot.
[2788.30 → 2793.74] But I mean, that came out of the pain of having experienced this at, at joint.
[2793.82 → 2796.64] And in particular, you know, some of the problems that we met, we mentioned some of
[2796.64 → 2801.40] the really horrible problems at joint, but some of them were not, they don't sound so
[2801.40 → 2801.64] bad.
[2801.70 → 2804.32] It was like, okay, this auto vacuum was running for three days.
[2804.32 → 2809.50] Actually, a lot of vacuums running for like a month on some shards and latency is degraded
[2809.50 → 2810.46] like 40%.
[2810.46 → 2814.18] And you're like, okay, but like this thing that was taking a hundred milliseconds is
[2814.18 → 2815.50] now taking 140 milliseconds.
[2815.72 → 2816.38] It's not so bad.
[2816.44 → 2822.04] And it's like, well, if your goal is to move like petabytes of data from one place to another,
[2822.22 → 2825.06] it's like, actually, that's a huge decrease in throughput and it's a huge problem.
[2825.28 → 2828.64] So it made me appreciate like how important it was to actually look at those graphs of
[2828.64 → 2833.28] latency and, and also like the small spikes and dips and stuff like that too.
[2833.28 → 2835.32] Like those can have a pretty big impact.
[2835.56 → 2838.12] And I just wanted to see if we were going to see some of those same effects.
[2838.12 → 2844.84] And we did see latency degrade in some cases, like, you know, I have to go back to the data
[2844.84 → 2847.22] to look at where it was, like which of these operations it was.
[2847.44 → 2850.48] It wasn't for like failures, transient failures and stuff like that.
[2850.48 → 2854.40] But I think some of the expansion and contraction use cases would see these latency degradations,
[2854.56 → 2858.30] but it wasn't, it wasn't enough of a problem at the time.
[2858.80 → 2861.32] Well, and we, we spent some time trying to investigate that, right?
[2861.32 → 2863.24] I think that those are the we had some outliers.
[2863.80 → 2863.88] Yeah.
[2864.20 → 2864.56] Yeah.
[2864.56 → 2867.94] We had two rounds of this testing and the first round actually didn't go that well.
[2868.28 → 2872.68] We had things would basically just stop for like two minutes or something like that while
[2872.68 → 2873.88] these operations were going on.
[2873.88 → 2878.26] And I think we concluded that they were CPU starved and maybe IO starved also.
[2879.38 → 2880.44] Um, I can't remember.
[2880.98 → 2885.66] And we ended up, fortunately we were able to just like to bump up a bunch of the resource limits
[2885.66 → 2886.72] and that helped quite a bit.
[2886.72 → 2892.02] This is also when I discovered the crazy, what I feel like is crazy behaviour on AWS, which
[2892.02 → 2896.68] is, I think Adam, you were like completely unsurprised by this, but it was like when
[2896.68 → 2903.84] you provision a new, when you reboot a VM on AWS, you get like a bunch of IOPS for
[2903.84 → 2905.46] free, like superfast IOPS.
[2905.72 → 2906.16] Yeah.
[2906.16 → 2909.54] And the idea is basically they want to make booting fast.
[2909.54 → 2915.42] They like whatever level of IOPS you're going to get from a disc of a given size.
[2916.26 → 2921.22] If you were to boot a typical VM at that IOPS rate, it would be pretty slow to boot.
[2921.46 → 2927.22] So they just give you a bunch of IOPS fast upfront, but they don't really know when
[2927.22 → 2927.70] you've booted.
[2927.88 → 2929.34] So you just get like a fixed number.
[2929.42 → 2930.22] It's like a lot of them.
[2930.34 → 2934.88] And so we had all these tests where it's like things are great for like four hours.
[2934.88 → 2936.86] And then all of a sudden it just craters.
[2937.50 → 2941.32] And it was because I just hit the limit that like however many IOPS they thought I needed
[2941.32 → 2945.02] for booting, I hit it four hours into the test and then things cratered.
[2946.08 → 2949.98] Is that, I can't remember if that's actually, it must be in the write-up from the first testing
[2949.98 → 2952.04] notes, but that was crazy to me.
[2952.08 → 2953.36] I mean, is that something everyone just knows?
[2954.64 → 2958.18] No, I think that's one of those things that you only learn the hard way.
[2958.74 → 2963.02] Like even, even as you're saying it, even now that it's on the podcast, now that we've
[2963.02 → 2966.62] told people, people are going to hit it the hard way and say, oh yeah, I remember Dave
[2966.62 → 2968.78] told me, but I had to learn it the hard way.
[2970.92 → 2971.28] Yeah.
[2971.42 → 2975.46] It's, and it's also very, it's subtle because like, there's nothing that goes off and says
[2975.46 → 2978.32] you hit this limit, and now it's going to be slow.
[2978.46 → 2978.74] Oh yeah.
[2978.92 → 2979.10] No.
[2979.18 → 2979.36] Right.
[2979.90 → 2985.06] You can tell, like if you go into the cloud metrics thing and like to look up the throttle
[2985.06 → 2987.88] metric or whatever, like you can confirm that this is the case.
[2987.88 → 2989.44] And I did confirm that.
[2989.66 → 2991.20] Thank you for pointing me to that, Adam.
[2991.20 → 2994.20] But anyway, yeah.
[2994.26 → 2996.06] So we, we did have to run a couple of rounds of tests.
[2996.18 → 2999.44] We did find a couple of problems, but we were able to get to a pretty good point when we
[2999.44 → 3005.68] understood that problem and, um, and had the right amount of resources in HVM.
[3007.44 → 3014.14] So we, the one question coming from the chat is that, um, in RFT53, it doesn't call it SQL
[3014.14 → 3019.88] per se, but it mentions that we need transactions, and we need acid semantics, atomicity, consistency,
[3020.14 → 3020.70] integrity, durability.
[3020.70 → 3025.48] Um, the and obviously Season would indicate the consistency is important to us.
[3025.88 → 3028.50] Uh, and the question is kind of curious about the reasoning there.
[3028.50 → 3032.64] Um, the like, do you, um, yeah.
[3032.64 → 3035.76] So the, the consistency is sort of easier to think about.
[3035.76 → 3041.72] Um, like if you, if you were using something like EC2 or any, I mean, any API where you're
[3041.72 → 3046.88] going to go provision to VM, it would be pretty weird if you could create a VM and then list
[3046.88 → 3051.00] your VMs, and it wasn't there or like to create a VM and then get it state.
[3051.06 → 3051.94] Is it booted yet?
[3051.94 → 3053.64] And it's like, actually, I don't even know about it.
[3054.00 → 3060.16] So strong consistency was important for just the user experience of using our API and being
[3060.16 → 3063.50] able to configure things and getting a consistent view of whatever it is you've done.
[3063.66 → 3066.12] Similar example would be a firewall rules, right?
[3066.12 → 3070.80] If you imagined an eventually consistent API for firewall rules where you're like putting
[3070.80 → 3075.54] a bunch of firewall rules and then the networking in your VMs doesn't do what you expect.
[3075.54 → 3080.00] And you go check the state in the API, and it's showing you something that's old or might
[3080.00 → 3083.36] be old, and you don't know, that would be a pretty awful experience, I think.
[3083.36 → 3086.82] So that's why I would say consistency was really important.
[3087.00 → 3087.64] It's just what we want.
[3087.68 → 3088.32] Consistency is really, yeah.
[3089.06 → 3094.50] And especially then you want, it's just very, and this also, there are not so many elements
[3094.50 → 3096.40] in this database that consistency is unreasonable.
[3096.64 → 3100.46] This is not, you know, this is, this is not exabytes of data.
[3101.56 → 3101.98] So that's true.
[3102.18 → 3103.28] That was a huge help.
[3103.36 → 3105.06] You're certainly relative to the joint use case.
[3105.94 → 3109.26] It's a much smaller database, and it's probably much smaller throughput.
[3109.38 → 3112.34] It's certainly a much smaller throughput now, but I think even for a long time, it probably
[3112.34 → 3112.96] will be.
[3113.36 → 3114.96] But we care a lot about it.
[3115.36 → 3116.48] We care about its consistency.
[3116.70 → 3117.64] We care about its availability.
[3118.48 → 3118.54] Yeah.
[3119.34 → 3125.28] And we, because if it's not consistent, there's just, or it's eventually consistent, that just
[3125.28 → 3132.12] casts such a long shadow up the control plane and just end up with, and then it's like,
[3132.28 → 3138.44] also, I mean, how do you, when, oh, if it's not there, just like wait a little bit.
[3138.50 → 3139.04] It's like, well, okay.
[3139.06 → 3141.48] So at what point is that kind of pathological?
[3141.48 → 3142.00] It's like, I don't know.
[3142.04 → 3143.22] I guess you got to wait a day this time.
[3143.36 → 3143.64] I don't know.
[3143.64 → 3149.58] And I mean, then you are kind of like training yourself to not really explore provisioning
[3149.58 → 3151.04] failures or long tails of provisioning.
[3151.10 → 3157.64] We want to provision to be really quick, really robust, and to always succeed or fail very
[3157.64 → 3158.10] explicitly.
[3158.32 → 3163.46] Like we don't want to have that kind of gooey property that it's like, yeah, it's kind of
[3163.46 → 3164.28] in a bad mood today.
[3164.40 → 3166.70] So maybe like, you know, go take a walk and see if it's done.
[3166.76 → 3168.36] It's like, nah, no, no.
[3168.36 → 3168.70] Thank you.
[3168.70 → 3169.14] Totally.
[3169.14 → 3169.58] Totally.
[3169.58 → 3170.22] Totally.
[3170.92 → 3173.86] The sort of transactions is, it's a little bit more abstract.
[3173.98 → 3175.36] I'd have to think about a better example.
[3175.36 → 3182.20] But like some examples would be, you know, if you provision a VM, we want to find the resources
[3182.20 → 3185.98] for it, which, you know, most basically includes like the sled we're going to put it on.
[3186.20 → 3187.82] And we want to allocate those resources.
[3188.32 → 3190.50] And that's a complicated decision.
[3190.64 → 3195.64] Actually, disks are even more complicated because we need to find three sleds that have enough
[3195.64 → 3196.48] storage on them.
[3196.48 → 3202.10] And enough, and that's, that storage needs to be on disks that are currently in service
[3202.10 → 3203.72] and believed to be working and blah, blah, blah.
[3203.80 → 3205.44] So it's like a complicated set of constraints.
[3206.02 → 3210.42] And then there's like an optimization around like which of the sets of ones do you want to
[3210.42 → 3210.98] actually pick?
[3211.06 → 3212.18] And then you want to commit to that.
[3212.26 → 3216.66] So like that looks like a CTE in SQL where you're basically fetching a bunch of state and
[3216.66 → 3219.46] then picking a couple of them and then like committing that state in the database.
[3219.46 → 3222.50] So that makes sense, I think, why that would be in a transaction.
[3223.22 → 3223.80] Another example.
[3224.08 → 3225.50] What a CTE is in SQL?
[3225.50 → 3228.20] Yeah, CTE is a common table expression.
[3228.62 → 3233.58] And it's basically a way of doing a, I think of it as a way of doing a bunch of things in
[3233.58 → 3234.60] sequence in SQL.
[3234.94 → 3239.48] Because SQL is sort of declarative, sort of, where you're basically like, you know, if
[3239.48 → 3242.58] you're writing a select, you're describing what you want the output to look like.
[3242.74 → 3246.98] But it is useful sometimes to be able to give names to some of the intermediate values.
[3247.26 → 3253.60] And so what a CTE lets you do is like with some name as some query, go execute some other
[3253.60 → 3255.66] query that uses that name in it.
[3256.10 → 3259.58] It's like kind of basic thing just to be able to do a bunch of things in a row, basically.
[3259.84 → 3261.36] And they all happen in a transaction.
[3263.02 → 3266.98] Maybe a better, maybe, I don't know if this is a better or worse example of using transactions
[3266.98 → 3273.06] is that I'm working on a system called Reconfigurator where we, the system, basically, it's kind
[3273.06 → 3274.18] of like the reconciler pattern.
[3274.26 → 3278.40] We talked about this a little bit last week, where the system is looking at the configured,
[3278.74 → 3282.66] like what the operator has configured, what they want the system to look like, and what
[3282.66 → 3283.66] it actually looks like.
[3283.66 → 3288.30] And making a plan that we call a blueprint that's like moving forward to the next step.
[3288.46 → 3294.88] And so the Nexus instances, the control plane instances, are looking, like potentially independently
[3294.88 → 3298.34] looking at that and then making a decision about what should happen and trying to create
[3298.34 → 3299.82] a next blueprint.
[3300.28 → 3304.84] And then they will try to make that the next blueprint that the system is trying to work
[3304.84 → 3305.12] towards.
[3305.26 → 3309.74] But it's conditional on other things not having invalidated those choices.
[3309.74 → 3314.30] So that's where we also want to use a transaction to say, basically, make this the new target
[3314.30 → 3318.84] blueprint if this other one is the current target, because that means nothing has changed
[3318.84 → 3320.28] since I made all these decisions.
[3321.00 → 3325.86] So hopefully that makes some sense in terms of like why we're using transactions.
[3326.00 → 3327.60] There are just a lot of decisions like that.
[3328.34 → 3328.44] Right.
[3329.46 → 3329.82] Right.
[3330.02 → 3333.58] And another, I mean, an example of where consistency is really important, actually.
[3333.70 → 3336.96] And we talk, I mean, you know, QR episode from last week in terms of sagas, where it'd
[3336.96 → 3340.20] be really hard to do that without transactions and consistency.
[3340.90 → 3341.02] Yeah.
[3343.62 → 3346.10] So what have been kind of our experience?
[3346.22 → 3349.38] So we decide to go cockroach.
[3349.90 → 3352.24] What were some of the actual, what were some of the drawbacks?
[3352.34 → 3354.14] We got the thing working.
[3355.00 → 3359.52] If I can do that, one or two more things to the testing that we did that I think were
[3359.52 → 3360.24] really huge.
[3361.02 → 3361.20] Yes.
[3361.20 → 3366.76] The cluster always converged to the right level of replication and came back online
[3366.76 → 3369.52] without operator intervention, no matter what I did to it.
[3369.90 → 3371.30] That was really huge for me.
[3371.44 → 3375.38] I mean, having just come off of a couple of years of fighting these issues, that was really
[3375.38 → 3375.68] huge.
[3375.94 → 3380.50] And it also clearly communicated when data was under replicated and what it was doing to
[3380.50 → 3382.54] fix it and like what the progress was like on that.
[3383.04 → 3387.44] And it was, it was just, there was a breath of fresh air compared to what I had been doing.
[3387.52 → 3388.08] So that was huge.
[3388.08 → 3393.10] When it tells you that we're in the kind of the design centre for this thing, someone
[3393.10 → 3396.56] just cared about that kind of tooling and that kind of visibility.
[3397.18 → 3397.46] That's right.
[3397.54 → 3398.16] That's exactly right.
[3398.22 → 3403.08] It makes, it made me feel like the people who built it understood some of the complexities
[3403.08 → 3407.84] that at least we didn't understand when we chose Postgres for, for the joint use case.
[3408.34 → 3410.60] And, and that made me feel better about it.
[3412.06 → 3414.34] And the experience I'd say has been pretty positive.
[3414.34 → 3417.84] I don't think we've had too many major issues with it.
[3418.54 → 3424.22] The couple that come to mind, we did, Ben and I ran into some horrible problem around
[3424.22 → 3428.34] partial indexes being corrupted, which turned out to be a known issue that had been already
[3428.34 → 3429.94] fixed in the, in the latest version.
[3430.10 → 3431.32] And we were able to upgrade to it.
[3431.40 → 3432.96] And like that, that was great.
[3433.38 → 3435.24] I mean, it was good to know that they had already found it.
[3435.30 → 3436.10] I mean, it was scary.
[3436.24 → 3441.00] And I did this demo at demo day when I just like did a bunch of selects and updates in
[3441.00 → 3443.56] such a way that it produced obviously wrong data.
[3444.48 → 3447.58] So that was definitely scary, but you know, they've taken it seriously.
[3447.72 → 3449.62] They'd had a cockroach technical advisory for that.
[3449.72 → 3452.40] I think that was the point where I started subscribing to those and making sure that we
[3452.40 → 3454.76] were aware of all those kinds of problems.
[3455.60 → 3456.66] Do you have that issue?
[3456.76 → 3457.92] Do you, well, we'll dig that up.
[3458.20 → 3459.76] I can, I can definitely dig it up.
[3460.90 → 3466.48] The other one is client side retries were a bit of a were a thing we had to go figure
[3466.48 → 3466.80] out.
[3467.24 → 3470.50] And this is definitely, this is a little different from Postgres.
[3471.20 → 3472.16] I think so.
[3472.84 → 3474.08] I'd have to actually think about that.
[3474.30 → 3478.42] So cockroach DB is generally Postgres compatible, but it is distributed under the hood and everything
[3478.42 → 3482.76] you write goes through raft and, you know, winds up on a couple of nodes, and you can have
[3482.76 → 3488.50] failure modes that are at least much less common than on Postgres where you are trying
[3488.50 → 3493.66] to make some change and cockroach DB is, or sorry, you're trying to make some change
[3493.66 → 3497.62] that ends up spanning more nodes than a simple change would.
[3497.62 → 3502.40] And in that process, some of the stuff changed out from under you.
[3502.54 → 3504.32] And the thing you tried to do is no longer valid.
[3504.46 → 3506.54] Does that sound like rambling or did that make any sense?
[3508.68 → 3509.48] Yeah, it makes sense.
[3509.74 → 3512.10] It's, it's a little bit like optimistic concurrency control.
[3512.10 → 3515.62] It's not exactly that, but what's happening under the hood is it's basically making a
[3515.62 → 3519.80] bunch of changes conditional on the underlying state not having changed on the other node.
[3520.40 → 3524.32] And if the underlying state does change, then it basically aborts the transaction with an
[3524.32 → 3527.08] error saying, sorry, you just need to do this again.
[3527.22 → 3528.72] And if you run it again, it should work.
[3528.72 → 3532.98] Which is like a little cheesy, but it's a pretty pragmatic trade-off, I think, because the
[3532.98 → 3534.38] alternative is to try it by itself.
[3534.38 → 3539.76] And then you have, you know, silent latency bubbles, but it actually can retry it by itself
[3539.76 → 3541.50] when they are simple transactions.
[3541.50 → 3546.04] Like if you just, if you're able to issue the whole, you know, begin, select, insert,
[3546.16 → 3550.26] update, whatever, commit in one go, then it can retry it by itself.
[3550.26 → 3551.52] And you don't have to think about this at all.
[3552.02 → 3557.14] But we, for better and worse, use a bunch of this pattern that I call interactive transactions,
[3557.14 → 3561.88] where in Rust, we will write like begin, the beginning transaction thing.
[3562.28 → 3564.02] And then we will go issue more SQL.
[3564.18 → 3565.88] But like our client is involved in that.
[3565.98 → 3568.78] It's not like we're issuing all that stuff to the database at once.
[3568.88 → 3573.60] We're having a conversation with the database with the transaction open and then committing
[3573.60 → 3573.82] it.
[3573.92 → 3577.76] And that, it, that opens you up to a much longer window where this can happen.
[3577.76 → 3581.96] And it also means that the database can't retry it by itself because it can't replay
[3581.96 → 3582.64] that conversation.
[3582.80 → 3584.10] It doesn't know what you're going to say.
[3584.44 → 3584.90] You know what I mean?
[3585.92 → 3590.14] It doesn't know what, what SQL to replay because it was dependent on whatever results you got
[3590.14 → 3592.32] back from earlier queries in the same transaction.
[3592.96 → 3595.86] So that was a thing that we had to go build some mechanism for that.
[3596.08 → 3601.06] And I mean, I don't know if I, I'd say pain point in terms of our usage of it more than
[3601.06 → 3605.56] anything, because it is actually pretty well documented that this is a thing and that there's,
[3605.56 → 3606.92] there are two ways of dealing with it.
[3606.92 → 3611.68] And you might have to invest some client side work if your language doesn't already have
[3611.68 → 3611.88] it.
[3612.40 → 3613.72] And then we had to do that.
[3615.00 → 3621.34] And then how, I mean, so the autonomous operation has so far been okay.
[3621.86 → 3622.94] We haven't had.
[3623.98 → 3624.38] Yeah.
[3624.46 → 3625.00] I'm trying to think.
[3625.08 → 3626.24] Like, I don't remember.
[3627.14 → 3631.22] So I would say we probably don't have enough monitoring to know that it's not crashing
[3631.22 → 3634.08] transiently and like coming back really quickly and working.
[3634.08 → 3635.04] You know what I mean?
[3635.52 → 3639.62] But like, I don't think we have like dozens of core files from production systems.
[3639.76 → 3643.42] We certainly, like, I cannot ever remember getting to a system where cockroach was down
[3643.42 → 3647.56] and we couldn't bring it back up or, or even where it was down.
[3647.92 → 3648.28] Yeah.
[3648.52 → 3651.22] Like, I think it's just basically stayed up.
[3652.00 → 3657.68] And, and as I say that out loud, it makes me worry that we're not, that the things we're
[3657.68 → 3660.52] trying to do are just in its wheelhouse, and we haven't hit it in the places where it's
[3660.52 → 3661.80] not ready for it.
[3661.80 → 3663.48] Like that's, that's helpful enough, right?
[3664.68 → 3665.56] And this was definitely not true.
[3665.56 → 3665.62] Yeah.
[3665.62 → 3668.30] I mean, we don't trust anecdotal evidence, including our own anecdotal evidence.
[3668.68 → 3669.08] Absolutely.
[3669.20 → 3669.52] Absolutely.
[3669.90 → 3672.56] But that was never true of Postgres at Joy ant.
[3672.70 → 3677.24] Even in, like in development, we'd, all of, all the time we'd run into cases where it
[3677.24 → 3681.24] had just like decided replication was broken, and you had to like figure out what was wrong
[3681.24 → 3682.52] and then manually fix it.
[3683.08 → 3687.22] So like there were tons of cases where it would just like fall down and not come up without
[3687.22 → 3687.84] your intervention.
[3687.84 → 3689.24] And that just hasn't been the case.
[3689.24 → 3690.24] So that's been pretty good.
[3691.24 → 3697.18] And Dave, the two places where we have been questioned data integrity turned out to be
[3697.18 → 3698.92] not related to Cockroach at all.
[3699.04 → 3703.06] I think one was when you came on the show two years ago to talk about, is there called the
[3703.06 → 3704.06] MM registers?
[3704.06 → 3710.06] And like basically a gap in, in our operating system in Helios.
[3710.26 → 3717.94] And then the other one being a misunderstanding of cancellation with Rust async.
[3718.32 → 3719.60] And both of this sort of, right.
[3720.06 → 3726.54] Kind of looked like data corruption, but it was not the cockroach, cockroach's fault.
[3726.54 → 3726.98] Yeah.
[3726.98 → 3727.42] Yeah.
[3727.42 → 3727.86] Yeah.
[3727.86 → 3731.16] That, that second one was very wild.
[3731.86 → 3737.30] And I mean, so that one was, we, we walked up to a system that was broken.
[3737.44 → 3739.92] I think it was our pre-production system, our dog food system.
[3740.58 → 3746.08] And it, its log had indicated that it had done a bunch of work that was not in the database.
[3746.08 → 3750.64] And like, it's simple enough code that like there was like, it's an insert only thing.
[3750.72 → 3752.16] Nothing ever deletes anything from it.
[3752.22 → 3753.62] It's like, how can this not be there?
[3753.62 → 3762.02] And that turned out to be a client side problem where we were, our connection pool basically
[3762.02 → 3764.16] had a bug where we would check out the connection.
[3764.38 → 3765.42] We'd begin a transaction.
[3765.64 → 3769.80] Then we'd encounter an error that would cause Rust async cancellation to happen.
[3769.80 → 3771.38] And we weren't aborting the transaction.
[3771.96 → 3778.22] And so anything else that tried to go do something with that connection was operating in the fantasy
[3778.22 → 3781.56] land in which this transaction was going to complete.
[3781.78 → 3783.42] Like an alternate universe.
[3783.62 → 3784.40] It's absolutely.
[3785.10 → 3786.30] And which is actually kind of amazing.
[3787.30 → 3789.16] It would run for hours like that.
[3789.30 → 3791.14] And like, that's kind of a problem.
[3791.52 → 3795.44] I mean, I don't know that Postgres would have done worse with that, but like, I mean, it's
[3795.44 → 3798.42] a problem for the client, but it's also a problem for the database because you end up
[3798.42 → 3802.70] having all this data that is sitting there, not referenced by anything, but it still has
[3802.70 → 3803.48] to hang on to it.
[3803.68 → 3805.02] And if you decide not to do anything, it's still there.
[3805.02 → 3807.00] This is a hell of a transaction you guys have going on.
[3807.12 → 3807.52] But all right.
[3807.56 → 3807.74] Yeah.
[3808.24 → 3808.74] Another one.
[3808.82 → 3809.20] Come on in.
[3810.20 → 3814.64] I'm using like a terabyte of storage and like hundreds of gigabytes of memory for this
[3814.64 → 3814.86] thing.
[3814.98 → 3816.64] Like, are you sure you want to do something with it?
[3816.72 → 3818.42] Are you going to close this transaction at some point?
[3818.48 → 3818.76] All right.
[3818.88 → 3819.20] Whatever.
[3819.44 → 3819.70] All right.
[3819.76 → 3820.40] No, I guess not.
[3820.48 → 3820.70] All right.
[3820.70 → 3821.18] Give me some more.
[3821.30 → 3821.56] It's fine.
[3821.66 → 3822.02] I'm here.
[3822.02 → 3822.46] Yeah.
[3822.96 → 3825.98] That was a big eye-opener for us about cancellation.
[3826.24 → 3829.46] But fortunately, even though it looked for all the world at first, like, oh my God, has
[3829.46 → 3830.92] the database completely eaten everything?
[3830.92 → 3831.04] Yeah.
[3831.10 → 3835.78] I mean, did you kind of breath a little bit when you first realized like it's not in the
[3835.78 → 3836.18] database?
[3836.30 → 3836.68] You're just like.
[3838.68 → 3839.04] Yeah.
[3839.04 → 3840.00] It's happening again.
[3841.34 → 3843.28] It's like data corruption week was last week.
[3843.38 → 3844.54] This can't be happening right now.
[3845.18 → 3845.50] Yeah.
[3846.44 → 3846.70] Yeah.
[3846.70 → 3846.80] Yeah.
[3846.80 → 3847.12] I was.
[3847.38 → 3847.48] Yeah.
[3847.60 → 3849.18] It's the Adam.
[3849.30 → 3851.46] I have totally forgotten about the.
[3851.46 → 3855.90] The, the transaction being left open because the it's certainly the debugging odyssey
[3855.90 → 3861.92] that we, that Dave, you described two years ago is, uh, I think, cause there was also,
[3861.92 → 3867.76] you know, some vibes online of like, oh, like self-supporting on a database.
[3867.76 → 3872.20] Like you, that, that should, you should go listen to this.
[3872.20 → 3879.24] And, uh, I mean, we kind of, we knew, and I think this is kind of an important detail
[3879.24 → 3883.36] about the decision around cockroach and Dave, I thought it was very interesting because you're
[3883.36 → 3884.36] very pression about this.
[3884.72 → 3889.18] Um, in our FD one 10, we knew we were self-supporting at the outside.
[3889.70 → 3894.00] Um, we were not, we knew we're running it first on an Illumes derivative in terms
[3894.00 → 3894.52] of Helios.
[3894.80 → 3898.14] And it was very, I mean, we were having to do a lot of work to get it to work there.
[3898.64 → 3901.24] Um, we were using the open source builds.
[3901.24 → 3905.46] Dave, a lot of the things that you've found that have been busted have kind of been like
[3905.46 → 3907.64] little things with the open source build.
[3907.80 → 3908.36] Is that correct?
[3909.16 → 3909.40] Yeah.
[3909.64 → 3915.96] So, um, the context here is that it's been, since we've, since we have used Cockroach DB,
[3916.42 → 3921.74] I, not just for the last week, it has had parts that were proprietary or more proprietary
[3921.74 → 3923.30] guests and parts that were more open.
[3923.96 → 3929.28] And we had decided early on, we wanted to stick to the open source stuff, and they had a build
[3929.28 → 3930.90] target for that, which was amazing.
[3931.10 → 3931.82] I was like, that's perfect.
[3931.82 → 3932.18] It was very helpful.
[3932.68 → 3932.80] Yeah.
[3932.88 → 3937.48] We can go build just the OSS thing and not, and know that we're not accidentally using
[3937.48 → 3940.40] some of these features that, you know, then we'd be in violation of their license.
[3940.58 → 3943.02] So, but occasionally they would break it.
[3943.08 → 3944.56] I don't think they were testing it that heavily.
[3945.08 → 3948.88] I'm not sure if they just didn't have a CI for it or something, but yeah, I found a couple
[3948.88 → 3950.78] of issues like that, but they were pretty good about fixing them.
[3951.78 → 3956.28] And I think that, you know, part of like when we were, you know, when people wonder like,
[3956.34 → 3958.22] why would you adopt a beautiful license software?
[3958.22 → 3963.28] Part of it because like they did have things like this that made it easy for us to not
[3963.28 → 3969.32] accidentally trip over into their CCL, poorly named CCL, the cockroach community license,
[3969.44 → 3971.38] which is basically like proprietary stuff, basically.
[3972.64 → 3976.84] And their abuse of clause was pretty crisply defined.
[3976.90 → 3981.16] So there are a bunch of reasons why it's like, no, this feels like this is not OSI approved
[3981.16 → 3985.28] open, but it is actually sufficiently open for us for what we need to go to.
[3985.28 → 3989.92] And then again, we are, we know we're self-support, we're born self-supporting on this.
[3990.18 → 3995.48] We're just not going to get help is not on the way, which is one of the many oxide mottos.
[3996.20 → 4000.14] We are, we do for many of the things that we do.
[4000.44 → 4001.92] We are very much on our own.
[4002.10 → 4005.14] So we were not, and this is no different in that regard.
[4005.14 → 4005.44] Yeah.
[4005.74 → 4006.06] Yeah.
[4006.16 → 4010.36] I mean, I should say we filed a bunch of issues with cockroach GB and working with
[4010.36 → 4013.26] your engineering has always been a pretty positive experience, I would say.
[4013.66 → 4018.70] And also we all know from our experience that our use case, our platform is different enough
[4018.70 → 4020.64] that what did you say earlier?
[4020.68 → 4022.30] Nobody cares about your workload.
[4022.30 → 4022.78] Like you do.
[4022.84 → 4024.62] Like we're not going to get this.
[4024.62 → 4030.16] Um, this, we're not going to have the experience of like, we can just write to you with this
[4030.16 → 4032.00] issue, and you're just going to be able to fix it for us.
[4032.42 → 4032.78] Right.
[4032.90 → 4037.88] That's not been our experience with other software, um, in general, but also on our platform and
[4037.88 → 4038.58] in its use case.
[4038.58 → 4042.96] So like, yeah, we were going to be self-supporting to a large degree, but hopefully with the help
[4042.96 → 4043.72] of the engineering team.
[4043.76 → 4044.78] And that's been pretty true.
[4044.78 → 4045.22] Right.
[4046.42 → 4046.66] Right.
[4046.72 → 4053.48] We've been, because we, and even when we had, um, I mean, we had this issue, um, about,
[4053.48 → 4058.80] uh, you know, where we went and had to go very deep on the YEM registers, um, not being,
[4058.80 → 4060.08] uh, restored properly.
[4060.50 → 4068.16] And, um, you know, we did reach out to them and, you know, they were like reasonably, they
[4068.16 → 4070.58] were, they were as earnest as you could kind of expect them.
[4070.58 → 4076.66] I mean, they, they, and you know, they were kind of reasonably saying like this, I don't
[4076.66 → 4079.62] know, it might be an OS issue, but I felt like they weren't blowing us off.
[4079.70 → 4081.16] It felt like we were being taken seriously, which is great.
[4081.46 → 4086.52] That was wild because that particular issue could cause all kinds of bedlam, like absolutely
[4086.52 → 4089.42] all kinds of can't happen bugs would happen.
[4090.00 → 4094.20] And so before we figured this out, I wound up filing like four or five different bugs that
[4094.20 → 4099.42] were like, from their perspective, somewhere between you got pretty unlucky in some race
[4099.42 → 4101.22] condition and this really can't happen.
[4101.94 → 4104.04] And as you said, they replied to them all pretty earnestly.
[4104.22 → 4105.74] They were like, okay, well you are seeing this.
[4105.78 → 4106.72] So here's what I would try.
[4107.12 → 4108.06] Here's what I would go validate.
[4108.16 → 4112.00] Go validate that, that, that, that the go test suite passes on your system or that, you
[4112.00 → 4113.74] know, this memory test works or whatever.
[4114.12 → 4114.90] And it was helpful.
[4114.96 → 4116.44] It wasn't just like go fetch rocks.
[4116.50 → 4117.72] It was like actually helpful stuff.
[4118.68 → 4123.98] Um, and a question in the chat about, um, how we're feeling about CRDB written in go, um,
[4124.02 → 4127.18] go is obviously not our first choice for things.
[4127.18 → 4129.84] Um, a lot of CRDB is written in C++, which is important.
[4130.66 → 4138.12] Um, it's not merely go, but, um, you know, I think it's on the one hand, you know, not
[4138.12 → 4138.48] great.
[4138.50 → 4142.10] On the other hand, um, it's something that we need to work on the platform.
[4142.10 → 4146.82] So it's, I think it's kind of helpful to have a, a current use case for it.
[4146.98 → 4147.36] I don't know.
[4147.48 → 4148.04] Dave, what do you feel?
[4149.32 → 4151.90] Uh, yeah, I mean, definitely didn't feel great.
[4151.96 → 4155.62] I don't like it, but that's not, I'm not going to not use something because of that.
[4155.62 → 4162.28] I mean, in, in the course of debugging that horrible signal handler, MM thing, there
[4162.28 → 4166.22] were a lot of cases where I ran, I was, I spent a lot of time with the go memory allocator
[4166.22 → 4173.28] and there was an awful lot of stuff that was runtime and variance that could not be verified
[4173.28 → 4174.00] at compile time.
[4174.00 → 4177.06] And I was thinking the whole time, like, man, if this were rust, like this just couldn't
[4177.06 → 4181.00] happen, but I need to rule all these things out because I know this thing is broken and
[4181.00 → 4183.10] I don't know which of these things is broken or why or anything.
[4183.10 → 4186.58] It was definitely like a lot of convention, I guess is what I'd say.
[4186.66 → 4189.46] It was like working by a lot of convention, like a lot of C code bases do.
[4190.08 → 4190.18] Right.
[4190.28 → 4190.44] Right.
[4190.44 → 4192.78] It's like everyone has to use this function correctly.
[4193.26 → 4194.52] There are a hundred callers.
[4195.04 → 4197.40] I'm going to go check them all, you know?
[4199.18 → 4203.96] So it is all, it's also worth mentioning that one of our challenges with Cockroach is
[4203.96 → 4209.06] that we, it has been robust enough that we're kind of far behind.
[4209.86 → 4211.78] And Leana's got a great RFD.
[4212.32 → 4216.54] Leana, I know you, I, I actually, I did not, I will make that one public.
[4216.64 → 4220.22] I didn't want to make that one, Leana was out on vacation, and it felt unsporting to make
[4220.22 → 4221.96] someone's RFD public when they were out.
[4222.04 → 4222.28] I don't know.
[4222.30 → 4224.62] It just felt like, I don't know, talk about social contracts.
[4224.74 → 4227.52] Leana, I just felt like I would be violating one if I made 469 public.
[4227.52 → 4230.42] But I did, there's nothing incriminating at 469.
[4230.52 → 4231.84] I just wanted to kind of get your blessing.
[4232.10 → 4233.26] So Leana has given me your blessing.
[4233.38 → 4235.56] So I will make that public later tonight here.
[4236.62 → 4241.36] But one of the things that we had is like, okay, wow, we're really kind of far behind
[4241.36 → 4245.28] and we needed to find a way to kind of catch up.
[4245.30 → 4247.96] Because I think one of the things we were concerned about, and it actually highlighted
[4247.96 → 4252.12] another constraint that I kind of mentioned at the top, that like we actually need to
[4252.12 → 4255.88] support the stuff, support kind of pretty old versions of the stuff.
[4255.88 → 4259.80] And, you know, we're on what, 22.1.9, right, Dave?
[4260.82 → 4267.76] And I think, isn't that like out of their support window, even if we were, again, we were
[4267.76 → 4273.10] born self-supporting, but I think that is, I think that is too old, which actually in
[4273.10 → 4280.78] this case has been, I think that that has actually been helpful to us because they are not, I think
[4280.78 → 4284.06] that it is the supported releases that are being relicensed.
[4284.06 → 4287.68] If it were supported, it would also be subject to this relicensing.
[4289.52 → 4294.96] I would say, because I didn't mention this at the top, I don't like the fact that the
[4294.96 → 4296.40] patch releases are being relicensed.
[4296.40 → 4302.24] And I think that that is the one bit of this.
[4302.44 → 4306.98] There are two bits that, such as there is a social contract between Cockroach Labs and
[4306.98 → 4315.24] Oxide, or Cockroach Labs and users of Cockroach DB, of the open source fan of Cockroach DB, and
[4315.24 → 4315.96] or the public.
[4316.04 → 4318.96] There are two kind of social contracts that I think are being stretched a bit.
[4318.96 → 4323.74] One, I don't like the fact that the patch releases are, because the patch release, you're
[4323.74 → 4328.46] taking a release that was first released a year and a half ago, and you are now, there
[4328.46 → 4333.80] are potential regressions in there, and the fix for the regression is now going to be proprietary.
[4334.50 → 4335.74] More like a security update?
[4335.92 → 4336.54] That kind of sucks.
[4336.54 → 4337.12] Security update.
[4337.26 → 4337.48] I know.
[4337.62 → 4340.66] That just feels, it just, it sucks.
[4340.66 → 4345.30] And it, it, I do think, like, I don't think that that's okay.
[4345.56 → 4347.34] I don't think Cockroach Labs should get a free pass on that.
[4347.44 → 4350.98] I think that does, Tara, add a bit of the social responsibility.
[4351.32 → 4353.16] Like, if you didn't want to do it, you shouldn't have open sourced it.
[4353.70 → 4356.26] And so I think that, that is.
[4356.48 → 4357.78] I think that's what they're saying, too.
[4357.86 → 4359.14] Like, we shouldn't have open sourced it.
[4359.14 → 4361.76] I think this guy gets it.
[4361.94 → 4362.68] This guy gets it.
[4362.78 → 4364.46] That's exactly, that's what our blog entry says.
[4364.60 → 4366.92] And practically, that was a line in the blog entry.
[4367.08 → 4368.02] We shouldn't have open sourced it.
[4368.10 → 4369.68] The prevailing thesis, yeah.
[4369.68 → 4371.48] I know, you did open source it.
[4371.60 → 4372.22] That's the problem.
[4372.34 → 4373.26] You did open source it.
[4373.64 → 4375.38] So I think that that is not great.
[4375.66 → 4380.66] I also think, and I, sorry, this is the other one that I did not say at the top, but I also
[4380.66 → 4381.82] think it's not great about this.
[4382.48 → 4390.38] The all the, the blog entries and the discussion of the move to the Buts in, I believe, 2019
[4390.38 → 4391.50] has all been deleted.
[4392.38 → 4393.64] And I think that that's lame.
[4394.00 → 4395.32] Oh, that's gross, yeah.
[4395.32 → 4402.02] Because I think that, like, look, you had a bunch of rhetoric in 2019 about how Amazon
[4402.02 → 4407.92] was, and it was called out as Amazon over and over and over again, that Amazon was, you
[4407.92 → 4411.18] know, taking your product, taking your project and turning it into a service and that you
[4411.18 → 4412.80] had to punish Amazon with this clause.
[4412.80 → 4414.56] But like, that's okay.
[4415.06 → 4416.08] That's not where we are now.
[4416.66 → 4419.32] So clearly like, this is not about Amazon anymore.
[4419.72 → 4423.02] And I just think like, just to own all that and just say like, yeah, that was then.
[4423.06 → 4423.58] And this is now.
[4423.60 → 4425.94] And like, this is like how our thinking has changed and expanded.
[4425.94 → 4429.20] And I, I wish they would be a little bit more transparent about that.
[4429.20 → 4430.02] I think that's a bit lame.
[4431.20 → 4437.50] Um, but again, I don't think that they, they, the other reason I think that, that just to
[4437.50 → 4439.76] be clear, they definitely don't owe us anything.
[4439.76 → 4443.98] It's like, also cockroach could be, when we make the decision to play cockroach, cockroach
[4443.98 → 4444.94] could go out of business.
[4445.26 → 4445.62] Right.
[4445.78 → 4450.58] And that did happen to like to rethink TB, you know, rip rethink TB.
[4450.84 → 4455.52] Adam, do you remember me during my, my rethink TB?
[4455.68 → 4457.58] I know Dave wasn't, Dave was like, oh my God, you weren't.
[4457.58 → 4460.48] Yeah, no, I was going to, I wasn't going to bring it up because it was so embarrassing,
[4460.80 → 4463.98] but I remember how excited you were.
[4464.06 → 4465.74] I think we were, I think it was general excitement.
[4466.26 → 4473.58] I liked, I really liked rethink TB and, and rethink TB was, uh, and they have like a model
[4473.58 → 4476.80] that is like not an unreasonable model of it's a GPL.
[4476.80 → 4480.72] And if you want not to be a GPL, then, you know, contact us and like, well, I'm, you
[4480.72 → 4486.90] know, using this for this, you know, uh, cord up database for Thoth and, um, the
[4486.90 → 4491.96] um, but rethink TB went out of business and went out of business extremely abruptly.
[4492.70 → 4497.28] Um, and left, it doesn't matter who you were, like everybody, whether you're a commercial
[4497.28 → 4503.64] customer or an open source user, you're like, okay, like that now we're, uh, what now?
[4503.64 → 4512.46] Um, and yeah, Adam, Adam's linking to the, uh, on the CNCF and I, and I, I, you know, I, uh,
[4512.46 → 4518.22] really am, am grateful to Dan Cohn who has since passed away, but, um, Dan, who was the
[4518.22 → 4523.86] executive director of the CNCF, um, also was like, oh my God, it's like folks that are using
[4523.86 → 4526.12] these are now really stuck.
[4526.68 → 4533.40] And, uh, Dan went and found the, uh, the folks that had bitten the, the investors because I mean,
[4533.58 → 4536.06] it, rethink TB really went into the side of the mountain.
[4536.06 → 4537.42] It went quickly, right?
[4537.54 → 4538.76] Like very quickly.
[4539.40 → 4539.66] Yeah.
[4539.82 → 4541.24] I mean, it went so quickly.
[4542.00 → 4542.44] Yeah.
[4542.48 → 4543.52] Free startup advice.
[4543.72 → 4547.42] Um, if like the VCs aren't paying attention, that's not a good thing.
[4547.44 → 4548.14] That's a bad thing.
[4548.14 → 4554.28] Um, and the, uh, the, the VCs had kind of mentally zeroed it out, and I just don't think
[4554.28 → 4556.18] the executive management over there realized it.
[4556.68 → 4564.04] And by the time they realized it, like the, the, the altimeter was, was, uh, the terrain
[4564.04 → 4564.84] was coming up.
[4564.84 → 4569.68] The warnings were blaring, and that thing just absolutely went out of business within, you
[4569.68 → 4571.10] know, like very abruptly.
[4571.82 → 4577.44] And, uh, they found one of the, uh, the investors who had received all the IP Dan did.
[4577.44 → 4579.18] And he's like, actually, I kind of know these guys.
[4579.22 → 4580.08] I should just call them up.
[4580.70 → 4583.64] Um, and they had no idea what they had.
[4583.78 → 4588.26] And Dan bought it for, did I put the dollar figure in there?
[4588.84 → 4590.94] Um, he was like, what was it?
[4591.02 → 4591.78] Remind us.
[4593.16 → 4594.04] Don't read the blog entry.
[4594.14 → 4594.70] I'm sure it's in there.
[4594.74 → 4595.60] Just tell us what it is now.
[4596.60 → 4602.16] No, I was going to say, so I think it was like, they wanted 1.5 million and Dan's like,
[4602.30 → 4603.58] how about 5,000?
[4603.70 → 4606.08] And they were like, how about 10,000?
[4606.08 → 4607.44] It sounds like so old.
[4609.38 → 4615.48] So, you know, I, uh, and again, you know, Dan has unfortunately since passed away and,
[4615.48 → 4618.98] you know, Dan and I didn't see eye to eye and everything, but I was always incredibly
[4618.98 → 4622.56] grateful for what Dan did for the Rethink TV community.
[4622.56 → 4624.04] And I just like getting it out.
[4624.10 → 4629.00] I mean, even if it was lived only as kind of artifact that people could now just like
[4629.00 → 4630.26] freely borrow from, right.
[4630.28 → 4634.56] If there's any, if there's value in there, um, and it's, you know, it's, it's, it's there.
[4634.56 → 4635.36] It's, it exists.
[4635.46 → 4636.12] People can use it.
[4636.26 → 4641.18] It's not something that is current necessarily, but, um, so that could happen too.
[4641.24 → 4645.66] Like if you're using open source, like you just can't assume that like, and a commercial
[4645.66 → 4649.82] entity does not have an obligation to you to exist, and they can fly into the side of the
[4649.82 → 4652.76] mountain, and you can't really have like, you know, what are you going to have like a blog
[4652.76 → 4654.84] entry explaining how they shouldn't have flown into the side of the mountain?
[4654.90 → 4656.32] It's like, yeah, they, like, they know that.
[4656.32 → 4663.66] Um, and, uh, so I, you always have to know that, that the, the, the self-support is going
[4663.66 → 4666.86] to be, um, that's what you have to, you'd have to take that responsibility.
[4667.86 → 4671.88] And that, I mean, that is one of the benefits of, of open source.
[4672.84 → 4673.28] Yes.
[4674.46 → 4681.38] Extremely important is that, that the and I think that, you know, and again, you know, Adam,
[4681.38 → 4687.86] you and Dave and I have been through a couple iterations of this and have seen software survive
[4687.86 → 4689.06] the corporate vessel that it's in.
[4689.96 → 4697.10] And so the, the corporate vessel separating from the software is not as shocking to us
[4697.10 → 4698.26] as it might be to other people.
[4698.86 → 4701.64] And it's also not as foreclosing as it may be to other people.
[4701.72 → 4703.84] And the idea of like, oh my God, like you'll never self-support this.
[4703.88 → 4705.90] It's like, yeah, go listen to our episode on board, bring up.
[4705.96 → 4706.48] We're not worried.
[4707.42 → 4711.36] Um, you know, not to, not to minimize how hard it is to support a database.
[4711.38 → 4713.68] But I just like, I feel we can do it.
[4714.06 → 4720.62] Um, and, um, you know, I, I think that we, um, and we, I think we, we said as much in,
[4720.64 → 4726.74] in 508 that, um, we intend to allow other people to run cockroach as we're running it.
[4726.84 → 4728.70] That does not necessarily mean it's a community fork.
[4728.82 → 4730.94] I don't think it'd be interesting to see.
[4731.02 → 4732.88] I'm not sure if a community fork is going to spring up on this one.
[4732.90 → 4734.02] I got to tell you, I'm not sure.
[4735.06 → 4735.38] Yeah.
[4735.54 → 4735.90] Unclear.
[4735.98 → 4737.78] I mean, I've not seen a bunch of noise about it.
[4737.82 → 4740.24] I wonder what the community use of it is like.
[4740.24 → 4740.96] Yeah.
[4741.00 → 4744.74] So Dave, I guess maybe to bring us up to the present, I mean, what was your kind of
[4744.74 → 4746.98] reaction to the, the news?
[4747.04 → 4747.96] And did you see this coming?
[4748.04 → 4749.92] What was, what was your thought on Thursday morning?
[4750.40 → 4751.20] How did you learn about it?
[4751.68 → 4755.90] I, I checked my email like early in the day, like I might've just been in bed, just like
[4755.90 → 4757.38] open the phone and open the email.
[4757.38 → 4760.96] And I had an email, um, I think from the CEO.
[4760.96 → 4764.56] I mean, it was a blast email to everyone who was on any of their mailing lists being like
[4764.56 → 4767.56] great news for everyone who's using cockroach TV.
[4768.02 → 4769.44] And I was like, Oh no.
[4769.72 → 4770.38] Oh no.
[4770.72 → 4771.44] Oh no.
[4772.06 → 4772.68] No, no.
[4772.68 → 4774.12] It really was like good news, everyone.
[4774.46 → 4775.46] Good news, everyone.
[4775.64 → 4776.42] Oh, totally.
[4777.04 → 4778.14] Oh yeah.
[4778.28 → 4779.86] Uh, and definitely disappointing.
[4779.86 → 4784.52] I mean, I, I understand, you know, they're making an argument that like, this is better
[4784.52 → 4789.82] for a lot of people who want some of the enterprise features, but could never have gotten an enterprise
[4789.82 → 4790.26] license.
[4790.26 → 4795.70] And now that may be sort of free, I guess, but you still have to get a license key and
[4795.70 → 4798.24] like prove that you are entitled to a free one.
[4798.32 → 4798.70] I don't know.
[4799.42 → 4803.90] I don't, I mean, it seemed from the hacker news thread that some folks anyway are pretty
[4803.90 → 4804.50] happy about it.
[4804.54 → 4807.76] I don't know what most people's experience with it is.
[4807.76 → 4809.98] I was definitely not happy to learn of this.
[4811.52 → 4815.44] I'm embarrassed that I obviously I did not get the email because you know, you're on
[4815.44 → 4816.22] their lists, and I'm not.
[4816.74 → 4822.94] Um, and, uh, but I, I am embarrassed to say that I learned about this on Twitter from Adam
[4822.94 → 4823.20] Jacob.
[4823.36 → 4827.48] So Adam, you are, I'm like, I look at Adam's, I'm like, Oh no.
[4827.66 → 4829.62] And then I'm like, I wonder if anyone's talking about this internally.
[4829.62 → 4832.20] Of course, everyone, by the time I'm like, okay, I should have gone to, I should have gone
[4832.20 → 4833.12] to water cooler first.
[4833.22 → 4837.74] Everyone has been, um, the you're Matt Keeper, I think had, uh, uh, I'm like, I'm
[4837.74 → 4840.54] seeing this very early in the morning and had ice on these coasts.
[4840.62 → 4844.00] So, um, people were all avidly discussing it.
[4844.04 → 4848.06] I'm like, all right, I guess I think my, my first movement in the morning should be probably
[4848.06 → 4849.80] to our own internal chat and not to Twitter.
[4850.12 → 4851.98] But Adam, there you go.
[4852.04 → 4852.86] You're a news agency.
[4852.86 → 4860.16] Um, uh, so, and then in terms of our options, just to bring it back to kind of 508 at Dave,
[4860.20 → 4863.64] I mean, I think we, what were your thoughts in terms of our options there?
[4863.64 → 4871.96] Um, well, gosh, I mean, I mean, from first principles, we could obviously like rip cockroach
[4871.96 → 4872.20] out.
[4872.34 → 4873.14] That's one option.
[4873.42 → 4873.78] Oof.
[4874.00 → 4875.14] An incredible amount of work.
[4875.66 → 4877.52] And it is basically working for us.
[4877.60 → 4882.54] So, you know, that suggests option two, which is to just jump off the train at the point we're
[4882.54 → 4882.88] at.
[4883.94 → 4890.48] Um, sort of related option is upgrade to the latest free or greenish thing that we can and
[4890.48 → 4894.26] then jump off, but you raised the point that you raised earlier, which is like there's
[4894.26 → 4901.50] this real risk that in updating to the latest, we encounter a new problem.
[4901.80 → 4903.42] I mean, it may not even be a regression, right?
[4903.42 → 4909.42] It might just be some change in behaviour that happens to be broken for our workload and like
[4909.42 → 4911.66] not be able to get the fix, which is pretty scary.
[4912.22 → 4916.68] So, I, you know, we kind of concluded on it, and you know, you could probably speak more
[4916.68 → 4920.38] to the option of like, we'll just pay them and license it, but you kind of talked at
[4920.38 → 4922.38] the top about why we don't really want to do that.
[4923.46 → 4926.58] Um, yeah, which, which doesn't close all commercial relationships by the way.
[4926.66 → 4929.96] And there may be, you know, I, I think in my kind of ideal world, there'd be a commercial
[4929.96 → 4935.26] relationship that allows us to get like some of those patch releases open source, you know,
[4935.28 → 4936.30] or I don't know.
[4936.60 → 4939.16] I, I, I think that we, um, we'll see.
[4939.16 → 4945.18] Um, but I would love to have a way of getting us to something that is, um, that we, because
[4945.18 → 4949.34] we have, we have seen issues that were, you know, we, we've seen the upgrades have been
[4949.34 → 4956.74] good news for cockroach, not bad news, which broadly, which is not the case for all software.
[4957.74 → 4964.26] Um, and then someone's, uh, the Leana had said in the chat that I think very aptly, like
[4964.26 → 4967.20] it's going to be hard to self-support a database, but it's not the hardest thing we've done.
[4967.76 → 4970.42] And someone's like, all right, well, what metrics do you use for that?
[4970.42 → 4973.70] Um, and I, I w which is a very valid question.
[4974.06 → 4979.02] Um, I would say it's not the hardest thing we've done because it doesn't feel like existential
[4979.02 → 4979.56] risk.
[4979.90 → 4986.12] Um, and we've got, um, an extraordinary amount of software expertise, um, at oxide.
[4986.28 → 4991.38] Um, we've had some terrifying things that were, that did feel like, well, if we don't
[4991.38 → 4995.42] find this, if, if the, the nick doesn't come out of reset, like we don't have a company,
[4995.42 → 5001.04] or if the CPU doesn't come out of reset, we don't have a company, or if the if we can't
[5001.04 → 5003.70] get that lowest level of platform enabled software working, we don't have a company.
[5004.10 → 5007.90] Um, and so we, we've, we've had some things that have been really, terrifying.
[5008.28 → 5014.56] Um, but, but we, we, we've also, I mean, God, I, I'd be loved to get your perspective on
[5014.56 → 5019.80] it, uh, Dave and Adam, but I feel with any, you know, Alan Hanson, our, our colleagues has
[5019.80 → 5025.12] pointed this out a couple of times that every time we knock one of those things down as a
[5025.12 → 5027.32] team, I think it improves.
[5027.48 → 5031.16] It, it, it, it gives us confidence that we can knock down the next thing.
[5031.62 → 5037.28] Um, and I, you know, I, I don't think it's, I just feel like, man, if we hold together
[5037.28 → 5040.24] and like, we can, we can do it, we can figure it out.
[5040.34 → 5044.34] Uh, it would just not say like, it could be really, really hard.
[5044.60 → 5047.82] And, uh, but if it's really hard, I mean, that's podcast content, right?
[5048.64 → 5050.52] Now you're talking, I got it.
[5050.54 → 5053.64] I have to tell you, you know, as someone like, you know, Adam's looking at the numbers, he'll
[5053.64 → 5054.36] tell you stuff.
[5055.16 → 5055.56] Yeah.
[5056.12 → 5060.04] And like, I totally agree with you, Brian and agree with Alan's sentiment there.
[5061.04 → 5066.96] And like, this is not to diminish the complexity of these things, but we're, we're pretty good
[5066.96 → 5067.38] at software.
[5067.60 → 5071.24] We're pretty good at debugging and cockroach has been great.
[5071.62 → 5073.50] It's been very solid for us.
[5073.80 → 5078.18] So the other thing is like, we've been running this stuff in production for years now.
[5078.18 → 5083.20] Like it's not, it's, I mean, I guess tomorrow we could have some horrible, impossible to
[5083.20 → 5085.22] debug problem, but like it obviously will.
[5085.50 → 5090.02] I mean, so we're sitting here like on our knees begging for it.
[5090.08 → 5094.98] And the gods are like this guy again, how many times do we have to punish this guy before
[5094.98 → 5095.66] he stops doing this?
[5095.78 → 5100.78] Like, Oh, if you're going to make this judgment about like how much work is it going to be
[5100.78 → 5104.36] to support this thing based on the last couple of years of self-supporting it?
[5104.36 → 5107.08] Like, like, I mean, you would look to that, right?
[5107.22 → 5109.10] And it's like, well, we actually haven't spent that much.
[5109.26 → 5112.60] The most effort we spent by far was what turned out to be the OS bug.
[5112.84 → 5113.64] Yeah, absolutely.
[5114.12 → 5116.62] Well, by like an order of magnitude or two.
[5116.84 → 5122.52] Not only have we not invested much, we haven't even sort of taken the time to upgrade us to
[5122.52 → 5123.70] a more modern version.
[5124.84 → 5126.96] In part because we hadn't, haven't had to.
[5127.38 → 5133.24] And then that turns out to be pretty lucky where it's going to roll over to be Apache 2 in
[5133.24 → 5138.76] nine months, as opposed to, you know, multiple years, if we had been a little more diligent
[5138.76 → 5139.44] about upgrading.
[5141.06 → 5141.42] Absolutely.
[5141.80 → 5145.24] We've got, so, I mean, the fact that it is actually going to be that we are with every
[5145.24 → 5149.34] passing day, this is getting closer and closer to being, and again, we're not worried about
[5149.34 → 5149.84] the Basil.
[5150.00 → 5151.22] They've constructed that clause.
[5151.36 → 5153.00] Well, we are not violating it.
[5153.08 → 5153.74] It would not be.
[5153.86 → 5154.80] So we're abiding by it.
[5154.86 → 5155.34] It's all fine.
[5155.68 → 5158.08] But boy, it being Apache 2.0 would be great.
[5158.50 → 5159.02] Yeah, totally.
[5159.54 → 5159.88] Yes.
[5159.88 → 5162.84] I did, like, did you see Steven O'Grady's tweet on that?
[5163.00 → 5163.66] I thought it was pretty funny.
[5163.96 → 5164.14] Yeah.
[5164.28 → 5164.66] What do you say?
[5165.42 → 5169.68] It's like, well, Oxide would be the first company that would be deploying something that
[5169.68 → 5171.58] basically had timed out into Apache.
[5172.30 → 5175.74] And again, or once again, Oxide goes its own way.
[5176.26 → 5178.78] Like, you bet maybe Oxide goes its own way.
[5179.12 → 5185.50] You know, the Basil, I had previously thought that flip over to open source was kind of baloney,
[5185.58 → 5186.48] was kind of window dressing.
[5186.48 → 5187.28] Yeah.
[5187.68 → 5192.26] Like, kind of thinking, well, who wants three-year-old software anyway?
[5192.92 → 5194.44] But it turns out, like, that was way wrong.
[5194.44 → 5200.12] People running two-year-old and three-month-old software, actually, are counting down the months
[5200.12 → 5200.50] to three.
[5200.56 → 5201.04] Yeah, totally.
[5201.36 → 5202.00] I feel the same way.
[5202.12 → 5203.56] I felt like, and actually, you know what?
[5203.62 → 5204.04] It was funny.
[5204.10 → 5206.54] It's like, I actually thought it was five years.
[5207.90 → 5212.38] And it was only when Matt, I think, in our internal chat was being like, oh, wait a minute.
[5212.74 → 5213.66] And I was doing the math.
[5213.70 → 5214.26] I'm like, wait a minute.
[5214.26 → 5215.02] It's only three.
[5215.06 → 5215.52] Oh, wow.
[5216.28 → 5216.48] Wow.
[5216.58 → 5220.78] Three years feels like a really long time and is in some regards, but, like, is not.
[5221.28 → 5228.02] So we, so I think that, you know, we are, our path is pretty clear here.
[5228.02 → 5233.38] And Dave, I felt like that was, as a result, like, this just doesn't feel that anxiety
[5233.38 → 5235.78] producing relative to the other crises.
[5236.52 → 5236.72] Right.
[5236.90 → 5240.68] I think it's like, you could reasonably ask, like, is this the 10-year plan?
[5240.92 → 5246.38] Are we, are we in 10 years going to be running Cockroach 2219 on the go version that's there?
[5246.38 → 5248.68] And, like, I'm sure we will run into problems.
[5249.36 → 5255.82] Like, you know, the DLS that is in there is no longer allowed by any of the clients that we want to use or something like that.
[5255.90 → 5263.74] But, like, these are not, oh, my God, we need to rip everything out and rewrite, you know, how we use the control plane data store problems.
[5263.82 → 5264.34] You know what I mean?
[5264.34 → 5268.16] These are like, okay, we'll deal with those problems when they come up.
[5268.92 → 5269.42] That's right.
[5269.54 → 5270.42] We got some work to do.
[5270.60 → 5272.42] But we always have some work to do.
[5272.54 → 5278.90] When a customer has 100 oxide racks, you know, spanning multiple geos, and are we revisiting the decision?
[5279.02 → 5279.90] Like, conceivably.
[5280.64 → 5282.62] Like, when that happens, sure.
[5283.70 → 5291.00] Yeah, I mean, and Andrew, I'm not sure if Andrew is lurking, but our colleague Andrew Stone is just, like, itching to write the RFD on what the he's like.
[5291.00 → 5304.64] Because we will, I mean, like, the next step for us, unless, I mean, if we hit something that invalidated Cockroach with a new use case or what have you, I mean, we'd probably, like, go back to the rubric a little bit, Dave.
[5304.68 → 5308.36] And I think it would be, you know, I think we would kind of reevaluate everything at that point.
[5308.78 → 5311.54] And who knows what that world would look like.
[5312.88 → 5316.08] And will we be writing our database before or after we're doing our own ASIC?
[5316.30 → 5317.16] Only time will tell.
[5317.16 → 5323.32] Well, these are two things that we believe we will do in the fullness of time, but not today.
[5326.98 → 5329.46] Well, Dave, this was great.
[5330.94 → 5333.32] And great to talk about the kind of the whole rubric.
[5333.50 → 5340.48] I really would encourage people to check out not just the rubric, but all the evaluation you did.
[5340.48 → 5346.94] I really do think it's a model for, and Dave, especially because you didn't, like, think of this as all being public.
[5347.18 → 5351.64] But I think our disposition is to be, is to get as much of the stuff out there as possible.
[5352.84 → 5357.54] Yeah, if you really go digging, you can find my day-to-day notes and all the stupid missteps I made along the way.
[5357.72 → 5358.58] I discovered them there.
[5359.64 → 5361.92] But it was actually fun going through the history again.
[5362.74 → 5364.26] It was fun going through the history again.
[5364.26 → 5368.28] Yeah, it was fun just because I also feel that, like, damn, this analysis is perfect.
[5368.62 → 5371.06] And then you were like, God, was it?
[5371.22 → 5374.60] Because I don't remember at the time, you're just like, am I spending too much time on the analysis here?
[5374.62 → 5375.76] It's like, no, definitely not.
[5375.84 → 5381.02] This is an perfect use of time and gave us a lot of confidence in the decision.
[5382.16 → 5387.62] And, you know, I think it's been terrific to get these RFDs out there.
[5387.62 → 5392.60] And thank you for both 53 and 110.
[5392.60 → 5395.26] Two RFDs that I definitely, like, appreciated at the time.
[5395.56 → 5399.60] But there's always, like, an R, you know, the RFD that you read, and you're like, oh, yeah, this seems great.
[5399.94 → 5403.02] And then all of a sudden something changes where it's like everything's low-bearing.
[5403.20 → 5407.30] In some cases, like, for me, that's like, okay, I'm actually implementing this bit now.
[5407.52 → 5411.70] Or, like, now this has become an issue that is a hot issue the way it is with cockroach.
[5411.72 → 5414.02] So now I'm, like, reading every word of this RFD.
[5414.02 → 5420.72] I would love to tell you that I read 110 as closely then as I did after Thursday, Dave.
[5421.00 → 5424.58] But the and just remind me, this is perfect.
[5424.64 → 5424.86] What's that?
[5425.38 → 5427.92] I wouldn't blame you for not saying that the first time around.
[5428.90 → 5432.94] Well, just like, it'd be just because, like, your metric is totally different, right?
[5433.00 → 5436.38] In terms, and it was just great to go back and reread all that.
[5436.88 → 5443.52] It was also great, and this is a segue, a teaser for, Adam, we are doing something.
[5444.02 → 5446.02] It's nearly unprecedented for Oxide.
[5446.10 → 5447.28] I'm not going to say totally unprecedented.
[5448.02 → 5450.12] Yeah, I think it's only maybe happened once or twice before.
[5450.20 → 5451.20] It's happened once or twice.
[5451.38 → 5454.06] We are scheduling an episode in advance.
[5454.28 → 5455.94] Only one week in advance, but still.
[5456.38 → 5457.60] I mean, it's pretty amazing.
[5457.74 → 5458.06] A whole week.
[5458.20 → 5459.32] Yeah, a whole week.
[5459.42 → 5460.48] An entire week.
[5460.96 → 5461.30] An entire week.
[5461.36 → 5467.02] Of course, this is going to be the week that, like, Oracle acquires Broadcom.
[5467.02 → 5471.44] And they both merged with the Linux Foundation or something.
[5471.58 → 5477.60] And there's something, you know, something absolute, like, absolute spectacularity is basically guaranteed this week.
[5478.74 → 5482.04] The like, Eric Schmidt's going to shoot his mouth off again.
[5482.10 → 5484.12] He's going to go off and be more excited diatribe.
[5484.30 → 5484.96] He's going to be like, oh, wait a minute.
[5485.02 → 5486.32] Oxide and Friends can't talk about it on Monday?
[5486.44 → 5488.98] Okay, I want to get back to that return to the office thing I was getting on.
[5489.16 → 5489.48] That's right.
[5489.60 → 5491.34] It's a good time to bury all your news, folks.
[5491.92 → 5492.80] Bury all your news.
[5492.90 → 5493.70] Get it out there now.
[5493.70 → 5498.34] But we are going to talk about RFDs.
[5498.54 → 5503.96] And we're going to talk about why we developed RFDs, how we've used them.
[5504.06 → 5509.60] But very importantly, we're going to talk about the actual mechanics that we've developed.
[5510.54 → 5512.90] And our colleagues, Ben Leonard and Augustus Mayer, are going to join us.
[5512.94 → 5513.82] I'm really excited about that.
[5514.08 → 5520.56] Because something that was really important here is our ability to make individual RFDs public.
[5520.56 → 5523.60] And that really relies on the RFD site, which has been great.
[5524.22 → 5526.86] And so we can go through and share this stuff with you.
[5527.12 → 5529.32] And that's been really, really helpful.
[5529.68 → 5531.72] And it's been our disposition for more and more RFDs.
[5532.44 → 5534.06] Although we do wait for people to get back from vacation.
[5534.38 → 5535.48] So, Liana, thank you for your blessing.
[5536.68 → 5537.86] But really looking forward to that one.
[5537.86 → 5545.62] And, Adam, because Ben is in the UK, and you are going to be in Europe.
[5546.14 → 5551.08] So this is going to be a European-friendly episode on RFDs.
[5551.14 → 5554.10] And we're going to do it at 9 a.m. Pacific on Monday.
[5554.26 → 5559.82] It's going to be, which I understand to be 5 p.m. in London and 6 p.m. in Europe.
[5560.14 → 5561.08] Allegedly, yes.
[5561.08 → 5561.40] Allegedly.
[5562.40 → 5572.48] So I apologize to all of Europe for having to catch us on time delay or in Trance waking up at 3 in the morning or whatever it is in Armenia.
[5572.72 → 5575.74] But this is going to be a great one.
[5575.88 → 5576.72] I'm really looking forward to that.
[5576.84 → 5579.10] Because that RFD site has been really, really important.
[5579.60 → 5580.84] And someone's saying in the chat, it's gorgeous.
[5580.98 → 5581.62] It really is gorgeous.
[5581.72 → 5582.56] It looks great on mobile.
[5583.52 → 5586.70] And there's a lot of technical meat behind it.
[5586.70 → 5590.70] And then that's been extremely important for the way that we do engineering.
[5590.98 → 5593.12] I think Adam and Zoo ten are kicking around titles.
[5593.46 → 5595.40] We are calling it the backbone of oxide.
[5595.92 → 5596.52] It really is.
[5596.90 → 5597.40] It really is.
[5599.14 → 5599.72] All right.
[5599.92 → 5602.78] Dave, thank you very much for joining us.
[5602.86 → 5605.26] You should join us next week, too, on RFDs, man.
[5605.36 → 5606.42] I know.
[5606.72 → 5610.06] But I really, really appreciate you joining us in the evening hours here.
[5610.56 → 5610.70] Yeah.
[5610.78 → 5611.44] Thanks for having me.
[5611.64 → 5611.96] It's been great.
[5612.96 → 5613.94] Really great stuff.
[5613.94 → 5619.00] So, on the one hand, it was a bit of a downer to get the news.
[5619.12 → 5621.44] But on the other hand, I think it was a real opportunity.
[5622.46 → 5624.44] When one door closes, another door opens.
[5624.76 → 5627.04] And it was great for us to be able to get all this stuff public out there,
[5627.12 → 5630.82] describe what we're doing, and really know our own fate.
[5631.02 → 5633.52] It's always nice to know where you're going.
[5636.00 → 5636.60] All right.
[5636.98 → 5640.96] Adam, when we talk next, you will be on a distant shore.
[5640.96 → 5641.96] And we will be talking RFDs.
[5642.88 → 5643.50] Looking forward to it.
[5643.94 → 5644.32] All right.
[5644.44 → 5644.96] Thanks, everybody.
[5645.10 → 5645.76] Talk to you next time.
