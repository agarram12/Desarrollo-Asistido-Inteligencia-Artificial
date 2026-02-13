import pandas as pd

ventas = {
    'producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Webcam', 'Auriculares'],
    'categoria': ['Informática', 'Accesorios', 'Informática', 'Accesorios', 'Accesorios', 'Accesorios'],
    'precio': [800, 20, 200, 45, 60, 35],
    'cantidad': [5, 30, 8, 15, 12, 20]
}

df = pd.DataFrame(ventas)

df['subtotal'] = df['precio'] * df['cantidad']

grupo = df.groupby('categoria').agg({
    'subtotal' : 'sum',
    'precio' : 'mean',
    'prodcuto' : 'count'
}).rename(columns={
    'subtotal' : 'total_vendido',
    'precio' : 'precio_medio',
    'producto' : 'cantidad_prodcutos_diferencia'
})

ingresos_max = grupo['total_vendido'].idxmax()
mas_vendido = df.loc[df['cantidad'].idxmax(), 'producto']
