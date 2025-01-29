from unittest.mock import patch

from prototypes.standalone_farkle import Trick, play_game, scores


from unittest.mock import patch
import pytest


def mock_input(prompt):
    """Custom mock input to handle different prompts."""
    if "Which dice do you want to bank?" in prompt:
        return "all"  # Always bank all tricks
    elif "Do you want to throw again?" in prompt:
        return "n"  # Always stop after the first roll
    else:
        raise ValueError(f"Unexpected input prompt: {prompt}")


def test_play_game_bank_all():
    target = 500
    players = ["Alice"]

    # Patch input with custom mock logic
    with patch("builtins.input", side_effect=mock_input):
        play_game(players, num_dice=6, target=target)
