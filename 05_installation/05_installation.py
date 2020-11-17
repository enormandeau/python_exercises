#!/usr/bin/env python3

# Documentation (docstring)
"""Install scripts so they can be used from anywhere

Usage:
    <script.py>
"""

# Exercise
"""
GOAL:
    Learn about the $PATH variable and how to install scripts.

    WARNING: This will only work in Linux or Mac.

NOTE:
    Once you have a working script, it is useful to be able to use it like any
    other program on your system. Namely, you want to be able to enter the name
    of the script in the terminal without having to think about where the
    program actually is on your system.

    To do that, we have to use the $PATH variable in the Bash terminal. Follow
    the steps in the TODO section to install this script and use it from
    anywhere.

    NOTE: This will only work in Linux or MacOS. Some things are better in
    the UNIX world...
    
    Whenever you see <script.py>, use the actual name of the script instead.
    
TODO:
    1) First try launching this script from its current position with:
        `./<script.py>`

    2) Then, try launching it without the `./` part from another folder. You
    can first type `cd` to move to your home folder (supposing the script is
    not in that folder) then `05_installation.py`.
    
    That should not work. You should see a message like:
        `05_installation.py: command not found`

    3) We will now temporarilly add the folder containing the script to the
    PATH variable:
        `export PATH="$PATH:/folder/to/script/"`

    For example:
        `export PATH="$PATH:/home/user/python_exercises/05_installation/"`

    Then try to launch the script with `05_installation.py`. This should now
    work and the program will report where it was launched form and where it is
    installed.

    If this step did not work, try again and make sure your `export PATH`
    command is OK. If your terminal seems broken, close it and open a new one.
    Our modification was only temporary.

    4) If you could make it work, now we need to make the change permanent.
    This means you need to put the script somewhere where the system will
    expect it. You could put it in `/usr/local/bin`, but putting all the
    scripts in there creates a mess. The best option is to create your own
    `scripts` folder, maybe in your home folder, and then add the following
    line to your `~/.bashrc` file if you are using Linux or in
    `~/.bash_profile` if you are using a Mac. These are called *hidden* files
    so they may be hidden and you may have to tell your file browser to show
    them.

        `export PATH="$PATH:/home/user/scripts/05_installation/"`

    This will make the script available to your user from anywhere. Contrary to
    our previous method, this change is permanent. For the change to take
    effect, however, you will need to close your terminal and open a new one,
    then type `05_installation.py` to test the installation.

LEARN:
    You now know how to install scripts or programs on your Linux or Mac system
    so that they can be called from anywhere. On Windows, you will have to type
    `python3` before giving the path to the script.

CONCLUSION:
    Make a habit of creating a dedicated folder for your scripts and programs.
    Within that folder, add subfolders by projects and add these to the PATH
    variable. That way of proceeding keeps all your scripts neatly separated
    and avoids some pitfalls if two scripts ended up having the same name.
"""

# Modules
import sys
import os

# Print success message when launched
print(f"{os.path.basename(__file__)} was successfully launched!")
print("---")
print(f"You are here:      {os.path.abspath('.')}")
print(f"Script found here: {os.path.abspath(os.path.dirname(__file__))}")
