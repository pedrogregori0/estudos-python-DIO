#Aula 19
# Funções parte 2

# ============== Somente posicional / ==============
# Antes da / tudo tem que ser sem nomes, o que define é a posição (Ex: modelo, ano, placa)

def criar_carro_posicional(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro_posicional("Walkirie", 2024, "ABC-1234", marca= "Aston Martin", motor= "v8", combustivel="Gasolina") # Válido pois segue a ordem correta, e respeita a regra da /
#criar_carro(modelo="Walkirie", ano=2024, placa="ABC-1234", marca= "Aston Martin", motor= "v8", combustivel="Gasolina") # Inválido pois não respeita a regra


# ============== Somente Nomeados * ==============
# - todo mundo que for passado, tem que ser passado por nome (Ex: modelo= "Walkirie")

def criar_carro_nomeado(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro_nomeado(modelo="Walkirie", ano=2024, placa="ABC-1234", marca= "Aston Martin", motor= "v8", combustivel="Gasolina") #Válido


# ============== Parametros Posicionais e Nomeados /, * ==============

def criar_carro_hibrido(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro_hibrido("Walkirie", 2024, "ABC-1234", marca= "Aston Martin", motor= "v8", combustivel="Gasolina")


# ============== Objetos de primeira classe ============== 

def somar(a,b): #função de soma, recebe 2 valores
    return a + b

def exibir_resultado(a, b, funcao): # tem que receber 2 valores a, b e o valor equivalente a uma funcao que seja executado, no caso aqui seria somente a "somar"
    resultado = funcao(a, b) #atribui o resultado e atribui tambem a funcao recebida, fazendo com que ela seja executada com os valores e devolva os resultados
    print(f"O resultado da operação é {resultado}")
    
exibir_resultado(5,5, somar) # Aqui eu passo os valores pra soma, e tambem passo qual funcao eu quero que seja feita (somar) 