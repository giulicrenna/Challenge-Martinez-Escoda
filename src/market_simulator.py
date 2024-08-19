import random
from typing import List, Dict, Any

class MarketSimulation:
    """
    Clase que simula la generación de datos de mercado, produciendo una lista de 'books' 
    que contienen precios y cantidades de activos.
    """
    
    def __init__(self, n_books: int = 5):
        """
        Inicializa un nuevo objeto MarketSimulation con un número predeterminado de 'books'.
        """
        self.n_books = n_books

    def generar_books(self) -> List[Dict[str, Any]]:
        """
        Genera una lista de 'books', donde cada 'book' es un diccionario que contiene 
        un precio aleatorio y una cantidad aleatoria.
        """
        books = []
        
        for _ in range(self.n_books):
            precio = round(random.uniform(100, 200), 2)  # Precio aleatorio entre 100 y 200
            cantidad = random.randint(1, 100)  # Cantidad aleatoria entre 1 y 100
            books.append({"precio": precio, "cantidad": cantidad})
        
        return books