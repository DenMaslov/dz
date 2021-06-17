import random as r

from game import Game
from army import Army
from reader import Reader

def random_armies() -> None:
    army1 = Army("east")
    army2 = Army("west")
    army1.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    army2.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    game = Game()
    game.add_army(army1)
    game.add_army(army2)
    game.start()

def config_armies(filename: str) -> None:
    game = Game()
    reader = Reader()
    armies = reader.read(filename)
    for army in armies:
        game.add_army(army)
    game.start()

def main() -> None:
    #random_armies()
    config_armies("config.yaml")


if __name__ == "__main__":
    main()
