##### Chapter Summary ( collections ) #####
# --------------------------------------- #

# collections #
# ----------- #

# 1- what is collections
# a collection in programming lets me group similar items together using a single name, which is known as a variable.
# Organizing data in this way has a few advantages.
# First, creating a collection uses your code structure to indicate that multiple pieces of data are related.
# So, rather than storing a bunch of values and needing to identify which ones are relevant for different processes in my program, all the related data is grouped in a single place.
# Second, using a collection avoids creating a potentially huge number of variables to track within my code.
# Instead, all the related data is stored under the same variable name with syntax to retrieve or change the specific data I need at any point. And finally, it's common to need to access multiple related pieces of data and then perform the same process on each piece of data.
# A collection offers simplified syntax for performing this type of process.
# Collections can take different forms and programming languages vary in the types of collections they support.
# Learning how to create and use collections in programming will help you to write more efficient and better organized code that can easily work with data from a wide variety of sources.


# Creating simple collections #
# --------------------------- #

# 1- LIST ==> A list is a type of collections in Python that is a mutable,or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item.
# lists are defined by having values between square brackets [ ].

# 2- Features of list
# Lists are used to store multiple items in a single variable.
# Lists are great to use when you want to work with many related values.
# They enable you to keep data together that belongs together, condense your code, and perform the same methods and operations on multiple values at once.

# 3- List Items
# The items in the list are written between double quotes or single quotes if they are of a type of strings and if they are numbers written without quotes
# Each item in the list is separated by a ==> ( , )


# example

list_name = [
    "Mohamed",
    'ali',
    34,
]


# Creating more complex collections #
# --------------------------------- #

# 1- what is dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.

# 2- Syntax for Dictionary
# Dictionary is listed in curly brackets, inside these curly brackets {}, keys and values are declared.
# Each key is separated from its value by a colon (:), while commas (,) separate each element.

# example

dict_name = {
    "name": "Mohamed ali",
    "age": 34,
    "email": "dev.mohali22@gmail.com",
}


# Working with collections #
# ------------------------ #

# 1- List items are indexed, the first item has index [0], the second item has index [1] etc.
# you can access them by referring to the index number
# Choose the name of the variable or the name of the list and open square brackets ==> [],
# and then write the index number inside the square brackets ==> [1]

# example

list_name = [
    "Mohamed",
    'ali',
    34,
]

list_name[0]  # will choose item number one on the list ==> Mohamed


# 2- Dictionary items you can access by referring to its key name, inside square brackets ==> ["name_item"]

# example

dict_name = {
    "name": "Mohamed ali",
    "age": 34,
    "email": "dev.mohali22@gmail.com",
}


dict_name["age"]  # will choose item of key name (age) ==> 34
