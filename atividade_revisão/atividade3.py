#3.Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso?


turno=input('Digite turmo que voce estuda? ').lower()
if turno == 'matutino':
    print('Bom dia!')
elif turno == 'vespertino':
    print('Boa tarde!')
elif turno == 'noturno':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
