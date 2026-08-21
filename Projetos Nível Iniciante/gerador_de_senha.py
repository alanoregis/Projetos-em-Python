import random
import string

def gerador_de_senha(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    usuario_senha = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        usuario_senha = usuario_senha + digit

    return usuario_senha

usuario_escolha = input("Quantos digitos na senha? ")

if usuario_escolha.isdigit():
    usuario_escolha = int(usuario_escolha)
else:
    print("Entrada inválida!")
    quit()

resposta = gerador_de_senha(usuario_escolha)
print(f"Senha gerada:\n{resposta}")