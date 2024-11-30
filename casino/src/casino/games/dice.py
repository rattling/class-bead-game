import random


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
                print(f"Player {player.name} scored {player.round_score}!")
            self._update_scores()
        self._declare_winner()

    def _update_scores(self):
        highest_round_score = max(self.players, key=lambda p: p.round_score).round_score
        for player in self.players:
            if player.round_score == highest_round_score:
                print(f"Player {player.name} is a round winner!")
                player.game_score += 1

    def _declare_winner(self):
        highest_game_score = max(self.players, key=lambda p: p.game_score).game_score
        for player in self.players:
            if player.game_score == highest_game_score:
                print(f"\nPlayer {player.name} is a game winner!")


if __name__ == "__main__":
    game = Game(players=["computer", "Mike", "Anne"], num_dice=3, rounds=6)
    game.play()
