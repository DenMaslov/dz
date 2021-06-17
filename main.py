import random as r

from game import Game
from army import Army
from reader import Reader

def random_armies():
    army1 = Army("east")
    army2 = Army("west")
    army1.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    army2.fill_random_squads(r.randint(Game.MIN_SQUADS, Game.MAX_SQUADS))
    game = Game()
    game.add_army(army1)
    game.add_army(army2)
    game.start()

def config_armies():
    game = Game()
    reader = Reader()
    armies = reader.read("config.yaml")
    for army in armies:
        game.add_army(army)
    game.start()

def main():
    #random_armies()
    config_armies()
   


if __name__ == "__main__":
    main()
