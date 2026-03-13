• Discussion of title changes for an article or presentation
• Bryan Can trill and Adam Levinthal's banter and friendly teasing about the title
• Introduction of Robert Mustachio and a lighthearted anecdote about his "bigamist" 4-year-old
• Discussion of AMD's Turin launch and Oxide's involvement
• George Coma's blog entry on Hacker News and its success
• The unusual positive comments on the video accompanying the blog entry
• George Coma's theory that the disappearance of in-depth content on the Internet has led to a renewed appreciation for quality content
• Benchmarking with Cruncher on Turin CPU, achieving a sub-5 second result
• Discussion of the Turin CPU's ability to hit 5 GHz on some skews
• AMD's Zen 5 c cores having a full 5-12 bit FPU and 3.7 GHz top clock speed
• Comparison of AMD's and Intel's SKU stacks and trade-offs
• Discussion of the importance of mid-range SKUs in the Turin lineup
• Comparison of the Zen 4 to Zen 5 and Zen 4 c to Zen 5 c performance jumps
• The discussion centres around the benefits of having a unified ISA (Instruction Set Architecture) and how it simplifies development and deployment
• The p cores and e cores from Intel are discussed, with the e cores being more efficient and the p cores being more performance-oriented
• The concept of ISA segmentation is criticized, particularly in the context of Intel's recent developments
• The Zen 5 and Zen 5 c architectures from AMD are compared to Intel's p and e core architectures, with AMD's approach being more straightforward and less confusing
• The discussion also touches on the trade-offs involved in choosing between different architectures and the importance of a unified ISA
• The conversation also veers into the history of the Centaur team and their acquisition by Intel, as well as the shutdown of the Via company and the transfer of the Centaur team to Intel.
• Discussion of Boxing's x86 manufacturing capabilities and their attempts to make x86 CPUs
• Comparison of Intel's AVX-512 implementation to AMD's AVX-512 implementation in Zen 5
• Analysis of the benefits of AMD's AVX-512 implementation, including increased clock speeds and reduced power consumption
• Discussion of Intel's Skylike and Bradwell CPUs and their issues with AVX-512 instructions
• Critique of Intel's Granite Rapids Leon chip and its lack of competitiveness compared to AMD's Zen 5
• Comparison of AMD's Zen 5 to Intel's Sierra Forest and Touring CPUs
• Discussion of SKU (Stock Keeping Unit) power and its impact on data centre power consumption
• Comparison of previous Genoa SKU stack to current SKU stack and its benefits
• Analysis of power savings from consolidating racks
• Evaluation of Turin-based sleds and their potential advantages
• Discussion of AMD's Infrastructure Roadmap (IRM) and its group classification for CPU TDP ranges (group e, group g, etc.)
• Planning for next-gen sled (Cosmo) and targeting specific power groups (group b, group g)
• Power stage design and routing issues with high-power CPUs
• Trade-offs between cost, space, and flexibility in power design
• Margin for error in power design to avoid misbehaviour and reliability issues
• Importance of firmware and software updates for power stages
• Discussion on using the same regulator and thermal design for high-power CPUs
• Discussion of thermal considerations for a 500-watt TDP CPU
• Implications of CPU's peak power draw exceeding its TDP
• Effects of high transient power spikes on power stages and PCB design
• Review of Peasants's new product and its potential impact
• Challenges of designing for density within a fixed power budget
• Considerations for power efficiency in rack-scale systems
• Managing power consumption in systems with high core counts and memory usage
• Excitement about p4 programmability and its potential
• Announcement of Excite Labs' use of p4 on next-gen switch
• Interest in AMD's Polaris announcement, which is a p4-based NIC
• Discussion of the importance of network programmability and its benefits
• Challenges in working with vendors to establish a p4 compiler substrate
• Need for an open and documented ISA to write p4 compilers against
• Discussion of AMD's potential to make their own switches and vertically integrate their technology
• Importance of establishing an open ecosystem and substrate for others to build on
• Importance of well-documented and committed interfaces for hardware to support multiple software stacks
• Excite Labs' features, including oxide, and alignment with the speaker's vision for programmable networking
• Bias in systems, with the speaker joking about having no bias
• Differences between Turin, Genoa, and Milan, including increased parallelism and changes to register numbers
• Changes to firmware blobs and the MPI framework in Turin
• Device training, a process of discovering and communicating with PCIe devices and adjusting link parameters.
• The challenges of working with complex hardware and firmware
• The use of reference platforms (such as Volcano and Ruby) for development
• The limitations of using reference platforms
• The development of a custom BMC (Baseboard Management Controller) card called Grapefruit
• The espy boot protocol and its advantages over traditional Spinor boot
• The need for espy to handle flash storage and other devices
• The comparison between espy and Spinor protocols
• espy allows the FPGA to translate flash pages, simplifying the process for AMD
• DDR 5 training times can be slow and laborious, taking around 11 minutes in some cases
• The use of espy enables the recovery of a second UART channel lost in Turin
• The need for a second UART channel is due to hardware handshaking requirements
• AMD provided a fix to allow the PSP to operate at 3 megabaud, greatly improving performance
• Discussion of espy and its capabilities for faster data transmission
• Comparison of espy to 3 megabaud and the potential benefits of faster data transmission
• Shared anecdote about a 1980s-era data uplink system that was still in use in 2020
• Explanation of the importance of the 3 megabaud link for system recovery and the potential for improvement with espy
• Discussion of the recovery process and the use of a slim down image for faster recovery
• Explanation of the benefits of using espy for recovery, including improved reliability, degradability, and manageability
• Discussion of OpenSSL updates and the potential for removing a specific component (LISA)
• Discussion of Turin and its relation to open cell
• Overview of OpenSSL and its development
• AMD's adoption of open standards, including Calibra and Open Cell
• Comparison of different software ecosystems on the same hardware
• Discussion of memory clocks and DDR 5 vs. DDR 4
• Changes from SP3 to SP5, including increased channels and memory size
• Discussion of memory bandwidth and latency in GPUs and HBM
• Comparison of 12-channel 1DPC vs 8-channel 2DPC configurations
• Trade-offs between memory latency and capacity
• Intel's Mediums and their deviation from JE DEC standard
• Importance of airflow and thermal design in high-density systems
• Discussion of backfilled via and their impact on signal integrity in high-frequency signals
• Back drilling requirements for high-speed boards and the challenges of accurately drilling via
• Increasing demand for back drilling due to growing frequency content and higher signal integrity requirements
• Use of simulation tools such as ANSIs and ADS to optimize via design and minimize signal integrity issues
• Discussion of specific CPU parts, including the 9175f, 9575f, 9965, and 9755, and their suitability for various workloads and applications
• Complexity and physicality of modern CPU design and the difficulty of managing power and performance requirements
• Partnering with Murat to support rack power above 15 kW
• AMD's support for HPC and FP 64
• AVX 512 and its benefits for AI workloads
• AMD's APU strategy and its future in AI and HPC
• Development of Apus continues despite hyperscaler focus on SKUs
• Availability of AMD MI300 A dev kit and its potential sale on New egg
• AMD's progress in the market, surpassing Intel
• Software support for AMD products, with a focus on the Open Sail initiative
• The importance of software support for AMD's success
• Trace, a tool for debugging and monitoring systems, with an upcoming conference in December