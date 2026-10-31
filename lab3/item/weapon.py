from __future__ import annotations

from abc import abstractmethod

from ..combat.hit import Hit
from .enchantment import FOR_WEAPONS, Enchantment
from .item import Item


class Weapon(Item):

    def __init__(self, code: str, name: str, base_price: int, damage: int) -> None:
        super().__init__(code, name, base_price)
        self._damage = damage

    @abstractmethod
    def roll_damage(self) -> Hit: ...

    @property
    def damage(self) -> int:
        return self._damage + sum(enchantment.bonus_damage for enchantment in self.enchantments)

    @property
    def possible_enchantments(self) -> tuple[Enchantment, ...]:
        return FOR_WEAPONS