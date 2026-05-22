# Sulay-Chacha-PRACTICA-PYTHON
EJERCIOS DE INSTITUTO
# ENTREGA:
#   - Nombre del archivo: 05_tarea_{TUAPELLIDO}.py
#   - Plataforma: Moodle (aula virtual)
# ============================================================

import sys
import socket
import datetime  # <-- módulo nuevo que debes investigar

# --- Bienvenida ---
print("=" * 50)
print("   HOLA, RED SEGURA — VERSIÓN CON FECHA Y HORA")
print("=" * 50)

nombre = input("¿Cuál es tu nombre, analista? ")

# --- Obtener fecha y hora actual ---
# PISTA: datetime.datetime.now() te devuelve la fecha y hora
ahora = datetime.datetime.now()

# --- Formatear la fecha de forma legible ---
# PISTA: investiga el método .strftime("%d/%m/%Y %H:%M:%S")
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")  # <-- COMPLETAR si quieres otro formato

# --- Información del sistema ---
version_python = sys.version.split()[0]
nombre_host = socket.gethostname()

try:
    ip_local = socket.gethostbyname(nombre_host)
except socket.gaierror:
    ip_local = "127.0.0.1"

# --- Salida con fecha y hora ---
print(f"\nHola, {nombre}!")
print(f"Sesión iniciada el: {fecha_formateada}")
print(f"Python {version_python} en {nombre_host} ({ip_local})")
print("\n¡Listo para automatizar la red!")

# ============================================================
# DESAFÍO OPCIONAL (+1 punto extra):
#   Agrega una línea que calcule y muestre cuántos días faltan
#   para el fin del ciclo académico 2026-1 (30 de agosto de 2026).
#   Pista: resta dos objetos datetime y usa el atributo .days
# ============================================================
