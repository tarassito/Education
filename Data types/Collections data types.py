import collections


# Counter
a = collections.Counter('superfluous')
# Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = collections.Counter('superfluous')
counter['u']
# 3

counter.most_common(2)
# [('u', 3), ('s', 2)]

b = collections.Counter('super')
a.subtract(b)
# Counter({'u': 2, 's': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 0, 'e': 0, 'r': 0})

# ----------------------------------------------------------------------------------

# namedtuple()
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
p.x
# 1
p[0]
# 1

# ----------------------------------------------------------------------------------

# ChainMap
car_parts = {
    'hood': 500,
    'engine': 5000,
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
car_pricing['hood']
# 500

# ----------------------------------------------------------------------------------

# deque
d = collections.deque('abcdefg')
for elem in d:
    print(elem.upper())
# A B C D E F G
d.append('h')
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
d.appendleft('0')
# deque(['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
d.popleft()
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])


# ----------------------------------------------------------------------------------

# OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = collections.OrderedDict(sorted(d.items()))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

new_d['atomato']  = 10
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1), ('atomato', 10)])

# ----------------------------------------------------------------------------------

# UserDict
# UserList
# UserString
