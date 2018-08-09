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

    # @property
    # def owner_data(self):
    #     return [self.owner_name, 'random_id']


class OwnerCollection(object):

    def __init__(self, items):
        self.items = items

    @property
    def get_list_of_owners(self):
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

result = OwnerCollection((a, b, c))
print(result.get_list_of_owners)