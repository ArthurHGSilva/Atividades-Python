a = []
b = []
c = []
ta = int(input('Digite o tamanho de A: '))
tb = int(input('Digite o tamanho de B: '))

for i in range(ta):
    a.append(int(input('Digite um número: ')))
c.append(a[0])

for i in range(tb):
    b.append(int(input('Coloque um número: ')))

for i in range(len(a)):
    cont = 0
    for x in range(len(c)):
        if c[x] == a[i]:
            cont = cont + 1
    if cont == 0:
        c.append(a[i])

for i in range(len(b)):
    cont = 0
    for x in range(len(c)):
        if c[x] == b[i]:
            cont = cont + 1
    if cont == 0:
        c.append(b[i])

print(c)

    
