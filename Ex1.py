def classificar_produto(quantidade):
    if quantidade < 0:
        return "Quantidade inválida"
    if quantidade == 0:
        return "Sem estoque"
    if quantidade <= 5:
        return "Estoque baixo"
    if quantidade <= 20:
        return "Estoque normal"
    return "Estoque alto"
