• The conversation revolves around a past article written by Speaker 1 about unikernels and Docker's acquisition of unikernel systems.
• The discussion centres around the hype and excitement surrounding unikernels in 2016, which is referred to as "peak Docker" by Speaker 1.
• Speaker 2 reflects on his experience learning about unikernels and how it seemed to be a solution in search of a problem.
• The conversation touches on the issue of overgeneralization and the use of prefixes like "mono", "micro", and "uni" to describe concepts that can lead to false dichotomies and emotional reactions.
• The discussion concludes with a debate about the value of revisiting and questioning existing abstractions, with Speaker 1 suggesting that there is both good and bad questioning happening in the unikernel space.
• The conversation also touches on the idea that some advocates of unikernels may undermine their own cause by not thinking critically and nuanced about the issues at hand.
• Discussion of abstractions in computing, with the idea that some abstractions may be flawed or unnecessary
• Mention of the "external" concept, which proposes that applications should handle their own low-level details
• Critique of the external idea, with speakers arguing that it would be difficult to debug and maintain
• Discussion of the appeal of microkernels and unikernels, which can provide a more manageable and conceptual framework for building systems
• Idea that the complexity of modern operating systems can be overwhelming and that revisiting and shedding unnecessary abstractions could be beneficial
• Reference to a recent decision to use a specific kernel or API instead of a different one, and whether this represents a missed opportunity to rethink and simplify existing abstractions.
• POSIX and WebAssembly integration challenges
• Difficulty implementing unikernels in practice
• External vs unikernel conceptual differences
• Importance of memory protection domains
• Spectre's impact on security considerations
• Hubris kernel experience with safe language and stack access
• Addressing the halting problem in kernel development
• Prior art in kernel development (e.g. biscuit kernel)
• Defining a unikernel and its characteristics
• Difference between a unikernel and a traditional operating system
• Importance of protection boundaries in preventing data corruption and system crashes
• Trade-offs between safety and efficiency in system design
• Hubris as a hybrid system that combines aspects of unikernels and traditional operating systems
• Discussion of stack size and memory protection in system design
• The idea of unikernels and their limitations in executing arbitrary processes
• Criticisms of unikernels for dismissing debuggability and its importance
• Comparison of debugging unikernels versus traditional operating systems
• The concept of debuggability and its value in building robust systems
• The trade-offs between debugging on the host versus in production
• The idea that unikernels can be seen as delivering software from another platform, which may not have a high value on debuggability
• The tension between treating machines like pets (debugging) versus cattle (scalability)
• Discussion of the challenges in debugging firmware and embedded systems
• Claim that the main issue is lack of care and attention to debuggability, rather than a fundamental problem
• Introduction of the concept of "runtime" and its importance in debuggability
• Discussion of specific tools and technologies, such as Core Site and ETB, and how they are not being used
• Argument that poor debugability is a result of lack of effort and prioritization
• Debate about the feasibility of debugging in remote environments and the role of SWD and root of trust.
• The community and open-source landscape for building tools for firmware development is lacking.
• Hardware-focused approach to debugging and development can be limiting.
• Current tools and libraries for firmware development are not well-suited for the task.
• A comparison is drawn between firmware development and software development, highlighting the potential for better tools and practices in firmware development.
• Unikernels are mentioned as a possible model for firmware development, but it's noted that there is no inherent reason why firmware cannot be built like software.
• The importance of investing in tooling and building tools alongside products is emphasized.
• The idea that the lack of robustness in unikernels is due to a lack of investment in tooling rather than an inherent property of unikernels is discussed.
• Examples of systems that have successfully implemented real-time systems without operating systems are mentioned.
• Discussion about whether it's possible to reason about stack depth and whether stack depth is a noble goal.
• A custom language that generated C code for a specific chip in a radar use case, but was never used.
• The importance of tools and languages that enforce strict constraints, such as no cycles in the call graph.
• Comparison of engineering and academic approaches to systems development, with a focus on real-time operating systems.
• The role of Rust as a language that helps shift cognitive load and enforces strict constraints.
• Discussion of MIRA and its limitations in being adapted to Rust.
• Efforts to adapt Rust for use in safety-critical applications, such as medical devices.
• Debate about whether the "best" technology always wins, and the influence of human factors.
• Discussion on the ubiquity and greatness of technology
• Turning point for Rust and its success
• Importance of taking social and non-technical factors into account in programming language design
• Role of backing and funding in a programming language's success
• Balance between purely technical and non-technical aspects of a technology
• Discussion on trust, distribution, and price as factors in a technology's success
• Importance of human factors and non-technical considerations in programming language design
• Exploration of new problem spaces and ideas in programming languages
• Differences between various unikernel systems, such as Mirage and Rump
• OCaml's potential as a language for building unikernels and its current resurgence in popularity
• Facebook's use of OCaml for tooling and programming language-related tasks
• Criticism of PRNESTOStrups piece on safety and its portrayal of the software community
• Discussion of the importance of considering the unit of delivery and complexity in software systems
• Reference to Levinthal's conundrum, a metaphor for finding the root cause of a system's problems
• Complexity in systems and emergent behaviour
• Reducing cognitive load and simplifying abstractions
• The success of Rust and its approach to language design
• Graydon's expertise in programming languages and Rust's design
• Consumer Reports' report on memory safety and its implications for Rust and the programming language community
• Criticism of unikernels for lacking a clear problem statement
• Importance of having a strong reason for removing memory protection
• Need for practical examples of unikernels in use
• Comparison of compilers and operating systems, and the limitations of each
• The reality of a middle ground between compilation and runtime, and the need to balance the two
• Discussion of a university's operating systems class being taught by two professors with opposing views
• Debuggability of unikernels
• Importance of solving real problems and minimizing created problems
• Pragmatic middle ground for unikernels with virtual memory and debugging capabilities
• General-purpose operating system vs. unikernel
• Future of memory safety report and potential discussion