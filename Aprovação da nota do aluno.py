nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda ? '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('ALUNO REPROVADO')
elif media < 5:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')
elif media >= 7.0:
    print('VOCÊ FOI APROVADO!')
