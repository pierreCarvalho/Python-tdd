# Given-When-Then metodologia
# Dado(Contexto)
# Quando(Ação)
# Então(Desfecho)
import pytest
from codigo.bytebank import Funcionario
from pytest import mark
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000" # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade() # When - Ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"

        funcionario_teste = Funcionario(entrada, 2000, 1111)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado
    
    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado= funcionario_teste.salario

        assert resultado == esperado
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario("Ana", "11/11/2000", entrada)
        
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000 #given

            funcionario_teste = Funcionario("Ana", "11/11/2000", entrada)
            
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

