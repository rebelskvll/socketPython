#!/usr/bin/python3

"""
- https://realpython.com/python-sockets/
- https://itecnote.com/tecnote/python-how-to-send-the-content-of-a-dictionary-properly-over-sockets-in-python3x/
- https://docs.python.org/es/3/howto/sockets.html
"""

# Módulo para el manejo de sockets
import socket
import json

# Se define la dirección IP y el puerto en escucha
HOST = "192.168.0.120"
PORT = 65432

# Función para añadir el registro al archivo txt
def crearArchivo(diccionario):

    operacion = ""
    
    try:
        with open ('./registro.txt', 'a') as file:
            file.write(diccionario["cuenta"] + "," + diccionario["valor"] + "\n")
        operacion = "OK"
    except:
        operacion = "NO OK"
    finally:
        return operacion

while True: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Cliente conectado")
            while 1:
                datos = conn.recv(1024)
                if not datos:
                    break
                deserializado = json.loads(datos.decode('utf-8'))
                respuesta = crearArchivo(deserializado)
                conn.sendall(str.encode(respuesta))
        s.close()
            