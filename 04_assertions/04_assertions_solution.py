#!/usr/bin/env python3

# Documentation (docstring)
"""Make sure entered parameters are valid

Usage:
    ./<script.py> name 'password'

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

    NOTE: Entered password should be between single quotes (eg: 'PassW0rd!!!')
    to avoid problems with your terminal trying to interpret some of the
    special characters.
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
import string
import sys

# Parse user input
try:
    name = sys.argv[1]
    password = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Validate input

## Name
# Name must be 6 to 20 letters (lower or upper case)
assert len(name) >= 6 and len(name) <= 20, \
        f"Name ({name}) must have from 6 to 20 characters"

# No special characters are allowed (eg, no `~|!"/$%?&*()_`...)
invalid_in_name = [x for x in name if x not in string.ascii_letters]
assert len(invalid_in_name) == 0, \
        f"Name must contain only letters, found '{''.join(invalid_in_name)}'"

# Must be 8 to 20 characters
assert len(password) >= 8 and len(password) <= 20, \
        f"Password ({password}) must have from 8 to 20 characters"

## Password
# No invalid characters
invalid_in_password =  [x for x in password if x not in string.digits + string.ascii_letters + string.punctuation]
assert len(invalid_in_password) == 0, \
        f"Password must not contain these characters: ({''.join(invalid_in_password)})"

# At least one number
numbers = [x for x in password if x in string.digits]
assert len(numbers) >= 1, \
        "Password must contain at least one number"

# At least one lower case letter
lower_letters = [x for x in password if x in string.ascii_lowercase]
assert len(lower_letters) >= 1, \
        "Password must contain at least one lower case letter"

# At least one upper case letter
upper_letters = [x for x in password if x in string.ascii_uppercase]
assert len(upper_letters) >= 1, \
        "Password must contain at least one upper case letter"

# At least one special ascii character
symbols = [x for x in password if x in string.punctuation]
assert len(symbols) >= 1, \
        "Password must contain at least one symbol"

# Print login and password for validation using an f-string
print(f"Login: {name}\nPassword: {password}")
