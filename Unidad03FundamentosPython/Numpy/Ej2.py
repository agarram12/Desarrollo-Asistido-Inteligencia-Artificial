def analizar_texto(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    
    palabra_mas_larga = ""
    for p in palabras:
        if len(p) > len(palabra_mas_larga):
            palabra_mas_larga = p
            
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto.lower():
        if letra in vocales:
            vocales[letra] += 1
            
    top_3 = sorted(palabras, key=len, reverse=True)[:3]

    print(f"Número de palabras: {total_palabras}")
    print(f"Palabra más larga: {palabra_mas_larga} ({len(palabra_mas_larga)} caracteres)")
    
    vocales_fmt = ", ".join([f"{k}={v}" for k, v in vocales.items()])
    print(f"Vocales: {vocales_fmt}")
    
    print(f"Top 3 palabras más largas: {', '.join(top_3)}")

texto_ejemplo = "Python es un lenguaje de programación increíble para ciencia de datos"
analizar_texto(texto_ejemplo)