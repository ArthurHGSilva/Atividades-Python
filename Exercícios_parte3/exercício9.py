kWh = float(input('Qual a quantidade de kW/h consumida? '))
instalacao = str(input('Qual é o tipo de instalação? '))

if kWh <= 500 and instalacao == 'residencial':
    print('R$', kWh * 0.40)

elif kWh > 500 and instalacao == 'residencial':
        print('R$', kWh * 0.60)


if kWh <= 1000 and instalacao == 'comercial':
    print('R$', kWh * 0.55)

elif kWh > 1000 and instalacao == 'comercial':
    print('R$', kWh * 0.60)


if kWh <= 5000 and instalacao == 'industrial':
    print('R$', kWh * 0.55)

elif kWh > 5000 and instalacao == 'industrial':
    print('R$', kWh * 0.60)

