from time import sleep,time

########## decorators ###############################

def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time()
        some_function()
        t2 = time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

# decorator with params
def sleep_for(seconds):
    def sleep_decorator(function):

        """
        Limits how fast the function is
        called.
        """

        def wrapper():
            sleep(seconds)
            return function()
        return wrapper
    return sleep_decorator
##########################################################


# @timing_function
@sleep_for(1)
def my_function():
    """
    my_function.
    """
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


def function():
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
# the same ass with @
timing_function(sleep_for(3)(function()))
