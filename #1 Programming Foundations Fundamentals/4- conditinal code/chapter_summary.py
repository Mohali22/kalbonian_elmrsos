##### Chapter Summary (conditinal code) #####
# ----------------------------------------- #

# relational operators #
# -------------------- #

# 1- (  == ) ==> equal to
# 2- (  != ) ==> not equal to
# 3- (  <  )  ==> less than
# 4- (  >  )  ==> greater than
# 5- (  >= ) ==> greater then or equal
# 6- (  <= ) ==> less than or equal


# They are used in comparing variables
# The value of this process is ( true | false )

# example

age = 34
number = 34

result = age == number  # the result is true

num1 = 50
num2 = 51

result_number = num1 > num2  # the result is false


# if statement #
# ------------ #

# It is used for condition, if this condition is true, a specific result is displayed and if this condition is false, another result will be displayed
# ( if statement ) ==> It's called a block of code
# The Code inside the if statement body runs if the condition is true, if the condition is false the interpreter will Out from the Body of the ( if statement )
# any line of code outside of the if statement  will ignore


# example

if age == number:
    print("you are old")


print(age)  # this line not inside the ( if statement ) block, will be ignored by the interpreter


# if-else statement #
# ----------------- #

# the condition for ( else statement ) will be run if condition for ( if statement ) is false
# ( if statement ) did not come without ( else statement ) ==> Do not be a complete phrase

# example

if age == number:
    print("you are old")  # this code will be run is condition is ture
else:
    print("you are young")  # this code will be run is condition is false


# Conditionals across languages #
# ----------------------------- #

# ( if statement ) is important in any programming language, But the syntax is different between language and other
# the if statement in JAVA language Write this way


# this example for ( if statement ) in JAVA language

# if(condition here) {
#     System.out.printIn("this is result")
# }
# else {
#     System.out.printIn("this is result")
# }
