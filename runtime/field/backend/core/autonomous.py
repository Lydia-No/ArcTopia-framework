class AutonomousAgent:
    def __init__(self, base, intel):
        self.base=base
        self.intel=intel
        self.last_action=None

    def step(self, field):
        action=self.intel.process(self.base, field)
        self.base.apply_action(action)
        self.last_action=action
