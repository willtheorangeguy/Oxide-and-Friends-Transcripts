• Conversation about doing the podcast from Oxide and experiencing direct sun exposure
• Discussion of Adam's possible use of AI-generated photo of Italy and European window dimensions
• Apology to German listeners for offending them with previous comments
• Introduction of an apology video, with the host joking about bringing back a trend
• Discussion of a "long time coming" episode, with the host expressing excitement and relief that it's happening now
• Mention of recent changes made to the product and company, including open-sourcing software
• Introduction of a topic to be discussed, but the host gets cut off and the conversation ends abruptly
• RFDs (Request for Discussion) are essential to the company and have been from its early days
• RFDs are idiosyncratic, meaning they're unique and not necessarily following standard practices
• RFDs describe the RFD process, which was first written in August 2019
• The ability to make single RFDs public has been life-changing for the company
• This ability was built on the work of Ben, Augustus, and David Crespo
• The company's early days were marked by limited resources and a focus on establishing key documents and processes
• Some of the first RFDs written were related to principles and values, hiring process, and the RFD process itself
• Discussion about the early days of RFD (Request for Documentation) process and its development
• Mention of the first commit message in October and the team's transition to a new space with heating issues
• Comparison of the oxide office's heating to the garage where the team previously worked
• Explanation of the PSARC (Platform Software Architectural Review Committee) process at Sun Microsystems
• Recollections of the PSARC process, including the development of materials for PSARC cases and the value of writing down ideas
• Critique of the PSARC process, describing it as bureaucratic and time-consuming, with approval or rejection rather than constructive feedback
• Comparison of the PSARC process to a parole board, with senior engineers acting as gatekeepers of new ideas
• Intentional creation of issues to distract from the main goal
• Using August review boards and cultural milieus to achieve goals
• The concept of the "queen's duck" and its application in business and politics
• The use of micromanagement and deliberate issue introduction in game development (Battle Chess)
• Writing down processes and avoiding informal, unwritten systems (RCS and Detroit's bug database)
• Discussion of a previous project called Peace Arc and its impact on the team
• Need for a way to write down and document ideas and processes
• Complexity of projects such as Triton and Manta requiring documentation
• Introduction of a concept based on RFCs (Request for Comments) for documenting ideas and processes
• Importance of encouraging people to write things down in a loose and flexible format
• Realization that the concept of RFCs can be applied to the team's needs
• The RFC3 document's guidelines on submitting notes, which encourage timeliness over polish, are still relevant today.
• The joint RFP repo aims to promote the exchange and discussion of ideas without the need for perfect writing or approval.
• RFCs have become more formal over time, and the joint RFP repo is a way to draw inspiration from RFCs while being something different.
• The use of RFDs (Request for Discussion) instead of RFCs (Request for Comments) helps to avoid conflation with the IETF construct and promotes a more informal approach to submitting ideas.
• Discussion of RFD (Request for Discussion) process at Joyent and how it was improved
• Experiences with RFDs at Joyant, including difficulties with discussion and feedback
• Comparison of RFD process at Joyent and at Delphix (including use of Google Docs)
• Challenges with discussion and feedback in RFD process, including lack of searchability and difficulty commenting on specific pieces
• Benefits of having a centralized repository for RFDs and discussion process
• Use of GitHub and GitHub PRs for RFDs, including challenges and pros and cons
• Desire for a Google doc frontend with ASCII doc backend and a canonical repository
• Discoverability and ease of seeing changes over time
• Use of Markdown and ASCII doc, with the speaker being the only one using Markdown
• ASCII doc features and capabilities, including linking between sections and callouts
• Limitations of Markdown, including constraints on rendering and lack of features for complex documents
• ASCII doc vs HTML rendering
• Chris's discovery of ASCII doc
• Robert's heavy contribution to RFDs (1.4 million words, 364,000 words alone)
• Discussion on measuring RFDs and author contributions
• Robert's prolific writing and collaboration with others on RFDs
• The importance of cross-pollination and co-authoring in RFDs
• The total word count of Shakespeare's works is approximately 800,000 words.
• The difficulty of reading every RFD (Request for Discussion) document produced by the company.
• The use of ASCII Doc and Markdown for documentation, with ASCII Doc being the preferred choice.
• The transition from Joint to Oxide, including the implementation of new discussion methods and the use of GitHub PRs (pull requests) for line-by-line feedback.
• The benefits of using GitHub history, including the preservation of comments and discussions, but also the challenge of finding them.
• The use of branches and automation for RFD management, including the addition of a new state called "ideation".
• Initial issues with out-of-box experience, installation, and documentation
• Use of RFDs as a collaborative space and for ideation
• Adding contributors to RFDs and using it as part of the hiring process
• Showing documentation to candidates and its impact on their interest in joining the team
• Problems with searching and sharing individual RFDs
• Origin and history of the RFD site
• The full text search feature for RFDs has been a major improvement
• Previous methods for searching RFDs were inadequate and time-consuming (e.g. Lucene grab)
• The full text search on the RFD site has been a game-changer, allowing for easy access to information
• There is still room for improvement, such as summarizing RFDs and generating reading lists for new users
• The RFD site's rendering of ASCII doc has been improved, but there are still pain points with this feature
• Use of ASCII doc on the RFD site and potential issues
• Discussion of the developer's recent experience with ASCII doc and its capabilities
• Balance between spending time on developing ASCII doc renderer and its potential use
• Explanation of how the company uses ASCII doc across multiple sites, including documentation and marketing
• Comparison of ASCII doc to Markdown and the developer's positive opinion on it
• Discussion of the limitations of ASCII doc, including the lack of native libraries for Rust and JavaScript
• React components for rendering images and interacting with attributes
• Challenging issues with rendering content with footnotes
• Intermediary format for ASCII doc processing on the server
• Dynamic documentation and reducing library size
• GitHub integration for discussions and accessibility
• Making process accessible for non-engineers in sales, operations, and design teams
• Tracing and linking lines in an ASCII doc to associated line numbers
• Querying the GitHub API to collect comments and rendering them alongside content
• Associating original documents with rendered documents and adding a sidebar for full discussion
• RFD database and revisions, pulling comments into revisions and tying comments to specific revisions
• GitHub API issues and the importance of data streaming and asynchronous rendering
• Remix framework for streaming data from the server and rendering comments asynchronously
• Mileage may vary on the actual gap between the spinner and actual content loading
• The rendered content looks great and is important for mobile users
• The previous GitHub group for friends of oxide had issues with large numbers of outside collaborators and high GitHub bills
• The team needed to model RFD access around actual permission sets
• Fine-grained permissions are game-changing for RFDs, allowing for public RFDs and easier sharing
• The new RFD API allows for public flagging and has improved access to public RFDs
• The difference between "public" and "actually public" is significant, with the latter allowing for easy sharing and access
• RFD site and API development
• Fine-grained control and group permissions
• Open-sourcing of the RFD site and API
• RFD API being more abstract and less specific to Oxide
• Challenges with open-sourcing the RFD site due to its customization and styling
• Potential for others to adapt and use the RFD site with their own branding and styling
• Discussion of the RFD (Request for Discussion) API and its features
• Pride and shame over the use of progenitor-generated CLIs
• Use of RFD COI (Content of Interest) and its auto-generated features
• Assumptions made by the RFD API, such as the use of ASCII doctor and mermaid diagrams
• Setup guide for the RFD API and its potential pain points
• Database management using Postgres and rendering RFD contents as an RFD site
• GitHub repo integration and scanning of branches for RFDs
• Coupling of the RFD API to the GitHub model and potential friction points
• The discussion is about the RFD (Request for Discussion) process on GitHub
• The current RFD model is less coupled to the branching model and more to the document structure
• Automation has made the RFD process more efficient, but can be clumsy for authors
• The goal is to make the RFD process accessible to everyone, not just engineers
• Incremental development of the RFD API and use of GitHub's platform for simplicity
• The RFD API will allow users to create RFDs from the website directly
• Working on basic authoring features, but avoiding recreating GitHub and Google Docs
• Internal tooling development has been beneficial for the team and the project
• The use of standardized tools allows for a "flywheel" effect where investments in internal tooling also benefit the product
• Concerns about using paid services like Notion due to restrictions on usage
• Importance of a Git repository for RFDs (Requests for Decision) to be the canonical location
• ASCII doc rendering is a critical element of the system
• Versioning and control over the system's fate are essential
• Owning and controlling one's own "strategic weirdness" (in this case, RFDs) is crucial
• The effort put into developing and maintaining the system has been valuable and cost-effective
• The system allows for control over usage and costs, avoiding unnecessary expenses and licensing fees
• Discussion of using GitHub less for comments and exploring alternative options
• RFDs (Requests for Discussion) as a means to resolve conflicts and facilitate discussion
• Pitfalls of RFDs, including becoming "lightning rods" and not solving organizational problems
• The importance of having written records of conflicts and discussions, even if they become heated
• Clarifying the purpose of RFDs as requests for discussion, not rehashing previously decided issues
• Exploring different methods for navigating conflicts and bringing discussion to a determination
• RFD process and determinations
• Published state vs discussion state
• RFDs can be updated or replaced
• Importance of discussion and documentation
• Published RFDs are not immutable
• Value of RFDs in determining and reviewing decisions
• Abandoned state for RFDs
• Chat RFDs may be in an abandoned state
• Importance of linking RFDs to one another
• Use of graphical representations to navigate RFDs
• RFDs for Cosmo, with a focus on reuse of existing systems and components
• Differences in approach between Gimlet and Cosmo, with Gimlet being a more initial and foundational effort
• Disk drive interface options (U.2, E3S, E1S, E1L)
• FPGA role and features
• Collaboration and different approaches to problem-solving
• Appendix on abandoned ideas and their reasoning
• Importance of written artifacts for scaling an organization and retaining knowledge
• Ramping up on complex topics (optics) and the value of having comprehensive documentation
• Value of RFDs has increased over time due to increased usage and accessibility
• Fine-grained permissions allow for targeted sharing of RFDs
• RFDs are a backbone of Oxide
• The team has done excellent work on RFDs, making them essential
• The system is adaptable and adoptable by other engineering organizations
• Future plans include doing European-timed episodes to accommodate remote work requirements