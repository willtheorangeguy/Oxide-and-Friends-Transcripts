• Demo Friday at Oxide is a weekly event where team members demo their work to peers
• Andrew presented a demo of a CLI-based software for configuring a rack of servers
• The software is used to configure the network and control plane of the rack
• The presenter, Andrew, initially thought someone else would build the software, but ended up creating it himself
• The software is a terminal UI that uses a technician port to connect to the rack
• The team chose a CLI over a web UI to keep it simple and accessible in various environments
• Andrew discovered a "universe of Chewy's" (text-based user interfaces) and had fun building the software
• Captive shell, Wicket, built on top of 2ERS, cross term, and Rust, presents a graphical interface inside the terminal
• Manufacturing station has a similar interface, built by Josh Clulo
• Wicket allows configuration of the system and talks to a downstream service called WICD
• Demo of Wicket showed a recording of a live session being replayed
• Debugger written by Andrew allows replaying of a recording, but does not allow going backwards
• Internal workings of Wicket and its limitations, such as expensive state capture, were discussed
• Possibility of building a normal captive CLI, similar to Readline, was mentioned
• The technique of replay debugging is discussed, allowing for the recording and replaying of system events.
• The importance of separating IO from state and mutable state is emphasized, enabling the recording and replaying of system events.
• The WICkit system is built using an event loop and global state, with messages being totally ordered and serialized for replay.
• The system's design allows for the debugging of UI interactions, including user input and downstream events.
• Time-related events, such as animations, are also considered and handled through a channel that normalizes all events into a total order.
• The design decisions are influenced by the speaker's background in building distributed systems and consensus protocols.
• The Elm architecture is mentioned as being similar to the system's design, but the speaker claims to have learned about it after making the design decisions.
• Replicas in the system are single-threaded and can be run in total order
• The system is not a real test, but a simulation, and leaves out network and non-determinism
• The speaker built a debugger for a previous project at VMware, but it was canceled
• The speaker was one of the early users of Rust, and experienced its "raw" state in 2015
• The speaker built the debugger as a weekend project to simulate events in the UI and test animations and styling
• The debugger allows single-stepping, playing at different speeds, and recording simulations
• The ability to record and replay user interactions for debugging and testing purposes
• Using event streams (ERS) to automate testing and validate code changes
• The ability to resize the screen and handle different window sizes in recordings
• Implementing a system to store and dump event streams in production environments
• Using a state machine to constrain the history of events and manage memory usage
• The ability to take snapshots of the application state and dump event streams for postmortem debugging purposes
• Automating debugging and testing processes with ERS to improve efficiency and reduce time spent on debugging
• Discussion of Serde, a serialization and deserialization library in Rust
• Benefits of using Serde, including its ability to generate serialization and deserialization code automatically
• Explanation of procedural macros and how Serde uses them to generate code
• Overview of the SERDES visitor pattern and pluggable serialization formats
• Use case of Serde in a Wixit project, where it was used to serialize and deserialize events
• Discussion of Rust's broad use case and the benefits of its pattern and approach
• Comparison of Rust to other languages and serialization technologies, including Tcl, Python, C++, and Perl
• The ease of use and power of Rust compared to JavaScript
• Applying distributed systems patterns to a new domain without the complexity of distributed systems
• The value of combining knowledge and experience from one domain to solve problems in another
• The benefits of experimenting and learning new skills, even if it's outside one's comfort zone
• The importance of application-specific debugging infrastructure for developing powerful and efficient debugging tools
• The tension between general-purpose and special-purpose debugging infrastructure and the benefits of special-purpose tools like Sandra
• The idea that one should take advantage of opportunities to apply new techniques and learn new skills, as demonstrated by the development of Sandra
• Property-based testing allows exercising large portions of a system with a large input space
• It involves writing a "property" that defines a specific behavior, such as "reversing a list twice results in the original list"
• The testing infrastructure generates a range of inputs that are then passed to the system being tested, automatically checking that the property holds
• Property-based testing can be used to test complex systems, but requires deterministic code to ensure consistent results
• There are two main types of property-based testing: stateless and stateful, with the latter involving maintaining a model of the system's state and comparing it to the actual state
• Property-based testing tools can provide a history of the inputs and assertions that led to a test failure, and can use "shrinking" to reduce the state space and identify the minimal sequence of events that caused the failure
• The PropTest crate and QuickCheck from Haskell are examples of property-based testing tools.
• PropTest and QuickCheck compared and contrasted
• PropTest's advantages over QuickCheck, including its ability to derive and compose types and generate new outputs
• PropTest's features and tools, including an introductory book and a focus on coherence
• Recommendation to use PropTest for testing and debugging
• Discussion of the influence of Haskell on Rust and other programming languages
• Personal anecdotes about the Automated and Algorithmic Debugging conference
• Story about the conference being discontinued due to logistical issues
• Mention of a humorous incident involving Adam's reaction to California's horse meat ban
• Traveling to Belgium in 2003 and attempting to find horse meat
• Misunderstanding the slang for horse meat (heroin) and confusion at a conference
• Visiting a butcher shop with a giant horse's rear end outside, but no horse meat available
• Searching for unpasteurized raw milk cheese as an alternative
• Implementing an open-source debugger and discussing its features and limitations
• Comparing the actor model, event-driven state machines, and CQRS (Command Query Replay) models
• Andrew's software provides a great terminal experience on the headset.
• The speaker appreciates Andrew's work and notes that Oxide's resources were poured into the project.
• Next week's topic will be the cable backplane, with guests including a mechanical engineer and an engineer from Semtech.
• The discussion will cover a mishap with the cable backplane and how it was debugged.