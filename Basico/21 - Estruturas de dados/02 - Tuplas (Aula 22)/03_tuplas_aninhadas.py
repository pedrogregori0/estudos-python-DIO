# Aula 22 - Matriz (Tuplas)
# Basicamente funciona o acesso igual as listas

matriz =(
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # retorna somente uma linha ([1, "a", 2])
matriz[0][0] #retona uma linha e uma coluna (1)
matriz[0][-1] #retona o valor da linha 0 e o ultimo item dessa própia linha (2)
matriz[-1][-1] #retona a ultima linha e a ultima coluna ("c")
