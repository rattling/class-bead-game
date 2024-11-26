import random
from itertools import zip_longest


class MSDie:

    def __init__(self, sides=6, loaded=None):
        if loaded and (loaded < 1 or loaded > sides):
            raise ValueError("Loaded side must be between 1 and the number of sides.")
        self.sides = sides
        if loaded:
            weights = [(1 - 2 / sides) / (sides - 1)] * sides
            weights[loaded - 1] = 2 / sides
        else:
            weights = [1 / sides] * sides
        self.weights = weights

    def roll(self):
        chosen_index = random.choices(range(len(self.weights)), weights=self.weights)[0]
        return chosen_index + 1


class Cup:
    def __init__(
        self,
        dices,
        num_dices=3,
    ):
        self.dices = dices or [MSDie() for _ in range(num_dices)]

    def shake(self):
        return sum(dice.roll() for dice in self.dices)


class Game:
    def __init__(self, num_dices, sides=None, loads=None):
        # Ensure num_dices has a valid value
        if num_dices is None:
            raise ValueError("Please provide value for num_dices")
        dices = self._create_dice(num_dices, sides, loads)
        self.cup = Cup(dices)

        sides = sides or [6] * num_dices
        loads = loads or [None] * num_dices

    def _create_dice(self, num_dices, sides, loads):
        sides = sides or [6] * num_dices
        loads = loads or [None] * num_dices
        return [
            MSDie(sides=s, loaded=l)
            for s, l in zip_longest(sides, loads, fillvalue=None)
        ]

    def play(self):
        return self.cup.shake()


def test_dice_client():
    print("OK then lets roll...")

    # 1. Roll a dice
    # Varying number of sides
    print("Just roll a dice")
    msdie = MSDie(sides=5)
    print(msdie.roll())

    # 2. Shake a cup
    # Mixed numeber of sides
    print("Now shake a cup of dices")
    cup = Cup(num_dices=3, dices=None)
    print(cup.shake())

    # 3. Play a game
    print("Lets play a game of 5 dices")
    game = Game(num_dices=5)
    print(game.play())

    # 3. Play a game with different size dice
    print("Lets play a more interesing game - 5 dices of different sizes")
    game = Game(num_dices=5, sides=[6, 5, 4, 3, 2])
    print(game.play())

    # 4. Play a game with differently weighted dice
    print("Lets play a more interesing game - 5 dices of different sizes and weights")
    game = Game(num_dices=5, sides=[6, 5, 4, 3, 2], loads=[1, 2, 3, 2, 1])
    print(game.play())


if __name__ == "__main__":
    test_dice_client()
