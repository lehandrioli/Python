#SENO, COSSENO, TANGENTE
import math
angulo = int(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O seno do ângulo é igual a: {:.2f}'.format(seno))
coseno = math.cos(math.radians(angulo))
print('O coseno do ângulo é igual a: {:.2f}'.format(coseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do ângulo é igual a: {:.2f}'.format(tangente))
