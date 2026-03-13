• Discussion of words not to be said
• Revisiting a previous episode and its topic
• Criticism of Nate Silber's list of top technologies
• Issue with reductive thinking and simplicity
• Importance of understanding complexity and nuance in technology
• Comparison of technologists' approach to making technology user-friendly vs. simplifying it too much
• Analysis of Amazon's S3 service as a complex example of simplicity
• Discussion of the complexity of storing and retrieving digital data
• Storage is a key component of the rack infrastructure
• Hyperconverged infrastructure is not well understood and has a "goopy" term
• Converged infrastructure is a previous term used to describe combining different storage protocols
• Hyperconverged infrastructure is when compute and data are co-resident on the same infrastructure
• Hyperconverged infrastructure is often associated with a fixed ratio of components
• The term HCI is an abbreviation for Hyperconverged Infrastructure, not Human Computer Interface
• Discussion about fiber channel and its perceived "steampunk" quality
• Concerns about relying on third-party storage and vendor lock-in
• Experience with Delphix and its software virtual appliance for storage
• Problems with storage products, including checksum errors and vendor unwillingness to accept evidence
• Analogy to Stockholm syndrome in dealing with storage issues
• Experiences with building and shipping storage products, including ZFS and its reliability concerns
• Importance of having storage in the box for private cloud infrastructure
• Constraints on building reliable storage, including data corruption and data loss
• Challenges in preventing data vacations and data corruption in storage systems
• Observations on the difficulty of building reliable storage, including the impact of a single bad disc on system latency
• Visceral learning from using ZFS in production at Joyent, including the impact of OS bugs on data corruption
• Importance of constraints in designing storage systems, including doing as little as possible
• Discussion of starting a new storage service from a "clean sheet of paper"
• Limitations of ZFS and the need for a new design basis
• Consideration of alternative storage solutions, including Ceph
• Evaluation of Ceph's requirements for operators and staff
• Decision to prioritize autonomy and simplicity in the new design
• Comparison of Ceph's journey and the need for a robust and reliable solution
• Conclusion that Ceph is not a fit for the new storage service and a decision to build a simpler and more robust solution.
• Discussion of past meeting about VMs on the rack in 2020, during the pandemic
• Review of possible architectures considered, including ZFS and distributed storage layer
• Mention of Delphix's work along similar lines
• Discussion of "mux" approach, where ZFS would be on distributed nodes managing SSDs
• Explanation of Southern Volume Manager and Northern MUX approaches
• Comparison of the two approaches and their differences in architecture
• Different architectures for storage considered
• Prototyping and simulation to inform decisions
• Nominal prototype of discs underneath ZFS
• Concerns about iSCSI and network storage
• Failure modes and new issues introduced by network storage
• Need for block semantics, not file semantics
• Simulator for proposed storage format and protocol
• Alternative approach with simpler, non-redundant ZFS pools
• Replication and mirroring to ensure reliability
• Decision to keep storage simple and not use complex erasure coding or RAID
• Importance of reliability and durability
• Three replicas to ensure availability and durability
• Network storage is a problem that the company had to overcome to implement live migration.
• The team viewed network storage as a constraint on their work and spent four years trying to make it work.
• The absence of live migration was a significant pain point that led to issues with rebooting compute nodes.
• Live migration requires network storage to be a first-class operation.
• The team used a simulator to test and refine their approach to network storage and live migration.
• The simulator helped to identify and address issues with ordering constraints, dependency ordering, and threading through the protocol.
• The team had to balance parallel processing with crash safety and ensure that each replica transitions through the same series of visible states.
• The simulator was used to square the promises made by disks with the implementation of a protocol on the backend.
• The team made simplifying assumptions, including having only one client, to simplify the problem.
• The nomenclature for the system was changed from "north" to "south" and from "upstairs" to "downstairs".
• The team's focus shifted to implementing the system with additional personnel being added to the team.
• Discussion of a startup and its understaffing before the pandemic
• Adam's mention of the long pole being storage and taking notes
• Joining of Alan in April 2021 and his background in storage at Sun, ThreePar, and DSSD
• Alan's experience and skills in storage and Rust programming
• The early days of the Oxide project and the formation of Crucible
• Implementing the lowest layers of Crucible and working with Josh and Adam's ideas
• Early milestones and the need for additional team members
• The origin of the name "Crucible" and its adoption in a short period of time
• Discussion of initial worries and excitement about starting work with Rust
• Comparison of working with Rust versus C, with Rust enabling faster progress
• Mention of hiring James for the storage team and his involvement with Crucible
• Early memories of working with Crucible, including interacting with low-level Rust code
• Discussion of demos and seeing the project come to life
• Joking about pet food names being used for data centers and the humor in it
• Closing with a mention of a diagram and using it as a background for a presentation
• Discussion about a system setup in a furnace room, including a mention of "the four machines named after dog food"
• Comparison of a setup in a bathtub and a professional setup
• Praise for James' approach to development and his contribution to the team
• Mention of the importance of collaboration and working through problems together
• Discussion of the RFD (Request For Development) document and its implementation details
• Reflection on the team's progress and the value of James' contribution to the team's speed and efficiency.
• Challenges of developing a system with intermittent power loss and errors
• Difficulty of testing complex systems with multiple failure modes
• Use of Rust programming language to write unit tests and make code more reliable
• Benefits of refactoring and updating the implementation in a Rust-based system
• Designing and implementing testing tools for simulating different failure modes
• Creating a control system to shut down and recover different parts of the system
• Building a fake front end to test specific sequences of events and replay scenarios
• The speaker discusses the importance of automating certain tasks in a system, allowing for easier maintenance and improvement.
• The system uses a combination of testing approaches, including unit tests and integration tests, with tools like CRUD and Tokyo tests.
• The speaker emphasizes the importance of testing and the need for a robust testing framework.
• The organization measures progress in terms of lines of code written per week, but the speaker notes that this metric can lead to perverse incentives.
• The speaker suggests that mass (i.e. the amount of code written) is a more important measure of a software system's quality.
• The conversation turns to optimizing the system's performance, particularly in terms of IO, with the speaker noting that there is no end to performance improvements.
• Discussion of the importance of having a comprehensive test suite for making radical changes to a system and increasing its speed
• Description of the author's background and how they joined the Crucible team to focus on improving performance
• Explanation of how the team replaced SQLite with a raw file approach for storing metadata, resulting in a 30% speed up for small writes
• Discussion of the challenges of using authenticated encryption, including the need to store additional metadata and ensure atomic updates
• Acknowledgement of the initial use of SQLite to manage metadata, which provided a speed boost but had limitations
• Reflection on the complexity added by encryption and the need for a more efficient approach
• Testing two versions of the system, one using raw files and the other using SQLite
• Ditching SQLite for simplicity, despite its robustness and ease of use
• Refactoring the system to improve performance, including RFD 444 which changed data ownership and RFD 445 which improved parallelism
• Removing unnecessary mutexes and improving confidence in the system's safety
• Focusing on correctness over performance in the initial design, with plans to optimize later
• Refactoring code to improve performance and reduce memory scans
• Comparison to ZFS development and performance improvements
• Discussion of snapshot deletion and its impact on system performance
• Challenges of refactoring in CFS and advantages of Crucible
• Importance of deliberate back pressure in distributed systems
• God's own back pressure vs. designed back pressure
• Data vacation and its effects on system availability
• Designing explicit back pressure in systems
• Designing a system to prevent infinite buffering of write data
• Analogy to ZFS write throttle and its solution to cache limitations
• Implementing a quadratic equation to delay writes and maintain a steady state
• Addressing the problem of pathological cases where the upstairs buffers infinitely much write data
• Discussing the concept of "back pressure" and its importance in system performance
• Comparing the need to throttle work to metering lights in traffic and the need to stop traffic to allow the aggregate system to move faster
• Challenges in implementing a cloud storage system
• Balancing implementation artifacts with core functionality
• Importance of reliability, encryption, and consistent ordering of I/O operations
• Development of snapshot functionality and its significance
• Refactoring efforts and their impact on system development
• Design and implementation of the volume layer and its benefits
• Propolis and its role in NVMe device emulation and communication with the upstairs and downstairs systems
• Support for booting from images, snapshots, and elastic properties like disk growth at runtime
• Layering problem in disk storage and snapshotting
• Introducing the concept of a "block I.O. trait" in Rust
• Volume hierarchy and implementing block I.O. for volumes
• Solving the layering problem using the volume object and read-only parents
• Using ZFS for snapshotting and leveraging its guarantees
• Design decisions behind using a Zpool on multiple SSDs
• Copy-on-write snapshotting features
• Leveraging ZFS snapshots to solve problems
• Using snapshotting mechanism to improve data management
• Growing and re-encrypting disks
• Importing read-only parents into subvolumes
• Performing scrubs with Propolis
• Dropping read-only parents and accessing subvolumes directly
• Upgrading Crucible and upgrading to V2
• Shadow migration feature from Fishworks appliance
• Hierarchical storage management and rekeying/migrating data format
• Using snapshotting to avoid downtime and upgrade software
• Discussion of a notable demo that impressed the speakers
• Reference to NFTs in the demo
• The "but wait, there's more" phenomenon in demos, where unexpected features or capabilities are discovered
• The difficulty of distinguishing between deliberate features and unexpected bugs in demos
• A specific demo where the speakers used Minecraft on the oxide rack
• The speakers' experiences and impressions of the demo, including the feeling of "bottling up" a successful experience for future reference
• A discussion about a technical detail in the demo, specifically the difference between "read only parent colon arc guest" and "dyn block IO"
• The importance of recognizing and building on positive momentum in software development
• ZFS snapshots and writable snapshots as a key feature of cloud-based infrastructure
• Challenges with live repair and ensuring consistency with other disks
• Importance of reliable storage and data integrity in distributed systems
• Open-sourcing of code as a matter of convenience or for other reasons
• Collaboration and shared responsibility among team members for project success
• Recognition of the complexity and interdependence of various system components
• Propolis and its dependencies, including the decision to open source Crucible
• The process of opening up private components to public access
• The ease of using Git dependencies and the benefits of containerization
• Performance improvements and the refactor that made it easier to add people to the source space
• Future work and the foundation built by the current project
• Storage and the ongoing need to address new customer requirements and workloads
• Discussion of work and accomplishments
• Importance of hiring and team composition
• Benefits of having a diverse team with different backgrounds and expertise
• Use of Rust programming language and its impact on the project
• Reflection on the team's success and lessons learned
• Plans for future episodes and discussions
• Goodbyes repeated over 12-second period
• Total of 19 instances of "Bye" mentioned