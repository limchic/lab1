from __future__ import annotations
from enum import Enum
from ..core.unknown_code_error import UnknownCodeError
from ..item.item_catalog import ItemCatalog
from ..kit.mage_kit_factory import MageKitFactory
from ..kit.warrior_kit_factory import WarriorKitFactory
from ..kit.starter_kit_factory import StarterKitFactory

class HeroClass(Enum):
    WARRIOR = ("warrior", "Воин", 120, WarriorKitFactory)
    MAGE = ("mage", "Маг", 85, MageKitFactory)

    def __init__(self, code: str, display_name: str, base_health: int, kit_factory: type) -> None:
        self.code = code
        self.display_name = display_name
        self.base_health = base_health
        self._kit_factory = kit_factory

    def starter_kit(self, catalog: ItemCatalog) -> StarterKitFactory:
        return self._kit_factory(catalog)