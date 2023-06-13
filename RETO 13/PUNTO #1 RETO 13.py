def todos_valores_mismo_tipo(diccionario):
    tipos = {type(valor) for valor in diccionario.values()}  # Crea un conjunto con los tipos únicos de los valores del diccionario
    return len(tipos) == 1  # Devuelve True si todos los valores son del mismo tipo, False de lo contrario

def convertir_valor(valor):
    if isinstance(valor, str):  # Comprueba si el valor es una cadena (str)
        return valor  # Devuelve el valor sin cambios
    else:
        return str(valor)  # Convierte el valor a una cadena y lo devuelve

n = int(input("¿Cuántos elementos tiene tu diccionario? "))  # Solicita al usuario el número de elementos del diccionario
diccionario = {}  # Crea un diccionario vacío

for i in range(n):
    clave = input(f"Ingresa la clave {i+1}: ")  # Solicita al usuario ingresar la clave
    valor = input(f"Ingresa el valor para la clave {clave}: ")  # Solicita al usuario ingresar el valor correspondiente a la clave
    diccionario[clave] = valor  # Agrega la clave y el valor al diccionario

print("Tu diccionario es: ")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")  # Imprime cada clave y valor del diccionario

if todos_valores_mismo_tipo(diccionario):  # Verifica si todos los valores del diccionario son del mismo tipo
    valores_ordenados = sorted(diccionario.values(), key=convertir_valor)
    print("Los valores ordenados de manera ascendente son:")
    for valor in valores_ordenados:
        print(valor)  # Imprime cada valor ordenado
else:
    print("No se pueden ordenar los valores porque no son todos del mismo tipo.")