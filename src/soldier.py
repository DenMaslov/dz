import random

from config import Config


class Soldier(Config):
    """ Base class of Soldier.

    Contains main fields of Soldier.
    """

    def __init__(self) -> None:
        random.seed(self.seed)
        self.__health = self.MAX_HEALTH
        self.__is_alive = True
        self.__experience = self.MIN_EXPERIENCE

    @property
    def recharge(self) -> int:
        """ Returns recharge in ms """
        return random.randint(self.MIN_RECHARGE,
                              self.MAX_RECHARGE)

    @property
    def health(self) -> float:
        """ Returns health of the soldier """
        return self.__health

    @health.setter
    def health(self, hp: float) -> None:
        """ Health setter, checks arg and set hp, if arg < min - sets min """
        if hp > self.MIN_HEALTH:
            self.__health = hp
        else:
            self.__is_alive = False
            self.__health = self.MIN_HEALTH

    @property
    def is_alive(self) -> bool:
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, state: bool) -> None:
        self.__is_alive = state
        if state is False:
            self.__health = self.MIN_HEALTH

    @property
    def experience(self) -> int:
        return self.__experience

    @experience.setter
    def experience(self, x: int) -> None:
        """ Experience setter, checks arg and set exp, if arg < min - sets min """
        if x < self.MAX_EXPERIENCE:
            self.__experience = x
        else:
            self.__experience = self.MAX_EXPERIENCE

    @property
    def attack_success(self) -> float:
        """ Estimates probability of successful attack. 0 <= x <= 1 """
        return (0.5 * (1 + self.health / 100) *
                random.randint(50 + self.experience, 100) / 100)

    def do_damage(self) -> float:
        """ Estimates amount of damage """
        res = 0.05 + self.experience / 100
        self.experience = self.experience + 1
        return res

    def get_damage(self, amount: float) -> None:
        """ Gets damage. Health = health - damage """
        self.health = self.health - amount
