"""Exercicio 73"""

print('=' * 30)

print('VAMOR JOGAR PAR OU ÍMPAR')
print('=' * 30)

from random import randint
cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um numero: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = (jogador + computador)
    resto_div = (soma % 2)
    if resto_div == 0 and tipo == 'I' or resto_div == 1 and tipo == 'P':
        break
    else:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi de {soma} ', end='')
        print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
        print('Você venceu!!!')
        print('Vamos jogar novamente...')
    cont += 1
print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi de {soma}')
print('Você Perdeu!!!')
print(f'Você venceu {cont} vezes seguidas.')
