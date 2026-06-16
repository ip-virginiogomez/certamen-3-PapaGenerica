velocidad_1 = int(input("Ingrese 1ra velocidad en Km/h"))
velocidad_2 = int(input("Ingrese 2da velocidad en Km/h"))
velocidad_3 = int(input("Ingrese 3ra velocidad en Km/h"))
velocidad_4 = int(input("Ingrese 4ta velocidad en Km/h"))
velocidad_5 = int(input("Ingrese 5ta velocidad en Km/h"))

velocidades = [velocidad_1,velocidad_2,velocidad_3,velocidad_4,velocidad_5]

print(velocidades)

for i in velocidades:
    print()
    if i >= 60:
        print("Velocidad permitida")
    elif i <= 20:
        print("Velocidad peligrosa por lentitud")
    elif i >= 140:
        print("Exceso de velocidad")
    else:
        print("ni fu ni fa")