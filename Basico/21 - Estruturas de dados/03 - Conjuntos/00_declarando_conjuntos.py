# Aula 23 - Declarando conjuntos (Conjuntos) 
# ele não deixa elementos duplicados usando o (set)
# set espera um iteravel no construtor

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # a ordem tende a ser aleatório de maquina pra maquina {'x', 'b', 'a', 'c', 'i'}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"celta", "gol", "palio"}

# Não muito utilizado
# pode ser declarado tambem dentro de chaves {}
linguagens = {"pyhton", "Java", "C#", "Java"} # {'pyhton', 'C#', 'Java'}
print(linguagens)