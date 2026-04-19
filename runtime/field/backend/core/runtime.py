from .intelligence import IntelligenceLayer
from .autonomous import AutonomousAgent
from .agent import Agent
from .hypercube import HypercubeField

class Runtime:
    def __init__(self,n=20):
        self.field=HypercubeField()
        self.intel=IntelligenceLayer()

        self.agents=[
            AutonomousAgent(Agent(i,self.field), self.intel)
            for i in range(n)
        ]

    def step(self):
        for a in self.agents:
            a.step(self.field)

        base=[a.base for a in self.agents]
        self.field.update(base)

    def state(self):
        return {
            "field":self.field.global_state,
            "agents":[
                {
                    "id":a.base.id,
                    "state":a.base.vector(),
                    "action":a.last_action
                } for a in self.agents
            ]
        }
