# Aula 23 - tirando algum valor dos conjuntos(Conjuntos) 
# Remove - tira um valor da lista com o argumento passado, se não tiver argumento ele retira o valor inicial

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros.remove(4))  # 4 remove o argumento 4

# numeros.remove(15) - esse exemplo causa um erro, ele não pode remover um argumento que não está no conjunto 

print(numeros) # {1, 2, 3, 5, 6, 7, 8, 9}