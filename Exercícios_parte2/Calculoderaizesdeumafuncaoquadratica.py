a = int(input('Coloque o valor de a: '))
b = int(input('Coloque o valor de b: '))
c = int(input('Coloque o valor de c: '))

delta = b**2 - 4*a*c

if delta>=0:
    raiz_del = delta ** (1/2)
    x1= (-b+raiz_del)/2*a
    x2= (-b-raiz_del)/2*a
    print(x1)
    print(x2)
else:
    print('Delta não tem raíz')
