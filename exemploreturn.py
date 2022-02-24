cadastrados = []
novousuario = {}
logandonome = logandousuario = logandosenha = ''
online = 0

for c in range(0,2):
    novousuario['nome'] = input('Digite seu nome: ')
    novousuario['nick'] = input('Digite seu nome de usuário: ')
    novousuario['senha'] = input('Digite sua senha: ')
    cadastrados.append(novousuario.copy())
print(cadastrados)

login = input('Digite seu nome de usuário: ')

for dicionario in cadastrados:
    if login == dicionario['nick']:
        logandonome = dicionario['nome']
        logandousuario = dicionario['nick']
        logandosenha = dicionario['senha']
        online = 1
        break
if online == 0:
    print('Usuário inválido. ')

password = input('Digite sua senha: ')
if password == logandosenha:
    print(f'Seja bem vindo(a) {logandonome}')
else:
    print('Senha inválida. ')

print(logandonome, logandousuario, logandosenha)
