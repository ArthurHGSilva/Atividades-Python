n1 = int(input('Coloque um número: '))
cont = 1

for x in range(1,n1+1):
    print(x)
    cont = cont * x
    if x == n1:
        print(cont)
