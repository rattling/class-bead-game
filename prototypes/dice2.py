import random


class GameStrategy:
    def calculate_roll_score(self, dice_roll):
        pass

    def calculate_round_score(self, dice_roll):
        pass

    def turn_over(self, dice_roll):
        pass

    def keep_dice(self, dice_roll):
        pass


class RollOffStrategy(GameStrategy):
    def calculate_roll_score(self, dice_roll):
        return sum(dice_roll)

    def calculate_round_score(self, dice_roll):
        return sum(dice_roll)

    def turn_over(self, dice_roll):
        return True

    def keep_dice(self, dice_roll):
        return dice_roll


class GameType:
    ROLLOFF = "roll off"
    FARKLE = "farkle"
    PIG = "pig"


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Cup:
    def __init__(self, dice=None, num_dice=3):
        if dice is None:
            self.dice = [Die() for _ in range(num_dice)]
        else:
            self.dice = dice

    def shake(self):
        return [die.roll() for die in self.dice]


class game:
    def __init__(self, game_type, players, rounds=1, cup=None, num_dice=3):
        self.players = players
        self.rounds = rounds
        self.cup = cup or Cup(num_dice=num_dice)
        self.strategy = game_type()

    def play(self):

        game_over = False
        game_scores = {player: 0 for player in self.players}
        while not game_over:
            for player in self.players:
                print(f"Player {player.name}'s turn!")
                player_score = 0
                turn_over = False
                while not turn_over:
                    dice_roll = self.cup.shake()
                    print(f"Player {player.name} rolled {dice_roll}")
                    score = self.strategy.calculate_roll_score(dice_roll)

                    if self.g.calculate_roll_score(dice_roll) == 0:
                        print("Farkle! Turn over.")
                        turn_over = True
                    else:
                        player_score += self.game_type.calculate_round_score(dice_roll)
                        print(
                            f"Player {player.name} has {player_score} points this turn."
                        )
                        turn_over = self.game_type.turn_over(dice_roll)
