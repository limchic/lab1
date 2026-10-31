from __future__ import annotations
from dataclasses import dataclass
from .battle_event import BattleEvent
from .outcome import Outcome
from .participant import Participant

@dataclass(frozen=True)
class BattleReport:
    hero: Participant
    enemy: Participant
    outcome: Outcome
    events: tuple[BattleEvent, ...]