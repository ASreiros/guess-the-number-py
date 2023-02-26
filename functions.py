import random
import art
EASY_GAME_LIVES = 5
HARD_GAME_LIVES = 10


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


def start():
    diff = ""
    mode = ""
    while mode != "p" and mode != "c":
        mode = input("Type 'p' for player or 'c' for computer:   ").lower()
    while diff != "e" and diff != "h":
        diff = input("Choose the difficulty of the game. Type 'h' for hard or 'e' for easy:   ").lower()
    if diff == "h":
        lives = EASY_GAME_LIVES
    else:
        lives = HARD_GAME_LIVES

    if mode == "p":
        chosen_number = random.randint(1, 100)
        # print(f"debug mode: chosen number is {chosen_number}")
    else:
        input(f"Think of the number  which the computer will try to guess and press any key")
        chosen_number = 0
    return [mode, diff, chosen_number, lives]


def greet():
    print(art.logo)
    print("Welcome to guessing game!")
    print("Who will be guessing? Choose who will be guessing?")