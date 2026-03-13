• Discussion of a personal experience involving the Three Stooges movie company and moving
• Book discussion of "Careless People" by Sarah Williams
• Decision to have Sarah Williams on a future episode of the podcast, but with a twist
• Comparison of reading "Bad Blood" and "Careless People" in terms of their engaging nature
• Discussion of the podcast's book club and planning a future episode focused on "Careless People"
• Introduction to a discussion of the Minibar project and the challenges of shipping hardware
• Explanation of how some developed software features are not shipped due to cost constraints
• Minibar is a tool for managing and testing the various components of a computer system, particularly the compute sleds and rack switches.
• The tool was developed to streamline the process of loading firmware and software onto the sleds and switches.
• The current process of programming the sleds involves loading multiple images, including firmware, host OS, and other software components, which takes around 10–15 minutes per sled.
• After programming, the sleds need to be tested to ensure they are functioning properly, which includes verifying communication with the rack switch, data plane Ethernet links, and ignition controllers.
• The development of Minibar aims to simplify and automate this process, making it more efficient and reducing the time required for programming and testing.
• The management network is an old network with integration and testing challenges.
• Sleds cannot be easily tested at the programming station due to locked interfaces behind Blind mate backplate connectors.
• Troubleshooting is labour-intensive and involves swapping sleds, switches, and backplate cables.
• Manufacturing and testing processes for sleds and racks have flaws and lead to unnecessary wear and tear.
• The team encountered a catastrophic failure of a sled's backplate connector, making it a priority to find a solution.
• A receptacle or interface that allows testing at the programming station is needed to eliminate errors and improve manufacturing efficiency.
• The need for a dedicated piece of hardware to facilitate development and testing of to compute sleds
• The idea of creating a "magical Ethernet" solution using a dongle board to connect to the management network
• The creative solutions used to test and develop the sleds in the absence of dedicated hardware, including using IKEA tables and lab sleds
• The identification of five specific hardware requirements for the manufacturing station, including connecting to the sled's ignition target, testing PCIe interfaces, breaking out management network Ethernet, and testing Ethernet links
• The development of the k-dot-2 adapter, which allows for the programming of the host OS image by pulling one of the u-dot-2 SSDs out of the sled and plugging in a PCB with a 10G Ethernet NIC
• The complexity and difficulty of programming the m-dot-twos, including the lack of functional m-dot-two programmers.
• Discussion of a 3D printed enclosure for a PCIe interface, and the issues that arose with its design and fit.
• Reference to a "mass casualty incident" where many sleds were damaged during programming, and the importance of careful programming to prevent such incidents.
• Discussion of the need for an operator-friendly solution for programming, including protection from ESD and careful handling of the printed circuit board.
• Introduction of the concept of "minibar", a name chosen for a new system that will address the issues discussed.
• Design of a rack switch to manage PCIe connections
• Origins of the "minibar" name and its development
• Challenges in designing minibar, including limited hardware engineering credits and the need to reuse existing architecture
• Transition from Orca to Actium for design tooling
• Pain points in building the first racks, including troubleshooting switch issues and QSFP port management
• Complications with the rack switch's design, including its multiple printed circuit boards and cabling
• Different customers have different optics and transceivers in their data centres, which requires customization for each switch.
• The process of testing and verifying the fibre connections and optical modules is a complex and time-consuming process.
• A manufacturing defect was discovered on the QSFP board, causing issues with the press fit connectors, which was difficult and time-consuming to repair.
• A custom-built "rotisserie" was designed to facilitate the repair of the QSFP board without having to remove the switch from the rack.
• The rotisserie has proven to be a valuable tool, but also a testament to the custom and often complex solutions that the company has to develop to address specific problems.
• Development of Medusa, a 32-port loop back tester for rack switches
• Transition to Actium CAD tool and creation of parts library
• Importance of upfront work in Actium, including component registration and review
• 10-month journey to learn Actium and build parts library
• Nathanael Huffman's work on integrating Actium's PLM and component libraries
• Integration of SolidWorks with Actium for mechanical design
• Benefits of Actium's 3D renderer and design rules for package-to-package distance
• Doug Ribbon's work on mechanical design and ECD co-design integration in Actium
• Collaboration between hardware engineers using Actium and SolidWorks.
• Describing a problem with connectors on the mini bar tester that are only rated for 250 mating cycles
• Exploring alternative design options, including using a short cable to bridge the gap between the compute sled and mini bar PCBA
• Discussing the benefits of using a cubby with a blind mate backplate connector to minimize the risk of operator error and damage to the connectors
• Considering the long-term implications of connector lifespan and the need for replacement, with estimates suggesting that up to one mini bar per year may be needed for replacement due to connector wear
• Emphasizing the importance of getting the design right to avoid costly failures and maintenance issues
• Mechanical design of a new system, including a rugged enclosure and a compact version called "minibar light"
• Development of the board and layout, including constraints on size and depth due to rack and shelf space
• Design of "minibar" and "minibar light", including features such as PCIe interface, management network switch, and root of trust
• Miniaturization and re-packaging of electronics for "minibar light" in a 3D printed enclosure
• Comparison of full "minibar" and "minibar light" designs, including costs and applications
• Discussion of manufacturing and lab use cases for the two designs
• Minibar Lite is a smaller, more lab-focused version of the original minibar, designed for oxide engineers familiar with the hardware.
• Discussion of adding a GPU to minibar, with limitations (75 watt or less, bi four mode).
• PCI add-in card for Ethernet NIC's can be used, and minibar can tolerate 75 watt class cards.
• The mechanical enclosure was designed by Doug, and features a PCIe riser cable.
• Minibar was designed to be cat-proof, with secure door latches.
• Bring-up process, including initial power-on checks done remotely, and upcoming in-person bring-up at Benchmark Electronics.
• Initial power-on checks were done by Ian at his house, with plans to assemble and test minibar mechanical assemblies in-person with the team.
• Describing power supply and system power rail setup in Minibar
• Observing green LEDs flickering on and off every 10 seconds, indicating a potential issue with the hot swap controller
• Identifying the ADM 12772 hot swap controller's reset input and its potential to cause the board to reset and boot loop
• Understanding the purpose of two hot swap controllers on Minibar: one for protecting system power supplies and another for hot-plugging sleds
• Discussing the ability to remotely power cycle the board and updating firmware
• Describing a design decision to tie the reset line to the FPGA's 3.3V power supply rail
• Analyzing the problem of ground bounce between 3.3V and ground, causing the hot swap controller to reset the board
• Identifying the solution as cutting the PCB trace to remove the pull-up resistor and hold the reset line reasserted
• Discussing a mistake where a probe touches 54V to the reset line, blowing up the board
• Noting the importance of having a backup board
• ESD protection structures in FPGA and hot swap controller causing issues
• Board with blown FPGA was reworked and replaced with another board
• Shipping issues with heat sink causing bowing
• Debugging and troubleshooting process on second board
• Importance of thorough checks and testing before powering up boards
• Boards have a defect where a current sense resistor is rotated 90 degrees, causing the switching supply to malfunction
• The malfunction occurs when the switching supply sees infinite current due to the short circuit
• The defect was caused by an assembly error, where the pick and place machine incorrectly placed the resistor
• The issue was present in 2 out of 15 boards, with 13 boards functioning correctly
• The defect was likely due to the similarity in colour between the resistor and the solder mask on the board, which may have caused the automated inspection camera to misidentify the resistor's orientation
• The issue was reported to the board assemblers to improve their process and prevent similar defects in the future
• The conversation is a humorous anecdote about the experiences of an engineer working in a bring-up lab
• Debugging process for a failed board with a popped power supply
• Difficulty in identifying the problem with the first board
• Use of Dickey to obtain replacement parts
• Theory that the failure mode was due to a short circuit when powering off
• Use of an oscilloscope to capture power supply rail traces
• Identification of a short circuit on the first board
• Troubleshooting techniques used to identify the short circuit
• Repairs made to the first board, including reworking and reassembling
• Testing and validation of the repaired board
• Discussion of software development and current status
• One identified bug in the RMI Ethernet signal connection
• Lessons learned from manufacturing and design process for Minibar
• Reworking of service processor on Minibar board to fix connectivity issue
• New design for Cosmo programming header to simplify and automate the process
• Unified programming header for unified manufacturing and scalability
• Plans for scaling up production and automating manufacturing processes
• Development of a product, specifically a hardware component, with significant progress and excitement
• Team effort and contributions from multiple people, including mechanical engineers
• Photos and demonstrations of the product, including a successful prototype
• Plans for manufacturing and distribution of the product
• Upcoming episode discussing a support case and future guests