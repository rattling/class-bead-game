import random

from casino.collection_utils import find_winners

"""Pig Dice Game V1 - WYSIWYG Code Logic = Game Logic

Strengths: Simple, easy to understand, easy to implement.

Weaknesses: 
    - Difficult to extend e.g. support a rule where the game ends suddenly if a players reaches 100 VS. let all players finish the round
    - Will need new module for other games, no reuse
    - No separation of concerns, so logic will become complex for more complex games


"""

players = ["Alice", "Bob", "Charlie"]
scores = {player: 0 for player in players}

game_over = False
num_dice = 6

# Game setup
players = ["Alice", "Bob", "Charlie"]
scores = {player: 0 for player in players}
num_dice = 3  # Number of dice rolled per turn
game_over = False
ties = False
finish_round = True

# Game loop
while not game_over:
    for player in players:
        turn_score = 0
        turn_over = False

        print(f"\n{player}'s turn! Current score: {scores[player]}")
        while not turn_over:
            raw_score = [random.randint(1, 6) for _ in range(num_dice)]
            print(f"{player} rolled {raw_score}")

            if 1 in raw_score:
                print(f"{player} rolled a 1! No points for this turn!")
                turn_score = 0
                turn_over = True
            else:
                turn_score += sum(raw_score)
                print(
                    f"Turn score: {turn_score}, Total if banked: {scores[player] + turn_score}"
                )
                roll_again = input("Roll again? (y/n): ")
                if roll_again.lower() == "n":
                    turn_over = True

        scores[player] += turn_score
        print(f"{player}'s total score: {scores[player]}")

    # Check for game over condition
    if max(scores.values()) >= 100:
        winners = find_winners(scores, lambda p: scores[p])
        if len(winners) > 1:
            print(
                f"Tie! Players {', '.join(winners)} are tied with {scores[winners[0]]} points."
            )
            players = winners  # Keep only tied players in the game
        else:
            print(f"\n{winners[0]} wins with {scores[winners[0]]} points!")
            game_over = True
