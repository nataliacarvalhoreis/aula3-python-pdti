# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem de
# erro e voltando a pedir as informações

continua = True

while continua:
    usuario = input("Informe o usuário: ")
    senha = input("Informe a senha: ")
    if usuario != senha:
        break
    else:
        print("O usuário e a senha precisam ser diferentes!")

print("Obrigada, informações corretas!")