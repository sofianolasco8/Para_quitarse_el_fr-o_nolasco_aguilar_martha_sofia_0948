print("nolasco_aguilar_martha_sofia_0948_3W")
def filtr_palabras(palabras, n):#se abre la funcion
    if not palabras:  # Verifica si la lista está vacía
        return []  # Devulve  una lista vacía si no hay palabras
    return [palabra for palabra in palabras if len(palabra) > n]  # muestra palabras con más de n caracteres

lista_palabras = ["sof", "dayana", "bri", "escobedo", "rodri"]#le da valor a la funcion
n = 4 #indica cules son las palabras con mas de 4 letras
resultado = filtr_palabras(lista_palabras, n)#muestra la funcion
print(f"Palabras con más de {n} caracteres: {resultado}")#muestra la funcion
