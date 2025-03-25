import pytest
from agents.researcher import ResearcherTools

def test_arxiv_search():
    researcher = ResearcherTools()
    # Use .invoke() with a dictionary to pass multiple args
    result = researcher.search_arxiv.invoke({"query": "transformer models", "max_results": 1})
    assert "transformer" in result.lower()