num1 = float(input('Coloque o valor do primeiro número: '))
num2 = float(input('Coloque o valor do segundo número: '))
operacao = input('Coloque a operação desejada: ')


if operacao == '+':
    resultado = num1 + num2
    print('Adição\t', resultado)

elif operacao == '-':
    resultado1 = num1 - num2
    print('Subtração\t', resultado1)

elif operacao == '*':
    resultado2 = num1 * num2
    print('Multiplicação\t', resultado2)

elif operacao == '/':
    resultado3 = num1 / num2
    print('Divisão\t', resultado3)
