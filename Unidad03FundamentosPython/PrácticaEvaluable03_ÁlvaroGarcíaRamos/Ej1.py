# Ventas mensuales en euros (Enero a Diciembre)
ventas = [15000, 18000, 22000, 17000, 25000, 30000, 28000, 32000, 27000, 29000, 35000, 40000]
# a)
total_ventas = sum(ventas)
print(f"a) Total anual: {total_ventas} €")
# b)
def calcular_estadisticas(lista): 
    total = sum(lista)
    promedio = total / len(ventas)
    mes_mejor = lista.index(max(lista))
    mes_peor = lista.index(min(lista))
    return (total, promedio, mes_mejor, mes_peor)
estadistica = calcular_estadisticas(ventas)
print(f"b) Estadísticas: ${estadistica}")
# c
promedio_anual = estadistica[1]
ventas_superiores = [f"Mes {i+1}: €{v}" for i, v in enumerate(ventas) if v > promedio_anual]
print(f"c) Ventas superiores al promedio: {ventas_superiores}")
# d
ventas_inflacion = list(map(lambda x: x * 1.15, ventas))
ventas_filtro = list(filter(lambda x: x > 30000, ventas_inflacion))
print(f"d) Ventas con inflación y filtrando > 30k: {ventas_filtro}")