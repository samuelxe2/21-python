from baraja_funcional import baraja_singleton, repartir_carta
from estrategia_funcional import obtener_valor_mano
from observer_funcional import notificar_observadores, imprimir_evento
from logica_blackjack import calcular_resultado, ajustar_apuesta, es_blackjack

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

def mostrar_mano(jugador, mano, mostrar_todas=False):
    if mostrar_todas:
        print(f"Jugador {jugador}, tus cartas: {mano}, Valor: {obtener_valor_mano(mano)}")
    else:
        print(f"Jugador {jugador}, tu carta visible: {mano[0]}")

def decision_manual(jugador, mano_jugador):
    mostrar_mano(jugador, mano_jugador, mostrar_todas=False)
    return input("¿Deseas pedir otra carta (P) o plantarte (S)? ").strip().upper()

def jugar_turno(jugador, mano_jugador, baraja, decision_fn):
    while True:
        decision = decision_fn(jugador, mano_jugador)
        if decision == 'P':
            carta, baraja = repartir_carta(baraja)
            mano_jugador.append(carta)
            if obtener_valor_mano(mano_jugador) > 21:
                break
        elif decision == 'S':
            break
    return mano_jugador, baraja

def jugar_blackjack(max_jugadores, baraja, decision_fn):
    manos_jugadores = []
    apuestas_jugadores = [solicitar_apuesta(i + 1) for i in range(max_jugadores)]
    mano_dealer = [repartir_carta(baraja)[0] for _ in range(2)]

    # Repartir cartas iniciales
    for i in range(1, max_jugadores + 1):
        mano_jugador = [repartir_carta(baraja)[0], repartir_carta(baraja)[0]]
        manos_jugadores.append(mano_jugador)
        mostrar_mano(i, mano_jugador, mostrar_todas=True)
        if es_blackjack(mano_jugador):
            print(f"¡Jugador {i} tiene Blackjack!")
            continue

        # Jugar turno para cada jugador
        mano_jugador, baraja = jugar_turno(i, mano_jugador, baraja, decision_fn)
        manos_jugadores[i - 1] = mano_jugador

    # Turno del dealer
    while obtener_valor_mano(mano_dealer) < 17:
        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)

    resultados = []
    for i in range(max_jugadores):
        valor_jugador = obtener_valor_mano(manos_jugadores[i])
        valor_dealer = obtener_valor_mano(mano_dealer)
        resultado = calcular_resultado(valor_jugador, valor_dealer)
        apuesta_final = ajustar_apuesta(resultado, apuestas_jugadores[i])
        resultados.append(apuesta_final)
        notificar_observadores(f"Jugador {i+1} {resultado.lower()}", [imprimir_evento])

    return resultados

if __name__ == "__main__":
    baraja = baraja_singleton()
    max_jugadores = 2  # Cambia este valor para ajustar el número de jugadores

    resultados = jugar_blackjack(max_jugadores, baraja, decision_manual)
    print("Resultados finales:", resultados)
