from abc import ABCMeta, abstractproperty


class Item(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def owner(self):
        pass


class Axe(Item):

    def __init__(self, owner_name):
        self.owner_name = owner_name

    @property
    def owner(self):
        return self.owner_name

# when we need to chagne behavior of our methods we just extends from this class and override that method
    # @property
    # def owner(self):
    #     return [self.owner_name, 'random_id']

# instead of changing this method we create new class, which extends from this class
class SomeOtherAxe(Axe):

    @property
    def owner(self):
        return self.owner_name + 'X'

class OwnerCollection(object):

    def __init__(self, items):
        self.items = items

    @property
    def count_items_by_owner(self):
        owners_list = {}
        for item in self.items:
            if item.owner in owners_list:
                owners_list[item.owner] += 1
            else:
                owners_list[item.owner] = 1
        return owners_list



a = Axe('Serhyi')
b = Axe('Kamar')
c = Axe('Kamar')
x = SomeOtherAxe('OtherOwner')

result = OwnerCollection((a, b, c, x))
print(result.count_items_by_owner)
