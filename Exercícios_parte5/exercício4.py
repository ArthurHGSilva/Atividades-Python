l1 = []
l2 = []

l3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, 10):
    num1 = int(input('Coloque um número na 1º lista: '))
    l1.append(num1)
for x in range(0, 10):
    num2 = int(input('Coloque um número na 2° lista: '))
    l2.append(num2)

l3[5] = l1[0] / l2[0]
l3[4] = l1[1] / l2[1]
l3[6] = l1[2] / l2[2]
l3[3] = l1[3] / l2[3]
l3[7] = l1[4] / l2[4]
l3[2] = l1[5] / l2[5]
l3[8] = l1[6] / l2[6]
l3[1] = l1[7] / l2[7]
l3[9] = l1[8] / l2[8]
l3[0] = l1[9] / l2[9]

print(l3)
