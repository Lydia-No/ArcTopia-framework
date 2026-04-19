from dataclasses import dataclass
from realerts.state_enums import (
    VerificationState,
    ObligationState,
    LineageState,
    AuthorityState,
    ImpactState,
    RecognitionState,
)


@dataclass
class StateVector:

    verification: VerificationState
    obligation: ObligationState
    lineage: LineageState
    authority: AuthorityState
    impact: ImpactState
    recognition: RecognitionState

    def copy(self):

        return StateVector(
            verification=self.verification,
            obligation=self.obligation,
            lineage=self.lineage,
            authority=self.authority,
            impact=self.impact,
            recognition=self.recognition,
        )

    @staticmethod
    def default():

        return StateVector(
            verification=VerificationState.UNVERIFIED,
            obligation=ObligationState.PENDING,
            lineage=LineageState.INTACT,
            authority=AuthorityState.RECOGNIZED,
            impact=ImpactState.UNASSESSED,
            recognition=RecognitionState.CONDITIONAL,
        )
