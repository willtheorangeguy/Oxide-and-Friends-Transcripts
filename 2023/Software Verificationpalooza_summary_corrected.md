• Lollapalooza and its evolution as a music festival
• Discussion of the Paloma suffix and its potential applications (Paloma Gate, Gate Paloma, etc.)
• Comparison of validation vs. verification and their implications
• Introduction to software verification and model checking using TLA+
• Live migration of instances in a system, including orchestration and distributed systems problems
• Designing a live migration procedure and the importance of design documentation and review
• The importance of prototyping versus thorough design and planning before coding
• The use of distributed sagas to ensure reliability in complex systems
• The challenges of concurrent operations in complex systems
• The need for formal methods, such as TLA+ (Temporal Logic of Actions), to reason about and verify complex systems
• The speaker's personal experience with TLA+ and formal methods, including their introduction to the topic in 2010-2011 while working on the Windows kernel team
• The speaker shares their experience with a bug in a Windows system that caused a critical section to be abandoned, and how it was eventually fixed with the help of a model checker in TLA+.
• The model checker was able to identify the bug and verify a solution to it in a fraction of the time it took the team to identify the issue manually.
• The speaker discusses their philosophy of using tools like TLA+ to avoid making mistakes in system design and to get extra assurance that the system will behave as intended.
• The speaker explains what TLA+ is and how it is used to create models of systems, including the use of set theory and formal logic to generate execution traces of a system's behaviour.
• The speaker describes how a model in TLA+ is a logical predicate that specifies the allowed states and transitions of a system, and how it can be used to express invariants that must hold over the variables in the system.
• Discussing the use of model checking to identify potential issues in a system
• Identifying the difference between a bug in the model and a bug in the program
• Describing the process of refining a model through iterative checks and corrections
• Highlighting the value of rapid iteration and feedback from model checkers in design and development
• Discussing the challenges of translating formal specifications into executable code
• Emphasizing the difficulty of identifying subtle issues through manual testing and code review
• Mentioning the example of a specific bug that was identified through model checking and its implications for system design and testing.
• Discussing the challenges of debugging rare bugs and the importance of using model checking to reproduce and understand the behaviour of complex systems.
• Introducing the Plus Cal language and its benefits for modelling and model checking, especially for procedurally oriented code and state machines.
• Sharing personal experiences with using Plus Cal to model and reproduce a bug in an existing system.
• Highlighting the value of practice and hands-on experience in learning to use model checking and modelling tools.
• Discussing the importance of being able to reproduce a known bug using a model to ensure that the model is accurate and useful.
• The use of a model checker to identify and verify a bug in a system
• Breaking the system into phases to prevent duplicate instance startup
• Benefits of pre-existing bugs being discovered during testing
• Use of models alongside software to document system behaviour
• Challenges of working with large models (700+ lines)
• Introduction to property-based testing and its potential applications
• Discussion of model-based reasoning and its limitations (e.g. concurrency)
• Overview of property-based testing, a testing approach that generates random test cases to ensure code correctness
• Historical context: property-based testing originated in Haskell in the 1990s, with the original library being Quick Check
• Comparison of property-based testing libraries, with Quick Check considered outdated and Protest (in Rust) and Hypothesis (in Python) considered modern and more effective
• Explanation of shrinking, a feature in modern property-based testing libraries that helps debug test failures by gradually reducing the size of the input until the smallest failing input is found
• Code example using Protest in Rust to demonstrate property-based testing for a sort function
• Discussion of the general pattern of testing against a preexisting "model" or "oracle" to ensure code correctness, particularly when comparing new code to existing, known implementations.
• Property-based testing can be used to verify the correctness of complex data structures and algorithms by comparing them against an "oracle" implementation.
• The oracle implementation can be a standard library function or another implementation that is known to be correct.
• Property-based testing can help catch bugs that are difficult to identify through other testing methods.
• The example of a "buff list" data structure was used to demonstrate the power of property-based testing in finding bugs.
• A "buff list" is a data structure that represents a segmented list of bytes chunks, and it is particularly useful for working with large amounts of data.
• Property-based testing can be used to generate random inputs and test the behaviour of the data structure against the oracle implementation.
• The property-based testing framework used in the example generates random values using "strategies" that combine value generation and shrinking (reducing the size of the input).
• The example found 6 separate bugs in the "buff list" implementation.
• Differences between property-based testing (Protest) and Quick Check
• Relationship between property-based testing and fuzzing
• Use of property-based testing to generate random inputs for fuzzing
• Complementarity of property-based testing, fuzzing, and formal modelling (e.g. TLA+)
• Importance of verifying production code in addition to design models
• Use of oracles (e.g. Cargo) to test implementation correctness
• Challenges of testing complex systems and edge cases
• Trade-offs between property-based testing, fuzzing, and formal modelling
• Discussion of Cargo and its use in validating disease models
• Intersection point between different data structures and models
• Challenges in dynamic systems with transaction sizing and throttling behaviour
• Use of formal methods and property-based testing for optimization and eliminating queuing delays
• Prop testing as a tool for checking models and its limitations
• Use cases for property-based testing, including serializes and deserializes
• Round tripping in JSON schema universe
• Using formalisms for rigorous approaches in software development
• Properties of formalisms (e.g. TLA+, Protest)
• Applications of formalisms (e.g. concurrency, verification)
• Adoption of formalisms in hyperscalers (e.g. Microsoft, Facebook)
• Experience with formalisms (e.g. difficulties, benefits)
• Future potential and opportunities for using formalisms
• Discussion of future episode topics
• Revisiting the topic of async
• Invitation for Rain to return for a future episode
• Joking reference to an "async therapy session"