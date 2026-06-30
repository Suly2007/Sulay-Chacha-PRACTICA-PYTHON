import csv

inventario = []


def mostrar_menu():
    print("\n===== INVENTARIO DE RED =====")
    print("1. Agregar dispositivo")
    print("2. Importar desde CSV")
    print("3. Mostrar reporte")
    print("4. Total de dispositivos")
    print("5. Salir")

###AGREGAR DISPOSITIVO#####

def agregar_dispositivo(nombre, tipo, ip):

    if validar_ip(ip):

        dispositivo = {
            "nombre": nombre,
            "tipo": tipo,
            "ip": ip,
            "clase": tipo_ip(ip)
        }

        inventario.append(dispositivo)

        print("Dispositivo agregado correctamente.")

    else:
        print("La dirección IP no es válida.")

###TOTAL DE DISPOSITIVOS#####


def total_dispositivos():
    return len(inventario)

###VALIDACION DE IP #####

def validar_ip(ip):

    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for numero in partes:

        if not numero.isdigit():
            return False

        numero = int(numero)

        if numero < 0 or numero > 255:
            return False

    return True


###SI ES IP PUBLICA O PRIVADA#####


def tipo_ip(ip):

    partes = ip.split(".")

    primero = int(partes[0])
    segundo = int(partes[1])

    if primero == 10:
        return "Privada"

    elif primero == 172 and 16 <= segundo <= 31:
        return "Privada"

    elif primero == 192 and segundo == 168:
        return "Privada"

    else:
        return "Pública"
    
###UTILIZAR EL ARCHIVO CSV ####    
    
def importar_csv():

    print("Intentando abrir el archivo...")

    try:

        with open("dispositivos.csv", "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            for fila in lector:

                print("Fila leída:", fila)

                agregar_dispositivo(fila[1], fila[2], fila[0])

        print("Archivo importado correctamente.")

    except Exception as e:
        print("ERROR:", e)

#### MOSTRAR EL REPORTE DE LOS DISPOSITIVOS ######
def mostrar_reporte():

    if len(inventario) == 0:
        print("No existen dispositivos.")
        return

    print("\n====== REPORTE ======")

    for dispositivo in inventario:

        print("------------------------")
        print("Nombre :", dispositivo["nombre"])
        print("Tipo   :", dispositivo["tipo"])
        print("IP     :", dispositivo["ip"])
        print("Clase  :", dispositivo["clase"])

###FUNCION LAMBDA #####

obtener_nombre = lambda dispositivo: dispositivo["nombre"]


#### EJECUCION DEL MENU ####
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        ip = input("Dirección IP: ")

        agregar_dispositivo(nombre, tipo, ip)

    elif opcion == "2":

        importar_csv()

    elif opcion == "3":

        mostrar_reporte()

    elif opcion == "4":

        print("Total de dispositivos:", total_dispositivos())

    elif opcion == "5":

        print("Programa finalizado.")
        break

    else:

        print("Opción incorrecta.")

