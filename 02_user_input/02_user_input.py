#!/usr/bin/env python3

# Documentation
"""Accept user input with sys.argv

Usage:
    ./<script.py> name age height

Where:
    name:   is the first name of the user <string>
    age:    is the age of the user in years <int>
    height: is the height of the user in meters <float>
"""

# Exercise
"""
GOAL:
    Learn how to take user inputs from the command line

NOTE:
    This basic method works well in a lot of cases. A more advanced approach
    with named parameters will be covered in a future exercise.
    
    Whenever you see <script.py>, use the actual name of the script instead.
    
TODO:
    1) Fill the code below to:

        a) Accept three variables from the user and change them in the
          appropriate type (eg: integer, float...)

        b) Print a sentence using these values

    2) Launch with appropriate values 
      `./<script.py> John 32 1.75`

    3) Launch without values

    4) Launch with a wrong number of values (too few and too many)

    5) Launch with values of the wrong type (eg: string instead of number)

LEARN:
    Scripts are not very useful if they cannot accept user input. This simple
    method works well in a lot of cases. Learn to use `sys.argv` to get user
    inputs as strings and transform them in another type if needed.

CONCLUSION:
    You now know how to write simple scripts that accept user inputs. This
    will be useful for most of the following exercises.

WARNING:
    This script will crash without a useful error message if the user does not
    give at least three parameters. The next exercice will give us the tools
    needed to improve this situation.
"""

# Modules
# We need the `sys` module to parse user input
import sys

# Parse user input
# use `sys.argv[i]` where `i` is the number of the argument
# TODO your code here
name = sys.argv[1]  # user name, no need to transform since already a string
age =               # in years, transform input into an integer (with `int`)
height =            # in meters, transform input into a float (with `float`)

# Print informations about the user
# For example: "Hello John! You are 32 years old and 1.75m meters tall."
# TODO your code here
