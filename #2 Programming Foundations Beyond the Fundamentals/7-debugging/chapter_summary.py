##### Chapter Summary ( debugging ) #####
# ------------------------------------- #

# Introduction to debugging #
# ------------------------- #

# what is debugging?
# Debugging is the routine process of locating and removing computer program bugs, errors or abnormalities,
# which is methodically handled by software programmers via debugging tools.
# Debugging checks, detects and corrects errors (or "bugs") to allow proper program operation, according to set specifications


# There are three main types of bugs in computer programs #
# ------------------------------------------------------- #

# 1- syntax error
# A syntax error is an error in the source code of a program.
# Since computer programs must follow strict syntax to compile correctly,
# any aspects of the code that do not conform to the syntax of the programming language will produce a syntax error.

# 2- The second type of error is a runtime error, so called because the error does not appear until you run the program
# For instance, suppose you include a call to a function that isn't ever defined.
# A function call is a valid statement.
# But when the interpreter tries to run your code,
# it won't be able to find and execute the function specified in your function call

# 3- logic error
# A third type of error happens when you write code that runs but doesn't produce the results you expect.
# For instance, a loop that counts in the wrong direction continues infinitely. And as a result the program never completes execution.
# This is known as a logic error because while the statements themselves constitute valid code,
# the result of the statements isn't what you were trying to achieve when you wrote the code


# Debugging code in an IDE #
# ------------------------ #

# An integrated development environment (IDE) is software for building applications that combines common developer tools into a single graphical user interface (GUI). An IDE typically consists of:

# 1- Source code editor: A text editor that can assist in writing software code with features such as syntax highlighting with visual cues,
# providing language specific auto-completion, and checking for bugs as code is being written.

# 2- Local build automation: Utilities that automate simple,
# repeatable tasks as part of creating a local build of the software for use by the developer,
# like compiling computer source code into binary code, packaging binary code, and running automated tests.

# 3- Debugger: A program for testing other programs that can graphically display the location of a bug in the original code.


# Interpreting error messages #
# --------------------------- #

# wrong example

# Correctly define a variable
temperature = 50

# we have an error because the temp variable is not defined
if temp < 60  # here the colon is missing
# the print statement not printing anything because the string, not covering between quote
print(Bring a jacket)


# right example

# Correctly define a variable
temperature = 50

# Here is the change between the variables (temp) to (temperature)
if temperature < 60:  # Then added the colon

    # Strings, covering between quotes
    print("Bring a jacket")
