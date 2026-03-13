• Discussion of a previous episode of "On the Metal" where they shared their favorite moments
• Mention of a specific episode featuring a clarinet solo and a measurement tweet
• Discussion of the development of Oxide's switch, including the challenges and uncertainties in the early days
• Mention of a upcoming blog post on the development of Oxide's switch
• Personal stories of how individuals, including Ryan Goodall, became involved with Oxide
• Discussion of the benefits of having a big, ambitious vision and how it attracts like-minded people to the company
• ASICs are complicated and historically proprietary, making it difficult to understand what's happening at a low level
• Declarative APIs and Linux-based switching environments don't provide a clear mental model of packet processing
• p4 is a data plane programming language that allows for fine-grained control over packet processing
• p4 programs can run at line rate, making it possible to parse and process packets at extremely high speeds
• Programmable switches, such as the Tofino 2 from Intel, support speeds of up to 12 terabits per second
• p4 can be used for various tasks, including packet modification, header injection, and telemetry data insertion
• The p4 language is powerful but has limits, and fixed-functionality is minimized.
• Programmable ASICs can adapt to changing workloads and protocol needs
• Fixed function ASICs have limited flexibility and resource allocation
• Tofino ASIC allows for dynamic resource allocation and reconfiguration
• The Tofino simulator is used for development and testing, but has limitations
• Building a software stack for Tofino requires a system-level approach
• The team is working on developing drivers, operating systems, and APIs for Tofino
• They are also working on implementing network end-to-end at a system level
• Discussion of using a cycle accurate ASIC simulator for testing
• Impediments to development due to simulator's suboptimal performance
• Challenges of developing software without the hardware in hand
• Decision to write a custom p4 compiler to bypass simulator limitations
• Overview of the p4 ecosystem and the potential for compiling p4 to Rust
• Discussion of the need for high-fidelity execution of P4 code in multiple environments
• Comparison of using the behavioral model version 2 (BDM 2) versus compiling P4 code directly
• Decision to implement a virtual ASIC inside a hypervisor to achieve high-fidelity execution
• Use of Oxide's beehive and propolis components to create a virtual ASIC substrate
• Achievement of gigabit speeds per port through the use of a dynamic library and IO paths
• Ability to test multipath routing algorithms at high speeds
• Description of the work involved in integrating and automating the P4 pipeline and control plane interactions
• Overview of the Oxide team's efforts to make the technology more accessible and user-friendly
• Gluing disparate vendor infrastructure together is a complex and painful process
• Issues with integration and communication between switches and servers
• OPTE (distributed virtual switch) lives in the kernel and leverages NICs to handle traffic
• Gimlets (servers) can interact with Tofino-based switches through a PCIe peripheral
• Integration between switches and servers at the software and control plane levels
• Challenges in getting different components to interoperate, even between large hyperscalers
• Large hyperscalers have invested significant work in managing their network configurations and tables
• Examples of complex routing and PubSub systems used by companies like Facebook/Meta to manage their networks
• Handing off control to a partner would lead to unreliable and untestable problems
• Meta's experience building a purpose-built switch can inform the design
• The focus is on high-performance IP packet transmission, rather than enterprise features
• The network's functionality is distributed across hosts, rather than being centralized in a switch
• The team has developed simulation tools and debug ability to manage the complex system
• The ability to instrument and verify the system's operation is a key benefit of building from scratch
• Building a foundation of decision-making logic and orchestration in the Nexus part of the system
• Using sagas to run dependent steps and unwind the sequence if anything fails
• Implementing a p4 compiler and integrating it with DTrace for debugging and visibility
• Embedding USDT probes in Rust using the USDT crate
• Reviewing the history of the company's early projects, including the first USDT crate and its potential for future development
• Discussing the benefits of building the system from the ground up and having control over the code and its integration with other tools
• Debugging networking protocols
• Importance of using Rust and its ecosystem for building tools
• Use of code generation tools, such as quote crates and Build RS
• Hygienic macros and their limitations
• Integration of p4 code with Rust using Progenitor tool
• Use cases for p4 and programmable networking, including observability and programmability in networking tools
• Integrated switch use cases for end-to-end control of the stack
• BGP implementations for interacting with upstream networks and CDNs
• Tunneling protocols (FireGuard, Geneva, VXLAN) for remote site connections
• Delay-driven multipath (DDM) routing protocol for scalable routing
• Oxide network architecture (underlay and overlay networks) with ipv6 underlay and GENEVE overlays
• Multipath physical network with fault tolerance and flexible topology construction
• Routing protocol requirements for scalability, load balancing, and fault tolerance
• Comparison of routing protocols (RIFT, ECMP) and drawbacks of current implementations
• Measurement and analysis of network traffic matrices for routing protocol optimization
• Combining microload balancing and congestion control approaches from 2017 and 2020 papers
• Using programmable data planes to add telemetry information to packets and make routing decisions in real-time
• Measuring delay and load balancing based on destination to avoid microcongestion and optimize network performance
• Importance of integration and programmability in switches and data paths for achieving desired results
• Observing micro congestion through techniques such as queue depth monitoring and packet-level latency measurements
• Minimizing TCP retransmits and reducing microcongestion to improve network performance and reduce latency
• Concerns about SmartNICs as a solution, considering the complexity of network stacks and the need for a more programmable approach
• Potential for SmartNICs to provide value in specific scenarios, such as line rate encryption on a per-flow basis
• Limitations of current SmartNICs, including speed and programmability
• Challenges in implementing DDM, including p4 programming and integrating with the operating system network stack
• Complexity of making choices about how to implement DDM, including offloading and acknowledgment messages
• Need for a clear understanding of the system's behavior and the ability to revisit and adjust decisions as needed
• Difficulty in finding the right layer of abstraction for DDM implementation
• Importance of expressing the Oxide rack in a customer's deployment, including integrating with their network and management systems
• Challenges with BMCs (Baseboard Management Controllers)
• Oxide rack deployment process and network setup
• Programmability and API integration for easier setup
• Vendor-agnostic approach to networking
• Customer feedback and acceptance of Oxide's innovative approach
• Team effort and collaboration to bring Oxide's vision to life