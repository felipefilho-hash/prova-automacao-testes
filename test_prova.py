import pytest
from unittest.mock import patch

from Ex1 import classificar_produto
from Ex2 import inverter_palavras
from Ex3 import validar_documento
from Ex4 import gerar_codigo, criar_identificacao
from Ex5 import verificar_permissao, acessar_sistema
from Ex6 import atender_proximo_cliente


# EXERCÍCIO 1
@pytest.mark.parametrize("quantidade, esperado", [
    (0, "Sem estoque"),
    (3, "Estoque baixo"),
    (10, "Estoque normal"),
    (30, "Estoque alto"),
    (-1, "Quantidade inválida"),
])
def test_classificar_produto(quantidade, esperado):
    assert classificar_produto(quantidade) == esperado


# EXERCÍCIO 2
@pytest.mark.parametrize("texto, esperado", [
    ("Python é muito interessante", "interessante muito é Python"),
    ("Python", "Python"),
    ("", ""),
    ("  Python   é legal  ", "legal é Python"),
    ("Python 3 versão 12", "12 versão 3 Python"),
])
def test_inverter_palavras(texto, esperado):
    assert inverter_palavras(texto) == esperado


# EXERCÍCIO 3
@pytest.mark.parametrize("documento, esperado", [
    ("12345678900", True),
    ("123.456.789-00", True),
    ("1234567890", False),
    ("123456789000", False),
    ("1234567890A", False),
    ("", False),
])
def test_validar_documento(documento, esperado):
    assert validar_documento(documento) is esperado


# EXERCÍCIO 4
def test_codigo_gerado():
    codigo = gerar_codigo()
    assert codigo.startswith("USR-")
    assert len(codigo) == 8
    assert codigo[4:].isdigit()


def test_identificacao():
    with patch("Ex4.gerar_codigo", return_value="USR-1234") as mock:
        resultado = criar_identificacao("Carlos")
        assert resultado == "Usuário Carlos cadastrado com código USR-1234."
        mock.assert_called_once_with()


def test_codigos_diferentes():
    with patch("Ex4.gerar_codigo", side_effect=["USR-1111", "USR-2222"]) as mock:
        assert criar_identificacao("Ana") == "Usuário Ana cadastrado com código USR-1111."
        assert criar_identificacao("João") == "Usuário João cadastrado com código USR-2222."
        assert mock.call_count == 2


def test_nomes_diferentes():
    with patch("Ex4.gerar_codigo", return_value="USR-9999"):
        assert criar_identificacao("Maria") == "Usuário Maria cadastrado com código USR-9999."
        assert criar_identificacao("Pedro") == "Usuário Pedro cadastrado com código USR-9999."


# EXERCÍCIO 5
def test_permissao_real():
    assert verificar_permissao("admin") is True
    assert verificar_permissao("visitante") is False


def test_acesso_autorizado():
    with patch("Ex5.verificar_permissao", return_value=True) as mock:
        assert acessar_sistema("Carlos") == "Acesso autorizado"
        mock.assert_called_once_with("Carlos")


def test_acesso_negado():
    with patch("Ex5.verificar_permissao", return_value=False) as mock:
        assert acessar_sistema("Maria") == "Acesso negado"
        mock.assert_called_once_with("Maria")


def test_dois_cenarios_acesso():
    with patch("Ex5.verificar_permissao", side_effect=[True, False]) as mock:
        assert acessar_sistema("Ana") == "Acesso autorizado"
        assert acessar_sistema("João") == "Acesso negado"
        assert mock.call_count == 2


# EXERCÍCIO 6
def test_atendimento_sucesso():
    with patch("Ex6.obter_proximo_cliente", return_value="Carlos") as proximo, \
         patch("Ex6.registrar_atendimento", return_value=True) as registro:
        assert atender_proximo_cliente() == "Atendimento realizado"
        proximo.assert_called_once_with()
        registro.assert_called_once_with("Carlos")


def test_fila_vazia():
    with patch("Ex6.obter_proximo_cliente", return_value=None) as proximo, \
         patch("Ex6.registrar_atendimento") as registro:
        assert atender_proximo_cliente() == "Fila vazia"
        proximo.assert_called_once_with()
        registro.assert_not_called()


def test_falha_atendimento():
    with patch("Ex6.obter_proximo_cliente", return_value="Ana") as proximo, \
         patch("Ex6.registrar_atendimento", return_value=False) as registro:
        assert atender_proximo_cliente() == "Falha no atendimento"
        proximo.assert_called_once_with()
        registro.assert_called_once_with("Ana")