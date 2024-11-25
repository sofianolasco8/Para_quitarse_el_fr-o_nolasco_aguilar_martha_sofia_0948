print("nolasco_aguilar_martha_sofia_0948_3W")
def contar_vocales(palabra):#abre una funcion
    # Inicia un diccionario para contar las vocales
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    # Recorrer cada carácter de la palabra
    for letra in palabra.lower():  # Convertir la palabra a minúsculas
        if letra in conteo:  # Si el carácter es una vocal
            conteo[letra] += 1  #  conteo de esa vocal
    
    return conteo

# indicar al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

# obtener el conteo de vocales
resultado = contar_vocales(palabra_usuario)

# mostrar el resultado
print("Conteo de vocales:")
for vocal, cantidad in resultado.items():
    print(f"{vocal}: {cantidad}")
