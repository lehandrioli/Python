nome = str(input('Informe seu nome completo: ')).strip().upper()
print('Olá {}, prazer em te conhecer.'.format(nome))

separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0]))

print('Seu ultimo nome é {}'.format(separa[len(separa)-1]))