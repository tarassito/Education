# This file describes mutable and immutable data types. Clearify hashable, unhashable objects in Python.

# Immutable examples
# String immutable
a = "Hello World"
b = a
a += "!!!"
print(id(a) == id(b)) #False

# Integer immutable
a = 10
b = a
a += 100

print(id(a) == id(b)) #False

# Mutable examples
# Mutable list
a = [1, 2, 3, 4]
b = a
a += [6]
print(id(a) == id(b)) #True

# Hashing example
a = hash('abc')
b = hash('abc')
c = hash('cba')
print(a == b) # True
print(c == a) # False

# hash([1, 2]) # TypeError... because list is mutable and that's why not hashable

#[:], copy,  deep copy

import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

#normal assignment
d = c
print(id(c) == id(d))  # True - d is the same object as c
print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]

# shallow copy or [:]
d = copy.copy(c)
print(id(c) == id(d))          # False - d is now a new object
print(id(c[0]) == id(d[0]))    # True - d[0] is the same object as c[0]


# deep copy
d = copy.deepcopy(c)
print(id(c) == id(d))          # False - d is now a new object
print(id(c[0]) == id(d[0]))  # False - d[0] is now a new object)
