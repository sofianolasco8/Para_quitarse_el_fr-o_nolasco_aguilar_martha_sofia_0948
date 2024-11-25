print("nolasco_aguilar_martha_sofia_0948_3W")
def contar_mayusculas(cadena):#abre la funcion
    contador = 0  #cuenta las letras mayuscular
    for caracter in cadena:  
        if caracter.isupper():  # Verifica si el carácter es una letra mayúscula
            contador += 1  #va sumando si es mayuscula
    return contador

# indica al usuario ingresar una palabra 
cadena_usuario = input(" ingresa una palabra: ")

# Calcula y muestra el número de letras mayúsculas
numero_mayusculas = contar_mayusculas(cadena_usuario)
print(f"La palabra contiene {numero_mayusculas} de letras mayúsculas.")


