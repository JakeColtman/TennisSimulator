from TennisSimulator.engine.match import Match
from TennisSimulator.engine.settings import Settings
from TennisSimulator.engine.player import Player

from TennisSimulator.points.points import equal_and_fixed_probabilities, Probability

if __name__ == "__main__":

    settings = Settings()
    player_one = Player("1")
    player_two = Player("2")

    f_points = equal_and_fixed_probabilities(Probability(0.5))

    def simulate_match():
        match = Match(player_one, player_two, [], settings)

        while not match.is_won():
            p = f_points(match)
            match = match.add_point(p)

        return match.winner()


    sample_winners = [simulate_match() for _ in range(1000)]

    from collections import Counter
    counter = Counter(sample_winners)
    print(counter[player_one] / len(sample_winners))