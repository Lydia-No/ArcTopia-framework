from enum import Enum


class VerificationState(Enum):
    UNVERIFIED = 0
    VERIFIED = 1
    REVOKED = 2


class ObligationState(Enum):
    PENDING = 0
    FULFILLED = 1
    OVERDUE = 2


class LineageState(Enum):
    INTACT = 0
    BROKEN = 1


class AuthorityState(Enum):
    RECOGNIZED = 0
    DISPUTED = 1


class ImpactState(Enum):
    UNASSESSED = 0
    ASSESSED = 1


class RecognitionState(Enum):
    CONDITIONAL = 0
    RECOGNIZED = 1
    SUSPENDED = 2
