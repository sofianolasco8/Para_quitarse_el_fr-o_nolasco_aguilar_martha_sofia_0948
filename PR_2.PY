print("nolasco_aguilar_martha_sofia_0948_3W")
def mas_larga(palabras):#se abre la funcion 
    if not palabras:  # Verifica si la lista está vacía
        return None  # Devuelve a  None si no hay palabras en la lista
    palabra_mas_larga = palabras[0]  # define que  la primera palabra es la más larga 
    for palabra in palabras:  # Recorre todas las palabras de la lista
        if len(palabra) > len(palabra_mas_larga):  # Compara longitudes
            palabra_mas_larga = palabra  # verifica si se encuentra una palabra más larga
    return palabra_mas_larga  # Devuelve la palabra más larga

lista_palabras = ["sofia", "dayana", "briana", "escobedo"]#valores de la funcion
resultado = mas_larga(lista_palabras)#muestra la palabra mas larga
print(f"La palabra más larga es: {resultado}")#imprime el resultado

