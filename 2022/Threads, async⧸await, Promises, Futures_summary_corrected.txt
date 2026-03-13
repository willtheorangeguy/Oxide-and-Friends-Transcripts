• The speaker expresses disdain for the word "performant" and suggests a drinking game where someone has to define it after using it
• The speaker also dislikes the word "learnings" and prefers "learning" or other more precise terms
• The speaker mentions that language is only evolving when it's convenient for the speaker, otherwise it's not
• The speaker discusses other overused business buzzwords, such as "leverage" and "utilize"
• The speaker references Richard Feynman's quote about explaining complex concepts to a bright but new audience as a metric for understanding
• The speaker reflects on the challenge of explaining technical concepts to users with varying levels of education and experience.
• Engineers should document their own ideas to learn from their flaws
• A speaker is trying to explain asynchronous systems to a 5-year-old son
• The speaker has two teenage sons, one who is learning C++ and the other who got a bad haircut
• The speaker's parenting experiences, including a 15-year-old's decision to get a buzz cut and a disastrous haircut
• The speaker's reactions to his sons' behaviour, including frustration and embarrassment
• Discussion of explaining threading and async programming to someone with a background in dozens of lines of code
• Confusion between threading and async programming and the difficulty of explaining the distinction
• The presence of both synchronous and asynchronous elements in any system
• Discussion of Thread Mod and its relation to multi-level threading
• Historical context of multi-level threading, including its origins in operating systems from the late 80s to early 90s that only supported multiple processes, not threads.
• M to N thread scheduling model vs pure async systems
• Comparison of synchronization primitives in multi-level threading
• Limitations of creating millions of threads
• Asynchronous programming and async await
• Multi-scheduler systems and affinity issues
• Scalability and visibility limitations in user-level scheduling
• Critique of async await and its trade-offs
• Comprehensibility and thread/task definition
• Program counter and state importance in concurrent systems
• Implementing synchrony in Hubris using a series of synchronous tasks
• Discussion of Unix design and its isolation of synchrony
• History of Unix and its evolution, including the introduction of threading and user-level processes
• Critique of traditional Unix model and its limitations in handling concurrency and parallelism
• Comparison with other operating systems, including Vax VMS, Windows NT, and Polaris
• Examination of the concept of I/O completion ports and their role in asynchronous I/O operations
• The limitations of the UNIX system interface, particularly in regard to blocking system calls
• The potential for blocking even in non-blocking system calls, such as open()
• The "halting problem" analogy for understanding the challenges of blocking in system calls
• The difficulties of debugging and reasoning about async systems, particularly when queues are architecturally hidden
• The need for better debugging tools and techniques for async systems
• The experience of implementing the USDT interface for Rust, specifically in regard to the D-Trace system
• Challenges with debugging async/await code in D-Trace
• The limitations of using thread IDs in debugging asynchronous code
• The importance of stack backtracks in understanding code execution
• The difficulties of debugging Node.js and the async/await model
• The limitations of using callbacks in debugging asynchronous code
• The potential of Erlang and the actor-based model for robustness, but also limitations in debugging and understanding complex systems
• Discussion of Erlang and its implementation in large systems
• Comparison of Erlang with other languages and frameworks
• Description of Erlang's process model and message passing
• Emergent behaviour in Erlang systems
• Discussion of the challenges and limitations of Erlang
• Critique of RabbitMQ and its reliability
• Discussion of the tension between emergent behaviour and system reliability
• The speaker is experiencing a production outage and trying to debug it
• Async/await is discussed, with the speaker comparing it to a stack frame-based approach
• The speaker explains that Big's philosophy is to make things explicit and give the programmer control
• Async/await in Big is implemented using stack frames and coroutines
• Debuggability is a design centre for Big, aiming to make it easier to understand what's happening
• A tangent is made about introducing async to inexperienced programmers, specifically a son of one of the speakers
• Discussion of teaching programming concepts, particularly asynchronous programming
• Introduction to Twisted Python, an asynchronous framework for Python
• Experience with Twisted and Node.js, including issues with emergent behaviour and accidental blocking
• Sharing of personal anecdotes about writing servers, including a project using the shout cast protocol
• Discussion of community-based internet radio stations and the development of custom servers
• Discussion on asynchronous operations and their benefits
• The speaker's introduction to async was through a project with long latency events
• Difficulty in explaining the concept of async and its importance
• Comparison of the speaker's initial multithreaded implementation to their later async implementation
• Challenges with blocking write miscalls and concurrent connections
• Introduction to the async core module in Python's standard library as a motivating example
• Brief overview of other topics, including RabbitMQ and Twisted
• Discussion of the HHVM (Hip-Hop Virtual Machine) project and its approach to concurrency
• Comparison of Node.js and Golang in terms of concurrency handling
• Explanation of the event loop starvation problem in Node.js
• Discussion of the async/await feature and its limitations
• Mention of the HHVM documentation and its visual approach to explaining concurrency
• Comparison of different concurrency models, including Asunción, G-unicorn, and Trolleys
• Explanation of the Trolleys project and its use of exception handling for concurrency
• Personal anecdote about building a production system using Trolleys
• Comparison of Trolleys with other concurrency models and hacks
• Core event loop with exception handling and state machine iteration
• Reusing mechanisms for different purposes without proper abstraction
• Experience with a private Docker registry called Quay (now known as Quay.io)
• Build manager system that orchestrated building Docker files
• Distributed process running on every node, talking to SCD to maintain state
• Asynchronous state management and debugging challenges
• Event loop with multiple co-routines, including the current and previous three
• Difficulty in debugging stack traces due to complex system state
• Abstractions have improved over time, making it easier to build systems today
• Better tools and languages available today (Rust, Big, Go)
• Asynchronous systems and their limitations
• Debugging and visibility into queuing delays
• Comparison to Postgres replication issues
• Overview of asynchronous systems and their purpose
• Experience-based understanding of asynchronous programming
• Strategies for working around blocking issues in asynchronous systems
• Discussion of poll and event ports as useful models for async interfaces
• Introduction of IOU ring, an alternate miscall layer that allows shared memory between kernel and user space
• Explanation of async futures and promises and the developer's initial struggle to understand them
• Different views on concurrency and async, with one developer seeing it as "getting out of the kernel's way" and another seeing it as "cooperative threading"
• History of Python's async support, including Stackless Python and the development of Vent let and G event
• Teaching async as a counter to threading and presenting it as cooperative threading
• Intergalactic warfare and concurrency mechanisms
• Twisted framework and its origins in a multiplayer game project
• Async versus threads discussion and its influence on the author's decisions
• Teasing the book "Losing the Signal" and its author's upcoming appearance
• Discussion of the book's themes and potential for a major motion picture
• Preview of upcoming conversation with Sean Slough
• Farewell and closing remarks