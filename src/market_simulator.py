import random
from typing import List, Dict, Any

class MarketSimulation:
    def __init__(self, n_books: int = 5):
        self.n_books = n_books

    def generar_books(self) -> List[Dict[str, Any]]:
        books = []
        
        for _ in range(self.n_books):
            precio = round(random.uniform(100, 200), 2)  # Precio aleatorio entre 100 y 200
            cantidad = random.randint(1, 100)  # Cantidad aleatoria entre 1 y 100
            books.append({"precio": precio, "cantidad": cantidad})
        
        return books