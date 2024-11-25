print("nolasco_aguilar_martha_sofia_0948_3W")
# Define una tupla con 10 edades
edades = (15, 22, 34, 19, 45, 23, 18, 30, 21, 50)

# Contar cuántas edades son mayores a 20
edades_mayores_20 = sum(1 for edad in edades if edad > 20)

# mostrar el resultado
print(f"Cantidad de personas con edades mayor a 20: {edades_mayores_20}")

# indicar al usuario que ingrese las edades
edades = tuple(int(input(f"Ingresa la edad de la persona {i + 1}: ")) for i in range(10))

# Contar cuantas edades son mayores a 20
edades_mayores_20 = sum(1 for edad in edades if edad > 20)

# Imprimir el resultado
print(f"personas con edades mayor a 20: {edades_mayores_20}")
