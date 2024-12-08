import random
from dataclasses import dataclass, field
from typing import List, Dict, Tuple


# Game Data Classes
@dataclass(frozen=True)
class Player:
    name: str
    score: int = 0


@dataclass(frozen=True)
class GameState:
    players: List[Player]
    target_score: int
    num_dice: int
    current_player_index: int = 0


@dataclass(frozen=True)
class TurnResult:
    updated_state: GameState
    roll_scores: List[int]
    turn_score: int
    turn_over: bool


# Pure Utility Functions
def roll_dice(num_dice: int) -> List[int]:
    """Simulate rolling a given number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def calculate_turn_score(dice: List[int]) -> int:
    """Calculate score for the current dice roll."""
    return 0 if 1 in dice else sum(dice)


def get_next_player_index(current_index: int, total_players: int) -> int:
    """Get the index of the next player in a round-robin fashion."""
    return (current_index + 1) % total_players


# Game Logic Functions
def play_turn(state: GameState, roll_decision_fn) -> TurnResult:
    """Simulate a single turn and return the updated game state."""
    player = state.players[state.current_player_index]
    turn_score = 0
    roll_scores = []
    turn_over = False

    while not turn_over:
        dice = roll_dice(state.num_dice)
        roll_scores.append(dice)
        roll_score = calculate_turn_score(dice)

        if roll_score == 0:
            # Player rolled a 1; turn is over with no points
            turn_over = True
            return TurnResult(state, roll_scores, 0, turn_over)

        turn_score += roll_score

        # Check if player wins during this turn
        if player.score + turn_score >= state.target_score:
            updated_players = [
                Player(
                    p.name, p.score + turn_score if p.name == player.name else p.score
                )
                for p in state.players
            ]
            updated_state = GameState(
                players=updated_players,
                target_score=state.target_score,
                num_dice=state.num_dice,
                current_player_index=state.current_player_index,
            )
            return TurnResult(updated_state, roll_scores, turn_score, True)

        # Decide whether to roll again
        turn_over = not roll_decision_fn(player, turn_score)

    # Update player score after the turn ends
    updated_players = [
        Player(p.name, p.score + turn_score if p.name == player.name else p.score)
        for p in state.players
    ]
    updated_state = GameState(
        players=updated_players,
        target_score=state.target_score,
        num_dice=state.num_dice,
        current_player_index=get_next_player_index(
            state.current_player_index, len(state.players)
        ),
    )
    return TurnResult(updated_state, roll_scores, turn_score, turn_over)


def check_winner(state: GameState) -> List[Player]:
    """Return a list of players who have reached or exceeded the target score."""
    return [player for player in state.players if player.score >= state.target_score]


# I/O Functions (Non-Pure)
def display_roll(player: Player, roll: List[int]):
    """Display the dice roll."""
    print(f"{player.name} rolled {roll}")


def display_turn_score(player: Player, turn_score: int, total_score: int):
    """Display the player's turn score."""
    print(f"Turn score: {turn_score}, Total if banked: {total_score}")


def display_winner(winners: List[Player]):
    """Display the game winner(s)."""
    if len(winners) == 1:
        print(f"\n{winners[0].name} wins with {winners[0].score} points!")
    else:
        print(
            f"\nIt's a tie! Players {', '.join([p.name for p in winners])} "
            f"are tied with {winners[0].score} points."
        )


def prompt_roll_decision(player: Player, turn_score: int) -> bool:
    """Prompt the player to decide whether to roll again."""
    while True:
        decision = (
            input(
                f"{player.name}, your turn score is {turn_score}. Roll again? (y/n): "
            )
            .strip()
            .lower()
        )
        if decision in {"y", "n"}:
            return decision == "y"
        print("Invalid input! Please enter 'y' or 'n'.")


# Game Flow (Pure Logic)
def game_loop(state: GameState, roll_decision_fn) -> GameState:
    """The main game loop that progresses the game until a winner is found."""
    while True:
        player = state.players[state.current_player_index]
        print(f"\n{player.name}'s turn! Current score: {player.score}")

        # Play the turn
        turn_result = play_turn(state, roll_decision_fn)
        state = turn_result.updated_state

        # Display rolls and turn results
        for roll in turn_result.roll_scores:
            display_roll(player, roll)
        display_turn_score(
            player, turn_result.turn_score, player.score + turn_result.turn_score
        )

        # Check for winners
        winners = check_winner(state)
        if winners:
            display_winner(winners)
            break

    return state


# Main Game Setup and Execution
def setup_game() -> GameState:
    """Set up the game with initial parameters."""
    players = [Player(name="Alice"), Player(name="Bob"), Player(name="Charlie")]
    return GameState(players=players, target_score=100, num_dice=3)


if __name__ == "__main__":
    initial_state = setup_game()
    game_loop(initial_state, prompt_roll_decision)
