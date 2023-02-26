import art
import random


def check_number(nr, local_chosen_number, local_low, local_high):
    if nr == local_chosen_number:
        print("You guessed right.")
        return [True, local_low, local_high]
    elif nr > local_chosen_number:
        print(f"Guessed number {nr} was too high. Chosen number is lower")
        local_high = nr
        return [False, local_low, local_high]
    else:
        local_low = nr
        print(f"Guessed number {nr} was too low. Chosen number is higher")
        return [False, local_low, local_high]


def guess_number(local_low, local_high):
    roll = random.randint(1, 6)
    difference = local_high - local_low
    if roll > 4:
        try_number = random.randint(local_low+1, local_high-1)
    elif difference % 2 == 1:
        top = local_low+1 + (difference-1)/2
        try_number = random.randint(local_low+1, top)
    else:
        top = local_low + 1 + difference / 2
        try_number = random.randint(local_low+1, top)

    result_flag = False
    guess_right = False
    while not result_flag:
        result = input(f"Computer guessed number is {try_number}. Please type 'c' for correct number, 'h' if number is too high or 'l' if number is too low:    ")
        if result == "c":
            result_flag = True
            guess_right = True
        elif result == "h" and try_number > local_low + 1:
            result_flag = True
            local_high = try_number
        elif result == "l" and try_number < local_high - 1:
            result_flag = True
            local_low = try_number
        else:
            print("That is not a valid option")
    return [guess_right, local_low, local_high]


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
        chosen_number = random.randint(1, 100)
        print(f"debug mode: chosen number is {chosen_number}")
    else:
        input(f"Think of the number  which the computer will try to guess and press any key")

    while mode == "p" and 100 > lives > 0:
        print(f"You have {lives} tries to guess the number")
        player_guess = input(f"Guess a number from {low+1} to {high-1}:       ")
        if player_guess.isdigit():
            if high > int(player_guess) > low:
                [reply, low, high] = check_number(int(player_guess), chosen_number, low, high)
                if reply:
                    lives = 100
                else:
                    lives -= 1
            else:
                print(f"Your number have to be from {low} to {high}. Try again")
        else:
            print("That is not a number. At least not a valid one. Try again")

    while mode == "c" and 100 > lives > 0:
        print(f"Computer has {lives} tries to guess the number")
        print(f"Computer will try to guess a number from {low+1} to {high-1}")
        [reply, low, high] = guess_number(low, high)
        if reply:
            lives = 100
        else:
            lives -= 1

    # End of the game block
    if lives == 100 and mode == "p" or lives == 0 and mode == "c":
        print("You win")
    elif lives == 100 and mode == "c":
        print("Computer guessed your number. Game over")
    else:
        print(f"You lose. Game over. Chosen number was {chosen_number}")
    if input("Do you want to play again? Type 'y' for yes or 'n' for no:    ").lower() != "y":
        play = False
