#Aula 14
# Fatiamento de strings

#Maiusculo e Minusculo nas strings
nome_baguncado = "pEdrO"

print(nome_baguncado.upper()) #metodo ".upper()" que deixa o nome todo em MAIUSCULO
print(nome_baguncado.lower()) #Metodo ".lower()"que deixa o nome todo em MINUSCULO
print(nome_baguncado.title() + "\n") #Metodo ".title()"que deixa o nome com a primeira letra em MAIUSCULO e o restante em MINUSCULO

#Remoção dos espaços das strings
nome_com_espacos = "     Pedro! "

print("." + nome_com_espacos + ". *os pontos definem o limite da frase com os espaços*")
print("." + nome_com_espacos.strip() + ".") #Metodo ".strip" que retira os espaços da string do lado direto e esquerdo
print("." + nome_com_espacos.lstrip() + ".") #Metodo ".lstrip" que retira os espacos do lado ESQUERDO da string
print("." + nome_com_espacos.rstrip() + ". \n") #Metodo ".rstrip" que retira os espacos do lado DIREITO da string

#Complemento de caracteres e centralizando a string
frase_boas_vindas = "Seja bem-vindo!"

print(frase_boas_vindas + " *frase original*")
print(frase_boas_vindas.center(30)) # Metodo que completa a qtd de caracteres; que voce colocar, deixando a string no meio (se não colocar parametro ele deixa vazio os espaços)
print(frase_boas_vindas.center(30, "#")) # foi passado o "#" como caracter para completar os espaços

#Iteração com cada caractere
print("|".join(frase_boas_vindas)) #faz a iteração entre cada letra e coloca o caractere definido entre " "