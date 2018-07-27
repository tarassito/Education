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


