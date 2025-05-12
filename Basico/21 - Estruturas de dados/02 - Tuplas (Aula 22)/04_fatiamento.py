# Aula 22 - Fatiamento (Tuplas)
# Acessa a Tupla e retorna o conteudo selecionado dentro do indice inicial e final, podendo tambem passar quantas posições pular no acesso

tupla = ("e", "x", "e", "m", "p", "l", "o",)

# É Obrigatório passar o inicio ou final (exemplo de erro > tupla [ : ])

tupla[2:] # Passado o parametro somente de inicio (vai ate o final), Indice 2 - ['e', 'm', 'p', 'l', 'o']

tupla[:3] # Passado somente o parametro de fim (vem desde o começo), Indice 3 - ['e', 'x', 'e']

tupla[1:5] # Parametro de inicio e de fim, Indice inicial de 1 e final de 5 - ['x', 'e', 'm', 'p']

tupla[0:4:2] # Passado parametro inicial, final e STEP(faz ele andar de 2 em 2(Indice passado)) - ['e', 'e']

tupla[::] # Vazio, sem inicio sem fim e sem STEP, ele vai de 0 ate o final da string e com o STEP padrão de 1 em 1 - ["e", "x", "e", "m", "p", "l", "o"]

tupla[::-1] # Sem inicio e sem fim, STEP -1 invertendo toda a Lista - ['o', 'l', 'p', 'm', 'e', 'x', 'e']