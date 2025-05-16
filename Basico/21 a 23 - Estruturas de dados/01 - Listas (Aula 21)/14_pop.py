# Aula 21 - Metodos da classe list (Listas)
# Pop - Conceito de pilha, pega a ultima coisa que foi colocada dentro da lista (um prato no topo da pilha por exemplo)

pilotos = ["M. Verstappen","G. Bortoleto","L. Norris", "C. Leclerc", "F. Alonso"]

pilotos.pop() # remove o ultimo parametro colocado na lista
pilotos.pop()
pilotos.pop(1) #remove o parametro indicado pelo indice

print(pilotos)