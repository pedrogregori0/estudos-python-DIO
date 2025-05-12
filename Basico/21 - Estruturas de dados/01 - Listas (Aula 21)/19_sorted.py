# Aula 21 - Metodos da classe list (Listas)
# Sorted - função ja inclusa na biblioteca de Python

pilotos = ["M. Verstappen","G. Bortoleto","L. Norris", "C. Leclerc", "F. Alonso","C. Leclerc"]


#Ordena em crescente do menor pro maior, no caso com o tamanho das letras em cada item da lista
print(sorted(pilotos, key=lambda x: len(x))) #(key=lambda x: len(x)) - lambda é uma função anônima, para cada item("x") ele ira executar o código("len(x)") - len vai ler o tamanho de cada string da lista

#Ordena em decrescente do MAIOR pro MENOR, fazendo assim os itens com mais letras começarem na lista
print(sorted(pilotos, key=lambda x: len(x), reverse=True))

print(sorted(pilotos)) #Vai organizar por ordem alfabética