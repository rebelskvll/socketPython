#!/usr/bin/python3

"""
Ejemplos tomados de: 
- https://realpython.com/python-sockets/
- https://itecnote.com/tecnote/python-how-to-send-the-content-of-a-dictionary-properly-over-sockets-in-python3x/
- https://docs.python.org/es/3/howto/sockets.html
"""

# Módulo para el manejo de sockets
import socket
import json

# Puerto por el cual se van a aceptar conexiones
host = "192.168.0.3"
puerto = 2040


# Se hace la creación del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:

    socketServer.bind ((host, puerto))
    socketServer.listen(5)

    conexion = socketServer.accept()

    b = b''


    while 1:
        tmp = conexion.recv(1024)
        b += tmp

    d = json.loads(b.decode('UTF-8'))

    print (d)




def guardarDatos(datos):
    
    pass