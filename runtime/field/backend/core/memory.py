class Memory:
    def __init__(self):
        self.log = []

    def store(self, entry):
        self.log.append(entry)
        if len(self.log) > 10000:
            self.log.pop(0)
