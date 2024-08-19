from typing import List, Dict, Any
from colorama import Fore, Style, init
import os
import random
import math

init()

class MarketMaker:
    """
    Clase que simula un market maker, generando precios futuros de contratos
    basados en el precio spot y una Tasa Nominal Anual (TNA).
    
    Atributos:
        tna (float): Tasa Nominal Anual utilizada para calcular los precios futuros.
        contratos (Dict[str, int]): Diccionario con nombre del contrato y días hasta vencimiento.
        datos_contratos (dict): Almacena los datos actualizados de los contratos, incluyendo precio futuro y cantidad.
        color_id (int): Identificador utilizado para asignar colores a los contratos.
    """
    
    def __init__(self, tna: float, contratos: Dict[str, int]):
        """
        Inicializa un nuevo objeto MarketMaker con la TNA y los contratos especificados.

        Args:
            tna (float): Tasa Nominal Anual.
            contratos (Dict[str, int]): Diccionario que asocia nombres de contratos con días hasta su vencimiento.
        """
        self.tna = tna
        self.contratos = contratos
        self.datos_contratos = {}
        self.color_id: int = 0
        
    def recibir_datos_mercado(self, books: List[Dict[str, Any]]):
        """
        Recibe datos de mercado (books), actualiza la información de los contratos,
        y la imprime formateada en la pantalla.

        Args:
            books (List[Dict[str, Any]]): Lista de diccionarios que contienen datos de mercado, como precios spot.
        """
        self.limpiar_pantalla()
        self.actualizar_datos_contratos(books)
        self.imprimir_encabezado()
        self.imprimir_datos_contratos()

    def calcular_precio_futuro(self, *, precio_spot: float, dias_hasta_vencimiento: int) -> float:
        """
        Calcula el precio futuro de un contrato basado en el precio spot y los días hasta su vencimiento,
        aplicando un modelo estocástico (Gaussiano) simple que incluye volatilidad y drift.

        Args:
            precio_spot (float): El precio actual del activo subyacente.
            dias_hasta_vencimiento (int): Días restantes hasta el vencimiento del contrato.

        Returns:
            float: El precio futuro calculado, redondeado a dos decimales.
        """
        volatilidad_anual = 0.2
        drift = self.tna / 365
        factor_volatilidad = volatilidad_anual * math.sqrt(dias_hasta_vencimiento / 365)
        shock_estocastico = random.gauss(0, 1)
        precio_futuro = precio_spot * math.exp((drift - 0.5 * factor_volatilidad ** 2) * dias_hasta_vencimiento + factor_volatilidad * shock_estocastico)
        return round(precio_futuro, 2)

    def actualizar_datos_contratos(self, books: List[Dict[str, Any]]):
        """
        Actualiza la información de los contratos con nuevos datos de mercado.

        Args:
            books (List[Dict[str, Any]]): Lista de diccionarios que contienen datos de mercado, como precios spot.
        """
        for contrato, dias in self.contratos.items():
            book = random.choice(books)
            precio_spot = book['precio']
            cantidad = random.randint(1, 100)
            precio_futuro = self.calcular_precio_futuro(precio_spot=precio_spot, dias_hasta_vencimiento=dias)
            self.datos_contratos[contrato] = {
                'precio_futuro': precio_futuro,
                'cantidad': cantidad
            }

    def formatear_cotizacion(self, contrato: str, precio_futuro: float, cantidad: int) -> str:
        color = self.get_color_for_contrato(contrato)
        return f"{color}{contrato:<15}\t{precio_futuro:<12}\t{cantidad:<8}{Style.RESET_ALL}"

    def imprimir_encabezado(self):
        print(f"{Fore.YELLOW}{'Contrato':<15}\t{'Precio Futuro':<12}\t{'Cantidad':<8}{Style.RESET_ALL}")

    def imprimir_datos_contratos(self):
        for contrato, datos in self.datos_contratos.items():
            precio_futuro = datos['precio_futuro']
            cantidad = datos['cantidad']
            cotizacion = self.formatear_cotizacion(contrato, precio_futuro, cantidad)
            print(cotizacion)

    def limpiar_pantalla(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def get_color_for_contrato(self, contrato: str) -> str:
        colors = [
            Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE
        ]
        
        return colors[hash(contrato) % len(colors)]