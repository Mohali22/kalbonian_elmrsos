##### Chapter Summary ( working with strings ) #####
# ----------------------------------------------- #


# Combining and manipulating strings #
# ---------------------------------- #

# concatenate, strings in programming are common
# to make a concatenate between two strings, we use the addition operator (+)
# if concatenation between number and string, python convert the number to string
# in this case, you will not be able to perform a calculation
# if you want to make a calculation,
# you need to convert a string to an integer will using a function ==> "int(here a string you want to convert to integer)"

# example

# this code ask a user what is his name, and save the value in the variable my_name
my_name = input("what's your neme?")

# here I using an addition operator (+) to concatenate between a string and a value of variable my_name
print("My name is : " + my_name)


# Finding patterns in strings #
# --------------------------- #

# often we want to deal with strings and find a specific word or convert characters from uppercase to lowercase and vice versa
# there are many functions in Python that help us with that

# example

# this code ask a user what is his first name, and save the value in the variable first_name
first_name = input("what's your first name?")

# this code ask a user what is his last name, and save the value in the variable last_name
last_name = input("what's your last name?")

# this two line of code converts the first letter in a string from lowercase to uppercase
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()

# here print this message with a first name and last of the user after converting the first letter to uppercase
# and concatenate together using an addition operator (+)
print("Hello " + first_name_cap + " " + last_name_cap)

# this variable has a string that contains two jobs
user_job = "software engineer and frontend engineer"

# in this code in search a software engineer as a job in user_job variable
find_job = user_job.find("software engineer")

# I print from index number 21 to ending the string in variable user_job ==> will be printed, frontend engineer
print(user_job[21:])
