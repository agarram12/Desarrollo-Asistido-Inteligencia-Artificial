texto = "Python es un lenguaje de programación increíble para ciencia de datos"

palabras = texto.split()

num_palabras = len(palabras)

palabra_larga = max(palabras, key=len)

vocales = "aeiou"
contador_vocales = {v: 0 for v in "aeiou"}

for letra in texto.lower():
    if letra in "a":
        contador_vocales["a"] += 1
    elif letra in "e":
        contador_vocales["e"] += 1
    elif letra in "i":
        contador_vocales["i"] += 1
    elif letra in "o":
        contador_vocales["o"] += 1
    elif letra in "u":
        contador_vocales["u"] += 1

top3 = sorted(set(palabras), key=len, reverse=True)[:3]

print(f"Número de palabras: {num_palabras}")
print(f"Palabra más larga: {palabra_larga} ({len(palabra_larga)} caracteres)")
print(f"Vocales: a= {contador_vocales['a']}, e= {contador_vocales['e']}, i= {contador_vocales['i']}, o= {contador_vocales['o']}, u= {contador_vocales['u']}")
print("Top 3 palabras más largas:", ", ".join(top3))
