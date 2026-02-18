import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (10, 6)

print("Cargar el Dataset")
try:
    df = pd.read_csv('dataset.csv')
    print("El dataset se ha cargado.")
except FileNotFoundError:
    print("El archivo dataset.csv no existe.")

# Limpieza de datos
print("Limpieza de datos")
# Información y tipos
df.info()

# Identificar nulos y detectar duplicados
print(f"Cantidad de nulos totales: {df.isnull().sum().sum()}")
print(f"Duplicados: {df.duplicated().sum()}")

# Normalizar a mayúsculas
df['plataforma'] = df['plataforma'].str.upper()

# Análisis estadístico
print(f"Análisis estadístico")

# Estadisticas por horas y puntuaciones
print(f"Estadísticas:")
print(df[['horas_jugadas', 'puntuacion']].describe())

print(f"Top géneros por puntuación Media:")
print(df.groupby('genero')['puntuacion'].mean().sort_values(ascending=False))
# Correlación de las horas frente a la puntuación

corr = df['horas_jugadas'].corr(df['puntuacion'])
print(f"Correlación de horas y puntos: {corr:.2f}")

# Visualizar con matplotlib
print("Generación de gráficos")

# Juegos por cada plataforma
plt.figure()
conteo = df['plataforma'].value_counts()
categorias = conteo.index
valores = conteo.values

plt.bar(categorias, valores, color='skyblue', edgecolor='black')
plt.title('Cantidad de Juegos por Plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('grafico_1_barras.png')
plt.show()

# Gráfico de horas jugadas
plt.figure()
plt.hist(df['horas_jugadas'], bins=10, color='purple', alpha=0.7, edgecolor='black')
plt.axvline(df['horas_jugadas'].mean(), color='red', linestyle='dashed', linewidth=1, label='Media')
plt.title('Distribución de Horas Jugadas')
plt.xlabel('Horas')
plt.ylabel('Frecuencia')
plt.legend()
plt.savefig('grafico_2_hist.png')
plt.show()

# Gráfico de horas frente a la puntuación

plt.figure()
groups = df.groupby('completado')
for name, group in groups:
    plt.scatter(group['horas_jugadas'], group['puntuacion'], marker='o', linestyle='', label=f'Completado: {name}', s=100, alpha=0.8)
plt.title('Relación: Horas Jugadas vs Puntuación')
plt.xlabel('Horas Jugadas')
plt.ylabel('Puntuación (0-10)')
plt.legend()
plt.grid(True)
plt.savefig('grafico_3_scatter.png')
plt.show()

# Puntuaciones por plataforma
plt.figure()
df.boxplot(column='puntuacion', by='plataforma', grid=True, patch_artist=True)
plt.title('Distribución de Puntuaciones por Plataforma')
plt.suptitle('')
plt.xlabel('Plataforma')
plt.ylabel('Puntuación')
plt.savefig('grafico_4_boxplot.png')
plt.show()

print("\nAnálisis finalizado.")



# Ver qué generos son los que mas he jugado
print(df['genero'].value_counts())
print(df.groupby('genero')['puntuacion'].mean().sort_values(ascending=False))