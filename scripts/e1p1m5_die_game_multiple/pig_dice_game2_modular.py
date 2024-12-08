import random

from casino.collection_utils import find_winners

"""Pig Dice Game V2 - Modular code using functions.

Strengths:
    - More modular, easier to extend and maintain
    - Separation of concerns, easier to understand and debug

Weaknesses: 
    - Still limited to Pig Dice game so not as reusable as it could be
    - Extensibility may become limited if more complex games are added
"""


import random
from casino.collection_utils import find_winners


# Utility Functions
def roll_dice(num_dice):
    """Rolls a given number of dice."""
    if num_dice <= 0:
        raise ValueError("Number of dice must be greater than zero.")
    return [random.randint(1, 6) for _ in range(num_dice)]


def display_roll(player, raw_score):
    """Displays the result of a player's roll."""
    print(f"{player} rolled {raw_score}")


def calculate_turn_score(raw_score):
    """Calculates the score for a single roll."""
    if 1 in raw_score:
        return 0
    return sum(raw_score)


def get_roll_decision():
    """Prompts the player to decide whether to roll again."""
    while True:
        roll_again = input("Roll again? (y/n): ").strip().lower()
        if roll_again in {"y", "n"}:
            return roll_again
        print("Invalid input! Please enter 'y' or 'n'.")


# Core Functions
def play_turn(player, current_score, num_dice, sudden_death=True):
    """Handles a single player's turn."""
    turn_score = 0
    while True:
        raw_score = roll_dice(num_dice)
        display_roll(player, raw_score)
        score = calculate_turn_score(raw_score)
        if score == 0:
            print(f"{player} rolled a 1! No points for this turn!")
            return 0  # Turn ends with no score
        turn_score += score
        print(
            f"Turn score: {turn_score}, Total if banked: {current_score + turn_score}"
        )
        # Sudden death condition
        if sudden_death and current_score + turn_score >= 100:
            return turn_score
        roll_again = get_roll_decision()
        if roll_again == "n":
            break
    return turn_score


def handle_player_turn(player, scores, num_dice, sudden_death):
    """Manages a single player's turn and updates their score."""
    print(f"\n{player}'s turn! Current score: {scores[player]}")
    turn_score = play_turn(player, scores[player], num_dice, sudden_death)
    scores[player] += turn_score
    print(f"{player}'s total score: {scores[player]}")
    return scores


def declare_winner(winners, scores):
    """Declares the winner or handles ties."""
    if len(winners) == 1:
        winner = winners[0]
        print(f"\n{winner} wins with {scores[winner]} points!")
    else:
        print(
            f"\nTie! Players {', '.join(winners)} are tied with {scores[winners[0]]} points."
        )


def check_winner(scores, sudden_death):
    """Checks for winners based on game state."""
    max_score = max(scores.values())
    if sudden_death:
        # Sudden death: A single winner immediately ends the game
        winners = [player for player, score in scores.items() if score >= 100]
        return winners if len(winners) == 1 else []
    else:
        # After a round, check for multiple winners
        return find_winners(scores, lambda p: scores[p]) if max_score >= 100 else []


def handle_tiebreakers(players, scores):
    """Handles tiebreakers when multiple players have the highest score."""
    print(
        f"Tie! Players {', '.join(players)} are tied with {scores[players[0]]} points."
    )
    return players  # Return the tied players for the next round


def end_round(scores, sudden_death, players):
    """Handles the end-of-round logic, including winner checks."""
    winners = check_winner(scores, sudden_death)
    if winners:
        declare_winner(winners, scores)
        if len(winners) == 1:
            return True, players  # Game over
        return False, winners  # Continue with tied players
    return False, players


# Game Setup
def setup_game():
    """Sets up the game by initializing players and their scores."""
    players = ["Alice", "Bob", "Charlie"]
    num_dice = 3
    scores = {player: 0 for player in players}
    return players, scores, num_dice


# Main Game Loop
def play_game(players, num_dice, sudden_death=True):
    """Plays the game of Pig."""
    scores = {player: 0 for player in players}
    game_over = False

    while not game_over:
        for player in players:
            scores = handle_player_turn(player, scores, num_dice, sudden_death)
            winners = check_winner(scores, sudden_death)
            if winners:
                declare_winner(winners, scores)
                if len(winners) == 1:
                    game_over = True
                else:
                    players = winners  # Update players to only the tied ones
                break
        if not sudden_death:  # Round-based winner check
            game_over, players = end_round(scores, sudden_death, players)


if __name__ == "__main__":
    players, scores, num_dice = setup_game()
    play_game(players, num_dice, sudden_death=True)
