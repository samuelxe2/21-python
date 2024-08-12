
import random
from carta import Carta

class Baraja:
    def __init__(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        self.cartas = [Carta(valor, palo) for valor in valores for palo in palos]
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()
