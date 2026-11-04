def validar_documento(documento):
    documento = str(documento).replace(".", "").replace("-", "")
    return len(documento) == 11 and documento.isascii() and documento.isdigit()
