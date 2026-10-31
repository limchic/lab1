from __future__ import annotations
from .enchantment import FOR_ARMOR, Enchantment
from .item import Item
MAX_DEFENSE = 0.75
class Armor(Item):
    def __init__(self, code: str, name: str, base_price: int, defense: float) -> None:
        super().__init__(code, name, base_price)
        self._defense = defense
    @property
    def defense(self) -> float:
        total = self._defense + sum(e.bonus_defense for e in self.enchantments)
        return min(total, MAX_DEFENSE)
    @property
    def possible_enchantments(self) -> tuple[Enchantment, ...]: return FOR_ARMOR
    @property
    def description(self) -> str: return f"защита {round(self.defense * 100)}%"