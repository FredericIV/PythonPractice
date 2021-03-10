#!/bin/python3


import sys


def valid_input(ask, type_in="alpha", try_again="That's not quite right; try again."):
    """Validate input"""
    if type_in == "alpha":
        while True:
            input_local = input(ask)
            if input_local.isalpha():
                return input_local.upper()
            else:
                print(try_again)
    elif type_in == "num":
        while True:
            input_local = input(ask)
            if input_local.isnumeric():
                return int(input_local)
            else:
                print(try_again)


def get_starting_word():
    if len(sys.argv) == 1:
        return valid_input("Please enter a word: ", "alpha", "That's not a word silly.")
    if len(sys.argv) == 2:
        if sys.argv[1].isalpha():
            return sys.argv[1].upper()
        else:
            print("NOT A WORD")
            raise SyntaxError
    if len(sys.argv) == 3:
        if sys.argv[1] in "-d" "d" "D" "-d" "dictionary" "DICTIONARY" "Dictionary":
            raise NotImplementedError  # TODO  Random dictionary word
    if len(sys.argv) > 3:
        print("TOO MANY ARGUMENTS\n")
        raise SyntaxError


def interface():
    pass


class CurrentView:
    """Holder and editor of the current_view"""

    def __init__(self, word_local, lives_local):
        self.guess_list = []
        self.current_view = []
        for i in range(len(word_local)):
            self.current_view.append("_")
        self.lives = lives_local

    def update(self, letter, word_local):
        if letter in self.guess_list:
            return True
        if letter not in word_local:
            self.lives -= 1
            self.guess_list.append(letter)
            return False
        for i, v in enumerate(word_local):
            if v != letter:
                continue
            self.current_view[i] = v
        self.guess_list.append(letter)
        return True


word = get_starting_word()
current_view = CurrentView(word, valid_input("How many lives would you like? ", "num"))

print("\n\n   ", *current_view.current_view)
while "_" in current_view.current_view:
    if current_view.lives == 0:
        print("You lose! The word was", word, end=".\n")
        break
    if not current_view.update(valid_input("What's your letter?"), word):
        if current_view.lives == 1:
            print("\nNope! You have", current_view.lives, "life left.")
        else:
            print("\nNope! You have", current_view.lives, "lives left.")
    print("\n")
    print("   ", *current_view.current_view)
    print("Letters Guessed:", *current_view.guess_list)
else:
    print("You win!")
