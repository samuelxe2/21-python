from baraja_funcional import baraja_singleton, repartir_carta
from estrategia_funcional import estrategia_agresiva, obtener_valor_mano
from observer_funcional import notificar_observadores, imprimir_evento

def calcular_resultado(valor_jugador, valor_dealer):
    if (valor_jugador <= 21) and ((valor_dealer > 21) or (valor_jugador > valor_dealer)):
        return "Jugador ganó"
    elif valor_jugador == valor_dealer:
        return "Empate"
    else:
        return "Dealer ganó"

def ajustar_apuesta(resultado, apuesta, blackjack=False):
    if resultado == "Jugador ganó":
        return apuesta * 2.5 if blackjack else apuesta * 2
    elif resultado == "Empate":
        return apuesta  # Recupera la apuesta
    else:
        return 0  # Pierde la apuesta

def es_blackjack(mano):
    return len(mano) == 2 and obtener_valor_mano(mano) == 21

def solicitar_apuesta():
    while True:
        try:
            apuesta = int(input("¿Cuánto deseas apostar? (Debe ser un número entero): "))
            if apuesta > 0:
                return apuesta
            else:
                print("La apuesta debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

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

    # Se solicita una apuesta inicial
    apuesta_inicial = solicitar_apuesta()
    apuesta = apuesta_inicial

    # Verificar si el jugador tiene un Blackjack
    if es_blackjack(mano_jugador):
        print("¡Blackjack! Tienes 21 con tus dos primeras cartas.")
        resultado = calcular_resultado(obtener_valor_mano(mano_jugador), obtener_valor_mano(mano_dealer))
        apuesta_final = ajustar_apuesta(resultado, apuesta_inicial, blackjack=True)
        print(f"¡Has ganado {apuesta_final} con un Blackjack!")
        notificar_observadores("Jugador ganó con Blackjack", [imprimir_evento])
        return

    # Turno del jugador
    while estrategia(mano_jugador):
        carta, baraja = repartir_carta(baraja)
        mano_jugador.append(carta)
        print("Tus cartas: ", mano_jugador)

        if obtener_valor_mano(mano_jugador) > 21:
            print("¡Te pasaste de 21! Has perdido.")
            notificar_observadores("Jugador perdió", [imprimir_evento])
            apuesta = 0  # Pierde la apuesta
            print(f"Has perdido tu apuesta de {apuesta_inicial}.")
            return

    # Turno del dealer
    while obtener_valor_mano(mano_dealer) < 17:
        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)

    print("Cartas del dealer: ", mano_dealer)

    valor_jugador = obtener_valor_mano(mano_jugador)
    valor_dealer = obtener_valor_mano(mano_dealer)

    # Determinar el resultado del juego
    resultado = calcular_resultado(valor_jugador, valor_dealer)
    apuesta_final = ajustar_apuesta(resultado, apuesta_inicial)

    print(f"Resultado: {resultado}")
    if resultado == "Jugador ganó":
        print(f"¡Has ganado {apuesta_final}!")
    elif resultado == "Empate":
        print(f"Es un empate. Recuperas tu apuesta de {apuesta_final}.")
    else:
        print(f"El dealer gana. Has perdido tu apuesta de {apuesta_inicial}.")

    notificar_observadores(resultado, [imprimir_evento])

if __name__ == "__main__":
    jugar_blackjack()
