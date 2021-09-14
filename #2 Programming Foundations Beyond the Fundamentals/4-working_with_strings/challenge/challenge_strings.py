# this code ask the user for distance in miles, and save this value in variable ==> miles
miles = input('Enter a distance in miles: ')

# in this variable converting a value from user answer from string to float number, using the (float) function
miles_float = float(miles)

# here we multiplication the value of user after converting to float number with (1.609344) and save the output in kilometers variable
kilometers = miles_float * 1.609344

# printing this message before printing the result of the kilometers varliable value 
print('That value in kilometers is')

# printing the result
print(kilometers)