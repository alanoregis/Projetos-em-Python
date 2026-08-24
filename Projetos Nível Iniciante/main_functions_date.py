from functions import *

print("############################\n")
print("Qual a data de vencimento?")
print("Formato: DIA-MES-ANO. Exemplo: 09-05-1999\n")
print("############################\n")

due_date = input("")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Entrada inválida!")