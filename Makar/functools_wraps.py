from functools import wraps
from time import sleep


def sleep_for(seconds):

    def sleep_decorator(function):

        """
        Limits how fast the function is
        called.
        """

        @wraps(function)
        def wrapper():
            sleep(seconds)
            return function()
        return wrapper
    return sleep_decorator

@sleep_for(4)
def my_function():
    """
    function.
    """
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


my_function()

print (my_function.__name__)
print (my_function.__doc__)
