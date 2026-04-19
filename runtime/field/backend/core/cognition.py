class Cognition:
    def decide(self,agent,field):
        avg=sum(field.global_state)/len(field.global_state)

        if avg>1.2: return "stabilize"
        if avg<0.5: return "expand"
        return "explore"
