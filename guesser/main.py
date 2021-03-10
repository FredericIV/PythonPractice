#!/bin/python3

import random


def find_factor(actual_local):
    """Find and return an array of factors"""
    result = []
    for i in range(2, actual_local):
        if (actual_local % i) == 0:
            result.append(i)
    return result


def compare(guess_local, actual_local):
    """Compare values and print to screen hints"""
    if guess_local == actual_local:
        print("You got it!")
        return True
    print("The number I'm thinking of is ", end="")
    if guess_local < actual_local:
        print("higher", end=" ")
    else:
        print("lower", end=" ")
    factor_array = find_factor(actual_local)
    if len(factor_array) != 0:
        print("and divisible by", factor_array[random.randrange(len(factor_array))], end=".\n")
    else:
        print("and prime.\n")


def get_guess():
    """Get and validate a guess from the user"""
    while True:
        in_guess = input("What's your guess? ")
        if in_guess.isnumeric():
            return int(in_guess)
        else:
            print("That's not a number, try again.")


actual = random.randrange(1, 1001)
print("Welcome to Guesser! Please guess a number between 1 and 1000.")
while True:
    if compare(get_guess(), actual):
        break
