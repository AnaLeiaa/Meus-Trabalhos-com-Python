from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
ida = atual - nascimento
print('Oatleta tem {} anos.'.format(ida))
if ida <= 9:
    print('ATÉ 9 ANOS É MIRIM.')
elif ida <= 14:
    print('ATÉ 14 É INFANTIL.')
elif ida <= 19:
    print('ATÉ 19 ANOS É JÚNIOR.')
elif ida == 25:
    print('ATÉ 20 ANOS É SÊNIOR.')
else:
    print('ACIMA DE 20 É MASTER.')


