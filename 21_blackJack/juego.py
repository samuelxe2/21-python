import random

# Clase para representar una carta
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

    def obtener_valor(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11
        else:
            return int(self.valor)

# Clase para representar una baraja de cartas
class Baraja:
    def __init__(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        self.cartas = [Carta(valor, palo) for valor in valores for palo in palos]
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()

# Clase para representar una mano de Blackjack
class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def obtener_valor(self):
        valor = sum(carta.obtener_valor() for carta in self.cartas)
        numero_ases = sum(1 for carta in self.cartas if carta.valor == 'A')

        # Ajustar valor del As si el total es mayor que 21
        while valor > 21 and numero_ases:
            valor -= 10
            numero_ases -= 1

        return valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)

# Clase Dealer
class Dealer:
    def __init__(self):
        self.mano = Mano()

    def jugar(self, baraja):
        # El dealer sigue jugando hasta que tenga al menos 17 puntos
        while self.mano.obtener_valor() < 17:
            self.mano.agregar_carta(baraja.repartir_carta())

        print("Cartas del dealer: ", self.mano)
        return self.mano.obtener_valor()

# Función principal para jugar Blackjack
def jugar_blackjack():
    baraja = Baraja()

    mano_jugador = Mano()
    dealer = Dealer()

    # Repartir dos cartas iniciales al jugador y al dealer
    mano_jugador.agregar_carta(baraja.repartir_carta())
    mano_jugador.agregar_carta(baraja.repartir_carta())
    dealer.mano.agregar_carta(baraja.repartir_carta())
    dealer.mano.agregar_carta(baraja.repartir_carta())

    print("Tus cartas: ", mano_jugador)
    print("Carta visible del dealer: ", dealer.mano.cartas[0])

    # Turno del jugador
    while True:
        accion = input("¿Deseas pedir otra carta? (s/n): ").lower()
        if accion == 's':
            mano_jugador.agregar_carta(baraja.repartir_carta())
            print("Tus cartas: ", mano_jugador)

            if mano_jugador.obtener_valor() > 21:
                print("¡Te pasaste de 21! Has perdido.")
                return
        else:
            break

    # Turno del dealer
    valor_dealer = dealer.jugar(baraja)

    valor_jugador = mano_jugador.obtener_valor()

    # Determinar el resultado del juego usando puertas lógicas
    gana_jugador = (valor_jugador <= 21) and ((valor_dealer > 21) or (valor_jugador > valor_dealer))
    empate = (valor_jugador == valor_dealer) and (valor_jugador <= 21)

    if gana_jugador:
        print("¡Has ganado!")
    elif empate:
        print("Es un empate.")
    else:
        print("El dealer gana.")

# Llamada a la función para jugar
jugar_blackjack()
