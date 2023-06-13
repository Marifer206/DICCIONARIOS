# :star: DICCIONARIOS :star:
## Un dia nuevo, un nuevo reto
REALIZANDO NUESTRO RETO #11

## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+ Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/T2VDNtkq/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2
+ Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
    
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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


```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/B62SmwBr/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #3  
+ Dado el JSON:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Daz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
 Cree un programa que lea de un archivo con dicho JSON y: 
 - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
 - Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

# Ejecuta la función main() 
if __name__ == "__main__":
    main()

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #4 
+ El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:

```python
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```

Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' ([aquí](https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date) pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby


```

  
### :round_pushpin: PUNTO #5
+ A través de un programa conectese a al menos 3 [API's ](https://apipheny.io/free-api/), obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
#5. Reto_13
import requests

# Función para obtener el JSON de una API y mostrar los pares de llave-valor
def obtener_datos(api_url):
    response = requests.get(api_url)
    json_data = response.json()
    
    # Imprimir el JSON completo
    print("JSON:")
    print(json_data)
    print()
    
    # Extraer y mostrar los pares de llave-valor
    print("Pares de llave-valor:")
    for key, value in json_data.items():
        print(f"Llave: {key}, Valor: {value}")
    print()

# Ejemplo 
obtener_datos("https://api.coindesk.com/v1/bpi/currentprice.json")
obtener_datos("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
obtener_datos("https://api.publicapis.org/entries")
```


## :sparkles: Esto es todo por hoy amigos :blush:, y creo que hemos llegado al final de los retos :sparkles: 
