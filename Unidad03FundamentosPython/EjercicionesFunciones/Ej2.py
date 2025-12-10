# Dada esta lista de calificaciones:
notas = [4.5, 7.0, 3.2, 8.5, 5.5, 9.0, 4.0, 6.5]

# Usa filter() para obtener solo las notas >= 5.0
# Luego usa map() para convertirlas a strings con formato "Nota: X.X"

aprobados = filter(lambda n: n >= 5.0, notas)
aprobados_formateados = map(lambda n: f"Nota: {n}", aprobados)
resultado = list(aprobados_formateados)
print(resultado)
