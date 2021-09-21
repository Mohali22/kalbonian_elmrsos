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


# Abstract and concrete classes #
# ----------------------------- #

# Abstract Class: An abstract class is a type of class in Java that is declared by the abstract keyword. An abstract class cannot be instantiated directly, i.e. the object of such class cannot be created directly using the new keyword. An abstract class can be instantiated either by a concrete subclass or by defining all the abstract method along with the new statement. It may or may not contain an abstract method. An abstract method is declared by abstract keyword, such methods cannot have a body. If a class contains an abstract method, then it also needs to be abstract.

# Concrete Class: A concrete class in Java is a type of subclass, which implements all the abstract method of its super abstract class which it extends to. It also has implementations of all methods of interfaces it implements.


# Interfaces #
# ---------- #
# What are Interfaces?
# Interfaces allow you to specify what methods a class should implement.
# Interfaces make it easy to use a variety of different classes in the same way. When one or more classes use the same interface, it is referred to as "polymorphism".
# In some languages such as java and PHP, Interfaces are declared with the interface keyword


# Like abstract classes, interfaces cannot be used to create objects
# Interface methods do not have a body - the body is provided by the "implement" class
# On implementation of an interface, you must override all of its methods
# Interface methods are by default abstract and public
# Interface attributes are by default public, static and final
# An interface cannot contain a constructor (as it cannot be used to create objects)


# Aggregation #
# ----------- #
