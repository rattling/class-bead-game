import random
from typing import List, Dict, Callable
from dataclasses import dataclass
from abc import ABC, abstractmethod


class GameRules(ABC):
    """
    Abstract base class for game-specific rules.
    """

    @abstractmethod
    def calculate_score(self, dice: List[int]) -> int:
        """
        Calculate score for a roll of dice.
        """
        pass

    @abstractmethod
    def validate_move(self, dice: List[int], banked_dice: List[int]) -> bool:
        """
        Validate whether the move (banking dice) is legal.
        """
        pass

    @abstractmethod
    def has_scoring_dice(self, dice: List[int]) -> bool:
        """
        Check if there are any scoring dice in the roll.
        """
        pass

    @abstractmethod
    def should_continue(self, player_score: int, target_score: int) -> bool:
        """
        Determine if the player can or should continue their turn.
        """
        pass


class FarkleRules(GameRules):
    """
    Rules specific to Farkle.
    """

    def calculate_score(self, dice: List[int]) -> int:
        print(f"Calculating score for Farkle: {dice}")
        # Dummy scoring logic for now:
        return dice.count(1) * 100 + dice.count(5) * 50  # Example scoring

    def validate_move(self, dice: List[int], banked_dice: List[int]) -> bool:
        print(
            f"Validating Farkle move with dice: {dice}, banked: {banked_dice}"
        )
        return True  # Replace with real validation.

    def has_scoring_dice(self, dice: List[int]) -> bool:
        # Check if there are any scoring dice (1s or 5s for simplicity)
        return 1 in dice or 5 in dice

    def should_continue(self, player_score: int, target_score: int) -> bool:
        # Check if the player has reached the target or wants to continue.
        return player_score < target_score


class PigRules(GameRules):
    """
    Rules specific to Pig.
    """

    def calculate_score(self, dice: List[int]) -> int:
        print(f"Calculating score for Pig: {dice}")
        if 1 in dice:
            return 0  # Pig-specific penalty for rolling a 1.
        return sum(dice)

    def validate_move(self, dice: List[int], banked_dice: List[int]) -> bool:
        return True

    def has_scoring_dice(self, dice: List[int]) -> bool:
        return 1 not in dice

    def should_continue(self, player_score: int, target_score: int) -> bool:
        return player_score < target_score


class Die:
    def roll(self) -> int:
        return random.randint(1, 6)


class Cup:
    def __init__(self, num_dice: int):
        self.dice = [Die() for _ in range(num_dice)]

    def roll(self) -> List[int]:
        return [die.roll() for die in self.dice]


class Player:
    def __init__(self, name: str):
        self.name = name

    def bank_dice(self, dice: List[int], rules: GameRules) -> List[int]:
        print(f"{self.name}, your dice: {dice}")
        indices = input(
            "Enter indices of dice to bank (space-separated): "
        ).split()
        return [dice[int(i)] for i in indices]

    def continue_rolling(self) -> bool:
        decision = input("Do you want to roll again? (y/n): ").lower()
        return decision == "y"


class Agent(Player):
    def __init__(
        self, name: str, strategy: Callable[[List[int], GameRules], List[int]]
    ):
        super().__init__(name)
        self.strategy = strategy

    def bank_dice(self, dice: List[int], rules: GameRules) -> List[int]:
        return self.strategy(dice, rules)

    def continue_rolling(self) -> bool:
        return False  # Always stops after the first roll


@dataclass
class Game:
    players: List[Player]
    num_dice: int
    target_score: int
    rules: GameRules

    def __post_init__(self):
        self.scores = {player.name: 0 for player in self.players}
        self.cup = Cup(self.num_dice)

    def play(self):
        print(f"Starting {self.rules.__class__.__name__}!")
        while not self.is_game_over():
            for player in self.players:
                self.play_turn(player)
        self.declare_winner()

    def play_turn(self, player: Player):
        print(
            f"\n{player.name}'s turn! Current score: {self.scores[player.name]}"
        )
        banked_score = 0
        num_dice = self.num_dice

        while True:
            dice = self.cup.roll()
            print(f"Dice rolled: {dice}")

            if not self.rules.has_scoring_dice(dice):
                print(f"{player.name} FARKLED! No points this turn.")
                banked_score = 0
                break

            banked_dice = player.bank_dice(dice, self.rules)
            banked_score += self.rules.calculate_score(banked_dice)
            num_dice -= len(banked_dice)

            print(f"{player.name} banked {banked_score} points.")
            if num_dice == 0:
                print(f"Hot dice! {player.name} rolls all dice again.")
                num_dice = self.num_dice

            if not self.rules.should_continue(
                self.scores[player.name] + banked_score, self.target_score
            ):
                break

        self.scores[player.name] += banked_score
        print(f"{player.name}'s total score: {self.scores[player.name]}")

    def is_game_over(self) -> bool:
        return any(
            score >= self.target_score for score in self.scores.values()
        )

    def declare_winner(self):
        winner = max(self.scores, key=self.scores.get)
        print(f"Game over! {winner} won with {self.scores[winner]} points!")


def farkle_strategy(dice: List[int], rules: GameRules) -> List[int]:
    return [die for die in dice if die == 1 or die == 5]


if __name__ == "__main__":
    human_player = Player(name="Alice")
    farkle_agent = Agent(name="Bob", strategy=farkle_strategy)
    farkle_agent2 = Agent(name="Schmoo", strategy=farkle_strategy)

    farkle_game = Game(
        players=[farkle_agent, farkle_agent2],
        num_dice=6,
        target_score=1000,
        rules=FarkleRules(),
    )

    farkle_game.play()
