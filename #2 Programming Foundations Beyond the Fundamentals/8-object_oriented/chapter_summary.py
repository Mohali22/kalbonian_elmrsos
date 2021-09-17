##### Chapter Summary ( object oriented ) #####
# ------------------------------------------- #


# Introduction to object-oriented programming #
# ------------------------------------------- #

# What is Object Oriented Programming (OOP)?
# OOP is a programming paradigm built on the concept of objects that contain both data and code to modify the data.
# OOP mimics a lot of the real-world attributes of objects.
# Object-oriented code breaks a program up into smaller parts known as objects.
# Each of these objects has its own distinct focus.
# Objects communicate with each other to make the program function,
# but the division into smaller units makes the code easier to maintain and easier to reuse.
# In object-oriented code, each object has attributes and behaviors. Each attribute is data that the object has,
# and each behavior is something that the object can do. These attributes are referred to as properties,
# and the behaviors are called methods. I can use an object's methods to work with its properties,
# and I can do this anywhere in my program.
# In an object-oriented language, you create objects using a blueprint known as a class.
# A class describes the types of attributes and behaviors that an object should have.
# You can use the same class to build out multiple objects based on the same pattern but containing different property values.


# Using built-in classes #
# ---------------------- #

# Python is one of the languages that follow the object-oriented programming approach
# Many of the functions in the language depend on classes that were created before to facilitate the programming process,
# for example, When you create a list containing some data you are actually creating an instance of the class called List,
# and here you can use the methods and attributes of that class.


# example

# This variable is of type List
flips = [
    'heads',
    'tails',
    'tails',
    'heads',
    'tails',
]

# (count) is one of the methods in the list class.
# This method can be used, to find out how many similar words there are inside the instance ==> flips
print(flips.count('heads'))

# (pop) The pop method deletes the last item in the list
print(flips.pop())


# Creating custom classes and objects #
# ----------------------------------- #


# When creating a class, use the keyword class
# Then give it a name
class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        # the name and tickets variables is an attribute for any instance object from this class
        self.name = name
        self.tickets = tickets

    # the displayAttendee() and addTicket() methods will be used in any instance object from this class
    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


# here create a new instance from class ==> Attendee, and assign the name and tickets as an argument
attendee1 = Attendee('B. Giles', 2)
attendee2 = Attendee('J. Ortega', 1)

# here use the displayAttendee() method already created in ==> Attendee class
attendee1.displayAttendee()
attendee2.displayAttendee()

# here use the addTicket() method already created in ==> Attendee class
attendee2.addTicket()
attendee2.addTicket()
