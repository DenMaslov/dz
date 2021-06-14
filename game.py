import logging as log

from army import Army
from squad import Squad
from config import Config

# rootLog is used for enabling/disabling info-messages
# useful for tests modules
rootLog = log.getLogger()
rootLog.setLevel(log.DEBUG)
log.basicConfig(format='%(message)s')


class Game(Config):

    def __init__(self) -> None:
        self.__armies = []

    def add_army(self, army: Army) -> None:
        """Adds alive army to the list of the armies"""
        if army.is_alive:
            self.__armies.append(army)
        else:
            raise ValueError("Army must be alive")

    def start(self) -> None:
        """Main game loop. Checks if number of armies >= 2"""
        if len(self.__armies) >= self.MIN_ARMIES:
            log.info("\n\n\n")
            while not self.have_winner():
                for attacker in self.__armies:
                    for defender in self.__armies:
                        if attacker != defender:
                            log.info(f"attacking army: {attacker.name}")
                            self.fight(attacker, defender)
                            self.show_state()
        else:
            raise ValueError("The game has to consist of 2 armies or more.")

    def fight(self, attacker: Army, defender: Army) -> None:
        """Simulates fight of attacker's squads against defenders"""
        for squad in attacker.squads:
            defending_squad = defender.get_squad_to_attack(squad.strategy)
            log.info("-" * 40)
            if self.attacker_win(squad, defending_squad):
                damage = squad.do_damage() * self.DAMAGE_BOOSTER
                log.info(f'{attacker.name} do damage {damage} to defender {defender.name}')
                defending_squad.get_damage(damage)

    def attacker_win(self, attacker: Squad, defender: Squad) -> bool:
        """Returns if attack_success of attacker greater then
        attack_success of defender
        """
        if isinstance(attacker, Squad) and isinstance(defender, Squad):
            if attacker.attack_success >= defender.attack_success:
                log.info("Attack is successful")
                return True
            else:
                log.info("Attack is not successful")
                return False

    def check_health(self) -> bool:
        """Checks if there are any alive armies"""
        for army in self.__armies:
            if not army.is_alive:
                return False
        else:
            return True

    def show_state(self) -> None:
        """Shows state of armies"""
        log.info("-" * 40)
        for army in self.__armies:
            log.info(f'state: {army.state()}')
        log.info("\n" + "=" * 100)
        log.info("\n")

    def have_winner(self) -> bool:
        """Checks if there is only one alive army"""
        alive_armies = []
        for army in self.__armies:
            for squad in army.squads:
                if squad.is_alive:
                    alive_armies.append(army.name)
                    break
        if len(alive_armies) == 1:
            log.info("*" * 50)
            log.info(f"The winner is - {alive_armies[0]}")
            log.info("*" * 50)
            return True
        else:
            return False

    def turn_off_logs(self) -> None:
        """Turns off logs. Used for test modules"""
        rootLog.setLevel(log.CRITICAL)
