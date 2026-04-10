'''sexo = str(input('Informe seu sexo: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))'''

while True:
    sexo = str(input('Informe seu sexo (M,F): ')).upper()

    if sexo not in ['M', 'F']:
        print('Sexo informado é inválido, coloque M para Masculino ou F para Feminino.')
    else:
        break

print('Sexo ', sexo, 'registrado com sucesso!')








