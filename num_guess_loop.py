#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 15th, 2023
# This program asks the user to guess a number between 0 and 9
# and tells the user if they got it correct, using random numbers,
# with a do while loop
import random


def main():
    # Generate random number between 0 and 9
    correct_guess = random.randint(0, 9)

    while True:
        # Get the user's guess
        user_guess_string = input("Guess a number between 0 and 9: ")

        # Making sure the user's guess is an integer
        try:
            user_guess_int = int(user_guess_string)

            if user_guess_int < 0:
                print(
                    "{} is not a positive integer. Guess again.".format(user_guess_int)
                )

            else:
                # Check if the user's guess is correct
                if correct_guess == user_guess_int:
                    break
                else:
                    print("{} is not correct. Guess again.".format(user_guess_int))
        except:
            # If the user did not enter an integer
            print("{} is not an integer. Guess again.".format(user_guess_string))

    # Tell the user they guessed correctly
    print("You have guessed the correct number!")


if __name__ == "__main__":
    main()
