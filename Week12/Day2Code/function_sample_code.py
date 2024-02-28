"""
This module defines a simple function that increments a value.
"""

def function_increment(increment_val):
    """
    This function takes in an increment value and adds it to a running
    total that is returned.
    :return: the total after adding in an increment value
    """

    i = 0
    while True:
        i += increment_val
        return i #value of i returned. Execution pauses until next(my_gen) called again

print(function_increment(1)) #begins execution of function, returns value of return statement
print(function_increment(1)) #begins execution of function, returns value of return statement
print(function_increment(1)) #begins execution of function, returns value of return statement