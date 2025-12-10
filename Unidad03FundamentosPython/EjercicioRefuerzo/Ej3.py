def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    nums = sorted(numeros)
    n = len(nums)
    if n % 2 == 1:
        mediana = nums[n // 2]
    else:
        mediana = (nums[n // 2 - 1] + nums[n // 2]) / 2
    from collections import Counter
    frecuencias = Counter(numeros)
    moda = frecuencias.most_common(1)[0][0]
    rango = max(numeros) - min(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    return {
        "media": round(media, 2),
        "mediana": mediana,
        "moda": moda,
        "rango": rango,
        "varianza": round(varianza, 2)
    }
datos = [23, 45, 67, 45, 89, 12, 45, 34, 56, 78]
resultados = calcular_estadisticas(datos)
print(resultados)