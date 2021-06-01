l1 = []
l2 = []

l3 = []
l4 = []


for x in range(0, 10):
    i = int(input('Coloque um número: '))
    l1.append(i)
for x in range(0, 10):
    i2 = int(input('Coloque um número: '))
    l2.append(i2)
for x in range(0, 10):
    i3 = input('Insira uma operação aritmética: ')
    l3.append(i3)
for x in range(len(l3)):
    if l3[x] == '+':
        i4 = l1[x] + l2[x]
        l4.append(i4)
    if l3[x] == '-':
        i4 = l1[x] - l2[x]
        l4.append(i4)
    if l3[x] == '*':
        i4 = l1[x] * l2[x]
        l4.append(i4)
    if l3[x] == '/':
        i4 = l1[x] / l2[x]
        l4.append(i4)
print(l4)
