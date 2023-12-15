from time import sleep
from random import randint
jogos = []
print('-----------------------------')
print('     JOGA NA MEGA SENA       ')
print('-----------------------------')
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'------ SORTEANDO {qtd_jogos} JOGOS ------')
for i in range(1, qtd_jogos+1):
    for c in range (1, 7):
        c = randint(1, 61)
        jogos.append(c)
    jogos.sort()
    print(f'Jogo {i}: {jogos}')
    sleep(2)
    jogos.clear()
print('------ BOA SORTE ------')