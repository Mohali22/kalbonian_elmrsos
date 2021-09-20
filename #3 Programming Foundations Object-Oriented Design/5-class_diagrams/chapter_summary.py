##### Chapter Summary ( class modling ) #####
# ----------------------------------------- #

# Creating class diagrams: Attributes #
# ----------------------------------- #

# A class diagram is a diagram used in designing and modeling software to describe classes and their relationships. 
# Class diagrams enable us to model software in a high level of abstraction and without having to look at the source code.

# Classes in a class diagram correspond with classes in the source code. 
# The diagram shows the names and attributes of the classes, connections between the classes, and sometimes also the methods of the classes.

# Describing class and class attributes #
# ===================================== #
# In a class diagram, a class is represented by a rectangle with the name of the class written on top. 
# A line below the name of the class divides the name from the list of attributes (names and types of the class variables). 
# The attributes are written one attribute per line.


# Creating class diagrams: Behaviors #
# ================================== #
# In a class diagram, we list all class methods including the constructors; constructors are listed first and then all class methods. 
# We also write the return type of a method in the class diagram.

# example

# =================== #
#        Person       #
# ------------------- #
#  personName: String #
#  -id: Int           #
#  isActive: Boolean  #
# ------------------- #
# -cardId(): Int      #
# +getName(): String  #
# =================== #


#  Minus (-) indicates that a member should be private to the class, meaning it's not directly accessible by other objects
# and plus (+) means the member should be public


# Converting class diagrams into code #
# ----------------------------------- #

# When creating a class, use the keyword class
# Then give it a name
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayName(self):
        print('your name is:', self.neme)

    def addTicket(self):
        self.tickets += 1
        print('your age is: ' , self.age)



# When creating a new instance of the class in most programming languages we use the keyword (new).
# but here I use pyhon programme language

# for creating a new instance in python writing a namem class dir