##### Chapter Summary ( class diagrams ) #####
# ------------------------------------------ #

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
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def displayName(self):
        print('your name is:', self.neme)

    def displayAge(self):
        print('your age is: ', self.age)

    def displayAge(self):
        print('your age is: ', self.job)


# Instantiating classes #
# --------------------- #

# When creating a new instance of the class in most programming languages we use the keyword (new).
# but here I use python program language

# for creating a new instance in python writing a name class directly
# example
personOne = Person('Mohamed ali', 34, 'software engineer')


# Class with multiple constructors #
# -------------------------------- #

# A class can have multiple constructors, as long as their signature (the parameters they take) are not the same.
# You can define as many constructors as you need.
# When a Java class contains multiple constructors, we say that the constructor is overloaded (comes in multiple versions).
# This is what constructor overloading means, that a Java class contains multiple constructors.

# Here is a Java constructor overloading example:

# this code for java

# public class MyClass {

#     private int number = 0;

#     public MyClass() {
#     }

#     public MyClass(int theNumber) {
#         this.number = theNumber;
#     }
# }

# The Java class above contains two constructors.
# The first constructor is a no-arg constructor, meaning it takes no parameters (no arguments).
# The second constructor takes an int parameter.
# Inside the constructor body the int parameter value is assigned to a field, meaning the value of the parameter is copied into the field.
# The field is thus initialized to the given parameter value.

# Static attributes and methods #
# ----------------------------- #

# Static variables belong to the class, with all objects of a class sharing a single static variable. Static methods are associated with the class, not objects of the class. Static variables are used with the class name and the dot operator, since they are associated with a class, not objects of a class.


# example on static variables in Java #
# =================================== #
# A static variable is common to all the instances (or objects) of the class because it is a class level variable. In other words you can say that only a single copy of static variable is created and shared among all the instances of the class. Memory allocation for such variables only happens once when the class is loaded in the memory.

# Static variables are also known as Class Variables.
# Unlike non-static variables, such variables can be accessed directly in static and non-static methods.


# public class StaticVariable{

#   // This is a static variables
#   public static int var1;
#   public static String var2;

#   // This is a instance variables
#   public int var1;
#   public String var2;

# }


# example on static method in Java #
# ================================ #

# Here we have a static method myMethod(), we can call this method without any object because when we make a member static it becomes class level. If we remove the static keyword and make it non-static then we must need to create an object of the class in order to call it.

# public class StaticMethod
# {
#     // This is a static method
#     public static void myMethod()
#     {
#         System.out.println("myMethod");
#     }

# }

# StaticMethod.myMathod()
