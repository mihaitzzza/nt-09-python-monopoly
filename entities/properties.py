class Monopoly:
    def __init__(self, name):
        self.name = name
        self.owner = None

    def set_owner(self, player):
        self.owner = player


class Property:
    def __init__(self, price, rent, name, monopoly):
        self.owner = None
        self.price = price
        self.rent = rent
        self.name = name
        self.monopoly = monopoly

    def set_owner(self, player):
        self.owner = player
