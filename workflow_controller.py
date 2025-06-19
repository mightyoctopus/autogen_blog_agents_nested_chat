from agent_manager import AgentManager

class WorkflowController:
    def __init__(self, agents: AgentManager):
        self.agents = agents

    def reflection_msg(self, _, messages, *__):
        if not messages:
            return "No content to review."
        last_msg = messages[-1]['content']
        return f"Review the following content:\n\n{last_msg}"

    def build_review_chats(self):
        reviewers = self.agents.reviewers
        common = {
            "message": self.reflection_msg,
            "summary_method": "reflection_with_llm",
            "summary_args":
                {
                    "summary_prompt": """
                        Return review in JSON object only:
                        {"Reviewer": "", "Review": ""}. Reviewer should be filled with the name of your role.
                        """
                },
            "max_turns": 1
        }
        return [
            {**{"recipient": reviewers["seo"]}, **common},
            {**{"recipient": reviewers["legal"]}, **common},
            {**{"recipient": reviewers["ethics"]}, **common},
            {
                "recipient": reviewers["meta"],
                "message": "Aggregate feedback from all other reviewers and provide the final suggestions on the blog content.",
                "max_turns": 1
            }
        ]

    def run(self, task):
        self.agents.critic.register_nested_chats(
            chat_queue=self.build_review_chats(),
            trigger=self.agents.writer
        )
        return self.agents.critic.initiate_chat(
            recipient=self.agents.writer,
            message=task,
            max_turns=2,
            summary_method="last_msg"
        )