import numpy as np

# Calificaciones: 20 estudiantes, 5 asignaturas
# Filas = estudiantes, Columnas = asignaturas
np.random.seed(123)
calificaciones = np.random.uniform(4, 10, size=(20, 5))
calificaciones = np.round(calificaciones, 1)

asignaturas = ["Matemáticas", "Física", "Programación", "Inglés", "Historia"]

# a)
aprobado_todo_mask = np.all(calificaciones >= 5.0, axis=1) 
indices_aprobados = np.where(aprobado_todo_mask)[0]
print(f"a) Estudiantes que aprobaron todo: {np.sum(aprobado_todo_mask)}")
print(f"   Índices: {indices_aprobados}")

#b)
media_asignaturas = np.mean(calificaciones, axis=0)
mejor_asignatura = asignaturas[np.argmax(media_asignaturas)]
peor_asignatura = asignaturas[np.argmin(media_asignaturas)]
std_asignaturas = np.std(calificaciones, axis=0)
asig_mas_variable = asignaturas[np.argmax(std_asignaturas)]

print(f"b) Mejor asig: {mejor_asignatura}, Peor: {peor_asignatura}")
print(f"   Más variabilidad: {asig_mas_variable}")

#c) 
notas_medias_estudiantes = np.mean(calificaciones, axis=1)
condiciones = [
    notas_medias_estudiantes >= 9,
    notas_medias_estudiantes >= 7,
    notas_medias_estudiantes >= 6,
    notas_medias_estudiantes >= 5,
    notas_medias_estudiantes < 5
]
etiquetas = ["Sobresaliente", "Notable", "Bien", "Aprobado", "Suspenso"]
clasificacion = np.select(condiciones, etiquetas)
print(f"c) Clasificación primeros 5 alumnos: {clasificacion[:5]}")

# d)
mejor_por_asig_idx = np.argmax(calificaciones, axis=0)
print(f"d) Mejores estudiantes por asignatura (índices): {mejor_por_asig_idx}")
diferencias = calificaciones - media_asignaturas
diff_positivas = np.where(diferencias > 0, diferencias, 0)
suma_dev_positiva = np.sum(diff_positivas, axis=1)
estudiante_top_dev = np.argmax(suma_dev_positiva)

print(f"   Estudiante con mayor desviación positiva acumulada: Índice {estudiante_top_dev}")