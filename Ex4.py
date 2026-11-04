import random

def gerar_codigo():
    return f"USR-{random.randint(1000, 9999)}"

def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."
