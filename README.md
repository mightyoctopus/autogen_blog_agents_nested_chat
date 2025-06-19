# Blog Writing Automation
This LLM agent app was built with Autogen and OpenAI API(GPT 4.1 Nano model)
to build an AI agentic system that automates blog writing processes.

## How The App Works
This multi-agent system is structured with 2 main agents and 4 sub-agents.
Each agent is in specialty on its role and work cohesively as a team.

## Multi Agent Structure
![Untitled Diagram.drawio (4).png](assets/Untitled%20Diagram.drawio%20%284%29.png)
1. Writer Agent: Its role is to write blog content in collaboration with Critic Agent
2. Critic Agent: Critic agent is to review the blog content and provide feedback to Writer Agent so Writer Agent ensures the best quality of its work.

And under Critic Agent, there are 4 more sub agent directly working with Critic Agent

- SEO Agent: Responsible for reviewing content and give SEO feedback
- Legal Agent: Responsible for checking possible legal issues on contents
- Ethics Agent: Checking contents and help contents best align with ethics perspective.
- Meta Agent: Aggregate all reviews and feedback from the other 3 review agents and finalize a report to the Critic Agent
  (And Critic Agent give the modification request based on compiled feedback to the Writer Agent)
## Requirements
Check the requirements.txt file for the details.