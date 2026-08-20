import random

print("Bem vindo ao Guess Number!")
escolha_numero = input("Digite o número teto do desafio: ")

if escolha_numero.isdigit():
    escolha_numero = int(escolha_numero)
else:
    print("O valor informado não é númerico, execute novamente e informe um número!")
    quit()

numero_aleatorio = random.randint(0, escolha_numero)

n_tentativas = 0

while True:
    resposta_usuario = input("Advinhe o número: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("O valor informado não é númerico, execute novamente e informe um número!")
        continue

    n_tentativas += 1
    if resposta_usuario == numero_aleatorio:
        print("Acertou!")
        break
    elif resposta_usuario > numero_aleatorio:
        print("Chutou alto, o número randomico é menor que isso...")
    else:
        print("Chutou baixo, o número randomico é maior que isso...")

print("Numero de tentativas: " + str(n_tentativas))