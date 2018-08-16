# __import__(name, globals=None, locals=None, fromlist=(), level=0)
"""
    The globals argument is only used to determine the context;
    they are not modified.  The locals argument is unused.  The fromlist
    should be a list of names to emulate ``from name import ...'', or an
    empty list to emulate ``import name''.
    When importing a module from a package, note that __import__('A.B', ...)
    returns package A when fromlist is empty, but its submodule B when
    fromlist is not empty.  The level argument is used to determine whether to
"""


# import main
# print(main)  # <module 'main' from '/home/oshto/Education/Ostap/import_examples/main.py'>
# CASTS TO:
# main = __import__('main', globals(), locals(), [], 0)
# print(main)  #  <module 'main' from '/home/oshto/Education/Ostap/import_examples/main.py'>


# import package.package_a.module_a
# print(package.package_a.module_a)  # <module 'package.package_a.module_a' from '...package_a/module_a.py'>
# print(package)  # <module 'package' (namespace)>
# package.package_a.module_a.func_a()
# print(dir())  # ['__name__', '__package__', '__spec__', 'package']

# CASTS TO:
# package = __import__('package.package_a.module_a', globals(), locals(), [], 0)

# from package.package_a import module_a
# print(module_a)  # <module 'package.package_a.module_a' from '...package/package_a/module_a.py'>
# module_a.func_a()  # func name: func_a from package.package_a.module_a
# CASTS TO:
# _temp = __import__('package.package_a', globals(), locals(), ['module_a'], 0)
# module_a = _temp.module_a
# module_a.func_a()  # func name: func_a from package.package_a.module_a

# from package.package_a.module_a import func_a, func_b
# func_a()  # func name: func_a from package.package_a.module_a
# CASTS TO:
# _temp = __import__('package.package_a.module_a', globals(), locals(), ['func_a', 'func_b'], 0)
# func_a = _temp.func_a
# func_b = _temp.func_b
# func_a()  # func name: func_a from package.package_a.module_a
# func_b()  # func name: func_b from package.package_a.module_a



# from package.package_a.module_a import *
# func_a()  # func name: func_a from package.package_a.module_a
# func_b()  # func name: func_b from package.package_a.module_a
# print(dir())  # ['__name__', '__package__', '__spec__', 'func_a', 'func_b']

# _temp = __import__('package.package_a.module_a', globals(), locals(), [None], 0)
# print(dir(_temp))  # [__name__', '__package__', '__spec__', 'func_a', 'func_b']
#
# _temp = __import__('package.package_a.module_a', globals(), locals(), [], 0)
# print(dir(_temp))  # ['__name__', '__package__', '__path__', '__spec__', 'package_a']

# import package.package_a  # package without __init__.py
# print(package.package_a)  # <module 'package.package_a' (namespace)>
# package.package_a.__path__ # _NamespacePath(['/home/oshto/Education/Ostap/import_examples/package/package_a'])
# package.package_a.module_a.func_a()  # AttributeError: module 'package.package_a' has no attribute 'module_a'
# print(dir(package.package_a))  # [ '__name__', '__package__', '__path__', '__spec__']

# import package.package_b  # package with __init__.py that import other modules
# print(package.package_b)  # <module 'package.package_b' from '/home/oshto/Education/Ostap/import_examples/package/package_b/__init__.py'>
# package.package_b.__path__ # ['/home/oshto/Education/Ostap/import_examples/package/package_b']
# package.package_b.module_b.func_b()  # func name: func_b from package.package_b.module_b
# package.package_b.module_c.func_c()  # func name: func_c from package.package_b.module_c
# print(dir(package.package_b))  # ['__name__', '__package__', '__path__', '__spec__', 'module_b', 'module_c']
# print(dir())  # ['__name__', '__package__', '__spec__', 'package']

# from package.package_b import *  # without export controll (__all__)
# print(dir())  # ['__name__', '__package__', '__spec__', 'module_b', 'module_c']

# from package.package_b import *  # without export controll (__all__)
# print(dir())  # [ '__name__', '__package__', '__spec__', 'func_b', 'func_c']
# CASTS TO
# _temp = __import__('package.package_b', globals(), locals(), ['__all__'], 0)
# print(dir(_temp))  # ['__name__', '__package__', '__path__', '__spec__', 'func_b', 'func_c', 'module_b', 'module_c']

# The import/export controls used in standart lib combine everything
# for example 'module' collections is not actually a module, actually a package that collects from few different places
# using __init__.py and __all__
# import collections # collections/__init__.py that import _collections(builtin) and _collection_abc.py
# print(__import__('_collections'))  # <module '_collections' (built-in)>
# print(dir(__import__('_collections')))  # ['OrderedDict', '__doc__', '__name__', '__package__',  'defaultdict', 'deque']
# print(__import__('_collections_abc'))  # <module '_collections_abc' from '..education/lib/python3.6/_collections_abc.py'>

# another example is asyncio
# import asyncio runs asyncio/__init__.py that contains:
# This relies on each of the submodules having an __all__ variable.
# from .base_events import *
# from .coroutines import *
# from .events import *
# from .futures import *
# from .locks import *
# from .protocols import *
# from .queues import *
# from .streams import *
# from .subprocess import *
# from .tasks import *
# from .transports import *
#
# __all__ = (base_events.__all__ +
#            coroutines.__all__ +
#            events.__all__ +
#            futures.__all__ +
#            locks.__all__ +
#            protocols.__all__ +
#            queues.__all__ +
#            streams.__all__ +
#            subprocess.__all__ +
#            tasks.__all__ +
#            transports.__all__)

# __all__ = []

# decorator for marking which name should be exported when start used.
# def export(func):
#     globals()[func.__name__] = func
#     __all__.append(func.__name__)
#     return func

# path hacking
# import asyncio
# asyncio.__path__
# asyncio.__path__.append('.')
# from asyncio.package.package_b import func_c
# func_c()

# package upgrading
# xml/__init__.py
#
# try:
#     import _xmlplus
#     import sys
#     sys.modules[__name__] = _xmlplus
# except ImportError:
#     pass

# Difference between 'python main.py' and 'python -m main'
# 1) the -m option runs as module and perform relative imports
# 2) run if exist __main__.py
# Examples of -m usage
# python -m http.server

# Module creation and import
# import types
# def import_module(modname):
#     sourcepath = modname + '.py'
#     with open(sourcepath, 'r') as f:
#         sourcecode = f.read()
#     mod = types.ModuleType(modname)
#     mod.__file__ = sourcepath
#     code = compile(sourcecode, sourcepath, 'exec')
#     exec(code, mod.__dict__)
#     return mod
#
# main = import_module('main')
# print(main)  # <module 'main' from 'main.py'>
# main.func_x()  # hello world!

# import hook
# def my_imp(name, *args, imp=__import__):
#     print('importing', name)
#     return imp(name, *args)
#
# import builtins
# builtins.__import__ = my_imp
#
# import sys  # importing sys

# from importlib.util import find_spec
# print(find_spec('collections'))
# ModuleSpec(name='collections', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f01cbd65198>,
# origin='/home/oshto/Envs/education/lib/python3.6/collections/__init__.py',
# submodule_search_locations=['/home/oshto/Envs/education/lib/python3.6/collections'])


