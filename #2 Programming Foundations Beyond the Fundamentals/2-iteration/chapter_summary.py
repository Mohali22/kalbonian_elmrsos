##### Chapter Summary ( iteration ) #####
# ------------------------------------- #

# Introduction to iteration #
# ------------------------- #

# 1- what is iteration
# In Python, the iterative statements are also known as looping statements or repetitive statements.
# The iterative statements are used to execute a part of the program repeatedly as long as a given condition is True.

# 2- To write code that iterates,
# you commonly need a few specific pieces of information.
# First, you need to specify the data that's being iterated.
# Second, you need to describe what should happen to the data on each iteration
# Finally, you need to indicate when the loop should stop
# a bug that can occur when the ending condition is omitted or specified incorrectly
# This creates a situation where the loop never stops
# which may result in a program that freezes or stops responding, as well as heavy demand on the computer running the program,
# which could slow it down or cause it to heat up.


# Iterating through collections #
# ----------------------------- #

# Using for loops with lists or other collections allows us to work with sets of data without writing repetitive code
# For loops are typically used when the number of iterations is known before entering the loop


# example

# here I define a list because using in for loop
languages = [
    "python",
    "java",
    "ruby"
]


# 1- the (for) keyword for defining  a for loop
# 2- the variable called (lang), using to save an item different in the (languages) list and using in every loop
# 3- the (IN) keyword refers to the list, Which we want to loop the elements
# 4- the print statement will print a different item each time of iteration from (languages) list

for lang in languages:
    print(lang)


# >>> Noticeable <<<
# any statement that has an indentation inside the for loop will be an iteration


# Iterating to a custom endpoint #
# ------------------------------ #

# To use an iteration dependent on a specific condition is used the keyword called (while)
# When a specific condition is selected from the iteration loop, the condition is checked if it is true, a given command is executed, and if false, the iterator is exited


# example

# this variable will use in iteration
i = 5

# 1- (while) keyword for defining an iteration dependent on a condition
# 2- using a variable called (i) to compare the number 100
# 3- if the value of a variable (i) is less than or equal to 100 (this is true) will print the value of the variable (i)
# 4- Then increment the value of the variable (i) by 5
# 5- Then check the condition again, if the value of a variable (i) is less than or equal to 100 (this is true) will print the value of the variable (i)
# and so until the condition is false, Now the code is out

while i <= 100:
    print(i)
    i += 5
