import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = currentdir.replace("tests", "src")
sys.path.append(currentdir)

from army import Army
from game import Game


class GameTestCase(unittest.TestCase):

    def test_init(self):
        g = Game()
        self.assertEqual(len(g._Game__armies), 0)

    def test_add_army(self):
        g = Game()
        ar = Army("red")
        ar.fill_random_squads(5)
        self.assertEqual(len(g._Game__armies), 0)
        g.add_army(ar)
        self.assertEqual(len(g._Game__armies), 1)

    def test_start(self):
        g = Game()
        g.turn_off_logs()
        ar = Army("red")
        ar.fill_random_squads(5)
        ar2 = Army("white")
        ar2.fill_random_squads(6)
        g.add_army(ar)
        g.add_army(ar2)
        self.assertEqual(len(g._Game__armies), 2)
        g.start()

    def test_fight(self):
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
        self.assertGreater(old_health, new_health)

    def test_check_health(self):
        g = Game()
        g.turn_off_logs()
        ar = Army("red")
        ar.fill_random_squads(5)
        g.add_army(ar)
        self.assertTrue(g.check_health())

    def test_have_winner(self):
        g = Game()
        g.turn_off_logs()
        ar = Army("red")
        ar1 = Army("white")
        ar.fill_random_squads(5)
        ar1.fill_random_squads(5)
        g.add_army(ar)
        self.assertTrue(g.have_winner())
        g.add_army(ar1)
        self.assertFalse(g.have_winner())
