a = int(input('DIGITE O PRIMEIRO VALOR: '))
b = int(input('DIGITE O SEGUNDO VALOR: '))
c = int(input('DIGITE O TERCEIRO VALOR'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {} '.format(maior))
print('O menor valor é {} '.format(menor))
