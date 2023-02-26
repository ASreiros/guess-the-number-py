import functions

play = True

while play:
    high = 101
    low = 0
    functions.greet()
    [mode, diff, chosen_number, lives] = functions.start()

    while mode == "p" and 100 > lives > 0:
        print(f"You have {lives} tries to guess the number")
        player_guess = input(f"Guess a number from {low+1} to {high-1}:       ")
        if player_guess.isdigit():
            if high > int(player_guess) > low:
                [reply, low, high] = functions.check_number(int(player_guess), chosen_number, low, high)
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
        [reply, low, high] = functions.guess_number(low, high)
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
