dia = int(input('Coloque o dia de hoje: '))
mes = int(input('Coloque em que mês estamos: '))
ano = int(input('Coloque em que ano estamos: '))

dia_nas = int(input('Coloque o dia que você nasceu: '))
mes_nas = int(input('Coloque o mês qeu você nasceu: '))
ano_nas = int(input('Coloque o ano que você nasceu: '))

resul_dia = dia - dia_nas
resul_mes = mes - mes_nas
resul_ano = ano - ano_nas

if resul_mes >= 0 and resul_dia >=0:
    aux1ano = resul_ano
    aux1mes = int(resul_ano * 12)
    aux1dia = int(resul_ano * 365)
    print('A sua idade é: ', aux1ano, 'anos', aux1mes, 'meses', aux1dia, 'dias')
else:
    aux2ano = int(resul_ano - 1)
    aux2mes = int(resul_ano * 12 - 12)
    aux2dia = int(resul_ano * 365 - 365)
    print('A sua idade é: ', aux2ano, 'anos', aux2mes, 'meses', aux2dia, 'dias')
