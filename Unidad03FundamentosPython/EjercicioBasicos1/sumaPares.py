# Usa un bucle for para sumar solo los números pares del 1 al 20
# Imprime el resultado final
numeros = range(1,21)
acumula = 0;
for num in numeros:
    if num % 2 == 0:
        num = num + acumula
        acumula = num

print(num)
