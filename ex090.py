aluno = dict()
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Média do aluno: '))

if aluno['media'] < 5:

    aluno['situacao'] = 'Reprovado(a)'

elif 5 >= aluno['media'] < 7:

    aluno['situacao'] = 'Recuperação'

else:

    aluno['situacao'] = 'Aprovado(a)'

print(f'O nome do aluno(a) é {aluno["nome"]}. ')
print(f'A média do aluno(a) é {aluno["media"]}. ')
print(f'A situação do aluno(a) é {aluno["situacao"]}. ')
