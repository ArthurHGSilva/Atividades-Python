estoque = {"Maça": [500, 0.35], "Banana": [3000, 0.15], "Manga": [350, 0.5]}
venda = [['Banana', 10], ['Manga', 5]]
total = 0

print('vendas: \n')

for indice in venda:
    produto, quantidade = indice
    preco = estoque[produto] [1]
    precoItem = preco * quantidade
    print('%-10s: %3d * %0.2f = %0.2f' %(produto, quantidade, preco, precoItem))
    estoque[produto] [0] -= quantidade
    total += precoItem
print('Preço Total: %16.2f \n' %total)
print('Estoque:\n')
for chave, dado in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dado[0])
    print('Preço: %0.2f' %dado[1])
