num1 = int(input('Coloque o valor do número:'))

mod = (num1 %3)
mod2 = (num1 %7)

if mod and mod2 == 0:
    print('O número é divisível por 3 e 7')
else:
    print('O número não é divisível nem por 3 nem por 7')
