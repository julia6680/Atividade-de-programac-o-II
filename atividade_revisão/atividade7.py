#7.Para votar, você deve ter entre 18 anos e menos de 65 anos. Escreva um
# programa que pergunte sua idade e diga se você é obrigado a votar ou não?

idd=int(input('Digite sua idade?'))
if idd >= 18 and idd < 65:
    print('Voce é obrigado a votar.')
else:
    print('Você não é obrigado a votar.')