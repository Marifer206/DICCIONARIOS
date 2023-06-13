import json

# Función para leer un archivo JSON y devolver su contenido como un objeto de Python
def leer_json(archivo):
    with open(archivo, 'r') as f:
        data = json.load(f)
    return data

# Función para encontrar deportistas que practican un deporte específico
def deportistas_por_deporte(data, deporte):
    resultado = []
    for persona, info in data.items():  # Iterar sobre las personas en el JSON
        if deporte in info['deportes']:  # Si el deporte está en la lista de deportes de la persona
            nombre_completo = f"{info['nombres']} {info['apellidos']}"  # Crear el nombre completo
            resultado.append(nombre_completo)  # Agregar el nombre completo a la lista de resultados
    return resultado

# Función para encontrar deportistas dentro de un rango de edades
def deportistas_por_edad(data, edad_min, edad_max):
    resultado = []
    for persona, info in data.items():  # Iterar sobre las personas en el JSON
        if edad_min <= info['edad'] <= edad_max:  # Si la edad de la persona está dentro del rango especificado
            nombre_completo = f"{info['nombres']} {info['apellidos']}"  # Crear el nombre completo
            resultado.append(nombre_completo)  # Agregar el nombre completo a la lista de resultados
    return resultado

# Función principal que ejecuta el programa
def main():
    archivo = 'datos.json'  # Reemplaza esto con el nombre de tu archivo JSON
    data = leer_json(archivo)  # Leer el archivo JSON

    deporte = input("Ingrese el deporte: ")  # Solicitar el deporte al usuario
    deportistas = deportistas_por_deporte(data, deporte)  # Encontrar deportistas que practican el deporte ingresado
    print(f"Personas que practican {deporte}:")  # Imprimir los resultados
    for deportista in deportistas:
        print(deportista)

    edad_min = int(input("Ingrese la edad mínima: "))  # Solicitar la edad mínima al usuario
    edad_max = int(input("Ingrese la edad máxima: "))  # Solicitar la edad máxima al usuario
    deportistas = deportistas_por_edad(data, edad_min, edad_max)  # Encontrar deportistas dentro del rango de edades ingresado
    print(f"Personas con edades entre {edad_min} y {edad_max}:")  # Imprimir los resultados
    for deportista in deportistas:
        print(deportista)

# Ejecuta la función main() si el script se ejecuta como un programa principal
if __name__ == "__main__":
    main()