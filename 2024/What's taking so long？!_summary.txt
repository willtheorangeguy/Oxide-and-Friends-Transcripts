• Intro music
• Discussion of a rap about the Gen Z Bible
• Debate over the book's author and the generation it represents
• Compile times as a hot topic
• Personal experiences with compile times, including working on the Solaris kernel at Sun Microsystems
• The impact of slow compile times on development and iteration
• Compile times were a problem for the company
• The problem was made worse by the architecture of the Hubris debugger
• The company's growth, including adding features and services, contributed to the problem
• Building a monorepo, like Omicron, can exacerbate the problem
• The issue is not just about speed, but also about being able to understand and optimize the build process
• A unifying system, like Rain, helped to address some of the issues
• The absolute times for build processes matter, and certain thresholds can make it difficult to work effectively.
• The discussion started with a personal anecdote about how the speaker left a project due to slow build times.
• The importance of accurate build times and the difference between initial build times and incremental compilation times.
• The history of Rust's build system, including the lack of incremental compilation in the past and how it was introduced.
• The evolution of Rust's terminology and how it has become more nuanced over time.
• The comparison between Rust's early days and its current state, with the speaker feeling that many pain points have been alleviated.
• The analogy of "telling the systems people that they can have nice things" and how cargo became a successful build system.
• A humorous exchange about the speaker's skepticism towards Rust Analyzer and its usefulness.
• Rust Analyzer's potential impact on the compiler
• Compiler technology changes since the Dragon Book
• Challenges of incremental compilation and handling malformed input
• History of tooling and the need to adapt to incremental compilation
• The Roslyn compiler's approach to incrementalism
• The Rust compiler's transition from batch to incremental compilation
• The query system's role in incremental compilation
• Time spent during build processes and the need for better understanding
• Target-rich environment of Rust makes it complicated to optimize build times
• Cargo LLVM lines and cargo bloat can help identify contributing factors to binary size
• Generics can sometimes lead to excessive monomorphization and large binaries
• Thin shims can be used to reduce the impact of generics on build times
• Refactoring code to use thin shims can be painful and not always possible
• Opting for trait objects over generics can be a good alternative in some cases
• Generics can have a cost and should be used judiciously
• Discussion of a retrospective or documentary-style discussion
• Trade-offs between using generic traits vs. trait objects in Rust
• Performance implications of using trait objects vs. generics
• Comparison of C++ and Rust's v-table implementations
• Trade-offs between optimizing runtime vs. build time performance
• Cargo's features and their impact on compile times
• Debugging and optimizing Cargo's performance issues
• Cargo's features feature causes issues with rebuilding dependencies when multiple crates use the same dependency with different features.
• A crate like syn can have multiple features, leading to a combinatorial explosion of possible feature sets.
• This can cause all dependent crates to be rebuilt, leading to a large number of unnecessary rebuilds.
• Mozilla Central Repository uses a workspace hack crate to solve this problem, but it requires manual management.
• Cargo Hakari is an automated workspace hack manager that resolves this issue by automatically adding build configurations to the workspace.
• Improved build times
• Cargo Akari's limitations
• Unit graph feature in Cargo
• Dependency graph and unit graph explanation
• Panic equals abort vs unwind settings
• Proc macro build with panic equals unwind
• Software cost associated with becoming part of the build process
• Panic handling in proc macros and its impact on build process
• Cargo's behavior with panic handling in proc macros and build scripts
• Tradeoff between dev and prod builds due to panic handling divergence
• Optimization and speedup achieved through changes to build process
• Impact on rebuild times and overall system performance
• Proc macros and build scripts can lead to bloated compile times
• Build scripts require careful setup to avoid unnecessary recompilation
• Proc macros can have significant performance impacts, especially with heavy use of derives
• Cargo provides a self-profiling flag to gain insight into build times and performance
• More tooling is needed to effectively interpret and utilize build performance data
• The challenges of analyzing large Rust crates and the need for better tooling
• The limitations of the cargo self-profiling feature and its inability to provide useful insights into performance issues
• The potential for a U32 overflow in the cargo self-profiling feature
• The need for more advanced tooling to analyze and optimize large Rust crates
• The importance of providing aggregates and summaries of performance data, particularly for derived traits
• The potential for more widespread adoption of Rust and the need for better tooling to support it
• A discussion of the Surdy crate and its limitations, and the exploration of alternative crates
• The flexibility and usefulness of Surdy (or similar tools) vs. other approaches like CERDI
• The trade-offs between generality and code that fits a specific use case
• The importance of understanding the costs of using certain tools or abstractions
• The natural back-and-forth between new functionality and its eventual stabilization
• The idea that there are always trade-offs and that different tools are better suited for different situations
• The importance of perspective and understanding the context in which certain tools are being used
• Cost reduction strategies for CERDI ecosystem
• Concerns about committing to CERDI and potential future changes
• Investigation of linker issues and performance
• Analysis of build times and developer velocity experience
• Comparison of different linkers (LD, LLD, mold) on various operating systems
• Results showing mold as a significant performance improvement in certain scenarios.
• Discussion about mold, a tool for integrating Rust code
• Comparison of mold's performance to other build tools, such as Lumos LD
• Explanation of why static linking is becoming more important, including the shift from dynamic linking and the benefits of multiple core usage
• Discussion of the implications of monomorphization on linking and the GPL
• Exploration of the blurring of lines between compilers and linkers, and the resulting complexities for projects using GPL-licensed crates.
• GPL and MIT licenses in the crate ecosystem
• Industry-wide rejection of the GPL
• Proposal to compile proc macros into WASM
• Potential security risks of executing WASM binaries
• Benefits of running proc macros in a sandboxed environment
• Robustness of Rust tooling and ecosystem
• Future of Rust tooling and workflow
• Need for improved profiling and optimization tools
• Desire for crate authors to have a clear understanding of their crate's performance and overhead
• Importance of being able to answer the question "what's taken so long?" in terms of build times
• Discussion of Buck and its capabilities in terms of caching and distributed caching
• Challenges and hurdles to adopting Buck as a build system for Rust projects
• The speaker mentions a tool called Reindeer, which converts cargo.toml files into Buck nodes
• The speaker highlights the challenges of moving from cargo to Buck, including porting tooling and dependencies
• The speaker discusses the test runner cargo next test and its limitations with Buck
• The speaker mentions the build tool Buck and its limitations, including the need for a deep understanding of its DSL
• The speaker compares Buck to other build systems, including Starlar, which is a DSL subset of Python used by Buck and Basil
• The speaker reflects on their past experiences with build systems, including scones and Woff, and how they can be frustrating to work with
• The speaker mentions the complexity and lack of guidance in build systems, including the need for manual patching and error handling.
• Implementing a good build system in Rust
• Research on build systems, including papers and authors
• Meta's involvement in implementing build systems based on research
• Discussion of a specific paper on build systems and its findings
• Analysis of various build systems, including make, Bazel, Buck, and Excel
• Categorization of build systems based on scheduling and dependency models
• Trade-offs between static and dynamic dependencies in build systems
• Monadic build systems and their design principles
• Discussion of Buck2 and its design choices, including its lack of support for features
• Comparison of Buck2 with Buck and Cargo, highlighting differences in build systems
• Trade-offs between Buck2's opinionated model and the need for feature support
• Advantages and disadvantages of Buck2's hermetic builds
• Discussion of Buck2's on-ramp and its potential to reduce friction in build systems
• Consideration of moving from Buck to Buck2, with potential benefits and drawbacks
• Discussion of David Barsky's work on cargo
• Need for a layer between cargo and tools that invoke it
• Importance of build times and developer flow
• Challenges and opportunities presented by Rust
• Integration of build systems and root cause analysis
• Personal anecdotes and lighthearted tone
• Brief mention of using AI to optimize builds