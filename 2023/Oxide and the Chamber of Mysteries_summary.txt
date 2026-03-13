• Discussion of compliance and regulatory requirements for electromagnetic compatibility (EMC)
• Circumventing EMC compliance in data centers, specifically the approach taken by Facebook
• Site testing and measurement of emissions in data centers
• Comparison of regulatory approaches between the US and Europe
• Historical examples of interference and its consequences (e.g. USS Forrestal, blender-TV interference)
• Importance of EMC compliance for preventing hazardous behavior in electronic devices
• Pre-compliance testing was done in June 2020 in Texas
• Complexity of electromagnetic compatibility (EMC) and high-frequency interactions in large systems
• Limitations of simulation and software in accurately predicting EMC issues
• Importance of physical testing in anechoic chambers (SACs) to measure device emissions in isolation
• Description of an anechoic chamber, its purpose, and how it simulates device performance in a quiet environment
• Discussion of cascading failures and the energy involved in complex systems
• The concept of EMF testing and compliance
• The experience of EMF testing in a Texas facility
• The challenges of integrating EMF testing with product development
• The discovery of issues with off-the-shelf power shelves and rectifiers
• The complexity and difficulty of designing and building a custom rectifier
• The realization that it is not feasible to design and build a custom rectifier in-house
• Discussing a test report from Murata that seemed suspicious
• Evaluating test reports from various test houses, including TUV, Intertek, and UL
• Realizing that the test was flawed and not accurately representing the product's emissions
• Understanding that components that are individually FCC compliant can still cause issues when combined
• Recognizing the need for a higher standard of compliance at the system integrator level
• Learning from the experience and becoming better prepared for future testing and compliance
• Sharing lessons learned, including the importance of properly wiring and cabling equipment
• Ethernet ports and limitations in a specific system
• Pre-compliance testing and its benefits
• Debugging process and challenges
• Test facilities and setup
• Faraday cages and shielding
• Logistics and operations of compliance
• Team and individual contributions and experiences
• Discussion of Franklin's brisket and Pepe's pizza in Austin
• Chambers for testing as a finite resource that's hard to book
• Compliance runs and the importance of team's efforts in getting everything ready
• A hardware issue with shark fin connectors that caused problems
• A manufacturing error that caused identical parts to have different logic functions
• Discussion of process problems in detecting and preventing such errors
• Discussion of a production issue where a wrong part was used in a system, leading to a shutdown
• Use of barcodes and scanning to track and identify parts, and how this helped in resolving the issue
• Mention of the "shark fin" part and the need to disassemble and rework hundreds of units
• Reference to the importance of compliance and the team's efforts to prepare for it
• Account of a subsequent test where the system failed to power on and had a fire hazard
• Mention of the compliance being canceled due to the test failure
• The speaker discusses a recent incident where a critical component failed, causing a problem with the rack.
• The team performed extensive testing, including 100-150 power cycles, to try to reproduce the issue.
• The hypothesis is that the components were damaged during programming on the bench, not during the initial power-up.
• The team made process changes to ensure more information is gathered in case of future failures.
• They are having 14 components decapped to understand the damage.
• The incident was a learning experience, and the team gained insights into how the rack powers on and how to troubleshoot issues.
• The team was able to reproduce the failure on the bench, but not in the rack, suggesting a design issue is unlikely.
• The incident led to heroic efforts to schedule a chamber in January to conduct further testing.
• Discussion of a delayed pickup of a large item and its dimensions
• Description of a testing facility and a "panel" with a giant matrix switch of power sources
• Results of electromagnetic compatibility (EMC) testing, including low frequency emissions and clock signals
• Discussion of a 6187.5 megahertz outlier and its potential harmonic source
• Manipulation of the testing equipment to identify and mitigate electromagnetic interference (EMI) issues
• Rear door being used as an antenna and causing issues with frequency resonance
• Importance of grounding and EMC compliance in electronics design
• Use of copper tape and gaskets to improve connections and reduce noise
• The purpose of springy fingers on drive bays for EMC compliance and ESD protection
• Methods of addressing EMC issues, including using an angle grinder to grind off paint and improve grounding
• Challenges and limitations of addressing EMC issues, including cost and complexity
• The need for careful testing and iteration to achieve EMC compliance
• Measuring signal strength at different points on a rack
• Determining that 2 meters high is the strongest point for signal strength
• Understanding the effects of electromagnetic waves on a 3D model
• Exploring the concept of spread spectrum clocking (SSC)
• How SSC reduces energy in a specific frequency range and makes it less likely to interfere with other devices
• Implementing SSC in a system and its effects on emissions and interference
• Debugging issues with SSC on specific components (SharkVid issue)
• SLEDs (Sensitive Line Equipment Devices) and SSC (Switch-Selector-Controller) need to be computed and understood for emissions reduction
• Exploration of the device with the door in a chamber, including testing of various systems and components
• Understanding the behavior of individual systems and how they combine, with some components requiring physical work to test
• Ensuring safety compliance and testing exposed services and ESD (Electrostatic Discharge) protection
• Safety testing, including tip testing, whip testing, and drop testing of the device with a calibrated doorknob
• Thermal testing to ensure the device does not overheat and cause bodily harm in the event of fan blockage
• Ensuring the device can operate safely and without significant redesign
• Testing of rack's cooling system with fans running up to 12 ks RPM
• Blocking air intakes to see how rack performs in a hot environment
• Testing with cardboard blocks to trap hot air in the rack
• Discussion of safety compliance and testing standards
• Review of rack's performance and heat output
• Changes made to pass safety compliance, including grounding and gasketing modifications
• Discussion of frequency range for testing (1 GHz to 8 GHz)
• Limitations of the 5th harmonic assumption in electromagnetic compatibility (EMC) testing
• Challenges of EMC testing at high frequencies (1-8 GHz)
• Issues with PCIe and spread spectrum signals causing interference
• Difficulty in passing EMC testing with a large system (32 individual components)
• Benefits of individually testing components in a rack system
• Challenges of testing complex systems with many interacting components
• The importance of realistic testing scenarios to ensure system reliability and safety
• Discussing a computer's physical condition after being moved and used in a chamber
• Software issues and reliability testing in the EMC Chamber
• Compliance and regulatory requirements for selling the product
• The process of fixing the computer after it malfunctioned
• The challenges of building a rack-scale computer
• Anticipating improvements for future projects
• Plans for shipping the product once compliance is achieved
• Discussion of FCC compliance for consumer products
• Reference to a defendant and defending a "point 0 8 d b"
• Mention of a TV product with an FCC sticker and its features
• Discussion of average performance of consumer products
• Clarification of points on barbecue recommendations (specifically, Franklin's brisket)
• Acknowledgment of CJ's contributions to the project, including pre-compliance and compliance efforts
• Praise for team members, including Steve and Matt Keeter