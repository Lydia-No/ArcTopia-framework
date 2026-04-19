from realerts.state_enums import (
    VerificationState,
    ObligationState,
    LineageState,
    RecognitionState,
)


def enforce_rules(state):

    if state.verification != VerificationState.VERIFIED:
        state.recognition = RecognitionState.CONDITIONAL

    if state.obligation == ObligationState.OVERDUE:
        state.recognition = RecognitionState.CONDITIONAL

    if state.lineage == LineageState.BROKEN:
        state.recognition = RecognitionState.SUSPENDED

    return state
