def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

a = int(input('Coloque o valor de a: '))
b = int(input('Coloque o valor de b: '))
print(multiplo(a, b))
