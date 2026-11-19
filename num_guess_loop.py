# !/usr/bin/env python3
# Created by: Sereke Asfeday
# Created on: 17, November 2026
# This program generate random number between 0 and 9 and asks user to guess
# if user guess is incorrect it will ask user to guess again until user guess the correct number
# by using while true loop.

import random


def main():

    correct_guess = random.randint(0, 9)

    while True:
        user_guess_as_str = input("Guess a number between 0 and 9: ")

        try:
            user_guess_as_int = int(user_guess_as_str)

            if user_guess_as_int >= 0 and user_guess_as_int <= 9:
                if user_guess_as_int == correct_guess:
                    print("You guessed the correct number!")
                    break
                else:
                    print("Incorrect guess, please try again.")
            else:
                print("{}, is not a between 0 and 9.".format(user_guess_as_int))

        except ValueError:
            print("{}, is not a valid number.".format(user_guess_as_str))

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
