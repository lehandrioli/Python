nome = str(input('Digite seu nome Completo: ')).strip().lower()
print('seu nome tem {} letras A'.format(nome.count('a')))
print('A primeira vez em que a letra A aparece é na posição {}'.format(nome.find('a')+1))
print ('A ultima vez em que a letra A aparece é na posição {}'.format(nome.rfind('a')+1))