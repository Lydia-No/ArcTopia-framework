import random

class Agent:
    def __init__(self, id, field, dim=6):
        self.id = id
        self.field = field

        self.state = [random.randint(0,1) for _ in range(dim)]
        self.history = []

    def vector(self):
        return self.state

    def record(self):
        self.history.append(tuple(self.state))
        if len(self.history) > 50:
            self.history.pop(0)

    def apply_action(self, action):

        if action == "flip":
            i = random.randint(0, len(self.state)-1)
            self.state[i] = 1 - self.state[i]

        elif action == "random_jump":
            self.state = [random.randint(0,1) for _ in self.state]

        elif action == "stay":
            pass
