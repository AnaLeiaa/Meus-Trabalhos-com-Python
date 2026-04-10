n = int(input('Digite um número: '))
b = n
text = ''
fat = 1
while n >= 1:
    text += str(n) + ' x '
    fat = fat * n
    n = n - 1


text = text[:-3]
print(f'Calculando {b}! =', text, '=', fat)



