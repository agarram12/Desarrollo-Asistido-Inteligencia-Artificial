inventario = {}

def agregar_producto(nombre, precio, cantidad):
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }

def valor_total_inventario():
    total = 0
    for producto in inventario.values():
        total += producto["precio"] * producto["cantidad"]
    return round(total, 2)

agregar_producto("Laptop", 899.99, 5)
agregar_producto("Mouse", 15.99, 20)
agregar_producto("Teclado", 45.50, 15)

print(valor_total_inventario())
