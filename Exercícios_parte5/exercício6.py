lista  = [8, 3, 2, 19]
qtd = 4

while qtd > 1:
    ind = 0
    troco = False
    while ind < (qtd-1):
        if lista[ind] < lista[ind+1]:
            troco = True
            aux = lista[ind]
            lista[ind] = lista[ind+1]
            lista[ind+1] = aux
        ind += 1
    if not troco:
        break
for i in lista:
    print(i)
