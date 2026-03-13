• Introducing a pick and place machine demo by Nathaniel
• Discussion of OpenPGP software and its use with the pick and place machine
• Overview of the machine's hardware and custom circuit board
• Cost of building the machine, with prices ranging from $1700 to the cost of individual parts
• Complexity of setting up the machine and its software, requiring many hours of work
• The TMP machine is being used to automate assembly tasks and is equipped with a vision system, vacuum, and additional lights.
• The vision system uses USB cameras with fisheye lenses to capture images and is used to track the movement of parts.
• The machine allows for on-demand production, enabling rapid prototyping and production of small boards.
• The team has used this technology to produce boards such as the Gimlet, which can be produced in large quantities for a relatively low cost.
• The ability to produce boards quickly has led to a shift in the team's approach to hardware development, with a focus on breaking down complex systems into smaller, more manageable components.
• The team has learned from experiences, such as the development of the Gemini board, which was too highly integrated and difficult to prototype.
• The team is now using a "roadkill build" approach, where components are prototyped in isolation to reduce the complexity of the final system.
• The Gemini board was a complex system with many features that made it difficult to manage and troubleshoot.
• The board was initially designed to be a slimmed-down version of a full x86 server, but even that proved to be too complicated.
• The Root of Trust was initially integrated into the board, but was later moved to a separate carrier board due to modularity issues.
• The team learned from the experience and improved their design process, allowing for quicker iteration and testing.
• The addition of full-time engineers in 2021 improved the team's ability to design and test complex systems.
• The Gemini board served as an educational experience for the team, highlighting the importance of modularity and integrability.
• The conversation discusses the challenges of the electronic supply chain disruption, specifically in regard to obtaining connectors and ICs.
• The team had to redesign the Gemini board repeatedly and eventually made their own custom solutions, including hand-soldering and modifying boards.
• The custom board was a "right-angle" board with a power connector, which was a crucial component for powering up the Gemini board.
• The team used a combination of in-house assembly and outsourcing to various assembly houses, depending on the complexity and quantity of the boards.
• The conversation highlights the importance of having flexibility and agility in the design and assembly process, particularly in times of supply chain disruption.
• The team also discusses the use of pick-and-place machines, which allows for more complex designs to be assembled in-house.
• The Spur board was designed to prototype a multiplexer circuit for sharing a flash part between an ARM processor and an AMD processor.
• The board was also used to test and understand the analog challenges of sharing a SPY/Quads Flash part.
• The designers wanted to explore different alternatives for implementing a specific feature and needed a quick and cost-effective way to prototype and test it.
• The Spur board was built in-house using KiCad and allowed the designers to test and understand the circuit's behaviour.
• The board was able to switch between the ARM and AMD processors at 33 MHz and could boot the x86 machine through the mix.
• The Spur board saved the team a significant amount of time and effort by allowing them to test and validate the circuit before moving to a full board spin.
• The Gimlet Let board was mentioned as a later design that benefited from the knowledge gained from the Spur board.
• The Gimlet board is a versatile and widely used device in the lab, with its photo showing the board's components and functionality.
• The board was designed to be a Swiss Army knife of sorts, with a multitude of interfaces and a simple pinout.
• The Gimlet's LEDs are used for communication and status purposes, with a specific flashing sequence for power supply controllers.
• Standard connectors and pinouts were used, making it easy to use and adapt the board to different projects.
• The board is connected to various devices and boards, including the Renaissance power evil boards and the 100 amp demo board from LTC.
• The P Mod connector is a standard interface that brings out primitive buses, making it easy to experiment and connect different components.
• The Gimlet board is a useful building block, allowing for a lot of work to be done on the operating system without peripherals.
• Discussing the Gimlet board and its functionality
• Explaining the NIC board and its purpose
• Describing the challenges of finding a suitable microcontroller
• Sharing experiences with microcontroller searching and navigating vendor websites
• Introducing the Gimlet board and its purpose
• Discussing the genesis of the Gimlet board and its role in solving a specific problem
• Discussing the desire for a board that can speak I2C to a DIMM's SPD chip
• Expressing surprise that such a board did not exist
• Use of DDR 4 Simms on a custom circuit with only 10 pins soldered, and the rest for mechanical stability
• The importance of the I2C bus translator and its rules about voltage relationships
• The use of the Dimwit board and its portability and ease of use
• The ability to prototype and test software ahead of time, thanks to the Dimwit board
• The challenges of working with I2C bus and the importance of accurate documentation
• The use of KiCad for design and the benefits of high-quality tools for PCB design
• The growth and development of KiCad and its potential to handle complex designs
• Discussion about KiCad and its comparison to Eagle
• Universally available design tools and their benefits
• Using KiCad for small board designs and transitioning to it for all boards
• Workflow and layout efficiency in KiCad
• Design of the gimbals and its regulators
• Breakout boards and adapters for Sam tech connectors
• Use of dongles and headers for I squared C buses and signal breakout
• Standardization of headers for easy analyzer connection
• Discussion of various components and tools, including Sale A two and Sur Cap
• Discussion of the GIMLET hardware and its various components, including the ICE 40 FPGA and MOD connectors
• Explanation of the ignition network and its role in power control
• Show and tell of various GIMLET-related boards and hardware, including the GIMLET carrier and the VSC 7448 network switch dev kit
• Mention of the importance of a development vehicle for the GIMLET hardware
• Discussion of a custom-made ribbon cable breakout for the GIMLET hardware
• Discussion of a ribbon cable with 40 conductors
• Mention of a breakout board
• Ada fruit's IDC cables for smaller pin count
• Using patient cables and chewing on them
• Kludge.2, its origin, and purpose
• Difficulty programming m.2 SSDs in SLED network
• Exploration of various solutions, including adapters and USB dongles
• Design and creation of an extender to extend PCIe out the front of the SLED
• Use of an Intel NIC as a useful computer interface
• Mechanical design issues with the extender, including a nibbler being used to modify the sled's design
• Discussion of a project that initially worked but had a refined version
• Importance of hot plugging and a safe interface
• Explanation of the Peugeot 2 and its functionality
• Discussion of a hubris system with a small processor (Cortex M0) and limited RAM (8k or 64k)
• Porting of code to the new processor
• Explanation of the Dong wet board and its functionality
• Discussion of the VPD board and its interface with the Dong wet board
• Explanation of the need for a new board (Dongle) due to shortage of original processor
• Discussion of the features of the Dongle board, including a regulator, USB connector, and SPI connector.
• VPD boards and programming using hubris and humility software
• Development of targeted hardware for VPD programming
• Manufacturing process and use of custom software and hardware
• Discussion of the importance of writing own manufacturing software
• Reusable parts and general-purpose firmware in manufacturing
• Customization of off-the-shelf components for testing (e.g. QSFP loop back module)
• Regulatory testing and thermal management challenges
• Temperature sensors and thermal management issues with certain components
• Development of synthetic load boards for DDR DIMM testing
• Creation of a 3D printed power adapter for Oxide's sled
• Discussion of tools development and the need for in-house load generation and testing
• Refinement of the Kludge Shot 2 design with improved mechanical and electrical components
• Development of the Flowchart 2 and its features
• Benefits of having Ethernet ports and IO interfaces on the manufacturing line
• Discussion of the "Swiss army knife effect" of the Gimme Whit let
• Role of in-house pick and place and its benefits
• Culture of prototyping and idea generation within the team
• Speed and ease of design cycles for new boards
• Collaboration and teamwork facilitated by rapid prototyping
• Potential for sharing designs with the community and open-sourcing them
• Reflection on the success of the team's rapid prototyping efforts
• End of meeting