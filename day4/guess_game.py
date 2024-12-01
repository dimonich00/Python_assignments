import random
import time


def main():
    start_info()
    game_cycle()


def start_info():
    print("Welcome to the guess game!")
    print("Creating of a secret number.", end="\r")
    time.sleep(1)
    print("Creating of a secret number..", end="\r")
    time.sleep(1)
    print("Creating of a secret number...", end="\r")
    time.sleep(1)
    print("                                              ")

    print("Please guess a number from 1 to 20")
    print("Input x for closing of the game")
    print("Input n to restart a game")
    print("Input s to see an answer")


def game_cycle():
    secret_number = create_secret_number()
    count = 0

    while True:
        input_symbol = input()
        if input_symbol == "x":
            print("Thank you for a game, goodbuy")
            break

        elif input_symbol == "n":
            secret_number = create_secret_number()
            start_info()
            count = 0

        elif input_symbol == "s":
            print(secret_number)
        else:
            try:
                player_number = int(input_symbol)
                if player_number > 0 and player_number <= 20:
                    count += 1

                    if player_number > secret_number:
                        print("smaller")
                    elif player_number < secret_number:
                        print("bigger")
                    else:
                        print(f"You win for {count} guesses")
                        count = 0
                        print(
                            "Enter n if you want to restart a game")
                else:
                    print("Number out of range")

            except ValueError:
                print("Not a number")
                continue


def create_secret_number():
    return random.randint(1, 20)


main()
