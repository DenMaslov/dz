import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from soldier import Soldier
from vehicle import Vehicle
from squad import Squad


class SquadTestCase(unittest.TestCase):
    
    def test_init(self):
        sq = Squad()
        self.assertEqual(sq.is_alive, False)
        self.assertEqual(sq.health, 0)
        self.assertTrue(isinstance(sq.strategy, str))

    def test_add_unit(self):
        s = Soldier()
        sq = Squad()
        sq.add_unit(s)
        sq.add_unit(Soldier())
        self.assertEqual(sq.health, s.health * 2)
        self.assertEqual(sq.is_alive, True)
    
    def test_health(self):
        sq = Squad()
        self.assertEqual(sq.health, 0)
        self.assertEqual(sq.is_alive, False)
        sq.add_unit(Soldier())
        sq.health = 80
        self.assertEqual(sq.health, 100)
        self.assertEqual(sq.is_alive, True)
        sq.health = -1000
        self.assertEqual(sq.health, 100)
        self.assertEqual(sq.is_alive, True)
    
    def test_estimate_health(self):
        sq = Squad()
        sq.add_unit(Soldier())
        sq.add_unit(Soldier())
        sq.estimate_health()
        self.assertEqual(sq.health, 200)
    
    def test_attack_success(self):
        sq = Squad()
        sq.add_unit(Soldier())
        self.assertLessEqual(sq.attack_success, 1)
        self.assertGreaterEqual(sq.attack_success, 0)
    
    def test_do_damage(self):
        sq = Squad()
        s = Soldier()
        v = Vehicle()
        sq.add_unit(Soldier())
        sq.add_unit(Vehicle())
        self.assertEqual(sq.do_damage(), s.do_damage() + v.do_damage())
    
    def test_get_damage(self):
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
        self.assertEqual(sq.health, v2.health + s.health)

    def test_fill_random(self):
        sq = Squad()
        sq.fill_random(5)
        self.assertEqual(len(sq._Squad__units), 5)
        flag = True
        for unit in sq._Squad__units:
            if isinstance(unit, Vehicle) or isinstance(unit, Soldier):
                pass
            else:
                flag = False
        self.assertTrue(flag)
        number_of_vehicle = 0
        number_of_soldiers = 0
        for unit in sq._Squad__units:
            if isinstance(unit, Vehicle):
                number_of_vehicle += 1
            else: 
                number_of_soldiers += 1
        self.assertEqual(sq.health, 
                        (number_of_soldiers + number_of_vehicle) * 100)
        
    def test_create_vehicle(self):
        sq = Squad()
        v = Vehicle()
        v.add_operator(Soldier())
        v.add_operator(Soldier())
        self.assertEqual(sq.create_vehicle(2).health, v.health)
        self.assertEqual(sq.create_vehicle(3).is_alive, True)
