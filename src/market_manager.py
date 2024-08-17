from src.market_simulator import MarketSimulation
from src.market_maker import MarketMaker
from typing import List

class MarketDataManager:
    def __init__(self, simulador: MarketSimulation):
        self.simulador = simulador
        self.subscritos: List[MarketMaker] = []

    def suscribir(self, subscrito):
        self.subscritos.append(subscrito)

    def distribuir_datos_mercado(self):
        books = self.simulador.generar_books()
        
        for subscrito in self.subscritos:
            subscrito.recibir_datos_mercado(books)