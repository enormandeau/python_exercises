#!/usr/bin/env python3

# Documentation (docstring)
"""Learn to use the docstring

Usage:
    ./<script.py> name age

Where:
    name:   is the first name of the user <string>
    age:    is the age of the user in years <int>
"""

# Exercise
"""
GOAL:
    Learn about the docstring and how to print usage

NOTE:
    Once again, this basic method works well in a lot of cases. A more advanced
    approach using the argparse module will be covered later.
    
    Whenever you see <script.py>, use the actual name of the script instead.
    
TODO:
    1) Look at the top of the file. The first comment enclosed in triple double
    quotes is called the docstring. Inside of a Python script, this string is
    stored in a variable named `__doc__`.

    2) Look at the `try/except` clause in the code below. We re-use our simple
    sys.argv approach of parsing the user input but with a twist. We enclose
    the parsing in a `try` clause and use `except` to catch any error. In the
    case of an error, we print the docstring and exit the program. Thus, the
    user has some help message showing them how to use the script. The
    docstring is also printed if the script is launched without any input.

    3) Launch the script with appropriate values 
      `./<script.py> John 32`

    4) Launch without values

    5) Launch with a wrong number of values (too few and too many)

    6) Launch with values of the wrong type (eg: string instead of number)

    7) There is no code to write in this exercice, but you should fool around
    with the existing code a bit to be sure you understand it.

LEARN:
    This simple `try/except` clause is a powerful way to catch usage errors and
    to print help.

CONCLUSION:
    You now know about docstrings and how to use them to print help when the
    script is not used properly.

WARNING:
    In the next exercice, we will learn how to make sure the provided parameters
    are valid.
"""

# Modules
import sys

# Parse user input
try:
    name = sys.argv[1]      # user name, no need to transform since already a string
    age = int(sys.argv[2])  # in years, transform input into an integer (with `int`)
except:
    print(__doc__)
    sys.exit(1)

# Print message about the user
condition = "young" if age < 18 else "old"
print(f"Hello {name}. It seems you are {condition} enough to use docstrings!")
