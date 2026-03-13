• Criticism of the word "performance" in a business context
• Discussion of the word "learnings" and its usage
• Argument that language is not evolving, but rather being used for personal gain
• Critique of the word "leverage" as a verb
• Explanation of the concept of being able to explain complex ideas to others as a metric for understanding
• Discussion of the importance of documentation in product design and engineering
• Story of a parent trying to explain async programming to their child
• Discussion of the challenges of parenting and the importance of being able to communicate complex ideas to children
• Discussion of a 15-year-old's haircut that looks like an industrial accident
• Explanation of threading and asynchronous systems to a beginner
• Comparing threading to asynchronous programming and their differences
• History of multilevel threading and its origins in operating systems
• Discussion of the trade-offs and limitations of multilevel threading
• Examination of the arguments for and against multilevel threading
• Discussion of the limitations of async/await and its comparison to threads
• Conway's Law and its relevance to asynchrony
• Problems with 2-level scheduling models, such as loss of locality and affinity
• Critique of async/await for losing kernel-provided locality and affinity
• Importance of comprehensibility and the program counter in understanding threading and concurrency
• History of Unix and its evolution, including the introduction of multithreading and user-space threading
• Discussion of IO completion ports and their implementation in VMS/Windows NT
• Comparison of threading models, including end-to-end threading and user-space threading
• Discussion of Solaris' and other systems' handling of blocking system calls
• Comparison of POSIX signal handling in Solaris, Slaters, and other systems
• Criticism of UNIX design and its influence on modern async systems
• Examination of the Go runtime's use of timer-based signaling
• Discussion of Rust async and its potential for nonlinearity of response time
• Analysis of the debugging challenges in async systems
• Criticism of the lack of effort in making async systems debuggable and comprehensible
• Asynchrony and debuggability issues in Node.js and futures
• Comparison of Node.js with Rust and asynchronous programming
• Challenges of debugging asynchronous systems
• Erlang and RabbitMQ experiences, including difficulties with debugging
• Erlang's process-based concurrency model and message passing
• Implementing large systems in Erlang, including scalability and debugging considerations
• Discussion of emergent behavior in complex systems
• React and RabbitMQ examples of distributed systems
• Debugging issues with RabbitMQ and its limitations
• Single wait concept in Zig programming language
• Zig's approach to async programming and coroutines
• Debugability as a design center for Zig
• Introducing asynchronous programming to beginners, especially those with little experience
• Callback-based approach vs high-level abstraction in asynchronous programming
• Twisted Python, an asynchronous framework for Python, and its limitations
• Emergent behavior and production bugs in asynchronous systems
• Personal anecdotes of learning asynchronous programming through writing servers for specific projects (e.g. Shoutcast protocol, Internet radio stations)
• Discussion on how async is often introduced in practice, but not well documented or covered in academia
• Audio streaming with multiple listeners and issues with blocking write calls causing flaky connections
• Use of LAME MP3 encoder and concurrent processing to handle multiple listeners
• Introduction of asynchronous programming using Python's async core module and Twisted library
• Discussion of concurrency models and event loops in Node.js and Go
• Description of the HHBM/Hack async operations concept and its relation to Facebook's fork from PHP
• Event loop starvation problem and need for programmers to understand underlying models and use tools like CPU profiles
• Zig concurrency story and comparisons to existing concurrency models like gunicorn
• Trollius: a Python library that used the exception model for async IO
• Quay.io: a private Docker registry with a build manager that used Trollius
• Abusing the exception model for async IO is considered an "async hack"
• The system built with Trollius was considered a nightmare to work with
• Quay.io used a distributed process to build Docker files, with a lot of async state
• The speakers agree that building such a system today would be easier with better tools
• The discussion touches on the issue of runtime skewing throughput and the need for better debugging tools for async systems
• Post-crash replication issues with asynchronous systems
• Challenges of asynchronous programming, particularly in the context of kernel interactions
• Discussion of various asynchronous programming models and interfaces, including select, POSIX threads, and IOU rings
• Comparison of different approaches to concurrency, including futures and promises vs. asynchronous I/O
• History of Python's async programming models, including Stackless Python and Gevent
• General discussion of the difficulties of teaching and understanding asynchronous programming concepts
• Teaching threading and async as cooperative threading
• Origins of the Twisted framework from a multiplayer game project
• Discussion of why async is preferred over threads
• Upcoming guest Sean Silcox to discuss the book "Losing the Signal" about RIM's rise and fall
• Preview of the book and its potential as a major motion picture