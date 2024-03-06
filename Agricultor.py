print("Cuanto debes de regar los cultivos")
Papa = 0
Yuca = 0
Zanahoria = 0
cultivos = int(input("<<<< CULTIVOS EXISTENTES >>>>\n1. Papa ->\n2. Yuca ->\n3. Zanahoria ->\n -> "))
if cultivos == 1:
    for i in range(3):
        litrosPInt = int(input("Cuantos litros regaste -> "))
        Papa = Papa + litrosPInt
    print("Tu total de litros regados fueron", Papa)
elif cultivos == 2:
    for i in range(3):
        litrosYInt = int(input("Cuantos litros regaste -> "))
        Yuca = Yuca + litrosYInt
    print("Tu total de litros regados fueron", Yuca)
elif cultivos == 3:
    for i in range(3):
        litrosZInt = int(input("Cuantos litros regaste -> "))
        Zanahoria = Zanahoria + litrosZInt
    print("Tu total de litros regados fueron", Zanahoria)

