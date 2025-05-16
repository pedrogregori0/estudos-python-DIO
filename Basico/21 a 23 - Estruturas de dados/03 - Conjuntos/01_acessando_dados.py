# Aula 23 - Acessando dados de Conjuntos (Conjuntos) 
# Conjuntos não suportam Indexação e nem Fatiamento
# É necessario converter o Set para uma lista, para poder acessar os dados

numeros = {1,2,3,2}

lista_numeros = list(numeros) # Transforma o set em listam pra poder ser acessado por indice

print(lista_numeros[0])