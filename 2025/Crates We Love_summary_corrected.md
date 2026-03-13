• The conversation starts with Adam and Bryan discussing a previous episode of their podcast and its length.
• Bryan shares a news article about Intel's CEO search and discusses the possibility of a permanent CEO being named.
• Adam and Bryan engage in a lighthearted "quiz" where Adam tries to guess the titles of books that had an impact on Bryan's professional life.
• The books in question are "Steve Jobs and the Next Big Thing", "Solve the New Machine", and the title of Bryan's blog entry when they launched the company, which was "Oxide".
• Bryan reveals that he had asked his high school senior son, Alexander, to ask him and his wife for three books that had an impact on them as adults, as part of an assignment.
• Discussion of reading the book "Skunk Works" by Ben Rich
• Introduction to a series of podcasts discussing books that have influenced the speakers professionally
• Mention of a tweet from Chris Kraków that inspired the discussion
• Introduction to the crate "pretty-please" and its use in formatting Rust code
• Discussion of the challenges of using Rust format in a programmatic context
• Introduction to the crate "quote" and its use in quoting Rust code for formatting
• Announcement that the speakers are implementing "pretty-please" and "quote" in their crates
• Discussion of the benefits of using these crates, including debuggable and testable code.
• Discussion of error handling in Rust and the need to collect and report multiple errors at once
• Introduction of the Minute crate, which provides high-quality error reporting and is inspired by Rust's error messages
• Example use cases of Minute, including storing a list of errors and reporting them with source code and byte offsets
• Comparison of Minute to other error handling libraries and tools
• Successful integration of Minute into the Rust IDE, Idle, to improve error messages
• Discussion of the benefits of high-quality error reporting and the value of collecting and reporting multiple errors at once.
• Discussing the benefits of using crates for error handling in configuration files
• Introducing crates serve ignored and serve path to error for error handling
• Comparing serve ignored and serve path to error, and their uses
• Mentioning the limitations of detail net credits and suggesting a higher limit
• Introducing crate derive where for automating implementation of traits
• Explaining the use case for derive where in a specific project
• Discussing the benefits of using derive where for a common problem in Rust development
• The experience of using ChatGPT to find crates in Rust and the phenomenon of ChatGPT "hallucinating" and creating non-existent crates
• The discussion of Choose Your Own Adventure books, specifically Inside UFO 5440, and how they were often meta and required unorthodox thinking
• The shared experience of reading Choose Your Own Adventure books and how they can be a common interest that bridges generational gaps
• The challenges of finding crates and Rust documentation, and the strategies for discovering new crates, such as sticking around in a particular codebase or using search engines
• The positive feedback loop of the Rust ecosystem growing and making it easier to find and use crates, and the excitement of discovering new crates through this process
• Discussion of the Ratatouille episode coming up in 2 weeks with a maintainer of the project
• Issue of finding crates with similar implementations and performance characteristics
• Importance of upfront documentation in crate development, specifically comparing with other crates and explaining why to use or not use a particular crate
• Bit field crates and comparison between different crates with varying interfaces
• Value of explicit documentation of a crate's values and considerations, such as performance or memory usage
• Discussion of the importance of being upfront about a crate's limitations and encouraging users to find the best tool for their job
• Discussion of performance trade-offs in Rust libraries
• Benefits and drawbacks of using specific libraries for command-line interface (CLI) parsing, such as clap and Lex opt
• Importance of documenting performance trade-offs and usage patterns
• Comparison of different libraries, including their design philosophies and features
• Mention of Loom, a model checker for concurrent Rust programs
• Conditional compilation for deterministic models in C++
• Using Loom to detect data races and deadlocks in concurrent code
• Loom's ability to exhaustively explore all permitted interleaving in a test
• The importance of using model checking tools like Loom to verify concurrent code correctness
• Loom's differences from other tools like than, SAN, and Val grind
• The challenges of writing concurrent code and the need for tools like Loom to detect hidden bugs
• The benefits of using Loom to improve code quality and reliability
• The impact of Loom on Eliza's approach to writing concurrent code and her opinion on its importance for complex concurrent software.
• Tokyo and its rewrite of the multithreaded runtime
• CDS Checker and its implementation in Tokyo
• Performance optimization of Tokyo
• Postcard serialization format and its use in Humility and Hubris
• BBQ crate and its unique features
• Pet Graph crate and its graph data structures and algorithms
• Discussion of Pet Graph, a Rust crate for graph data structures and algorithms
• Pet Graph's ability to manage adjacency lists and provide multiple graph representations
• Adam Levinthal's experience with Pet Graph in a project involving JSON schema to Rust conversion
• The crate's support for strongly connected components and other graph algorithms
• Comparison of Pet Graph to other Rust crates, including Detonate and SYN
• Discussion of the crate's popularity and how it's not too mainstream for some users
• Discussion of the "pound" operator in C and its equivalent in Rust
• Use of Paste, a crate for creating and managing code, and its limitations
• Comparison of libel and lib dwarf libraries for working with ELF and DWARF files
• Recommendation of Goblin and Gigli crates for working with ELF and DWARF files
• Discussion of HTTP mock crate and its use in end-to-end validation
• Shoutouts to various crates, including HTTP mock, RHDL, and Camino
• Rust's focus on being correct and handling edge cases
• Introducing the Amino library, which provides a simplified way to handle paths and strings
• Discussion of the trade-offs between handling all possible paths and the limitations of libraries like Amino
• Introduction of Evie Maps, an eventually consistent hash map
• Explanation of Evie Maps' design and how it reduces contention between readers and writers
• Comparison of Evie Maps to other concurrent hash map implementations
• Mention of other useful crates, including index maps and multi maps
• Brief mention of the bytes crate and its relationship to the hyper library
• Bytes is a reference counted byte buffer library, allowing for slices of the buffer to be taken and participate in the buffer's reference count.
• Buff list is a library built on top of bytes, providing a unified interface for working with byte sequences.
• Winnow is a parser library that provides a joyful experience for writing parsers, with a complete tutorial and high-quality implementation.
• Nom is another parser library mentioned, but Winnow is preferred for its ease of use and quality implementation.