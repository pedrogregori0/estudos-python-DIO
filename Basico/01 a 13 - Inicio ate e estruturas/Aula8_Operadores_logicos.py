#Aula 8 
#Operadores Lógicos (True, False, And, Or, Not)

# TRUE = Sempre vai ser verdadeiro
# FALSE = Sempre vai ser Falso
# AND = Para ser True tudo tem que ser True
# OR = Para ser True, somente um tem que ser True
# NOT = Inverte o resultado Booleano, se for Verdadeiro ele ira deixar Falso, e vice-versa

saldo = 1000
saque = 200
limite = 100
conta_especial = True
mensagem = "A Operação é: "
string_vazia = ""
contatos_de_emergencia = [] #lista vazia, sem valores

print("*AND*")
print("True and True =", True and True) #Resultado True
print("True and False =", True and False) #Resultado False
print("False and False =", False and False,"\n") #Resultado False

print("*OR*")
print("True or True =", True or True) #Resultado True
print("True or False =", True or False) #Resultado True
print("False or False =", False or False,"\n") #Resultado False

print("*NOT* (inverte o resultado)")
print("Era False mas o (not) inverteu e deixou: ", not 1000 > 1500) # "not" é a negação, seria o inverso do que é passado a ele, aqui 1000 nunca vai ser maior que 1500
print ("era False mas o (not) inverteu e deixou: ", not contatos_de_emergencia) #lista vazia é reconhecida como falsa, por não ter valor
print("era True mas o (not) inverteu e deixou: ", not "string saque 1000;")  #o not reconhece como "False", pois há um valor associado a String
print("Era False mas o (not) inverteu e deixou: ", not "" or string_vazia, "\n") #string vazia é reconhecida como falsa, pois não tem valor associado, mas o not reconhece como "True"

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite #as duas condições tem que ser verdadeiras, caso uma não for sera False
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
print("Conta normal com saldo suficiente: ",conta_normal_com_saldo_suficiente)
print("Conta Especial com saldo Suficiente:",conta_especial_com_saldo_suficiente, "\n")

print(mensagem, saldo >= saque or saque <= limite) #ou é um ou é outro
print(mensagem, saldo >= saque and saque <= limite or conta_especial and saldo >= saque) #True
print(mensagem, (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque),"\n") #True
