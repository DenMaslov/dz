from abc import ABC, abstractmethod


class BaseUnit(ABC):
    
    @property
    @abstractmethod
    def recharge(self) -> int:
        pass

    @property
    @abstractmethod
    def health(self) -> float:
        pass

    @property
    @abstractmethod
    def is_alive(self) -> bool:
        pass

    @property
    @abstractmethod
    def attack_success(self) -> float:
        pass

    @abstractmethod
    def do_damage(self) -> float:
        pass

    @abstractmethod
    def get_damage(self, amount: float) -> None:
        pass