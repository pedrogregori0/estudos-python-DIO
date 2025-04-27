#Aula 16
# Fatiamento de Strings

# variavel[start:end] - colocar os indices dentro das [ : ] para ele fatiar o conteudo da string
# para espelhar a variavel [::-1]

nome = "Pedro Rafael Adriano Gregório"

print(nome[0]) #pega somente a letra do indice passado no colchete
print(nome[-1]) #pega a ultima letra 
print(nome[:5]) #fatia desde o começo ate o indice passado
print(nome[13:]) #fatia do indice passado ate o final
print(nome[6:13]) #fatia somente o que há dentro dos indices - (sub-string)
print(nome[:]) #Pega toda a string
print(nome[::-1])

