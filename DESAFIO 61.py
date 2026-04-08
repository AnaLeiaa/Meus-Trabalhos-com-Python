print('GERADOR DE PA')
print('-=-'*7)
primeiro = int(input('Primeiro termo: '))
razao = int(input('RAZÃO DA PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} => ', end=' ')
    termo += razao
    cont += 1
print('FIM')
