import time



######### Object itself

a = 10

print(id(a))
# 139887213020960

print(type(a))
# <class 'int'>

print(a)
# 10


########## How variables work

X = 42
Y = 42
print(X == Y)
print(X is Y)

# True
# True

X = 42123123124
Y = 421245234234
print(X == Y)
print(X is Y)

########## referrers count

import gc
import sys

a = 'asdsdgsg'
print(sys.getrefcount(a))

print(gc.get_referrers(a))
# dict with builtins and references
#######
a = 37
b = a
c = []
c.append(b)

########################## Cyclic dependancy

a = {}
b = {}
a['b'] = b # a contains ref to b
b['a'] = a # b contains ref to a
del a
del b
# del takes ref conuts and delets names, but objects refs to each other so kepps live

########## gc #############

import gc
import ctypes

# используется ctypes для доступа к объектам по адресу памяти
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # выключаем циклический GC

lst = []
lst.append(lst)

# сохраняем адрес списка lst
lst_address = id(lst)

# удаляем ссылку lst
del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

# удаляем ссылки
del object_1, object_2

# для запуска ручной сборки объектов с циклическими ссылками
# gc.collect()

# проверяем счетчик ссылок
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)
