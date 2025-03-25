from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

class ReviewerTools:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    @tool("Report Reviewer")
    def critique_report(self, report: str) -> str:
        """Critique a report for accuracy and coherence."""
        prompt = f"""Critique this report:
        {report}
        Focus on factual errors and clarity. Be harsh!"""
        return self.llm.invoke(prompt).content