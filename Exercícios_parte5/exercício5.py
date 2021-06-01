l1 = []
a = 0

for x in range(a, 10):
    n1 = int(input('Coloque um número: '))
    l1.append(n1)
print(l1)

for i in range(0, len(l1)):
    for x in range(0, len(l1)):
        aux = l1[i]
        if l1[x] > aux:
            l1[i] = l1[x]
            l1[x] = aux
print(l1)
