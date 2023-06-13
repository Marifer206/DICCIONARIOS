import requests
def obtener_datos(api_url):
    response = requests.get(api_url)
    json_data = response.json()

    print("JSON:")
    print(json_data)
    print()

    print("Pares de llave-valor:")
    for key, value in json_data.items():
        print(f"Llave: {key}, Valor: {value}")
    print()

obtener_datos("https://api.publicapis.org/entries")
obtener_datos("https://catfact.ninja/fact")
obtener_datos("https://api.coindesk.com/v1/bpi/currentprice.json")