• The speakers discuss the challenges of working remotely and interacting with colleagues through video conferencing.
• They mention the difficulties of recognizing and interacting with colleagues in person after working with them remotely for a while.
• The speakers discuss a specific video conferencing habit, where they give an overly emphatic thumbs up next to their cheekbone, and how it's harder to stop doing this habit even when in person.
• They also discuss the tendency to have sidebar conversations during meetings, which can become an important part of the discussion.
• The conversation shifts to a technical topic, where the speakers discuss debugging a problem related to TCP No delay being set on a connection.
• They explain that the problem resulted in delayed acts and Nagel's algorithm, and they will dive deeper into the details.
• The speakers discuss the importance of visualizing every single IO path when dealing with IO pathologies, rather than aggregating them into buckets.
• Latency art visualization
• Debugging production issues
• Drive firmware issues
• Visualization of IO performance
• Use of BPF trace for data analysis
• Discussion of data visualization and its importance
• Discussion of EPF and BCC (Berkeley Packet Filter and BCC)
• Comparison of Trace, EPF, and BCC with different design centres and goals
• Origins and design of Trace and its influence on other systems
• Dynamic instrumentation and data loss in EPF and BCC
• Importance of data integrity and notification in dynamic tracing
• Discussion of data drops and lack of notification in BPF trace
• Problems with instrumenting the system correctly
• IO operations not being traced due to incorrect instrumentation
• Comparison with Illumes, Helios, and Polaris IO tracing
• Issues with BPF (Berkeley Packet Filter) tracing and instrumentation
• Problems with coherence and consistency of instrumentation
• Potential for probes to fire out of order or not at all
• Difficulties in debugging and understanding the system's behaviour
• Discussing the use of Rust for post-processing data and its advantages over traditional tools like shell and AWK
• Identifying and investigating outliers in data, specifically banding at 100 milliseconds, and how it affects performance
• Reproducing the issue on an oxide rack and using USDT probes to instrument the system and gather data
• Correlating activity on the client and server sides using job identifiers and wall timestamps
• Troubleshooting the issue and determining that the outliers are not due to network latency, but rather a client-side issue
• Discussion of TCP and IP probes and their role in diagnosing network issues
• Explanation of Nagel's algorithm and its purpose of reducing congestion in networks
• Mention of the "great Internet collapse of 1986" and its relation to network congestion
• Explanation of Van Jacobsen's work in 1988 and its importance in saving the Internet
• Discussion of the design of early networks and the need for algorithms like Nagel's to prevent network collapse
• Explanation of the concept of "getting Nailed" and its relation to network latency and congestion
• Humorous anecdotes and asides about the conversation
• Delayed ACK behaviour and its implications for network performance
• TCP design point and its limitations in handling request-response protocols
• Evolution of networking speeds and hardware capabilities (e.g. CPU speeds, RAM sizes, network speeds)
• Optimization techniques for reducing packet transmission and loss (e.g. bundling packets, avoiding unnecessary packet transmission)
• Historical context for TCP constants (e.g. minimum timeout, retransmit time) and their enduring presence despite advancements in technology
• Critique of TCP attributes as being overly rigid and not adaptable to modern network contexts (e.g. data centres)
• Discussion of optimizing network settings and timeout values
• Reference to an RFC for network optimization
• Debugging of a network-related issue with angle's algorithm
• Story of a Google Ads technology summit and a presentation on an event system
• Description of a specific issue with the event system's buffering and Eagle's algorithm
• Discussion of buffering and Eagle's algorithm in various systems and environments
• Story of a lucky discovery and debugging of the issue through inspection
• Comparison of debugging approaches and the challenges of debugging complex systems
• TCP Eagle's algorithm and its impact on network latency
• Difficulty in detecting issues related to TCP Eagle's algorithm
• Twitter and Mastodon posts about TCP no delay
• Researcher's personal experience with TCP Eagle's algorithm in 2012
• Historical perspective on congestion control research and TCP Eagle's algorithm
• Cooperative congestion control and the lack of intentional prevention of congestion
• Default settings and the potential for problems when changing them
• Discussion of whether TCP Eagle's algorithm should remain as a default setting
• Discussion of Eagle's algorithm and its default behaviour in various programming languages and libraries
• Importance of defaults in library settings and their impact on user experience
• Parking brake tweet and its origin from a GitHub issue related to Tokyo
• Comparison of Rust's standard library and Tokyo's default settings
• Potential to change default settings to match industry-wide norms
• Shared experiences of various reactor libraries and their handling of Eagle's algorithm
• Example of a demo app (Mini Regis) and its intentionally limited features to demonstrate educational concepts
• Discussion about a benchmark being misleading due to local machine pipelining
• Importance of checking Eagle's algorithm in debugging network performance issues
• Review of Linux socket options and lack of Eagle's in the list
• Need for improved debugging and visibility into TCP stream delays
• Proposal to change TCP stream debugging format to include delay information
• Discussion of TCP back off and close wait timeouts being overly long
• Impact of these timeouts on system performance and user experience
• Debugging connection issues and the idea of having a "scream for help" mechanism
• Proposal to add a kernel statistic to track dropped packets
• Discussion of naming the statistic, with suggestions including "Eagle resend drop" and "JK dropped"
• Importance of visualizing network latency and outliers in packet data
• Proposal to assign unique time-out values to systems to help identify issues
• Discussion of the limitations and potential solutions for visualizing complex system data
• Humorous exchange about running out of time-out values and buying them from others
• Final discussion on the challenges of visualizing complex system data and the need for a more intuitive interface
• Discussion of debugging latency and visualizing latency distribution
• Critique of using averages to describe latency, and the importance of visualizing the entire distribution
• Introduction to the tool Honeycomb and its ability to analyze and surface unusual metrics in a dataset
• Mention of Angela Collier's videos on data visualization and her criticism of violin plots
• Discussion of JVM garbage collection algorithms and the complexity of tuning them
• Joking reference to needing a "theatre recession" for JVM flags, and a suggestion that they need a content warning
• Discussion of the "magic" of JVM flags and the internal politics of Sun Microsystems
• Mention of a "civil war" within Sun Microsystems between Labs and Unsoft
• Discussion of shibboleths in software development and the importance of understanding their origins
• Discussion of troubleshooting techniques, including checking for TCB No delay and Eagle's algorithm
• Suggestions for making TCP no delay more visible and easier to debug, including a Wireshark warning filter