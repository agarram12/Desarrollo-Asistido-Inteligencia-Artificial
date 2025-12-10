# Dada esta lista de precios en euros:
precios_euros = [19.99, 49.99, 12.50, 99.99, 5.00]

# Usa map() para:
# 1. Convertir a dólares (multiplica por 1.1)
# 2. Redondear a 2 decimales con round()
# Imprime la lista resultante

def convertir(precios_euros):
    dolares = precios_euros * 1.1
    return round(dolares, 2)

dolares = map(convertir, precios_euros)
dolares = list(dolares)
print(dolares)