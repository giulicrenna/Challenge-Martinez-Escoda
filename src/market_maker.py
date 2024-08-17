from typing import List, Dict, Any
from colorama import Fore, Style, init
import os
import random
import math

init()

class MarketMaker:
    def __init__(self, tna: float, contratos: Dict[str, int]):
        self.tna = tna  # Tasa Nominal Anual (TNA)
        self.contratos = contratos  # Diccionario con nombre del contrato y días hasta vencimiento
        self.datos_contratos = {}
        self.color_id: int = 0
        
    def recibir_datos_mercado(self, books: List[Dict[str, Any]]):
        self.limpiar_pantalla()  # Limpiar pantalla antes de imprimir
        self.actualizar_datos_contratos(books)
        self.imprimir_encabezado()
        self.imprimir_datos_contratos()

    def calcular_precio_futuro(self, *, precio_spot: float, dias_hasta_vencimiento: int) -> float:
        volatilidad_anual = 0.2  # Volatilidad anual estimada (20%)
        drift = self.tna / 365  # Ajuste por la tasa nominal anual basado en 365 días
        factor_volatilidad = volatilidad_anual * math.sqrt(dias_hasta_vencimiento / 365)
        shock_estocastico = random.gauss(0, 1)  # Genera un número aleatorio de distribución normal estándar
        precio_futuro = precio_spot * math.exp((drift - 0.5 * factor_volatilidad ** 2) * dias_hasta_vencimiento + factor_volatilidad * shock_estocastico)
        return round(precio_futuro, 2)

    def actualizar_datos_contratos(self, books: List[Dict[str, Any]]):
        for contrato, dias in self.contratos.items():
            # Seleccionar una cantidad aleatoria para cada contrato en función de los libros
            book = random.choice(books)
            precio_spot = book['precio']
            cantidad = random.randint(1, 100)  # Generar una cantidad aleatoria para cada contrato
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
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para otros sistemas operativos (Linux/Mac)
            os.system('clear')

    def get_color_for_contrato(self, contrato: str) -> str:
        colors = [
            Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE
        ]
        
        return colors[hash(contrato) % len(colors)]  # Colorea con un hash distribuido
