# functools!!!!
from functools import partial, wraps, reduce, lru_cache, total_ordering, singledispatch


# partial
# це функція, яка приймає функцію з аргументами і повертає функцію з меншою кількістю аргументів
def greet(greeting, separator, name, emphasis):
    print(greeting + separator + name + emphasis)

newfunc = partial(greet, greeting='Hello', separator=',', emphasis='.')
newfunc(name='German') # Hello,German.
newfunc(name='Ivan') # Hello,Ivan.

newfunc2 = partial(greet, greeting='Hello', emphasis='.')
newfunc2(name='German', separator='...') # Hello...German.
newfunc2(name='Ivan', separator='..') # Hello..Ivan.

print(newfunc2.func) # <function greet at 0x7f20b2650e18>
print(newfunc2.keywords) # {'greeting': 'Hello', 'emphasis': '.'}


# приклад 2
def make_actions():
    acts = []

    def func(x, y):
        return x * y

    for i in range(5):
        acts.append(partial(func, y=i))
    return acts

for act in make_actions(): # 0, 2, 4, 6, 8,
    print(act(2), end=', ')

# partialmethod - partial, але для методів в класі


# wraps
# копіює всю інформацію функції, яку обгортаємо(її імя, з якого модуля, докстрінгу ...) в функцію обгортку
def foo():
    print("foo")

print(foo.__name__) # foo


def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__) # wrapper


def bar(func):
    @wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")


print(foo.__name__) # foo


# reduce
# приймає функцію і набір елементів, повертає результат обчислення всіх елементів.
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])) # 15
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100)) # 115
print(reduce(lambda x, y: x*y, [1, 2, 3, 4, 5])) # 120


# lru_cache - декоратор, який зберігає і повторно використовує раніше обчисленні значення(метод мемоізації)
import time
def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print('fib(25) =', fib(25))

# total_ordering - декоратор класа, який автоматично добавляє магічні методи порівнянняю Треба визначити лише
# __eq__() і один з (__lt__(), __le__(), __gt__(), __ge__())

@total_ordering
class Student:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

std1 = Student('Chak', 'Noris')
std2 = Student('Jack', 'White')

std1 >= std2


# singledispatch
@singledispatch
def fun(arg):
        print("Let me just say,", end=" ")
        return arg


@fun.register(int)
def _(arg):
        print("Strength in numbers, eh?", end=" ")
        return arg


@fun.register(list)
def _for_list(arg):
    print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)
    return "Enumeration finished!"

print(fun(1)) # Strength in numbers, eh? 1
print(fun([2, 3, 4, 10])) # Enumerate this: 0 2, 1 3, 2 4, 3 10  Enumeration finished!
print(fun('Hi')) # Let me just say, Hi

print(fun.registry.keys()) # dict_keys([<class 'object'>, <class 'int'>, <class 'list'>])
print(fun.registry[list]) # <function _for_list at 0x7fd8a12b58c8>
