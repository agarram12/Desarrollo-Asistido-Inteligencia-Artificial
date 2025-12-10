# Ejemplo de salida esperada:
# Ingrese la temperatura: 25
# Unidad de origen (C/F/K): C
# Unidad de destino (C/F/K): F
# 25.0°C = 77.0°F

temperatura = float(input("Ingrese la temperatura: "))
origen = input("Unidad de origen (C/F/K): ").upper()
destino = input("Unidad de destino (C/F/K): ").upper()

if origen == "C":
    temp_c = temperatura
elif origen == "F":
    temp_c = (temperatura - 32) * 5 / 9
elif origen == "K":
    temp_c = temperatura - 273.15
else:
    print("Elige una opción de origen válida (C/F/K)")
    exit()

if destino == "C":
    temp_destino = temp_c
elif destino == "F":
    temp_destino = temp_c * 9/5 + 32
elif destino == "K":
    temp_destino = temp_c + 273.15
else:
    print("Elige una opción de destino válida (C/F/K)")
    exit()

print(f"{temperatura}°{origen} = {temp_destino}°{destino}")
