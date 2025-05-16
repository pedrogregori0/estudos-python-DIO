# Aula 23 - Unindo dados com o metodo .issuperset (Conjuntos) 
# IsSuperSet retorna True ou False - verifica se todos os elementos do conjunto estão em outro conjunto

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b)) # False - todos os elementos de B estão em A? Não!
print(conjunto_b.issuperset(conjunto_a)) # True - todos os elementos de A estão em b? Sim!
