

class Settings:

    def __init__(self, max_sets: int=3, max_games: int=6, max_points=5, has_deuce: bool=False):
        self.max_sets = max_sets
        self.max_games = max_games
        self.has_deuce = has_deuce
        self.max_points = max_points
