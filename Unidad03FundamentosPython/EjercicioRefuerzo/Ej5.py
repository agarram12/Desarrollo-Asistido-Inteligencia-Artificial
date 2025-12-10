estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota_media": 8.5, "asignaturas_aprobadas": 12},
    {"nombre": "Carlos", "edad": 22, "nota_media": 6.2, "asignaturas_aprobadas": 9},
    {"nombre": "Beatriz", "edad": 21, "nota_media": 7.8, "asignaturas_aprobadas": 14},
    {"nombre": "David", "edad": 23, "nota_media": 5.9, "asignaturas_aprobadas": 7},
    {"nombre": "Elena", "edad": 19, "nota_media": 9.1, "asignaturas_aprobadas": 15},
    {"nombre": "Fernando", "edad": 24, "nota_media": 6.8, "asignaturas_aprobadas": 10},
    {"nombre": "Gabriela", "edad": 20, "nota_media": 7.2, "asignaturas_aprobadas": 11},
    {"nombre": "Hugo", "edad": 22, "nota_media": 8.1, "asignaturas_aprobadas": 13},
    {"nombre": "Irene", "edad": 21, "nota_media": 6.5, "asignaturas_aprobadas": 8},
    {"nombre": "Javier", "edad": 25, "nota_media": 7.9, "asignaturas_aprobadas": 16}
]

aprobados = [est for est in estudiantes if est["nota_media"] >= 7.0]

top_asignaturas = max(estudiantes, key=lambda e: e["asignaturas_aprobadas"])

edad_promedio = sum(est["edad"] for est in aprobados) / len(aprobados)

print("Estudiantes aprobados (nota_media >= 7.0):")
for estudiante in aprobados:
    print(f"- {estudiante['nombre']} ({estudiante['nota_media']})")

print("\nEstudiante con más asignaturas aprobadas:")
print(f"{top_asignaturas['nombre']} ({top_asignaturas['asignaturas_aprobadas']} asignaturas)")
print(f"\nEdad promedio de los estudiantes aprobados: {round(edad_promedio, 2)}")
