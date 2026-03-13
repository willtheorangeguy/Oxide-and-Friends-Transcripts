• Oxide's approach to building technology is unique and focuses on deep partnerships with suppliers
• Oxide distinguishes between partners and vendors, with partners expected to innovate and take responsibility
• Oxide values deep relationships and has a history of viewing suppliers and customers as partners, as seen at Sun
• Oxide was initially looking for a supplier for a specific component, but ultimately found a partner in Sam tech
• The challenge was to connect the QSFP ports to the ASIC, with a long PCB potentially causing signal integrity issues
• The flyover cable system from NewTek was identified as a solution to this problem, allowing for shorter cabling and improved performance
• Seek solution was already available on their website
• Arden and Jonathan had not heard of Seek before
• They discovered the Seek flyover design through a video on the website
• Jonathan was impressed by the design and contacted Seek
• Sam tech shipped a cable to Jonathan quickly and without requiring an NDA
• This was a unique experience compared to other companies they had contacted
• Sam tech's approach is to support engineers and get them the parts they need to solve their problems
• This approach has generated a loyal following among engineers
• The company's philosophy is to provide not just products, but also comprehensive services to customers.
• The company's "sudden service" has evolved to include signal integrity analysis, cable management mock-ups, and thermal analysis.
• Cables are complex and require careful consideration of signal integrity, power integrity, and thermal effects.
• Designing with cables introduces a new level of complexity, requiring collaboration between electrical, mechanical, and manufacturing engineers.
• The traditional approach to designing with cables is inadequate for modern systems, and a more holistic approach is needed.
• Manufacturing a complex cable system requires careful planning and coordination between design, mechanical, and manufacturing teams.
• Discussing a design approach that simplifies a switch design by not using a traditional backplate PCB
• Exploring benefits of this design approach, including reduced design effort and cost savings
• Comparing this design to a traditional switch design, highlighting limitations of traditional designs with high-speed interfaces
• Mentioning an advantage of starting with a "clean sheet of paper" to design a system, citing the development of Flash storage technology as an example
• Discussing the thermal challenges of traditional switch designs with high-speed interfaces and heat loads from QSFP interfaces
• Designing the QSFP board separately from the main board allowed for a more manageable and modular design process.
• The QSFP board was more complex than expected, with 2,500 components and requiring a month or more to design and complete.
• The use of flyover cables enabled a cleaner and more flexible design, allowing for easy reconfiguration of the QSFP board in different configurations.
• The QSFP board can be reconfigured to support different port configurations, such as 32 ports of 200-gig or 16 ports of 400-gig, with minimal effort.
• The design of the flyover cables and pinout allows for future variations of the QSFP board, including support for SFPD modules or other form factors.
• The use of a GPS module on the QSFP board could provide precise timing for certain network applications.
• The modular design enabled by flyover cables allows for compartmentalized problem-solving and minimizes engineering effort for future variations of the switch chassis.
• Initial consideration of Sam tech was not primary, with plans to use it for flyover cables but seek another vendor for cable backplate
• A vendor was already being worked with, and attempts to transition them from vendor to partner were unsuccessful
• Delays in receiving drawings for backplate cables with XMX connectors
• Concerns about second-sourcing XMX connectors from the vendor
• Comparison between advertised and actual capabilities of connector and cable manufacturers
• Initial reluctance to switch to Sam Tuck due to concerns about time and potential for pitting companies against each other
• Jonathan's involvement led to Sam Tuck catching up and eventually delivering drawings before the other vendor
• Frustration with the original vendor due to slow response times and difficulty in communication
• Benefits of working with Sam Tuck, including a smaller number of involved people and efficient communication
• Comparison to the original vendor, with a focus on the importance of treating the project like it's one's own system.
• Jonathan was described as treating a system as something built together with the company, showing attention to detail and empathy.
• The company was behind schedule with a critical project but quickly caught up with Jonathan's help.
• A no-brainer decision was made to work with Jonathan and the company because of their partnership and care for the company's problems.
• The partnership has been successful, and other companies have benefited from it, such as RFK who wanted to be part of the conversation.
• The company and Oxide have a good partnership, and Oxide does a good job in buying cables from the company.
• The company and Oxide have an open discussion about design, production, and cable layout, which helps facilitate a good working relationship.
• The company appreciates Jonathan's help in making sure the design is optimized and accommodates their production needs.
• A specific example of good bends versus bad bends in cables was discussed.
• Twin cable construction and importance of bending centre conductors together
• Signal integrity issues caused by poor bending practices
• Effects of differential pairs and P and N skew on signal quality
• Importance of minimizing signal losses and having sufficient margins
• Description of a specific issue with damaged solder joints in cables due to stress
• Discussion of collaboration between Sam tech and Benchmark to resolve the issue
• Discussing a manufacturing facility in Rochester, Minnesota, and how the timing of a project worked out
• Mentioning the company's decision to have manufacturing onshore in the US, rather than overseas
• Comparing the costs of onshore and offshore manufacturing
• Discussing the benefits of onshore manufacturing, including reduced travel time and easier access to facilities
• Noting that designing products in a modular fashion can make onshore manufacturing competitive
• Discussing the company's engineering presence in Rochester, Minnesota, and how it has allowed for more efficient communication and collaboration
• Travelling to a manufacturing facility for a short period is not feasible due to extra overhead and strain on the team.
• Investigation of damaged cables revealed a cracked solder joint due to excessive handling and stress.
• The speaker appreciated Jonathan's ability to quickly and effectively diagnose the issue.
• The team's disposition was refreshing in that they accepted responsibility for the faulty component and worked together to understand and resolve the issue.
• The use of shared physics and problem-solving approaches was beneficial in resolving the issue.
• The collaborative effort between three different companies was successful in resolving the issue in a timely manner.
• Collaboration and communication are key to building successful partnerships
• Companies that prioritize customer success and technical understanding tend to be more successful
• Some companies may not intentionally hinder customer success, but may lack the structure or knowledge to facilitate it
• Collaboration and communication can be hindered by politics and the complexity of multiple stakeholders involved
• Prioritizing customer success and technical understanding can lead to better outcomes for all parties involved
• Difficulty in getting customer feedback and understanding from other companies
• Importance of having a single point of contact and understanding customer needs
• Need for companies to take responsibility for their own decisions and consequences
• Importance of listening to and understanding customer problems and concerns
• Value of having a customer support approach that involves walking with the customer through their problem
• Difficulty in getting detailed customer feedback and understanding due to lack of technical expertise in customer support teams
• Discussion about Bigness's role as a technologist and his involvement in detailed conversations
• Importance of understanding the mechanical and electrical aspects of cabled backplates
• Concerns about potential failures of cable systems and the need for accurate design decisions
• Explanation of XMX connectors and their counter-opposing fingers that provide tension
• Importance of testing and verifying mechanical solutions to ensure design accuracy
• Discussion about the limitations of PCB material for backplate design and the need for a cabled solution
• Mention of considering a fibre optic link as a future option
• Debate about the limitations of copper and the potential for future advancements
• The product in question has 64 differential pairs in a half-inch by half-inch footprint, consisting of 32 TX and 32 RX.
• Copper is still the preferred method for building systems, despite some thinking optics are the right way to do it.
• Customers prefer front-panel optics if possible, but this also leads to temperature-related issues with sensitive optics.
• Copper cables can withstand higher temperatures than silicon and are a more reliable option.
• Power consumption is a significant factor, as optical conversion can be power-intensive.
• Integrated photonics on the chaplet or package can potentially change the power consumption equation.
• Blinding mating optical links could be a challenge, but not impossible.
• Thermal monitoring on QSFP ports is a concern, especially given the potential high power consumption.
• Lasers are power-hungry and staying in copper has thermal and mechanical advantages
• Converting directly from the package saves loss
• Next-generation cables (Twin Air) have a dielectric with air voids, reducing loss by 20%
• This reduction in loss has significant ramifications for power and signal integrity
• As receivers improve, they become more complex and require more silicon, driving the need for chaplets
• Further improvements in interfaces could enable even more complex systems
• Discussing the impact of higher data rates on longer cable lengths
• Pairing the longest cables with the shortest traces on print circuit boards to conserve margin
• Hesitation to consider 112 gig link due to lack of modelling
• Importance of blind mate interfaces and consistency in manufacturing
• Silicon Photonics being "one year away from mainstream" for a decade
• Discussion on chaplets and photonics technology integration challenges
• Frustration with manufacturers dangling photonics as a solution every time
• Intel's repeated disappointment in not delivering Silicon Photonics solutions
• Discussing Arian's potential and enthusiasm for Silicon Photonics
• Concerns about Silicon Photonics being a "heartbreaker" due to technical limitations
• Possession of a Silicon Photonics sample and plans to send it to Arian
• Importance of integrating Silicon Photonics with package on package (Pop) technology
• Need for switching silicon, potentially through partnership with Santa
• Comparison of DNA (company culture) between Santa and another company (Oxide)
• Partnership between these two companies and their potential for collaboration
• Discussion of co-packaged photonics and partnerships with major chipmakers
• Discussion about the challenges of getting three companies to work together, particularly with large companies that have multiple roles in the industry.
• Mention of the complexity of ASIC design and development, which has traditionally happened in isolation.
• Explanation of how the current situation requires coordination and planning between multiple stakeholders, including ASIC designers, package designers, and system integrators.
• Discussion of the potential for partnerships and collaborations to slow down or fail due to complexity and coordination issues.
• Comparison of the company's approach to the industry standard, with the company defining its own form factor and architecture.
• Praise for the company's innovative approach and willingness to challenge traditional norms.
• Partnership between the company and Sam tech oxide
• Appreciation for Jonathan's efforts in finding the partnership
• Discussion of innovative work done together
• Mention of a demo room in Santa Clara and offer for a lunch and learn session
• Upcoming talk by one of the speakers on social audio
• Plans to attend the talk and engage with the audience