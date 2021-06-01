nadador = int(input('Coloque a idade do nadador: '))

if nadador >= 5 and nadador <= 7:
    print('Infantil A')

elif nadador >= 8 and nadador <= 10:
    print('Infantil B')

elif nadador >= 11 and nadador <= 13:
    print('Junevil A')

elif nadador >= 14 and nadador <= 17:
    print('Juvenil B')

elif nadador >= 18:
    print('Adulto')

else:
    print('O nadador é muito novo e ainda não pode participar')
