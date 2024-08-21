def imprimir_evento(evento):
    print(evento)

def notificar_observadores(evento, observadores):
    for observador in observadores:
        observador(evento)
