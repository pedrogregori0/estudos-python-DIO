# Aula 23 - Unindo dados com o metodo .issubset (Conjuntos) 
# IsSubSet retorna True ou False - verifica se todos os elementos do conjunto pertencem a outro conjunto

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b)) # True - todos os elementos do conjunto A pertencem ao grupo B
print(conjunto_b.issubset(conjunto_a)) # False - não há todos os elementros no Conjunto A