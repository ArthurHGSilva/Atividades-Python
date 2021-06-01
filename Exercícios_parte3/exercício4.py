salario = float(input('Coloque o valor do seu salário: '))
novo_s = 10
novo_i = 15

if salario > 1250:
    print((salario * novo_s / 100) + salario)
elif salario < 1250:
    print((salario * novo_i / 100) + salario)
