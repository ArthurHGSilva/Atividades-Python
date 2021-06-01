frase = list(input('Coloque uma frase: '))
meu_dicionario = {}

for x in range (len(frase)):
    meu_dicionario[frase[x]] = frase.count(frase[x])
print(meu_dicionario)
