import streamlit as st
from main import DreamSemanticFlow
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv(override=True)

st.title("Identifying Hidden PTSD Triggers using Dream Descriptions")

# Text input area for dream description
dream_text = st.text_area("Enter your dream description:", height=250)

if st.button("Find Hidden Triggers"):
    if dream_text.strip():
        dream_flow = DreamSemanticFlow()

        # Inject dream_text into state before kickoff
        dream_flow.state.dream_text = dream_text  

        # Run the flow
        dream_flow.kickoff()  

        st.success("✅ Flow completed! Results saved to output/ folder.")

        # Show report if generated
        report_path = Path("output/dream_report.md")
        if report_path.exists():
            st.subheader("Comprehensive Dream Report")
            with report_path.open("r", encoding="utf-8") as f:
                report_md = f.read()
            st.markdown(report_md)
