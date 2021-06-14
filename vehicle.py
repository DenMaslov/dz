import random
from statistics import geometric_mean as gavg

from soldier import Soldier
from config import Config


class Vehicle(Config):
    """ Class represents Vehicle model.
    Contains main fields of Vehicle.
    As operators are used instances of Soldier class.
    """
    def __init__(self) -> None:
        self.__operators = []
        self.__health = self.MAX_HEALTH
        self.__is_alive = False

    def add_operator(self, operator: Soldier) -> None:
        """Adds operator to list of operators. 
        List should contain from 1 to 3 operators.
        """
        if isinstance(operator, Soldier):
            if len(self.__operators) < self.MAX_OPERATORS:
                self.__operators.append(operator)
                self.__is_alive = True
        else:
            raise TypeError("argument must be a Soldier")

    @property
    def recharge(self) -> int:
        """ Returns recharge in ms """
        return random.randint(self.MIN_RECHARGE_VEHICLE,
                             self.MAX_RECHARGE)

    @property
    def is_alive(self) -> bool:
        """Checks if crew are alive and total health greater than min"""
        self.check_is_alive()
        return self.__is_alive

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    def health(self, hp: float) -> None:
        if hp > self.MIN_HEALTH:
            self.__health = hp
            self.__is_alive = True
        else:
            self.__health = self.MIN_HEALTH
            self.__is_alive = False

    @property
    def attack_success(self) -> float:
        attack_operators = []
        for operator in self.__operators:
            attack_operators.append(operator.attack_success)
        return (0.5 * (1 + self.health / 100) *
                gavg(attack_operators))

    def estimate_total_health(self) -> None:
        """Health = avarage health of crew and vehicle"""
        crew_health = 0
        for operator in self.__operators:
            crew_health += operator.health
        crew_health += self.__health
        self.__health = crew_health / (len(self.__operators) + 1)

    def do_damage(self) -> float:
        """Returns amount of damage"""
        sum = 0
        for operator in self.__operators:
            if operator.is_alive:
                operator.experience += 1
                sum += operator.experience / 100
        return 0.1 + sum

    def get_damage(self, amount: float) -> None:
        """Distributes damage to crew and vehicle"""
        self.health = self.health - amount * self.DMG_TO_VEHICLE
        rnd_operator = random.choice(self.__operators)
        rnd_operator.get_damage(amount * self.DMG_TO_ONE_OPER)
        for operator in self.__operators:
            if operator != rnd_operator:
                operator.get_damage(amount * self.DMG_TO_OPER)
        self.estimate_total_health()
        self.check_is_alive()

    def check_is_alive(self) -> bool:
        """Checks if crew and vehicle are alive """
        crew_alive = False
        for operator in self.__operators:
            if operator.is_alive:
                crew_alive = True
                break
        if crew_alive and self.health > self.MIN_HEALTH:
            self.__is_alive = True
            return True
        else:
            self.__is_alive = False
            return False
