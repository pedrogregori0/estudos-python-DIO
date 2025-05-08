#Aula 12
#Estruturas condicionais (Etapa 1 = if, if-else, elif) (Etapa 2 = if aninhado) (Etapa 3 = if ternário)

Maior_de_idade = 18

#if elif e else (Etapa 1)
idade = int(input("Coloque sua idade: "))

if idade >= Maior_de_idade:
    print("Você é maior de idade, pode tirar a CNH")
    
elif(idade <= 0):
    print("essa idade é invalida")

else:
    print("Voce é menor de idade, ainda não pode tirar a CNH")
    
    
#if aninhado (if dentro de if) (Etapa 2)
conta_normal = False #trocar as contas pra ver o exemplo rodar
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o cheque especial")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente para saque")
        
else:
    print("Nenhuma conta vinculada")
    
    
#if ternário (if em uma linha) (Etapa 3)
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
