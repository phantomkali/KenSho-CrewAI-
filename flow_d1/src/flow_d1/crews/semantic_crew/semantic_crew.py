from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path

@CrewBase
class SemanticCrew:
    """Semantic Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def semantic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["semantic_agent"],  
        )

    @task
    def dream_to_semantic(self) -> Task:
        return Task(
            config=self.tasks_config["dream_to_semantic"],  
            output_file="output.json"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True,
        )

"""# running a test case to see if it works
guidelines_path = Path("flow_d1/src/flow_d1/guidelines.md")
guidelines_text = guidelines_path.read_text(encoding="utf-8")

dream_text =
I was running through a ruined city at night. The sound of explosions echoed in the distance, 
and the sky kept flashing red from the blasts. I ducked into a broken building, but inside I could hear 
people crying and someone calling for help. I tried to move toward the voice, but the floor collapsed 
under me, and I was trapped in the rubble. My chest felt heavy, and I couldn't breathe. Suddenly, I saw 
soldiers with rifles moving past me, their boots pounding on the ground. I wanted to shout, but no sound 
came out. Then, I woke up shaking and drenched in sweat.

result = (SemanticCrew().crew().kickoff(inputs={"guidelines": guidelines_text, "dream_text": dream_text}))
print(result)
"""
