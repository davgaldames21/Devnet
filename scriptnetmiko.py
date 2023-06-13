import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = {
    "ip": "192.168.75.132",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Show command that vamos a ejecutar.
command = "show version"

# Establecer conexión SSH con el enrutador Cisco
with ConnectHandler(**cisco1) as net_connect:
    # Enviar el comando show al enrutador y obtener la salida
    output = net_connect.send_command(command)

# Imprimir la salida obtenida
print()
print(output)
print()