# app/main.py (updated)
import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.orchestration import Orchestrator
from evaluation.quality_check import ReportEvaluator

st.set_page_config(page_title="Autonomous Research Assistant")
orchestrator = Orchestrator()
evaluator = ReportEvaluator()

query = st.text_input("Research topic (e.g., 'AI in climate modeling'):")
if query:
    with st.spinner("Generating report..."):
        report = orchestrator.run_pipeline(query)
        st.subheader("Final Report")
        st.markdown(report)
        
        st.subheader("Evaluation")
        scores = evaluator.evaluate(report)
        st.json(scores)