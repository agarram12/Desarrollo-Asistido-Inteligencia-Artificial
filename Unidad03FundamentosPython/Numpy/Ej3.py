def calcular_estadisticas(numeros):
    n = len(numeros)
    numeros_ordenados = sorted(numeros)
    
    media = sum(numeros) / n
    
    mitad = n // 2
    if n % 2 == 0:
        mediana = (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    else:
        mediana = numeros_ordenados[mitad]
        
    frecuencias = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    
    max_frecuencia = 0
    moda = numeros[0]
    for num, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            moda = num
            
    rango = max(numeros) - min(numeros)
    
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    varianza = suma_cuadrados / n

    return {
        'media': round(media, 2),
        'mediana': mediana,
        'moda': moda,
        'rango': rango,
        'varianza': round(varianza, 2)
    }

datos = [23, 45, 67, 45, 89, 12, 45, 34, 56, 78]
resultados = calcular_estadisticas(datos)
print(resultados)