# Aula 23 - verifica os conjuntos separados (Conjuntos) 
# IsDisjoint retorna True ou False - verifica se todos os elementos do conjunto estão juntos de outro conjunto com intersecção

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True - Vê que os elementos dos conjuntos não estão interseccionados, cada conjunto tem elementos diferente e assim retorna True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False - ele vê que o "1" tem intersecção com os 2 conjuntos e da False, porque não é "Disjunto"
print(resultado)