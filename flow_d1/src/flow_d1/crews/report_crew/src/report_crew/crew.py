from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ReportCrew():
    """ReportCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]   
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ReportCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator 
            tasks=self.tasks, # Automatically created by the @task decorator    
            process=Process.sequential,
            verbose=True,
        )