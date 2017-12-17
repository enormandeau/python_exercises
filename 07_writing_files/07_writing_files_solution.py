#!/usr/bin/env python3

# Documentation (docstring)
"""Writing to text files

Usage:
    ./<script.py> input_file output_file

Where:
    input_file is the name of an input text file
    output_file is the name of an output text file
"""

# Exercise
"""
GOAL:
    Learn to write to text files

NOTE:
    What good is it to read files without being able to write to files? In this
    exercice we read lines from a file, modify them and then write them to
    another file.

    Whenever you see <script.py>, use the actual name of the script instead.

TODO:
    1) Complete the code below to modify the lines read by adding a line number
    (from 1 to the number of lines) and by making every word start with a
    capital letter (user the `.title()` method on the lines).

    2) Fool around with the code to be sure you understand it.

LEARN:
    Use this pattern whenever you need to read from and write to files.

CONCLUSION:
    In the next exercice, we will read from and write to compressed files.
"""

# Modules
import sys

# Parse user input
try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

line_number = 0
with open(output_file, "w") as output_file_handle:
    with open(input_file) as input_file_handle:
        for line in input_file_handle:
            line_number += 1
            output_file_handle.write(f"{line_number} {line.title()}")
