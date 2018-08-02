# This file describes built-in data types

# Number: Integer, Float, Complex
print(17 / 3) # 5.666666
print(17 // 3) # 5
print(-17 // 3) # -6
print(17 % 3) # 2
print(2 ** 2) # 4
divmod(17, 3) # 5, 2

# String

a = 'Hello World!'
print(a[:5]) # Hello
print(a[6:]) # World!
print(a * 2) # Hello World!Hello World!
print("5" * -5) # ''

print("couldn\"t") # couldn"t
print('couldn\'t') # couldn't
print("couldn't") # couldn't
print(""" This is simple to use online converter of weights and measures. Simply select
the input unit, enter the value and click "Convert" button. The value will be converted to
all other units of the actual measure. You can simply convert for example between metric,
UK imperial and US customary units system.""")

print("My name is %s" % ("Taras")) # faster but old
print("My name is {}".format("Taras"))

uni = u"Unicode text"
print(uni) # Why not unicode is returning?

str = "mary has a little lamb"
print(dir(str))
print(str.split(' ')) # ['Mary', 'has', 'a', 'little', 'lamb']
print(str.capitalize()) # Mary has a little lamb
print(str.replace('mary', 'Cherry')) # Cherry has a little lamb
print(str.find('lamb')) # 18
s = '!'
seq = ('a', 'b', 'c')
print(s.join(seq)) # a!b!c


# Boolean
a, b, c = '', [], {} # False
a, b, c = '123', [1, 2, 3], {'k': 1} # True


# Tuple
t = (1, 2, [3, 4], 2)
# a[2] = [5, 6] - don't support item assignment
t[1] # 2
print(t.index(2)) # 1
print(t.count(2)) # 2



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
#b_set.remove(1000) # Error

b_set.pop() # take random element
z_set = {1, 2, 3}
x_set = {3, 4, 5}
union_set = z_set.union(x_set) # 1, 2, 3, 4, 5 Math operator - |
intersection_set = z_set.intersection(x_set) # 3 Math operator - &
intersection_update_set = z_set.intersection_update(x_set) # None z_set = {3}
z_set.update({1, 2})
difference_set = z_set.difference(x_set) # 1, 2 Math operator - - Create new set
difference_update_set = z_set.difference_update(x_set) # None Change z_set
z_set.update({3})
symmetric_difference_set = z_set.symmetric_difference(x_set) # 1, 2, 4, 5 Math operator - ^


z_set.isdisjoint(x_set) # False ; True if no intersection
z_set.issubset(x_set) # False; True if another set contains this set
z_set.issuperset(x_set) # False; True if this set contains another set


# Dictionary
keys = {'a', 'b', 'c', 'd'}
values = '1'
dic = dict.fromkeys(keys, values)
# {'d': '1', 'c': '1', 'b': '1', 'a': '1'}
# dic['z'] # KeyError
dic.get('z')
# None
dic.get('x', 10)
# 10
dic.setdefault('z')
# {'d': '1', 'b': '1', 'a': '1', 'c': '1', 'z': None}
dic.setdefault('x', 42)
# 42
dic
# {'a': '1', 'c': '1', 'd': '1', 'b': '1', 'z': None, 'x': 42}


a_dict = {'Name': 'Taras', 'DOB': 20}
keys = ('Name', "User")
values = ['Taras', 'tarassito']
a_dict = dict(zip(keys, values))

a_dict['User'] = 'tarassito'
# {'DOB': 20, 'Name': 'Taras', 'User': 'tarassito'}
print('Name' in a_dict)
# True
print('Name' in a_dict.keys())
# True
print('Name' in a_dict.values())
# False
print(('Name','Taras' in a_dict.values()))
# False
a_dict.clear()
# {}


[i for i in a_dict]
# ['Name', 'User'] iteration by key
[i for i in a_dict.items()]
# [('Name', 'Taras'), ('User', 'tarassito')] Iteration by key and value

