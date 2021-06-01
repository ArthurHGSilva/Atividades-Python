cig_dias = int(input('Quantos cigarros por dia você fuma? '))
anos_fu = int(input('Há quantos anos você fuma? '))
total_cig = anos_fu * 365 * cig_dias
red_vida = total_cig * (10/(60*24))
print('Você perdeu', red_vida, 'dias de vida')
