import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier
from squad import Squad
from army import Army



def test_init():
    ar = Army("red")
    assert ar.name == "red"
    assert ar.is_alive == False
    assert isinstance(ar.strategy, str)
    
def test_add_squad():
    ar = Army("red")
    ar.strategy = "weakest"
    sq = Squad()
    sq.strategy = "strongest"
    sq.add_unit(Soldier())
    ar.add_squad(sq)
    ar2 = Army("white")
    assert ar.is_alive != ar2.is_alive
    assert ar.strategy == sq.strategy
    assert len(ar._Army__squads) == 1
    sq.get_damage(10000000000)
    assert ar.is_alive == False

def test_squads():
    ar = Army("red")
    ar.strategy = "weakest"
    sq1 = Squad()
    sq1.add_unit(Soldier())
    sq1.strategy = "strongest"
    sq2 = Squad()
    sq2.add_unit(Soldier())
    sq2.strategy = "strongest"
    ar.add_squad(sq1)
    ar.add_squad(sq2)
    arr = [sq1, sq2]
    assert ar.squads == arr
    assert ar.squads[0].strategy == ar.strategy
    assert ar.squads[1].strategy == ar.strategy

def test_is_alive():
    ar = Army("red")
    assert ar.is_alive == False
    sq1 = Squad()
    sq1.add_unit(Soldier())
    ar.add_squad(sq1)
    assert ar.is_alive == True
    ar.squads[0].get_damage(100000)
    assert ar.is_alive == False

def test_fill_random_squads():
    ar = Army("red")
    assert ar.is_alive == False
    ar.fill_random_squads(6)
    assert len(ar.squads) == 6
    assert ar.is_alive == True
    flag = True
    for squad in ar.squads:
        if not squad.health >= 500 or squad.health > 1000:
            flag = False
    assert flag == True

def test_weakest_squad():
    ar = Army("red")
    sq1 = Squad()
    sq1.add_unit(Soldier())
    sq2 = Squad()
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    ar.add_squad(sq1)
    ar.add_squad(sq2)
    assert ar.weakest_squad == sq1
    
def test_strongest_squad():
    ar = Army("red")
    sq1 = Squad()
    sq1.add_unit(Soldier())
    sq2 = Squad()
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    ar.add_squad(sq1)
    ar.add_squad(sq2)
    assert ar.strongest_squad == sq2
    
def test_random_squad():
    ar = Army("red")
    sq1 = Squad()
    sq1.add_unit(Soldier())
    sq2 = Squad()
    sq2.add_unit(Soldier())
    ar.add_squad(sq1)
    ar.add_squad(sq2)
    assert isinstance(ar.random_squad, Squad) == True

def test_get_squad_to_attack():
    ar = Army("red")
    sq1 = Squad()
    sq1.add_unit(Soldier())
    sq2 = Squad()
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    sq2.add_unit(Soldier())
    ar.add_squad(sq1)
    ar.add_squad(sq2)
    assert ar.get_squad_to_attack("strongest") == sq2
    assert ar.get_squad_to_attack("weakest") == sq1
