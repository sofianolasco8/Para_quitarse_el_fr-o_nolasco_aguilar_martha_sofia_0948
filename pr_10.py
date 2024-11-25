print("nolasco_aguilar_martha_sofia_0948_3W")
def es_bisiesto(año):#abrir funcion
    if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        return True
    else:
        return False

# indicar al usuario que ingrese un año
año_usuario = int(input("Ingresa un año: "))

# mostrar el resultado
if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es bisiesto.")
else:
    print(f"El año {año_usuario} no es bisiesto.")
