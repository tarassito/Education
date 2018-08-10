# Магічні методи
# __init__


class Planet:

    # консруктор, викликається при створенні об'єктів(після методу new). Дозволяє ініцілізувати атрибути.
    def __init__(self, name, radius):
        """Enter name and radius of the planet"""
        self.name = name
        self.radius = radius

planet3 = Planet('Earth', 6371)
# planet2 = Planet.__init__(Planet, name='Venus', radius=6000) ????????????? is it possible?

print(planet3)
# <__main__.Planet object at 0x7f8c19c83d30>

# print(Planet.name) #AttributeError: type object 'Planet' has no attribute 'name'


class Planet:
    def __init__(self, name, radius):
        """Enter name and radius of the planet"""
        self.name = name
        self.radius = radius

    # для розробниківю Ціль бути однозначним. Рекомендується надавати більш точну інфу.
    def __repr__(self):
        return "{}({},{})".format(self.__class__.__name__, self.name, self.radius)


    # Для користувачів. Ціль бути читабельним. Рекомендується бути коротким і user-friendly.
    # Якщо __str__ не визначений, а __repr__ визначений, то __str__ = __repr__
    def __str__(self):
        return "A planet {} has radius {} km".format(self.name, self.radius)

planet3 = Planet('Earth', 6371)
print(planet3)
# str
print('{}'.format(planet3))
# str
print(repr(planet3))
# repr
# виклик об'єкта planet3 використовує repr. Для наглядності використовуй термінал.


class Planet:
    # деструктор, викликається коли інстанц(напр. planet3) стає поза скоупом
    def __del__(self):
        return "Object is deleted"


class Planet:
    # викликається при присвоєні атрибуту
    def __setattr__(self, key, value):
        print('Add attribute {}'.format(key))
        self.__dict__[key] = len(str(value))

    # викликається, якщо атрибуту немає
    def __getattr__(self, attr):
        print("Attribute {} doesn't exist".format(attr))

    def __delattr__(self, attr):
        print("We are in delattr method, but we don't want to delete {}.".format(attr))


planet2 = Planet()


planet2.name = 'Venus' # planet2.__setattr__(self, key, value)
# Add attribute name
print(planet2.name)
# 5

planet2.radius = 6000
# Add attribute radius

# __delattr__
delattr(planet2, 'radius')

# __getattr__
planet2.air
# Attribute air doesn't exist

# Доступ по видаленому атрибуту(delattr) не видає помилку
planet2.radius

