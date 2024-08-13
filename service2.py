import requests
import json
import time

# Configuración
SERVER_URL = 'http://localhost:5000/logs'
TOKEN = 'token_service2'

# Generar logs y enviarlos al servidor
def enviar_log():
    while True:
        log = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'service_name': 'service2',
            'severity': 'error',
            'message': 'Log generado por el servicio 2'
        }
        headers = {'Authorization': TOKEN}
        response = requests.post(SERVER_URL, json=log, headers=headers)
        print(f"Respuesta del servidor: {response.status_code}")
        time.sleep(10)

if __name__ == "__main__":
    enviar_log()
