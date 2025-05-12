# Aula 21 - (Listas)
# Declarando listas 

frutas = ["Strawberry", "Apple", "Grappes"] #Lista com conteúdo
print(frutas)

frutas = [] #Lista vazia - pode ser declarada vazia, sem valores 
print(frutas)

letras = list("frase") #Lista criada de uma string, ele não coloca a string como objeto dentro, cada letra é um elemento ITERAVEL ("f","r","a","s","e")
print(letras)

numeros = list(range(10)) #Range ira gerar valores ate o valor passado como parametro
print(numeros)

carro = ["Audi","A8", 110000, 2020, 350, "São Paulo", True] #Lista com varios tipos dentro
print(carro)