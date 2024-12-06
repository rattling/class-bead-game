import random

from casino.collection_utils import find_winners

VALID_SIDES = [4, 6, 8, 10, 20]


class Die:
    """
    Represents a die for rolling.

    Valid number of sides:
    - 4: Tetrahedron (4)
    - 5: Triangular Prism (5)
    - 6: Cube (6)
    - 8: Octahedron (8)
    - 10: Pentagonal trapezohedron (10)
    - 20: Icosahedron (20)

    For invalid inputs, an error will be raised.
    """

    def __init__(self, sides=6, biased_side=None, bias_points=1):
        if sides not in VALID_SIDES:
            raise ValueError(
                f"Invalid number of sides: {sides}. "
                f"Valid options are: {', '.join(map(str, VALID_SIDES))}. "
                "Only fair dice shapes are supported."
            )
        self.sides = sides
        bias_perc = bias_points / 100

        self.weights = self._calculate_weights(sides, biased_side, bias_perc)

    def _calculate_weights(self, sides, biased_side, bias_perc):
        """
        Calculate the weights for each side of the die.

        Prove that non-biased sides equal 1 - bias_perc / n:
            n: number of sides
            b: bias percentage
            x: weight for non biased sides

            x (n-1) + x + b = 1
            nx - x + x + b = 1
            nx = 1 - b
            x = (1 - b)/n

        Normalize the weights to sum to 1 in case of rounding errors.

        """
        if biased_side:
            if 1 <= biased_side <= sides:

                standard_weight = (1 - bias_perc) / sides
                weights = [standard_weight] * sides
                weights[biased_side - 1] = standard_weight + bias_perc
            else:
                raise ValueError("Bias must be between 1 and the number of sides.")
        else:
            weights = [1 / sides] * sides

        # Normalize weights to ensure they sum to 1
        total = sum(weights)
        weights = [round(w * 1 / total, 2) for w in weights]

        # Adjust the last element to fix any rounding discrepancy
        weights[-1] += 1 - sum(weights)

        assert sum(weights) == 1

        return weights

    def roll(self):
        chosen_index = random.choices(range(len(self.weights)), weights=self.weights)[0]
        return chosen_index + 1


class Cup:
    def __init__(self, dice=None, num_dice=3):
        if dice is None:
            self.dice = [Die() for _ in range(num_dice)]
        else:
            self.dice = dice

    def shake(self):
        return sum(die.roll() for die in self.dice)


class Player:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.game_score = 0

    def play_turn(self, cup):
        return cup.shake()


class Game:
    def __init__(self, players, cup=None, num_dice=3, rounds=1):
        self.players = [Player(name) for name in players]
        self.cup = cup or Cup(num_dice=num_dice)
        self.rounds = rounds

    def play(self):
        print("Let's play!\n")
        for round in range(self.rounds):
            print(f"\nRound {round+1}. Let's go!")
            for player in self.players:
                player.round_score = player.play_turn(self.cup)
            round_winners = find_winners(self.players, lambda p: p.round_score)
            for winner in round_winners:
                print(f"Player {winner.name} is a round winner!")
                winner.game_score += 1

        game_winners = find_winners(self.players, lambda p: p.game_score)
        for winner in game_winners:
            print(f"\nPlayer {winner.name} is a game winner!")

    def _create_fair_cup(self, num_dice):
        return Cup(num_dice=num_dice)


if __name__ == "__main__":

    print("\nGame1 is on!\n")
    game1 = Game(
        players=["computer", "Mike", "Anne"],
        num_dice=3,
        rounds=6,
    )
    game1.play()

    print("\nGame1 is on!\n")
    dice = [Die(sides=6, biased_side=3), Die(sides=8, biased_side=8), Die()]
    custom_cup = Cup(dice)
    game2 = Game(
        players=["computer", "Mike", "Anne"],
        cup=custom_cup,
        rounds=6,
    )
    game2.play()
