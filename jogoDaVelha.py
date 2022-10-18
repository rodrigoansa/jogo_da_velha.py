import os

#cadastro de jogadores
print('Cadastre os jogadores.')
jogador_x = input('Jogador x: ')
jogador_o = input('Jogador o: ')

#escolha de quem começa jogando
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


p = [None, None, None, None, None, None, None, None, None,]
vez = None

if escolha == '1':
    vez == jogador_x
    p == 'x'
else:
    vez == jogador_o
    



linha = input('Linha: ')
coluna = input('Coluna: ')

def posicao():
    if linha == '1' and coluna == '1':
        print(p[0])
    elif linha == '1' and coluna == '2':
        print(p[1])
    elif linha == '1' and coluna == '3':
        print(p[2])
    elif linha == '2' and coluna == '1':
        print(p[3])
    elif linha == '2' and coluna == '2':
        print(p[4])
    elif linha == '2' and coluna == '3':
        print(p[5])
    elif linha == '3' and coluna == '1':
        print(p[6])
    elif linha == '3' and coluna == '2':
        print(p[7])
    elif linha == '3' and coluna == '3':
        print(p[8])

posicao()

while p == 'x':
    p == 'o'



#Front
print('     1      2      3')
print(f'1{p[0]}|{p[1]}|{p[2]}')
print('   -------------------')
print(f'2{p[3]}|{p[4]}|{p[5]}')
print('   -------------------')
print(f'3{p[6]}|{p[7]}|{p[8]}')