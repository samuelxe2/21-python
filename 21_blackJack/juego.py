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

        # Usar puertas lógicas para ajustar el valor del As si el total es mayor que 21
        while (valor > 21) and (numero_ases > 0):
            valor -= 10
            numero_ases -= 1

        return valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)

# Función principal para jugar Blackjack
def jugar_blackjack():
    baraja = Baraja()

    mano_jugador = Mano()
    mano_croupier = Mano()

    # Repartir dos cartas iniciales al jugador y al croupier
    mano_jugador.agregar_carta(baraja.repartir_carta())
    mano_jugador.agregar_carta(baraja.repartir_carta())
    mano_croupier.agregar_carta(baraja.repartir_carta())
    mano_croupier.agregar_carta(baraja.repartir_carta())

    print("Tus cartas: ", mano_jugador)
    print("Cartas del croupier: ", mano_croupier.cartas[0])

    # Turno del jugador
    while True:
        accion = input("¿Deseas pedir otra carta? (s/n): ").lower()
        if accion == 's':
            mano_jugador.agregar_carta(baraja.repartir_carta())
            print("Tus cartas: ", mano_jugador)

            # Verificación con puertas lógicas
            if mano_jugador.obtener_valor() > 21:
                print("¡Te pasaste de 21! Has perdido.")
                return
        else:
            break

    # Turno del croupier
    while mano_croupier.obtener_valor() < 17:
        mano_croupier.agregar_carta(baraja.repartir_carta())

    print("Cartas del croupier: ", mano_croupier)

    valor_jugador = mano_jugador.obtener_valor()
    valor_croupier = mano_croupier.obtener_valor()

    # Determinar el resultado del juego usando puertas lógicas
    gana_jugador = (valor_jugador <= 21) and ((valor_croupier > 21) or (valor_jugador > valor_croupier))
    empate = (valor_jugador == valor_croupier) and (valor_jugador <= 21)

    if gana_jugador:
        print("¡Has ganado!")
    elif empate:
        print("Es un empate.")
    else:
        print("El croupier gana.")

# Llamada a la función para jugar
jugar_blackjack()
