import json
from langchain_google_genai import ChatGoogleGenerativeAI

class ReportEvaluator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    def evaluate(self, report: str) -> dict:
        prompt = f"""Evaluate this report (1-5 scale):
        {report}
        Return JSON: {{"accuracy": score, "clarity": score, "citations": score}}"""
        response = self.llm.invoke(prompt)
        return json.loads(response.content)