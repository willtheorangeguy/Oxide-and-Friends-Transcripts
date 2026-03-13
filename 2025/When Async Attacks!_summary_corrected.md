• Discussion of Linux audio issues and the humorous reactions to them
• Comparison of dealing with screaming children on flights to audio issues
• Shared experiences of travelling with young children and dealing with peanut allergies on flights
• Joking about the lack of functional systems and audio on the call
• Reference to a previous Meet failure and its impact on the discussion
• Overview of the company's oxide rack development and production processes
• Mention of a testing environment for the oxide rack, affectionately called "dog food"
• Discussion of a data centre setup for testing the oxide rack
• Problems with performance and latency issues after a software update
• Explanation of a disk removal process for compliance testing
• Investigation of database connection issues and latency problems
• Discussion of a 5-node Cockroach DB cluster with replication factor set to 5
• Use of debugging tools to determine database response and connectivity issues
• Review of the debugging process and identification of possible causes of the latency problem
• Discussion of a performance issue where HTTP requests were taking 8–9 seconds to complete, but database queries were not taking that long
• Use of Trace probes to investigate the issue and find that the problem was not with the database
• Introduction of the Ross USDT crate, which allowed for dynamic instrumentation of Rust programs
• Explanation of how the USDT provider or probes were used to exonerate the database and identify the issue
• Discussion of the Oasis JSON processing and how it was used to transmit complex types from user land to the kernel
• Mention of the CPU performance counter probes and their implementation in Trace
• Conclusion that the issue was not with the database, but with the control plane endpoints
• Discussing a mysterious 8-9 second delay in handling requests
• Investigating logs to understand the delay and finding 100-150ms discrepancy between reported and actual handling time
• Considering possible causes, including client issues, TCP problems, or database queries
• Focusing on CORE, a connection pooling and service discovery crate, as a potential cause
• Analyzing error messages and connection management to understand CORE's behaviour
• Investigating how many connections were available at any given time to determine if it was a connection pool issue
• Discussing the limitations of CORE and the need for more evidence before making changes
• Treating a problem without understanding its root cause
• Difficulty in determining whether a problem is resolved
• Concerns about Core scheduling claims
• Instrumentation and data analysis
• Desperation and brainstorming for solutions
• Latency and error analysis in claim acquisition
• Trace probes and system monitoring
• Surprising latency issues due to many claims being held for extended periods
• Investigation into the number of connections in use, finding only 2–3 connections in use at a time
• Difficulty tracing the number of claims outstanding due to relative differences rather than absolute numbers
• Async Rust code complicating debugging efforts
• Limited ability to infer state about the system due to lack of experience with async models
• Difficulty in tracking the program counter and understanding the location of tasks in the async system
• Debugging asynchronous systems is challenging due to the lack of information in the production binary.
• The program counter and stack pointer are architectural state, but additional information is often user-space specific and hard to access.
• Traditional debugging techniques may not work in asynchronous systems, and new approaches are needed.
• Tools like Trace and core probes can be used to track system activity, but they have limitations and require careful use.
• Speculative tracing can be used to gather information about system activity, but it may not always be applicable.
• Debugging asynchronous systems can be compared to trying to piece together events after waking up from a long unconscious period.
• The discussion of a system's behaviour, where claims were not satisfied for 10+ seconds but then suddenly satisfied with new connections.
• The use of state maps as a visualization tool to understand complex system behaviour.
• A Cassandra benchmark that performed poorly due to angling and QR issues.
• The use of state maps to diagnose problems, including a specific issue with Postgres writing zeros to a new file and causing right throttling.
• A discussion about the complexity of big systems and the need for tools like state maps to understand their behaviour.
• Writing zeros to a file causes system instability
• State maps used to explore problems, including the current issue
• Bryan Can trill skeptical of using state maps initially, but found them useful
• Sprig used to visualize system data, including CPU usage and delays
• Investigation reveals CPU bound threads, contrary to expectations
• Speculative tracing used to further investigate the issue
• Motivating example for speculative tracing: reducing trace data by delaying interest in events until after the fact
• Discussion of the issues with the current implementation of a Trace probe, including the high number of invalid probe arguments and the potential for cognitive overload.
• Description of a new approach to Trace that reduces the number of probe arguments and makes it easier to understand the output.
• Use of Trace to identify a performance issue with a background task in a system, specifically a task that assembles a data structure to help the system figure out which certificate to serve and which silo to operate on.
• Identification of the root cause of the performance issue, which was many invalid certificates (around 10,000) that were causing the system to slow down.
• Solution to the issue, which involved removing the invalid certificates and testing the system again to see if the problem had been resolved.
• Discussion of the remaining issue, which is a latency of around 500–700 milliseconds, but which is still less noticeable to users.
• The conversation starts with a discussion about a problem that doesn't make sense, but the data suggests a causal relationship.
• The problem is reproduced on a dev system, which changes the approach to solving it.
• The team decides to focus on understanding the issue rather than just resolving it, to potentially improve the overall system.
• Eliza Weisman suggests instrumenting Tokyo with TRACE probes to gather more information about the task lifecycle.
• The team is excited about the potential solution and decides to implement it immediately, rather than waiting for a formal demo.
• Tokyo task execution and correlation with OS threads
• Visualization of Tokyo task execution with a state map
• Identification of a specific pathology in task execution
• Discussion of the LIFO (last in first out) optimization in Tokyo
• Explanation of work stealing and its relation to task execution
• Comparison of Tokyo's LIFO optimization with a similar optimization in the OS
• Work stealing in Tokyo causes problems when a compute-bound task is in the LIFO slot of a thread, preventing other tasks from running
• Turning off work stealing or tuning it down can resolve the issue
• John's investigation revealed a potential problem in the work stealing code, where a division operation can prevent stealing tasks from another thread
• Dave's analysis connected the dots between the work stealing issue and the corking of the whole system, identifying a specific request that was critical to forward progress
• The problem was caused by a background task that held a database claim for a long time, preventing other tasks from releasing the claim and causing a bottleneck in the CORE code
• The corking of the whole process was related to a different code path in CORE that maintained connections to multiple database backends.
• Discussion about a system optimization issue related to async worker threads
• Problem with LIFO (Last-In-First-Out) slot causing tasks to be blocked
• Debate about the "Tokyo" documentation and its advice on compute-bound work
• Difficulty in determining when a system will hit the optimization issue
• Discussion about the trade-offs between async and blocking worker threads
• Example of a specific case where the optimization issue caused a problem
• Debate about the generality of the advice in the "Tokyo" documentation
• Discussion about the complexity of determining when to use async or blocking worker threads
• Comparison to the halting problem and its difficulty in determining when a system will behave unexpectedly
• Processor sets and their limitations in certain use cases
• Async work and the advantages of using a shared thread pool
• Tokyo console and its limitations in production environments
• Intrusive instrumentation and the disabled probe effect
• Runtime linting and warnings in Tokyo console
• D Trace crate and its ability to provide total visibility into system execution
• LIFO optimization and its impact on system behaviour
• Debugging of an issue related to Omicron, a system or component that is not fully understood
• Comparison to the Debug Odyssey, a previous complex debugging experience
• Discussion of the benefits of preemptive multitasking in avoiding similar issues
• Ideas for improving debugging, including:
	+ Adding more probes to the Tokyo console
	+ Implementing task microstates to track task state and activity
	+ Using USDT (Unix Socket for Debugging and Tracing) probes
• Analogy to the Apollo 13 mission, highlighting the value of collaboration and expertise in debugging complex problems
• The team is discussing a recent podcast episode
• The episode was generated quickly through collaboration and iteration
• The team jokingly refers to their company as a "ruse for generating content"
• Bryan Can trill mentions a hypothetical future episode with Morris Chang
• The team thanks each other and signs off