#11. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles?



num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
start = min(num1, num2)
end = max(num1, num2)
print(f"Números inteiros no intervalo de {start} a {end}:")
for i in range(start, end + 1):
    print(i, end=" ")