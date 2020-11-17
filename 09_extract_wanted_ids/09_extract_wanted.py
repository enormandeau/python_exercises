#!/usr/bin/env python3

# Documentation (docstring)
"""Extract information from wanted DNA sequences

Usage:
    ./<script.py> input_file wanted_file output_file

Where:
    input_file is the name of a csv file with two columns:
        1) a sequence name
        2) the DNA sequence itself

    wanted_file is the name of a text file with one sequence name per line

    output_file is a csv file with information about the wanted sequences in
    four comma separated columns:
        1) the wanted sequences' names
        2) its length
        3) the sequence itself
        4) the reverse complement of the sequence

Note:
    Use the input files in the 09_extract_wanted folder.
"""

# Exercise
"""
GOAL:
    Read files, parse lines, store data, produce reports and outputs.

NOTE:
    This exercise builds on all the previous notions (except using compressed
    files) but takes a significant leap from them. In it, you will need to
    write more code than in previous exercises. Comments are used below to
    remind you of what steps need to be performed and in what order. It is up
    to you to implement a solution.

    Multiple solutions are possible for each step, but it is highly
    encouraged to study the provided solution and understand how, and if
    possible why, things are done the way they are done.

    Whenever you see <script.py>, use the actual name of the script instead.

TODO:
    Complete the code below to:

    1) Read `wanted_file` and store the wanted sequence names. Choose the best
    data structure to do so.

    2) Read `input_file` line by line and check if the sequence is wanted.

    3) For each wanted sequence, write the following informations to the output
    file (a csv file with four columns separated by commas and including a
    header line with the name of the columns):

        a) the wanted sequences' names
        b) its length
        c) the sequence itself
        d) the reverse complement of the sequence

    4) The templates for the `complement` and `reverse` functions are provided.
    You will need to implement them since they are used by the
    `reverse_complement` function, which you will need.

LEARN:
    Retrieving wanted data from a larger file is frequently needed. For text
    files with custom formats, parsing skills and using proper data structures
    to store information is essential.

    Take your time. There is a potentially a lot to learn from this exercise.

CONCLUSION:
    This simple exercise could probably have been done in Excel in a fraction
    of the time by most people. However, as the format complexity increases and
    file sizes reach gigabytes, scripting becomes essential.
"""

# Modules
import sys

# Functions
# TODO implement
def complement(sequence):
    """Replace the four DNA nucleotides using the following correspondance:

    A: T
    T: A
    C: G
    G: C
    """
    pass

# TODO implement
def reverse(sequence):
    """Reverse the sequence sense
    """
    pass

def reverse_complement(sequence):
    """Produce a reverse complement of the input sequence

    Nothing to implement here. This function uses the `reverse` and
    `complement` functions. You must implement these.
    """
    return reverse(complement(sequence))

# Parse user input
# TODO your code here
try:
    input_file =  # use sys.argv
    wanted_file = # use sys.argv
    output_file = # use sys.argv
except:
    print(__doc__)
    sys.exit(1)

# TODO read wanted file and store wanted sequence names

# TODO read input file and find lines with wanted sequences

# TODO for wanted sequences compute or store:
#    a) the sequence name
#    b) its length
#    c) the sequence itself
#    d) the reverse complement of the sequence

# TODO write the output in csv format, including a header line with the column
# names
