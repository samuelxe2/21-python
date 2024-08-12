from mano import Mano
from baraja import Baraja

class Dealer:
    def __init__(self):
        self.mano = Mano()

    def jugar(self, baraja):
        while self.mano.obtener_valor() < 17:
            self.mano.agregar_carta(baraja.repartir_carta())

        print("Cartas del dealer: ", self.mano)
        return self.mano.obtener_valor()
