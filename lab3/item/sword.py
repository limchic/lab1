from ..combat.hit import Hit
from .weapon import Weapon
class Sword(Weapon):
    def roll_damage(self) -> Hit: return Hit(self.damage, False)
    @property
    def description(self) -> str: return f"урон {self.damage}"