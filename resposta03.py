# Faça um programa que leia e valide as seguintes informações:
# A. Nome: maior que 3 caracteres;
# B. Idade: entre 0 e 150;
# C. Salário: maior que zero;
# D. Sexo: 'f' ou 'm';
# E. Estado Civil: 's', 'c', 'v', 'd';

# Validação do nome
nome = ""
tamanho_nome = len(nome)
while len(nome) <= 3:
    nome = input("Informe o nome:")
    if len(nome) <= 3:
        print("O nome precisa ter mais que 3 letras!")

# Validação da idade
idade_invalida = True
while idade_invalida:
    idade = int(input("Informe a idade: "))
    idade_invalida = idade < 0 or idade > 150
    if idade_invalida:
        print("A idade deve ser entre 0 e 150!")

# Validação do salário
salario = -30
while salario<=0:
    salario = float(input("Informe seu salário"))
    if salario<=0:
        print("Informe um salário maior que 0!")

# Validação do sexo
sexo = ""
while sexo.upper() != "M" and sexo.upper() != "F":
    sexo = input("Informe o seu sexo:")
    if sexo.upper() != "M" and sexo.upper() != "F":
        print("O sexo deve ser M ou F")

#Validação do estado civil
estado_civil = "a"

while "SCVD".find(estado_civil.upper()) == -1:
    estado_civil = input("Informe o seu estado civil: ")
    if "SCVD".find(estado_civil.upper()) == -1:
        print("O estado civil precisa ser: (S)Solteiro, (C)Casado, (V)Viúvo ou (D)Divorciado!")