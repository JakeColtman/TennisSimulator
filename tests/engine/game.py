from unittest import TestCase
import unittest

from TennisSimulator.engine.settings import Settings
from TennisSimulator.engine.game import Game
from TennisSimulator.engine.player import Player
from TennisSimulator.engine.point import Point


class GameTest(TestCase):

    def setUp(self):
        self.player_one = Player("player_one")
        self.player_two = Player("player_two")

    def test_simple_server_win(self):
        settings = Settings(max_points=2)
        game = Game(self.player_one, self.player_two, [], settings)
        self.assertEqual(game.is_won(), False)

        point = Point(self.player_one)
        game = game.add_point(point)

        self.assertEqual([point], game.points)
        self.assertEqual(game.is_won(), False)
        game = game.add_point(Point(self.player_one))
        self.assertEqual(game.is_won(), True)
        self.assertEqual(game.winner(), self.player_one)


if __name__ == '__main__':
    unittest.main()