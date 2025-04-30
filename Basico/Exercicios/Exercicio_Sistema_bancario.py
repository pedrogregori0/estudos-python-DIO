# Exercicio: criar um sistema bancario simples

#Sistema Bancário

#Requisitos mínimos: sacar, depositar, extrato.

#Deposito - valor positivo somente, todos os depósitos tem que ser armazenado em uma variável.
#Saque - Deve ter o limite de 3 saques diários, cada saque com o limite de R$500,00, se não tiver saldo exibir mensagem na tela, todos os Saques tem que ser armazenados em uma variável. 
#Extrato - Deve listrar todos os depósitos e saques realizados, junto do saldo atual.



menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

""" # Deixar a mensagem com varios espaços é vantajoso pra mostrar no terminal sem inserir quebra de linha (\n) 

saldo = 0
limite_deposito = 500

valor_saque = 0
valor_deposito = 0
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES_DIARIO = 3

extratos_saques = []

extratos_depositos = []

valor_total_saques = 0 
valor_total_depositos = 0

#fazer uma def (funcao) de depositar e de sacar
#fazer uma tambem para extrato

mensagem_saldo_insuficiente = (f"o valor de saque é maior que seu saldo: R${saldo}")

def depositar(valor_deposito):
    global saldo
    global valor_total_depositos
    
    if valor_deposito < 0:
        print("Digite um valor positivo para depositar")
        return

    if valor_deposito <= limite_deposito: 
        
        saldo += valor_deposito
        valor_total_depositos += valor_deposito
        extratos_depositos.append(str(valor_deposito))
        print(f"Depósito efetuado com sucesso, saldo atual: R${saldo}")
        # inserir o deposito na lista de extrato
    else:
        print("Deposite um valor abaixo do limite de 500")

def sacar(valor_saque): 
    global saldo
    global valor_total_saques
    global numero_de_saques
    
    if saldo <= 0:
        print("Saldo insuficiente para saque!")
        return
    
    elif numero_de_saques == LIMITE_SAQUES_DIARIO:
        print("Limite de saques diário atingido, volte amanhã")
        return
     
    elif valor_saque <= saldo:
            numero_de_saques += 1
            valor_total_saques += valor_saque
            saldo -= valor_saque
            extratos_saques.append(str(valor_saque))
            print(numero_de_saques)
            print(f"Saque Efetuado com sucesso, saldo restante: R${saldo}")
    else:
        print("Saldo insuficiente para saque!")


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito") #inserir funcao aqui, pra ler o input
        valor_deposito  = float(input("R$"))
        depositar(valor_deposito)       
        

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("R$"))
        sacar(valor_saque)
        
    
    elif opcao == "e":
        print("Extrato")
        print(extratos_depositos)
        print(extratos_saques)
        print(f"R${valor_total_depositos}")          

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione uma opção corretamente")
