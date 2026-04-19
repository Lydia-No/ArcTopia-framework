from dataclasses import replace

from realerts.integrity import enforce_invariants
from realerts.ledger import EventType
from realerts.state_vector import (
    StateVector,
    VerificationState,
    ObligationState,
    LineageState,
    AuthorityState,
    ImpactState,
)


class TransitionEngine:
    @staticmethod
    def apply_event(state: StateVector, event_type: EventType) -> StateVector:
        new_state = state

        if event_type == EventType.VERIFICATION_APPROVED:
            new_state = replace(new_state, verification=VerificationState.VERIFIED)

        elif event_type == EventType.OBLIGATION_FULFILLED:
            new_state = replace(new_state, obligation=ObligationState.FULFILLED)

        elif event_type == EventType.OBLIGATION_OVERDUE:
            new_state = replace(new_state, obligation=ObligationState.OVERDUE)

        elif event_type == EventType.LINEAGE_BREAK:
            new_state = replace(new_state, lineage=LineageState.BROKEN)

        elif event_type == EventType.IMPACT_ASSESSED:
            new_state = replace(new_state, impact=ImpactState.ASSESSED)

        elif event_type == EventType.AUTHORITY_REVOKED:
            new_state = replace(new_state, authority=AuthorityState.DISPUTED)

        return enforce_invariants(new_state)
