#10.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    idade = int(input("Digite a idade (entre 0 e 150): "))
    salario = float(input("Digite o salário (maior que zero): "))
    sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower() 
    if len(nome) <= 3:
        print("Erro: O nome deve ter mais de 3 caracteres. Tente novamente.\n")
        continue
    
    if not (0 <= idade <= 150):
        print("Erro: A idade deve estar entre 0 e 150 anos. Tente novamente.\n")
        continue
    
    if salario <= 0:
        print("Erro: O salário deve ser maior que zero. Tente novamente.\n")
        continue
    
    if sexo not in ['f', 'm']:
        print("Erro: O sexo deve ser 'f' ou 'm'. Tente novamente.\n")
        continue
    
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.\n")
        continue
    break
print("\nInformações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
estado_civil_descricao = {
    's': 'Solteiro(a)',
    'c': 'Casado(a)',
    'v': 'Viúvo(a)',
    'd': 'Divorciado(a)'
}
print(f"Estado Civil: {estado_civil_descricao[estado_civil]}")
    