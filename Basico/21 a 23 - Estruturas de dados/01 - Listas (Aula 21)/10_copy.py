# Aula 21 - Metodos da classe list (Listas)
# Copy - Copia toda a lista, mas não é a lista original 

lista = [1, "teste", [1,65,2]]

print(lista)

lista2 = lista.copy() #copia a lista
lista2.append("segunda lista")

print(lista)
print(lista2)
