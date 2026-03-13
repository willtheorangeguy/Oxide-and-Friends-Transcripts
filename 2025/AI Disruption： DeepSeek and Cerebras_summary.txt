• Discussion of the hosts and guests' interactions and banter
• The hosts' discussion of the "wedding industrial complex" and embossed invitations
• Mention of the hosts' invitation to speak and their mutual friend's upcoming wedding
• Andy's mention of being compared to Mystery Science Theater 3000 (MST3K)
• Discussion of the hosts' goal to be the "car talk of technology" (click and clack of tech)
• Comparison of the hosts' conversational tone and humor to a "journal club" version of MST3K
• Discussion of the recent attention on deep seek and the release of their R1 model
• The CDC's announcement of its 6,600 system and the contrast between the modest effort put into developing it and the vast development activities of other companies
• TJ Watson Jr.'s 1963 memo to his team explaining the CDC's press conference and the laboratory's cost-conscious, hardworking, and highly motivated effort
• The comparison of the CDC's development to the current state of deep learning and its potential for massive disruption
• The use of deep learning, specifically cerebris, which allows for open and accessible models
• The speed and responsiveness of deep learning models, such as deep seek on cerebris, which can process and respond to questions instantaneously
• The feeling of "living a thousand lives" with the rapid response time of deep learning models
• Performance of Deep Seek and comparison to Cerebrus's own models
• Discussion of the release of Lama and its impact on Cerebrus
• Comparison of Cerebrus's previous exotic hardware to more mainstream options
• Impact of open models on hardware companies and developers
• Value of hardware-software co-design, as demonstrated by Deep Seek
• Cerebris' technological innovation is the development of a wafer scale engine, the largest computer chip ever made
• The wafer scale engine is over 50 times bigger than the largest chip built before it, and is about the size of a dinner plate
• The company built the big chip to meet the specific needs of AI workloads, which require a lot of compute power, but with low precision and a high degree of sparsity
• AI workloads require a high communication bandwidth and memory bandwidth to handle data in motion
• The wafer scale engine addresses these needs with 900,000 cores, 125 petaflops of sparse FP16 compute, and all on-chip SRAM memory
• The design keeps all components on one chip to achieve orders of magnitude more communication and memory bandwidth than traditional designs.
• The size of a silicon wafer and how it relates to the size of the chip
• The concept that the square root of a circle's area is larger than the circle itself, explained through an anecdote about the speaker's mistake in a blog post
• The memory capabilities of the Cerebrus chip, specifically its 44 gigabytes of on-chip SRAM
• The speed advantages of the Cerebrus chip in processing large language models (LLMs) due to its ability to store weights in SRAM and stream them through the ALU
• The limitations of GPU architectures in processing LLMs due to memory bandwidth limitations
• Cerebrus achieves a "GPU impossible" level of performance for certain problems
• 44 GB of S-RAM is required to store weights for large models
• Models are split across multiple wafers to fit in available memory
• Memory bandwidth is not a limiting factor for inference due to minimal memory requirements between layers
• Wafer-scaled chips can be used to achieve higher performance for larger models, unlike GPUs
• Current GPU unit of memory scaling is limited by NVLink, which maxes out at 8 GPUs
• New generation of GPUs may offer higher memory scaling capabilities, but efficiency is still unknown
• Srebres' programming model is distinct from CUDA, using a custom microcode instruction set and compiler
• Instruction set is designed to meet users where they are, with integration up to ML frameworks like PyTorch
• Developing for GPUs with PyTorch is easy and familiar
• Inference developers often use APIs and don't load models directly
• The software developer ecosystem has evolved beyond CUDA
• Cerebrus allows users to run PyTorch models with ease and high performance
• A marketing claim by NVIDIA is questioned, comparing CUDA to a 10,000 year lead
• A mathematical derivation is proposed to quantify the marketing claim
• The most exciting and relevant level of abstraction in developing for GPUs is debated
• The complexity of AI development has decreased significantly, making it accessible to a wider range of developers
• The introduction of the OpenAI API and other similar services has made it easy for developers to create AI applications with minimal coding knowledge
• Large language models like LLAMA have become a dominant force in AI development, making it easier for developers to create applications with standardized units of sale and consumption
• The growth of large language models has led to a stabilization of underlying architecture and compute kernels, making it easier for hardware companies to implement new architectures
• The introduction of LLAMA has helped hardware companies like Cerebris find product market fit and compete in the market
• The speaker discusses the ability of their product to deliver tokens at high speed and low cost, making it a compelling option for users.
• The speaker compares their product to the DeepSeek project, which appeared on GitHub with no documentation and was later found to be a 100-language quine.
• The speaker draws a parallel between the DeepSeek project and the Ouroboros, a snake that eats its own tail, and notes that it is an open question how the project was created.
• The speaker references an earlier project, the Ouroboros, which was a 100-language quine and was also created by an unknown individual.
• The speaker notes that the creators of the DeepSeek project remain unknown and have not revealed how they achieved their goal.
• DeepSeek and its surprise popularity
• Training cost of AI models
• Financial implications of AI model training
• Efficient and sustainable AI computing infrastructure
• Advancements in AI model architecture, specifically mixture of experts model
• Brute force approach vs efficient learning algorithms in AI development
• Improving model efficiency without increasing size or compute cost
• New reasoning models (O1 and R1) that think and respond rather than just outputting likely answers
• The concept of "yapping" in models, where they generate multiple responses
• The trade-off between model size and inference time
• The potential for inefficiency in training large models and the benefits of thinking longer rather than pre-baking more weights
• The example of Eric Meyer's team at Meta making AI training more efficient
• The challenges and inefficiencies in the current AI development process
• The innovator's dilemma and the concept of proving the value of AI
• AI has reached a proof of concept and proof of value phase, with GPT-4 and ChatGPT being key milestones
• The need for infrastructure development to make AI more accessible and customizable
• The importance of open source in making AI capabilities more accessible to a broader range of developers
• The need for the economics of AI to change, with the benefits of the technology accruing to the user, not just the provider
• The comparison of AI to supersonic flight, which was overhyped and ultimately not economically viable
• The potential for AI to become the "flying car" of technology, with a focus on building infrastructure and making it more accessible.
• Customer-provider relationship
• Open-source vs proprietary models
• Data privacy and sovereignty concerns
• Enterprise customers' sensitivity to data usage
• Trust breakdown in third-party models
• Developer accessibility and quick model building
• Fine-tuning and pre-training models
• Open-source benefits for long-tail development
• Model development as a process similar to education
• Naveen Rao's prediction that closed AI model providers will disappear, replaced by open models via APIs
• Discussion of the commoditization of AI models, where all capabilities are on par and there's no edge in using closed models
• Implication that the value will move to the app layer, and that open source models are as good as closed ones
• Metaphor of "deadwalking" for closed models, implying they're no longer viable
• Debate about the potential for closed source models to still hold value
• Mention of Naveen Rao as a potential CEO of Intel and the humorous discussion surrounding it
• Advantages of closed-source models in AI
• Evolution of AI models and infrastructure
• Challenges for closed-source model builders
• Importance of efficiency in AI development
• Viable closed-source models for specific purposes
• Proprietary models for enterprise use cases
• R1's chain of thought and comparison to open AI models
• Discussion about the AI model "DeepSeek" and its impressive capabilities, including its ability to generate coherent and somewhat coherent chains of thought
• Comparison with OpenAI's model, which is said to hide its chain of thought patterns to prevent copying
• Reference to Cerebrus, which is mentioned as being very fast and producing a "manic" output
• Analysis of the model's behavior, likened to self-doubt and neuroticism, and comparison to a scene from Breaking Bad
• Discussion about the limitations of current infrastructure in supporting the development of highly capable reasoning models
• Reference to the "dial-up era" of generative AI, with a comparison to the evolution of the internet from dial-up to broadband
• Faster computing leads to new applications and industries, rather than just faster versions of existing ones
• Efficiency is becoming a key factor in achieving performance, particularly with limited resources
• Open weights and open-source models are on the rise, with potential benefits and motivations discussed
• The era of application developers and open-source is emerging, with a focus on efficiency and general-purpose models
• Motivations behind OpenAI's DeepSeq and Llama being open-source are discussed, including giving back to the community and commoditizing competitors
• The potential for Facebook to commoditize competitors by offering a $20/month plan is mentioned
• DeepSeek app is similar to ChatGPT and could potentially steal users and monetize later, following Facebook's classic playbook
• The app's success is strange and unexpected, especially given its reinforcement learning breakthrough
• General populace doesn't fully understand the difference between a chatbot like ChatGPT and a reasoning model like DeepSeek
• People are downloading DeepSeek to participate in the water cooler conversation and to feel included in the social media sensation
• Teenagers are particularly enthusiastic about large language models and use them frequently, but don't fully understand their capabilities
• ChatGPT being used to write next door posts to troll neighbors
• Ease of use and effectiveness of ChatGPT for trolling
• Discussing the limitations of ChatGPT and the importance of understanding its reasoning process
• Co-design of hardware with AI models to optimize performance
• Using AI to automate tasks and the potential drawbacks of relying too heavily on AI
• High-performance computing and traditional physics-based modeling and simulation
• Potential for AI to simulate complex systems and processes in high-performance computing
• Molecular dynamics simulations and their applications in drug design and material design
• Running molecular dynamics simulations on GPUs and the potential for optimization
• Collaboration with the Department of Energy to optimize Cerebris architecture for molecular dynamics simulations
• Achieving record-breaking speeds in molecular dynamics simulations, outperforming the world's fastest supercomputer
• The need for new neural network architectures optimized for wafer scale and Cerebris architecture
• The importance of low-level programming and direct hardware access for achieving exceptional results
• The advantage of coming to a problem later, having access to resources and knowledge from previous efforts
• Co-design efforts between hardware and software teams to improve efficiency
• New model architectures and learning models being explored, such as those by Liquid AI
• Open-source models and open-weight models being used to achieve efficient and groundbreaking results
• The satisfaction of seeing users achieve incredible results with tools and platforms built by the speaker's team
• The journey of building a computing platform for a specific workload and seeing it used for groundbreaking work
• Upcoming plans and future projects
• Gratitude for James joining the conversation
• DeepSeek discussion and Cerebris' work
• Appreciation for the conversation and collaboration
• Upcoming episode featuring a European-friendly topic
• Discussion of future topics, including Ratatouille