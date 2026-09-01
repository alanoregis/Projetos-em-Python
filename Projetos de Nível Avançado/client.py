from database import DatabaseClient

database_1 = DatabaseClient(1234)
database_2 = DatabaseClient(5678)

print(database_1.get_connnection())
print(database_2.get_connnection())

if database_1 == database_2:
    print("São iguais!")
else:
    print("Não são iguais!")

database_1.set_classmates(["Alano"])
print(database_1.get_classmates())

database_2.set_classmates(["Myllena"])
print(database_2.get_classmates())
print(database_1.get_classmates())