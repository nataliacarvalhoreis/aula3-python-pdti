# Faça um algoritmo que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido.

nota = float(input("Informe uma nota entre 0 e 10: "))

while nota <= 0.0 or nota >= 10.0:
    nota=float(input("Informe uma nota entre 0 e 10:"))

print("Obrigada! A nota informada foi: ", nota)