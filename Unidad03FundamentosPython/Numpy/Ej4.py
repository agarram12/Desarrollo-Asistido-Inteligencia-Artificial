inventario = {}

def agregar_producto(nombre, precio, cantidad):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]["precio"] = nuevo_precio

def actualizar_stock(nombre, nueva_cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] = nueva_cantidad

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]

def mostrar_inventario_ordenado():
    # Ordenamos los productos por el valor 'precio' de su diccionario interno
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])
    for nombre, datos in productos_ordenados:
        print(f"{nombre}: ${datos['precio']} (Stock: {datos['cantidad']})")

def valor_total_inventario():
    total = sum(p["precio"] * p["cantidad"] for p in inventario.values())
    return round(total, 2)

# Pruebas del sistema
agregar_producto("Laptop", 899.99, 5)
agregar_producto("Mouse", 15.99, 20)
agregar_producto("Teclado", 45.50, 15)

print(f"Valor total inicial: {valor_total_inventario()}")

actualizar_precio("Mouse", 12.50)
eliminar_producto("Teclado")

print("--- Inventario ordenado por precio ---")
mostrar_inventario_ordenado()