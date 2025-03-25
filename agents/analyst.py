# agents/analyst.py
import pandas as pd
import matplotlib.pyplot as plt
from langchain.tools import tool
from pydantic import BaseModel, Field

class AnalystInput(BaseModel):
    data: str = Field(description="Raw text data (e.g., CSV/TSV)")
    query: str = Field(description="Original research topic")

class AnalystTools:
    @tool("Data Analysis", args_schema=AnalystInput)
    def analyze_data(data: str, query: str) -> dict:
        """Analyzes raw data and returns insights + original query."""
        try:
            # Process data (example)
            df = pd.DataFrame([x.split(",") for x in data.split("\n") if x.strip()])
            summary = df.describe().to_markdown()
            plt.hist(df[0])
            plt.savefig("data/histogram.png")
            
            return {
                "insights": f"Summary:\n{summary}\nChart: histogram.png",
                "query": query  # Pass query to the Writer Agent
            }
        except Exception as e:
            return {"insights": f"Error: {str(e)}", "query": query}