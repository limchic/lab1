from __future__ import annotations

from typing import Iterable

from ..core.unknown_code_error import UnknownCodeError
from .location import Location


class LocationRegistry:

    def __init__(self, locations: Iterable[Location]) -> None:
        self._locations: dict[str, Location] = {}
        for location in locations:
            self._locations[location.code] = location

    def get(self, code: str) -> Location:
        location = self._locations.get(code)
        if location is None:
            raise UnknownCodeError("Локация", code)

        return location

    @property
    def all(self) -> list[Location]:
        return list(self._locations.values())