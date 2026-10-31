from __future__ import annotations

from dataclasses import dataclass

from ..item.item import Item


@dataclass(frozen=True)
class Rewards:
    experience: int
    gold: int
    loot: Item | None
    levels_gained: int