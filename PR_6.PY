print("nolasco_aguilar_martha_sofia_0948_3W")
# indicar al usuario que ingrese  el año en curso
año_actual = int(input("Ingresa el año en curso: "))

# se abre una lista para almacenar los datos de las personas
personas = []

# indicar al usuario que ingrese los datos de las tres personas
for i in range(1, 4):
    nombre = input(f"Ingresa el primer nombre  {i}: ")
    año_nacimiento = int(input(f"Ingresa el año de nacimiento de {nombre}: "))
    personas.append((nombre, año_nacimiento))

print("\nResultados:")
# Calcula y muestra la edad que cumplirán durante el año en curso
for nombre, anio_nacimiento in personas:
    edad = año_actual - anio_nacimiento
    print(f"{nombre} cumplirá {edad} años en el año {año_actual}.")
