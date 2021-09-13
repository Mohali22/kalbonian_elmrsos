##### Chapter Summary ( using external code ) #####
# ----------------------------------------------- #


# Comparing types of external code #
# -------------------------------- #

# what is a external code
# It is a collection of code written by other programmers and shared with the public.
# These codes are public codes that can be used in any project to shorten the time and not write these codes from scratch.
# There are different types of external code files


# 1- module
# In Python, Modules are simply files containing Python code that can be imported inside another Python Program.
# contains code, like variables or functions
# Modules are included by keyword ==> (import)

# 2- package or a library
# library usually means collection of ready functions, classes, objects that you can use in your program.

# 3- framework
# The framework just gives you the basic structure around which you will write your code to have the greater functionality of the system.
# It will force you to work in a standard way, So indirectly It helps to make your application standardized.


# Working with a module #
# --------------------- #

# for using the (module) in any file in the project, only use the (import) keyword in any file you want to use the (module)
# be sure of the correct path to import the module
# if the module file existing in the same path for the file you want import the module into
# you can import the module file directly, like our example below
# if-else the module file existing in another path, make sure you type the correct path

# example
import testmodule  # now we able to use any function in our code

# this funcion existing in the testmodule.py file
testmodule.say_hello('Mohamed')
