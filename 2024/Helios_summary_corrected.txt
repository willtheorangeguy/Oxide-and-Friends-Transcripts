• Discussion of a Michael Jagger reference and its unexpectedness
• Generational references and the desire to appeal across generations
• Mistakenly placing ads on the wrong podcast
• Referring to one of the hosts as "Mick" and the ensuing confusion
• A request to draw a picture of Keith Richards
• Meta conversation about the podcast's meta references
• Introduction of a new guest, Nick, and discussion of audio quality
• Discussion of a podcast opening sequence and its historical significance
• Review of the book "High Noon" and its connection to the early history of Sun
• Discussion of the Unix wars and the AT&T deal
• Proposal to regift a book as a gift to one of the hosts
• Discussion about ordering books from the library
• The conversation turns to Helios, a project that was unexpectedly featured on Hacker News
• Explanation of Helios as a distribution of Lumps, similar to Ubuntu being a distribution of Linux
• Clarification of the relationship between Helios and Lumps, and the concept of distributions
• Discussion of the engineering complexity involved in creating a distribution, particularly with Linux
• Explanation of the integration of system libraries and commands in Lumps and Helios
• Building a custom operating system from existing components
• External dependencies and packages required for the OS
• History and evolution of the OS, including influences from Open Indiana and Amnios
• Challenges of building a custom OS, including bootstrapping and dependency management
• Roster support and crate maintenance
• Community engagement and contribution challenges
• Challenges with maintaining and interacting with certain Rust crates
• Friendly and receptive community, but with some busy or unresponsive maintainers
• Abstraction and cross-compilation capabilities of Rust
• Tier 2 support in Rust project and its implications
• Comparison of Rust to other languages (Go) and its ecosystem
• Development of hermetic, offline build process for Oxide
• Building and producing different types of images (ISO, disk images, RAM disk images)
• Ditching UEFI firmware in a server and using a custom approach
• Custom boot process for the Helios operating system
• Using a small bootloader written in Rust to load the Illumes kernel
• Implementing a read-only ZFS file system to locate the kernel and boot archive
• Addressing the "chicken and egg" problem of accessing the disk to load the RAM disk image
• Initializing PCI and other hardware components just once in NOR flash to avoid reversible operations
• Implementing a custom initialization approach to avoid the complexities of traditional UEFI initialization
• The CPI archive is a cache of files in the NOR flash, containing a subset of files also in the pool, to load before accessing the pool.
• The CPI archive is compressed to fit within the 8 megabyte limit of the NOR flash.
• Kernel modules are bifurcated, with some required for booting and others not, to optimize the CPI archive size.
• The CPI archive is generated at build time, similar to what would be generated on reboot after a software update.
• Helios is designed to run on commodity hardware, including non-oxide hardware, to allow for running on data centre servers or manufacturing stations.
• The team prioritizes thriftiness in hardware choices, including using commodity machines instead of specialized hardware when possible.
• Dell OptiPlex computers, specifically the 700–900 series from 2014-2015, were obtained for $100 each.
• Some of the computers had outdated firmware, but this was later resolved.
• The computers were acquired from an aggregator in Arizona and were not stolen.
• The acquisition of the computers was expensive due to their quantity.
• A 3x4 monitor was selected for use with the computers.
• The computers were used for Helios, a project to create a future-proof hardware platform.
• The speakers discussed the importance of consuming past hardware to create a sustainable future.
• They also discussed the challenges of working with BMC and UEFI.
• The speakers mentioned a desire to create a computer company and to standardize packaging and distribution of software.
• They discussed the benefits of having a central packaging repository and using additive and subtractive packaging steps.
• The speakers highlighted the importance of having consistent binaries across different hardware platforms.
• Packaging system IPS (Image Packaging System) was used in OpenSolaris and Polaris 11
• IPS was a reaction to the complexity of traditional packaging systems like RPM and Yum
• IPS introduced declarative actions to replace post-install scripts, which were prone to errors
• IPS allowed for more flexibility and safety in updating systems, including creating clones and reboots
• IPS was used as a build time step to assemble the RAM disk in the product system, providing a consistent and immutable environment
• Discussion of Helios and Oxide Rack implementation details
• Clarification that Helios is not user-facing and is an implementation detail
• Use of open source to allow for replication and flexibility
• Mention of Oxide supporting manufacturing stations and build servers
• Description of a unique clock setup in the office using a Helios-powered terminal
• Comparison of Helios to Amnios LTS and recommendation to use Amnios LTS for critical applications
• Importance of upstreaming code and avoiding accretion of changes
• Discussion of the benefits of upstreaming code, including staying current with the upstream fork
• Balancing act of prioritizing software updates and testing
• Pain of being broken by upstream changes and losing services
• Importance of testing and reviewing changes before merging
• The "Quality Death Spiral" and its avoidance through continuous improvement
• Challenges of managing downstream forks and merging upstream changes
• Need to test and debug changes as soon as possible after merging
• Importance of merging upstream changes regularly to prevent downstream issues
• St. Louis is a new architecture in the Lumps branch of Oxide, aimed at reducing the complexity of the codebase
• The St. Louis architecture is a separate entity from the ISA and machine architecture, with a focus on creating a single codebase that can be used by everyone
• The development process for St. Louis involves pushing code to a public repository on GitHub, allowing for collaboration and upstreaming
• Oxide is creating a new architecture that is separate from the traditional 86 PC architecture, allowing for multiple architectures to coexist and share common code
• The team is working to contribute to upstream Lumps and make it easier for others to contribute, with a focus on documentation and discoverability
• Documentation and contribution processes have been revamped, with links to the Lumps documentation repository and contributing guidelines available on the front page of lumos.org.
• Book recommendations for debugging memory corruption and device drivers
• Challenges with searching for "Lumps" due to Google's algorithm and synonym issues
• Recommended search strategies for finding accurate information on Lumps
• Perplexity.ai as a reliable source for Lumps-related information
• Experience with debugging a performance issue related to unable values and memory
• Discussion of the importance of updating unable values to match physical system attributes
• Discussing the concept of a "bonkers amount" of physical memory as a threshold for concern
• Comparing ancient computer memory sizes (14 megabytes) to modern terabytes
• The concept of "guest memory" and reserving memory for the operating system kernel
• The "asbestos" and "bees" analogy for describing complex system behaviour
• The adaptive replacement cache and its sensitivity to free memory thresholds
• Criticism of the use of thresholds as a proxy measurement
• The importance of measuring the rate of page out rather than physical memory usage
• The concept of "bang bang control" and its limitations in system management
• Discussion of the limitations of old operating systems, specifically 16 megabyte systems with 20 megahertz processors
• Reference to the "text of the sun bug" and its significance in the history of the system
• Mention of the importance of preserving historical evidence for future historians and engineers
• Discussion of the Helios repository and its value in open source development
• Comparison of the Helios system to other operating systems, such as Linux and FreeBSD
• Reference to the porting of Cockroach and Click House databases to the Helios OS
• Discussion of the importance of derisking and early porting of critical software
• Mention of the work done on getting Rust and Go working well on the Helios OS
• Discussion of the thousands of dimensions involved in selecting an operating system and the trade-offs that come with it
• Discussing the status of open source policy RFD and RFP 26
• Reflection on experiences, including a negative experience with Samsung
• Review of past decisions, including database and operating system choices
• Importance of understanding values and overlaps between project values and community values
• Positive experience with Rust and other open source projects
• Discussing the importance of explaining one's choice of tools or technologies, and the potential for people to feel defensive or insulted by certain language or assumptions.
• The example of SCO Open Server and its complex technical properties, and the idea that "open" can mean different things in different contexts.
• The history of operating systems and the evolution of openness, including the API being open even if the overall system is not.
• The appreciation for minority operating systems, such as Haiku, that have survived against the odds.
• The importance of making big decisions and considering multiple factors, including technical properties, and avoiding bias.
• Joking about the lack of 4-letter acronyms in certain discussions.
• Discussion of a 4-letter acronym "You"
• Jokes about old hardware and the concept of retro-hardware being resold on eBay
• Reference to the Helios project and its open-source nature
• Mention of a future episode discussing Crucible and the storage service
• Discussion of a potential future episode on Propel las with a guest
• Lighthearted banter and jokes throughout the conversation