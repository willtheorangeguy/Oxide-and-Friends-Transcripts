• The hosts discuss their return to a more spontaneous and unscripted format, referencing their "hurry-up offense" style
• They mention a comment from a listener who appreciated their return to this format
• The hosts discuss their previous episode on sagas and how it was a more structured and planned conversation
• They talk about their use of Cockroach TV, a data repository, and how they evaluated different options before deciding on it
• They discuss a recent controversy surrounding Cockroach Labs' decision to relicense aspects of their open-source project under a proprietary license
• They mention the release of an RFD (Request for Discussion) document that outlines their decision-making process and reasoning for this change
• The hosts discuss the attention their RFD received on Hacker News and the reactions from listeners and detractors
• Discussion of Kelsey Hightower's tweet about RFT 508
• Suspicions about Cockroach Labs' intentions
• Review of RFT 53 and RFT 110's impact on the decision to select CockroachDB
• Mention of a past podcast episode on corporate open source anti-patterns
• Concerns about social contracts between Cockroach Labs and Oxide
• Discussion of the importance of social contracts and their implications
• Acknowledgement of Cockroach Labs' right to relicense their software
• Concerns about the direction of the company and potential future incompatibility of values or use cases
• Licensing issues with Cockroach Labs, specifically requirements for $10 million ARR and mandatory telemetry
• Incompatibility of Cockroach Labs' terms with the company's needs and values
• Difficulty negotiating a perpetual royalty-free license with Cockroach Labs
• Importance of the company having control over its own pricing and value
• Concerns about long-term support and guarantees for customers using the company's software
• Discussion about a previous podcast topic and the host's confusion about its length
• Mention of Postgres and its potential use as a database solution
• Experience with Postgres at Joint, including a system called Manta
• Design considerations for Manta, including strong consistency and directory structure
• Implementation of Manta, including storage and metadata
• Requirements for high availability and horizontal scalability in a cloud service
• Choice of Postgres for Manta due to its reputation for data integrity and performance
• The speaker fired their postmortem lawyer and is now working with a public defender.
• The speaker reflects on a past decision-making process that was based on "vibes" and reputation rather than rigorous analysis.
• The speaker acknowledges that this is a common approach to decision-making in the tech industry.
• The speaker discusses how they would have approached the decision-making process differently if they had been more aware of the potential pitfalls.
• The speaker notes that the decision-making process was flawed, but it ultimately led to some successful outcomes.
• The speaker discusses the importance of verifying the properties of a system through independent testing, rather than relying on reputation or anecdotal evidence.
• The speaker summarizes the postmortem of a past project, which involved sharding Postgres for high availability and horizontal scalability.
• The speaker notes that CockroachDB is a solved problem in modern distributed databases, and they didn't want to redo existing work.
• The team's experience with Postgres highlighted its limitations in terms of design decisions made in an era where there was less traffic and fewer scalability issues.
• The team had issues with minor outages and pathological performance due to insufficient auto vacuum and inefficient use of primitives in the compute tier.
• A specific outage occurred on July 27, 2015, due to a latent bug in the configuration or setup of the system, which only manifested after 200 million transactions.
• The team's problems with auto vacuum and synchronous replication increased as they tried to scale their production, leading to operational challenges.
• The difficulties of working around issues in Postgres, particularly with wall replication
• The problem of synchronous replication lag, which can build up and cause replication to fall behind
• The issue of single-threaded replay logic on the secondary node in Postgres
• The consequences of this issue, including delayed replication and potential database downtime
• The experience of the speaker and others with Postgres, including hidden sharp edges and steep cliffs in the system's functionality
• The need for transparency and honesty about the limitations and challenges of using Postgres
• Shipping write ahead log from primary to secondary
• Two steps: sending data and writing it durably to disk and F-sync, and applying it to the live database on the sink
• Synchronous with respect to sending and writing, but not with respect to application
• Apply lag and potential for secret lag and double secret lag
• Importance of testing replication under high load conditions
• Difficulty of drawing conclusions from anecdotal good experiences with software
• Need for bad experiences to provide valuable insights into system limits
• The speaker regrets not testing a database solution themselves instead of relying on others' opinions
• The speaker is wary of "vibes" and instead wants to verify information through testing
• A colleague was once yelled at over a disagreement on a database solution, causing significant stress
• The speaker's team had a poor experience with Postgres due to its limitations and potential for downtime
• Modern databases are designed with zero-downtime and high availability in mind, unlike Postgres
• The speaker is cautious about using Postgres again due to past experiences and limitations
• They've considered other databases like Cassandra and learned from their own and others' experiences
• The team's nightmare with Postgres was ultimately a configuration problem, not a technical issue
• GC times were discussed as a potential issue
• Cassandra consultant was brought in to assess the situation
• Oxide's distributed database control plane was discussed
• NewSQL databases, including CockroachDB, were evaluated for potential use
• CockroachDB's strong Jepsen report and hands-off operability were cited as reasons to choose it
• The importance of shipping a working distributed system as a product was emphasized
• Implicit dependency on an operator in cloud SaaS era
• Autonomy and automation of system operations
• Comparison of various database systems, including Yuga Byte, TIKV, TIDB, and FoundationDB
• Strengths and weaknesses of Cockroach and FoundationDB
• Online expansion, contraction, and schema change testing of Cockroach
• Comparison of various database systems' operability and reliability
• No data loss was experienced during testing
• Cockroach DB was prone to crashing when clocks were out of sync, but this was resolved with the use of crony
• The evaluation repo for Dave's work was found to be thorough and well-maintained
• The report on joint's problems was detailed and helpful in identifying issues
• The importance of analyzing latency and small spikes in latency was highlighted
• The testing was conducted in two rounds, with the first round experiencing issues but the second round being successful
• The team experienced CPU and IO starvations during testing, which were resolved by increasing resource limits.
• The AWS environment has a unique behavior where it provides high IOPS for a short period (4 hours) when a VM is provisioned or rebooted, but then limits are hit.
• This behavior can be confirmed through cloud metrics, and it's a common issue that people may not be aware of until they experience it.
• Consistency was a crucial requirement for the RFT53 database due to the importance of user experience and the potential for eventual consistency to lead to unexpected behavior.
• The small size of the database and expected throughput made consistency a feasible goal.
• Consistency and availability of resources
• Pathological behavior when resources are not available
• Importance of explicit failure and provisioning success
• Provisioning transactions for complex resource allocation
• Use of transactions in database queries (CTEs in SQL)
• Example of using transactions in the Reconfigurator system
• Importance of consistency in decision-making processes
• Use of transactions in saga patterns
• Experience with CockroachDB
• Drawbacks of CockroachDB, including partial index corruption
• Benefits of CockroachDB, including self-healing and visibility
• Challenges of CockroachDB, including retry mechanisms and transactional consistency
• Comparison to Postgres, including differences in architecture and behavior
• Challenges with database retry mechanisms and replaying conversations
• Need to build a mechanism for handling dependent queries in transactions
• Autonomous operation of CockroachDB has been mostly successful, but lacks comprehensive monitoring
• Comparison to Postgres experience at Joyant, where replication issues were common and required manual intervention
• Two instances of questioned data integrity were unrelated to CockroachDB, attributed to OS issues and client-side Rust async problems
• Discussion of a specific client-side bug that led to a long-standing transaction in a "fantasy land"
• Data accumulation and storage concerns
• Transactional issues with database and data corruption
• Debugging odyssey with CockroachDB
• Decision-making around proprietary vs open-source components in CockroachDB
• Self-supporting nature of database setup and maintenance
• Concerns about open-source license and community license implications
• Filing issues with Cockroach DB and experience with their engineering team
• Difficulty with workload and memory management in Go
• Previous issue with YMEM registers not being restored properly, and positive experience with Cockroach DB's engineering team
• Current use case for Go in CRDB and general feelings about it
• Challenges with working with Go, including lack of compile-time verification and reliance on convention
• Concerns about violating a social contract by releasing information publicly
• Patch releases being relicensed, allowing proprietary fixes for potential regressions
• Two social contracts being stretched: between Cockroach Labs and Oxide, and between Cockroach Labs and users/public
• Criticism of Cockroach Labs not being transparent about how their thinking has changed regarding Amazon and relicensing
• Transparency about deleted blog entries and discussion of the 2019 move to the Bucel
• Discussion of whether Cockroach Labs owes anything to users or should be transparent about their decision-making process
• Rethink TB and its GPL model
• Abrupt closure of Rethink TB due to lack of VC attention
• Dan Cohn's efforts to save IP and assets
• Sale of Rethink TB's IP for $5,000
• Importance of self-support in open-source projects
• Risks of relying on commercial entities for software sustainability
• Benefits of open-source for project sustainability
• Corporate vessel separating from software
• Concerns about self-supporting a database
• Possibility of community fork
• Reaction to news of corporate vessel separating
• Discussion of enterprise features and licensing
• Options for handling situation, including ripping out cockroach or upgrading and then leaving
• Risk of encountering new problems when updating to the latest software version
• Difficulty of self-supporting a database and the need for expertise
• Oxide's experience with complex software issues and debugging
• Comparison of current situation to past challenges and successes
• Limited investment in self-supporting the database and potential future upgrades
• Concerns about meeting the "busil" clause and adhering to the Apache 2.0 license
• Discussion of the potential benefits of being part of the Apache 2.0 project
• Reference to a tweet by Steven O'Grady about the project
• Reflection on the company's decision to open-source its software and how it has been received
• Discussion of the company's long-term plans and the potential for future problems
• Consideration of the company's current software and hardware setup and the possibility of revisiting decisions made in the past
• Mention of a colleague's desire to write a Request For Discussion (RFD) document on the company's decision-making process
• Discussion of the company's future plans, including the possibility of writing its own database and developing its own ASIC.
• Discussion of time spent on analysis and confidence in decision-making
• Review of RFDs (Request for Decision) process and importance of reading and re-reading RFDs
• Upcoming episode on RFDs, with guests Ben Leonard and Augustus Mayer
• Scheduling of episode in advance, a rare occurrence for Oxide
• Discussion of Oracle and Broadcom merger and potential impact on episode
• Burying news, including the return to office discussion, until a later time
• Mechanics of RFDs and public individual RFDs
• Importance of RFD site and sharing RFDs with the public
• European-friendly episode time and format
• Discussion of Dave's visit and invitation to join again
• Dave's reflection on recent news and its opportunities
• Mention of a door closing and another opening
• Discussion of making information public and knowing one's fate
• Adam's impending travel and planned future discussion on RFDs
• Closing remarks and thanks to the audience