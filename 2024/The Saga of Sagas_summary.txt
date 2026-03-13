• Discussion about the hosts' youth and nostalgia for the Mickey Mouse Club
• Talk about a proposed topic or project and its history on the hosts' list
• Joking about the concept of "Leventhaling" (being right after previously being wrong)
• Introduction of Lure from Futurama, a reference to the TV show
• Explanation of the name "Omicron" and its Futurama origins
• Discussion about the Omicron repository and its name
• Mention of the COVID-19 variant Omicron, but clarification that it's not about that
• Reference to a journal club with Katie McCaffrey and a discussion about reading and listening to previous episodes
• Humor about mispronunciation of "Omicron" and other technical terms
• Challenges of evaluating outside work and adopting a "shrink to fit" model for journal clubs
• Discussion of Katie McCaffrey's work on distributed sagas and its impact on the team's understanding of transactionality in distributed systems
• Adam Leventhal's origin story of introducing the concept of distributed sagas to the team
• Dave Pacheco's first explorations of workflows and sagas, including the concept of sagas and their application to complex operations
• The VM provisioning example and its use as a case study for the challenges of coordination and error handling in distributed systems
• The team's experience with ad hoc code and the desire to find a more elegant solution using sagas
• Discussion of workflow engines and their limitations
• Conway's law and its relevance to workflow engines
• Investigation of various workflow engines, some of which were fictional
• Conclusion that a custom solution was necessary
• Review of past discussions, including RFP 107 and its prescience
• Investigation of sagas, a concept used in distributed systems
• Decomposition of complex operations into individual actions with undo actions
• Acyclic graph model for distributed saga
• Steno framework in Rust for executing distributed saga
• Distributed saga rules for convergence
• Saga as a non-atomic database transaction
• Saga pattern for failure handling and undo actions
• Steno's log-based implementation and storage backend
• Nexus component incorporating Steno for saga execution
• Saga vs workflow discussion and definition
• Saga as a pattern for distributed systems inspired by database patterns
• Difficulty in defining and implementing sagas due to their abstract nature
• Idempotence of actions to handle incomplete operations
• Potential for actions to run multiple times, and the need for undo actions to work in these cases
• Challenges in testing sagas, such as inducing failures and unwinding them
• Difference between sagas and workflows, with sagas implying transaction semantics and workflows being a DSL
• Implementing control plane using sagas, and finding wins and challenges
• SCC (Saga Execution Coordinator) failure and failover, and the difficulty in extending the saga model for this
• Sharing state between sagas, and the need for a way to store and retrieve shared data
• Designing a system to manage state between actions in a saga
• Discussing the pros and cons of sharing state between actions
• Introducing the concept of one immutable value produced by each action
• Describing how dependent actions can consume values from previous actions
• Talking about the implementation of actions in Rust and how it affects the saga log
• Discussing the challenges of upgrading and migrating the coordinators due to changes in the actions and their implementation
• Exploring the idea of storing code, such as WASM, with the saga log to handle versioning and upgrades
• Update problem is a challenging issue for a distributed system
• The system's design choice makes it hard to get right and test quickly
• The solution involves quiescing old versions of the software and letting them finish their sagas before removing them
• This approach has an unfortunate downside: you can't fix a bug in a saga in a software update
• The distributed system's constraints make it difficult to solve the update problem, as it's a product that can't have human intervention or batch scripts
• Simplifying assumptions, such as a single value emitted from every action, can help make the system more robust and easier to deliver.
• Discussing the idea of simplifying complex systems
• The concept of sagas and their implementation in Steno
• Challenges in making sagas dynamic and supporting sub-sagas
• The solution to store DAGs in the database and embed sub-sagas
• The benefits of privacy encapsulation and dynamic DAG building
• A discussion on the importance of abstraction in Steno's design
• The team discusses their struggles with code complexity and repetition in the oxide control plane.
• They mention a "saga" system that was created to handle long sequences of actions, but it had issues with maintenance and synchronization.
• A "nexus" component was introduced to handle the complexities of the saga system, but it still had issues with state management.
• Eliza Weisman describes her experience working with the nexus component and the "sled agent" to manage the state of VM instances.
• The team mentions "feral concurrency control" as a previous approach to managing state, but it had its own set of issues.
• They discuss the importance of abstraction and avoiding code repetition in software development.
• Problem with compute instance state updates and server ownership
• Concurrency control issues with live migration
• Complexity of bookkeeping when VMs stop or migrate
• Previous system's flaws in handling updates and state changes
• Introduction of sagas as a solution to these problems
• Sagas' ability to handle distributed locking and state changes
• Eliza's project to implement sagas in the oxide control plane
• Distributed locking controversy among attendees
• Distributed locking concerns: what happens when a process holding a lock dies or takes a long time to release it
• Challenges with distributed locking, including lack of coordinated clocks and network partitions
• Concept of "unwinding" in sagas, which allows for reliable release of locks even in distributed systems
• Terminology debate: "undo" vs. "compensating action" for describing the reversal of actions in a saga
• Implementation of sagas and compensating actions in a distributed system, including instance update saga
• Guarantee of lock release and reduced fear of distributed locking through saga unwinding and compensating actions
• Provision encounters and resource cleanup
• Saga implementation for instance state updates
• Separation of VMM and instance concepts
• Locking mechanism for concurrent updates
• Background tasks and reconcilers for state management
• Moving state out of locks and using compensating actions
• Triggering background tasks for explicit updates
• Moving work out of a lock in a distributed system
• Design of a saga system to handle concurrent state updates
• Feral concurrency control and its application to the saga system
• Optimistic concurrency control and its interaction with saga unwinding
• Introduction of foreign keys as a solution to reduce lock contention
• Use of a gruesome SQL query to handle complex database interactions
• Discussion of the need for garbage collection to reclaim abandoned resources
• Challenges of testing concurrent data structures and ensuring correctness in complex systems
• Use of test helpers and manual testing to identify and fix concurrency-related issues
• Importance of accounting for resources and ensuring consistency in complex systems
• Consequences of neglecting concurrency issues, including resource leaks and system failures
• Use of specialized tools, such as the Omicron stress tool, to simulate and test concurrency scenarios
• The difficulty of creating unit tests for complex concurrency scenarios due to the large number of permutations and possibilities
• Complexities of saga code and the need for careful design
• Problem of concurrent state changes and distributed locking
• Solution of using a second saga to inherit the lock and perform a database compare and swap
• Use of a "trampoline" saga to construct and start a new saga
• Discussion of recording state changes in the database and the potential for changing Steno's logging mechanism
• Mention of a "catch-22" situation with concurrent data structures and the need for careful handling of locks and state changes
• Reference to a "sub saga" in Steno and its use for handling multiple state changes
• Discussion of the need for careful testing, including idempotency tests, to catch bugs in the code
• Trampoline sagas and lock acquisition issues
• Saga vs RPW (reliable persistent workflow) usage and trade-offs
• DNS management and saga/RPW fit
• Nexus system architecture and interaction between sagas and RPWs
• Distributed system complexity and abstraction challenges
• Team's writing-intensive culture and hiring process
• Complexities of provisioning virtual machines (VMs) and dealing with unexpected issues
• The need to update software and manage migration during provisioning
• The importance of addressing fundamental issues rather than just patching bugs
• Eliza Weisman's work on abstracting and simplifying the process, deleting "hacky fixes"
• The difficulty of improving abstraction and making it hard to get it wrong
• The team's experience and learning over the past year and a half
• The integration of Eliza's work and its impact on the oxide rack system
• The team's gratitude and recognition of each other's contributions