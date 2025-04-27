#Aula 18
# Funções parte 1


# ============== Definindo funções ==============

def exibir_mensagem1():
    print("Hello world!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!") # É obrigatório receber um parametro "nome" para funcionar
    
def exibir_mensagem3(nome="Anônimo"): # É Opcional colocar o parametro, pois ja esta definido dentro da função como "Anônimo"
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem1() # Exibe normal, a função não recebe parametros

exibir_mensagem2(nome="Pedro") # É necessario passar o parametro "nome" para ele funcionar

exibir_mensagem3() # Não é necessario passar o parametro "nome", pois ja esta definido um dentro da função, fica opcional inserir o parametro nome
exibir_mensagem3(nome="Fierce") # Como foi passado o parametro ele ira exibir o que foi passado a ele


# ============== Retorno da função ==============

def calcular_total(numeros): # Tem que receber numeros para fazer o calculo e retornar a soma
    return sum(numeros)

def num_antecessor_e_sucessor(numero): 
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor #retorna uma tupla (29,31)

print(calcular_total([1, 6, 9, 0, 11])) 
print(num_antecessor_e_sucessor(30))


# ============== Argumentos nomeados ============== 

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido no banco de dados! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("McLaren", "Senna", "2023", "SEN-2003")
salvar_carro(marca="McLaren", modelo="Senna", ano="2023", placa="SEN-2003")
salvar_carro(**{"marca":"McLaren", "modelo": "Senna", "ano": "2023", "placa": "SEN-2003\n"}) # Tipo um dicionario


# ============== *Args e **Kwargs (*Lista e **Dicionario) ============== 

#Args - renderiza como uma tupla, valores vem dentro de uma tupla (Ex: "Uma frase dentro de string", [0, 2, 23])
#- tudo que estiver dentro de um parenteses com um valor simples("valor","valor")e estiver separado por apenas uma virgula, vai ser um *Args

#Kwargs - renderiza como dicionario, valores vem como dicionario (Ex: {"marca":"McLaren", "modelo": "Senna", "ano": "2023", "placa": "SEN-2003"} )
#- quando ele reconhecer que há chave e valor(Ex: nome = "pedro")

def exibir_poema(data_extenso, *args, **kwargs): # (*args = lista) (**kwargs = dicionario)
    texto = "\n".join(args) #cada vez que chegar no fim de um argumento("frase de exemplo"), ele ira adicionar uma quebra de linha 
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) #Pega o que vem em formato Kwargs(Dicionario) e separa para exibir
    mensagem = f"{data_extenso}\n\n {texto}\n\n {meta_dados}" #pega tudo que foi gerado acima organiza e coloca quebra de linhas pra facilitar a leitura
    print(mensagem)
    
exibir_poema("Sabádo, 26 de Abril", "Um lindo poema", "que contem apenas 3 linhas", "mas foi um bom exemplo", autor= "Pedro Gregório", ano = 2025)