from typing import List, Optional

class Property:
    def __init__(self, name: str, cost: int, rent: int):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None

class Player:
    def __init__(self, name: str):
        self.name = name
        self.balance = 300
        self.properties = []
        self.is_active = True

    def buy_property(self, property: Property):
        if self.balance >= property.cost:
            self.balance -= property.cost
            self.properties.append(property)
            property.owner = self

    def pay_rent(self, property: Property):
        if property.owner != self:
            self.balance -= property.rent
            property.owner.balance += property.rent

    def complete_turn(self):
        if self.balance < 0:
            self.is_active = False
