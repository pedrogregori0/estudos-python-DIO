# Aula 23 - Discarta algum valor dos conjuntos(Conjuntos) 
# Discard - Discarta o valor passado como parâmetro

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) # descarta o numero 1
numeros.discard(45) # descarta o numero 45, ele ira ignorar o valor que não existe

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}