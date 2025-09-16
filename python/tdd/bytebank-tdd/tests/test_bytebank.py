from codigo.bytebank import Funcionario 
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_25(self):
        entrada = '13/03/2000'  # Given - Contexto 
        esperado = 25
        
        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade() # When - Ação

        assert resultado == esperado  # Then - Desfecho / Resultado esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'  # Given - Contexto 
        esperado = 'Carvalho'
        
        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)

        resultado = funcionario_teste.sobrenome() # When - Ação

        assert resultado == esperado  # Then - Desfecho / Resultado esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given - Contexto
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)

        resultado = funcionario_teste.decrescimo_salario() # When - Ação

        assert resultado == esperado  # Then - Desfecho / Resultado esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # Given - Contexto 
        esperado = 100
        
        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada)

        resultado = funcionario_teste.calcular_bonus() # When - Ação

        assert resultado == esperado  # Then - Desfecho / Resultado esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10001_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10001  # Given - Contexto 
            
            funcionario_teste = Funcionario('Teste', '13/03/2000', entrada)
            resultado = funcionario_teste.calcular_bonus() # When - Ação

            assert resultado  # Then - Desfecho / Resultado esperado