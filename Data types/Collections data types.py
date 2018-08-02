import collections

# Counter - dict subclass for counting hashable objects
a = collections.Counter('superfluous')
# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = collections.Counter('superfluous')
counter['u']
# 3
counter['z']
# 0

counter.most_common(2)
# [('u', 3), ('s', 2)]

b = collections.Counter('super')
a.subtract(b)
# Counter({'u': 2, 's': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 0, 'e': 0, 'r': 0})

a + b
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

a - b
# Counter({'u': 1, 'f': 1, 'l': 1, 'o': 1})

# ----------------------------------------------------------------------------------

# deque - list-like container with fast appends and pops on either end
d = collections.deque('abcdefg')

d.append('h')
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
d.appendleft('0')
# deque(['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
d.popleft()
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
q = collections.deque([1, 2], maxlen=2)
# deque([1, 2], maxlen=2)
q.append(3)
# deque([2, 3], maxlen=2)

# ----------------------------------------------------------------------------------

# OrderedDict - dict subclass that remembers the order entries were added
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = collections.OrderedDict(d)
# OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
list(new_d)
# ['banana', 'apple', 'pear', 'orange']
new_d['tomato']  = 10
# OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2), ('tomato', 10)])
new_d['apple'] = 11
# OrderedDict([('banana', 3), ('apple', 11), ('pear', 1), ('orange', 2), ('tomato', 10)])

# ----------------------------------------------------------------------------------

#defaultdict - dict subclass that calls a factory function to supply missing values

# somedict = {}
# print(somedict[3])
# # KeyError

someddict = collections.defaultdict(int)
# 0

kwargs = {'a': 10, 'b': 12, 'c': 13}
d_int = collections.defaultdict(int, **kwargs)
# defaultdict(<class 'int'>, {'a': 10, 'b': 12, 'c': 13})
d_int['a']
# 10
d_int['d']
# 0
d_int
# defaultdict(<class 'int'>, {'a': 10, 'b': 12, 'c': 13, 'd': 0})
# ----------------------------------------------------------------------------------

# namedtuple() - factory function for creating tuple subclasses with named fields
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
p.x
# 1
p[0]
#1
p._fields
# ('x', 'y')
p._asdict()
# OrderedDict([('x', 1), ('y', 2)])
print(p._replace(x=10))
# Point(x=10, y=2)
p.x
# 1
p[0]
# 1

# ----------------------------------------------------------------------------------


# ChainMap
car_parts = {
    'hood': 500,
    'Turbo': 5000,
    'front_door': 750
}

car_options = {
    'A/C': 1000,
    'Turbo': 2500,
    'rollbar': 300
}

car_accessories = {
    'cover': 100,
    'hood_ornament': 150,
    'seat_cover': 99
}

car_pricing = collections.ChainMap(car_accessories, car_options, car_parts)
car_pricing['Turbo']
# 2500
car_pricing
# ChainMap({'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}, {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}, {'hood': 500, 'Turbo': 5000, 'front_door': 750})

# ----------------------------------------------------------------------------------

