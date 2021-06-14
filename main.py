import random as r

from game import Game
from army import Army


def main():
    army1 = Army("east")
    army2 = Army("west")
    army1.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    army2.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    game = Game()
    game.add_army(army1)
    game.add_army(army2)
    game.start()


if __name__ == "__main__":
    main()
