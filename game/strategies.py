import random
from game.models import Player, Property

class ImpulsivePlayer:
    def make_decision(self, player: Player, property: Property):
        if property.owner is None and player.balance >= property.cost:
            player.buy_property(property)

class DemandingPlayer:
    def make_decision(self, player: Player, property: Property):
        if property.owner is None and player.balance >= property.cost and property.rent > 50:
            player.buy_property(property)

class CautiousPlayer:
    def make_decision(self, player: Player, property: Property):
        if property.owner is None and player.balance - property.cost >= 80:
            player.buy_property(property)

class RandomPlayer:
    def make_decision(self, player: Player, property: Property):
        if property.owner is None and player.balance >= property.cost:
            if random.random() > 0.5:  # 50% chance to buy
                player.buy_property(property)
