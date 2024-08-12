
from carta import Carta

class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def obtener_valor(self):
        valor = sum(carta.obtener_valor() for carta in self.cartas)
        numero_ases = sum(1 for carta in self.cartas if carta.valor == 'A')

        while valor > 21 and numero_ases:
            valor -= 10
            numero_ases -= 1

        return valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)
