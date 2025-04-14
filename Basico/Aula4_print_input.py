#Aula 4
#input pega a resposta do usuario atraves do console, por padrão sempre vai vir em "string"
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade) #por padrão o (end="") é o \n, pra dar a quebra de linha
print(nome, idade, end=" ... \n")
print(nome, idade, sep="#") #o que for inserido dentro do separador (sep="") vai separar as linhas
