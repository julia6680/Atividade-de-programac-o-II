#4.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida?

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split('/'))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
dias_por_mes = [31, 28 if not bissexto else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
data_valida = (1 <= mes <= 12) and (1 <= dia <= dias_por_mes[mes - 1])
if data_valida:
    print(f"A data {data} é válida.")
else:
    print(f"A data {data} não é válida.")

