def recursiva(n1 , n2):
    if n2 == 0:
        return 1
    else:
        fat = n1 * recursiva(n1, n2 -1)
    return fat
n1 = int(input('Coloque um número: '))
n2 = int(input('Coloque um número: '))
print(recursiva(n1,n2))
