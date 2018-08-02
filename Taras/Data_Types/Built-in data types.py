# This file describes built-in data types

# Number: Integer, Float, Complex
print(17/3) # 5.666666
print(17//3) # 5
print(-17//3) # -6
print(17 % 3) # 2
print(2**2) # 4

# String

a = 'Hello World!'
print("Updated String :- ", a[:6] + 'Python') # Updated String :-  Hello Python
print(a*2) # Hello World!Hello World!

print("My name is %s" % ("Taras"))
# OR ???
print("My name is {}".format("Taras"))

# Boolean
a, b, c = '', [], {} # False
a, b, c = '123', [1, 2, 3], {'k': 1} # True

# Tuple
t = (1, 2, [3, 4])
# a[2] = [5, 6] - don't support item assignment
t[1] # 2



# Frozen set

# List
# Create, slice, add, delete
a = [1, 2, 3, 4, 5, 6]
b = list([1, 5])
print(a[2:]) # start(include) [3, 4, 5, 6]
print(a[2:4]) # stop(not include) [3, 4]
print(a[::-1]) # step [6, 5, 4, 3, 2, 1]

REVERSE = slice(None,None, -1)
print(a[REVERSE]) # [6, 5, 4, 3, 2, 1]
print(b[REVERSE]) # [5,1]

b += [1, 2] # [1, 5, 1, 2]
b.append(['yes','no']) # [1, 5, 1, 2, ['yes', 'no']]
b.extend(['Great!']) # [1, 5, 1, 2, ['yes', 'no'], 'Great!']
b.insert(4, 3) # [1, 5, 1, 2, 3, ['yes', 'no'], 'Great!']
print(b.count(1)) # 2
print(b.index(1)) # 0
# print(b.index(10)) ValueError

b.remove(['yes', 'no']) # [1, 5, 1, 2, 3, 'Great!']
d = b.pop() # [1, 5, 1, 2, 3] , d = 'Great!'
del b[0] # [5, 1, 2, 3]

# Set

a_set = {1, 2}
ls = [1, 2, 3, 4, 5, 1, 2, 3]
b_set = set(ls) # {1, 2, 3, 4, 5}
b_set.add(10) # {1, 2, 3, 4, 5, 10} - add single argument
b_set.update({20, 30, 1, 2}) # {1, 2, 3, 4, 5, 10, 20, 30}
b_set.discard(10) # {1, 2, 3, 4, 5, 20, 30}
b_set.discard(1000) # No error
# b_set.discard(1000) # Error
b_set.pop() # take random element
z_set = {1, 2, 3}
x_set = {3, 4, 5}
union_set = z_set.union(x_set) # 1, 2, 3, 4, 5
intersection_set = z_set.intersection(x_set) # 3
difference_set = z_set.difference(x_set) # 1, 2
symmetric_difference_set = z_set.symmetric_difference(x_set) # 1, 2


# Dictionary
a_dict = {'Name': 'Taras', 'DOB': 20}
a_dict['User'] = 'tarassito' # {'DOB': 20, 'Name': 'Taras', 'User': 'tarassito'}
print('Name' in a_dict) # True
print('Name' in a_dict.keys()) # True
print('Name' in a_dict.values()) # False
print(('Name','Taras' in a_dict.values())) # False
a_dict.clear() # {}
keys = ('Name', "User")
values = ['Taras', 'tarassito']
a_dict = dict(zip(keys, values))

print(a_dict)

