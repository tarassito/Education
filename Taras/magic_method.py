# Магічні методи


# __init__
class Planet:

    # консруктор, викликається при створенні об'єктів(після методу new). Дозволяє ініцілізувати атрибути.
    def __init__(self, name, radius):
        """Enter name and radius of the planet"""
        self.name = name
        self.radius = radius

planet3 = Planet('Earth', 6371)

print(planet3.name)
# Earth

# print(Planet.name) #AttributeError: type object 'Planet' has no attribute 'name'


# __str__ and __repr__
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
print(planet3) # __str__
print('{}'.format(planet3)) # __str__
print(repr(planet3)) # __repr__
# виклик об'єкта planet3 використовує repr. Для наглядності використовуй термінал.


# __del__
class Planet:
    # деструктор, викликається коли інстанц(напр. planet3) стає поза скоупом
    def __del__(self):
        return "Object is deleted"


# __setattr__ __getattr__ __getattribute__ __delattr__
class Planet:
    # викликається при присвоєні атрибуту
    def __setattr__(self, key, value):
        print('Add attribute {}'.format(key))
        self.__dict__[key] = len(str(value))

    # викликається, якщо атрибуту немає
    def __getattr__(self, attr):
         print("Attribute {} doesn't exist".format(attr))

    # викликається перед __getattr__, при спробі отримати значення атрибута
    def __getattribute__(self, attr):
        if attr.startswith('a'):
            raise AttributeError("ALARM!!!!!!!! Don't start attribute with 'a' ")
        return super().__getattribute__(attr)

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
# We are in delattr method, but we don't want to delete radius.

# __getattr__
planet2.air
# Attribute air doesn't exist


# __dict__ - це сховище атрибутів, які визначені користувачем
class Example:
    class_attr = 'class_attr'

    def __init__(self, name):
        self.name = name

exp1 = Example("first")
exp2 = Example("second")

print(exp1.__dict__)
# {'name': 'first'}
print(Example.__dict__)
# {'__module__': '__main__', 'class_attr': 'class_attr', ...}


# __dir__
# якщо пустий, то вертає ліст імен в даному скоупі
print(dir())
# ['Example', 'Planet', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
#  '__name__', '__package__', '__spec__', 'exp1', 'exp2', 'planet2', 'planet3']

# якщо з аргументом, то вертає всі атрибути для цього обєкту.
print(dir(exp1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'class_attr', 'name']


# __slots__
class Slotter:
    # обмежує імена атрибутів тими, які вказані в __slots__, тоді не створюється __dict__
    # навіть якщо ти створиш метод init і спробуєш визначити якісь атрибути для об'єкту, яких немає в slots, то пайтон не дозволить
    # використовується для зменшення кількості використаної пам'яті

    __slots__ = ['a', 'b']

    # def __init__(self):
    #     self.attr = "attribute"
    # AttributeError: 'Slotter' object has no attribute 'attr'


s = Slotter()
# print(s.__dict__) # AttributeError
# s.c = 1 # AttributeError
s.a = 1
print(s.a) # 1


# __prepare__ - Вертає словник, запускається перед створенням(перед __new__).
#  Викликати з type . Визначає простір імен(namespace)

# створюємо метаклас, визначаємо prepare
class EnumMeta(type):
    def __prepare__(*args):
        return AutoDict()

# створюємо dict, який рахує атрибути
class AutoDict(dict):
    def __init__(self):
        self.count = 0

    def __getitem__(self, key):
        if key.startswith("__") and key.endswith("__"):
            return super().__getitem__(key)

        self[key] = self.count
        self.count += 1


class Color(metaclass=EnumMeta):
    RED
    GREEN
    YELLOW


print(Color.RED) # 0
print(Color.GREEN) # 1
print(Color.YELLOW) # 2


# __instancecheck__ перевіряє чи об'єкт є нащадком класу
#  __subclasscheck__  перевіряє чим один клас є субкласом іншого класу
# перевизначаються в метакласі

print(isinstance(100, int)) # True
print(isinstance('a', int)) # False
print(isinstance(True, int)) # True цікавинка! Тому що issubclass(bool, int) == True


class A(object):
    pass


class B(A):
    pass

print(issubclass(B, A)) # True
print(isinstance(B, A)) # False


class Meta(type):
    def __instancecheck__(self, other):
        print('__instancecheck__ was called')

    def __subclasscheck__(self, other):
        print('__subclasscheck__ was called')
        return True


class A(metaclass=Meta):
    pass


class B(A):
    pass


obj = B()
print(isinstance(obj, A))
# __instancecheck__ was called False
print(issubclass(B, A))
# __subclasscheck__ was called True



# object
# об'єкт, з якого все наслідується. Батько всіх класів.
print(issubclass(type, object)) # True
print(issubclass(object, type)) # False
print(isinstance((1, '2', list, dict, set, A, B, A(), type), object)) # True
print(B.__mro__) # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(type.__mro__) # (<class 'type'>, <class 'object'>)
