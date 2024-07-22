#8.Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
# Escreva um programa que pergunta a situação do usuário (se é idoso, se é
# gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não?


opcao = int(input('Digite o numero correspondente á sua situação:'))
if opcao == 1 or opcao == 2 or opcao == 3 :
    print('Você tem acesso à fila de prioridade.')
else:
    print('Você não tem acesso à fila de prioridade.')
    print("Situações possíveis:")
    print("1 - Idoso")
    print("2 - Gestante")
    print("3 - Pessoa com Deficiência (PCD)")
    print("4 - Nenhum destes")