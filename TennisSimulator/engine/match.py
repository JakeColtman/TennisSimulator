from collections import Counter
from typing import List, Optional

from TennisSimulator.engine.player import Player
from TennisSimulator.engine.point import Point
from TennisSimulator.engine.set import Set
from TennisSimulator.engine.settings import Settings


class Match:

    def __init__(self, on_serve_player: Player, off_serve_player: Player, sets: List[Set], settings: Settings):
        self.on_serve_player = on_serve_player
        self.off_serve_player = off_serve_player
        self.settings = settings

        if len(sets) == 0:
            self.sets = [Set(on_serve_player, off_serve_player, [], self.settings)]
        else:
            self.sets = sets

    def add_point(self, point: Point) -> 'Match':
        sets = self.sets
        sets[-1] = sets[-1].add_point(point)

        if sets[-1].is_won():
            if not self.is_won():
                sets = self.sets + [Set(self.off_serve_player, self.on_serve_player, [], self.settings)]

        return Match(sets[-1].on_serve_player, sets[-1].off_serve_player, sets, self.settings)

    def winner(self) -> Optional[Player]:
        counter = Counter([x.winner() for x in self.sets])
        if counter[self.on_serve_player] == 3:
            return self.on_serve_player
        elif counter[self.off_serve_player] == 3:
            return self.off_serve_player
        else:
            return None

    def is_won(self) -> bool:
        return self.winner() is not None
