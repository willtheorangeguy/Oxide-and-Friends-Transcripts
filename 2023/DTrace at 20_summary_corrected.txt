• Integrating Trace into a project 20 years ago
• Discussing the difference between Detract and Trace
• Bryan and Adam's personal experiences with the project, including their marriage
• Humorous discussion about Hungry Jack's and Burger King in Australia
• Recalling the stress and anxiety of meeting deadlines for the project
• Reflecting on the success and longevity of the software and its continued use
• Bryan Can trill created a fake online profile to scope out potential suitors
• He used the root account on a lab machine to create a fake profile named "Beak root"
• The fake profile received an overwhelming amount of interest, largely due to its tagline
• Bryan's experience with the fake profile led him to realize the need for a better way to understand what software is doing
• He began exploring the idea of dynamically instrumenting program text
• Bryan's interest in this idea was sparked by his OS professor at university, and later reinforced by a conversation with Jeff Bon wick and Barb Smolders at Sun
• He eventually developed Trace, which allows for dynamic tracing of system calls and other low-level activities
• Bryan's experience with Trace was influenced by his earlier work on Polaris and debugging complex performance problems
• Performance issues on large systems (e10k) 
• Use of Lock stat tool for dynamic instrumentation of synchronization primitives 
• Difficulty in understanding system behaviour with limited visibility 
• Large e10k system running SAP benchmark, experiencing prolonged periods of slowness 
• Misconfiguration of system as a router caused the issues 
• Importance of understanding high-level issues through deep symptoms 
• Development of Trace as a solution to these problems 
• Trace's reputation as a solution to system problems before its development
• The importance of focusing on a specific goal, like Trace, rather than just solving the problems it's supposed to solve
• The hype surrounding new technology and the need to separate it from reality
• The development of Trace and its early struggles, including the lack of type information in the kernel
• The Cheetah Plus microprocessor's issues, including a large TLB problem
• The incorrect decision to implement a 16-entry, 2-way associative TLB for large pages
• The consequences of this decision, including thrashing and poor performance
• The need for time and focus to properly implement Trace and other projects
• The connection to the Spark operating system and its struggles with x86 hardware
• Trap stat is integrated into the system, allowing for instrumenting the trap table and measuring TLB miss handler time
• Lint pass 2 was spending 60% of its time filling the TLB due to a large resonance set
• Trace was started in the fall of 2001, after Polaris 9 had shipped
• The foundation laid by previous projects (such as zones and SMF) allowed for a focus on Trace and other new abstractions
• Working from home led to increased focus and productivity, allowing for a "sweet spot" of innovation
• Trace's early work focused on debugging real bugs on the actual system
• The first feature to get working was FBT (function boundary tracing), and everything added to Trace was because it was needed.
• Importance of a crisp provider boundary in system design
• Running a system in production with minimal instrumentation and no penalties
• Constraint of running the operating system on the same hardware as the development team
• Need for safe and non-intrusive instrumentation to debug issues in situ
• Early success with FPT and being able to see system behaviour on a desktop
• Vision and excitement for the potential of Trace
• Presentation to Sun IT and its enthusiastic reception
• Sun IT's naming convention (first initials, last initial, badge ID) and the reaction to it
• Discussion of an early video presentation or project from 2002
• Mention of a DVD containing the video presentation
• Recollection of a project's early development and achievements
• Discussion of anonymous tracing and its importance
• Mention of a bug that was fixed, shaving 8 seconds off of boot time
• Discussion of a project that reimaged the boot process
• Mention of the presentation's limitations in distinguishing between completed and future work
• Discussion of the cultural impact of the presentation in getting people excited about the work
• Mention of Bryan Can trill's fear of death while heli-skiing in 2002
• Discussion of the economic concerns and risks associated with heli-skiing at the time
• A group ski trip where one of the participants had a near-death experience in an avalanche
• Discussion of a device called the Avalon, which was designed to prevent asphyxiation in an avalanche, but was found to be ineffective
• The awkwardness of being the only one in a group taking safety precautions, and the social implications of doing so
• Bryan Can trill's fear of death and his decision to write his last will and testament on a whiteboard in his office
• The humorous reaction of his colleagues to the whiteboard will, and the idea that they might be haunted by his ghost if they don't implement his last wishes
• The lesson learned from the experience that one should work on the things they are passionate about, and not get distracted by other priorities.
• Developing a user-level tracing system, including understanding of machine code and assembly
• Using a 32-bit trap instruction to get into the kernel, move an instruction, and resume in user land
• Creation of the stack project, which pulled out registers through register windows
• Development of the mister Sparkle provider, which included raw instrumentation and identifying probe locations
• Overcoming challenges with jump tables and identifying instructions vs. data
• Instrumenting every instruction in Firefox, including dealing with corner cases such as asynchronous signals
• Discussion of Trace features and their impact on system performance
• Identification of the system in question as being on a SPARC platform, not x86
• Mention of "mister Sparkle" and its presence in the codebase
• Discussion of FBT, FPT, and PID provider support for x86
• Recollection of a "great darkness" for x86 in January 2002 to October 2002, where Trace was nearly killed but later revived
• Discussion of a Git branch called "Fast Trap minus x" and its use in the development of Trace
• Description of a project called "Trace Gate" that allowed projects to sync up with the Trace codebase instead of the operating system
• Mention of several projects (SMF, CFS, and zones) that used the Trace Gate
• Discussion of a successful integration of Trace into the operating system
• Discussion of the date being September 11, 2003, and the significance of the anniversary of 9/11
• Memories of the 9/11 attacks in 2001 and how they affected the world and personal experiences
• Travel plans and flight from Brussels to DC on 9/11/03, and the unusual circumstances of an almost empty plane
• Osama bin Laden's threat to commit a terrorist act on 9/11/03, and the discussion of its potential marketing impact
• The development of a paper on Detract, a technical project, and its submission to the UNIX conference
• The importance of documenting technical work and the benefits of writing it down for posterity
• Trace's early days and open sourcing in 2004
• Importance of blogging and transparency in the development of Trace
• The role of comments and community in Trace's development and adoption
• The transition to open sourcing Trace and its impact on the project
• The importance of making technology available and accessible to others
• Personal anecdotes and reflections on the impact of Trace on users and the development community
• Awards and recognition for Trace, including the Wall Street Journal award
• Discussion about the importance of diabetes and the mention of incapable insulin
• Reference to a past podcast episode on incapable insulin
• Discussion of the development of lock stat and its transition to Trace
• Explanation of USDT (statically defined tracing) and its use in tracing
• Mention of the development of USDT providers, including the Foxtrot provider
• Discussion of the use of Trace with Java and the development of the hotspot provider
• Explanation of JST (Java Stack Tracing) and its role in Trace
• Discussion of the complexity and safety features of Trace
• Explanation of the differences between Trace and other tracing tools, such as EPF and system tap
• Discussion of the importance of safety in Trace and its design principles
• Discussion of the early days of Trace and its adoption at Sun
• Concerns about the potential downsides of Trace, with Bryan Can trill noting that no one worried about it causing system crashes or data corruption
• Incident where Jared Jensen's use of Stack caused system unresponsiveness
• Importance of liveness criteria and preventing systemic unresponsiveness
• Discussion of the post-Sun Trace journey, including the launch of dtrace.com and the first Trace conference
• Bryan Can trill's anecdote about Steven O'Grady's skeptical reaction to the conference and his praise for the technical level of the attendees
• Brief mention of Apple's use of Trace to identify a performance problem
• Fish Pong and Dtrace.com events
• Discussion of past and future events
• Oxide sponsoring of Dtrace.com events
• USDT (User-Space Trace) crate for Rust
• Use of USDT for debugging and performance analysis
• Instrumentation of kernel instructions and non-instruction events
• Use of Trace in conjunction with MDB for postmortem tracing and debugging
• Specific example of a data corruption problem (OS 1028) and how Trace helped solve it
• Discussion of speculative tracing for debugging and performance issues
• Mention of Trace's portability and extensions by various contributors
• Development of Trace and its probe system
• Improving Trace's ability to pick apart JSON strings in the kernel
• Experiences with Oracle's port of Linux and Apple's early adoption issues
• Reuters' insistence on disabling Trace for their application
• IBM meeting where a colleague fell asleep and snored loudly, causing embarrassment
• Trace's attention from other companies, including IBM, and potential partnerships
• Discussion of the SVR 4 vision and its completeness
• Mention of Bryan Can trill's "detract" presentation from 2016
• Gratitude for finding CVEs and vulnerabilities
• Story of Ben Murphy's discovery of the eight integer issues
• Reflection on USDT (Unix Shared Tracing) and its role in enabling statically defined tracing across languages
• Discussion of "is enabled probes" and its significance
• Shared memories of past events and projects, including networking guidance in 2003 and the Shanghai skyline
• Interface stability on probes in Trace
• Library interfaces into Trace for building tools like lock stat
• Stability of swapped out buffers in Trace probes
• PARC (architectural review committee) and its challenges
• Splitting the Trace case into multiple cases to expedite approval
• Using a "shot clock" strategy to run out the approval clock and guarantee approval
• Discussion of a case similar to Erin Brockovich, where they brought in a stack of manuals documenting their work without preapproval
• Use of "bike shedding" questions to distract from important topics and allow team to understand the issue without getting bogged down
• Success in passing the case with minimal discussion, while also addressing issues with provider cases and interface stability
• Gratitude for the impact of anonymous tracing and its continued use and evolution
• Discussion of the team's experience and growth, including the open sourcing of the project by Sun and Jonathan Schwartz
• Reflection on the 20-year anniversary of the project and its continued relevance and use.