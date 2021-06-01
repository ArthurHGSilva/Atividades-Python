num = []
x = 100

while True:
    x = int(input('Coloque um número: '))
    if x != 0:
        num.append(x)
    else:
        break
print(num)
