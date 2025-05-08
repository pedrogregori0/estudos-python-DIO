#Aula 20
# Funções parte 3 - escopo local e global

salario = 2000 #esta definido fora da função que vai utiliza-lo

def salario_bonus(bonus):
    
    global salario #sem o global, dentro da definição a variavel salario não é vista
    
    lista_aux = lista.copy() #copia a lista de fora, associando os valores dela para a variavel lista_aux
    lista_aux.append(2)
    print(f"Lista Auxiliar = {lista_aux}")
    
    salario += bonus #agora que foi "declarada" voce pode fazer a operação
    return salario


lista = [1]
salario_bonificado = salario_bonus(500)
print(salario_bonificado)
print(lista)

