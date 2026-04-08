n = cont = soma = 0
while True:
    n = int(input('Digite um numero: '))
    cont += 1
    if n != 999:
        soma += n
    else:
        break
print(f'A quantidade de numeros digitados é {cont} e a soma entre eles é {soma}')
print('Acabou')

