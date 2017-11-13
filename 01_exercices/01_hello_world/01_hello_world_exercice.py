#!/usr/bin/env python
"""Run a script that prints "Hello World!" when run from the command line

GOAL:
    Learn how to launch scripts from the terminal (Windows, Mac, Linux).

NOTE:
    The integration of scripts from multiple languages is always going to be
    easier in Bash, so Mac and Linux users will have it easier. There are
    ways to use Bash in Windows. One of them is to install cygwin, a Linux
    emulator.

TODO:
    - Fill the code below to print "Hello World!"
    - Launch the script in one of two ways:

        1) Use the `python` command directly to tell it to execute the script:
            `python hello_world.py`

        2) For Mac and Linux: make script executable
            `chmod +x hello_world.py`
        and tell Bash to run it
            `./hello_world.py`

LEARN:
    In order to run a script, you either tell the Python program to run it or,
    better, you give instructions to Bash on the first line of the script that
    tell it what interpreter to use. We use a line beginning with `#!`, also
    known as *shebang*, followed by the interpreter to use.
    
    Instead of giving the specific path to the Python interpreter, like for
    example `#!/usr/bin/python3`, we let Bash use the Python interpreter that
    is presently used in the current Bash environment. This is what the part
    `/usr/bin/env python` does. This is MUCH BETTER than giving a specific
    interpreter path because you DO NOT KNOW which Python interpreter the user
    of your script is going to use. They may have anaconda or miniconda or
    another python interpreter installed.

CONCLUSION:
    You now know how to write simple scripts and launch them in the terminal.
    All the future exercises will use these tricks.
"""

# Print "Hello World!"
# your code here
