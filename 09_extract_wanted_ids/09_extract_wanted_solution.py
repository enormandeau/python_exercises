#!/usr/bin/env python3

# Documentation (docstring)
"""Extract information from wanted DNA sequences

Usage:
    ./<script.py> input_file wanted_file output_file

Where:
    input_file is the name of a csv file with two columns:
        1) a sequence name
        2) the DNA sequence itself

    wanted_file is the name a text file with one sequence name per line

    output_file is a csv file with information about the wanted sequences in
    four comma separated columns:
        1) the wanted sequences' names
        2) their length
        3) the sequence itself
        4) the reverse complement of the sequence
"""

# Exercise
"""
GOAL:
    Read files, parse lines, store data, and produce reports and outputs.

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
        b) their length
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
def complement(sequence):
    """Replace the four DNA nucleotides using the following correspondance:

    A: T
    T: A
    C: G
    G: C
    """
    before = "ATCG"
    after  = "TAGC"
    translation_table = str.maketrans(before, after)
    return sequence.translate(translation_table)

def reverse(sequence):
    """Reverse the sequence sense
    """
    return sequence[::-1]

def reverse_complement(sequence):
    """Produce a reverse complement of the input sequence
    """
    return reverse(complement(sequence))

# Parse user input
try:
    input_file = sys.argv[1]
    wanted_file = sys.argv[2]
    output_file = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Read wanted file and store wanted sequence names
wanted_sequences = set()

with open(wanted_file) as wanted_file_handle:
    for line in wanted_file_handle:
        wanted_sequences.add(line.strip())

# Open output file
with open(output_file, "w") as output_file_handle:

    # Write csv file header
    output_file_handle.write("Name,Length,Sequence,RevComp\n")

    # Read input file and find lines with wanted sequences
    with open(input_file) as input_file_handle:
        for line in input_file_handle:

            # Parse lines and crash on badly formed
            try:
                name, sequence = line.strip().split(",")
            except:
                print("Error: Line does not contain two comma separated columns")
                print(line)
                sys.exit(1)

            # Check if sequence is wanted
            if name in wanted_sequences:

                # Compute sequence length
                length = len(sequence)

                # Compute sequence reverse complement
                revcomp = reverse_complement(sequence)

                # Create output line and write to output file
                outfile.write(f"{name},{str(length)},{sequence},{revcomp}\n")
