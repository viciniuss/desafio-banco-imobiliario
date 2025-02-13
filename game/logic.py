import random
from game.models import Player, Property
from game.strategies import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer

class Game:
    def __init__(self):
        self.players = []
        self.properties = [Property(f"Property {i}", cost=100 + i * 50, rent=30 + i * 10) for i in range(20)]
        self.rounds = 0

    def add_player(self, player: Player, strategy):
        self.players.append((player, strategy))

    def play_turn(self, player: Player, strategy):
        if not player.is_active:
            return

        # Simula o lançamento do dado (1 a 6)
        dice_roll = random.randint(1, 6)
        position = (self.rounds + dice_roll) % 20
        current_property = self.properties[position]

        if current_property.owner is None:
            strategy.make_decision(player, current_property)
        else:
            player.pay_rent(current_property)

        player.complete_turn()

    def simulate_game(self):
        while self.rounds < 1000:
            for player, strategy in self.players:
                self.play_turn(player, strategy)
                if sum(1 for p, _ in self.players if p.is_active) == 1:
                    break

            self.rounds += 1
            if sum(1 for p, _ in self.players if p.is_active) == 1:
                break

        # Vencedor é o jogador com saldo maior
        winner = max(self.players, key=lambda x: x[0].balance)[0]
        sorted_players = sorted(self.players, key=lambda x: x[0].balance, reverse=True)
        
        return winner.name, [p[0].name for p in sorted_players]
