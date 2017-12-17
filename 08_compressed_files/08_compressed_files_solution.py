#!/usr/bin/env python3

# Documentation (docstring)
"""Reading from and writing to compressed files

Usage:
    ./<script.py> input_file output_file

Where:
    input_file is the name of a compressed input text file
    output_file is the name of a compressed output text file

Note:
    The input and output text files names must end with the `.gz` extension in
    order to be treated properly.
"""

# Exercise
"""
GOAL:
    Learn to use gzip compressed text files

NOTE:
    Input and output files are sometimes going to be compressed. The `gzip`
    modules provides tools to access these files.

    Whenever you see <script.py>, use the actual name of the script instead.

TODO:
    1) Complete the code below to modify the lines read from input file by
    making the first word all CAPITAL LETTERS (use the `.upper()` method)
    and add spaces after the first word to make the second word start at
    the 16th character of the string.

    2) Print the resulting lines on screen.

    3) Write them to the compressed file.

    4) Fool around with the code to be sure you understand it.

LEARN:
    This simple `myopen` function transparently takes care of gzip compressed
    files.

CONCLUSION:
    In the next exercices, we will start using our aquired foundations to read
    data from files, sometimes more than one, extract important informations
    into appropriate data structures, print summaries, and write useful output
    files.
"""

# Modules
import gzip
import sys

# Define custom version of `open` function
def myopen(file_handle, mode="rt"):
    """Replacement for `open` function to accept gzip files

    Use gzip compression algorithm on files ending with `.gz`

    `myopen` can be used like the `open` function because it has the same
    behaviour. Namely, it returns a file handle (ie: an opened connection
    to a file).
    """

    # If filename ends with .gz, open in gzip mode
    if file_handle.endswith(".gz"):
        return gzip.open(file_handle, mode=mode)

    # Else open normally
    else:
        return open(file_handle, mode=mode)

# Parse user input
try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Note that the "t" in "wt" and "rt" is needed. If it is omitted,
# `gzip.open` will use binary encoding instead (ie: "wb" and "rb")
with myopen(output_file, "wt") as output_file_handle:
    with myopen(input_file, "rt") as input_file_handle:
        for line in input_file_handle:
            l = line.strip().split(" ")

            # Put first word in capital letters
            l[0] = l[0].upper()

            # Compute number of spaces after first word
            padding = 16 - len(l[0]) - 1

            # Create new formatted line
            formatted_line = l[0] + " " * padding + " ".join(l[1:]) + "\n"

            # Print new line
            print(formatted_line, end="")

            # Write new line to file
            output_file_handle.write(formatted_line)
