def mudaNome(nome, index):
    clientes[index] = nome

def deletaNome(nome):
    clientes.pop(nome)

"""itens"""
saia = 30.00
moletom = 70.50
camisa01 = 40.00
camisa02 = 45.50
celular = 300.00
notebook = 700.00
itens = ["saia - 30.00R$", "moletom - 70.50R$", "camisa roxa - 40.00R$", "camisa preta - 45.50R$", "celular - 300.00R$", "notebook - 700.00R$"]

clientes = []
credito = []
itens01 = []
itens02 = []
itens03 = []
clienteAtual = ""
dinheiroAtual = 0

while True:
    if(len(clientes == 0)):
        escolha = int(input("Olá, você ainda não se registrou, aperte [1] para registrar um nome, [2] para adicionar fundos "))
    elif(len(clientes) == 3):
        escolha = int(input("Você já não consegue adicionar mais contas, por favor escolha outra coisa: [3] para apagar alguma conta, [4] para alterar nome, [5] entrar na conta, [6] comprar "))
    else:
        escolha = int(input("Olá, aperte [1] para registrar um nome, [2] para adicionar fundos, [3] para apagar alguma conta, [4] para alterar nome, [5] entrar na conta, [6] comprar "))

    """Analise da escolha do user"""
    if(escolha == 1):
        nome = input("Digite seu nome: ")
        nome.upper()
        clientes.append(nome)
    
    elif(escolha == 2):
        dinheiro = float(input("Quanto desejará depositar? "))
        credito.append(dinheiro)
    
    elif(escolha == 3):
        if(len(clientes) == 0):
            print("Ainda não há clientes registrados!")
            escolha = int(input("Olá, você ainda não se registrou, aperte [1] para registrar um nome, [2] para adicionar fundos "))
        elif(len(clientes) == 3):
            escolha = int(input("Você já não consegue adicionar mais contas, por favor escolha outra coisa: [3] para apagar alguma conta, [4] para alterar nome, [5] entrar na conta, [6] comprar "))
        print(clientes)
        index = int(input("qual destes clientes deseja apagar?"))
        deletaNome(index)
    
    elif(escolha == 4):
        print(clientes)
        index = int(input("Qual desses clientes deseja alterar? "))
        nome = input("Coloque o novo nome: ")
        mudaNome(nome, index)
    
    elif(escolha == 5):
        if(len(clientes) == 0):
            print("Ainda não há clientes registrados!")
            escolha = int(input("Olá, você ainda não se registrou, aperte [1] para registrar um nome, [2] para adicionar fundos "))
        print(clientes)
        index = int(input("Selecione o cliente para entrar"))
        clienteAtual = clientes[index]
        dinheiroAtual = credito[index]
    
    elif(escolha == 6):
        print("Venda de itens")
        print(saia, moletom, camisa01, camisa02, celular, notebook)
        if(dinheiroAtual < 30):
            print("Parece que você não tem dinheiro, volte outra hora")
        else:
            print("Qual destes itens, você gostaria de comprar?")
            for i in itens:
                print(i)
                buy = int(input("Aperte [1] para comprar e [2] para negar: "))
                if(buy == 1 and clienteAtual == clientes[0]):
                    itens01.append(i)
                elif(buy == 1 and clienteAtual == clientes[1]):
                    itens02.append(i)
                elif(buy == 1 and clienteAtual == clientes[2]):
                    itens03.append(i)

    else:
        print("algo deu errado, tente novamente")
