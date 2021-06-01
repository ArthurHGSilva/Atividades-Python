dep_inicial = float(input('Coloque o valor do depósito: '))
tx = float(input('Coloque a taxa de juros: '))
mes = 1
saldo = dep_inicial

while mes <= 24:
    saldo = (saldo * (tx / 100)) + saldo
    print('Saldo do', mes, 'é %.4f' %saldo)
    mes = mes + 1
print('O ganho obtido com os juros durantes os 24 meses foi %.3f' %saldo)
