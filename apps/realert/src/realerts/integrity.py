from dataclasses import replace

from realerts.state_vector import (
    StateVector,
    VerificationState,
    ObligationState,
    LineageState,
    RecognitionState,
)


def enforce_invariants(state: StateVector) -> StateVector:
    new_state = state

    if new_state.verification != VerificationState.VERIFIED:
        new_state = replace(new_state, recognition=RecognitionState.CONDITIONAL)

    if new_state.obligation == ObligationState.OVERDUE:
        new_state = replace(new_state, recognition=RecognitionState.CONDITIONAL)

    if new_state.lineage == LineageState.BROKEN:
        new_state = replace(new_state, recognition=RecognitionState.SUSPENDED)

    return new_state
