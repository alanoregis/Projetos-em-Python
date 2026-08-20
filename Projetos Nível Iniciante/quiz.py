print("Bem vindo ao Quiz de Shin Megami Tensei V!")
resposta_usuario = input("Quer começar? (S/N) ")
print(resposta_usuario)

if resposta_usuario != "S":
    quit()

score = 0

print("Começando...")
print("Em Shin Megami Tensei V, qual é o nome dado à fusão entre um estudante humano e Aogami que forma o protagonista? \n (A) Demiurge \n (B) Nahobino \n (C) Demi-Fiend \n (D) Chrono Trigger \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "B":
    print("Correto!")
    score += 1
else:
    print("Game Over!")

print("Em Shin Megami Tensei III: Nocturne, qual é o nome do protagonista? \n (A) Demi-Fiend \n (B) Raidou Kuzunoha \n (C) Dante \n (D) Amala \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "A":
    print("Correto!")
    score += 1
else:
    print("Game Over!")

print(f"Quiz acabou... Pontuação: {score}/2")