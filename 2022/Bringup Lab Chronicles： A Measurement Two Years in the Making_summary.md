• Origin of the project and its measurement of backplane cabling
• Explanation of a TDR measurement and its use with a wave pulser
• Benefits and limitations of TDR compared to S-parameter measurement
• Challenges of measuring high-speed signals in a 100 gigabit backplane
• Impedance profile and reflections in a channel and their effects on signal transmission
• Noise floor and signal processing requirements for receiver to accurately measure signal
• Connection of cable, connectors, and PCB and their impact on signal transmission
• Signal processing chain at receiver end
• Manufacturer's specification for signal loss
• Insertion loss and return loss parameters
• Impedance mismatch and reflections in high-speed signal integrity
• Relationship between RF terms and high-speed signal integrity
• Example of setting pin speed too high in software
• Discussing the challenge of sending a 20 megahertz clock signal with a 1.6 gigahertz edge rate
• Explaining impedance and how it relates to the amount of information that travels from one place to another
• Describing impedance as a measure of energy going into a channel and how it can cause reflections when not matched
• Discussing characteristic impedance and its relation to voltage and current
• Identifying specific impedance values for different transmission protocols (e.g. PCIe, single-ended, broadcast)
• The concept of 50 ohms as a standard impedance for electronic systems
• The reasons behind choosing 50 ohms, including historical and practical considerations
• The differences between 50 ohms and 75 ohms used in the broadcast industry
• The importance of matching impedance in electronic systems to minimize reflections
• The concept of impedance and its relevance to high-speed serial links
• The challenges of intuitively understanding impedance and its application in RF systems
• The trade-offs between complexity, power consumption, and performance in high-speed serial links
• Forward error correction and its importance in radio protocols to prevent retransmission
• Use of sophisticated techniques in serial receivers for wired Ethernet and PCI Express
• Planning and modeling of systems to ensure they work, including use of software and simulations
• Importance of PCB design and layout to minimize signal loss
• Use of field solvers to analyze and optimize PCB traces and vias
• Complications of vias in PCB design and the need for 3D field solvers to analyze them
• Inductances and capacitances in vias and their impact on signal behavior
• The discussion involves creating a 3D physical piece of art with complex vias and circuit board layers
• The challenge of debugging and simulating the system's behavior, including RX layer coupling to TX layers
• The limitations of 2D CAD programs and the importance of visualizing the system in 3D
• The difficulty of testing and validating the simulation, including assigning ports and solving equations
• The complexity of extracting S parameters from a large number of ports, which can take a significant amount of time and resources
• Challenges in simulating complex physical systems, particularly with high-frequency signals
• Importance of accurate modeling and simulation in avoiding costly mistakes
• Comparison between simple software simulations and complex physical systems, highlighting the limitations of software simulations
• Discussion of the behavior of electrons in physical systems and the difficulty of modeling their behavior accurately
• Importance of understanding the physics of interconnects and their impact on signal transmission
• Effects of loss and frequency-dependent loss on signal transmission and the importance of accurate modeling
• Discussion of standing waves and their impact on signal transmission, including the creation of notches in the signal
• Importance of accurate spacing of vias and IC packages in avoiding signal degradation and errors
• Discussion of simulation methods for analyzing signal transmission and eye diagrams
• Explanation of eye diagrams, including open and closed eyes, and their significance in determining signal quality
• Comparison of different signaling methods, including PAM 4, PAM 5, and PAM 16
• Critique of the limitations of eye diagrams and the potential for errors in data sheets
• Discussion of the importance of validation and accuracy in simulation and signal analysis
• Ground-based physics simulations using electromagnetic field simulators
• Analyzing signal behavior at differential vias and escape routing
• Using finite elements and wave equations to solve for field behavior
• Creating circuit models by cascading individual component models
• Frequency domain analysis: insertion loss vs frequency and signal propagation
• Time domain reflectometry (TDR) analysis: determining discontinuities and impedance
• Analogies to phone lines and cable TV, where TDR devices were used for troubleshooting
• Time Domain Reflectometry (TDR) used to measure discontinuities in transmission lines
• TDR calculates distance resolution based on time resolution and propagation velocity of light
• Method used to locate and repair faults in underground power lines
• High-speed interconnects use TDR to measure signal propagation and impedance
• Simulation data used to iterate and optimize circuit design
• Tools help mesh structures for accurate time domain measurements
• Diagnostic used to learn more about circuits and tune them
• Iterative process of running simulations and acting on results to optimize design
• Discussion of a NIC (Network Interface Card) that is not working as expected
• Issue with the NIC not reaching 28 Gbps, but working at 10 Gbps
• Analysis of jitter using a Teledyne LaCroix scope
• Discussion of the cost and complexity of the scope
• Investigation into the source of the jitter, including power and clock input
• Conclusion that the issue may be due to the lack of a 100 ohm differential termination on the input clock
• The device was put into LVDS mode, but lacked a 100 ohm differential terminator, which was suspected to be the cause of the clock jitter issue.
• Adding a 100 ohm differential terminator improved the clock jitter, but the device still did not work properly.
• The discussion turned to the NIC's clock source and transmission lines, with the conclusion that the NIC's clock source was electrically short and therefore did not need a terminator.
• The team realized that they had been relying on the reference design and not fully understanding the underlying principles, which had led to the issue.
• Adding the 100 ohm differential terminator was determined to be the solution to the clock jitter issue, and would allow for longer cable lengths.
• Discussion of verifying a design through simulation and iteration
• Verification of the design's feasibility and plausibility
• Identification of a missing resistor in the clock circuit and resolution of the issue
• Discussion of signal quality and degradation in a channel
• Explanation of equalization methods (CTLE, DFE, FFE) to boost high frequencies
• Description of a custom-built probe station to measure signal quality
• Discussion of challenges in probing a complex PCB and the limitations of commercial probe stations
• The speaker mentions a plan to open-source a design they had been working on in a previous job.
• The speaker notes that it's a common theme across the company for employees to come in with ideas for tools or software they want to build on their own.
• Tom provides feedback that the speaker hasn't acted on yet.
• The speaker discusses the benefits of allowing employees to build their own tooling, as it often results in better solutions.
• The conversation turns to a specific tool, the probe station, which is a mechanical system for testing.
• The speaker highlights a unique feature of the probe station, the ability to adjust the plenarity of the probe points without moving the tip.
• Discussion of an open-source application called GLScope client for oscilloscopes
• Explanation of LibScope, an object-oriented library that provides an API to oscilloscopes
• Description of the ability to connect to various oscilloscope brands using the same UI and API
• Overview of the filter graph architecture used in the system
• Explanation of how data can be acquired from any source node, including physical instruments or file data
• Discussion of the ability to apply channel emulation and visualize the output of transformations
• Description of the vendor-agnostic C++ API presented by LibScope
• Explanation of the benefits of using LibScope, including reduced vendor-specific code and increased flexibility.
• The discussion revolves around a high-speed data link using QSIGMI (Quad Serial Gigabit Media Independent Interface) and its encoding and decoding processes.
• The link has four lanes, each running at 1.25 Gbps, with a round-robin send sequence.
• The encoding process involves sending a 10-bit symbol from each lane, with specific idle characters to maintain sync.
• The signaling within each lane is serial GIMME (Gigabit Media Independent Interface Media Extension), similar to regular gigabit Ethernet.
• A custom filter block was written to work with the QSIGMI data, which decodes 8B10B symbols and outputs four additional streams at one quarter of the rate.
• The block determines the correct lane by identifying the idle character and then creates four streams of data at one quarter of the rate.
• The streams can then be fed into individual protocol decoders for serial GIMME, which will decode Ethernet frames.
• The discussion also touches on the plugin model and the possibility of creating custom protocol decoders using the underlying libraries.
• The binary stability is still a work in progress, and releasing a binary blob protocol decode is not recommended due to the lack of binary stability.
• Developing a decode for gigabit ethernet
• Writing a new decode that takes in AP10B objects and spits out ethernet frame objects
• Using existing decodes to process output of new decode
• Building multiple switches, not just one, with different network configurations
• Importance of simulation and postmortem analysis in verifying network designs
• Factors affecting simulation accuracy, such as dielectric constants, weave effects, and surface roughness
• Difficulty in accurately specifying surface roughness values from vendors and the need for characterization by users
• Skin effect on copper transmission lines at high frequencies
• Rough surface of copper can affect resistance loss in transmission lines
• Intentionally rough surface on one side of copper for adhesion to epoxy layer
• Importance of designing PCB stackup to minimize losses
• Trapezoidal effects on traces and their impact on signal transmission
• Enig (Electroless Nickel Immersion Gold) plating and its advantages
• Nickel's poor performance as a conductor for RF signals
• Use of microstrip instead of external traces
• Effect of nickel-phosphorus alloy on signal transmission and resistance loss
• Use of gold plating on external layers due to its conductivity and solderability
• Resistance losses in PCBs are a major concern and are often more significant than dielectric losses.
• Dielectric losses can be reduced by using materials with low dissipation factors, but this comes at a cost.
• Copper resistance losses can be improved by increasing the width of the copper trace, but this can lead to issues with dielectric thickness and layer count.
• The fiber weave effect, where the orientation of the fiberglass weave affects the dielectric constant, can cause issues with signal delay and skew.
• Simulation can capture the effects of the fiber weave, but measurement is also possible.
• Mitigating the fiber weave effect requires careful routing and optimization, and can be a significant challenge.
• The impact of the fiber weave effect can be as little as 1-2 picoseconds, which can be critical in high-speed designs.
• Analyzing the fiber weave effect in simulation can be done by modeling the epoxy and fiberglass weave.
• The topic has been explored in research papers, but specific references were not mentioned.
• Development of a measurement system that took two years to complete
• Unique challenge of connecting two systems with known specifications
• Flexibility in design due to controlling both sides of the link
• Complex backplane design with multiple connectors and copper connections
• Measurement and characterization of cable lengths and quality
• Importance of margin and buffer in system design
• Team effort and collaboration in achieving the goal
• Open source software and its role in the project
• Importance of reliable software performance on the system
• Call to action for software developers to prioritize correct code and efficient use of resources.
• The meeting is wrapping up
• Kate will be discussing supply chain next time
• The next meeting will be about supply chain
• The host thanks attendees, including Robert and Larry
• The meeting is closing with repeated goodbyes