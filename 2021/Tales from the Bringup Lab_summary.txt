• Discussion of initial board bring-up process
• Steve's first-hand experience with a quick board bring-up
• Comparison of Steve's expectations vs. reality
• Issues encountered during power checkout and testing
• Description of the server board's components and features
• Discussion of low resistance values between power planes and subsequent investigation
• Use of Cliff and Rick's test hardware to verify findings
• Explanation of the AMD Milan silicon and its capabilities
• Mention of the board's monolithic design and integrated components
• Discussion of a DC-powered board without a traditional power supply, operating at 54 volts
• Pre-power checkout and debugging process, including beeping out and schematic comparisons
• Part swap and rework with manufacturing partner to address issues with multiphase power supplies and connectors
• Initial power-up attempt with a Chrome event supply and current fault
• Troubleshooting and adjusting current settings to safely power up the board
• Checking the 54-volt supply and derived power after power-up
• Discussion of current limiter functionality and its role in protecting the board from overcurrent
• Explanation of the "no man's land" area on the board and its use for fans
• Design trade-offs and challenges related to fan placement and replacement
• Discussion of fan modification to reduce noise and potential for bearing failure
• Design decisions made to not make fans hot pluggable
• Issues with a small ice 40 FPGA in the power domain, including a schematic issue
• Debugging and resolving the FPGA issue
• Bringing up the IBC (54 to 12 volt converter) and power rails
• Debugging and resolving issues with supply rails and devices on the board
• Programming the service processor and running Hubris OS
• Checking out I squared z buses and devices on the network
• Resolving a spec change issue with resistor straps and device addresses
• Consistency and clarity in documentation and life cycle of units
• Importance of documenting changes during bring-up process
• Use of a dedicated person to document changes, resulting in extensive documentation
• Benefits of clear documentation for the rest of the team
• Progress with SPs, I-squared-c buses, and FPGA loading
• Challenges with power-on sequence and sequencer
• Replacement of flash parts on the board
• Use of a board heater to reflow BGA components
• The process of heating the board to reflow solder
• The importance of avoiding errors and manufacturing issues with the FPGA bitstream
• The use of a "board preview" or convection oven to heat the board
• The benefits of using the new bitstream compression method
• The attestation of the FPGA image and the potential for tampering
• The plan to attest the FPGA image before loading it into the FPGA
• The creation of the "zombie board" for power supply testing and design
• The issues with net names and level translators in the FPGA design
• Single-threaded approach to rework on a single piece of hardware
• Transition to parallelization and using flying probe testing
• Description of flying probe testing and its benefits
• Using thermal cameras for detection of overheating components
• Experience with a "zombie board" and issues with power supply and capacitors
• SDLE (SDVoE) is a load generator used to test power supplies and verify their performance under various conditions
• SDLE simulates power load steps, voltage changes, and frequency changes to test power supplies' ability to respond and behave
• The device uses Labview to connect to the power supplies and collect data, which is then analyzed to create graphs and reports
• SDLE can test power supplies' behavior at frequencies up to 300 kHz and can simulate power load steps of up to 200 amps
• The team used SDLE to test their power supplies and discovered quirks in the rails, but the two main power supplies passed testing with "flying colors"
• The team is now preparing to attempt their first SP3 power on with a Rome processor loaded into the system
• FPGA behavior causes issues with I squared c bus
• Level shifters on the bus have undefined behavior when powered off
• Different manufacturers' data sheets provide varying levels of information on how level shifters work
• TI's data sheets are considered better and more informative
• The problem was eventually solved by understanding the interaction between the FPGA and the level shifters
• The team experienced fear and confusion during the debugging process due to the complexity of the issue
• Powering on a system in Houston and observing unrelated issues in Atlanta
• Reviewing the power-on process and identifying potential issues with sequencing
• Revisiting the mobile lab and attempting to power on the system again
• Discussing the importance of protecting the SDLE (SP3) and its irreplaceable value
• Describing the team's efforts to troubleshoot the system, including testing and reworking wires
• Identifying the source of the issue as a bus scan error in PowerNavigator
• Describing the system's response to the error, including bus resetting and undefined behavior
• Discussion of a processor malfunction, initially suspected to be dead
• Troubleshooting of an I2C bus transaction issue
• Explanation of PowerNavigator software's behavior in response to synchronization loss
• Critique of vendor software, including PLL software, with ADI and TI mentioned specifically
• Discussion of loading an eeprom in a clock generator and issues with the software
• Acknowledgement of a button in the software that does not work
• Discussion of PowerNavigator and PMBus communication
• Concerns about controlling voltages with PMBus and potential for processor damage
• Exploring ways to prevent over-voltage or under-voltage with PMBus
• Open-sourcing Hubris and Humility software for PMBus reporting
• Describing the team's approach to software-hardware co-design and attention to physical constraints
• Describing an issue with an infinite reset loop on a processor
• Discussion of the AMD-provided ethanol x reference system for troubleshooting
• Describing modifications made to a motherboard to replicate a specific issue
• Discussion of a board that cannot be made to fail, even with manipulated signals
• Explanation of KB reset L, a pin that can cause processor reset, and its connection to a BMC
• A problem with KB reset L being floating and the discovery that it was connected to a spring pin on the processor
• Use of magnet wire to create a connection to the spring pin and resolve the issue
• Amusing comparison of the board's behavior to a scene from Beverly Hills Cop
• Anecdote from a book about Antioch engineers during World War II, referring to the machine as "the maniac"
• Appreciation for the helpfulness of AMD and the value of documenting the process with extensive notes
• Difficulty in diagnosing and fixing a problematic board
• Exploring possible causes, including vendor issues and instrument calibration
• The process of iterating through possible solutions and verifying them
• The impact of limited time and resources on the troubleshooting process
• The discovery of a voltage foldback issue caused by a layout error
• The use of a creative solution (copper tape) to fix the issue
• The outcome of the fix, including its success and the new margin on the problematic component.
• Discussion of extremely good power margin and its implications
• Mention of SPI 2 traffic and its relation to power management
• Introduction of VOTF (Voltage On The Fly) and its purpose in voltage change requests
• Realization that the power tool was not sending VOTF packets as expected
• Discovery of a bug in the power tool that only implemented half of the SPI 2 protocol
• Resolution of the issue with the help of Renaissance and AMD support
• Attribution of the problem to a firmware bug rather than a hardware issue
• Discussion of a project's reference design and deviations from it
• Issues with the Spy Wiggles board and pinout problems
• Debugging and rework of the board to resolve issues
• Demo of the project and its components, including the AMD processor and service processor
• Troubleshooting and debugging of serial port issues and characters not appearing on the terminal
• Discussion of TX and RX (transmit and receive) issues with hardware and embedded systems
• Troubleshooting a problem with an FTDI chip and a dongle
• Discovery of broken DuPont wires in the setup, causing open circuits and further complications
• Realization that the issue was not with the circuit or firmware, but with a faulty wire
• Reflection on the "odyssey" of troubleshooting and the excitement and terror of working with complex systems
• Conclusion that the experience is a valuable lesson in the importance of attention to detail and the potential for unexpected challenges in technical work.
• Discussion of a recent event that was initially considered a disaster
• Reflection on how the event's ending made it enjoyable to discuss
• Mention of the podcast or recording being fun and enjoyable to participate in
• Appreciation for Rick's efforts in creating the content
• Comment on the recording being a valuable resource for future employees