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

#fazer uma def (funcao) de depositar e de sacar
#fazer uma tambem para extrato
mensagem_saldo_insuficiente = (f"o valor de saque é maior que seu saldo: R${saldo}")

def sacar(valor_saque): 
    if valor_saque >= 1 & valor_saque >= saldo:
        print(f"Saque Efetuado, saldo restante: R${saldo}")

def depositar(valor_deposito):
    global saldo
    
    if valor_deposito < 0:
        print("Digite um valor positivo para depositar")
        return

    if valor_deposito <= limite_deposito: 
        
        saldo += valor_deposito
        extrato_total_depositos + valor_deposito
        print(f"Depósito efetuado com sucesso, saldo atual: R${saldo}")
        print(extrato_total_depositos)
    else:
        print("Deposite um valor abaixo do limite de 500")




extratos_saques = [

]

extratos_depositos = [

]

extrato_geral = [
    extratos_saques,
    extratos_depositos
]

extrato_total_saques = 0 
extrato_total_depositos = []


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito") #inserir funcao aqui, pra ler o input
        valor_deposito  = int(input())
        print(type(valor_deposito))
        depositar(valor_deposito)                 
        #print(saldo)

    elif opcao == "s":
        print("Saque")
    
    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione uma opção corretamente")
