##### Chapter Summary ( inheritance and composition ) #####
# ------------------------------------------------------- #


# Identifying inheritance situations #
# ---------------------------------- #

# To define the relationship of inheritance between classes we use the term (IS-A)
# (IS-A) Relationship:

# In object-oriented programming, the concept of (IS-A) is a totally based on Inheritance, which can be of two types Class Inheritance or Interface Inheritance. It is just like saying "A is a B type of thing". 
# For example, Apple is a Fruit, Car is a Vehicle etc. Inheritance is uni-directional. For example, House is a Building. But Building is not a House.

# It is a key point to note that you can easily identify the (IS-A) relationship. Wherever you see an extends keyword or implements keyword in a class declaration, then this class is said to have (IS-A) relationship.


# Using inheritance #
# ----------------- #

# To make an inheritance from a specific class, each language has its own way to make an inheritance from a class, I use Python to make an inheritance from a person class

# example

# this is a super class
class Person:
    def __init__(self, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName

    def printname(self):
        print(self.firstname, self.lastname)


# this class inherit all methods and properties
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year
        
var1 = Student('Mohamed', 'Ali', 2005)
