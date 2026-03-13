• Discussion of a humorous rap about the Gen Z Bible
• Personal experiences with compile times, including a story about working at Sun Microsystems
• Debate about the generation that wrote the Gen Z Bible, with one speaker's kids calling them a "boomer"
• Compile times as a problem that sneaks up on developers, making it hard to notice
• Story about a developer's experience with slow compile times, including a struggle with a debugger
• Build times and repository size are major issues for the Omicron project
• Incremental compilation has become a standard feature in Rust, but the large size of the Omicron repository causes compile times to be slow
• The team has struggled to identify and address the causes of slow build times due to the complexity of the build process and the multiple ways to build the control plane
• Absolute build times matter, especially once the build time exceeds a certain threshold (e.g. 45 seconds to 3 minutes)
• The team has implemented various measures to improve build times, including the use of timers and a unified build system
• The history of Rust's build systems, including the introduction of incremental compilation and the development of Cargo, has been discussed
• The team has expressed relief and satisfaction at the improvements made to build times and the development experience in Rust
• Voice analyzer discussed as a useful tool for developers
• Rust analyzer compared to syntax highlighting as a more useful tool
• Discussion of the history and evolution of compilers, including the shift from batch compiling to incremental compiling
• Roslyn compiler for C# mentioned as an example of a compiler that has adopted incremental compiling
• Query system in Rust's compiler discussed as an attempt to make it more incremental and efficient
• Discussion of the challenges of optimizing Rust builds and the need for a deeper understanding of where time is going
• Tools such as cargo build, cargo LLVM lines, and cargo bloat mentioned as helpful for analyzing build times and binary size
• Challenges of dealing with multiple signals and proxies for other data when trying to optimize builds
• Discussion of the complexities of solving build optimization problems and the need for a more nuanced understanding of the issues involved.
• The discussion revolves around the trade-off between using generics and "den objects" in Rust.
• Generics can lead to slower build times due to the creation of multiple function copies.
• A common technique to mitigate this is to use a thin shim to call a non-generic function, reducing the number of copies.
• The use of "den objects" can add a layer of indirection and runtime lookup, potentially affecting performance.
• The choice between generics and den objects depends on the specific situation and the importance of build time vs. runtime performance.
• The discussion touches on the concept of tables and their role in implementing polymorphism.
• Discussion of the trade-offs between using generics and traits in Rust
• Runtime performance differences between generics and traits
• Importance of being quantitative in measuring performance
• Cargo's feature system and its impact on compile times
• Cargo's "features" feature and its potential for combinatorial explosion
• A proposed solution using a "workspace hack crate" to manage dependencies
• Automation of this solution using Cargo Harari tooling
• Discussion of Cargo's dependency graph and unit graph feature
• Analysis of a specific issue with Cargo's unit graph causing unnecessary rebuilds
• Explanation of how panic handling works in Rust and its impact on build processes
• Identification of a problem with proc macros being built with panic equals unwind instead of panic equals abort
• Discussion of the limitations and trade-offs of using proc macros in Rust build processes
• Discussion of a problem with proc macros and build scripts causing inconsistent behaviour in dev and prod builds
• Realization that some configuration changes are needed to fix the issue, but no easy resolution is available
• Trade-off between dev and prod builds, with dev builds now using unwind instead of panic
• Importance of avoiding unnecessary work in system optimizations
• Review of changes made to address the issue, including a speed up of 1.26x in common scenarios
• Discussion of build scripts and their potential for causing performance issues
• Importance of proper handling of inputs and outputs in build scripts to avoid unnecessary recompilation
• The speaker discusses the difficulties in analyzing the output of the compiler's profiling tool, a JSON file that provides a timeline of the compiler's actions.
• The output is often in the tens to hundreds of megabytes, but can be as large as gigabytes when specific profiling is enabled.
• The speaker believes that more tooling is needed to make it easier to analyze the output and identify areas for optimization.
• The speaker is interested in developing tools that can provide aggregates based on modules and functions, and identify common patterns.
• The discussion touches on the use of the Serve library and its potential limitations, as well as the trade-off between generality and performance.
• The speakers also mention the importance of understanding the output of the compiler's profiling tool in order to optimize performance in large Rust projects.
• The discussion is about the trade-offs and costs associated with certain features and abstractions in Rust.
• The speakers mention the history of Rust and how it has evolved to include new features, some of which had hidden costs.
• They discuss the concept of "0 cost abstractions" and how it's not always true.
• The group talks about the pain points of using certain features, such as proc macros and Derive, and how they can be mitigated.
• They also discuss the importance of understanding the costs and trade-offs of using certain tools and libraries, such as Serve.
• The conversation also touches on the challenges of modernizing the Rust ecosystem and the potential costs of switching to a new library or feature.
• The speakers discuss the importance of considering the developer velocity experience, including build times, packaging, and deployment.
• Experience with linker options, specifically LLD, LD, and Mould
• Comparison of linker performance on different operating systems
• Benefits of using Mould, including speed and multicore utilization
• Discussion of static linking and its resurgence in importance
• Implications of monomorphization on linking and linking exceptions
• GPL and licensing implications of dynamic linking and code generation
• David Tone's proposal to compile proc macros into WASM and execute them to generate code
• Concerns about binary blobs and potential security risks
• Potential benefits of executing WASM binaries, including improved performance and sandboxing
• Tooling and profiling for Rust development, including single crate profiling
• Future of tooling and workflow for Rust development, including easily digestible profiling and overhead analysis
• Buck and distributed caching, and its potential application to caching and reproducible builds
• Discussion of build times and performance optimization in Rust development
• Buck 2 is a build system written in Rust, similar to Basel, and requires hermetic builds
• Buck 2 is a totalizing build system, meaning all dependencies must be expressed in its language
• The transition to Buck 2 requires porting existing tooling and potentially rewriting dependencies
• The use of Rust in Buck 2 is preferred over Python due to its performance and reliability
• There is a graveyard of abandoned build systems, including Sons and WAS
• Buck 2 is based on theoretical work in build systems and is a result of Meta's investment in this area
• There is ongoing discussion about writing a book on build scripts in Rust
• Discussion of a paper on build systems, specifically the paper by Simon Peyton Jones
• Analysis of various build systems, including Make, Basel, Buck, and Excel (as a build system in its own right)
• Categorization of build systems based on their scheduling and dependency models (static vs dynamic)
• Mention of Buck 2 and its design principles, including its lack of support for features
• Discussion of the trade-offs of Buck 2's design, including its opinionated model and hermetic builds
• Reference to the paper's influence on Buck 2's design and the trade-offs involved in using Buck 2
• Friction in build systems and how to deal with it
• Potential migration from Buck 1 to Buck 2
• Rust Analyzer compatibility with Buck 2
• Importance of build times and developer flow
• Discussion of various build systems and tools (e.g. Cargo, Harari, Excel)