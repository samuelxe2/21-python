from baraja import Baraja
from mano import Mano
from dealer import Dealer

def jugar_blackjack():
    baraja = Baraja()

    mano_jugador = Mano()
    dealer = Dealer()

    #Repartir  al jugador y al dealer
    mano_jugador.agregar_carta(baraja.repartir_carta())
    mano_jugador.agregar_carta(baraja.repartir_carta())
    dealer.mano.agregar_carta(baraja.repartir_carta())
    dealer.mano.agregar_carta(baraja.repartir_carta())

    print("Tus cartas: ", mano_jugador)
    print("Carta visible del dealer: ", dealer.mano.cartas[0])

    #Turno del jugador
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

    #Turno del dealer
    valor_dealer = dealer.jugar(baraja)
    valor_jugador = mano_jugador.obtener_valor()

    #Determinar el resultado del juego
    gana_jugador = (valor_jugador <= 21) and ((valor_dealer > 21) or (valor_jugador > valor_dealer))
    empate = (valor_jugador == valor_dealer) and (valor_jugador <= 21)

    if gana_jugador:
        print("¡Has ganado!")
    elif empate:
        print("Es un empate.")
    else:
        print("El dealer gana.")

if __name__ == "__main__":
    jugar_blackjack()
