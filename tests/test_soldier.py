import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier


def test_init():
    s = Soldier()
    assert s.health == 100
    assert s.experience == 0
    assert s.is_alive == True

def test_do_damage():
    s = Soldier()
    new = Soldier()
    assert s.do_damage() == 0.05 + new.experience / 100

def test_increasing_experience():
    s = Soldier()
    old_exp = s.experience
    s.do_damage()
    assert s.experience == old_exp + 1

def test_get_damage():
    s = Soldier()
    old_health = s.health
    s.get_damage(100)
    assert s.health == old_health - 100

def test_death_soldier():
    s = Soldier()
    s.get_damage(s.health * 100)
    assert s.health == 0
    assert s.is_alive == False

def test_attack_success():
    s = Soldier()
    assert s.attack_success > 0
    assert s.attack_success < 1

def test_health_setter():
    s = Soldier()
    s.health = -100
    assert s.is_alive == False
    assert s.health == 0
    s.health = 99
    assert s.health == 99
