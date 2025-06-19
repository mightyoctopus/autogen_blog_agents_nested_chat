import autogen
from dotenv import load_dotenv
import os
from pprint import pprint

from agent_manager import AgentManager
from workflow_controller import WorkflowController

load_dotenv()

config_list = {
    "model": "gpt-4.1-nano",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "cache_seed": 42,
}

task = """
        Write a blog post about vibe coding. Make sure the post has a 700 word count
        and it's fact checked across appropriate resources throughout the internet.
"""

agents = AgentManager(config_list)
controller = WorkflowController(agents)

# reply = agents.writer.generate_reply(messages=[{"content": task, "role": "user"}])
# print(reply)
# pprint(chat_result.summary)

result = controller.run(task)