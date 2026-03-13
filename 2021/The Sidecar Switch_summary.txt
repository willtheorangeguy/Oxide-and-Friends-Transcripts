• Twitter's limitations and multi-tasking challenges
• Abe Simpson references and cultural knowledge passing down to younger generations
• Aboard design process and signal layer visualization
• Use of Allegro PCB Designer and Cadence software for board design and rendering
• Aesthetic appeal and invitation to explore complex systems
• Generational knowledge and cultural references becoming lost over time
• The speaker discusses the intricacies of printed circuit boards (PCBs) and their importance in technology.
• The speaker interviews Arne, one of the earliest employees of Oxide, about the company's early days and vision.
• Oxide's early days involved focusing on root of trust and code integrity, with Arne initially suggesting using an off-the-shelf switch.
• Arne and the speaker discuss the challenges of building a custom switch and the integration of components in the rack.
• The speaker reflects on how Oxide's approach to building a custom switch was influenced by conversations with other companies and individuals.
• Arne reveals that Keith suggested making the switch an external PCI Express device, which led to the development of a custom chassis.
• The conversation touches on the confidence gained by Oxide after learning that Google had successfully built a similar system in the past.
• The team discussed using reference designs from vendors, but found that modifying existing designs was too complicated and they would have been "on their own" creating a semi-custom solution.
• Intel's Tofino ASIC was introduced as a viable option, which is a programmable and flexible device that can be tailored to the user's application.
• The Tofino ASIC uses the P4 language, which is an open language for describing switching and data flow applications.
• Broadcom's similar ASIC is also programmable, but uses its own language and environment.
• The team ultimately chose Intel's Tofino ASIC over Broadcom's due to its better fit with their needs and vision.
• The discussion touches on the concept of "getting weird" and finding partners who are willing to do so, which aligns with Oxide's vision for a software-controlled data center.
• Broadcom and novel features of the chip
• Using the chip as a load balancer, tunnel endpoint, and DNS server
• Hardware-accelerated firewalls, load balancers, and other features
• P4 programming language and its use in developing applications
• Tofino 2 chip design and its power requirements
• Ability to mix and match applications on the switch
• Limited flexibility in slicing the switch up to run multiple programs simultaneously
• Need to decide upfront what program to deploy on the switch
• The product has a lot of potential and can go in different directions
• It's a real pain point for those deploying on-prem infrastructure, particularly due to lack of visibility into switch performance and reliability issues
• The product is overpowered, with 32 ports, which can lead to interesting oversubscription ratios and dense fabric capabilities
• Programmable aspects enable tagging of extra data onto packets for telemetry and tracing, allowing for better network troubleshooting and performance analysis
• The design involves a blindmated cabled backplane and a unique ASIC placement to minimize losses in cables and connectors
• Flyover cables are used to connect to optical modules, and the design has focused on reducing loss and making transitions as low as possible
• The product is called "sidecar" due to its external connection to a compute node, with the term also having a secondary meaning as a reference to a cocktail.
• Plans for future systems with "drink inspired" design
• Discussion of the "sidecar" story and experience with proper cocktails
• Complexity of management network and service processors
• NCSI (network control and status interface) as a solution for out-of-band management
• Concerns about firmware control and potential for exploits
• Decision to add a separate switch for out-of-band management
• Complexity and potential drawbacks of NCSI and other solutions
• Discussion about the complexity of the NIC design and the potential for issues with NCSI
• Flipped ownership model where the host owns the device, which can lead to problems
• Concerns about implementation and vendor support for NCSI
• Comparison to other devices, such as routers, and how they handle management networks
• Explanation of the design of a large switch with separate switches and management networks
• Discussion of custom firmware and SDN customization on management nodes
• Tension between implementing SDN at different levels and concerns about latency and interrupt latency
• Explanation of how software will be run on compute nodes, including potential for low interrupt latency
• NCI's machine acts as a big resistor due to HPC, turning current and voltage into thermal energy and an IO bandwidth problem
• Discussion of using AMD CPUs with multiple cores to dedicate resources to a specific task
• Intel's approach to network function virtualization, prioritizing complexity management over splitting tasks between kernel and VM
• Flexibility in running code directly on the main OS or in a VM
• Simulator and software development with Intel's SDE and RTL model
• Simulation capabilities, including packet tracing and logging, and processing speeds of a couple thousand packets per second
• Development of infrastructure with the simulation model and VMs
• Discussion of the development vehicle and traditional switch form factor
• Importance of hardware-software co-design and unhooking software engineering from hardware engineering
• Intel's recognition of hardware-software co-design and exposure of the RTL model to customers
• Discussion of the trust model and secure boot process for the switch
• The management network is running the intended configuration and is able to initiate power and reset for the Tofino ASIC.
• The system has built-in redundancy, including two switches in the rack, which can take over in case of failure.
• The system can continue to run even if the host CPU fails, but will not be able to establish new sessions or program tables.
• The out-of-band management network is used to detect and respond to failures, and to direct traffic around the failed node.
• The team plans to implement continuous integration and testing to ensure that p4 programs are not shipped with errors.
• The simulator will be a key tool for testing and validating the system, and will be used to simulate multiple scenarios, including multi-rack and multi-AZ environments.
• The system is open-sourced, with the operating system, Hubris, to be released as open source.
• Discussion of the aesthetic beauty of a newly developed artifact
• Engineering details and complexities of the artifact, including clock generation and signal propagation
• Challenges in designing and assembling the artifact, including thermal management and mechanical stress
• Use of non-functional units and testing for physical properties to understand limits of the artifact
• Concerns about shipping and handling the artifact due to its size and weight
• Discussion of the project's current stage and the challenges ahead