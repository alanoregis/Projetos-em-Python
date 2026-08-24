import json
import random 

f = open("words.json", encoding="utf8")

words = json.load(f)
print(list(words.keys()))
choice_c = random.choice(list(words.keys()))

print("Ola, Bem vindo a SMT!")
print("###############################")

n_choices = 5
win = False

while n_choices > 0 and win is not True:
    print("Dica: " + words[choice_c])
    answer_user = input("data: DDMMAAAA\n")
    print("#############################\n")

    if len (answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation += 1
            else:
                check.append("❌")
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("########################\n")

        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue
    n_choices -= 1

if win == True:
    print("Um Verdadeiro Summoner!!!")
else:
    print("GAME OVER")
    print("A resposta era: " + choice_c)