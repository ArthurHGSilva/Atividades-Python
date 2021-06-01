
p_total = int(input('Digite o número de entrevistados: '))

p_g = 0
p_ng = 0

m = 0
m_g = 0
m_ng = 0
por_m_ng = 0

f = 0
f_g = 0
f_ng = 0


for x in range(0,p_total):
    sexo = input('Qual é o seu sexo? M = masculino, F = feminino ')
    resposta = input('Gostou ou não? ')
    if resposta == 'gostei':
        p_g = p_g + 1
    if resposta == 'não':
        p_ng = p_ng + 1

    if sexo == 'M':
        m = m + 1
    if sexo == 'F':
        f = f + 1

    if sexo == 'M' and resposta == 'gostei':
        m_g = m_g + 1
    if sexo == 'M' and resposta == 'não':
        m_ng = m_ng + 1
    if sexo == 'F' and resposta == 'gostei':
        f_g = f_g + 1


print(p_g, 'pessoa(s) gostaram do produto')
print(p_ng, 'pessoa(s) não gostaram do produto')

por_m_ng = (m_ng*100) / m
print('A porcentagem das pessoas do sexo masculino que não gostaram foi de', por_m_ng, '%')

if f_g > m_g:
    print('O produto foi melhor recebido entre as mulheres')
if m_g > f_g:
    print('O produto foi melhor recebido entre os homens')
if f_g == m_g:
    print('O produto foi bem recebido por ambos os públicos')
