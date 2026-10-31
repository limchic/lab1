from ..enemy.dragon import Dragon
from ..enemy.enemy import Enemy
from ..item.default_catalog import DAWN_BLADE, DRAGONSCALE_ARMOR
from ..item.item_catalog import ItemCatalog
from .location import Location


class DragonLair(Location):

    CODE = "dragon-lair"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(DragonLair.CODE, "Логово дракона", 5, catalog)

    def _create_enemy(self) -> Enemy:
        return Dragon()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (DAWN_BLADE, DRAGONSCALE_ARMOR)