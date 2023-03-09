import requests
import json

# Se ingresa el monto por linea de comando
monto = input('Ingresa el monto a convertir: ')

# Si el valor tiene decimales, debe ser con '.'
if "," in monto:
    exit("Error: no utilizar ',' en el monto para especificar decimales. Utilizar '.'")
else:
    pass

# Se elige la moneda por linea de comando
moneda = input('Selecciona la moneda [ARS o EUR]: ')

# Controla que la moneda ingresada sea solo ARS o EUR. Ahora tambien acepta minusculas.
match moneda:
    case "ARS"|"EUR":
        pass
    case "ars"|"eur":
        moneda = moneda.upper()
    case other:
        exit("La moneda seleccionada no es correcta, solo acepta ARS o EUR por el momento.")

# Se guarda la API Key, los parametros y la URL de Currency API para obtener las cotizaciones
api_key = "33c0924ef4c5256e1341fc05eb4e96d701f7ea03"
parameters = {"api_key": api_key, "format": "application/json", "from": "USD", "to": moneda, "amount": monto}
url = "https://api.getgeoapi.com/v2/currency/convert"

# Ejecuta la llamada API
response = requests.get(url, parameters)

# Convierte el archivo a JSON para filtrar los campos
convertion = json.loads(response.text)
valor = convertion["rates"][moneda]["rate"]
monto_convertido = convertion["rates"][moneda]["rate_for_amount"]

# Imprime en pantalla los valores
print(f'El valor del USD es: {moneda} {valor}')
print(f'El valor final de la conversion es: {moneda} {monto_convertido}')

