##### Chapter Summary (modular code) #####
# -------------------------------------- #

# Introduction to functions #
# ------------------------- #

# 1- what is the function
# are a set of instructions bundled together to achieve a specific outcome. Functions are a good alternative to having repeating blocks of code in a program. Functions also increase the reusability of code.
# also called subroutines in some programming languages and ‘methods’ in most object oriented programming languages
# Values can be passed to a function using variables – we call these parameters or arguments. Functions can also return values.

# 2- Why do we Write Functions?
# [*] They allow us to conceive of our program as a bunch of sub-steps. (Each sub-step can be its own function. When any program seems too hard, just break the overall program into sub-steps!)
# [*] They allow us to reuse code instead of rewriting it.


# Creating and calling functions #
# ------------------------------ #

# 1-  define statement, That starts with the ( def ) keyword, which is short for define
# 2- give the function a unique name just like variables make sure you respect the rules of the Python language
# 3- add an opening and closing parentheses, and then a colon.
# 4- make sure you have indents


# example

def say_hello():
    print("Hello world!")


# call a function by using its name, followed by a set of open and close parentheses

# example

say_hello()


# Setting parameters and arguments #
# -------------------------------- #

# 1- what is the parameters and arguments?
# ==> Information can be passed into functions as arguments, Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# 2- What is the difference between?
# ==> The terms parameter and argument can be used for the same thing: information that are passed into a function
# ==> A parameter is the variable listed inside the parentheses in the function definition
# ==> An argument is the value that are sent to the function when it is called

# example

def my_name(frist_name, last_name):
    print("my name is ", frist_name, last_name)


my_name("Mohamed", "ali")


# Returning values from functions #
# ------------------------------- #

# The return keyword is to return a value from the function and exit a function

# example

def calc_number(x, y):
    # the return value from this function will be total variables ==> X and Y
    return print(x + y)
    # this code not working because this code comes after the retuen keyword
    print("this not working")


calc_number(5, 10)  # the return value equal ==> 15


# Functions across languages #
# -------------------------- #

# this function in JAVA

# void say_hello() {
#     System.out.printIn("Hello world!");
# }

# void keyword in JAVA  Specifies the return type from the function, void means the function does not return a value
