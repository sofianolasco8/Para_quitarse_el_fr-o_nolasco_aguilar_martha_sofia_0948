print("nolasco_aguilar_martha_sofia_0948_3W")
def max_in_list(numbers):#abre la funcion
    if not numbers:  # revisa si la lista está vacía
        return None  # Devuelve None si no hay elementos en la lista
    max_num = numbers[0]  # define que el primer número es el mayor inicialmente
    for num in numbers:  # Recorre todos los números de la lista
        if num > max_num:  # Compara con el máximo actual
            max_num = num  # Actualiza el máximo si se encuentra un número mayor
    return max_num  # Devolver el número más grande

lista = [4, 5, 6, 7, 8]#le da valor a la funcion
resultado = max_in_list(lista)#indica que se debe mostrar el mayor
print(f"El número más grande es: {resultado}")#muestra el resultado
