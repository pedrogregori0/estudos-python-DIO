# Aula 21 - Metodos da classe list (Listas)
# Sort - Ordena os itens dentro da lista

pilotos = ["M. Verstappen","G. Bortoleto","L. Norris", "C. Leclerc", "F. Alonso","C. Leclerc"]

pilotos.sort() #Ordena em ordem alfabética
print(pilotos)

pilotos.sort(reverse=True) #Ordena em ordem alfabética ao CONTRÁRIO
print(pilotos)

#(key=lambda x: len(x)) - lambda é uma função anônima, para cada item("x") ele ira executar o código("len(x)") - len vai ler o tamanho de cada string da lista
pilotos.sort(key=lambda x: len(x)) #Ordena em crescente do menor pro maior, no caso com o tamanho das letras em cada item da lista
print(pilotos)

pilotos.sort(key=lambda x: len(x), reverse=True) #Ordena em decrescente do MAIOR pro MENOR, fazendo assim os itens com mais letras começarem na lista
print(pilotos)
