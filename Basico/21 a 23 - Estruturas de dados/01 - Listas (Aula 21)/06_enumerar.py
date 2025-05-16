# Aula 21 - Enumerando Listas (Listas)
# utilizado para demonstrar o indice do objeto dentro de um laço for, por exemplo.

pilotos = ["M. Verstappen","G. Bortoleto","L. Norris", "C. Leclerc", "F. Alonso"]

# indice sera o contador, piloto é o iteravel da lista
for indice, piloto in enumerate(pilotos):
    print(f"{indice} - {piloto}")