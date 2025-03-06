#ANALISE DE FRASE
nome = str(input('Digite seu nome Completo: ')).strip()
print('O seu nome com todas as letras maiusculas fica:')
print('{}'.format(nome.upper()))
print('O seu nome com todas as letras minusculas fica:')
print('{}'.format(nome.lower()))

dividido = nome.split()

print('O seu nome tem {} Letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} Letras'.format(len(dividido[0])))