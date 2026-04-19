from .cognition import Cognition
from .memory import Memory
from .attractor import AttractorDetector

class IntelligenceLayer:
    def __init__(self):
        self.cognition = Cognition()
        self.memory = Memory()
        self.attractor = AttractorDetector()

    def process(self, agent, field):

        cycle = self.attractor.detect_cycle(agent.history)

        if cycle:
            action = "random_jump"   # escape attractor

        else:
            action = self.cognition.decide(agent, field)

        self.memory.store({
            "agent": agent.id,
            "action": action,
            "state": agent.state
        })

        return action
