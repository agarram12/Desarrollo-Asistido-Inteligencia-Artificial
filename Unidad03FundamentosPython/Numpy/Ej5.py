estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota_media": 8.5, "asignaturas_aprobadas": 12},
    {"nombre": "Carlos", "edad": 22, "nota_media": 6.2, "asignaturas_aprobadas": 9},
    {"nombre": "Lucía", "edad": 19, "nota_media": 9.1, "asignaturas_aprobadas": 15},
    {"nombre": "Marcos", "edad": 21, "nota_media": 7.0, "asignaturas_aprobadas": 10},
    {"nombre": "Elena", "edad": 23, "nota_media": 5.8, "asignaturas_aprobadas": 7},
    {"nombre": "Sofía", "edad": 20, "nota_media": 7.8, "asignaturas_aprobadas": 13},
    {"nombre": "David", "edad": 22, "nota_media": 8.2, "asignaturas_aprobadas": 11},
    {"nombre": "Javier", "edad": 21, "nota_media": 4.5, "asignaturas_aprobadas": 5},
    {"nombre": "Marta", "edad": 19, "nota_media": 7.2, "asignaturas_aprobadas": 10},
    {"nombre": "Hugo", "edad": 20, "nota_media": 6.9, "asignaturas_aprobadas": 8}
]

# 1. Filtrar estudiantes con nota_media >= 7.0
sobresalientes = [est for est in estudiantes if est["nota_media"] >= 7.0]

# 2. Estudiante con más asignaturas aprobadas
estudiante_top = max(estudiantes, key=lambda x: x["asignaturas_aprobadas"])

# 3. Edad promedio de los estudiantes aprobados (nota_media >= 5.0)
edades_aprobados = [est["edad"] for est in estudiantes if est["nota_media"] >= 5.0]
edad_promedio = sum(edades_aprobados) / len(edades_aprobados) if edades_aprobados else 0

print(f"Estudiantes con nota >= 7.0: {[e['nombre'] for e in sobresalientes]}")
print(f"Estudiante con más aprobadas: {estudiante_top['nombre']} ({estudiante_top['asignaturas_aprobadas']})")
print(f"Edad promedio de aprobados: {edad_promedio:.1f} años")