#!/usr/bin/python3

"""
- https://realpython.com/python-sockets/
- https://itecnote.com/tecnote/python-how-to-send-the-content-of-a-dictionary-properly-over-sockets-in-python3x/
- https://docs.python.org/es/3/howto/sockets.html
"""

# Módulo para el manejo de sockets
import socket
import json

HOST = "127.0.0.1"
PORT = 65432

def crearArchivo(diccionario):

    operacion = ""
    
    try:
        with open ('registro.csv', 'a') as file:
            file.write(diccionario["cuenta"] + "," + diccionario["valor"])
        operacion = "OK"
    except:
        operacion = "NO OK"
    finally:
        return operacion



    return operacion

while True: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Cliente {addr[0]} conectado")
            while 1:
                datos = conn.recv(1024)
                if not datos:
                    break
                deserializado = json.loads(datos.decode('utf-8'))
                respuesta = crearArchivo(deserializado)
                conn.sendall(str.encode(respuesta))
            