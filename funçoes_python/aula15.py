def soma(n1,n2):
    return n1+n2
    


def subtração (n1,n2):
    return n1-n2


def multli (n1,n2):
    return n1*n2



def divisão (n1,n2):
    return n1/n2



n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))

 
escolha = input("1. soma 2.multli  3.divisao  4.sub : ")

if escolha == '1':
    print(soma(n1,n2))
elif escolha =='2':
    print(multli(n1,n2))
elif escolha =='3':
    print(multli(n1,n2))
elif escolha =='4':
    print(multli(n1,n2))



