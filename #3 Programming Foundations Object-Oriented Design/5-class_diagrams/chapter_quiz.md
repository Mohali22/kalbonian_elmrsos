# These are the answers to the chapter five quiz

## Question 1
In which language is the following class specification written?

```
class Dog():
      def __init__(self):
#instance variables
      self.breed=""
       self.weight=50
#methods
```

## Answer 1
Python

## Question 2
Instantiating a class in many languages looks similar to that in C++, DinnerPlate *myPlate = new DinnerPlate(). What is the main difference between Python and Swift for achieving the same goal?

## Answer 2
the absence of the word new

## Question 3
A class Dog has the following constructors:

```
public Dog() 
public Dog(String breed)
public Dog(int weight)
```

## Answer 3
How would you instantiate a Dog with the weight set in Java?

## Question 4
Which languages require the use of static to declare class-wide variables or methods?

## Answer 4
Java and C#

## Question 5
Which class diagram correctly specifies data types and default values?

## Answer 5
```
Asteroid
size: Integer=5
position: Coordinate=(0.5,0.5,0.6)
velocity: Coordinate=(1,0,0)
```

## Question 6
Which is the function of a finalizer or destructor?

## Answer 6
to relinquish resources that are no longer needed

## Question 7
How would you declare a class variable in Ruby named maxScore?

## Answer 7
@@maxScore

## Question 8
A class diagram contains the following behavior specifications. Which data type is returned by the accelerate() behavior?

```
move(Direction)
accelerate(Acceleration): Velocity
setPosition(Coordinate)
explodePieces(Integer)
```

## Answer 8
Velocity

## Question 9
A class diagram contains the following behavior specifications. The explodePieces() behavior breaks up an object into a number of pieces. What is the data type for that number? The answer will take the place of the '???'.

```
move(Direction)
accelerate(Acceleration): Velocity
setPosition(Coordinate)
explodePieces(???)
```

## Answer 9
Integer

## Question 10
For which case would the use of a static attribute be appropriate?

## Answer 10
the weather conditions for each house in a small neighborhood

## Question 11
In which language would you find the following declaration of an instance variable?

```
private var _size: Int
```

## Answer 11
Swift


## Question 12
What other terminology is used for variables that are declared static?

## Answer 12
class or shared


## Question 13
What does the value (0.5,0.5,0.5) indicate in the class diagram specification position: Coordinate = (0.5,0.5,0.5)?

## Answer 13
a default value of the position attribute

## Question 14
In a UML class diagram, how would you write an attribute called Name that is a String data type and has a default value of Jane?


## Answer 14
Name: String = "Jane"

## Question 15
In the class diagram specification setSize(Integer):Integer, to what do the integer specifications refer?

## Answer 15
the data types for the argument, and return of the function setSize

## Question 16
Which line of Java code declares a public method called getName that accepts no arguments and returns a String value?

## Answer 16
```
public String getName()
```

## Question 17
Which line of Java code will instantiate a new object named Student from the Person class?

## Answer 17
```
Person Student = new Person()
```

## Question 18
Which is the purpose of a constructor?

## Answer 18
to initialize attribute values

## Question 19
The class Person has the following constructors:

```
public Person()
public Person(String name)
public Person(int age)
```

Which one will be called when a new person is created with the following command?

```
Person Steve = new Person(39)
```

## Answer 19
```
Person(int age)
```

## Question 21
What does it mean if a class attribute is private?

## Answer 21
It can only be accessed from within the class.


## Question 22
How do you declare a private variable in Python?

## Answer 22
Python does not have private or public variables.



