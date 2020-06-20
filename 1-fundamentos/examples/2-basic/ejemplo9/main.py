name = input("¿Cúal es tu nombre?\n")
age = int(input("¿Cúal es tu edad?\n"))
weigh = float(input("¿Cúal es tu peso?\n"))
auth = bool(input("¿Estas autorizado? (si/no)\n") == "si")

print("Hola:", name)
print("Edad:", age)
print("Peso:", weigh)
print("Autorización:", auth)
