edad_usuario = int(input("Ingrese su edad"))
tarjeta_s = input("¿Tiene tarjeta de socio? si/no")
monto = int(input("Ingrese el monto total de su compra"))

if monto > 10000:
    print()
    
elif tarjeta_s == "si" or edad_usuario > 60:
    print("Puede acceder al descuento")

else:
    print("No puede acceder al descuento")

if monto > 10000 and (tarjeta_s == "si" or edad_usuario == 60):
    print(f"Tiene acceso al descuento de 15% en su compra de {monto} dejando asi")