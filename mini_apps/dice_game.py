from random import randint
from time import sleep


def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print(f"The maximum possible value is: {max_val}")

    guess = get_user_guess()
    if guess > max_val:
        print("No guessing higher than the maximum possible value!")
    else:
        print("Rolling...")
        sleep(2)
        print(f"The 1st roll is: {first_roll}")
        sleep(1)
        print(f"The 2nd roll is: {second_roll}")

        total_roll = first_roll + second_roll
        print(f"The total value is: {total_roll}")
        print("Result...")
        sleep(1)

        if guess == total_roll:
            print("You won!")
        else:
            print("You lost, try again.")


roll_dice(6)
