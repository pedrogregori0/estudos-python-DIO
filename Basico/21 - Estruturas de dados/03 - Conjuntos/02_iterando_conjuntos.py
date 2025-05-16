# Aula 23 - Iterando e Enumerando os dados (Conjuntos) 
# É possivel iterar os conjutos item a item

carros = {"Bmw", "Porsche","McLaren"}
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(indice, carro)