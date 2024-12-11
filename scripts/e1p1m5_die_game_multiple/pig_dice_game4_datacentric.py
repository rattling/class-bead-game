import random
from dataclasses import dataclass, field
from typing import List, Dict


# Game Rules
GAME_RULES = {
    "target_score": 100,  # Score needed to win
    "num_dice": 3,  # Number of dice rolled per turn
    "scoring": {
        "1": 0,  # Rolling a 1 ends the turn with no points
        "default": "sum",  # Default scoring sums the dice
    },
    "roll_again_prompt": True,  # Whether players are prompted to roll again
}


# Data Classes
@dataclass
class GameState:
    players: Dict[str, int]  # Player scores
    current_player: str  # Name of the current player
    turn_score: int = 0  # Accumulated score for the current turn
    roll_history: List[List[int]] = field(
        default_factory=list
    )  # Dice rolls in the current turn


# Utility Functions
def roll_dice(num_dice: int) -> List[int]:
    """Simulates rolling dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def apply_scoring(dice: List[int], scoring_rules: Dict) -> int:
    """Calculates the score for a dice roll based on scoring rules."""
    if "1" in scoring_rules and 1 in dice:
        return scoring_rules["1"]  # Rolling a 1 ends the turn
    if scoring_rules["default"] == "sum":
        return sum(dice)
    return 0


def check_winner(state: GameState, target_score: int) -> List[str]:
    """Returns a list of players who have reached or exceeded the target score."""
    return [player for player, score in state.players.items() if score >= target_score]


def get_next_player_index(current_player: str, players: List[str]) -> str:
    """Get the name of the next player in a round-robin fashion."""
    current_index = players.index(current_player)
    next_index = (current_index + 1) % len(players)
    return players[next_index]


# Turn Logic
def play_turn(state: GameState, rules: Dict) -> GameState:
    """Plays a single turn for the current player."""
    roll_history = []
    turn_score = 0

    while True:
        # Roll dice and calculate score
        dice = roll_dice(rules["num_dice"])
        roll_history.append(dice)
        print(f"{state.current_player} rolled {dice}")

        roll_score = apply_scoring(dice, rules["scoring"])
        if roll_score == 0:
            print(f"{state.current_player} rolled a 1! Turn over with no points.")
            return GameState(
                players=state.players,
                current_player=state.current_player,
                turn_score=0,
                roll_history=roll_history,
            )

        turn_score += roll_score
        print(f"Turn score: {turn_score}")

        # Check if player wins during the turn
        if state.players[state.current_player] + turn_score >= rules["target_score"]:
            updated_scores = {
                **state.players,
                state.current_player: state.players[state.current_player] + turn_score,
            }
            return GameState(
                players=updated_scores,
                current_player=state.current_player,
                turn_score=turn_score,
                roll_history=roll_history,
            )

        # Prompt to roll again
        if rules["roll_again_prompt"]:
            decision = (
                input(f"Roll again, {state.current_player}? (y/n): ").strip().lower()
            )
            if decision == "n":
                break

    # Update player scores at the end of the turn
    updated_scores = {
        **state.players,
        state.current_player: state.players[state.current_player] + turn_score,
    }
    return GameState(
        players=updated_scores,
        current_player=state.current_player,
        turn_score=turn_score,
        roll_history=roll_history,
    )


# Game Loop
def game_loop(state: GameState, rules: Dict):
    """The main game loop that manages player turns and determines the winner."""
    players = list(state.players.keys())

    while True:
        print(
            f"\n{state.current_player}'s turn. Current score: {state.players[state.current_player]}"
        )
        state = play_turn(state, rules)

        # Check for winners
        winners = check_winner(state, rules["target_score"])
        if winners:
            if len(winners) == 1:
                print(f"\n{winners[0]} wins with {state.players[winners[0]]} points!")
            else:
                print(
                    f"\nIt's a tie! Players {', '.join(winners)} "
                    f"are tied with {state.players[winners[0]]} points."
                )
            break

        # Move to the next player
        state.current_player = get_next_player_index(state.current_player, players)


# Setup and Execute
def setup_game() -> GameState:
    """Initializes the game state."""
    players = {"Alice": 0, "Bob": 0, "Charlie": 0}
    return GameState(players=players, current_player="Alice")


if __name__ == "__main__":
    initial_state = setup_game()
    game_loop(initial_state, GAME_RULES)
