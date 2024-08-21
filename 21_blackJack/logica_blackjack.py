from estrategia_funcional import obtener_valor_mano

def es_blackjack(mano):
    return len(mano) == 2 and obtener_valor_mano(mano) == 21

def calcular_resultado(valor_jugador, valor_dealer):
    if valor_jugador > 21:
        return "Dealer ganó"
    elif valor_dealer > 21 or valor_jugador > valor_dealer:
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
