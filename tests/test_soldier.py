import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier


class SoldierTestCase(unittest.TestCase):

    def test_init(self):
        s = Soldier()
        self.assertEqual(s.health, 100)
        self.assertEqual(s.experience, 0)
        self.assertEqual(s.is_alive, True)

    def test_do_damage(self):
        s = Soldier()
        new = Soldier()
        self.assertEqual(s.do_damage(), 0.05 + new.experience / 100)

    def test_increasing_experience(self):
        s = Soldier()
        old_exp = s.experience
        s.do_damage()
        self.assertEqual(s.experience, old_exp + 1)

    def test_get_damage(self):
        s = Soldier()
        old_health = s.health
        s.get_damage(100)
        self.assertEqual(s.health, old_health - 100)

    def test_death_soldier(self):
        s = Soldier()
        s.get_damage(s.health * 100)
        self.assertEqual(s.health, 0)
        self.assertEqual(s.is_alive, False)

    def test_attack_success(self):
        s = Soldier()
        self.assertGreater(s.attack_success, 0)
        self.assertLess(s.attack_success, 1)

    def test_health_setter(self):
        s = Soldier()
        s.health = -100
        self.assertEqual(s.is_alive, False)
        self.assertEqual(s.health, 0)
        s.health = 99
        self.assertEqual(s.health, 99)
