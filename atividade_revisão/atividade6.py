#6.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da 
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente"?


perguntas = ["Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"]
pontos = 0 
for pergunta in perguntas:

   print(pergunta)

   resposta = input('Responda sim ou não:  ').lower( ).replace( 'ã' , 'a' )

   if resposta == 'sim':
      pontos +=1
      if pontos == 2:
        print('Esta pessoa é suspeita...')
   elif 3 <= pontos < 5:
    print('Esta pessoa é cúmplice!')
   elif pontos == 5:
    print('Esta pessoa é o assasino!')
else:
    print('Esta pessoa é inocente.')
      
