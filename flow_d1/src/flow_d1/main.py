#!/usr/bin/env python
from ast import Pass
from random import randint
import json
from pydantic import BaseModel, Field
from typing import List, Optional
from crewai.flow import Flow, listen, start
import os
from crews.semantic_crew.semantic_crew import SemanticCrew
from crews.trigger_crew.src.trigger_crew.crew import TriggerCrew  
from crews.report_crew.src.report_crew.crew import ReportCrew

from pathlib import Path

# Define Flow State
class SemanticRepresentation(BaseModel):
    event_type: str = ""
    context: str = ""
    symptoms: List[str] = []
    specific_events: List[str] = []

class SemanticOutput(BaseModel):
    semantic_representation: SemanticRepresentation

class DreamSemanticState(BaseModel):
    dream_text: str = ""
    guidelines: str = ""
    semantic_result: Optional[SemanticOutput] = None
    triggers_result: Optional[dict] = None   # ✅ add triggers field
    report_markdown: str = ""

# Define Flow
class DreamSemanticFlow(Flow[DreamSemanticState]):
    """Flow for converting dream descriptions into semantic + PTSD trigger mapping"""

    @start()
    def get_dream_input(self):
        """Get dream description + guidelines text from state"""
        print("\n=== Dream Semantic Flow ===\n")

        # Use dream_text already set in state
        dream_text = self.state.dream_text  
        self.state.dream_text = dream_text

        #guidelines_path = Path("flow_d1/src/flow_d1/guidelines.md")
        guidelines_path = Path(__file__).parent / "guidelines.md"
        guidelines_text = guidelines_path.read_text(encoding="utf-8")
        self.state.guidelines = guidelines_text

        print("\nDream input received. Running semantic crew...\n")
        return self.state

    @listen(get_dream_input)
    def run_semantic_crew(self, state: DreamSemanticState):
        """Run the SemanticCrew with dream_text + guidelines"""
        result = SemanticCrew().crew().kickoff(
            inputs={
                "dream_text": state.dream_text,
                "guidelines": state.guidelines,
            }
        )

        parsed = json.loads(result.raw)
        state.semantic_result = SemanticOutput(**parsed)
        
        os.makedirs("output", exist_ok=True)
        semantic_path = Path("output/dream_semantic.json")
        with semantic_path.open("w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2, ensure_ascii=False)

        print("✅ Semantic representation saved to output/dream_semantic.json")
        return state

    @listen(run_semantic_crew)
    def run_trigger_crew(self, state: DreamSemanticState):
        """Run the TriggerCrew with dream_text + semantic_json + guidelines"""
        semantic_path = Path("output/dream_semantic.json")
        semantic_json = semantic_path.read_text(encoding="utf-8")

        result = TriggerCrew().crew().kickoff(
            inputs={
                "dream_text": state.dream_text,
                "guidelines": state.guidelines,
                "semantic_json": semantic_json,
            }
        )

        triggers = json.loads(result.raw)
        state.triggers_result = triggers

        trigger_path = Path("output/dream_triggers.json")
        with trigger_path.open("w", encoding="utf-8") as f:
            json.dump(triggers, f, indent=2, ensure_ascii=False)

        print("✅ PTSD triggers saved to output/dream_triggers.json")
        return state

    @listen(run_trigger_crew)
    def run_report_crew(self, state: DreamSemanticState):
        print("__ -- writing the report -- __")
        semantic_path = Path("output/dream_semantic.json")
        semantic_json = semantic_path.read_text(encoding="utf-8")

        trigger_path = Path("output/dream_triggers.json")
        trigger_json = trigger_path.read_text(encoding="utf-8")

        result = ReportCrew().crew().kickoff(
            inputs={
                "semantic": semantic_json,
                "trigger": trigger_json
            }
        )

        # Save report in state + file
        state.report_markdown = result.raw  
        report_path = Path("output/dream_report.md")
        report_path.write_text(state.report_markdown, encoding="utf-8")

        print("✅ Report saved to output/dream_report.md")
        return state


def kickoff(dream_text):
    dream_flow = DreamSemanticFlow()
    dream_flow.kickoff(dream_text = dream_text)


def plot():
    dream_flow = DreamSemanticFlow()
    dream_flow.plot()


if __name__ == "__main__":
    # For testing - you can provide a sample dream text
    sample_dream = "I was running through a dark forest, chased by something I couldn't see. I felt terrified and couldn't find my way out."
    kickoff(sample_dream)
