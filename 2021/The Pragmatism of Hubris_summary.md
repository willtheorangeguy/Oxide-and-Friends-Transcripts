• Cliff's participation in Twitter Spaces is hindered by technical difficulties
• Cliff is using a custom keyboard with a microphone, but is experiencing issues with audio
• The group is discussing the limitations of Twitter Spaces, including the lack of ability to download recordings and the issue with audio cutting out after 3 days
• Cliff's representative, Steve, is attempting to communicate on his behalf
• The group is joking about the technical difficulties and Cliff's status as a "Twitter conscientious objector"
• Discussion of Cliff's presentation on Hubris
• Cliff's experience working on Project Loon at Google
• Loon project overview and its high altitude balloon system
• Similarities and differences between Loon and space-faring systems
• Challenges in system software for Loon firmware
• Development of the Major Tom framework for Loon
• Frustrations with the Major Tom framework and its limitations
• Cliff's vision for Hubris and its goals
• Cliff's experience and approach to building Hubris at Oxide
• Discussion of the challenges of building a reliable operating system for a specific use case
• Comparison of different approaches, including using an existing OS (Talk) and building a custom OS (Hubris)
• Reflection on the decision-making process and the evaluation of different options
• Importance of code quality, debugging experience, and reliability in operating system design
• Challenges of using existing OS solutions and the limitations of available options
• Discussion of the trade-offs and considerations involved in building a custom OS
• Acknowledgement of the importance of aligning with the values and goals of the project and its stakeholders
• Node and Joyant's divorce and its impact on the speaker's values and goals
• The importance of humility in software development and the need for a language that prioritizes it
• The development of humility, a language that aims to make programming easier and more accessible
• The challenges of working with OpenTitan and the need for a secure and reliable root of trust
• The limitations of current secure FPGAs and the reliance on security through obscurity
• The exploration of alternative solutions, such as reconfigurable computing, for achieving a secure and reliable root of trust
• The group discusses their experiences with writing an operating system, specifically using the STM32 F4 microcontroller on the F407 discovery board.
• They mention the challenges of working with soft logic and RTL (Register-Transfer Level) components, and the potential risks of using proprietary tools and ecosystems.
• The group recalls attempting to use FPGAs (Field-Programmable Gate Arrays) but facing issues with open-source tooling and vendor support.
• Cliff is mentioned as having worked on the project for a couple of weeks, and the group discusses the process of defining what an operating system is and how to approach its development.
• They mention the importance of debugging tooling, build systems, and bug tracking in a complex project.
• The group also discusses the "2,200 lines of code" milestone and how it was achieved, as well as their experiences with Rust and LLVM.
• They recall participating in a journal club where they discussed papers on synchronous IPC systems and the L4 family tree.
• The group explains the purpose and process of journal club, where members read papers and discuss them together.
• Microkernels, specifically Mach and L4, and their performance
• The impact of papers that criticized microkernels for performance issues
• The reaction of Licki, who wrote L3 and L4, and his inspiration for L4
• The influence of Licki's work on Hubris and its IPC mechanism
• The avoidance of labeling Hubris as a microkernel due to potential negativity
• The complexities of categorizing operating systems and software
• The importance of considering specific use cases and requirements when evaluating systems
• The speakers discuss the importance of not being rigid with categories and labels in computer science, and how they can be fabricated for convenience.
• The Hubris operating system is compared to traditional micro kernels, but is found to have nuanced differences and similarities.
• The speakers discuss the benefits of knowing all tasks at compile time, and how this eliminates certain problems and complexities.
• The design of Hubris was influenced by the constraints of deeply embedded systems, where the operating system is designed to compile other things.
• The speakers discuss the origin of Hubris and how it was influenced by the debugging of Talk and the need for a new approach.
• The development of Hubris is discussed, including the initial port to the STM chip and the later port to the LPC55.
• The speakers discuss the challenges and quirks of developing for different hardware platforms, and how some tasks are easier than others.
• Discussion of semi-hosting as a debugging technique for embedded systems
• History of debugging in embedded systems, including the limitations of semi-hosting
• Comparison of semi-hosting to other debugging methods, such as JTAG and on-chip debuggers
• Explanation of how semi-hosting works, including its protocol and limitations
• Discussion of the advantages and disadvantages of semi-hosting, including its speed and ability to work on a wide range of chips
• Warning about the potential consequences of using semi-hosting in shipping code
• Semi hosting: running parts of code on workstation and parts of code on embedded processor
• ITM (instrumentation trace macro cell): faster, but lossy
• Advantages of semi hosting: not lossy, guaranteed output
• Build process: producing ELF files per task, kernel, and build archive
• Build archive: containing ELF files, configuration files, and interface definitions
• Core dump support: blowing out ELF file with build archive in one section
• Debugging: using build archive to ensure correct symbol set and version of firmware
• Discussion of debugging information being included in zip files, separate from the binary, to reduce device storage
• Comparison of this approach to Windows, which also separates debugging information from the binary
• Explanation of how Rust's cross-platform development story allows code to work on multiple operating systems, including Windows, with minimal issues
• Discussion of the difficulty of building on Windows due to slow GitHub actions and lack of package managers
• Personal anecdotes about using Rust on Windows and the ease of development on the platform
• The speakers discuss an issue they had with Cargo, a package manager for Rust, that was resolved by using a scriptable environment.
• They introduce X Task, a pattern for writing custom scripts in Rust projects, which allows for more flexibility and automation.
• The speakers discuss how X Task has improved their build system and made it easier to extend the system.
• They mention that Cargo's design is geared towards building libraries and binaries, but not an entire OS, making X Task a necessary layer on top of Cargo.
• The conversation touches on the benefits of having a build system written in Rust, including ease of extension and maintenance.
• The speakers also discuss the importance of leveraging existing Rust libraries and frameworks, such as the one responsible for parsing DWARF information, to simplify tasks.
• They share their experiences and challenges with implementing and extending the build system using X Task and Rust.
• DWARF (Debugging with Dynamic Disassembly of Windows and Representations of Frames) limitations in Rust
• Use of Ada's variant records in Rust's DWARF representation
• Data-bearing enums in Rust and their use in debugging and logging
• Ring buffers and their use in storing and parsing data
• Dynamic dispatch and its importance in Rust's DWARF representation
• Rust's goal of being a memory-safe language for tasks and kernel development
• Comparison to Fuchsia's use of memory-unsafe languages in the kernel
• Hubris's design choices and limitations, including the lack of an IDL (Interface Description Language)
• Introduction of an IDL to generate client-server stubs and improve task development.
• Speaker 1 expresses concern that they may have come across as anti-IDL, leading to a discussion of the past.
• The group discusses using humans as code generators, and how past traumas and experiences can affect current work.
• A team member, Cliff, presents a new project called "Eyeball IDL", inspired by the poem "Ozymandias".
• The project's mascot is a broken statue, and its name is a reference to the poem's themes of grandiosity and decline.
• The group discusses the power of build.rs files in the Rust ecosystem, and how they can be used for code generation and dependency management.
• A team member notes that build.rs files are often underappreciated, but can be incredibly powerful and flexible.
• Discussion of integrating Rust and firmware for server board
• Use of Include bytes directive in Rust to include compressed binary data in firmware
• Leveraging Cargo to build crate for embedded architecture
• Using Ron for generating interface definitions and asset definitions
• Parsing and error messages for Ron
• Importance of having interface definitions in build archive for Humility
• Connection between current project and hardware-software co-design research
• The definition of co-design in software and hardware development is discussed, with one speaker noting it's a spectrum and another arguing that it's about making compromises across the software and hardware stacks.
• A common modeling language or system is mentioned as a possible approach to co-design, but its limitations are acknowledged, specifically the difficulty of machines to make intuitive leaps.
• The "Berkeley definition" of co-design, which involves simulating the entire system and then partitioning it, is discussed, but it's noted that this approach may not be practical for all situations.
• A practical example of co-design is shared, where a person used a "mocking out" approach to simulate hardware interfaces on a desktop system before building the actual hardware.
• The idea of treating the hardware and software stacks as a single problem space is discussed, and it's noted that co-design should focus on human judgment and engineering rather than relying on a single unified software system.
• The flexibility and options provided by co-design are highlighted, allowing for different approaches to building a system and choosing the right abstractions.
• The concept of having a "toolbox" of tools, including both hardware and software, is introduced as a key aspect of co-design.
• A specific example of co-design is given, where a decision was made to use an FPGA for power sequencing, and the flexibility to change this approach in the future is noted.
• Discussion of Conway's Law and the benefits of not letting the structure of a product or software application reflect the structure of the organization that created it
• The importance of humility in systems development, specifically the use of the Humility Diagnose tool
• The value of simplicity and flexibility in system design, with a focus on reducing complexity and overhead
• The impact of Rust on system development, particularly in terms of reducing mental overhead and enabling developers to focus on higher-level concerns
• The benefits of stealing (i.e. adopting) successful ideas from other fields, including memory protection, secure silicon, and debugging features
• The importance of considering the needs of future developers and the potential for embedded systems to become more complex and difficult to work with.
• Challenges with formatting floating point numbers in Hubris
• Stack overflow issues due to formatting code
• Excitement and appreciation for the Hubris project
• Open-source nature of Hubris and Humility
• Upcoming plans for the podcast (possible cancellation for the holidays)
• Review of a video featuring a user's experience with Hubris