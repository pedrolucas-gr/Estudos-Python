from turtle import Turtle
t = Turtle()
t.speed(1)
resposta = ''
while resposta != 'n':
    direcao = input('Para qual direção devemos ir? (f)frente ou (t)trás ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        rotacionar = input('Rotacionar para (d)direita, (e)esquerda, (n)não rotacionar ')
        if rotacionar == 'd':
            angulo = int(input('Quanto graus para a direita devemos rotacionar? '))
            t.right(angulo)
        elif rotacionar == 'e':
            angulo = int(input('Quanto grauspara a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        rotacionar = input('Rotacionar para (d)direita, (e)esquerda, (n)não rotacionar ')
        if rotacionar == 'd':
            angulo = int(input('Quanto graus para a direita devemos rotacionar? '))
            t.right(angulo)
        elif rotacionar == 'e':
            angulo = int(input('Quanto graus para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continuar andando? (s)sim ou (n)não ')
print('Fim')