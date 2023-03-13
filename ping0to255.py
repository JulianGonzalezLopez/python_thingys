import os
import time


def cargarRango():
    octetos = []
    for x in range(1,4):
        octetos.append(input(f"Ingresa el octeto {x}: "))
    print(f"Se enviaran pings a todas las posibles IP en {octetos[0]}.{octetos[1]}.{octetos[2]}. 0 hasta 255")
    time.sleep(2)
    return octetos

def ping(ip,buenas):
    res = os.popen(f"ping {ip}").read()
    print(res)
    if "inaccesible" and "Tiempo de espera agotado para esta solicitud" not in res:
        if ip not in buenas:
            buenas.append(ip)

def pings(base):
    buenas = []
    buenas.append(f"IP EN RANGO: {base[0]}.{base[1]}.{base[2]}. ...")
    for i in range(0,255):
        print(f"PING {base[0]}.{base[1]}.{base[2]}.{i}")
        res = os.popen(f"ping {base[0]}.{base[1]}.{base[2]}.{i}").read()
        if not ("Host de destino inaccesible" or "Tiempo de espera agotado para esta solicitud") in res:
            if i not in buenas:
                buenas.append(i)
                print("Ok")
    return buenas

def cargarIPArchivo(arr):
    arch = open("datos.txt","w") 
    for ip in arr:
        arch.write(f"{str(ip)}\n")

ips = pings(cargarRango())

cargarIPArchivo(ips)