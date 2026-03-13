• Measurement of backplane cabling between switch and compute sled using TDR
• Explanation of TDR measurement and how it works
• Discussion of challenges in measuring high-speed signals at 100 gigabit rates
• Explanation of insertion loss and its effect on signal quality
• Description of the signal processing chain at the receiver end
• Discussion of the noise floor and the need to keep the signal above it
• Discussion of the terms "insertion loss" and "return loss" and their significance in signal integrity
• Origins of the terms and their roots in RF engineering
• Impedance mismatch and its effects on signal transmission, including reflections and signal distortion
• The difference between circuit board and wireless channel signal tolerance
• The importance of signal speed and edge rate in signal integrity
• Explanation of impedance in non-mathematical terms, focusing on energy transfer and loss
• Discussion of impedance mismatch and discontinuity, including the effects of sharp edges and reflections
• The concept of impedance and its importance in signal transmission
• The definition of impedance as the ratio of voltage to current in a propagating channel
• The importance of matching impedance to the transmitter source impedance and destination receiver impedance
• The standard impedances for different protocols (e.g. PCIe, broadcast)
• The challenges of understanding impedance and its application in electrical engineering
• The analogy of high-speed serial links as "crappy radios" that can have idealistic channels
• The need for forward error correction and other techniques to recover signals in noisy environments
• The increasing complexity of receivers as speeds increase, and the borrowing of radio receiver techniques.
• Designing complex serial receivers for wired Ethernet and PCI Express
• Importance of modeling and simulation in system design
• Challenges of dealing with insertion loss and signal degradation in PCB design
• Role of software in system design, including ANSYS and Ensis
• Difficulties of vias and cross-sections in PCB design
• Need for 3D field software to accurately model complex PCB structures
• Discussion of the limitations of 2D math and the need for more sophisticated tools
• Comparison of current software limitations to older systems (e.g. Solaris)
• Difficulty in routing vias and traces in 3D geometry
• Challenges in simulating and debugging complex electromagnetic interactions
• Importance of accurate modeling and simulation in high-speed digital design
• Complexity of simulating 3D geometry and electromagnetic interactions
• Need for sophisticated software and expertise to run simulations
• High consequence of getting simulations wrong due to potential discontinuities and losses
• Importance of considering frequency-dependent loss and interconnect behavior
• Challenges in predicting and optimizing signal integrity and electromagnetic interactions
• Standing waves and energy loss at 28 gigahertz
• Importance of simulation in frequency and time domains
• Eye diagrams and their significance in data transmission
• PAM 4 and PAM 16 signaling and their impact on eye diagrams
• Validation of simulation data and its limitations
• Use of electromagnetic field simulators to model and analyze complex systems
• Insertion loss versus frequency discussed
• TDR (Time Domain Reflectometry) explained
• TDR used to identify discontinuities in a line
• TDR used in cable TV and power line maintenance
• TDR used in simulation to analyze high-speed interconnects
• Impedance calculation using TDR data
• Iterative process of simulation and analysis
• Use of TDR to optimize circuit board layout
• Discussion about validating simulation results with final physical testing
• Mention of the challenges and apprehensions in bringing up a new device
• Reference to a previous story about getting the Chelseo NIC up and running
• Description of issues with getting the 100 Gb/s link to work, with jitter being a major problem
• Discussion of expensive equipment (Labmaster scope) used to measure jitter
• Analysis of the clock source and finding the root cause of the jitter issue (100 ohm termination missing)
• Solution of adding a 100 ohm discharge resistor to fix the problem
• Reflection on the importance of proper termination for high-speed signals
• Clock signal was missing a terminating resistor
• Signal reflection and jitter caused issues
• Spec sheet stated not to use a terminating resistor due to short length
• Termination resolved the issue and improved signal quality
• Equalization (CTLE, DFE) used to recover signal from poor channel conditions
• Probe station was built to hold and stabilize microwave probes for measuring channel signals
• Probe station is a custom-made collection of off-the-shelf parts for precise measurements
• Plans to publish and open source a design for a tooling system
• Discussion of a common theme across the company of employees wanting to create their own tooling due to dissatisfaction with commercial products
• Benefits of allowing engineers to build their own tooling, including expertise in the problem and ability to create a solution that fits their needs
• Showcase of a custom probe station with a unique feature that adjusts the planarity of the probe
• Introduction to the GLscope client, an open source application for oscilloscopes that provides a user interface and front end
• Explanation of the GLscope client's architecture and features, including its ability to connect to multiple oscilloscope models and load waveform data from files
• Discussion of the importance of open standards and APIs for equipment, and how this prevents vendor lock-in and bad behavior
• API for oscilloscope connectivity provides a unified vendor-agnostic interface for writing code against a minimum set of requirements
• Feature allows connecting to multiple scopes and probing a common test point with channels from different scopes to view delta between them
• Data graph architecture allows applying transformations to data sources and visualizing output or using as input to other blocks
• Specific data example: quad serial gigabit media independent interface (QS-GMII) with 4 lanes of up to gigabit data
• Filter blocks for recovering clock, thresholding analog waveform, decoding 8b10b, and outputting 4 additional streams of 8b10b symbols
• Data streams can be fed to individual product decoders, such as for serial gigabit Ethernet, and decoded further
• Filter blocks are strongly typed, requiring input to match expected data type, and can be cascaded arbitrarily
• Open-source underlying libraries and a plugin model allow for custom decoders to be written and integrated
• Discussing a decode that converts 8-10 B objects to Ethernet frame objects
• Integrating the new decode with existing IP decode
• Building multiple switches and managing network complexity
• The importance of post-mortem analysis and simulation correlation
• Factors affecting simulation accuracy, including surface roughness and skin effect
• Details of transmission line construction and material properties (copper, nickel, plating)
• Copper vs. phosphorus doped nickel
• ENIG (electroless nickel immersion gold) process
• Service roughness and its impact on PCBs
• Resistance vs. dielectric losses in PCBs
• Fiber weave effect and its impact on signal integrity
• Simulation and measurement of PCB losses and fiber weave effect
• Importance of surface roughness and adhesion in PCBs
• Impact of PCB losses on high-speed digital design (jitter, skew, etc.)
• Developing a custom backplane with precise control over components
• Advantage of building from first principles and simulation-intensive design
• Unique approach to system design, controlling both sides of the link
• Overcoming challenges and measuring performance to ensure system reliability
• Team effort and collaboration in achieving a complex system goal
• Open source software and its importance in the domain
• Next discussion topic: supply chain security and management