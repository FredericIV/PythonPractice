#!/bin/python3

# Libraries
import sys
import array
import textwrap

# Variable Declaration
madlib_selection = "example.txt"
madlib_array = array.array('i')
copy_state = False
user_filler = ""
new_madlib = []

if len(sys.argv) != 1:
    print(len(sys.argv))
    if sys.argv[1] == "-":
        print("This program takes the path to a madlib as an argument. Showing default now.")
        ## TODO: Add input validation, i.e. make sure the input is actully text.
    else:
        ## TODO: Add pipe as input option.
        madlib_selection = sys.argv[1]

with open(madlib_selection, 'r') as madlib:
    read_madlib = madlib.read()
    for i in range(read_madlib.count("#")//2):
        first = read_madlib.index("#")
        second = read_madlib.index("#", first+1)
        replacement = input("Please give me " + read_madlib[first+1:second] + ":")
        new_madlib = read_madlib[0:first] + replacement + read_madlib[second+1:]
        read_madlib = new_madlib
    print("\n\n\n")
    print(textwrap.fill(read_madlib, drop_whitespace=False, replace_whitespace=False))
