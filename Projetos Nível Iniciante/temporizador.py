import time

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()

while t: # 0 simboliza o False / 1,2, ... simboliza True
    minutos, segundos = divmod(t, 60)
    timer = f"{minutos:02d}:{segundos:02d}"
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("SEU TEMPO ACABOU!!!")