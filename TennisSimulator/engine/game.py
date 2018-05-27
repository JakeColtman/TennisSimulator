from collections import Counter
from typing import List, Optional

from TennisSimulator.engine.point import Point
from TennisSimulator.engine.player import Player
from TennisSimulator.engine.settings import Settings


class Game:

    def __init__(self, on_serve_player: Player, off_serve_player: Player, points: List[Point], settings: Settings):
        self.server = on_serve_player
        self.receiver = off_serve_player
        self.points = points
        self.settings = settings

    def add_point(self, point: Point):
        return Game(self.server, self.receiver, self.points + [point], self.settings)

    def is_won(self) -> bool:
        return self.winner() is not None

    def winner(self) -> Optional[Player]:
        counter = Counter([x.player for x in self.points])
        if counter[self.server] == self.settings.max_points:
            return self.server
        elif counter[self.receiver] == self.settings.max_points:
            return self.receiver
        else:
            return None

