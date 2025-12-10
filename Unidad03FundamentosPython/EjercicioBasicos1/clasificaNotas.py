# Crea un programa que reciba una nota (0-10) y muestre:
# - "Suspenso" si es menor que 5
# - "Aprobado" si está entre 5 y 6.9
# - "Notable" si está entre 7 y 8.9
# - "Sobresaliente" si es 9 o más
nota = 7.5
# Tu código aquí
if nota < 5: 
    print("Suspenso")
elif nota > 5 and nota < 6.9:
    print("Aprobado")
elif nota > 7 and nota < 8.9:
    print("Notable")
elif nota > 9:
    print("Sobresaliente")
else:
    print("Nota no válida")