n = []

for x in range(0,20):
    nomes = str(input('Coloque o seu nome: '))
    idade = int(input('Coloque a sua idade: '))
    sexo = str(input('Coloque o seu sexo: '))
    if sexo == str('Masculino') and idade > 21:
        n.append(nomes)
print(n)
