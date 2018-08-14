# from my_package import *
# Цей вираз вказує на те, що будуть імпортнуті усі модулі з my_package, які зазначені в змінній __all__
# в __init__.py my_package
# Змінна __all__ - це є список модулі які будуть імпортнуті у випадку використання *
# __all__ = ["module_1", "module2"]
#

from import_all_examples import *

# dir() - функція, що повертає список імен, що були визначені, якщо її викликати без аргументів
# Список імен включає в себе назви функцій, змінних, модулей та інше
# Якщо викликати з аргументом dir(builtins), то можем отримати список імен built-in функцій та змінних
import builtins
print(dir(builtins)) # ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError'........]
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'echo', 'reverse']

l = [1, 2, 3]

echo.sound(l) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
reverse.sound(l) # [3, 2, 1]
returned.sound(l) # NameError: name 'returned' is not defined. Тому що імені returned нема в змінній __all__

from import_all_examples import returned
returned.sound(l) # [1, 2, 3, 3, 2, 1]