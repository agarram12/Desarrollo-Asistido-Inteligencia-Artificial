import numpy as np

# Datos de sensores: 5 sensores, 7 días de mediciones
# Cada fila es un sensor, cada columna un día
np.random.seed(42)
temperaturas = np.random.uniform(15, 35, size=(5, 7))

# a)
print(f"a) Shape {temperaturas.shape}")
print(f"Media global: {np.mean(temperaturas):.2f}")
print(f"Max: {np.max(temperaturas):.2f}, Min: {np.min(temperaturas):.2f}")
# b)
media_sensores = np.mean(temperaturas, axis=1)
media_dias = np.mean(temperaturas, axis=0)
sensor_mas_caliente = np.argmax(media_sensores)
print(f"b) Sensor más caliente: {sensor_mas_caliente}")

# c)
mask_high = temperaturas > 28
count_ajustes = np.sum(mask_high)
temperaturas[mask_high] = 28
print("d) Primeras 3 filas normalizadas:\n", temp_norm[:3, :])

# d)
t_min = np.min(temperaturas)
t_max = np.max(temperaturas)
temp_norm = (temperaturas - t_min) / (t_max - t_min)

# e)
alertas = np.array([10, 20, 15, 25, 18])
alertas_reshaped = alertas[:, np.newaxis] 
temp_con_alertas = temperaturas + alertas_reshaped
print(f"e) Shape resultante tras broadcasting: {temp_con_alertas.shape}")