USUARIOS_PERMITIDOS = {"admin", "Carlos"}

def verificar_permissao(usuario):
    return usuario in USUARIOS_PERMITIDOS

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"