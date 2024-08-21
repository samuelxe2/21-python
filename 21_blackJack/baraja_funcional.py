import random

def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(valor, palo) for valor in valores for palo in palos]


def baraja_singleton():
    baraja = crear_baraja()
    random.shuffle(baraja)
    return baraja

def repartir_carta(baraja):
    return baraja[0], baraja[1:]