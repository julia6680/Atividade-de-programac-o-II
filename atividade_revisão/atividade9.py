#9.Faça um programa que leia um nome de usuário e a sua senha e não aceite
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e
# voltando a pedir as informações?


while True:
    usuario = input ('Digite o nome de usuario:')
    senha = input('Digite a senha:')
    if senha == usuario:
        print('Erro: A senha nao pode ser igual ao nome de usuario .tente novamente.')
    else:
        print('Cadastro realizado com sucesso!')
        break
