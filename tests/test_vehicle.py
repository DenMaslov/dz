import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier
from vehicle import Vehicle


def test_init():
    v = Vehicle()
    assert v.health == 100
    assert v.is_alive == False
    assert v._Vehicle__operators == []

def test_add_operator():
    v = Vehicle()
    operator = Soldier()
    v.add_operator(operator)
    assert v.is_alive == True
    assert len(v._Vehicle__operators) == 1
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    assert len(v._Vehicle__operators) == 3

def test_health():
    v = Vehicle()
    v.add_operator(Soldier())
    v.health = -100000
    assert v.health == 0
    assert v.is_alive == False
    v.health = 50
    assert v.health == 50
    assert v.is_alive == True

def test_estimate_total_health():
    v = Vehicle()
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    old_health = v.health
    v.estimate_total_health()
    assert v.health == 100
    v = Vehicle()
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    s = Soldier()
    s.health = 50
    v.add_operator(s)
    v.estimate_total_health()
    assert v.health == 350 / 4

def test_do_damage():
    v = Vehicle()
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    s = Soldier()
    s.experience += 1
    assert v.do_damage() == 0.1 + s.experience / 100 * 3

def test_check_is_alive():
    v = Vehicle()
    v.health = 100
    assert v.is_alive == False
    v.add_operator(Soldier())
    assert v.is_alive == True

def test_attack_success():
    v = Vehicle()
    v.add_operator(Soldier())
    assert v.attack_success <= 1
    assert v.attack_success >= 0

def test_get_damage():
    v = Vehicle()
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.add_operator(Soldier())
    v.get_damage(100)
    assert v.health == (40 + 80 + 90 + 90) / 4
    assert v.is_alive == True
    v.get_damage(100000)
    assert v.health == 0 
    assert v.is_alive == False
