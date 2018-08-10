'''
Metaclasses are deeper magic than 99% of users should ever worry
    about. If you wonder whether you need them, you don't (the
    people who actually need them know with certainty that they need
    them, and don't need an explanation about why).
                                            Python's superguru Tim Peters
'''


# Метакласи створюють класи
# Метаклса -> Клас -> Екземпляр класа
# type - метаклас, який Python використовує по замовченню для створення класів.
# Всі створені метакласи наслідуються від type

# type(classname, superclasses, attributes_dict)
# Простий приклад використання type
Foo = type('Foo', (), {})
print(Foo) # <class '__main__.Foo'>
print(Foo.__class__) # <class 'type'>


# Процес створення класу
# Клас є екземпляром метакласу
# a = Foo()
# 1)Викликається метод __call__() Foo, або батьківського
# 2) __call__() викликає по черзі:
#       __new__() - створює екземпляр класу
#       __init__() - ініціалізує екземпляр(присвоює змінні наприклад)

# Створимо метаклас
class ExampleMeta(type):
    def __new__(cls, name, bases, dct):
         print("Виділяєм пам'ять для класу", name)
         return type.__new__(cls, name, bases, dct)
    def __init__(cls, name, bases, dct):
         print("ініціалізуєм клас", name)
         super().__init__(name, bases, dct)
    def whoami(cls):
        print('Я клас ', cls.__name__)

MyClass = ExampleMeta('MyClass', (), {})
# Виділяєм пам'ять для класу MyClass
# Ініціалізуєм клас MyClass
MyClass.whoami() # Я клас MyClass

#Визначати який метаклас використовувати можна за допомогою атрибуту класу __metaclass__ Python2, metaclass=.... Python3
# class MyClass2():
    # __metaclass__ = ExampleMeta

class MyClass2(metaclass=ExampleMeta):
    pass
# Після визначення класу ми побачим в консолі:
# Виділяєм пам'ять для класу MyClass2
# Ініціалізуєм клас MyClass2

MyClass2.whoami() # Я клас MyClass2

#Example з першої ссилки на Хабр(доволі банальний, але для закріплення знань по метакласам саме то)
#Створимо метаклас, який при створенні екземпляра класа буде перетворювати всі атрибути класа на uppercase атрибути

class UpperMeta(type):
    def __new__(cls, name, bases, attrs_dict):
        upper_attrs = {key.upper(): value for key, value in attrs_dict.items()}
        return super().__new__(cls, name, bases, upper_attrs) # Це еквівалентно type.__new__(cls, name, bases, upper_attrs)

class LowecaseClass(metaclass=UpperMeta):
    bar = 'hello'

x = LowecaseClass()
print(x.bar) #AttributeError: 'LowecaseClass' object has no attribute 'bar'
print(x.BAR) # hello

# Підсумок(по простому)

# перехопити створення класу
# змінити клас
# повернути модифікований
