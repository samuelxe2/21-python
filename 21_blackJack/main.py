from baraja_funcional import baraja_singleton, repartir_carta
from estrategia_funcional import obtener_valor_mano
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
        return apuesta
    else:
        return 0

def es_blackjack(mano):
    return len(mano) == 2 and obtener_valor_mano(mano) == 21

def solicitar_apuesta(jugador):
    while True:
        try:
            apuesta = int(input(f"Jugador {jugador}, ¿cuánto deseas apostar? (Debe ser un número entero): "))
            if apuesta > 0:
                return apuesta
            else:
                print("La apuesta debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

def mostrar_mano(jugador, mano):
    print(f"Jugador {jugador}, tus cartas: {mano}, Valor: {obtener_valor_mano(mano)}")

def jugar_turno_jugador(jugador, mano_jugador, baraja):
    while True:
        mostrar_mano(jugador, mano_jugador)
        decision = input("¿Deseas pedir otra carta (P) o plantarte (S)? ").strip().upper()
        if decision == 'P':
            carta, baraja = repartir_carta(baraja)
            mano_jugador.append(carta)
            if obtener_valor_mano(mano_jugador) > 21:
                mostrar_mano(jugador, mano_jugador)
                print(f"Jugador {jugador}, ¡te pasaste de 21! Has perdido.")
                notificar_observadores(f"Jugador {jugador} perdió", [imprimir_evento])
                return mano_jugador, baraja, False
        elif decision == 'S':
            return mano_jugador, baraja, True
        else:
            print("Decisión no válida. Introduce 'P' para pedir o 'S' para plantarte.")

def jugar_blackjack():
    baraja = baraja_singleton()

    num_jugadores = int(input("¿Cuántos jugadores van a jugar? "))
    manos_jugadores = [[] for _ in range(num_jugadores)]
    apuestas_jugadores = []
    resultados_jugadores = []

    mano_dealer = []

    # Repartir dos cartas iniciales a cada jugador y al dealer
    for i in range(num_jugadores):
        carta, baraja = repartir_carta(baraja)
        manos_jugadores[i].append(carta)
        carta, baraja = repartir_carta(baraja)
        manos_jugadores[i].append(carta)
        apuestas_jugadores.append(solicitar_apuesta(i + 1))

    carta, baraja = repartir_carta(baraja)
    mano_dealer.append(carta)
    carta, baraja = repartir_carta(baraja)
    mano_dealer.append(carta)

    print("Carta visible del dealer: ", mano_dealer[0])

    for i in range(num_jugadores):
        if es_blackjack(manos_jugadores[i]):
            print(f"¡Jugador {i + 1} tiene Blackjack!")
            apuesta_final = ajustar_apuesta("Jugador ganó", apuestas_jugadores[i], blackjack=True)
            print(f"¡Jugador {i + 1} ha ganado {apuesta_final} con un Blackjack!")
            notificar_observadores(f"Jugador {i + 1} ganó con Blackjack", [imprimir_evento])
            resultados_jugadores.append(apuesta_final)
        else:
            mano_jugador, baraja, sigue_en_juego = jugar_turno_jugador(i + 1, manos_jugadores[i], baraja)
            if sigue_en_juego:
                resultados_jugadores.append(apuestas_jugadores[i])
            else:
                resultados_jugadores.append(0)

    while obtener_valor_mano(mano_dealer) < 17:
        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)

    print("Cartas del dealer: ", mano_dealer)

    valor_dealer = obtener_valor_mano(mano_dealer)

    for i in range(num_jugadores):
        if resultados_jugadores[i] != 0:
            valor_jugador = obtener_valor_mano(manos_jugadores[i])
            resultado = calcular_resultado(valor_jugador, valor_dealer)
            apuesta_final = ajustar_apuesta(resultado, apuestas_jugadores[i])
            print(f"Jugador {i + 1}: Resultado: {resultado}. Ganancias: {apuesta_final}")
            notificar_observadores(f"Jugador {i + 1} {resultado.lower()}", [imprimir_evento])
            resultados_jugadores[i] = apuesta_final

if __name__ == "__main__":
    jugar_blackjack()


