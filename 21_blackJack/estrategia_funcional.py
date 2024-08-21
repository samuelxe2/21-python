def obtener_valor_carta(carta):
    valor, _ = carta
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

def ajustar_por_ases(mano, valor_total):
    ases = len([carta for carta in mano if carta[0] == 'A'])
    while valor_total > 21 and ases > 0:
        valor_total -= 10
        ases -= 1
    return valor_total

def obtener_valor_mano(mano):
    valor_inicial = sum(map(obtener_valor_carta, mano))
    return ajustar_por_ases(mano, valor_inicial)

def carta_valor(carta):
    valor, _ = carta
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)