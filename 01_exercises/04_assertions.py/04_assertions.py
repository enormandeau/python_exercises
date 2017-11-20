#!/usr/bin/env python3

# Documentation (docstring)
"""Make sure entered parameters are valid

Usage:
    ./<script.py> name password

Where:
    name: Name used for login. Must be 6 to 20 letter characters (lower or
        upper case). No special or punctuation characters are allowed.
        eg, no `~|!"/$%?&*()_`

    password: Password. Must be 8 to 20 characters. Must contain at least one:
        - number
        - lower case letter
        - upper case letter
        - punctuation ascii character
        - no special character like spaces, °, », µ, greek letters...
"""

# Exercise
"""
GOAL:
    Learn to validate input or variables with assertions.

NOTE:
    It is important when you do computations to insure that values are valid
    in the context of your computations. For example, `-400` is not a valid
    Celcius temperature and a person cannot own -3 cars. In examples like
    these, it would be good to be able to confirm that values in Celcius
    are equal to or greater than -273.15°C or that the number of owned cars
    is equal or greater than zero.
    
    Whenever you see <script.py>, use the actual name of the script instead.
    
TODO:
    1) This script asks for a login name and password. Complete the code to
    accept the user input in the `try/except` clause.

    2) User `assert` to confirm that the name and password inputs are good.
    For the password, you may need to import the `string` module and use
    some of the following:
        - string.ascii_letters
        - string.ascii_lowercase
        - string.ascii_uppercase
        - string.digits
        - string.punctuation

    3) If some of the name or password pre-requisites are not respected,
    print a useful error message.

    4) Launch the script with appropriate values 
      `./<script.py> John 32`

    5) Launch without values

    6) Launch with a wrong number of values (too few and too many)

    7) Launch with invalid name and password values

    8) Fool around with the existing code a bit to be sure you understand it.

LEARN:
    Using assertions makes code much more robust. It is much better to detect
    an invalid value as soon as possible then to risk producing results that
    are invalid.

CONCLUSION:
    You learned the basics about assertions. Use them to validate values
    through your code. Your code will be better and you will have much less
    debugging to do.

WARNING:
    Most asserts are easier than the ones we are doing in this case, but they
    are still essential to ensuring scripts produce valid results.
"""

# Modules
import sys

# Parse user input
# TODO your code here
try:
    pass
    #name = 
    #password = 
except:
    print(__doc__)
    sys.exit(1)

# example with number of cars owned:
#num_cars_list = [0, 1, 2, -2, "one", "3"]
#for num_cars in num_cars_list:
#    # num_cars must be an integer
#    assert isinstance(num_cars, int), f"({num_cars}, {type(num_cars)}): Number of owned cars must be an integer"

#    # num_cars must be >= 0
#    assert num_cars >= 0, f"({num_cars}, {type(num_cars)}): Number of owned cars must be equal to or greater than zero."

# Validate input
# name:    Name used for login. Must be 6+ letter (lower or upper case)
#     characters. No special characters are allowed
#     (eg, no `~|!"/$%?&*()_`...)
# TODO your code here

# password:   Password. Must be 8+ characters. Must contain at least one:
#     - number
#     - lower case letter
#     - upper case letter
#     - special ascii character
# TODO your code here

# Print login and password for validation using an f-string
