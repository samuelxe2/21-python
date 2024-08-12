import random

def baraja_singleton():
    if not hasattr(baraja_singleton, "_instance"):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        cartas = [(valor, palo) for valor in valores for palo in palos]
        random.shuffle(cartas)
        baraja_singleton._instance = cartas
    return baraja_singleton._instance[:]

def repartir_carta(baraja):
    return baraja.pop(), baraja