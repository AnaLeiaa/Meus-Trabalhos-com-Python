nome = str(input('Qual é o seu nome? '))
if nome == 'Léia':
    print('Que nome bonito você tem!')
elif nome == 'John' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é popular no Brasil')
elif nome == 'Fernanda':
    print('nome feio esse kk')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
