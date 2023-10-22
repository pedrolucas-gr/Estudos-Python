tentativas = 0
max_tentativas = 3
numero_premiado = 25
while tentativas < max_tentativas:
    numero_usuario = int(input("Escolha um número de 1 a 30: "))
    tentativas += 1
    if numero_usuario < numero_premiado:
        print("O número premiado é maior")
    elif numero_usuario > numero_premiado:
        print("O número premiado é menor")
    elif numero_usuario == numero_premiado:
        print("Parabéns, você ganhou!")
        break
    if tentativas == max_tentativas:
        print("Fim de Jogo! Número de tentativas acabou.")