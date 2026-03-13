• Introduction and banter among the hosts
• Discussion of a previous episode on sagas and the hosts' decision to not reveal the topic for 17 minutes
• Introduction of Cockroach DB and its role in the company's data repository
• Explanation of the company's decision to use Cockroach DB and its evaluation process
• Discussion of Cockroach Labs' move to a proprietary license and the company's response, including a public RFP
• Reference to a Hacker News thread and a comment about the company "lamps as a computer company"
• Discussion of the RFP's unexpected attention and praise from Kelsey Hightower
• Appreciation for the work done in RFPs 53 and 110 in evaluating and selecting Cockroach DB
• Mention of a comment online referencing the "garment" and the hosts' decision to save it for a later episode
• Discussion of going back in time to 2020 to explore the company's decision to use Cockroach DB
• Cockroach Labs relicensing Cockroach DB, raising concerns about social contracts and the future direction of the company
• Discussion of the business source license and its implications for users
• Importance of social contracts in the open-source community and the role of contributors to Cockroach DB
• Concerns about telemetry and data collection, particularly in secure environments
• Difficulty in negotiating a perpetual royalty-free license with Cockroach Labs
• Importance of having control over pricing and being able to make guarantees about software compatibility
• Reaction to the decision to relicense Cockroach DB, with some suggesting that Postgres could have been used instead
• Discussion of Postgres implementation at Joy ant
• Manta system: HTTP object store with strong consistency and directory structure
• Postgres as metadata tier for high availability and horizontal scalability
• Criticism of decision-making process, relying on reputation and experience
• Contrast with later decision-making process, involving rigorous evaluation
• Sharded Postgres for metadata tier in production deployment
• Reflection on lessons learned and future decision-making processes
• The speakers discuss their experience with high availability and horizontal scalability in a database system, specifically with Postgres.
• They mention the use of synchronous replication and a consistent hashing system to manage high availability.
• They discuss the challenges of running a large-scale database, including pathological performance and 6-hour outages due to a "wrap around auto vacuum" issue.
• The speakers compare their experience with modern distributed databases, such as Cockroach DB.
• They discuss the difficulties of operationalizing Postgres, including poorly documented behaviour and hard-to-work-around issues.
• They share a specific example of a problem with Postgres's replication logic, which caused replication to be days behind and led to long outages.
• Postgres replication has "ridiculously sharp edges and steep cliffs" that can undermine its reliability narrative
• The issue of synchronous replication applies lag and "secret lag" can lead to unmonitored and unmanaged replication gaps
• There is a lack of documentation and testing around these issues, leading to unexpected problems during high-load or high-throughput scenarios
• The importance of fault testing and understanding the limits of a system through bad experiences rather than anecdotal good experiences
• The challenge of drawing conclusions from good experiences with software and the importance of probing system limits to understand their capabilities.
• The speakers discuss a experience with a database that was built in an era where downtime was acceptable and DBA's were responsible for maintenance.
• They compare this to modern databases that prioritize zero downtime, horizontal scalability, and high availability.
• The speakers mention Postgres as an example of a database that was built in an earlier era and is not well-suited for modern needs.
• They discuss their own data nightmare and how it was eventually solved by debugging a configuration problem.
• The speakers reflect on the importance of finding a database that aligns with their values and needs.
• They introduce oxide as a new world of distributed databases and discuss the benefits of using a New SQL database like Cockroach DB.
• The speakers highlight the importance of stress testing and verifying a database's properties with respect to the CAP theorem.
• Discussion of testing and evaluation of various distributed databases, including Cockroach DB, Gabite, Tiki, Tide, and Foundation DB.
• Concerns about operability, crash recovery, and data loss in the context of a distributed system for space missions.
• Importance of autonomous operation and hands-off maintenance in a distributed system.
• Evaluation of Cockroach DB's strengths, including ease of use and hands-off operability.
• Review of testing and evaluation methods used for Cockroach DB, including online expansion, online contraction, and online schema change.
• Discussion of Cockroach DB's weaknesses, including crash behaviour and data loss.
• Praise for Dave Pacheco's rigorous approach to engineering and evaluation.
• The evaluation repo is detailed and thorough, with graphs and analysis that show the rigour of the work.
• ChatGPT could potentially automate some of the tasks, but the work was done by hand to provide a detailed analysis.
• The evaluation process involved two rounds of testing, with the first round encountering issues due to CPU and IO starvation.
• The team discovered a specific AWS behaviour where provisioned IOPS are given for free during the initial boot process, but then limit out after a certain time.
• Consistency is a key consideration in the database, with the team aiming for strong consistency to provide a good user experience.
• The evaluation repo is not just about documenting issues, but also about providing a detailed analysis of the performance and behaviour of the system.
• Consistency and availability of small databases and control plane instances
• Use of transactions for complex decisions and state changes
• Examples of transactions in provisioning and reconfiguration processes
• Importance of consistency in scenarios like sagas
• Experience with Cockroach DB, including advantages and drawbacks
• Cockroach DB's cluster convergence and replication features
• Cockroach DB's client-side retries and differences from Postgres
• Cockroach DB's handling of concurrent transactions and node failures
• Optimistic concurrency control and its limitations
• Interactive transactions and the need for client-side handling of retries
• Autonomous operation of Cockroach DB and its monitoring
• Data integrity and potential issues with client-side code and Rust async cancellation
• Experience with Cockroach DB compared to Postgres, including issues with replication and data corruption
• Data corruption issues with Cockroach DB
• Discussion of using open source vs. proprietary Cockroach DB builds
• Importance of self-sufficiency in software support and maintenance
• Experiences with Cockroach DB engineering team and issue resolution
• Opinions on using Go as a programming language for software development
• Comparison of Go with other languages, such as Rust and C++
• Concerns about making someone's RFD (request for discussion) public while they're out of vacation
• Discussion of patch releases being relicensed, violating a social contract
• Criticism of Cockroach Labs for not supporting old versions of the software
• Concerns about transparency and the deletion of blog entries and discussions about the company's past actions
• Comparison to Rethink DB's abrupt shutdown and the subsequent consequences for its users
• Discussion of a specific blog entry or article
• Mention of Dan, a former developer who has passed away
• Explanation of the concept of self-support in open-source software
• Discussion of the implications of a commercial entity abandoning a project
• Explanation of how open-source software can survive the departure of its original developers
• Discussion of the potential for a community fork of a project
• Reaction to the news of a project's abandonment
• Discussion of the options available to the team, including ripping out the project, upgrading to the latest version, or paying for a license.
• Discussion of Cockroach DB's self-supporting database and its potential difficulties
• Comparison of Cockroach DB's challenges to previous, more critical issues faced by the company
• Confidence in the team's ability to overcome challenges due to experiences
• Acknowledgment of the complexity of supporting an older version of Cockroach DB (version 2)
• Discussion of the company's past efforts to upgrade and its potential consequences
• Joking about the company's tendency to stick with older versions of software
• Acknowledgment of the need to address potential issues with Cockroach DB's TLS and client compatibility in the future
• Discussion of the company's ability to adapt to future problems and challenges.
• Discussion of writing an RFP for Cockroach
• Review and evaluation of the rubric for NS
• Publication of RFPs and analysis
• Scheduling a future episode to discuss RFPs and mechanics
• Announcement of a European-friendly episode on RFPs
• Discussion of the RFP site and its importance for engineering
• Review of the RFP process and plans for future episodes
• The meeting appears to have concluded.