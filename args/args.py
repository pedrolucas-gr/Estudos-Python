#Exercício que multiplica os argumentos não nomeados.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)