import math
from collections import Counter


def compute_entropy(states):

    total = len(states)

    counter = Counter(states)

    entropy = 0.0

    for count in counter.values():

        p = count / total

        entropy -= p * math.log(p)

    return entropy
