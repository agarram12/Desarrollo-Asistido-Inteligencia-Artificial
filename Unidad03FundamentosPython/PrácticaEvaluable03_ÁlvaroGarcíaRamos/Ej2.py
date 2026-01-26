# Inventario inicial
productos = {
    "laptop": {"precio": 850, "stock": 15, "categoria": "informatica"},
    "raton": {"precio": 25, "stock": 50, "categoria": "informatica"},
    "teclado": {"precio": 45, "stock": 30, "categoria": "informatica"},
    "monitor": {"precio": 200, "stock": 20, "categoria": "informatica"},
    "silla": {"precio": 150, "stock": 10, "categoria": "mobiliario"},
    "mesa": {"precio": 300, "stock": 5, "categoria": "mobiliario"}
}

# a)
def valor_total_inventario(productos):
    total = 0
    for prod in productos.values():
        total += prod["precio"] * prod["stock"]
    return total
print(f"a) El valor total del inventario es: {valor_total_inventario(productos)} €")
# b)
def productos_por_categoria(productos, categoria):
    dicc = {}
    for nombre, datos in productos.items():
        if datos["categoria"] == categoria:
            dicc[nombre] = datos
    return dicc
print (f"b) Informática {productos_por_categoria(productos, "informatica").keys()}")
# c)
productos_bajo_stock = {k: v["stock"] for k, v in productos.items() if v["stock"] < 20}
print(f"c) Bajo stock: {productos_bajo_stock}")
# d) 
def actualizar_precios(productos, porcentaje):
    caros = []
    multiplicador = 1 + (porcentaje / 100)
    for nombre, datos in productos.items():
        datos["precio"] = round(datos["precio"] * multiplicador, 2)

        if datos["precio"] > 200:
            caros.append(nombre)
    return caros
caros = actualizar_precios(productos, 10)
print(f"d) Productos que superan 200€ tras subida: {caros}")