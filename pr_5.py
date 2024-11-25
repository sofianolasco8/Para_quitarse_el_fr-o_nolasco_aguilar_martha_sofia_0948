print("nolasco_aguilar_martha_sofia_0948_3W")
def binario_a_entero(binario):
    try:
        # Convierte la cadena binaria a entero usando int(base=2)
        return int(binario, 2)
    except ValueError:
        # Marca errores si la cadena no es un número binario válido
        return " Entrada no válida. Asegúrate de ingresar solo 0s y 1s."

# indica al usuario que ingrese un número binario
binario_usuario = input(" ingresa un número binario: ")

# Convierte el binario a entero y mostrar el resultado
resultado = binario_a_entero(binario_usuario)
print(f"El número entero es: {resultado}")#imprime el resultado
