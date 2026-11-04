FILA = ["Carlos", "Ana"]

def obter_proximo_cliente():
    return FILA.pop(0) if FILA else None

def registrar_atendimento(cliente):
    return True

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()

    if cliente is None:
        return "Fila vazia"

    if registrar_atendimento(cliente):
        return "Atendimento realizado"

    return "Falha no atendimento"
    