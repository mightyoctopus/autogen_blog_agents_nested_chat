import autogen

class AgentManager:
    def __init__(self, config):
        self.config = config
        self.writer = self._create_writer()
        self.critic = self._create_critic()
        self.reviewers = self._create_reviewers()

    def _create_writer(self):
        return autogen.AssistantAgent(
            name="Writer",
            system_message="""
            You are a blog writer. Your role is writing an engaging blog post on given topic.
            You must polish your writing based on the feedback you receive and refine your blog post 
            to be aligned with the given feedback. One more thing that you have to make sure is that
            you have to return the pure content of your blog post without your additional comments so
            that the content is only handed off to the other agent and he further processes it without confusion.
            """,
            llm_config=self.config,
        )

    def _create_critic(self):
        return autogen.AssistantAgent(
            name="Critic",
            system_message="""
            You're a critic. You review the work of the writer and provide constructive 
            feedback to the writer so that he can refine his writing and improve the overall quality.
            """,
            llm_config=self.config
        )

    # ================ Nested Multi Agents (Nested Chat) Working Under Critic ======================#
    ### SEO, Legal, Ethics, Meta Reviewers
    def _create_reviewers(self):
        return {
            "seo": autogen.AssistantAgent(
                name="SEO_Reviewer",
                llm_config=self.config,
                system_message="""You are a professional SEO reviewer that knows the best 
                on-page SEO optimization practices. You do not only know the technical SEO practices
                but you also know what makes content more engaging to the audience. 
                Make sure your suggestion is concise and summarize your points within 3 bullet points.
                You need to begin your review, stating your role.
                """
            ),
            "legal": autogen.AssistantAgent(
                name="Legal_Reviewer",
                llm_config=self.config,
                system_message="""You are a legal reviewer known for your ability in ensuring 
                content is legally aligned and compliant. Your role is to make the content
                free from all possible legal issues. Make sure your suggestion is concise and summarize your points within 3 bullet points.
                You need to begin your review, stating your role.
                """
            ),
            "ethics": autogen.AssistantAgent(
                name="Ethics_Reviewer",
                llm_config=self.config,
                system_message="""You are an ethics reviewer and you have a great ability in
                ensuring the blog content sounds ethically correct. Make sure your suggestion is concise and summarize your points within 3 bullet points.
                You need to begin your review, stating your role.
                """
            ),

            ## Add Meta Reviewer to summarize the 3 reviewers above.
            ## Good practice to handle complex structure of agent roles and data for better precision.
            "meta": autogen.AssistantAgent(
                name="Meta_Reviewer",
                llm_config=self.config,
                system_message="""You are a meta reviewer responsible for aggregating 
                and evaluating the feedback provided by three specialized reviewers: 
                the SEO Reviewer, the Legal Reviewer, and the Ethics Reviewer. 
                As the final step in the review process, your role is to synthesize 
                their input and deliver a comprehensive, well-balanced conclusion
                """
            )
        }

