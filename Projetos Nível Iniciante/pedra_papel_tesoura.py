import random

usuario_pontos = 0
computer_pontos = 0

opcoes = ["r", "t", "p"]

while True:
    escolha_usuario = input("Escolha R(Pedra) /T(Tesoura) /P(Papel) ou Q para sair.").lower()

    if escolha_usuario == 'q':
        break

    escolha_computer = random.randint(0,2)
    # 0 : R, 1 : T, 2 : P
    opcao_computer = opcoes[escolha_computer]

    print("O computador escolheu " + opcao_computer.upper())

    if escolha_usuario == opcao_computer:
        print("Empate!")

    elif escolha_usuario == "r" and opcao_computer == "t":
        print("Você ganhou!")
        usuario_pontos += 1

    elif escolha_usuario == "p" and opcao_computer == "r":
            print("Você ganhou!")
            usuario_pontos += 1

    elif escolha_usuario == "t" and opcao_computer == "p":
            print("Você ganhou!")
            usuario_pontos += 1

    else:
         print("Você Perdeu!")
         computer_pontos += 1

print("Sua pontuação: " + str(usuario_pontos))
print("Pontuação do Computador: " + str(computer_pontos))

if usuario_pontos > computer_pontos:
     print("Vitória!!!")
elif computer_pontos == usuario_pontos:
     print("Empate")
else:
     print("Derrota!!!")