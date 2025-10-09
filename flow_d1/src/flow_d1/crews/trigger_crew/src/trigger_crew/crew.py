from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path
import json

@CrewBase
class TriggerCrew():
    """TriggerCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def trigger_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['trigger_agent'], 
            verbose=True
        )

    @task
    def semantic_to_triggers(self) -> Task:
        return Task(
            config=self.tasks_config['semantic_to_triggers'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TriggerCrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )

# Test case (commented out to avoid execution issues)
"""
json_path = Path("flow_d1/src/flow_d1/crews/trigger_crew/src/trigger_crew/dream_semantic.json")
semantic_json = json_path.read_text(encoding="utf-8")  

guidelines_path = Path("flow_d1/src/flow_d1/crews/trigger_crew/src/trigger_crew/guidelines.md")
guidelines_text = guidelines_path.read_text(encoding="utf-8")

dream_text = '''
I was running through a ruined city at night. The sound of explosions echoed in the distance, 
and the sky kept flashing red from the blasts. I ducked into a broken building, but inside I could hear 
people crying and someone calling for help. I tried to move toward the voice, but the floor collapsed 
under me, and I was trapped in the rubble. My chest felt heavy, and I couldn't breathe. Suddenly, I saw 
soldiers with rifles moving past me, their boots pounding on the ground. I wanted to shout, but no sound 
came out. Then, I woke up shaking and drenched in sweat.
'''

# run crew with required inputs
result = TriggerCrew().crew().kickoff(
    inputs={
        "guidelines": guidelines_text,
        "dream_text": dream_text,
        "semantic_json": semantic_json
    }
)

print(result)  # if it's CrewOutput, use .raw to extract text/JSON
"""
