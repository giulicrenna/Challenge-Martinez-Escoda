from src.market_maker import MarketMaker
from src.market_manager import MarketDataManager
from src.market_simulator import MarketSimulation
from typing import Dict
import time

"""
El programa puede recibir cualquier cantidad de contratos.
"""
contratos: Dict[str, int] = {
        "Contrato_1": 30, 
        "Contrato_2": 60, 
        "Contrato_3": 90, 
        "Contrato_4": 120, 
        "Contrato_5": 150, 
        "Contrato_6": 180,
        "Contrato_7": 45,
        "Contrato_8": 67
}

if __name__ == "__main__":
    simulador_mercado = MarketSimulation(n_books=len(contratos.keys()))
    
    gestor_datos_mercado = MarketDataManager(simulador=simulador_mercado)
    
    market_maker = MarketMaker(tna=0.05, contratos=contratos)
    
    gestor_datos_mercado.suscribir(market_maker)

    while True:
        gestor_datos_mercado.distribuir_datos_mercado()
        time.sleep(2) 