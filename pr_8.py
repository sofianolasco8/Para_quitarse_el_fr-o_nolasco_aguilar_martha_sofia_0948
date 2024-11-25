print("nolasco_aguilar_martha_sofia_0948_3W")
# Definir una lista de nombres
nombres = ["Ana", "Carlos", "Andrés", "Beatriz", "Alberto", "Carmen", "Amalia"]

# indicar al usuario que elija una letra
letra = input("Ingresa la letra para buscar nombres que comiencen con ella: ").lower()

# Contar cuántos nombres comienzan con la letra elegida
cantidad = sum(1 for nombre in nombres if nombre.lower().startswith(letra))

# Imprimir el resultado
print(f" nombres que comienzan con la letra '{letra}': {cantidad}")
