class AttractorDetector:

    def detect_cycle(self, history):
        if len(history) < 6:
            return None

        last = history[-1]

        for i in range(len(history)-2):
            if history[i] == last:
                return len(history) - i - 1

        return None
