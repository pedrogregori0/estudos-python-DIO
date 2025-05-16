# Aula 23 - tirando algum valor dos conjuntos(Conjuntos) 
# Pop - tira um valor da lista, não precisa do argumento

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # vai sequencialmente, pelo inicio
print(numeros.pop())  # 0 # mostra o item retirado
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9} # mostra o conjunto atualizado com os argumentos removidos