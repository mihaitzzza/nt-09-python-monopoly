from abc import abstractmethod


class Space:

    @abstractmethod
    def action(self, player):
        pass


class TaxSpace(Space):
    def action(self, player):
        player.pay(50)


class CornerSpace(Space):
    def __init__(self, is_free_parking = True, is_start = False, is_go_to_jail = False, is_visit_jail = False):
        self.is_free_parking = is_free_parking
        self.is_start = is_start
        self.is_go_to_jail = is_go_to_jail
        self.is_visit_jail = is_visit_jail

    def action(self, player):
        if self.is_start:
            player.get_paycheck()
        elif self.is_go_to_jail:
            player.go_to_jail()


class PropertySpace(Space):
    def __init__(self, property_):
        self.property = property_

    def action(self, player):
        if self.property.owner is None:
            player.buy(self.property)
        elif self.property.owner is not player:
            if self.property.monopoly.owner:
                price_to_pay = self.property.rent * 2
            else:
                price_to_pay = self.property.rent
            player.pay(price_to_pay, self.property.owner)
