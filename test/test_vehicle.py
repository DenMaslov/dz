import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from soldier import Soldier
from vehicle import Vehicle


class VehicleTestCase(unittest.TestCase):

    def test_init(self):
        v = Vehicle()
        self.assertEqual(v.health, 100)
        self.assertEqual(v.is_alive, False)
        self.assertEqual(v._Vehicle__operators, [])

    def test_add_operator(self):
        v = Vehicle()
        operator = Soldier()
        v.add_operator(operator)
        self.assertEqual(v.is_alive, True)
        self.assertEqual(len(v._Vehicle__operators), 1)
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        self.assertEqual(len(v._Vehicle__operators), 3)
    
    def test_health(self):
        v = Vehicle()
        v.add_operator(Soldier())
        v.health = -100000
        self.assertEqual(v.health, 0)
        self.assertEqual(v.is_alive, False)
        v.health = 50
        self.assertEqual(v.health, 50)
        self.assertEqual(v.is_alive, True)
    
    def test_estimate_total_health(self):
        v = Vehicle()
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        old_health = v.health
        v.estimate_total_health()
        self.assertEqual(v.health, 100)
        v = Vehicle()
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        s = Soldier()
        s.health = 50
        v.add_operator(s)
        v.estimate_total_health()
        self.assertEqual(v.health, 350 / 4)

    def test_do_damage(self):
        v = Vehicle()
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        s = Soldier()
        s.experience += 1
        self.assertEqual(v.do_damage(), 0.1 + s.experience / 100 * 3)
    
    def test_check_is_alive(self):
        v = Vehicle()
        v.health = 100
        self.assertEqual(v.is_alive, False)
        v.add_operator(Soldier())
        self.assertEqual(v.is_alive, True)
    
    def test_attack_success(self):
        v = Vehicle()
        v.add_operator(Soldier())
        self.assertLessEqual(v.attack_success, 1)
        self.assertGreater(v.attack_success, 0)

    def test_get_damage(self):
        v = Vehicle()
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        v.get_damage(100)
        self.assertEqual(v.health, (40 + 80 + 90 + 90) / 4) 
        self.assertEqual(v.is_alive, True)
        v.get_damage(100000)
        self.assertEqual(v.health, 0) 
        self.assertEqual(v.is_alive, False)
