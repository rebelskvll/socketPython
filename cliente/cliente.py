import socket
import json

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

diccionario = {
    "cuenta":0,
    "valor":0
}

diccionario["cuenta"] = int(input ("Digite el número de la cuenta: "))
diccionario["valor"] = int(input ("Digite el valor: "))
serializado = json.dumps(diccionario).encode('utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(serializado)
    data = s.recv(1024)
print(data.decode("utf-8"))