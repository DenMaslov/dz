import random

from squad import Squad
from config import Config


class Army(Config):
    """ Class of Army model.

    Contains main fields of Army.
    Army is constituted by squads. 
    """
    
    def __init__(self, name: str) -> None:
        self.__name = name
        random.seed(self.seed)
        self.__squads = []
        self.__strategy = random.choice(self.STRATEGIES)
        self.__is_alive = False

    def add_squad(self, squad: Squad) -> None:
        """Adds alive squad to the list of the squads"""
        if squad.is_alive:
            squad.strategy = self.strategy
            self.__squads.append(squad)
        else:
            raise ValueError("Squad is not alive")

    @property
    def squads(self) -> list:
        return self.__squads

    @property
    def is_alive(self) -> bool:
        """Checks if there is any alive squad"""
        squads_alive = False
        for squad in self.__squads:
            if squad.is_alive:
                squads_alive = True
                break
        self.__is_alive = squads_alive
        return self.__is_alive

    @property
    def strategy(self) -> str:
        return self.__strategy

    @strategy.setter
    def strategy(self, strat: str) -> None:
        strat = strat.lower()
        for s in self.STRATEGIES:
            if s == strat:
                self.__strategy = s
                break

    def fill_random_squads(self, amount: int) -> None:
        """Fills army with n-number of squads. Vehicle operators = 3"""
        for i in range(amount):
            temp = Squad()
            temp.fill_random(random.randint(self.MIN_UNITS, self.MAX_UNITS))
            temp.strategy = self.strategy
            self.__squads.append(temp)

    @property
    def weakest_squad(self) -> Squad:
        """Returns squad with the lowest hp"""
        self.__squads.sort()
        if self.is_alive:
            for squad in self.__squads:
                if squad.is_alive:
                    return squad
        return None

    @property
    def random_squad(self) -> Squad:
        """Returns random squad"""
        if self.is_alive:
            return random.choice(self.__squads)
        return None

    @property
    def strongest_squad(self) -> Squad:
        """Returns squad with the biggest hp"""
        self.__squads.sort()
        if self.is_alive:
            for squad in self.__squads[::-1]:
                if squad.is_alive:
                    return squad
        return None

    @property
    def name(self) -> str:
        """Returns name. Used only for logging"""
        return self.__name

    def get_squad_to_attack(self, strategy: str) -> Squad:
        """Returns squad judging by strategy"""
        if strategy == self.STRATEGIES[0]:
            return self.random_squad
        if strategy == self.STRATEGIES[1]:
            return self.weakest_squad
        if strategy == self.STRATEGIES[2]:
            return self.strongest_squad
        raise ValueError("Wrong strategy, can't find any matches")

    def state(self) -> dict:
        """Returns dict of name and squads hp"""
        res = {}
        res["name:"] = self.name
        for i in range(len(self.__squads)):
            res[f"{i + 1} squad"] = self.__squads[i].health
        return res
