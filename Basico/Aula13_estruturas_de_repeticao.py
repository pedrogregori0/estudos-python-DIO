#Aula 13
#Estruturas de repetição (for e while)

#For
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: #para cada letra no texto faça:
    if letra.upper() in VOGAIS: #se a letra.Maiuscula estar em Vogais faça:
        print(letra, end="") #imprime a letra e retorna para o começo ate finalizar o laço 
        
else: #não é muito comum usar o else no final do For
    print() #adiciona a quebra de linha 
    print("print do final do laço for\n") 

#exemplo de função built-in range
for numero in range(0, 51, 5): # range tem (inicio, fim, passos(no caso vai ser de 5 em 5))
    print(numero)
print()
#While (enquanto não for definido o fim, ele sera executado)
opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma opção\n1- Sacar\n2- Extrato\n0- Sair \n"))
    
    if opcao == 1:
        print("Sacando...\n")
    elif opcao == 2:
        print("Exibindo o extrato...\n")
    else:
        print("Obrigado por utilizar nosso sistema")
        
        #break quebra a sequencia e finaliza o laco