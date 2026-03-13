• Introductions and attendance
• Discussion of Twitter Spaces technical issues
• Overview of projects being worked on (Gimlet, Sidecar, PowerShell controller)
• Explanation of challenges with bringing up the Sidecar board, particularly the Tofino 2 ASIC
• Discussion of the power delivery network (PDN) and its limitations
• Explanation of the "load step" issue and its impact on the ASIC's operation
• High current spikes in ASICs can cause voltage drops and potentially damage the device
• Overshoot can cause an overvoltage, which may damage the part
• Operating within a narrow window is crucial to avoid damage or malfunction
• ASICs have specific requirements for undershoot and overshoot, typically 3-4% and 5-6 millivolts above the spec respectively
• Non-traditional power controllers, such as the Infineon, require complex tuning and tweaking of control loops
• A clear guide to control loop parameters is essential for proper tuning and optimization.
• Load slammer adapters used to simulate power delivery network
• Challenge of testing power delivery network without actual silicon
• Use of car audio cables for DC load and to test transient magnetic field
• Replacement of Tofino on select boards with load slammer
• FPGA control and sequencing of power rails
• Use of simulation models (Simplus) for initial tuning parameters
• Tuning of power delivery network with load slammer
• Work on other components such as management network and FPGA control
• Configuration of clock generator and auxiliary pieces on a board
• Incorrect bus connections and depopulation of components
• Device tree configuration and device indexing issues with TOML
• Stability of table order in TOML files due to b-tree processing
• Comparison of TOML to other file formats, including INI, highlighting its lack of strong typing
• Cliff abandoned the project and started his own variant called "order TOML".
• A board had a bus fault and the team had to move hotels due to power issues.
• The team experienced issues with the 1st week of bring-up, including power outages.
• Eric's tuning and testing revealed issues with the PDN and ground planes.
• The team discovered that 40-50 watts of power were being dissipated through the PCB due to copper resistance.
• Remote sense is used in some chips to measure voltage differential at the load.
• The team had difficulty measuring the PDN and ground plane issues due to limitations in differential probe technology.
• Measuring and resolving issues with voltage drops and ground balance on a device
• Identifying and ruling out noise and quirks in the device's measurements
• Understanding and explaining the device's power rails and multiphase controllers
• The device's first power-up and testing process
• A prank played on the team during a meeting with a potential investor
• Discussion of the heat sink used in the device and its vapor chamber technology
• Design of a large heat sink for a GPU, with concerns about its size and potential to crack the die
• Moment arm crisis: the heat sink's size and weight could cause it to rock and crack the die
• Solution: changing the heat sink from copper to aluminum, and shaving off excess fins to reduce weight
• Mechanical engineers' concerns about the heat sink's size and weight
• Comparison to future GPUs, which will also require large heat sinks
• Monitoring the heat sink's performance, including temperature and voltage
• Using Kapton to reduce thermal camera interference and track temperature
• Initial testing and verification of the heat sink's performance
• Discussion of "puppy dog warm" and "happy kitty warm" as descriptive phrases for ambient warmth
• Explanation of the tier switch and its management network
• Introduction of the 54-port 80-gigabit switch and its complexity
• Description of the VSE 7448 chip and its MIPS processor
• Discussion of the SDK and its role in bringing up the switch
• Explanation of the dev board and its unusual size
• Mention of the use of a separate microcontroller to talk to the switch via spy and write configuration settings
• Discussion of undocumented settings and configuration blobs
• Microcontroller slew rate configuration options (slow, medium, fast, very fast)
• Importance of setting slew rate to "slow" to avoid signal bounce and data corruption
• Use of a logic analyzer can sometimes resolve the issue
• Adding capacitance to the lines can also provide termination and resolve the issue
• Defaulting to "slow" slew rate is recommended, not "fast"
• Discussion of PLL failing to lock and its resolution
• Compiling the SDK and printing register reads and writes to identify the source of an issue
• Using a load-bearing dongle to program FPGAs, and the challenges of having only two dongles
• Troubleshooting issues with slew rate being too fast and bit errors
• Programming an external ePROM with parameters for the SerDes IP and Tofino ASIC
• Achieving a sign of life with the device, including clocks running and SPY data transmission
• Successfully programming the ePROM with the necessary parameters after resolving slew rate issues
• Discussion of a recent test or trial of a device or system
• Comparison of the test results to those of a similar system (Gimlet)
• Mention of a custom cable backplane and its development
• Explanation of the use of a PCI Express test card and adapter board
• Description of the "contraption" built to connect the device to a PCI Express slot
• Mention of eBay and online purchases for test equipment
• Discussion of clock recovery and PCI Express configuration modes
• Explanation of the source clock mechanism and its default mode in PCI Express configurations
• Configuring PCI Express clocking and recovery for a large PCI device
• Troubleshooting a clocking issue with a Tufino device
• Understanding the complexity of the ASIC and the need for Intel's SDK
• Discussing the development process for the VSC 7448 and Tufino devices
• Identifying issues with the Gimlet device, specifically with the PCIe connection and reset
• Exploring the importance of the Gimlet device for the company's existence
• Troubleshooting issues with a clock generator and PLL chip
• Dual-stuffed oscillators causing clocking problems
• External clock generator not resolving issues
• Resemblance to previous problem with the SP3, a similar device
• Team members' frustration and uncertainty about the issue
• Breakthrough in resolving the problem, but not the exact date
• Team's optimism and determination to solve the issue
• Discussion of a hardware issue with a custom board
• Identification of a problem with a pull-down resistor
• Change from 10k ohm to 500 ohm resistor resolved the issue
• Excitement and relief expressed by team members when the issue was resolved
• Importance of probing voltage measurements and reviewing vendor-provided IP
• Breakthrough in understanding voltage and pull-down requirements
• Footprint issue with 16-pin DFN packages, CAD error causing rotated pin numbers
• Difficulty with reworking small DFN packages due to lack of lead and small pitch
• Volunteers rework 12-13 footprints on a board, requiring fine work and specialized tools
• Importance of validating logic before revising board design
• The team is discussing a process called "dead bugging" where a chip is glued to a PCB with its legs up in the air.
• The team member spent 3.5 hours reworking the 4 chips to test the hot plug circuitry, which ultimately worked as expected.
• The issue was caused by a human error mismatch between the schematic symbol and the footprint, where the pin 1 location was incorrectly marked.
• The team has been lucky in avoiding similar mistakes, but the error had significant consequences.
• The team has been reworking issues on the Gimlet project, including a wrong package callout on the sidecar project.
• The team had trouble with a link between two ports on a chip, leading to a diagnosis of a missing loopback cable
• A software issue with a JSON parser led to missed configuration steps, including analog tuning parameters for SerDes
• A mismatch between port numbers in the schematic and spreadsheet was found and corrected, resolving the link issue
• The team spent several hours reconfiguring the platform, but ultimately found that the issue was due to the port number mismatch
• The experience highlighted the importance of collaboration with engineers and careful attention to configuration details
• The team's experience working with a partner, particularly Jeff Heat from the FAA, who was very responsive and helpful in resolving issues.
• The team's process of debugging and testing, which involved using shared knowledge and experience to identify and fix problems.
• The use of software tools and debug software to improve the debugging process.
• The importance of perseverance and retaining resolve in the face of challenging problems.
• The benefits of having a distributed team and using remote collaboration tools, which allowed for external perspectives and different approaches to problems.
• The use of chat channels and shared communication tools to facilitate collaboration and information sharing.
• Discussing the current activity of searching for a party parrot in party hats
• Expressing gratitude to listeners for joining the recording
• Mentioning past episodes and reminiscing about future recordings
• Referencing a past crisis or traumatic event and its resolution (the "500 ohms")