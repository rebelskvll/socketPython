import socket
import json

diccionario = {
    "llave1":"Hola",
    "llave2":"Adiós"
}

HOST = "192.168.0.3"  # The server's hostname or IP address
PORT = 2040  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    b = json.dumps(diccionario).encode('utf-8')
    s.sendall(b)
    data = s.recv(1024)