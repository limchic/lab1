from ..combat.hit import Hit
from ..core.dice import Dice
from .weapon import Weapon
CRITICAL_MULTIPLIER = 2
class Bow(Weapon):
    def __init__(self, code: str, name: str, base_price: int, damage: int, critical_chance: float) -> None:
        super().__init__(code, name, base_price, damage)
        self._critical_chance = critical_chance
    def roll_damage(self) -> Hit:
        if Dice().chance(self._critical_chance): return Hit(self.damage * CRITICAL_MULTIPLIER, True)
        return Hit(self.damage, False)
    @property
    def description(self) -> str: return f"урон {self.damage}, шанс крита {round(self._critical_chance * 100)}%"