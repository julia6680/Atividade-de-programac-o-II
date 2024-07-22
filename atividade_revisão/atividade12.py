#12.Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores?


numeros = input("Digite os números separados por espaço: ")
min_valor = None
max_valor = None
soma = 0
for i in range(numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    if min_valor is None or numero < min_valor:
        min_valor = numero
    if max_valor is None or numeros > max_valor:
        max_valor = numeros
    soma += numeros
print(f"Menor valor: {min_valor}")
print(f"Maior valor: {max_valor}")
print(f"Soma dos valores: {soma}")