import random

from casino.collection_utils import find_winners


class Die:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)


class Cup:
    def __init__(self, num_dice):
        self.dice = [Die() for _ in range(num_dice)]

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
    def __init__(self, players, num_dice, rounds):
        self.players = [Player(name) for name in players]
        self.cup = Cup(num_dice)
        self.rounds = rounds

    def play(self):
        print("Let's play!\n\n")
        for round in range(self.rounds):
            print(f"\n\nRound {round+1}. Let's go!")
            for player in self.players:
                player.round_score = player.play_turn(self.cup)
            round_winners = find_winners(self.players, lambda p: p.round_score)
            for winner in round_winners:
                print(f"Player {winner.name} is a round winner!")
                winner.game_score += 1

        game_winners = find_winners(self.players, lambda p: p.round_score)
        for winner in game_winners:
            print(f"\nPlayer {winner.name} is a game winner!")


if __name__ == "__main__":
    game = Game(players=["computer", "Mike", "Anne"], num_dice=3, rounds=6)
    game.play()
