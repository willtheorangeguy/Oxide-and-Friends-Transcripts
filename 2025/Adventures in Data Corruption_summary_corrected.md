• The hosts, Adam and Bryan, discuss how the average age of Discord users seems to be getting younger, making them feel out of place.
• Bryan shares his concern that the updates on Discord are too youth-oriented and confusing, leading to feelings of discomfort.
• The hosts joke about being "accidentally lingering by a tent of 15-year-olds" and feeling out of place in a space dominated by younger users.
• They mention that Discord is making money off of them, despite not being the target demographic.
• The conversation shifts to a previously discussed topic, a potential microprocessor vulnerability, which they were concerned about two years ago.
• They share their experience of trying to disclose the vulnerability to AMD, but being rebuffed.
• Bryan finally decides to do a podcast episode on the topic after two years of discussion.
• The hosts discuss how the manifestations of the underlying issue are far removed from the root cause, making it surprising and unexpected.
• UPDATE sled recovery process involves uploading a TURF repository (a zip file) containing software updates to a functional sled
• The process assumes the target sled is unable to boot or communicate with its service processor
• The functional sled (driving the process) uses Wicket to unpack the zip file and provide the recovery image to the target sled
• The target sled is sent a stripped-down recovery image over the management network, which boots and runs Installinator
• Installinator asks the service processor for the hashes of the real OS image and control plane software, then finds peers on the Bootstrap network to retrieve the images
• The process takes about 15 minutes to complete the initial recovery, with the remaining steps taking only seconds
• Discussion of a sled recovery process in five minutes
• Issue of corrupted OS image on sleds after software update
• Importance of f syncing drives and flushing disk caches
• Adding extra logging and checks to detect corruption in the future
• Importance of not assuming a problem is fixed and instead seeking more information
• Company culture of investigating and addressing issues, rather than letting them go.
• Concerns about data corruption in the system
• Discussion of the checks added to the code to prevent data corruption
• Explanation of the process of downloading an OS image from Wicket
• Mention of the possibility of data corruption in the Wicket repository
• Discussion of the failure modes and how the team is thinking about them
• Mention of the "data corruption week" and how it was handled
• Explanation of the two checks added to the code and which one failed first
• Discussion of the potential sources of data corruption, including user land and the CFS path
• Mention of the instrumentation added to Tokyo to rule out Tokyo as a source of data corruption
• Separating Installinator from its environment to make it reproducible
• Creating an independent binary for Installinator
• Reproducing the issue by running Installinator on a separate host
• Identifying the issue as a nondeterministic problem with a 10-15% failure rate
• Modifying the code to check for zeros in the binary
• Determining that the zeros were not in the actual artifact, but in the fetched data
• Tweaking Tokyo source code to panic when zeros are detected
• Realizing that the software between the wire and Installinator was the culprit
• Implementing a panic condition when a run of zeros is detected
• Observing the printing printing the correct non-corrupted data, leading to confusion and realization of the bug's nature.
• Data corruption issues with ePrintLAN
• Discussion of trying to debug the issue using Trace and other tools
• Observations of cache corruption and CPU structure issues
• Experimentation with moving the process to different CPUs to try to isolate the problem
• Reflection on the unconventional and unpredictable nature of the bug
• Discussion of the concept of "psychotic" bugs that break the abstractions of the operating system
• Discussion of a mysterious bug that causes unpredictable and bizarre data corruption
• Initial hypotheses of a virtual memory bug, but inability to describe or explain the behaviour
• Realization that the bug's symptoms are unlike any other known issue, including data corruption and unexpected oscillation between correct and incorrect data
• Exploration of page aliasing as a possible cause, but its inability to explain the bug's behaviour
• Discussion of the possibility of a virtually indexed physically tagged cache causing aliases and data corruption
• Reproducibility of the bug on different CPUs and its continued manifestation after moving processes between CPUs
• Frustration and surprise at the bug's strange behaviour and reproducibility
• Consideration of various theories, including KPI and trace me involvement.
• Discussion of tracing memory (trace me) and its limitations
• Bryan Can trill's intentional introduction of a "flickering" effect in trace me
• Concerns about the possibility of a user-land bug versus a hardware issue
• Reproduction of the issue on specific CPUs and not on others
• Isolation of the issue to a single system and not on other platforms (Linux, macOS)
• Hypothesis about a potential memory corruption issue
• Discussion of the operating system's sensitivity to memory corruption
• Recollection of a previous experiment corrupting memory and the system's behaviour
• The team's continued confusion and uncertainty about the issue
• Review of the next day's efforts and the introduction of new team members
• Discussion about a mysterious VM bug and its possible meaning
• Reference to astrology and virtual addresses
• Introduction of the concept of a "haunted VA region"
• Explanation of how debugging is scalable and remote work-friendly
• Explanation of how the team uses recordings to collaborate and avoid "backseat driving"
• Discussion of a workaround for the haunted VA region using a "balloon" technique
• Mention of a commit that allocated a large vector to bypass the haunted VA region
• Discussion of the term "balloon" and its origins in VMware
• Reference to a similar bug, Richmond 16, and its possible connection to the haunted VA region
• Discussion of a bug in the "haunted VA region" and the process of identifying and debugging the issue
• Reference to the TV show Scooby-Doo as a cultural phenomenon and a metaphor for the decline of critical thinking and science education
• Explanation of a specific technical problem with a kernel mapping and the process of using Trace to diagnose the issue
• Mention of other related bugs and issues, including the "Richmond 16" and "OS 1028" bugs
• Reflection on the process of debugging and the importance of finding the root cause of a problem rather than just treating symptoms.
• Trace gives explicit errors for soft errors rather than crashing the process
• Trace allows tracing memory, even with incorrect addresses, without panicking the system
• Soft errors cause processes to have a "haunted" virtual address region, where data is sometimes valid and sometimes corrupted
• Corruption occurs due to storing to a specific virtual address, which is not reallocated and can be accessed by other processes
• The problem is connected to speculative execution and page table isolation
• Kernel page table isolation (KPI) was implemented to prevent attacks like Meltdown, which allowed CPUs to execute speculatively based on addresses that weren't allowed to be read
• The "stowaway mapping" is in a different c r three than the user and kernel user c r three, and is accessible only for a brief period when the processor is executing speculatively.
• TLB (translation look aside buffer) loading issues causing flickering
• TLB shoot down not working correctly, allowing speculative execution
• Pathological bug from 1999 with similar symptoms
• Explanation of TLB and its importance in caching virtual to physical address translations
• Discussion of speculative execution and its benefits and drawbacks
• Reference to Spark and its performance issues, with joking comments about its slowness
• Intel was criticized for the way their operating system handles shoot down with the mapping dial
• A bug in the Spark architecture manual was mentioned, which caused data corruption and was eventually found by an engineer at SMCC
• The conversation turned to a specific bug related to speculation and its impact on the operating system
• The bug was eventually reproduced on various CPUs, including Milan, Gimlet, and Genoa
• The conversation centred around whether the bug could be abused to undermine KPI (Kernel Page Table Isolation)
• AMD's response to the bug was mentioned, with their answer being that it's not a problem
• Discussion about a kernel issue caused by a specific virtual address range
• Reluctance to discuss the issue due to AMD's involvement
• Comparison of the issue to historical fiction, specifically "The Man in the High Castle"
• Explanation of how the issue would have been difficult to debug without the use of parallelization
• Discussion of the importance of quickly addressing the issue and the lessons learned from the debugging process
• Acknowledgement of the role of group debugging sessions in resolving the issue during the pandemic
• Mention of a developer taking a half-measure to mitigate the issue, which proved to be effective
• Discussion of a recent debugging experience and the process of identifying a bug in the operating system
• Identification of a stowaway mapping as the root cause of the issue
• Importance of a solid foundation and robust code in preventing issues like this
• Comparison of debugging in Rust versus C and the benefits of Rust's safer programming model
• The need to invest time and resources in debugging and resolving issues like this to prevent future problems
• Conclusion that building systems with a solid foundation from the beginning is crucial to preventing issues like this
• Discussion of a system vulnerability or "stowaway" in the kernel
• The vulnerability's impact and how it was fixed
• Reflection on the process of working on and fixing the issue
• The role of team members, including John, Rain, and Keith
• A mention of a future guest, Morris Chang, and potential future episodes