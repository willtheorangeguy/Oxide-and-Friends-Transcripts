• Discussion of sending a social media message
• Refusal to send the message on LinkedIn
• Introduction of new participants and celebration of a new addition to a family
• Discussion of a previous problem-solving effort, Oxide, and the development of a service processor
• Explanation of baseboard management controllers (BMCs) and their limitations
• Criticism of BMCs and their painful user experience
• Discussion of the challenges of connecting service processors over a network
• Mention of a 2019 talk by Rick Alther on a BMC exploit, "BMC Anywhere"
• Explanation of the vulnerability and its potential consequences
• Discussion of the use of NCSI (Network Configuration and Services Interface)
• NIC (Network Interface Card) features and requirements
• NCSI (Network Channel Sideband Interconnect) protocol and its challenges
• Reset and power domain concerns with NCSI
• Complexity of NICs with multiple power rails, CPU cores, and features
• Difficulty in understanding vendor implementation of NCSI and lack of documentation
• Uncertainty and frustration with NCSI's potential to work correctly
• Comparison of NCSI to traditional OCP (Open Compute Project) designs
• Discussion of "NCSI or bust" catchphrase and its implications.
• The difficulties of implementing NCSI (Network Control and Status Interface) due to power management complexities and conflicting design decisions.
• The decision to pursue a cable backplane and blindmating into it, which reduced the argument for NCSI.
• The realization that a separate management network was necessary and the adoption of the "monorail" solution.
• The origin of the name "monorail" and its technical significance.
• The constraints that led to the development of monorail, including the use of a secondary ASIC in the same chassis and the need for a reduced number of ports.
• Developing a high-port-count ASIC for a 32-server rack with 32 sleds and 2 switches
• Need for 30-37 ports and challenges in finding a suitable ASIC with that many ports
• Industry pseudo-standard QSGMII and use of breakout chips to achieve 48 ports
• Difficulty in finding inventory due to supplier shortages and automotive industry's demand for Ethernet
• Conflict between 2-conductor and 8-conductor Ethernet connections
• Use of magnetics in twisted pair Ethernet and limitations in finding space for them on a circuit board
• Alternative solution using Microchip's switch ASIC with SDMAI (Serial Gigabit Independent Interface)
• Use of SDMAI for differential signaling, allowing for AC coupling and reduced need for magnetics
• Compatibility with existing cabling and potential for future upgrades to 1 or 100 gigabit speeds
• The name "monorail" was inspired by a Simpsons reference
• The term was coined by Keith
• The first reference to "monorail" in Oxide's history was in November 2020
• The team had to find a solution to connect the service processor to two independent switches using a single RMII connection
• They used a PHY part from Microchip to translate the RMII interface to SDMI and 100 FX interfaces
• The solution was complex and involved using VLAN trickery to keep the two paths separate
• The team had to overcome several challenges, including finding a suitable small switch and ensuring no switching loops occurred
• The solution was unique and had never been built before
• Moving the Switch chassis to sit in another chassis across a cable, exposing a clean SGMII interface to the outside world.
• Exploring the possibility of connecting a microcontroller with an SDMI interface or a small switch with 2 SGMII interfaces and an RMI link.
• Discovering that 100 Base FX has no standard, and companies have been implementing their own versions with no clear specification.
• Figuring out the electrical specification of 100 Base FX through experimental setup and prototype development.
• Introducing Matt and having him work on making the software side of the system work, including using the VSC 7448 manual and bypassing the MIPS core in the switch ASIC.
• Discussing the massive size and cost of the dev kit for the 7448, and how Matt would be working with it.
• The group wants to own the firmware and have trust in the system, without needing another processor.
• The reset of the chip is done through pin strapping and configuration over spy, but setting registers to correct values is complex.
• The chip's datasheet and register list are not sufficient to bring up the chip, and the canonical way to do it is through Microchip's Mesa API.
• The group used a soft emulator to log register operations and compare against their own configuration code.
• The chip has a mode where groups of 4 SerDes are ganged together, which causes issues if not properly configured.
• The group discovered that some ports only work if another port is up, and had to use a probe and oscilloscope to analyze the packets.
• They were able to tune the link remotely after using the probe and oscilloscope.
• Setting up a Google Meet with a webcam to tune an oscilloscope
• Using a network switch to remotely connect to a computer and twiddle survey parameters
• Discovering that the oscilloscope needed to see the right kind of transition to trigger
• Figuring out that the firmware payload needs to be loaded onto the PHY chip
• Patching an 8051 core to load the firmware update
• Understanding the complex layers of IP and indirect registers to communicate with the chip
• Realizing the importance of correct 8051 code for the link to function
• Comparing the complexity of working with 1G and 100G links
• Appreciating Microchip's publication of their documentation, including register specs and notes about Bugzilla fixes
• Challenges in obtaining specific parts due to inventory issues and lead times
• Selection of non-automotive grade parts due to availability and cost
• Development of tooling to understand and work with the parts, including writing a Doxygen parser and building Rust code
• Building and testing of a network switch using a dev kit and off-the-shelf components
• Creation of demo to showcase the switch's capabilities and features
• Discussion of lead times and the impact on inventory and procurement decisions
• Discussion of a tool called Monorail status and its usefulness in system status monitoring
• Troubleshooting issues with a link between the Monorail switch and a big switch, including auto negotiation problems
• Use of watchdogs to detect and reset stuck links
• Comparison with other network configurations, including DTrace and NCSI alternative
• Importance of a robust management network for debugging and system operation
• Discussion of tooling for accessing SPs on management network, including structured and unstructured (hacky) tooling
• Description of hacky tooling, which allows reading of arbitrary memory from the chip
• Importance of management network speed and its impact on debugging and updating systems
• Explanation of the management gateway service and its role in exposing functionality to the service processor management network
• Discussion of the connection between the service processor and host OS, and how it is exposed over the management network
• Description of a serial console proxy feature that allows access to the service processor's serial console over UDP
• Discussion of the use of John's work on the Humidi console and its non-lossy, non-faithful serial console proxy
• The Humility console proxy allows for serial console access without a management network connection
• The proxy uses a debug dongle and can simulate a management network with a 400ms delay
• The tool was created in response to a need for serial console access without a management network
• The service processor in the system has a UART that is used for inter-processor communication and is load-bearing
• The system has the ability to boot over k dot 2, and early boot time parameters can be set by the service processor
• The inter-processor control channel (IPCC) is used for communication between the service processor and host
• The team has developed a way to restore a "gimlet" (a type of device) to a working state using the management network, even if the device's hard drives are dead or missing.
• The process involves using a hash in the device's RAM to locate a matching image on the management network, which is then streamed to the device.
• The current speed of the process is around 300 kilobytes per second, which is relatively slow, but the team is working to improve it.
• The team has also developed a way to use the management network to install a new image on a device, which can be used in the factory instead of manually imaging the device's hard drives.
• The team has tested this process in their manufacturing process and found that it works as expected, even in a "last resort" scenario where the device's hard drives are dead or missing.
• Discussion of the technician port vs. network download speeds
• Challenges of integrating multiple components and systems
• Development of a recovery process for the system
• Use of a debugger to streamline debugging process
• Importance of getting feedback from users on tooling and systems
• Reflection on the process of building and refining systems and tools over time
• Oxide's management network and the power control network, Ignition
• Challenges and difficulties in developing robust systems
• The importance of Ignition Control in debugging and recovery
• Kernel bugs and their impact on the control plane agent task
• Hubris and its design for robustness and reliability
• Open-source nature of the discussed projects and code availability