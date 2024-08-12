def estrategia_agresiva(mano):
    return obtener_valor_mano(mano) < 18

def estrategia_conservadora(mano):
    return obtener_valor_mano(mano) < 15

def obtener_valor_mano(mano):
    valor = sum(carta_valor(carta) for carta in mano)
    numero_ases = sum(1 for carta in mano if carta[0] == 'A')

    while valor > 21 and numero_ases:
        valor -= 10
        numero_ases -= 1

    return valor

def carta_valor(carta):
    valor, _ = carta
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)