
trab = float(input('A nota do trabalho foi:'))
P1 = float(input('A nota da P1 foi:'))
P2 = float(input('A nota da P2 foi:'))

med_arit = (P1 + P2) / 2
med_final = (med_arit * (0.7)) + (trab * (0.3))
print('A média final é:', str(med_final))
