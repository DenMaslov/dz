import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier
from vehicle import Vehicle
from squad import Squad

    
def test_init():
    sq = Squad()
    assert sq.is_alive == False
    assert sq.health == 0
    assert isinstance(sq.strategy, str) == True

def test_add_unit():
    s = Soldier()
    sq = Squad()
    sq.add_unit(s)
    sq.add_unit(Soldier())
    assert sq.health == s.health * 2
    assert sq.is_alive == True

def test_health():
    sq = Squad()
    assert sq.health == 0
    assert sq.is_alive == False
    sq.add_unit(Soldier())
    sq.health = 80
    assert sq.health == 100
    assert sq.is_alive == True
    sq.health = -1000
    assert sq.health == 100
    assert sq.is_alive == True

def test_estimate_health():
    sq = Squad()
    sq.add_unit(Soldier())
    sq.add_unit(Soldier())
    sq.estimate_health()
    assert sq.health == 200

def test_attack_success():
    sq = Squad()
    sq.add_unit(Soldier())
    assert sq.attack_success <= 1
    assert sq.attack_success >= 0

def test_do_damage():
    sq = Squad()
    s = Soldier()
    v = Vehicle()
    sq.add_unit(Soldier())
    sq.add_unit(Vehicle())
    assert sq.do_damage() == s.do_damage() + v.do_damage()

def test_get_damage():
    sq = Squad()
    s = Soldier()
    v1 = Vehicle()
    v2 = Vehicle()
    for i in range(3):
        v1.add_operator(Soldier())
        v2.add_operator(Soldier())
    sq.add_unit(Soldier())
    sq.add_unit(v1)
    sq.get_damage(100)
    s.get_damage(100 / 2)
    v2.get_damage(100 / 2)
    assert sq.health == v2.health + s.health

def test_fill_random():
    sq = Squad()
    sq.fill_random(5)
    assert len(sq._Squad__units) == 5
    flag = True
    for unit in sq._Squad__units:
        if isinstance(unit, Vehicle) or isinstance(unit, Soldier):
            pass
        else:
            flag = False
    assert flag == True
    number_of_vehicle = 0
    number_of_soldiers = 0
    for unit in sq._Squad__units:
        if isinstance(unit, Vehicle):
            number_of_vehicle += 1
        else: 
            number_of_soldiers += 1
    assert sq.health == (number_of_soldiers + number_of_vehicle) * 100
    
def test_create_vehicle():
    sq = Squad()
    v = Vehicle()
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    assert sq.create_vehicle(2).health == v.health
    assert sq.create_vehicle(3).is_alive == True
