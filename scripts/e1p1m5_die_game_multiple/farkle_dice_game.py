import random
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
from enum import Enum
from bidict import bidict


from casino.collection_utils import find_winners, find_in_list


"""Farkle Dice Game V1 - WYSIWYG Code Logic = Game Logic




"""

players = ["Alice", "Bob", "Charlie"]
scores = {player: 0 for player in players}


@dataclass()
class Trick:
    name: str
    score: int
    pattern: List[int]
    found_pattern: List[List[int]] = field(default_factory=list)


game_over = False
num_dice = 6
target = 1000

# Game setup
players = ["Alice", "Bob", "Charlie"]
players = ["Alice"]
scores = {player: 0 for player in players}
num_dice = 6  # Number of dice rolled per turn
game_over = False
ties = False
finish_round = True


def find_trick(tricks, name):
    for trick in tricks:
        if trick.name == name:
            return trick
    return None


def ask_for_bank():
    _input = input("Which dice do you want to bank? (space separated): ")
    return [int(x) - 1 for x in _input.split()]


def calc_tricks(tricks, raw_score, player):
    die_trick = [None] * num_dice
    raw_score_copy = raw_score.copy()
    for trick in tricks:
        found_pattern = find_in_list(trick.pattern, raw_score_copy)
        if found_pattern:
            trick.found_pattern += found_pattern
            for die in found_pattern:
                die_trick[die] = trick
                raw_score_copy[die] = 0
            print(f"{player} scored {trick.score} points with {trick.name}")

    return die_trick


def roll_dice(num_dice, player):
    raw_score = [random.randint(1, 6) for _ in range(num_dice)]
    print(f"{player} rolled {(raw_score)}")
    print(f"Sorted dice: {sorted(raw_score)}")
    return raw_score


def bank_dice(bank_idx, raw_score, die_trick):
    bank = [raw_score[i] for i in bank_idx]
    bank_score = 0
    used_dice = set()
    for die in bank_idx:
        if die not in used_dice:
            if die_trick[die]:
                trick = die_trick[die]
                if find_in_list(trick.pattern, bank):
                    bank_score += trick.score
                    used_dice |= set(trick.found_pattern)
                else:
                    print(f"Die {die} is not part of a trick. Choose again.")
                    bank_idx = ask_for_bank()
                    break
            else:
                print(f"Die {die} is not part of a trick. Choose again.")
                bank_idx = ask_for_bank()
                break
    return bank_score


def play_game(players, num_dice, target, tricks):
    # Game loop
    while True:
        for player in players:
            bank_score = 0

            print(f"\n{player}'s turn! Current score: {scores[player]}")
            while True:
                # Roll the dice and calculate tricks
                raw_score = roll_dice(num_dice, player)
                raw_score = [6, 1, 3, 1, 2, 4]  # TODO remove after debugging
                die_trick = calc_tricks(tricks, raw_score, player)
                # Check if player farkled
                if not any(die_trick):
                    print(f"{player} FARKLED! No points this turn")
                    bank_score = 0
                    break
                # Bank scores, check if dice left and if so ask if player wants to throw again
                bank_idx = ask_for_bank()
                bank_score += bank_dice(bank_idx, raw_score, die_trick)
                num_dice = len(raw_score) - len(bank_idx)
                if num_dice > 0:
                    throw_again = input("Do you want to throw again? (y/n): ")
                    if throw_again.lower() == "n":
                        break
                else:
                    # Hot dice, players throws full set again
                    num_dice = 6
            scores[player] += bank_score
            print(f"{player} banked {bank_score} points")
        if max(scores.values()) >= target:
            break
    print(f"Game over! {find_winners(scores)} won with {max(scores.values())} points")


if __name__ == "__main__":

    tricks = [
        Trick("Three 1s", 1000, [1, 1, 1]),
        Trick("Three 6s", 600, [6, 6, 6]),
        Trick("Three 5s", 500, [5, 5, 5]),
        Trick("Three 4s", 400, [4, 4, 4]),
        Trick("Three 3s", 300, [3, 3, 3]),
        Trick("Three 2s", 200, [2, 2, 2]),
        Trick("One 1", 100, [1]),
        Trick("One 5", 50, [5]),
    ]
    play_game(players, num_dice, target, tricks)


# clear up any obvious bugs
# main function and set up function
# pass callable input() rather than embed
# work with chatgpt on any function breakdowns or similar improvements one by one
# consider oop refactor one step at a time to ensure value ie. first step might just be having it all in single class with func= method
# get the oop solid
# add some basic pytests
# how to get an agent to play the game i.e. be able to dynamically respond to rolls and how to test that? simple agent that only banks
#   vs agent that never banks vs so-called optimal agent. want to program them with strategies.
#   does agent respond through command line print/input or through accessing game state more directly? and how can that work well?
#   actually it probably just through the class API! the agent will invoke the API and do stuff based on the return values
#   these agents should be invoked the integration tests basically as want the agents to work through many paths as a human would rather than specify in advance
#   which would anyway be impossible with th random element of the dice rolls
#   Should be able to assert in the aggregate and might also be some more specific tests can make. i..e let them try to break it etc.
