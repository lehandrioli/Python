#COMPRA COM DESCONTO
print('\33[1;36m=' *10, 'LOJA TESTE', '='*10)

valor = float(input('\33[0mInforme o valor da compra: R$'))
vl1 = valor*0.10
vl2 = valor*0.05
vl3 = valor*0.20

print('''\33[1;36m[1] À VISTA (DINHEIRO/CHEQUE)
[2] À VISTA CARTÃO DE CRÉDITO 
[3] CARTÃO DE CRÉDITO (2x)
[4] CARTÃO DE CREDITO (3x OU MAIS''')
ops = int(input('\33[0mEscolha a forma de pagamento: '))

if ops == 1:
    print('\33[1;32mVocê obteve 10% de desconto, a sua compra saira por R$ {:.2f}'.format(valor - vl1))
elif ops == 2:
    print('\33[1;32mVocê obteve 5% de desconto, a sua compra saira por R$ {:.2f}'.format(valor - vl2))
elif ops == 3:
    print('\33[1;32mA sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(valor/2))
elif ops == 4:
    parc = int(input('\33[0mQuantas parcelas? '))
    juros = valor + vl3
    print('''\33[1;32mA sua compra será parcelada em {}x de {:.2f} COM JUROS.
Sua compra de {:.2f} vai custar R$ {:.2f} no final.'''.format(parc,(juros/parc), valor, juros))
else:
    print('\33[1;31mCOMANDO INVALIDO')