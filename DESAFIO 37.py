num = int(input('Digite um número inteiro: '))
base = str(input('Qual base de conversão você quer? Digite o item: \n[1] binario\n[2] octadecimal\n[3] hexadecimal\n'))
a = bin(num)
b = oct(num)
c = hex(num)
if base == '1':
    print('O valor {} em binário fica: {}'.format(num, a[2:]))
elif base == '2':
    print('O valor {} em octadecimal fica {}'.format(num, b[2:]))
elif base == '3':
    print('O valor {} em hexadecimal fica {}'.format(num, c[2:]))
else:
    print('O intem informado é invalido!')


