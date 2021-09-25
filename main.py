from ast import Num
from interfaces.executar import Executar
from interfaces.opQuatro import ListarFuncionario
from interfaces.opTres import AlteraFuncionario
from interfaces.opDois import RemoveFuncionario
from interfaces.interface import Interface
from interfaces.opUm import AddFuncionario
import pendulum
from modelo.funcionario_model import Funcionario
from tipo_funcionario.assalariado import Assalariado
from tipo_funcionario.comissario import Comissario
from tipo_funcionario.horista import Horista
from funcionalidades.crud import Crud
from funcionalidades.crud import listaFuncionario
 


crud = Crud()

def opcoesFuncionario():
    print("\nOpções de funcionário:")
    print("""    1 - Adicionar funcionário
    2 - Remover funcionário
    3 - Alterar dados
    4 - Listar funcionários
    5 - Voltar""")
    escolha = int(input("O que deseja?\n"))
    if escolha == 5: opcoes()

    list = [0, AddFuncionario(Interface), RemoveFuncionario(Interface), AlteraFuncionario(Interface), ListarFuncionario(Interface)]
    system_Function = list[escolha]
    executar = Executar()
    executar.setComando(system_Function)
    return executar.Escolha()

def opcoesFolha():
    print("\nOpções da folha:")
    print("""1 - Gerar Folha de Pagamento\n
             2 - Voltar""")
    escolha = int(input("O que deseja?\n"))
    if escolha == 1:
        Crud.listar()
        valor = float
        id = int(input("Insira o id do funcionário desejado: "))
        funcionario = None
        for i in listaFuncionario:
            # print(' entra ', i.getId())
            if i.getId() == id:
                funcionario = i

        if not funcionario:
            print('Id não encontrado')
            return 

        print(funcionario)
        
    
        if funcionario.getTipoFuncionario() == 'Horista':
            valor = funcionario.cartaoPonto()
            funcionario.setValorSalario(0)
            # opcoes()
            exit()
        elif funcionario.getTipoFuncionario() == 'Assalariado':
            valor = funcionario.salarioAssalariado()
            funcionario.setSalario(0)
            # opcoes()
            exit()
        else:
            valor = funcionario.comissao()
            funcionario.setTaxaComissao(0)
            # opcoes()
            exit()

        funcionario.agendar()
        print('Salario: | Data de pagamento: \n', valor, funcionario.agenda)
        
    
    if escolha == 2:
        opcoesFolha()
         

def opcoes():
    print("\nMenu principal:")
    print("""1 - Espaço funcionario\n2 - Folha de Pagamento\n3 - Sair""")
    escolha = int(input("O que deseja?\n"))
# 
    if escolha == 1:
        while(True):
            opcoesFuncionario()
    elif escolha == 2:
# 
        opcoesFolha()
    elif escolha == 3:
        print("Obrigada por utilizar nosso sistema, volte sempre!")
        exit()
    else:
        print("\nNão entendi, vamos recomeçar o atendimento")
        opcoes()

print("Seja bem-vindo ao sistema Folha de Pagamento")

opcoes()