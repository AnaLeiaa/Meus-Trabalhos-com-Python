num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 é para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 é para parar]: '))
print(f'VocÊ digitou {cont} numeros e a soma entre eles foi {soma}')
