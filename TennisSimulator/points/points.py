from random import random
from typing import Callable

from TennisSimulator.engine.match import Match
from TennisSimulator.engine.point import Point


class Probability:

    def __init__(self, probability: float):
        if probability < 0 or probability > 1:
            raise ValueError("Probabilities must be between 0 and 1, found {}".format(probability))
        else:
            self.probability = probability


def equal_and_fixed_probabilities(server_win_percentage: Probability) -> Callable[[Match], Point]:
    def generate_point(match: Match) -> Point:
        r = random()
        if r < server_win_percentage.probability:
            return Point(match.on_serve_player)
        else:
            return Point(match.off_serve_player)

    return generate_point
