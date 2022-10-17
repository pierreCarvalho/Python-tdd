from bytebank import Funcionario


#lucas =  Funcionario("Lucas Carvalho", "13/03/2000", 1000)
#print(lucas.idade())

def test_idade():
    funcionario_teste = Funcionario('Teste', "13/03/2000", 1111)
    print(f'Teste = {funcionario_teste.idade()}')



test_idade()