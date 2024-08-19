from src.market_simulator import MarketSimulation
from src.market_maker import MarketMaker
from typing import List

class MarketDataManager:
    """
    Clase que gestiona la distribución de datos de mercado a múltiples suscriptores, 
    como los market makers, utilizando un simulador de mercado.
    """
    
    def __init__(self, simulador: MarketSimulation):
        """
        Inicializa un nuevo objeto MarketDataManager con un simulador de mercado.
        """
        self.simulador = simulador
        self.subscritos: List[MarketMaker] = []

    def suscribir(self, subscrito: MarketMaker):
        """
        Suscribe un nuevo market maker a la distribución de datos de mercado.
        """
        self.subscritos.append(subscrito)

    def distribuir_datos_mercado(self):
        """
        Genera datos de mercado utilizando el simulador y los distribuye a todos los market makers suscritos.
        """
        books = self.simulador.generar_books()
        
        for subscrito in self.subscritos:
            subscrito.recibir_datos_mercado(books)