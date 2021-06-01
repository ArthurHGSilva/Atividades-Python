vagassalas = [20, 5, 10, 2]
print('Salas disponíveis: ')
print('Sala 1 =', vagassalas[0], '\nSala 2 =', vagassalas[1], '\nSala 3 =', vagassalas[2], '\nSala 4 =', vagassalas[3])

while True:
    sala = int(input('Qual sala você vai querer? '))
    if sala == 0 or sala > 4:
        print('Esta sala sala não existe')
        break
    qtd = int(input('Quantos ingressos você vai querer? '))
    if qtd > vagassalas[sala-1]:
        print('Não há lugares disponíveis nessa sala, escolha outra')
        print('\nSala 1 =', vagassalas[0], '\nSala 2 =', vagassalas[1], '\nSala 3 =', vagassalas[2], '\nSala 4 =', vagassalas[3])
    if qtd <= vagassalas[sala-1]:
        print('Ticket comprado')
        vagassalas[sala-1] = vagassalas[sala-1] - qtd
        print('Salas disponíveis: ')
        print('\nSala 1 =', vagassalas[0], '\nSala 2 =', vagassalas[1], '\nSala 3 =', vagassalas[2], '\nSala 4 =', vagassalas[3])
        break
