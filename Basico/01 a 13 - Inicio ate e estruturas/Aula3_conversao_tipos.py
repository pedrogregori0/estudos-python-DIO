#Aula 3
#Conversões

#Int
print(int(2.0)) #Declarando como inteiro, ele printa e reconhece como inteiro 

#Int de Str
print(int("20")) #Converte a string "20" para inteiro - *sem ser numero da erro*

#Float de Str
print(float("20.20")) #Converte a string "20.20" para float - *sem ser numero da erro*

#Float de Int
print(float(23)) #Converte o inteiro 23 para float 

#String de Float
print(str(10.10)) #declarado como float - é converido para String

valor = 30
valor_str = str(valor)
print(type(valor)) #(type) - Mostra o tipo da variavel
print(type(valor_str))

print(100/4) #Toda divisão da o resultado em float
print(100//4) #Define que ira aparecer apenas a parte inteira, sem ser flutuante
