from src.market_maker import MarketMaker
from src.market_manager import MarketDataManager
from src.market_simulator import MarketSimulation
from typing import Dict
import time

# Definir contratos futuros con días hasta vencimiento (se pueden agregar más contratos)
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
    # Inicializar componentes
    simulador_mercado = MarketSimulation(n_books=5)
    gestor_datos_mercado = MarketDataManager(simulador=simulador_mercado)
    
    # Inicializar MarketMaker con una TNA del 5%
    market_maker = MarketMaker(tna=0.05, contratos=contratos)
    
    # Suscribir el MarketMaker al gestor de datos de mercado
    gestor_datos_mercado.suscribir(market_maker)
    
    # Simular la distribución de datos de mercado
    while True:
        gestor_datos_mercado.distribuir_datos_mercado()
        time.sleep(2)  # Esperar 2 segundos antes de la siguiente simulación
