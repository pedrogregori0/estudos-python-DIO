#Aula 10
#Operadores de Associação (in, not in), são operadores utilizados para verificar se um objeto esta presente em uma sequência

frutas = ["limao", "uva", "pera"] #lista de palavras
curso = "Curso de Python"

mensagem_falsa ="não esta em "
mensagem_verdadeira = "esta em"

if ("laranja" not in frutas):
    print("laranja", mensagem_falsa, "frutas")
if("limao" in frutas):
    print("limao", mensagem_verdadeira, "frutas")
    
print("laranja" in frutas) #laranja não esta então sera Falso
print("limao" not in frutas) #limão esta entao sera Falso
print("Python" in curso) #Python esta em curso, lembrando que é case sensitive, tem que estar escrito da MESMA forma