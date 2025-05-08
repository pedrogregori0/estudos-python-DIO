#Aula 11
#Identação e blocos (bloco = espaçamento para melhorar a leitura do código, ou o TAB)

#Em python sempre tem que ser identado o bloco, se não ele não le corretamente, diferente de C# ou Java
def sacar(valor):
    saldo = 500
    
    #não precisa de {} pra abrir ou fechar o bloco, ele entende isso automaticamente, para abrir o bloco usasse o (:)
    if saldo >= valor:
        print("Saque efetuado!")
        
    print("Operação sinalizada")    
    
    
sacar(400)        
        
        
