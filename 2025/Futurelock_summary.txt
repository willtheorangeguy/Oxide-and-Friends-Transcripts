• Bryan and Adam discuss the scheduling of their podcast and its potential conflict with the World Series
• They debate whether a runner should be sent from first to second in a specific baseball situation
• Bryan argues that sending the runner would have been the correct play, citing baseball strategy and logic
• They also discuss Will Klein's impressive pitching performance in the 2018 World Series
• The podcasters discuss their failure to discuss the async cancellation issue in a previous episode, with Rain Paharia's blog entry on the topic being mentioned
• Debugging a pathology in the oxide rack distributed system
• Identifying a hung Nexus instance and trying to reproduce the issue
• Using logging and database queries to rule out obvious causes
• Using paid provider tracing and probes to identify the problem
• The issue is related to Qorb connection pooling and Tokyo task activity
• The problem is similar to a previous issue debugged in June, where the Tokyo scheduler was not picking up a runnable task
• CORB (CORB pool) has probes and internal bookkeeping, which seems to be functioning normally
• CORB's behavior is not matching expectations, with messages not being received from senders
• The team has ruled out several theories, including observing the wrong CORB pool and CPU issues
• The main theories being considered are that the Tokyo MPSC channel is broken or that there are two database connection pools
• The team is struggling to understand the behavior, with Bryan Cantrill comparing it to a mystery to be solved
• The tracing has shown that senders are going to sleep on the sending side, and the receiver is frequently polling but finding no messages
• The team is discussing how it's possible for this behavior to occur and are considering the possibility that there's an oversimplification in their mental model of the MPSC channel
• Discussion of a mysterious problem with a channel being empty despite many tasks trying to send to it
• Use of DTrace and dynamic instrumentation to collect core dumps and debug the problem
• Analysis of the core dumps using Ghidra and source-assisted reverse engineering
• Investigation of the semaphore and linked list used in the channel
• Confirmation that the channel is indeed empty and that there is no data corruption
• Discussion of the implications of the findings and the ongoing investigation
• Investigation of a system failure caused by a bug in the distribution of permits
• Use of Loom, a concurrency model checker, to simulate possible interleavings of events
• Attempt to reproduce the problem through production-focused debugging
• Collection of core files from the sender and receiver
• Analysis of core files to determine the internal state of the channel
• Confirmation of two theories: the internal state of the channel is corrupted, and the channel has no permits available
• Elimination of other theories, including sender leakage and receiver failure to return permits
• Discussion of a system issue and multiple theories for its cause
• The system has self-corrected, but the issue is expected to recur
• Debugging efforts have been ongoing, including examining the core file and message blocks
• The team has realized that linked list blocks can be reused and potentially uninitialized
• A key discovery was made by John Gallagher, which was described in the transcript
• The team has been unable to replicate the issue and is trying to figure out what caused it
• A previous question by Sean Klein is identified as the one that led to the answer
• Discussion of a difficult-to-reproduce bug in Tokyo
• John Gallagher describes the failure mode and its relation to a select with a mute feature
• Reproducer is created and reproduces the problem immediately
• Celebration of the success in reproducing the bug, likened to a "walk off home run"
• Explanation of the crux of the problem, involving multiple futures and a Tokyo task
• Discussion of the task versus future distinction in Tokyo and its importance in understanding the bug
• Explanation of concurrency and parallelism in the context of Tokyo and async Rust.
• Complexity of concurrency vs. parallelism in programming
• Importance of intention and context in understanding concurrency issues
• Difficulty in debugging concurrency problems, particularly in asynchronous systems
• Comparison between traditional deadlocks and live locks, and the unique characteristics of future locks
• Role of language constructs and tooling in hiding or revealing concurrency issues
• Difficulty in understanding and managing concurrent state in asynchronous systems
• Novelty of concurrency issues in asynchronous systems, and the need for new approaches to debugging and understanding them
• The need for concurrent execution of multiple futures in a single task
• Comparison between tasks and threads, and how treating tasks as threads can avoid certain bugs
• Analogies to the "green threads" model and the end-to-end scheduling model
• The historical example of the MNET scheduling model in Solaris, which had problems with blocking threads
• The introduction of the SIGWAIT signal to mitigate the problems of the MNET model
• The impact on programming and debugging when signals are involved
• The challenge of reproducing and debugging concurrent execution issues in complex systems
• Abstraction layers in software development
• Debate over async Rust idiosyncrasies
• Discussion of a specific bug in the Tokyo library
• Analysis of the library's documentation and communication
• Comparison to C++ memory management and Node.js
• Discussion of "zebras" - unusual and complex problems in software development
• Acknowledgement of Rust's success in eliminating certain runtime problems.
• Discussion of a recent software bug and its resolution
• Comparison to previous similar bugs, including the "Tokyo delay slot" issue
• Importance of testing and debugging software in-house
• Analysis of the bug's cause, including the use of selects in loops with mutably borrowed futures
• Development of a checklist for identifying the specific conditions that lead to the bug
• Discussion of the "fire triangle" concept and the importance of understanding the interactions between different factors that can lead to a bug
• Importance of defensive programming and refactoring code to prevent similar bugs in the future
• Cancellation and future lock safety issues in asynchronous programming
• Difficulty in avoiding cancellation vs future lock bugs
• Importance of defensive programming to prevent pathologies
• Lack of documentation and clear guidelines for cancellation and its impacts
• Naming and socializing the problem to raise awareness
• Creating a PSA (Public Service Announcement) to describe the problem and its solutions
• Discussion of a deadlock issue and how chatGPT was able to identify the problem
• Dave Pacheco's use of intentionally vague variable names in the minimum reproducer
• Comments on hacker news, including some that were deemed unhelpful or beside the point
• Bryan Cantrill's praise for Dave Pacheco's responses to comments on hacker news
• Discussion of the tenor of the comments on hacker news and the ability of the community to have a productive discussion
• Discussion of a team's experience with a Rust async issue that was only found after writing 500,000 lines of code
• Reflection on the importance of good documentation and tooling for avoiding common pitfalls in async programming
• Acknowledgement that the issue was a validation of Rust's safety features, but also highlighted areas where the language could improve
• Talk of the need for better observability and debugging tools for complex issues like async programming
• Mention of the difficulty of debugging async problems due to their passive nature
• Discussion of how the experience was a reminder of the importance of defensive programming and the need for tools like Clippy to help prevent issues like this in the future
• Refactoring of Corb to make it more defensive has strengthened the project and given confidence in its future
• Upcoming episode on async cancellation will be discussed
• Upcoming episode will feature a "scrum of founders" discussing the book "Founder vs. Investor" by Elizabeth Zalman and Jerry Newman
• Bryan Cantrill apologizes for missing the Rust Conference due to not forcing the guests to attend