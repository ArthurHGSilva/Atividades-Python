notas = []
soma = 0
qtd_notas = 0
final = float

while qtd_notas < 5:
    notas.append(int(input('Coloque as notas: ')))
    qtd_notas = qtd_notas + 1
    final = sum(notas)/5
print(final)
