from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class EventType(Enum):
    EXTRACTION_RECORDED = 0
    VERIFICATION_APPROVED = 1
    OBLIGATION_FULFILLED = 2
    OBLIGATION_OVERDUE = 3
    LINEAGE_BREAK = 4
    IMPACT_ASSESSED = 5
    AUTHORITY_REVOKED = 6


@dataclass(frozen=True)
class Event:
    event_type: EventType
    resource_id: str
    timestamp: datetime
    payload: dict[str, Any] = field(default_factory=dict)


class Ledger:
    def __init__(self) -> None:
        self.events: list[Event] = []

    def append(self, event: Event) -> None:
        self.events.append(event)

    def get_events(self, resource_id: str) -> list[Event]:
        return [e for e in self.events if e.resource_id == resource_id]
