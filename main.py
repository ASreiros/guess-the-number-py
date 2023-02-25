import art
import random


def guess(nr1, nr2):
    return random.randint(nr1 + 1, nr2)


def print_terminate_warning():
    print(f"It looks like chosen number is higher than {low}, but lower that {high}.")
    print("Clearly something wrong. Game will be terminated.")


def check_number(nr, chosen_number):
    if nr == chosen_number:
        print("You guessed right.")
        return True
    elif nr > chosen_number:
        print(f"Guessed number {nr} was too high. Chosen number is lower")
        return False
    else:
        print(f"Guessed number {nr} was too low. Chosen number is higher")
        return False


play = True

while play:
    high = 101
    low = 0
    diff = ""
    mode = ""
    chosen_number = 0

    print(art.logo)
    print("Welcome to guessing game!")
    print("Who will be guessing? Choose who will be guessing?")

    while mode != "p" and mode != "c":
        mode = input("Type 'p' for player or 'c' for computer:   ").lower()
    while diff != "e" and diff != "h":
        diff = input("Choose the difficulty of the game. Type 'h' for hard or 'e' for easy:   ").lower()
    if diff == "h":
        lives = 5
    else:
        lives = 10

    if mode == "p":
        chosen_number = random.randint(1, 101)
        print(f"debug mode: chosen number is {chosen_number}")

    while mode == "p" and 100 > lives > 0:
        print(f"You have {lives} tries to guess the number")
        player_guess = input(f"Guess a number between {low+1} and {high-1}:       ")
        if player_guess.isdigit():
            if high > int(player_guess) > low:
                if check_number(int(player_guess), chosen_number):
                    lives = 100
                else:
                    lives -= 1
            else:
                print(f"Your number have to be between {low+1} and {high-1}. Try again")
        else:
            print("That is not a number. At least not a valid one. Try again")



    # End of the game block
    if lives == 100:
        print("You win")
    else:
        print("You lose. Game over")
    if input("Do you want to play again? Type 'y' for yes or 'n' for no:    ").lower() != "y":
        play = False
