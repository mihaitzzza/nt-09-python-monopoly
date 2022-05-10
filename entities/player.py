import uuid


class Player:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.position = 0
        self.budget = 1500
        self.doubles = 0
        self.is_bankrupt = False

    def receive(self, amount):
        self.budget += amount

    def check_bankruptcy(self):
        self.is_bankrupt = self.budget < 0
        return self.is_bankrupt

    def pay(self, amount, player=None):
        self.budget -= amount
        if player is not None:
            player.receive(amount)
        self.check_bankruptcy()

    def get_paycheck(self):
        self.budget += 200

    def buy(self, property_):
        if self.budget >= property_.price:
            self.pay(property_.price)
            property_.set_owner(self)
            owner_ids = set([
                monopoly_property.owner.id if monopoly_property.owner is not None else None
                for monopoly_property in property_.monopoly.properties
            ])
            if len(owner_ids) == 1:
                property_.monopoly.set_owner(self)

    def go_to_jail(self):
        self.budget -= 50

    def __str__(self):
        return self.name
