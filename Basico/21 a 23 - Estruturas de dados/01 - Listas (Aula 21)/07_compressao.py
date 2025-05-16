# Aula 21 - Compressão de Listas (Listas)
# A Compressão de lista oferece uma sintaxe mais curta quando voce deseja: criar uma nova lista com base nos valores de uma lista ja existente,
# ou gerar uma nova lista aplicando alguma modificação nos elementos da lista original

numeros = [1, 5, 44, 16, 33, 10, 12, 55]
pares = []

#exemplo basico de um for
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) #se o resto da divisão por 2 ser 0 ele adiciona na lista de pares e printa a lista na linha a baixo

#exemplo de comprehension do PYTHON
pares = [numero for numero in numeros if numero % 2 == 0] #basicamente é igual o exemplo de cima

#exemplo de modificação de valor
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) #pega o numero e multiplica ao quadrado, logo apos insere na lista quadrado

print(f"Pares:{pares}")
print(f"Ao quadrado:{quadrado}")

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])