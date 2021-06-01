n1 = int(input('Digite um número: '))
list = []
soma = 0

for x in range(0, n1):
    num = int(input('Coloque um número: '))
    list.append(num)
    soma = soma + num
print(min(list))
print(max(list))

media = soma/n1
print(media)
