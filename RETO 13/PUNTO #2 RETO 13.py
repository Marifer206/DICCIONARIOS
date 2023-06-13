# Función para mezclar dos diccionarios
def mezclar_diccionarios(d1, d2):
    nuevo_diccionario = d1.copy()  # Copiar el primer diccionario
    for clave, valor in d2.items():  # Iterar sobre los elementos del segundo diccionario
        if clave not in nuevo_diccionario:  # Si la clave no está en el nuevo diccionario
            nuevo_diccionario[clave] = valor  # Agregar la clave y el valor al nuevo diccionario
    return nuevo_diccionario

# Función para crear un diccionario a partir de la entrada del usuario
def crear_diccionarios(n):
    diccionario = {}  # Crea un diccionario vacío
    for i in range(n):  # Iterar n veces
        clave = input(f"Ingresa la clave {i+1}: ")  # Solicita al usuario ingresar la clave
        valor = input(f"Ingresa el valor para la clave {clave}: ")  # Solicita al usuario ingresar el valor correspondiente a la clave
        diccionario[clave] = valor  # Agrega la clave y el valor al diccionario
    return diccionario

# Función principal que ejecuta el programa
def main():
    n1 = int(input("¿Cuántos elementos tiene el primer diccionario? "))  # Solicita al usuario el número de elementos del primer diccionario
    diccionario1 = crear_diccionarios(n1)  # Crea el primer diccionario

    n2 = int(input("¿Cuántos elementos tiene el segundo diccionario? "))  # Solicita al usuario el número de elementos del segundo diccionario
    diccionario2 = crear_diccionarios(n2)  # Crea el segundo diccionario

    resultado = mezclar_diccionarios(diccionario1, diccionario2)  # Mezcla los dos diccionarios

    # Imprimir los diccionarios originales y el resultado de la mezcla
    print("Primer diccionario:", diccionario1)
    print("Segundo diccionario:", diccionario2)
    print("Resultado de la mezcla:", resultado)

# Ejecuta la función main()
if __name__ == "__main__":
    main()
