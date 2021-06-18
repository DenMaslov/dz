import random
from statistics import geometric_mean as gavg

from soldier import Soldier
from vehicle import Vehicle
from config import Config


class Squad(Config):

    def __init__(self) -> None:
        random.seed(self.seed)
        self.__strategy = random.choice(self.STRATEGIES)
        self.__units = []
        self.__is_alive = False
        self.__health = self.MIN_HEALTH

    def add_unit(self, unit) -> None:
        """Adds Soldier or Vehicle to list of units"""
        self.__units.append(unit)
        self.estimate_health()
        self.__is_alive = True

    @property
    def health(self) -> float:
        """Returns total health of all units"""
        self.estimate_health()
        return self.__health

    @property
    def strategy(self) -> str:
        return self.__strategy

    @strategy.setter
    def strategy(self, strat: str) -> None:
        """Sets strategy. Strategy should be one of the list 'STRATEGIES' """
        strat = strat.lower()
        for s in self.STRATEGIES:
            if s == strat:
                self.__strategy = s
                break

    @property
    def is_alive(self) -> bool:
        """Checks if at least one unit is alive and health > min """
        squad_alive = False
        for unit in self.__units:
            if unit.is_alive:
                squad_alive = True
                break
        if squad_alive and self.health > self.MIN_HEALTH:
            self.__is_alive = True
            return self.__is_alive
        else:
            self.__is_alive = False
            return self.__is_alive

    @health.setter
    def health(self, hp: float) -> None:
        if hp > self.MIN_HEALTH:
            self.__health = hp
            self.__is_alive = True
        else:
            self.__health = self.MIN_HEALTH
            self.__is_alive = False

    def estimate_health(self) -> None:
        """Returns sum of units' health"""
        res_health = 0
        for unit in self.__units:
            res_health += unit.health
        self.health = res_health

    @property
    def attack_success(self) -> float:
        """Returns geom. avg of units probability of successful attack"""
        units_attack = []
        for unit in self.__units:
            units_attack.append(unit.attack_success)
        return gavg(units_attack)

    def do_damage(self) -> float:
        """Returns damage as sum of units damage"""
        res_damage = 0
        for unit in self.__units:
            res_damage += unit.do_damage()
        return res_damage

    def get_damage(self, amount: float) -> None:
        """Distributes damage evenly"""
        amount = amount / len(self.__units)
        for unit in self.__units:
            unit.get_damage(amount)
        self.estimate_health()

    def fill_random(self, n: int) -> None:
        """Fills squad with n-number of units. Vehicle operators = 3"""
        for i in range(n):
            if random.randint(0, 1):
                self.__units.append(self.create_vehicle(3))
            else:
                self.__units.append(self.create_soldier())

    def create_vehicle(self, operators: int) -> Vehicle:
        temp = Vehicle()
        for i in range(operators):
            temp.add_operator(self.create_soldier())
        return temp

    def create_soldier(self) -> Soldier:
        return Soldier()

    def __lt__(self, other) -> bool:
        return self.health < other.health
