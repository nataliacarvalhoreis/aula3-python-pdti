# Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a
# operação

paisA = float(input("Informe a população do primeiro pais: "))
taxaA = float(input("Informe a taxa do primeiro pais: "))
paisB = float(input("Informe a população do segundo pais: "))
taxaB = float(input("Informe a taxa do segundo pais: "))

ano = 0

while paisA < paisB:
    paisA = paisA + paisA * taxaA
    paisB = paisB + paisB * taxaB
    ano += 1

print("Quantidade de anos: ", ano)
print("População de A: ", paisA)
print("População de B: ", paisB)