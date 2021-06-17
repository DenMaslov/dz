import random as r

from game import Game
from army import Army
from reader import Reader


def main():
    # army1 = Army("east")
    # army2 = Army("west")
    # army1.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    # army2.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    game = Game()
    # game.add_army(army1)
    # game.add_army(army2)
    reader = Reader()
    armies = reader.read("config.yaml")
    for army in armies:
        game.add_army(army)
    game.start()


if __name__ == "__main__":
    main()
