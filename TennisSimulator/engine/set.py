from collections import Counter
from typing import List, Optional

from TennisSimulator.engine.game import Game
from TennisSimulator.engine.player import Player
from TennisSimulator.engine.point import Point
from TennisSimulator.engine.settings import Settings


class Set:

    def __init__(self, on_serve_player: Player, off_serve_player: Player, games: List[Game], settings: Settings):
        self.on_serve_player = on_serve_player
        self.off_serve_player = off_serve_player
        self.settings = settings

        if len(games) == 0:
            self.games = [Game(on_serve_player, off_serve_player, [], self.settings)]
        else:
            self.games = games

    def add_point(self, point: Point):
        games = self.games
        games[-1] = games[-1].add_point(point)

        if games[-1].is_won():
            if not self.is_won():
                games = self.games + [Game(self.off_serve_player, self.on_serve_player, [], self.settings)]

        return Set(games[-1].server, games[-1].receiver, games, self.settings)

    def winner(self) -> Optional[Player]:
        counter = Counter([x.winner() for x in self.games])
        if counter[self.on_serve_player] == self.settings.max_games:
            return self.on_serve_player
        elif counter[self.off_serve_player] == self.settings.max_games:
            return self.off_serve_player
        else:
            return None

    def is_won(self) -> bool:
        return self.winner() is not None
