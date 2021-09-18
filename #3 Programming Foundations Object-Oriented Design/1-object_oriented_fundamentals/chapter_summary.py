##### Chapter Summary ( Object-oriented fundamentals ) #####
# -------------------------------------------------------- #

# Object-oriented thinking #
# ------------------------ #

# Differences between Procedural and OOP #
# ========================================

# 1- What is Procedural Programming?
# Procedural Programming may be the first programming paradigm that a new developer will learn.
# Fundamentally, the procedural code is the one that directly instructs a device on how to finish a task in logical steps.
# This paradigm uses a linear top-down approach and treats data and procedures as two different entities.
# Based on the concept of a procedure call, Procedural Programming divides the program into procedures,
# which are also known as routines or functions, simply containing a series of steps to be carried out.
# Simply put, Procedural Programming involves writing down a list of instructions to tell the computer what it should do step-by-step to finish the task at hand.

# What is Object Oriented Programming?
# Object oriented programming can be defined as a programming model which is based upon the concept of objects.
# Objects contain data in the form of attributes and code in the form of methods.
# In object oriented programming, computer programs are designed using the concept of objects that interact with real world.
# Object oriented programming languages are various but the most popular ones are class-based,
# meaning that objects are instances of classes, which also determine their types.


# What are the advantages of object-oriented programming #
# ====================================================== #

# 1- Re-usability
# 2- Data Redundancy
# 3- Code Maintenance
# 4- Better productivity
# 5- Easy troubleshooting


# Objects #
# ======= #

# What is Object?
# Object is an instance of a class.
# An object in OOPS is nothing but a self-contained component which consists of methods and properties to make a particular type of data useful.
# For example color name, table, bag, barking.
# When you send a message to an object, you are asking the object to invoke or execute one of its methods as defined in the class.

# The object contains #
# ------------------- #

# 1- properties
# Object properties differentiate objects from other objects. The basic properties of an object are those items identified for instance
# (name - age - height)

# 2- Behaviors
# Behaviors are the tasks that an object performs
# behaviors include the fact that a person can speak, run, walk, and eat
#---------------------------------------------------------#
# Literally anything can be modelled as an object in OOP as long as it has attributes and behaviours.
# This is because the purpose of OOP is to map real-world objects and their actions.


# class #
# ===== #

# What is class?
# Class is a blueprint or a set of instructions to build a specific type of object.
# It is a basic concept of Object-Oriented Programming which revolves around real-life entities.
# Class determines how an object will behave and what the object will contain.
# can use it to create as many objects based on that class.
# Different classes let us create different types of objects
# When creating a class, use the keyword class, Then give it a name


# What is methods?
# The class contains methods and attributes that describe the object to be instantiated from this class.
# A method is a block of code or procedure that can be called to perform some action, and it may return a value.
# ==> ( methods are the verb of the class )

# What is attributes?
# Attributes are data stored inside a class or instance and represent the state or quality of the class or instance.
# One can think of attributes as noun or adjective


# There are four fundamental ideas in object-oriented programming to keep in mind when creating classes.
# And they have the names
# 1- Abstraction.
# 2- Encapsulation.
# 3- Inheritance.
# 4- Polymorphism.


# 1- Abstraction
# Data abstraction is one of the most essential and important feature of object oriented programming.
# Abstraction means displaying only essential information and hiding the details.
# Data abstraction refers to providing only essential information about the data to the outside world,
# hiding the background details or implementation.

# example of a man driving a car.
# The man only knows that pressing the accelerators will increase the speed of car or applying brakes will stop the car but he does not know about how on pressing accelerator the speed is actually increasing,
# he does not know about the inner mechanism of the car or the implementation of accelerator, brakes etc in the car.
# This is what abstraction is.


# 2- Encapsulation
# The process of wrapping up variables and methods into a single entity is known as Encapsulation.
# It is one of the underlying concepts in object-oriented programming (OOP).
# It acts as a protective shield that puts restrictions on accessing variables and methods directly,
# and can prevent accidental or unauthorized modification of data.
# Encapsulation also makes objects into more self-sufficient, independently functioning pieces.

# How is the encapsulated data accessed?
# The public setXXX() and getXXX() methods are the access points of the instance variables of the class.
# Normally, these methods are referred to as getters and setters.
# Therefore, any class that wants to access the variables should access them through these getters and setters.


# 3- Inheritance
# Inheritance in OOP is the process of inheriting properties and methods from another class without having to repeat the same properties and methods in a new class,
# in addition to taking advantage of code reuse.
# The class to be inherited from is called the superclass or parental class.
# One of the advantages of inheritance is that if you make a change in a superclass,
# It will automatically filter and affect all subclasses.


# 4- Polymorphism
