from dataclasses import dataclass
from .event_type import EventType
from .side import Side

@dataclass(frozen=True)
class BattleEvent:
    round: int
    type: EventType
    source: Side
    target: Side
    amount: int
    target_health_after: int