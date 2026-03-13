• Sam Altman was reportedly losing millions due to being polite to AI
• Bryan Can trill joked about wanting it to cost him billions
• Microsoft's study found that being polite to AI leads to politeness and respect in return
• Bryan Can trill's motives for being polite to AI were questioned
• Discussion of past conversations and Bring Up episodes
• Review of past projects, including Gimlet and the AMD Turin-based sled
• Discussion of the design and development process of Gimlet and its challenges
• Mention of changes made to the design process and team structure
• Difficulty in finding quality or understanding of specific needs in early stages of project
• Lack of a consolidated part library and inefficient corporate processes
• Need to own and consolidate hardware design processes, including CAD and PLM systems
• Transition from Orca to LTM (Actium) and focus on holistic design changes
• Addition of FPGA for sequencing and flexibility in power management
• Explanation of PLM (product life cycle management) and its role in managing BOM and product tree
• Discussion of sequencing requirements for complex chips and power domains
• Chip sequence and handshake signals
• Use of FPGA for programmable logic
• I2C interface and SPD (Serial Presence Detect) bus
• espy boot and multiplex channels
• UART and IPCC (Inter-Processor Communication) channels
• Hot plug subsystem and PCA 9506
• Discrete logic and reworking challenges
• AIC NIC and U dot two interface
• Changes to logical gates and active low logic
• Designing a new board, Cosmo, with three FPGAs: one for ignition, one for sequencing, and one for hot plug IO
• Using a Filing Spartan seven FPGA for sequencing and a Lattice ICE 40 FPGA for hot plug IO
• Maintaining the same Secure Silicon architecture as Gimlet, despite concerns over the LPC 55 chip
• Implementing espy and its boot process on Cosmo, with some reservations about its performance
• Using a "grapefruit" board, based on the OCP form factor, as a development platform to test and validate Cosmo's design
• Risk-retiring some of the FPGA design using grapefruit, including implementing Spy and hubris drivers for Cosmo
• Development of a shim to fetch data from flash
• Implementation of espy design for FPGA, including infrastructure and build setup
• Integration of espy with Ruby and Grapefruit, including debugging and risk retirement
• Hubris integration with FPGA, including coordination of outputs and inputs
• Use of FMC bus for connecting FPGA peripherals to SP's memory space
• Workarounds for strange errata on FMC peripheral
• Use of grapefruit to test and debug Cosmos, including finding potential errors and changes to be made.
• Importance of the FPGA in the design and its impact on the validation process
• Finding and fixing a missing pull-up resistor on the weight pin in Grapefruit
• Need to add pull-up resistors on I2C level translators in Cosmo
• Impact of not having a functioning FPGA on the project timeline and validation process
• Benefits of testing and validating on Grapefruit before moving to Cosmo
• Issues with testing the SPD proxy and Ruby on Cosmo, including signal integrity problems
• Other items that will be tested for the first time on Cosmo, including hot plug functionality and sequencing
• Process of bringing up Cosmo in the manufacturing facility, including quick resolution of initial power-on issues
• Implementing a 12V converter and FPGA for power management
• Flashing a Cosmo image and experiencing issues with peripheral addresses
• Identifying a pin on the FMC bus that was not wired up correctly
• Performing a rework to jumper the pin and bypass the issue
• Debugging a data path problem in the FPGA and determining it was caused by a hubris peripheral conflict
• Resolving the conflict and testing a different board to prove the fix
• Replacing the SP and FPGA on the original board and successfully testing it
• Discussion of a board design issue that led to power failure and "board of death"
• Importance of reworking and re-testing the boards to ensure functionality
• Value of reworkable boards due to high cost of replacement parts
• Offer to give away dead boards as souvenirs to listeners
• Gratitude for benchmark rework services for repairing damaged boards
• Discussion of rework process for Gimlet Rev and Rev boards
• Upcoming SP5 power-up and issues with SALE telemetry
• Resolution of firmware update issues with Renaissance's help
• Discussion of progress on "SP5" and "Gimlet" projects
• Installation of capacitors for TLVR design
• Powering up "SP5" and initial results
• Clock issues with processor, suspected to be due to lack of burden resistors
• Installation of burden resistors and subsequent success in getting clocks to run
• Discussion of method for measuring clock signals due to probe effects
• Explanation of RTC clock behaviour and its slow start time due to power cycling
• Problem with quartz crystal circuit taking a long time to stabilize
• Solution is to keep it powered by a battery, as most servers don't turn off the rail
• Difficulty measuring clock signal and sequencing process
• Troubleshooting involved using oscilloscope to "glitch" the crystal into starting
• Sequencing process involves handshakes between components, with final step being release of reset pin
• Concerns about clocks and need for further exploration and debugging
• Discussion of various dongles and programming adapters, including the "mega dongle"
• Discussion of a consolidated board connection for contract manufacturer
• Use of debug headers for FPGA development
• Debugging of FPGA issues, including build variability and timing constraints
• Introduction of the ILA (Embedded Logic Analyzer) tool for debugging
• Use of the ILA tool to detect booting of the FPGA
• Discussion of pranking and showmanship in debugging processes
• Troubleshooting of issues with FPGA sequencing and booting
• Troubleshooting issues with SP5 FPGA design, including clock crossing and pin issues
• Discussion of debugging techniques, including using a Sale to understand the FPGA's behaviour
• Minibar board development, including validation of the management network and successful tests
• Challenges and bugs encountered during Minibar development, including RTL bugs and issues with the Spy interface
• Celebration of Minibar's successful development and validation, with emphasis on the team's efforts and accomplishments.
• The group discusses a project where they were testing a system, and it seemed to work, but then would suddenly stop.
• Nathanael Huffman mentions that he's spent a lot of time looking at "spy traces" and has a good understanding of what they're supposed to look like.
• The group determines that the issue is likely related to the FPGA, not clocking or other issues.
• Nathanael Huffman discovers that a reset pin was misconfigured as an output instead of an input.
• The pin is translated, which caused the system to malfunction.
• Nathanael Huffman also mentions that he made assumptions about debug pins that may have been incorrect or may be a tool bug.
• Reset line with no driver in the design
• Synthesizer warning and defaulting to zero
• Debug pin connected to internal net by VIVO
• Build-to-build variability and potential functional change
• Importance of following design rules and timing constraints
• Challenge of navigating a sea of warnings and finding the critical one
• Debugging process and resolving issues with Soft Logic
• Booting and achieving functional results after resolving issues
• The team was experiencing issues with the SPD bus on their hardware, Cosmo, which was causing problems with reading the SPD signals.
• The team suspected that the voltage translation was causing the issue, but they couldn't convince themselves that everything was working as expected.
• Aaron Hart wig mentioned that he was using a slow VNC connection to develop the code, which was frustrating.
• The team spent time looking at ILA traces and probing the Sale, but couldn't find the source of the problem.
• Nathanael Huffman suspected that the issue was due to the level translators not functioning as expected, and that they were causing the bus to float.
• The team decided to try adding pull-down resistors to the level translators to see if that would fix the issue.
• Nathanael Huffman added 16 2.21k resistors to the board, and it fixed the problem, allowing the team to boot up the hardware successfully.
• The team is now able to train the Simms and is moving forward with their development.
• Discussion of the training time for a project, which is longer than expected but is being addressed by caching information
• Progress update on the project, including successfully booting and reaching multi-user mode
• Resolving issues with PCIe and other components, including level translators and hot plug controller
• Review of the team's efforts and progress over the past few months, including the use of simulation tools and actual hardware
• Discussion of the time it took to bring the project up to speed, estimated to be around 5–6 months
• Plans for future work, including dim margining, eye diagram analysis, and PCI link training
• The new schematic for a project (Cosmo) is more readable and easier to use than the previous one (Gimlet).
• The team is proud of the work they've done on the new schematic and its readability.
• The team is hoping to share the new schematic with others and have them appreciate its craftsmanship.
• A bizarre issue was resolved quickly, and the team is proud of their work.
• The next priority is to work with Morris Chang.