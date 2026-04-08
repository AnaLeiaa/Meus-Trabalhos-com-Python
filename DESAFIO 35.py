print('\033[7;32m-=-\033[m' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('\033[7;32m-=-\033[m' * 20)
seg1 = float(input('PRIMEIRO SEGUIMENTO: '))
seg2 = float(input('SEGUNDO SEGMENTO: '))
seg3 = float(input('TERCEIRO SEGMENTO: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima podem formar triângulo ')
else:
    print('Os segmentos acima NÃO podem formar triangulo ')

