• Discussion of Oxide's remote work setup and Bryan Cantrill's morning routine
• Adam Leventhal's European background and its relevance to Oxide
• Joking about German listeners and airport security
• Bryan Cantrill's apology to Germany
• Oxide's open-sourced software and its benefits
• Discussion of "Requests for Discussion" (RFPs) and their importance to Oxide
• Adam Leventhal's "big reveal" of the topic, which is the RFP mechanism and its role in Oxide's decision-making process
• Ben, Augustus, and Dave Crespo's work is discussed and highlighted
• The history of the work is touched upon, with Bryan mentioning that it started as "nice" and "great" and evolved into something more profound
• The RFT process is mentioned, with Bryan stating it was written in August 2019, one of the company's earliest documents
• The company's early days are discussed, including the garage setup and the initial lack of funding
• The PSARC process at Sun is mentioned as a precursor to the RFT process, with Bryan describing it as valuable for forcing engineers to document their ideas and identify issues
• The PSARC process is also described as time-consuming and bureaucratic, with approval or rejection being the only outcomes
• The politics of a project can be onerous and lead to wasteful efforts, but writing down ideas can be valuable
• The "August review boards" are a reference to a game from the 1980s called Battle Chess, where the VP would introduce deliberate issues to distract from the micromanaging
• Writing down ideas can be a way to force thinking about a project ahead of time and clarify complexity
• The group had previously had a bug database that was a single text file under RCS control
• The group was lacking a good way to write down ideas and projects until Alex Wilson needed a vessel for his container naming service, leading to the development of the RFT ( Rough Framework Template) system
• The RFT system was developed to help teams write down and organize their ideas and projects in a structured way, and to reduce complexity and confusion.
• Discussion on the concept of notes and the importance of encouraging timely and unpolished ideas
• Comparison of RFCs (Request for Comments) with the proposed joint RFD (Request for Discussion) format
• Inspiration from RFC 3 and its ethos of allowing for a wide range of quality and encouraging people to write down their ideas without perfection
• Discussion on the name change from RFCs to RFPs (Requests for Proposals) to avoid conflation with IETF constructs
• Retrospective on the implementation of RFPs at Joyent and experiences with the format
• Discussion on what worked well and what did not work well with the first embodiment of RFPs
• Content organization and sectioning for RFPs
• Methods of discussion and collaboration
• Use of GitHub and PRs for RFPs
• Comparison of RFP systems at Joyant and Delphix
• Importance of discoverability and searchability
• Use of Markdown and AsciiDoc for RFPs
• Challenges of rendering Markdown documents locally
• Evolution of RFP system and current goals
• Discussion of Markdown and AsciiDoc as documentation formats
• AsciiDoc's strengths and weaknesses compared to Markdown
• Robert Mustacchi's experience with AsciiDoc and its features
• Bryan Cantrill's realization about the widespread use of Markdown
• Statistics on the number of RFDs and words contributed to them
• Robert Mustacchi's prolific contribution to RFDs
• Adam Leventhal's high number of collaborators on RFDs
• Discussion of the benefits of co-authorship on RFDs
• Discussion of the volume of documentation at Oxide and the challenge of keeping up with updates
• Use of AsciiDoc as a documentation format and its benefits
• Transition from Markdown to AsciiDoc and the reasoning behind it
• Description of the GitHub repository and its use for discussion and collaboration
• Challenges and limitations of using GitHub for discussion and collaboration
• Use of branches and automation to manage RFPs and their states
• Discussion of the hiring process and the use of RFPs as part of it
• Transparency and the importance of showing the documentation to prospective employees
• RFTs (Request For Tasks) and RFDs (Request For Discussion) system and its evolution
• Initial version of RFD site and its limitations
• Pain points of searching RFTs, including no full text search and relying on manual grep searches
• Development of full text search and its impact on productivity
• Future plans to improve RFD site, including summarizing RFTs and generating reading lists for new employees
• Discussion of ASCII doc rendering on the RFD site
• Shared experiences and "aha" moments of improving the RFD site functionality
• Discussion of AsciiDoc and its use across various systems
• Challenges with using AsciiDoc, including lack of native libraries and assumptions about processing
• Development of a React renderer for AsciiDoc to improve interactivity and accessibility
• Creation of an intermediary format for AsciiDoc to improve performance and dynamic documentation
• Benefits of using AsciiDoc for documentation, including cross-linking and GitHub integration
• Discussion of oxide's engineering-driven approach and its impact on accessibility
• Introducing GitHub discussions directly into the RFD site to make it more accessible to non-technical users
• Implementing a system to associate GitHub comments with specific lines in AsciiDoc documents
• Using a front-end database to improve performance and reduce the need to fetch comments from GitHub
• Addressing issues with the GitHub API and implementing a solution to fetch comments asynchronously
• Improving user experience and making the RFP site more accessible on mobile devices
• Introducing permissioning and access control to the RFD site, allowing for more granular control over who can access specific RFPs and discussions
• Fine-grain permissions in updates
• Making individual RFTs public and sharing with customers
• RFD API and site updates, including open-sourcing
• Open-sourcing RFD site and API, with challenges and limitations
• Using the RFD API, including built-in CLI and dependencies on other oxide tools
• Augustus is the only consumer of per-gender generated CLIs that the speaker is aware of
• The RFD API makes some assumptions about the branching model and document structure
• The API is fairly coupled to the current branching model, but can be decoupled
• The API automates tasks such as generating PRs and closing out RFDs
• The goal is to make the RFD API accessible to everyone, not just engineers
• There are plans to add a user-friendly interface for creating RFDs, but not to recreate GitHub or Google Docs
• Working on internal tooling has been beneficial for the team, allowing them to get more out of GitHub.
• Discussion about using internal tooling and standardization
• Concerns about using paid services, such as Notion, and restrictions on usage
• Importance of controlling the fate of RFTs and having a Git repository with RFDs
• Versioning and integration with other tools
• Importance of owning and controlling strategic weirdness, such as RFTs
• Benefits of not using off-the-shelf tools and being able to open-source RFTs
• Discussion about conflict resolution and the role of RFTs in organizational problems
• Discussion vs. determinations in the RFP process
• Benefits of having RFPs in writing, including clarity and completeness
• Importance of considering the process vs. just publishing RFPs
• RFPs can be immutable, but can also be updated or replaced
• Value of having a published state, discussion state, and abandoned state for RFPs
• Need for clear language in RFPs and RFDs
• Linking RFDs to one another for navigation and understanding
• Development of the Gimlet hardware sled and the use of Request For Technical (RFT) documents
• Challenges of creating RFTs for Gimlet, including separating specific requirements from general guidelines
• Creation of the Cosmo RFT, which builds on existing RFTs and incorporates feedback from multiple team members
• Discussion of how RFTs can be used to document and reuse existing knowledge, and to enable onboarding and ramping up on complex topics
• Benefits of having a detailed and thorough RFT, including being able to revisit and understand previous design decisions and trade-offs
• The value of using RFTs (Request for Task) has increased over time due to increased accessibility and usage.
• The system has enabled fine-grained permissions and has become essential to Oxnard's operations.
• The collaboration and work done by a team, led by Adam, has been praised and recognized.
• There is a suggestion to adapt this system for other engineering organizations, with the original creators willing to receive feedback.
• A future plan is to conduct European-timed episodes of the show, ideally once a quarter.