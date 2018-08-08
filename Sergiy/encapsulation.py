#Інкапсуляція – механізм, який поєднує дані та методи, що обробляють ці дані і захищає і те і інше від зовнішнього впливу або не вірного використання.

class Car:

    def __init__(self):
        self.__maxspeed = 200
        self._name = "Supercar"
        self.driver = "Jack"

    def getMaxSpeed(self):
        print('maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

    def info(self):
        print(self._name, self.driver)



a = Car()
a.getMaxSpeed() # driving. maxspeed 200
a.setMaxSpeed(300)
a.getMaxSpeed() # driving. maxspeed 300

a.info()



print(a.driver) # Jack
print(a._name) # Supercar
print(a.__maxspeed) #AttributeError: 'Car' object has no attribute '__maxspeed'
print(a._Car__maxspeed)


#Descriptors

# Descriptor is to get, set or delete attributes from your object’s dictionary

#__get__, __set__, __delete__

#Descriptor protocol
#__get__(self, obj, type=None), returns value
#__set__(self, obj, value), returns None
#__delete__(self, obj), returns None

class AccessDescr(object):
    """Data descriptor that sets  and returns values
       and prints message about access to attribute.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Getting', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class MyClass():
    x = AccessDescr(10, 'var "x"')
    y = 5

m = MyClass()
print(m.x) # Getting var "x" 10
m.x = 20 # Updating var "x"
print(m.x) # Getting var "x" 20
print(m.y) # 5


#Property
#A call to the property () is enough to create
# a data descriptor that calls the desired functions at
# the access to the attribute

property(fget=None, fset=None, fdel=None, doc=None)

class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm attribute 'x'.")