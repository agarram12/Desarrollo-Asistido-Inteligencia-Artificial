from functools import reduce
# Dada esta lista de ventas diarias:
ventas = [150, 200, 175, 300, 250, 180, 220]

# Usa reduce() para:
# 1. Calcular el total de ventas
# 2. Encontrar la venta máxima (sin usar max())
# 3. Calcular el promedio (combina reduce con len())

total = reduce(lambda a, b: a + b, ventas)

maximo_venta = reduce(lambda a,b: a if a > b else b, ventas)
promedio = total / len(ventas)

print("Total de ventas: ", total)
print("Venta máxima", maximo_venta)
print("Promedio: ", promedio)