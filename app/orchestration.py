# app/orchestration.py
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.researcher import ResearcherTools
from agents.analyst import AnalystTools
from agents.writer import WriterTools
from agents.reviewer import ReviewerTools
from dotenv import load_dotenv

load_dotenv()

class Orchestrator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
        self.tools = self._load_tools()

    def _load_tools(self):
        researcher = ResearcherTools()
        analyst = AnalystTools()
        writer = WriterTools()
        reviewer = ReviewerTools()

        return [
            Tool.from_function(
                func=researcher.search_arxiv,
                name="arXiv Search",
                description="Fetches summaries of arXiv papers on a topic."
            ),
            Tool.from_function(
                func=WriterTools.generate_report,
                name="Report Writer",
                description="Generates report from arXiv summaries AND original query. Input MUST be: {{'arxiv_summaries': '...', 'query': '...'}}"
            ),
            Tool.from_function(
                func=reviewer.critique_report,
                name="Report Reviewer",
                description="Critiques the report for accuracy."
            )
        ]
        # return [
        #     Tool.from_function(
        #         func=researcher.search_arxiv,
        #         name="arXiv Search",
        #         description="Fetches summaries of arXiv papers on a topic."
        #     ),
        #     Tool.from_function(
        #         func=analyst.analyze_data,
        #         name="Data Analysis",
        #         description="Analyzes raw data (CSV/TSV text) and requires the original query. Input: {'data': 'raw data', 'query': 'research topic'}"
        #     ),
        #     Tool.from_function(
        #         func=writer.generate_report,
        #         name="Report Writer",
        #         description="Generates a report using insights and the original query. Input: {'insights': '...', 'query': '...'}"
        #     ),
        #     Tool.from_function(
        #         func=reviewer.critique_report,
        #         name="Report Reviewer",
        #         description="Critiques the report for accuracy."
        #     )
        # ]

    def run_pipeline(self, query: str) -> str:
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent_type="structured-chat-zero-shot-react-description",
            verbose=True
        )
        return agent.invoke({"input": query})["output"]