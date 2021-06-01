dias = int(input('Coloque a quantidade de dias: '))
horas = int(input('Coloque a quantidade de horas: '))
min = int(input('Coloque a quantidade de minutos: '))
seg = int(input('Coloque a quantidade se segundos: '))

horas += dias * 24
min += horas * 60
seg += min * 60
print('O valor em segundos é', seg)
