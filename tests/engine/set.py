from unittest import TestCase
import unittest

from TennisSimulator.engine.settings import Settings
from TennisSimulator.engine.set import Set
from TennisSimulator.engine.player import Player
from TennisSimulator.engine.point import Point


class SetTest(TestCase):

    def setUp(self):
        self.player_one = Player("player_one")
        self.player_two = Player("player_two")

    def test_set_reaches_completion(self):
        settings = Settings(max_points=2, max_games=2)
        set = Set(self.player_one, self.player_two, [], settings)
        self.assertEqual(set.is_won(), False)

        set = set.add_point(Point(self.player_one))
        set = set.add_point(Point(self.player_one))
        set = set.add_point(Point(self.player_one))
        set = set.add_point(Point(self.player_one))

        self.assertEqual(set.is_won(), True)
        self.assertEqual(set.winner(), self.player_one)

    def test_new_game_creation(self):
        settings = Settings(max_points=2)
        set = Set(self.player_one, self.player_two, [], settings)
        self.assertEqual(set.games[-1].server, self.player_one)

        set = set.add_point(Point(self.player_one))
        set = set.add_point(Point(self.player_one))

        self.assertEqual(set.off_serve_player, self.player_one)
        self.assertEqual(set.on_serve_player, self.player_two)

        set = set.add_point(Point(self.player_one))
        set = set.add_point(Point(self.player_one))

        self.assertEqual(set.off_serve_player, self.player_two)
        self.assertEqual(set.on_serve_player, self.player_one)


if __name__ == '__main__':
    unittest.main()
