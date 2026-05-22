# =========================================
# TAREA SEMANA 3 - PROGRAMACIÓN EN PYTHON
# =========================================
# -----------------------------------------
# EJERCICIO 1: Protocolo seguro o inseguro
# -----------------------------------------
protocolo = "HTTPS"

if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
    print(f"El protocolo {protocolo} es SEGURO")
elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
    print(f"El protocolo {protocolo} es INSEGURO")
else:
    print("Desconocido")

# -----------------------------------------
# EJERCICIO 2: Servicio según puerto
# -----------------------------------------
puerto = 443

if puerto == 22:
    servicio = "SSH"
elif puerto == 80:
    servicio = "HTTP"
elif puerto == 443:
    servicio = "HTTPS"
elif puerto == 3306:
    servicio = "MySQL"
elif puerto == 3389:
    servicio = "RDP"
else:
    servicio = "Servicio desconocido"

print(f"Puerto {puerto}: {servicio}")

# -----------------------------------------
# EJERCICIO 3: IPs de subred /29
# -----------------------------------------
print("\nIPs de la subred 192.168.1.0/29:")
for i in range(8):
    print(f"192.168.1.{i}")

# -----------------------------------------
# EJERCICIO 4: Inventario con enumerate
# -----------------------------------------
print("\nInventario de dispositivos:")

dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]

for posicion, valor in enumerate(dispositivos, start=1):
    print(f"{posicion}. {valor}")

# -----------------------------------------
# EJERCICIO 5: Cuenta regresiva while
# -----------------------------------------
print("\nCuenta regresiva:")

contador = 5

while contador >= 1:
    print(f"Apagado en: {contador}")
    contador -= 1

print("Apagando servidor...")

# -----------------------------------------
# EJERCICIO 6: Reintento de conexión
# -----------------------------------------
print("\nReintento de conexión:")

intento = 1
conectado = False

while intento <= 5 and not conectado:
    if intento == 1:
        print("Intento 1: sin respuesta")
    elif intento == 2:
        print("Intento 2: sin respuesta")
    elif intento == 3:
        print("Intento 3: CONECTADO")
        conectado = True
    else:
        print(f"Intento {intento}: sin respuesta")

    intento += 1

# -----------------------------------------
# EJERCICIO 7: Primer puerto cerrado
# -----------------------------------------
print("\nPuertos:")

puertos = [21, 22, 23, 25, 80]
estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

for puerto, estado in zip(puertos, estados):
    if estado == "cerrado":
        print(f"Primer puerto cerrado: {puerto}")
        break
    else:
        print(f"Puerto {puerto}: {estado}")

# -----------------------------------------
# EJERCICIO 8: Lista negra de IPs
# -----------------------------------------
print("\nFiltrado de IPs:")

ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
blacklist = ["200.0.0.1", "45.33.32.156"]

total = 0

for ip in ips_log:
    if ip in blacklist:
        continue

    print(f"Procesando: {ip}")
    total += 1

print(f"Total procesadas: {total}")

# -----------------------------------------
# EJERCICIO 9: Buscar en inventario (for-else)
# -----------------------------------------
print("\nBúsqueda en inventario:")

inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]
buscar = "Firewall-FW1"

for d in inventario:
    if d == buscar:
        print(f'buscar = "{buscar}" -> Encontrado')
        break
else:
    print("No encontrado en el inventario")

# -----------------------------------------
# EJERCICIO 10: Validador IPv4
# -----------------------------------------
print("\nValidación de IPv4:")

ips = ["192.168.1.1", "10.0.0.255", "256.1.1.1", "192.168.1", "192.168.a.1"]

for ip in ips:
    partes = ip.split(".")
    valida = True

    if len(partes) != 4:
        valida = False
    else:
        for octeto in partes:
            if not octeto.isdigit():
                valida = False
                break
            if int(octeto) < 0 or int(octeto) > 255:
                valida = False
                break

    if valida:
        print(f"{ip} -> Valida")
    else:
        print(f"{ip} -> Invalida")