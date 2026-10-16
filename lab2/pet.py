from abc import ABC, abstractmethod

class Pet(ABC):

    @abstractmethod
    def express(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_age(self) -> int:
        pass

    @abstractmethod
    def get_age_in_human_years(self) -> int:
        pass
