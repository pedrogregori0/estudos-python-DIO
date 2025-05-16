# Aula 23 - Adiciona elementos nos conjuntos(Conjuntos) 
# Add - adiciona elementos passado como parâmetros e os adiciona em um conjunto caso ele não seja existente

sorteio = {1, 23}
print(sorteio) # {1,23}

sorteio.add(25) # {1,23, 25}
print(sorteio) 

sorteio.add(42) # {1,23, 25, 42}
print(sorteio) 

sorteio.add(25) # {1,23, 25, 42} - já existe, ele apenas ignora
print(sorteio) 
