from time import sleep
from random import randint
from Jogador import Player
from inputs import *
# JOGO

print("     ██   ██████   ██████    ██████       ██████   ██████   ██████ ".center(210))
print("     ██  ██    ██  ██       ██    ██      ██   ██  ██   ██  ██     ".center(210))
print("     ██  ██    ██  ██  ███  ██    ██      ██████   ██████   ██  ███".center(210))
print("██   ██  ██    ██  ██   ██  ██    ██      ██  ██   ██       ██   ██".center(210))
print(" █████    ██████    ██████   ██████       ██   ██  ██        ██████".center(210))
print('')
print('')
print('[1] Jogar')
print('[2] Carregar Save')
print('[3] Sair')
print('')
print('Selecione uma das Opções acima:')
print('')
esc1 = input_int('> ')
print('')
print('')
print('')
print('')
if esc1 == 1:
    print('')
    p1 = Player.criar_player(None)
    print('')
    print(f'Bem Vindo {p1.nickname}')
    print('')
elif esc1 == 3:
    print('Até mais')
    




