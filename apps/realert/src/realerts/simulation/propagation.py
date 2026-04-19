from realerts.state_vector import RecognitionState


def propagate_legitimacy(graph, states, resource_id):

    parent_state = states[resource_id]

    for child in graph.children(resource_id):

        child_state = states[child]

        if parent_state.recognition == RecognitionState.SUSPENDED:

            child_state = child_state.__class__(
                verification=child_state.verification,
                obligation=child_state.obligation,
                lineage=child_state.lineage,
                authority=child_state.authority,
                impact=child_state.impact,
                recognition=RecognitionState.CONDITIONAL,
            )

            states[child] = child_state

        propagate_legitimacy(graph, states, child)
