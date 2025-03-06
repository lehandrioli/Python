#ANALISADOS DE TRIANGULOS
print('-='*15)
print('ANALISADOR DE TRIANGULOS')
print('-='*15)

#segmentos
a = float(input('Primeiro Seguimento: '))
b = float(input('Segundo Seguimento: '))
c = float(input('Terceiro Seguimento: '))

if a < b + c and b < a + c and c < b + a:
    print('\033[1;32mOs seguimentos acima PODEM FORMAR triangulo!')
    if a == b == c:
        print('Este triangulo é EQUILÁTERO')
    elif a != b != c and c != a:
        print('Este triangulo é ESCALENO')
    else:
        print('Este triangulo é ISÓSCELES')
else:
    print('\033[1;31mOs seguimentos acima NãO PODEM FORMAR triangulo!')