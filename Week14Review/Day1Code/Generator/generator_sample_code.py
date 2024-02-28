"""
This module defines a simple generator that increments a value.
"""

def generator_increment(increment_val):
    """
    This generator takes in an increment value and adds it to a running
    total that is yielded. The generator should be initially started
    with a call to next that gets the loop going
    :return: Yield the total after adding in an increment value
    """

    i = 0
    while True:
        i += increment_val
        yield i #value of i returned. Execution pauses until next(my_gen) called again

my_gen = generator_increment(1)

print(next(my_gen)) #begins execution of generator, returns value of yield statement then pauses
print(next(my_gen)) #continues execution from yield i
print(next(my_gen)) #continues execution from yield i