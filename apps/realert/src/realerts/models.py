from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Activity:
    origin: str
    material: str
    quantity: float
    id: str = str(uuid4())


@dataclass
class Evidence:
    activity_id: str
    source: str
    evidence_hash: str


@dataclass
class Assessment:
    activity_id: str
    method: str


@dataclass
class Verification:
    activity_id: str
    verifier: str
    decision: str


@dataclass
class Obligation:
    """
    Represents a governance obligation attached to an activity.
    """

    activity_id: str
    obligation_type: str
    due_date: str
    status: str = "pending"


@dataclass
class RecognitionState:
    activity_id: str
    status: str
    authority: str
