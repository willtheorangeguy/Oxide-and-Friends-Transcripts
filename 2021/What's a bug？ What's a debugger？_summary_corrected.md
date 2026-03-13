• The speaker's tendency to click on Twitter Spaces despite being aware of the time-wasting potential
• The speaker's "pathology" of being drawn to Twitter Spaces while trying to attend to a three-year-old
• The speaker's struggle to leave Twitter Spaces once they've entered, even when they're no longer interested
• The speaker's confession of being "accidentally load-bearing" in spaces they enter, feeling pressure to stay engaged
• The speaker's experience of having to apologize to interviewees for their child's interruptions
• The discussion of the goal of Twitter Spaces to bring in new voices and perspectives
• The speaker's anecdote about writing a Linux debugger, which they claim to have seen on Lobsters and Hacker News.
• The speaker has experience with Twitter and a debugger called lobsters
• They discuss the complexity of software systems and how it's hard to know what they're actually doing
• The speaker reflects on their experiences with debugging, including writing their first debugger as an undergraduate
• They share a story about a past project where they had to write a tool to understand the binding between a thread and an LWP
• The speaker discusses how they had to "plow" through the procedural linkage table to see dynamic library calls
• They express regret and confusion about some of their past decisions, including how they thought certain approaches were good ideas
• The speaker reflects on how their experiences have influenced their current approach to debugging and understanding software systems
• The speaker reflects on their experience with TNF (Trace Normal Format) and how it was difficult to use and parse.
• Debuggers are often written by compiler folks, not systems folks, which can lead to a focus on compiler-related problems.
• The speaker believes debuggers are often designed to solve reproducible problems, rather than unobservable ones.
• In-situ breakpoint debugging is seen as a narrow approach that is not suitable for most debugging needs.
• The speaker highlights the importance of automation and scriptability in debugging.
• They discuss the limitations of human-in-the-loop debugging, where stopping the system can prevent further analysis.
• The conversation also touches on the definition of a debugger and the speaker's complicated feelings about Lib Disc.
• The idea of Lib Disc, which interprets binary instructions in a structural form to aid in understanding and manipulating program components.
• Comparison to Hydra and other reverse engineering tools, and the potential for more crossover with debugging tools.
• Discussion of the LPC35 vulnerability and its connection to reverse engineering.
• The concept of debugging and whether Lib Disc is considered a debugger.
• The problem with the term "debugging" and its implications, and the search for alternative terminology.
• The analogy of a debugger or observability tool as a diagnostic tool, similar to a CT or PET scanner.
• The speaker discusses the concept of observability and its relation to being able to see software
• The speaker compares observability to medical imaging technologies such as MRI and CT scans
• The speaker shares a personal anecdote about using D-Trace and discovering an issue with a system that was previously unknown
• The speaker highlights the importance of observability tools in identifying and debugging issues in complex systems
• The speaker touches on the idea that observability is not just a mathematical property, but also about being able to see and understand the behaviour of a system
• The importance of determining what's talking to what in debugging tools
• The value of debugging tools in determining if issues are due to code, database, or other factors
• The risk of drawing incorrect inferences or measuring the wrong thing with advanced debugging tools
• The "don't kill the patient" principle in debugging, where not killing the system is more important than accurately diagnosing issues
• The difficulty of production debugging, where not killing the patient is even harder to achieve
• Examples of how debugging tools can cause system crashes or loss of knowledge about system states
• The importance of considering the long-term consequences of using debugging tools in production environments.
• Debugger limitations and challenges
• Debugger paradigm and responsibility
• Debugging postmortem vs. real-time debugging
• Distributed systems and debugging
• Debugging technology not keeping pace with architecture changes
• Observing and interacting with a system without interfering with it
• Value of understanding and analyzing dead programs
• Transient vs. ephemeral problems and prioritization of business metrics
• Difficulty in debugging future problems due to lack of empowerment to invest in necessary tooling.
• Definition of a bug and its importance in categorizing problems.
• Differentiating between performance and unexpected behaviour as bugs.
• Importance of visibility tools in addressing complex bugs.
• Role of CCD and unit testing in addressing bugs and ensuring production quality.
• Disconnection between advancements in CCD and unit testing and the need for better debugging tools.
• Discussion on the complexity of defining and understanding "bugs" in software
• The difficulty of identifying and addressing issues in deployed systems
• The role of testing in identifying and addressing issues, and how it has reduced the need for traditional debuggers
• The emergence of new issues in complex systems, particularly those that are deployed and mature
• The concept of automated and algorithmic debugging, and the AAD bug conference
• The importance of history in programming languages
• Overemphasis on automated debugging and its limitations
• Undervaluation of the academic community and debugging as a field
• The impact of better tooling, languages, and practices on bug detection and prevention
• The emergence of new, more interesting challenges in debugging and observability
• The significance of studying dead processes, particularly kernel deaths with memory corruption
• The difficulty of diagnosing complex memory errors and the potential benefits of identifying neighbouring memory allocations.
• Searching for a specific pointer in memory and finding its origin
• Discussing the benefits of using Rust for memory management and safety
• Describing the process of propagating types through the system and determining the type of memory object
• Comparing the ease of use and effectiveness of debuggers versus print statements (e.g. Print)
• Discussing how Rust's safety features reduce the need for forensic debugging and tooling, but leave intact more difficult bugs
• Mentioning the tradeoff between using debuggers and other tools to solve easier bugs vs. focusing on more complex and difficult ones
• The importance of Print debugging for quick and effective problem-solving
• Criticism of a professor's approach to teaching students to use a debugger over Print debugging
• Comparison of Print debugging with using a debugger, with the latter being more powerful but requiring more setup and knowledge
• The human UX aspect of why people reach for Print debugging before using a debugger
• Suggestions for improving debugger interfaces and education to encourage their use
• The speaker discusses discovering a statistical package and a patch that instrumented programs to log memory writes and infer bugs
• The speaker reflects on their initial reaction to a paper on abnormal memory writes and bug inference, and how their perspective has changed over time
• The speaker and others discuss the challenges of developing sophisticated tooling, including the need for specificity and the risk of creating a "least common denominator" tool like GDB
• The discussion touches on the importance of abstraction and programmability in tool development, and how these features can make a tool more powerful and easier to use
• The speaker and others discuss the need to motivate the education of new tooling and the challenges of getting people to try new technologies without an immediate need
• Discussion of print debugging and its limitations
• Use of QEMU and info registers for debugging
• In-situ debugging and its importance
• Observability and software tracing efforts
• CCD and test-driven development practices
• The need for debugging infrastructure and tooling to become a standard part of the development process
• Challenges of debugging dynamic languages
• Brief mention of a past project, Parrot, and its potential for making VMs debuggable
• Discussion about the name change of the software from Parrot/Pearl Six to ROK/Baku
• Mention of the difficulty in recalling the new name
• Reference to the end of Moore's Law and its impact on understanding and optimizing systems
• Discussion of the importance of understanding system behaviour and performance
• Lighthearted exchange between participants, including a claim of someone sitting on a point for several minutes