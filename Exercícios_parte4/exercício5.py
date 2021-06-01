dep_inicial = float(input('Coloque o valor do depósito: '))
tx = float(input('Coloque a taxa de juros: '))

mes = 1
saldo = dep_inicial

while mes <= 24:
    if mes < 2:
        dep_inicial = (dep_inicial * (tx / 100)) + dep_inicial
        print('Saldo do mês', mes, 'é %.3f' %dep_inicial)

    else:
        dep_mensal = float(input('Coloque o valor do depósito mensal: '))
        dep_inicial = (dep_inicial * (tx / 100)) + dep_inicial + dep_mensal
        print('Saldo do mês', mes, 'é %.3f' %dep_inicial)
    mes = mes + 1
print('O ganho obtido com os juros durantes os 24 meses foi%.3f' %dep_inicial)
