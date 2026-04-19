def determine_recognition_status(state):
    """
    Determine recognition state based on governance conditions.
    """

    if state.verification != "verified":
        return "conditional"

    if state.obligation == "overdue":
        return "conditional"

    if state.lineage == "broken":
        return "suspended"

    return "recognized"


def can_recognize(state):
    """
    Check if recognition is allowed.
    """

    return state.verification == "verified"


def recognize(state):
    """
    Apply recognition rule.
    """

    state.recognition = determine_recognition_status(state)

    return state
