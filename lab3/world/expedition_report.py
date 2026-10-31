from dataclasses import dataclass

from ..combat.battle_report import BattleReport
from .rewards import Rewards


@dataclass(frozen=True)
class ExpeditionReport:
    seed: int
    location_code: str
    battle: BattleReport
    rewards: Rewards