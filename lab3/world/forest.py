from ..enemy.enemy import Enemy
from ..enemy.goblin import Goblin
from ..item.default_catalog import GOBLIN_CLEAVER, HUNTING_BOW, LEATHER_ARMOR
from ..item.item_catalog import ItemCatalog
from .location import Location


class Forest(Location):

    CODE = "forest"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(Forest.CODE, "Мистический лес", 1, catalog)

    def _create_enemy(self) -> Enemy:
        return Goblin()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (GOBLIN_CLEAVER, HUNTING_BOW, LEATHER_ARMOR)