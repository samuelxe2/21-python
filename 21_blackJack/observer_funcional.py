
def notificar_observadores(evento, observadores):
    for observador in observadores:
        observador(evento)

def imprimir_evento(evento):
    print(f"Evento recibido: {evento}")
