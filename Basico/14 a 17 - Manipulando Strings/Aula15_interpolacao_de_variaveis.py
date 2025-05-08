# Aula 15
# exemplos de como chamar a variavel dentro da frase (String)

nome = "Pedro"
idade = 23
profissao = "estudante"
linguagem = "Python"
saldo = 99.929

#Utiliza o "%" para chamar a variavel, junto da variavel no final da string na sequencia correta
print("Nome: %s Idade: %d (porcentagem)" % (nome, idade)) #igual em C#, mas não é ideal pra usar em python

#Utiliza as "{}" para chamar a variavel, tambem junto do ".format" no final da string, na sequencia que é chamada
print("Nome: {} Idade: {} (Chaves)".format (nome, idade))

#Usa da mesma forma da anterior, porem se guiando pelos Indices 
print("Nome: {0} Idade: {1} (Chaves + Indices)".format (nome, idade))

#Utiliza o modo mais pratico e facil de leitura, o f string (**** IDEAL SEMPRE ****)
print(f"Meu nome é {nome}, tenho {idade} anos e atualmente sou {profissao} da linguagem {linguagem}, na minha conta bancária hoje tenho {saldo} (f Strings)")
print(f"ou na verdade {saldo:.2f}")