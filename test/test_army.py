import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from soldier import Soldier
from squad import Squad
from army import Army


class ArmyTestCase(unittest.TestCase):

    def test_init(self):
        ar = Army("red")
        self.assertEqual(ar.name, "red")
        self.assertEqual(ar.is_alive, False)
        self.assertTrue(isinstance(ar.strategy, str))
    
    def test_add_squad(self):
        ar = Army("red")
        ar.strategy = "weakest"
        sq = Squad()
        sq.strategy = "strongest"
        sq.add_unit(Soldier())
        ar.add_squad(sq)
        ar2 = Army("white")
        self.assertNotEqual(ar.is_alive, ar2.is_alive)
        self.assertEqual(ar.strategy, sq.strategy)
        self.assertEqual(len(ar._Army__squads), 1)
        sq.get_damage(10000000000)
        self.assertEqual(ar.is_alive, False)
    
    def test_squads(self):
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
        self.assertEqual(ar.squads, arr)
        self.assertEqual(ar.squads[0].strategy, ar.strategy)
        self.assertEqual(ar.squads[1].strategy, ar.strategy)

    def test_is_alive(self):
        ar = Army("red")
        self.assertEqual(ar.is_alive, False)
        sq1 = Squad()
        sq1.add_unit(Soldier())
        ar.add_squad(sq1)
        self.assertEqual(ar.is_alive, True)
        ar.squads[0].get_damage(100000)
        self.assertEqual(ar.is_alive, False)

    def test_fill_random_squads(self):
        ar = Army("red")
        self.assertEqual(ar.is_alive, False)
        ar.fill_random_squads(6)
        self.assertEqual(len(ar.squads), 6)
        self.assertEqual(ar.is_alive, True)
        flag = True
        for squad in ar.squads:
            if not squad.health >= 500 or squad.health > 1000:
                flag = False
        self.assertTrue(flag)
    
    def test_weakest_squad(self):
        ar = Army("red")
        sq1 = Squad()
        sq1.add_unit(Soldier())
        sq2 = Squad()
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        ar.add_squad(sq1)
        ar.add_squad(sq2)
        self.assertEqual(ar.weakest_squad, sq1)
        
    def test_strongest_squad(self):
        ar = Army("red")
        sq1 = Squad()
        sq1.add_unit(Soldier())
        sq2 = Squad()
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        ar.add_squad(sq1)
        ar.add_squad(sq2)
        self.assertEqual(ar.strongest_squad, sq2)
        
    def test_random_squad(self):
        ar = Army("red")
        sq1 = Squad()
        sq1.add_unit(Soldier())
        sq2 = Squad()
        sq2.add_unit(Soldier())
        ar.add_squad(sq1)
        ar.add_squad(sq2)
        self.assertTrue(isinstance(ar.random_squad, Squad))

    def test_get_squad_to_attack(self):
        ar = Army("red")
        sq1 = Squad()
        sq1.add_unit(Soldier())
        sq2 = Squad()
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        sq2.add_unit(Soldier())
        ar.add_squad(sq1)
        ar.add_squad(sq2)
        self.assertEqual(ar.get_squad_to_attack("strongest"), sq2)
        self.assertEqual(ar.get_squad_to_attack("weakest"), sq1)
