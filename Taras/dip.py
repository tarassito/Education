# The Dependency Inversion Principle - Depend on abstractions, not on concretions.

# Модулі верхніх рівнів не повинні залежати від модулів нижніх рівнів. Обидва типи модулів мають бути залежні від абстакцій.
# Абстракції не мають залежати від деталей. Деталі мають залежати від абстракцій.


class UnHappyMan:
    def __init__(self):
        self.wife = FirstWife()

    def food(self):
        return self.wife.get_food()


class FirstWife:
    @staticmethod
    def get_food():
        return "Disgusting food"


un_happy_man = UnHappyMan()
print(un_happy_man.food())

# Верхній модуль UnHappyMan залежить від нижнього модуля FirstWife. UnHappyMan не може змінити жінку.

from abc import ABC, abstractmethod


class Wife(ABC):
    @staticmethod
    @abstractmethod
    def get_food():
        pass


class FirstWife(Wife):
    @staticmethod
    def get_food():
        return "Disgusting food"


class SecondWife(Wife):
    @staticmethod
    def get_food():
        return "Tasty food"


class NormalMan:
    def __init__(self, wife):
        self.wife = wife

    def food(self):
        return self.wife.get_food()


normal_man = NormalMan(FirstWife)
print(normal_man.food())
normal_man.wife = SecondWife
print(normal_man.food())

# Може міняти їжу і жінку. Якщо чувак хоче іншу їжу, йому треба міняти жінку. Тобто Верхній клас залежить від нижнього.


from abc import ABC, abstractmethod


class GetFood(ABC):
    @staticmethod
    @abstractmethod
    def get_food():
        pass


class FirstWife(GetFood):
    @staticmethod
    def get_food():
        return "Disgusting food"


class SecondWife(GetFood):
    @staticmethod
    def get_food():
        return "Tasty food"


class BurgerKing(GetFood):
    @staticmethod
    def get_food():
        return "Fast food"


class Mother(GetFood):
    @staticmethod
    def get_food():
        return "Mother's food"


class HappyMan:
    def __init__(self, food_provider):
        self.food_provider = food_provider

    def food(self):
        return self.food_provider.get_food()


happy_man = HappyMan(BurgerKing)
print(happy_man.food())

# Що змінилося? Верхній клас не залежить від нижнього. Обидва типа клсів залежать від абстракцій.

# Ще окрім абстракцій використовують інтерфейси. В пайтоні для цього використовують модуль zope.interface.
# Інтерфейс шось типу договору по якому мають формуватися класи.

