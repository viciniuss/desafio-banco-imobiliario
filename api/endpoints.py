from fastapi import APIRouter
from game.models import Player
from game.logic import Game
from game.strategies import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer

router = APIRouter()

@router.get("/jogo/simular")
async def simular_jogo():
    game = Game()
    
    game.add_player(Player("impulsivo"), ImpulsivePlayer())
    game.add_player(Player("exigente"), DemandingPlayer())
    game.add_player(Player("cauteloso"), CautiousPlayer())
    game.add_player(Player("aleatorio"), RandomPlayer())

    vencedor, jogadores = game.simulate_game()

    return {
        "vencedor": vencedor,
        "jogadores": jogadores
    }
