import matplotlib.pyplot as plt
import pandas as pd

ventas = {
    'producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Webcam', 'Auriculares'],
    'categoria': ['Informática', 'Accesorios', 'Informática', 'Accesorios', 'Accesorios', 'Accesorios'],
    'precio': [800, 20, 200, 45, 60, 35],
    'cantidad': [5, 30, 8, 15, 12, 20]
}

df = pd.DataFrame(ventas)

df['subtotal'] = df['precio'] * df['cantidad']
ventas_categoria = df.groupby('categoria')['subtotal'].sum()
df_ordenado = df.sort_values('subtotal')

fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].bar(ventas_categoria.index, ventas_categoria.values, color=['steelblue', 'orange'])
axs[0].set_title('Total Vendido por Categoría')
axs[0].set_xlabel('Categoría')
axs[0].set_ylabel('Total (€)')
axs[0].tick_params(axis='x', rotation=45)

axs[1].pie(ventas_categoria.values,
           labels=ventas_categoria.index,
           autopct='%1.1f%%',
           colors=['steelblue', 'orange'])
axs[1].set_title('Porcentaje de Ventas')

axs[2].barh(df_ordenado['producto'], df_ordenado['subtotal'], color='seagreen')
axs[2].set_title('Ventas por Producto')
axs[2].set_xlabel('Subtotal (€)')
axs[2].set_ylabel('Producto')

plt.tight_layout()
plt.show()
