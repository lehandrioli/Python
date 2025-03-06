#CALCULO ANO BISSEXTO
import datetime
ano = int(input('Informe um ano: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ANO {} É ANO BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É ANO BISSEXTO'.format(ano))
