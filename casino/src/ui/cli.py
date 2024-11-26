from casino.src.games.dice import Game


def main_menu():
    print(
        "Welcome to the Casino!\n"
        + "1.Play Dice Game"
        + "2. View Results\n"
        + "3. Quit\n"
    )
    return int(input())


def game_menu():
    while True:
        print("How many dice? (Hit Enter for Default of 3)\n")
        num_dice = int(input()) if input() is not None else 3
        game = Game(num_dice)
        game.play()
        print(f"You have rolled {game.play()}\n")
        print(f"Try Again? y/n")
        if input() == "n":
            return


while not quit:
    option = main_menu()
    if option == 1:
        game_menu()


if __name__ == "__main__":
    game_menu()
