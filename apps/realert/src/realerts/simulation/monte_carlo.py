import random

from realerts.ledger import EventType
from realerts.simulation.transition_engine import TransitionEngine


class MonteCarloSimulator:

    def __init__(self, event_probabilities=None):

        if event_probabilities is None:
            event_probabilities = {
                EventType.VERIFICATION_APPROVED: 0.3,
                EventType.OBLIGATION_FULFILLED: 0.2,
                EventType.OBLIGATION_OVERDUE: 0.2,
                EventType.LINEAGE_BREAK: 0.05,
                EventType.IMPACT_ASSESSED: 0.2,
                EventType.AUTHORITY_REVOKED: 0.05,
            }

        self.event_probabilities = event_probabilities

    def random_event(self):

        events = list(self.event_probabilities.keys())
        weights = list(self.event_probabilities.values())

        return random.choices(events, weights=weights, k=1)[0]

    def run_trajectory(self, initial_state, steps=20):

        state = initial_state
        trajectory = [state]

        for _ in range(steps):

            event = self.random_event()
            state = TransitionEngine.apply_event(state, event)

            trajectory.append(state)

        return trajectory

    def run_many(self, initial_state, runs=1000):

        trajectories = []

        for _ in range(runs):
            traj = self.run_trajectory(initial_state)
            trajectories.append(traj)

        return trajectories
