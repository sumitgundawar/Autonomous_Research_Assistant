# agents/writer.py
from pydantic import BaseModel, Field
from langchain.tools import tool

class WriterInput(BaseModel):
    arxiv_summaries: str = Field(description="Summaries from arXiv papers")
    query: str = Field(description="Original research topic")

class WriterTools:
    @tool("Report Writer", args_schema=WriterInput)
    def generate_report(data: WriterInput) -> str:  # <-- Accept single input object
        """Generate a report using arXiv summaries and the original query."""
        return f"# Report: {data.query}\n\n## arXiv Findings\n{data.arxiv_summaries}"