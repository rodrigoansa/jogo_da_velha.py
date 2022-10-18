import os

print('Cadastre os jogadores.')
jogador_x = input('Jogador x: ')
jogador_o = input('Jogador o: ')

print(f'Escolha quem começa o jogo.\n1 - Jogador x: {jogador_x} \n2 - Jogador o: {jogador_o}')
escolha = input('Escolha: ')
os.system('clear')

if escolha == '1':
    print('Ordem de jogadores')
    print(f'1: {jogador_x}')
    print(f'2: {jogador_o}')
else:
    print(f'1: {jogador_o}')
    print(f'2: {jogador_x}')

#posição
p = [1,2,3,4,5,6,7,8,9]
jogada_1 = input('')


#Front
print('___|___|___')
print('___|___|___')
print('   |   |   ')
