• Discussion of the Memorial Day weekend and the Ballers baseball team
• Viewers watching the team's road trip online
• Personal account of watching the team's games and enjoying the experience
• Conversation about the team's performance and potential supporters
• Introduction of other viewers and potential supporters
• Discussion of a previous incident or anniversary (10th anniversary of an incident)
• Exchange about the duration of time spent researching the incident's date
• Attempt to bargain or negotiate about the discussion's direction or content
• A massive outage occurred 10 years ago today
• The outage affected a large portion of the company's infrastructure, including the website and key systems
• The company rebooted their most important data center, U.S. East 1
• The incident was surprising and unsettling, with participants recalling their reactions and trying to make sense of what happened
• The company had backup plans in place, including access to Slack and IRC
• The participants reflect on how they would have communicated and coordinated if the outage had been more severe
• Discussion of a past event where the speaker and others experienced a terrifying moment
• The speaker's recollection of being unable to think and potentially catatonic for a brief moment
• Explanation of the company's architecture and how it contributed to the situation
• Discussion of a technical issue with the database and how it was eventually resolved
• Details about the number of machines that were intended to be rebooted and the subsequent consequences
• Thousands of machines were in a state where they could be rebooted multiple times without issue due to a specific command error
• The machines were running an error-prone command that failed to elide an argument specifying the node
• The command was incorrectly specifying a comma-separated list of hosts, without a prefix indicating the type of command
• This caused the system to ignore command syntax validation and concatenate the command, sending it as a single command
• The system would have executed the command "hostname reboot" and returned an error if it had not been for the use of a specific flag (-T1) that bypassed the waiting for the reboot command to exit
• The flag (-T1) caused the system to return immediately, bypassing the waiting time for the reboot command to exit
• Discussion about a post-mortem analysis of a system failure
• Mention of a bespoke options parser and criticism from Mr. Cluelo
• Use of the get ops library instead of writing a custom parser
• Reference to a timeout setting that ignores all failures
• Discussion of exit code 113 and its significance
• Introduction of a new topic: a tool called STC that uses rabbit MQ to speak to the UR agent
• Explanation of the UR agent and its role in executing commands
• Comparison of the safety of curl pipe to sudo versus STC
• Discussion of a vulnerability in the Triton control plane
• Mention of a controlled admin network and its security features
• Discussion about the significance of the number 215 and 113
• Mention of a kernel group or manager communication on February 15th
• Reference to a Jira issue about in-band signaling and colors in Jira text
• Explanation of a temporary hack in 2011
• Discussion about the source code and its claims about exit code 113
• Explanation of the 30th prime number and Einstein prime connections to 113
• Speculation about the origin of the number 113 and its significance
• Discussion of the number 113 and its cultural significance
• Explanation of why 113 is unlikely to be used as an error status code
• Recollection of a specific event on January 13th and the use of 113 in it
• Discussion of the reboot command and its potential to cause issues
• Explanation of the use of 113 as a way to exit cleanly and avoid issues
• Mention of a "wacky other button" for rebooting and the use of reboot -t with a timeout
• Discussion of how 113 was an "engineering secret" and not well-advertised
• Recollection of a past incident where the entire data center was rebooted due to human error and brittle command
• Lighthearted digression about a rusty scalpel and preschool sing-alongs
• Design flaws in the system led to a brittle failure mode that could be triggered by operator error
• Operators were supportive and cooperative during the outage, with one even admitting to having almost made the same mistake
• The team's disposition was to work together to fix the issue, rather than placing blame or questioning job security
• The operator received personal notes of appreciation from team members, and the team handled the outage in a way that was seen as exemplary
• The incident highlighted the importance of social perspective and teamwork in resolving complex technical issues
• The team was aware of implicit dependencies in the system that were not well understood, and this was a concern that needed to be addressed
• Concerns about a catastrophic system failure and the potential consequences of a complete shut down
• Similarities between the current situation and Google's past system failures
• Lack of knowledge about the system's behavior and the potential outcomes
• Comparison of the current system to other large and complex systems that have never experienced a complete cold start
• Discussion about drills and testing, but not actual failures of the system in question
• Recollection of events during the system failure, including:
	+ Systems being unable to boot
	+ Zone for TFTP being maxed out on CPU
	+ Initial attempts to boot systems from PIX and use of a RAM disk
	+ Splitting off into teams to address different parts of the failure
	+ Waiting for Manatee and Moray to come online in a one-node-only mode
	+ Chained replication and HA Postgres setup
• Attempts to piece together the sequence of events during the system failure
• Issues with system timing out
• Observations of system behavior during the "Sandy Bridge era"
• Discussion of the "booter" process, including its role as a TFTP server and its resource limitations
• Examination of the system's resource constraints, including low DRAM and CPU limitations
• Implications of the system's architecture on its performance and behavior under various load conditions
• Discussion of a system that was experiencing high latency and slow performance
• Mention of a discovery made by Robert that improved system performance
• Explanation of how giving the system "breathing room" by reducing load and rebooting nodes helped to resolve the issue
• Description of how putting a process into a real-time scheduling class and removing CPU caps helped to improve performance
• Discussion of the measures taken to address the high latency and slow performance, including powering off machines and implementing scheduling changes
• Technical issues with servers and infrastructure
• Impact on customers, including some being completely down and others experiencing partial outages
• Concerns about Steve, who is on paternity leave, not being informed about the issues
• Need to communicate with customers and let them know they are down
• Discussion about bringing up machines by hand if necessary
• Mention of Broadcom firmware issue affecting some systems
• BNX error and its impact on system uptime
• IPMI (Intelligent Platform Management Interface) and manual rebooting
• BIOS issues with timed out TFTP (Trivial File Transfer Protocol) connections
• Broadcom bug
• NetExtreme 2 (NIC) and its closed driver
• Driver genealogy and tracing roots
• 23andMe for driver ancestry
• Discussion about a driver issue in France
• Problem with interrupt enablement and disablement
• Source code availability and licensing
• Company deal to treat the driver as open source
• PCIe device interrupt control and MSI/MSIX
• Device specific interrupt generation and control
• Issues with IP address assignment in the link
• Discussion about technical issues with audio
• Mention of a difficult topic being discussed
• Reference to a personal event (a birth)
• Discussion of the 10th birthday of a person
• Mention of a CEO being fired
• Discussion of a shared experience (firing a person) between the speaker and someone else
• Reference to the speaker being in the hospital
• The speaker remembers receiving a call from someone named Steve who is from Missouri.
• Steve is the director of operations, and the speaker is surprised to hear that the East US system is down.
• The speaker has a strong reaction to the news, initially joking that they're throwing up on themselves.
• The speaker compares the feeling of hearing the news to the first time they heard about the birth of their daughter, Abby.
• Discussing the aftermath of a meteor hitting the hospital and its impact on the speakers
• Recalling a presentation by Mark, Briaco, and Steve on a Heroku outage that lasted 66 hours
• Discussing the effects of a multi-day outage on sleep management and team actions
• Sharing lessons learned from the Heroku outage and applying them to the current situation
• Discussion of a system failure and recovery
• Timeframe of the failure and recovery process
• Analysis of the root cause of the issue
• Comparison of the actual recovery time to a hypothetical faster recovery time
• Description of the "booter" system and its role in the recovery process
• Discussion of the "long pull intent" and its impact on the recovery process
• Dimensions of a website going down and coming back up
• Joint.com being down and its subsequent return
• Team members working on reboots and website recovery
• Successful transfer of the website to US West
• Christmas being the time of the website's recovery
• Emotional response of the team upon realizing the website was still up
• Memory of the moment and being physically together as a team
• Discussion about a past experience of huddling together in a small space
• Mention of a head node that was able to boot off of stable storage
• Reference to a system recovery and the importance of a quorum
• Explanation of how the system can get stuck if it can't contact peer instances
• Discussion about tricking manatee into one node mode to resolve the issue
• Question about how the quorum issue was resolved in the past
• Problems with a system that was full of files and had never been able to talk to a database
• The system was restarted and was unable to function due to not looking at its cache
• Discussion of booting up the system from cold and the process of getting all nodes online
• A quote from one person to another about punching things in the face to get the system to work
• Outage and communication during the incident
• Text updates received by one person during the outage
• Follow-up on a missed call from Brent during the outage
• Crisis communications during unexpected outages
• Importance of frequent updates to customers
• Need to be transparent and communicate even when information is limited
• Use of internal information to provide updates to customers
• Role of internal team in communicating with customers and external parties (AWS, Heroku)
• Example of sending text messages to customers with updates and estimated times for further information
• Lack of transparency from AWS
• 2011 incident and its impact on the company
• Transition to a more automated system
• Human error and its role in system failures
• Growth and limitations of the system
• System improvements
• Options parsing in STC
• Journaling and data collection
• Safety culture and on-boarding tool
• Vendor name and status pattern
• Establishment of a bulletin board for customer updates
• Transparency in operations and communication with customers
• Misleading status page showing "all green" despite underlying issues
• Use of visitor numbers to determine whether to investigate issues
• Comparison to Google's tracking of flu outbreaks through search data
• Importance of having a backup plan and considering potential outcomes
• Redundancy and having multiple locations for critical services
• Lesson from AWS outage where status page was in a single location
• Discussion of a past outage and its impact on system thinking
• Implementation of GSLB (Global Server Load Balancing) system
• DNS-based failover system with short TTLs and multiple locations
• Health checks to determine server availability
• Improvement of system performance and redundancy as a result of the outage
• Moving a website to a new location
• Incomplete or failed migration process
• Creation of instances and attempting to bring the website up
• Postmortem analysis and review of events
• Contribution of multiple individuals to the postmortem report
• Transparency and communication about the incident
• Apology and expression of understanding for the magnitude of the incident
• Review of the timeline and events surrounding the incident
• Importance of infrastructure and customer communication
• Frustration with lack of status updates during downtime
• Importance of frequent communication even with limited information
• Avoiding speculation and rumors through transparent updates
• Consequences of withholding information and allowing speculation to spread
• Resuscitating software due to lack of activity
• Difficulty with SSTN each node tool
• Changes made to operational procedures
• Discussion of re-architecture of SSTN each node tool
• Revelation of a previously hidden ticket
• Review of changes made in 2006 and 2008
• Discussion of SSTN each node tool's functionality
• Syntax and misinterpretation
• Importance of identifying and addressing multiple issues
• Learning from accidents and improving systems
• Legacy code and its challenges
• Historical context of code changes
• Discussion about a presentation on streams and its potential to be made public
• Reference to a video or link that is not publicly available
• Suggestion to make the presentation or link public
• Mention of an email from 2006, 2007, and 2008
• Discussion about the age of the presentation and its relevance
• Mention of a customer having issues with a system reboot
• Description of the customer's lack of concern for the system outage
• Mention of a TJ Fontaine dispatch from the Node JS Front, describing unruliness and escalating issues
• IOJS fracture
• Tensions leading to IOJS fracture
• Reflection on node and its history
• Hiring a new CEO in 2014
• Communication between the speaker and Charles
• Hiring Scott to replace the CEO
• The speaker's memory of the events
• Discussion about a previous CEO's decision
• Mention of a "big waste of time"
• Context about a person getting a lot of haircuts
• Allusion to a conversation or chat about the person's haircut
• Explanation of the person's haircuts being a "hit or miss" with a barber
• Discussion about inventing reasons to leave the office to eat with the CEO
• Acknowledgment of awkwardness and looking "sharp" during meetings
• New flag for running on all nodes
• Leaning on italics in lieu of looping across the table
• Command validation and list validation
• Safety point regarding command failure and potential destructive behavior
• RabbitMQ server with a topic that triggers execution on every computer
• Re-architecture of the client and changes to how it executes jobs
• Client specifying host names that don't exist and potential timeout issues
• Execution of jobs with misspelled host names still being executed
• The speaker describes a situation where they had to pick up the pieces during an operation and adjust their approach.
• A discovery phase was created for the command to ensure that the nodes are alive before proceeding.
• The discovery phase includes checking for a broadcast from all nodes and verifying that the nodes match the specified list.
• The command is a stringly typed interface with a limited subset of valid host names, which can lead to safety issues.
• The command's looseness is beneficial in certain circumstances, such as when the control plan is down, as it allows for some actions to be taken.
• The command does not consult the database, but instead broadcasts and checks the responses from nodes.
• The disk is full
• Discussion of the incident and its impact on current projects and tools
• Use of Pilot as an engineering tool and its limitations
• Pixie booting and its benefits
• Stateful vs stateless services and their trade-offs
• Use of RAM disks and its implications
• Analogies and metaphors used to describe technical concepts and their implications
• Discussion of pixie and its challenges
• Inventing a pixie thing would have been required
• Other incidents informed the perspective
• Big challenges in the Triton and SDC era
• L2 broadcast domain and pixie configuration issues
• Switches and LACP (Link Aggregation Control Protocol) problems
• Securing pixie is difficult
• Using YubiKeys and certs in the UEFI chain store
• iPixie and its complexities
• Complete implementation of secure systems is unclear
• Difficulty testing and verifying code
• RAM disk usage and local download of images
• Cold boot capabilities of the rack
• Importance of the rack and cold booting
• Consequences of the outage and lessons learned
• Presence and use of the recovery path in the oxide rack
• Importance of exercising the recovery path and not relying on it solely for updates
• Difficulty in exercising the specific failure mode of turning off 600 machines and pixie booting them all at once
• Decision not to build a TFTP load generator to simplify the process
• Importance of regularly exercising the recovery path
• Different ways of simulating various aspects of a system
• No single way to simulate the entire system
• Importance of simulating different failure modes
• Challenges in creating a realistic simulation environment
• TFTP and back pressure issues
• Limitations of older protocols like TFTP and TCP
• Importance of congestion control in TCP
• The speaker discusses the rarity of a particular setup or deployment in 2014.
• They mention the use of hundreds of computers on a single network, which was uncommon.
• The speaker describes the deployment of the Pixie system and its automation capabilities.
• They discuss the reliability of the system and its ability to stay up for long periods without rebooting.
• The speaker mentions the limitations of rebooting systems, including the Samsung cloud, and the use of HTTP booting.
• They discuss a flag or setting that needed to be explicitly enabled for HTTP booting to work.
• Presence of HTTP booting is a direct consequence of avoiding existing firmware and protocols
• Using Nginx to serve images over HTTP
• TCP is used to transport images to computers because it coexists with other connections
• Lessons learned from Oxide computer relate to not using external firmware
• Challenges of dealing with Pixie ROM and firmware issues led to developing own solutions
• Sidestepping existing problems and developing new solutions is a consequence of this experience
• Broadcom issues discussed and their impact
• The Four Nicks of the Apocalypse and Nick selection
• Pastelance and Intel's involvement
• Famine and its effects on the body
• Concerns about confidentiality and public disclosure
• The influence of Broadcom issues on personal opinions and decisions
• Discussing a system and its reliability
• Creating API operations for operators and customers
• The importance of safety in system development
• Criticizing the type system for being too vague
• Enums being treated as strings rather than separate types
• The difficulty of ensuring exhaustiveness in certain checks
• The use of Rust and clap in system development
• Building a custom option parser
• Comparison of building in Rust vs. other languages
• Decision to build the future in Rust
• Design of the Oxide control plane
• Critique of the Triton control plane
• Importance of in-band signaling
• Discussion of string value handling in code
• Consequences of string value jamming in code
• Incident described as a near miss in every dimension
• No customer data was lost during the outage
• The company's transparency during the outage was praised by customers
• The company's approach to customer communication and collaboration during the outage was seen as refreshing and led to increased customer confidence
• The company's recovery from the outage was rapid, with some customers expressing amazement at the speed and efficiency of the recovery
• The comparison was made to a similar outage at a large cloud provider (AWS), where a recovery of this speed would not have been possible.
• The speaker and others have learned from past experiences, especially a major incident that could have been much worse.
• Being transparent about what one knows and doesn't know is important.
• It's hard for companies to be transparent, especially when they don't want to seem incompetent.
• The speaker believes that the company's culture and actions during the incident were refreshing and revealing.
• A team member was impressed by the company's response to the incident, feeling grateful for the teamwork and support.
• The company will return to normal operations when the data center is back up.
• Celebration of an anniversary or milestone (10th anniversary)
• Mention of individuals (Abby, Brian, Robert, Josh, Steve) and their contributions
• Sharing of tickets or documents (Jira tickets)
• Gratitude and appreciation for the group's efforts and contributions