from __future__ import annotations
from dataclasses import dataclass
from .combatant import Combatant

@dataclass(frozen=True)
class Participant:
    code: str
    name: str
    max_health: int

    @staticmethod
    def of(combatant: Combatant) -> "Participant":
        return Participant(combatant.code, combatant.name, combatant.max_health)