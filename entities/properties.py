class Monopoly:
    def __init__(self, name, properties=[]):
        self.name = name
        self.owner = None
        self.properties = properties

    def set_owner(self, player):
        self.owner = player

    def add_property(self, property_):
        self.properties.append(property_)


class Property:
    def __init__(self, price, rent, name, monopoly):
        self.owner = None
        self.price = price
        self.rent = rent
        self.name = name
        self.monopoly = monopoly

    def set_owner(self, player):
        self.owner = player
