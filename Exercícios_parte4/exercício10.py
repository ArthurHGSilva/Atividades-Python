n1 = int(input('Digite um número: '))
list = []

for x in range(0, n1):
    num = int(input('Coloque um número: '))
    list.append(num)
print(min(list))
