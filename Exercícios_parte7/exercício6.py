def fatorial(n):
    if n == 0:
        return 1
    else:
        fat = n * fatorial(n-1)
    return fat

def s(n1):
    if n1 == 1:
        return 1
    else:
        f = 1/fatorial(n1)
        f += s(n1 - 1)
    return f
n = int(input('Coloque um número: '))
print(s(n))
