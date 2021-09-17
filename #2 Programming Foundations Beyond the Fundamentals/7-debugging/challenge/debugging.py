# wrong example

def plant_recommendation(care):
    # There is a missing equals sign because the equals one sign means that we assign a value to the variable
    # We want to compare the value of the variable with the return value of the function,
    # and for this we need another equal sign
    if care = 'low':
        print('aloe')
    elif care == 'medium':  # here the value medium is repeated in another line of the code, so it will print only the first result of the condition
        print('pothos')
    elif care == 'medium':  # This condition has the same value in the previous line, so this condition is not printed. Here we want to change the value for this condition so that it works correctly
        print('orchid')


# This function call is wrong because the function is not defined. The correct function name must be specified
plant_rec('low')
plant_recommendation('medium')
plant_recommendation('high')


# right example


def plant_recommendation(care):
    if care == 'low':  # Another equal sign has been added
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':  # Condition value changed
        print('orchid')


plant_recommendation('low')  # Function name was called correctly
plant_recommendation('medium')
plant_recommendation('high')
