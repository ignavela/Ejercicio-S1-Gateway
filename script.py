import requests
import json

# Se ingresa el monto por linea de comando
monto = input('Ingresa el monto: ')
# Se elige la moneda por linea de comando
moneda = input('Selecciona la moneda [ARS o EUR]: ')

# Se guarda la API Key, los parametros y la URL de Currency API para obtener las cotizaciones
api_key = "33c0924ef4c5256e1341fc05eb4e96d701f7ea03"
parameters = {"api_key": api_key, "format": "application/json", "from": "USD", "to": moneda, "amount": monto}
url = "https://api.getgeoapi.com/v2/currency/convert"
# EJecuta la llamada API
response = requests.get(url, parameters)
# Convierte el archivo a JSON para filtrar los campos
convertion = json.loads(response.text)
valor = convertion["rates"][moneda]["rate"]
monto_convertido = convertion["rates"][moneda]["rate_for_amount"]

print(f'El valor del USD es: {moneda} {valor}')
print(f'El valor final de la conversion es: {moneda} {monto_convertido}')

