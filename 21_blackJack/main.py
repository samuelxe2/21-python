from baraja_funcional import baraja_singleton, repartir_carta
from estrategia_funcional import estrategia_agresiva, estrategia_conservadora, obtener_valor_mano
from observer_funcional import notificar_observadores, imprimir_evento

def jugar_blackjack():
    baraja = baraja_singleton()

    mano_jugador = []
    mano_dealer = []

    # Repartir dos cartas iniciales al jugador y al dealer
    carta, baraja = repartir_carta(baraja)
    mano_jugador.append(carta)
    carta, baraja = repartir_carta(baraja)
    mano_jugador.append(carta)
    
    carta, baraja = repartir_carta(baraja)
    mano_dealer.append(carta)
    carta, baraja = repartir_carta(baraja)
    mano_dealer.append(carta)

    print("Tus cartas: ", mano_jugador)
    print("Carta visible del dealer: ", mano_dealer[0])

    # Estrategia del jugador (puede cambiar dinámicamente)
    estrategia = estrategia_agresiva

    # Turno del jugador
    while estrategia(mano_jugador):
        carta, baraja = repartir_carta(baraja)
        mano_jugador.append(carta)
        print("Tus cartas: ", mano_jugador)

        if obtener_valor_mano(mano_jugador) > 21:
            print("¡Te pasaste de 21! Has perdido.")
            notificar_observadores("Jugador perdió", [imprimir_evento])
            return

    # Turno del dealer
    while obtener_valor_mano(mano_dealer) < 17:
        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)

    print("Cartas del dealer: ", mano_dealer)

    valor_jugador = obtener_valor_mano(mano_jugador)
    valor_dealer = obtener_valor_mano(mano_dealer)

    # Determinar el resultado del juego
    if (valor_jugador <= 21) and ((valor_dealer > 21) or (valor_jugador > valor_dealer)):
        print("¡Has ganado!")
        notificar_observadores("Jugador ganó", [imprimir_evento])
    elif valor_jugador == valor_dealer:
        print("Es un empate.")
        notificar_observadores("Empate", [imprimir_evento])
    else:
        print("El dealer gana.")
        notificar_observadores("Dealer ganó", [imprimir_evento])

if __name__ == "__main__":
    jugar_blackjack()