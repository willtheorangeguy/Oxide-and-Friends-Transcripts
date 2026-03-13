• The conversation begins with technical issues and Adam asking Brian to speak.
• Brian's 13-year-old son has created a fake Twitter account to troll him and pretend to be his #1 fan.
• Brian discusses the challenges of being a public figure and having his name and identity confused with others.
• He shares an experience where he was mistaken for Adam Leventhal, a British sportscaster, and received replies from him.
• Adam and Brian discuss the humorous side of being mistaken for each other and how it's a reasonable confusion.
• The speaker's favorite team is the Checkers, who are based in Nashville
• The speaker attended a minor league hockey game in Grand Rapids, Michigan, where they saw the Griffins play
• The game was in October 2001 and felt like a patriotic act in the aftermath of 9/11
• The speaker visited the Gerald Ford Presidential Museum in Grand Rapids
• The speaker initially had a cynical view of Gerald Ford, but was impressed by the museum's display of his inaugural address
• The speaker now has a positive view of Gerald Ford and is a "super fan"
• The discussion revolves around Roger Faulkner, the inventor of the proc file system
• Roger's passing and legacy are mentioned
• The speaker recalls writing an obituary for Roger and making his paper on the slash proc file system freely available
• The speaker shares anecdotes about Roger's work and personality, including his focus on making programs debuggable
• A conversation about Roger's use of linked lists in his code is discussed, with the speaker joking that Roger liked to "roll with" order of N squared performance.
• Code review of an AVL tree
• Watch points and their limitations
• Libwatch Malick and its problems
• AVL trees and their efficiency
• The use of watch points for debugging
• The speed and usefulness of watch points
• Discussing the debugging process and how it feels like a "soup" when it works
• Mentioning Roger's contribution to the debugging infrastructure and its impact
• Describing how building automation on top of reliable mechanisms exposes shortcomings
• Introducing S trace and its relation to tracing system calls and signals
• Discussing P trace and its flaws, including slow performance and interface issues
• Mentioning the replacement of P trace by /proc in Unix and its use in Linux for system information
• Discussing the pain of using Pete trace for debugging, particularly with regards to the weight system call
• Mentioning the concept of "overloading" in debugging and the need for a single word to describe it in German
• Misuse of a mechanism in the kernel
• Discussion of inter-process communication (IPC) in legacy systems
• Legacy system's reliance on Ptrace
• History of Ptrace and its documentation
• Difficulty in replacing or modifying legacy code
• Computers are growing exponentially and the best time to fix issues is now.
• It's better to apologize today than to wait 20 years.
• A past project emulated P trace using a shadow process.
• The project led to the development of branded zones that pretended to be Linux.
• The developers were granted a patent for their work.
• Josh is mocked for supposedly hating the emulated P trace.
• Discussion of emulating one system on another and the challenges of maintaining bug-for-bug compatibility
• Reference to Petrae's and the difficulties of implementing certain features
• Mention of Go's dependence on V fork semantics and signal disposition
• Emulation of a system's bugs and the complexity of thinking about the original implementers' intentions
• Discussion of P trace mechanism and its thin emulation
• Reference to upstart and its use of P trace to track process life cycle across double fork boundaries
• Emulation of a system did not receive the expected information, leading to a lot of implementation work to achieve sufficient fidelity.
• The emulation had to work like the real system and had to implement S trace correctly.
• The development team had to move from a trampoline-based model to stack switching, which changed the emulation path and affected the implementation of P trace.
• Stack switching was necessary because the original model did not work with the Linux system call API, which is passed by register with no stack requirement.
• The emulation had to adapt to the new stack switching model, which involved the kernel knowing which emulation stack to drop things onto.
• Bugs in an application that worked on one operating system but not on another
• Application core dumped due to reliance on implicit behavior (phishing in its own stack)
• Need to push additional values on the stack to work around Intel bugs
• Emulation stack vs. native stack and how they interact
• Challenges of collecting register information with shadow copying
• Lessons learned from the emulation stack: separating collection of information to a more secure location, but still needing to chain contexts together
• Use of magic values and signal handling in software development
• The problem with relying on magic values and signal handling
• The need for clear abstractions and rules in software development
• The concept of moving all signal handling into the kernel
• The inspiration of Microsoft's WSL from the speaker's work
• The regret of not fully pursuing the idea of moving all signal handling into the kernel
• Windows subsystem for Linux (WSL) explained as an emulation layer
• Discussing running Illumos on M1 (ARM CPU)
• M1's architecture and limitations for running certain operating systems
• Virtual machine and emulation capabilities on M1
• Laura's expertise on ARM and M1's performance
• M1's non-compliance with standards and its impact on running certain OSes
• Challenges and workarounds for booting operating systems on M1
• Efforts to get Linux and other operating systems to run on M1 hardware
• Challenges and controversy surrounding Linux kernel updates for M1
• Virtualization layers as a potential solution for running non-Apple operating systems on M1
• Difficulty in emulating M1 machines and the need for a complete emulator
• AWS offering a macOS platform for cloud development
• Mac Minis strung together
• Promo video
• Apple's lack of interest in the server space
• VMware Fusion
• Chirp systems and clones
• Power Computing
• The Power PC standard
• Apple's shift away from the PowerPC architecture
• Discussion of a stolen laptop, specifically a power PC laptop running Solaris 251
• Concerns about the treatment of the location where the laptop was stolen, including the use of the term "graveyard" and the feeling of "fetishizing the dead"
• Explanation of the laptop's uniqueness as a power PC implementation running a little-endian operating system
• Story about the laptop's potential "adventures" and the thief's realization of its worthlessness
• Commentary on the operating system's limitations and the irony of it being vindicated years later by the adoption of little-endian architecture in open power
• Discussion of a YouTube talk by Brian
• Mention of a laptop being present in the talk
• Accusation of retelling stories
• Reference to the H programming language
• Discussion of language H and its relation to a COBOL-like language
• Mention of the book "The Friendly Orange Glow" by Brian Deer
• Discussion of the D language and its relation to language H
• D Trace hooks in Mozilla's Spider monkey not maintained
• Experience with D Trace, but unable to get it to work
• D language and its capabilities
• D Trace review of Google, but it's incomplete
• Upgrade to app, mentioning it's impressive that it didn't crash
• DM about upgrading app, and a brief mention of Walter Bright's D
• Discussion about the D language
• Concerns about the name of the language, specifically that it is a letter of the alphabet and may be too generic
• Reference to the D trace language and its relation to the D language
• Mention of the language being developed in parallel with another language, D
• Discussion of the language's similarity to Auk and its development by multiple individuals
• Recollection of a specific time period and event in the development of the language
• Unix commands named after their authors
• Bourne shell and its relation to Algol 68
• Discussion about the programming language used for the Bourne shell
• Comparison of Algol 68 with other programming languages
• Explanation of Algol 68 constructs in the Bourne shell source code
• Interruption and loss of conversation due to phone issues
• The speaker is optimistic about a specific app not dying, citing previous experiences
• Android's visibility is poor, making it hard to diagnose memory leaks
• The speaker is looking for better tools for monitoring memory usage on Android, but none exist
• D-Trace review talk at Google is mentioned, and the speaker has built context for a question they care about
• D-Trace is a domain-specific language that is highly specific and ergonomic, allowing for declarative data collection
• The speaker is cut off by Twitter Spaces and they are trying to praise the new features of the platform
• The conversation ends with the speaker trying to continue a previous point about working with languages that aggregate data
• The speaker has experience with D-Trace and finds it somewhat ergonomic compared to SQL or Vizicalc
• D-Trace is a domain-specific language, but its syntax is similar to relational databases
• The speaker was inspired by Auk when designing D-Trace
• The aggregating operations in D-Trace came out of using the language itself
• The creators of D-Trace should use the language to make it more ergonomic
• D-Trace was used extensively for debugging by the speaker and others
• The speaker and others were not programming language experts, but had practical experience with D-Trace
• The limitations of D-Trace were stark compared to other languages.
• The speaker reflects on the development of the D programming language
• Auck is mentioned as a design principle, but also as a pejorative term in the context of programming languages
• The speaker notes that Auck was originally intended as a pragmatic approach, but is now viewed as a criticism by some in the PL community
• The speaker contrasts Auck with the D language, which is described as more structured and less fussy, but also notes that D is not immune to criticism
• The conversation touches on the importance of pragmatism in programming language design and the tension between ease of use and theoretical purity.
• Discussion about the creators and development of a software or technology
• Mention of Detrace and its relation to the current project
• Comparison of the development time of Detrace to the current project
• Reference to Greg Papadopoulos and his views on oxide
• Discussion of domain-specific languages and their impact on computer science
• Mention of CUDA, NVIDIA, and GPGPU
• Reference to Rust and its significance in the field of programming languages
• Discussion about the importance of language in computing systems
• Challenges of using new technologies and languages
• The concept of domain specificity and its benefits
• The use of proc macros in programming
• The potential of new technologies, such as Rust, to improve domain specificity
• The idea of "survivor bias" in the adoption of new technologies
• A humorous exchange about the activation of a microchip in someone's brain
• Rust's macro system is complex and powerful
• Macros in Rust expand into code that the compiler can handle well
• The macro system is particularly well-suited for metaprogramming
• Error messages from macro expansion can be difficult to understand
• The macro system is useful for a wide range of languages, including C++ and GLSL
• Metaprogramming is a challenging but powerful tool for programming
• Rust's macro system is being utilized by various efforts, including NVIDIA's const expert work
• Library called Salsa and its author's experience
• Comparison of build systems and their complexity
• Power of Rust's proc macro system to generate good error messages
• Similar experiences with error messages between Rust and other languages
• Latitude for error handling at the macro level in Rust
• Need to correlate user input with the compiler for effective error handling
• Comparison of proc macros to compiler plugins
• Writing a Rust program that interacts with the pause tree and token stream
• Controlling the compiler's behavior and output
• Error handling and user feedback from the Rust compiler
• The importance of debugability and usability in Rust macros
• Comparison of Rust macros with the C preprocessor and their respective limitations
• Discussion about the concept of "hygienic" and its relationship to programming
• Mention of Rust and its macro rules
• Comparison of Rust to other languages, such as Python
• Explanation of procedural macros in Rust
• Description of how procedural macros allow for "compiler channel programs"
• Discussion of the "forbidden fruit" aspect of procedural macros
• Mention of colleagues who feel procedural macros should be more restricted
• Explanation of how procedural macros allow for domain-specific languages (DSLs) within Rust
• Discussion of formatting challenges and indentation when using procedural macros
• Story about writing Python within Rust using procedural macros
• Discussion of language innovation and its importance
• Mention of Python, Java, and Rust programming languages
• Discussion of Proc macros and DSL in Rust
• Mention of TCL (Tool Command Language) and its relevance to EDA (Electronic Design Automation) world
• Intercal language being mentioned as a possible addition to the discussion
• Comment about Jonathan Turner and his expertise in Rust and its ergonomics
• Discussion of macros in Rust and their potential applications
• Mention of ptrace and its relevance to the discussion
• Desire to demonstrate analytics and viewership data to support a claim about VFork
• Discussion of D Trace and its implementation
• Feature request for time series data on who's listening
• Request for analytics and V fork effect in Twitter spaces
• Mention of Plan 9 and its implementation in D Trace
• Comparison of D Trace to Plan 9 and its syntax
• Discussion of Stack captures and backtrace features missing in D Trace
• Comment on the usefulness of D Trace despite some syntax issues
• Mention of Orc and its relation to Plan 9 and D Trace
• Discussion of a new space to meet in
• Kudos to the winter space team for improvement
• Touching on the documentary "Silicon Cowboys"
• Next week's meeting will focus on Silicon Cowboys and Compaq
• Review of a book called "Open" by Rod Canyon
• Discussion of the Netflix documentary "Silicon Cowboys"
• Review of the documentary's relevance and accuracy
• Parting thoughts and looking forward to next week's meeting
• Conversation ended