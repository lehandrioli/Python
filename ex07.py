#SORTEIO DE NUMEROS
import random

print('Estou pensando em um número... Será que você acerto?')
usuario = int(input('Escolha um numero entre 0 e 5: '))

lista = [0,1,2,3,4,5]
escolha = random.choice(lista)
print('Eu escolhi o numero: {}'.format(escolha))

print('Você escolheu o numero {}'.format(usuario))

if escolha == usuario:
    print('Parabéns você acertou o número que pensei!')
else:
    print('Poxa, você errou.')