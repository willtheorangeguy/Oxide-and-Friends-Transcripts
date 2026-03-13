• Memorial Day weekend plans and discussions about baseball
• Bryan's experience watching baseball on the road with a streaming provider
• Full-throated endorsement of a team, but also criticism of the Oakland A's
• Introduction of Josh Allow and Robert, and mention of a potential surprise guest
• 10th anniversary of a past event, specifically a massive outage and rebooting of data centres
• Discussion of US East 1 and US West data centres and their importance
• Recounting of a stressful moment when Bryan's infrastructure was affected during the outage
• Discussion of a major outage incident at a company, where all US East servers were rebooted
• Bryan Can trill recounts how the team was able to quickly recover, despite some initial confusion and catatonia
• Explanation of the company's architecture and how the reboot command caused a cascade failure
• Discussion of the importance of having a backup plan and redundancy in critical systems
• Recollection of the incident and its aftermath by various team members
• UUIDs and Unix commands
• Option parser issues and bespoke parser
• Timeouts and ignoring failures
• SCCS and spin locks
• Exit code 113 and agent issues
• RabbitMQ and ZFS
• Executing commands through API
• Brutality of command execution protocol
• The origin of exit code 113 is discussed, with Bryan Can trill mentioning that it's a controlled exit, and they need to find out why it's 113.
• Josh Allow suggests that the month is January, and Bryan mentions a specific date, January 13th, 2011, but later says it was a joke.
• The exit code 113 is revealed to be the 30th prime number and an Einstein prime, and Bryan is curious about its significance.
• Bryan mentions that the git blame for the code is 11 years old, and Brian Bennett points out that there are limited options for choosing a code, and it's unlikely to be 0.
• The group discusses the cultural significance of numbers and how 113 may have been chosen for its prime value or cultural references.
• Bryan mentions that the code is unlikely to be used spuriously and suggests that it was chosen because it's a large prime and unlikely to be used by software.
• The group discusses the origin of the code and how it was likely written on January 13th, 2011, and used as a temporary fix.
• Discussion of a command "113" and its use in rebooting a system without sending a response, leading to an outage
• Acknowledgment that the outage was caused by a combination of robust infrastructure and human error
• Analysis of the command's brittleness and how it was not well-documented or advertised
• Reflection on how the team handled the outage from a social perspective, including offering support to the operator and setting a collaborative tone
• Discussion of the implicit dependencies of the system and the challenges of evolving a complex system over time
• Discussion of whether large complex systems have ever been completely shut down and restarted
• Incident where the system was unable to boot and a process (TFTP server) was stuck, leading to high latency and node timeouts
• Analysis of the system's configuration, including CPU and DRAM limitations, and how it affected the system's behaviour
• Use of real-time scheduling to prioritize the stuck process and improve system performance
• Comparison of the incident to a "final exam" experience where the team had to quickly adapt to a new situation
• Issues with system booting due to CPU caps being removed
• US East servers being down, affecting all customers
• Broadcom firmware issue causing problems
• TFTP timeout issue with BIOS not handling it well
• Manual rebooting of systems due to Broadcom bug
• History of Broadcom driver and its development
• PCIe devices and interrupt enablement issues
• Extreme 2 driver problems causing boot issues
• Personal anecdotes and humour about dealing with the issues
• Discussion about notable events in the joint history of the company rather than individual birthdays
• Story about a CEO being fired and the reaction of a new team member
• Recollection of a specific day when the system went down and the team's initial reaction
• Reference to a Heroku outage and the importance of planning for extended downtime
• Discussion of the length of the outage and the challenges of managing sleep and staffing during the incident
• The head node rebooted on its own, causing initial issues
• Manatee was put into one-on-right mode, making things "serviceable"
• Booster was "unleashed", allowing everything else to come up
• The team "got lucky" in many dimensions, avoiding a much worse outcome
• The team worked to fail over the website to US West, eventually succeeding
• The team celebrated their success and relief that they could recover from the outage
• The team discussed how they were able to recover, including using the booster cache and tricking Manatee into one-on-right mode
• The team discussed the challenges of recovering from the outage, including issues with the BNX driver and DHCP
• Discussion of a past outage and the importance of transparency in communicating with customers
• Reference to a Mark talk about crisis communications and the challenges of communicating with customers during outages
• Discussion of the difficulties of communicating with AWS during the outage and the importance of transparency in their communications
• Reflection on the lessons learned from the outage and the improvements made to the system
• Discussion of the importance of having a well-established and easily accessible platform for communicating with customers during outages (e.g. giantstatus.com)
• Discussion of the need for transparency and communication in times of crisis, and the importance of not hiding behind a "green" status page.
• Discussion of a status page being used to determine if an issue should be investigated
• Comparison to Google's flu tracking by searching for symptoms, and how it could be used to gauge interest in a company's status
• Recounting of an AWS outage and how it affected the company's thinking on redundancy and failover systems
• Description of a DNS-based failover system implemented as a result of the outage
• Reflection on the importance of transparency and communication in the event of an outage, including apologizing and updating customers regularly
• Discussion of the impact of an outage on a company's customers and the importance of staying in communication during downtime
• The consequences of false rumours and how they can affect people and organizations
• The importance of quickly resolving issues and the potential for reputation damage if not addressed
• The rearchitecture of the SSC on each node tool and the ticket that documented it, which was previously private
• The specific changes made to the system, including:
	+ The default behaviour of SSC on each node
	+ The require command argument
	+ The validation of the node list before execution
• The discussion of how these changes could have prevented the issue that occurred
• The importance of learning from the experience and improving the system as a result
• The sharing of old code and documentation, including a relic from 2011
• The discussion of making public certain tickets and documentation, including the 2006, 2007, and 2008 tickets
• Reflection on the history of Node and a related company
• Hiring and dismissing CEOs
• Bryan Can trill's haircut and awkward meetings with Scott
• Discussion of a Node command that was rewritten to be safer
• Redesign of the command to include a discovery phase and a separate list of nodes
• Improvements to node selection and validation to prevent destructive behaviour
• Discussion of the value of having a control plane that can still function even if the main control plane is down
• Description of the SDC (System Deployment Configuration) tool and its ability to broadcast and check for matches
• Description of a past incident where a compute node was hung, but SDC was still able to function
• Discussion of how the past incident has informed the design of new systems, including Pilot and the oxide rack
• Comparison of pixie booting vs. using a recovery path for updating the system
• Discussion of the challenges of implementing a recovery path and the importance of exercising it regularly
• Importance of having multiple ways of simulating different aspects of the system for testing and failure mode analysis
• Simulation of production environment to test aspects of system
• Failure of TFTP mechanism due to lack of back pressure
• Importance of congestion control in TCP
• Challenges with pixie booting, including reliability and automation
• Introduction of HTTP booting and its benefits
• Lesson learned from Broadcom issue and its impact on system design
• Importance of controlling one's own fate and destiny in system design
• Considerations for creating safe and reliable API operations
• Discussion about the limitations of JavaScript and its impact on software rigour
• Critique of the "Washington washiness" of Rust's type system
• Comparison of Rust and other languages, including the ease of creating correct software in Rust
• Inland signalling and its issues
• Near-miss incident and the company's response, including transparency and customer confidence
• Reflection on the incident and its impact on the company's culture and approach to outages
• Discussion of debugging processes and team collaboration
• Celebrating a 10-year milestone and thanking attendees
• Sharing of past Jira tickets for public reference
• Thanks and closing remarks