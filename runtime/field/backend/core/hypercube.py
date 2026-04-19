from .math_utils import vector_add, random_vector, clamp

class HypercubeField:
    def __init__(self, d=6):
        self.dimensions = d
        self.global_state = [0.5]*d

    def update(self, agents):
        if not agents: return

        avg=[0]*self.dimensions
        for a in agents:
            vec=a.vector()
            for i in range(self.dimensions):
                avg[i]+=vec[i]

        self.global_state=[v/len(agents) for v in avg]

        drift=random_vector(self.dimensions,0.01)
        self.global_state=vector_add(self.global_state,drift)
        self.global_state=[clamp(v,0,2) for v in self.global_state]
