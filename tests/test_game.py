import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from army import Army
from game import Game


def test_init():
    g = Game()
    assert len(g._Game__armies) == 0

def test_add_army():
    g = Game()
    ar = Army("red")
    ar.fill_random_squads(5)
    assert len(g._Game__armies) == 0
    g.add_army(ar)
    assert len(g._Game__armies) == 1

def test_start():
    g = Game()
    g.turn_off_logs()
    ar = Army("red")
    ar.fill_random_squads(5)
    ar2 = Army("white")
    ar2.fill_random_squads(6)
    g.add_army(ar)
    g.add_army(ar2)
    assert len(g._Game__armies) == 2
    g.start()

def test_fight():
    g = Game()
    g.turn_off_logs()
    ar = Army("red")
    ar.fill_random_squads(5)
    ar2 = Army("white")
    ar2.fill_random_squads(6)
    old_health = 0
    for squad in ar2.squads:
        old_health += squad.health
    g.fight(ar, ar2)
    new_health = 0
    for squad in ar2.squads:
        new_health += squad.health
    assert old_health >= new_health

def test_check_health():
    g = Game()
    g.turn_off_logs()
    ar = Army("red")
    ar.fill_random_squads(5)
    g.add_army(ar)
    assert g.check_health() == True

def test_have_winner():
    g = Game()
    g.turn_off_logs()
    ar = Army("red")
    ar1 = Army("white")
    ar.fill_random_squads(5)
    ar1.fill_random_squads(5)
    g.add_army(ar)
    assert g.have_winner() == True
    g.add_army(ar1)
    assert g.have_winner() == False
