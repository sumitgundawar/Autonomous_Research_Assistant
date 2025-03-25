# Updated agents/researcher.py
from langchain_community.document_loaders import ArxivLoader
from pydantic import BaseModel, Field
from langchain.tools import tool

class ArxivInput(BaseModel):
    query: str = Field(description="Search query for arXiv papers")
    max_results: int = Field(default=3, description="Max number of results")

class ResearcherTools:
    @tool("arXiv Search", args_schema=ArxivInput)  # <-- Corrected decorator
    def search_arxiv(query: str, max_results: int = 3) -> str:
        """Fetch arXiv paper summaries (no PDFs)."""
        try:
            loader = ArxivLoader(query=query, max_results=max_results, load_all_available_meta=True)
            docs = loader.load()
            return "\n\n".join([
                f"Title: {doc.metadata['Title']}\nSummary: {doc.metadata['Summary']}"
                for doc in docs
            ])
        except Exception as e:
            return f"arXiv API Error: {str(e)}"