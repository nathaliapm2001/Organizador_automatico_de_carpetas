"""
Organizador de carpetas 

Este programa permite organizar automáticamente los archivos de una carpeta según su extensión, 
utilizando programación modular y recursividad.

El programa recorre la carpeta de origen y todas sus subcarpetas, clasifica los archivos y los 
mueve a una carpeta de destino, creando automáticamente las subcarpetas necesarias.

Al finalizar, genera un informe visual en consola mediante la librería Rich, mostrando los archivos 
movidos, el espacio ocupado y el historial de movimientos.
"""

# importacion de las librerias
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import os
import sys
import shutil
from rich.table import Table

# variable de la consola de rich
console = Console()


# FUNCIONES
# Funcion con los paneles, estilos del titulo del programa
def mostrar_cabecera(consola):

    consola.print(
        Panel.fit(f"[deep_pink4] {"Organizador automático de carpetas"}[/deep_pink4]"))

# Funcion con la peticion de las rutas de las carpetas


def peticion_rutas(consola):

    ruta_origen = Prompt.ask(
        "[cyan]Introduce la carpeta de origen[/cyan]", console=consola)

    ruta_destino = Prompt.ask(
        "[cyan]Introduce la carpeta de destino[/cyan]", console=consola)

    # Comprueba si corresponde a una carpeta existente
    if os.path.isdir(ruta_origen):
        consola.print("La carpeta origen existe")
    else:
        consola.print(
            Panel.fit("La carpeta no existe o no es una carpeta", border_style="red"))
        sys.exit()

    # comprueba si existe algo en esa ruta y comprueba si existe esa carpeta
    if os.path.exists(ruta_destino) and not os.path.isdir(ruta_destino):
        consola.print(Panel.fit("Ruta invalida", border_style="red"))
        sys.exit()

    # llamar funcion de comprobacion de una dentro de otra
    if una_dentro_de_otra(ruta_origen, ruta_destino):
        consola.print(Panel.fit(
            "Origen y destino no pueden ser iguales o estar uno dentro del otro", border_style="red"))

    return ruta_origen, ruta_destino

# Funscion obtiene nombre y extension del archivo


def obtener_extension(nombre_archivo):

    nombre, extension = os.path.splitext(nombre_archivo)

    if extension == "":
        return "sin_extension"

    else:

        # converrtir la extensionn en minuscula
        extension = extension.lower()

        # eliminar el punto de la extension
        extension = extension[1:]

        return extension

# Funcion de conversion de tamaño al mas adecuado


def tamano_legible(tamano_bytes):

    unidades = ["bytes", "KB", "MB", "GB"]
    tamano = tamano_bytes
    indice = 0

    # recorre hasta la unidad mas adecuada
    while tamano >= 1024 and indice < 3:
        tamano = tamano/1024
        indice += 1

    # devolver tamaño y su unidad
    if indice == 0:
        return str(tamano) + " bytes"
    else:
        return str(format(tamano, ".2f")) + " " + unidades[indice]

# Funcion comprobar si estan dentro una de otra


def una_dentro_de_otra(ruta_a, ruta_b):

    # obtiene la ruta absoluta
    ruta_a = os.path.abspath(ruta_a) + os.sep
    ruta_b = os.path.abspath(ruta_b) + os.sep

    # detecta si esta una dentro de otra
    return ruta_a.startswith(ruta_b) or ruta_b.startswith(ruta_a)

# Funcion comprobar si el nommbre esta disponible


def nombre_disponible(ruta_destino, nombre_archivo):

    contador = 1

    # Unir la ruta con el nombre del archivo
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    if not os.path.exists(ruta_completa):

        return nombre_archivo

    # Separar el nombre de la extensión
    nombre, extension = os.path.splitext(nombre_archivo)

    # Crear el primer nombre alternativo
    nuevo_nombre = nombre + "_" + str(contador) + extension
    ruta_nueva = os.path.join(ruta_destino, nuevo_nombre)

    # comprueba hasta crear uno diferente
    while os.path.exists(ruta_nueva):

        contador += 1

        nuevo_nombre = nombre + "_" + str(contador) + extension

        ruta_nueva = os.path.join(ruta_destino, nuevo_nombre)

    return nuevo_nombre

# Funcion donde mueve los archivos donde pertenecen


def clasificar_archivo(ruta_origen, nombre_archivo, ruta_destino, historial):

    # obtener extension
    extension = obtener_extension(nombre_archivo)

    # crear carpeta con la extension corresponda
    carpeta_extension = os.path.join(ruta_destino, extension)
    os.makedirs(carpeta_extension, exist_ok=True)

    # buscar nombre libre
    nombre_libre = nombre_disponible(carpeta_extension, nombre_archivo)

    # construir rutas completas
    archivo_origen = os.path.join(ruta_origen, nombre_archivo)
    archivo_destino = os.path.join(carpeta_extension, nombre_libre)

    # obtener el tamaño del archivo
    tamano = os.path.getsize(archivo_origen)

    # Mueve ele archivo
    shutil.move(archivo_origen, archivo_destino)

    # Guardar en el historial
    historial.append(archivo_origen + " -> " + archivo_destino)

    return tamano

# Funcion recursiva de movimiento de archivo


def clasificar_carpeta_recursivo(ruta_origen, ruta_destino, historial):

    total_bytes = 0

    # recorrer los elementos dentro el origen
    for elemento in os.listdir(ruta_origen):

        ruta_completa = os.path.join(ruta_origen, elemento)

        # comprobar si es una carpeta
        if os.path.isdir(ruta_completa):

            bytes_subcarpetas = clasificar_carpeta_recursivo(
                ruta_completa, ruta_destino, historial)

            total_bytes += bytes_subcarpetas

        else:

            bytes_archivo = clasificar_archivo(
                ruta_origen, elemento, ruta_destino, historial)

            total_bytes += bytes_archivo

    return total_bytes

# Funcion recursiva coontador de archivos


def contar_archivos_recursivo(ruta):

    total_archivos = 0

    if not os.path.isdir(ruta):
        return 0

        # recorrer los elementos dentro de la carpeta
    for elemento in os.listdir(ruta):

        ruta_completa = os.path.join(ruta, elemento)

        # entrar en subcarpetas
        if os.path.isdir(ruta_completa):

            total_archivos += contar_archivos_recursivo(ruta_completa)

        elif os.path.isfile(ruta_completa):

            total_archivos += 1

    return total_archivos

# Función para mostrar el informe final


def mostrar_informe(consola, movidos, tamano_total, en_origen, en_destino, historial):

    # crear tabla
    tabla = Table(title=" Informe final ")

    # columnas
    tabla.add_column("Concepto", style="cyan")
    tabla.add_column("Valor", justify="center", style="deep_pink4")

    # añadir resultados
    tabla.add_row("Archivos movidos", str(movidos))
    tabla.add_row("Tamaño total movido", tamano_legible(tamano_total))

    # comprobar si quedan archvios en el origeen
    if en_origen == 0:
        restantes = "[green]" + str(en_origen) + "[/green]"
    else:
        restantes = "[red]" + str(en_origen) + "[/red]"

    tabla.add_row("Archivos restantes en origen", restantes)
    tabla.add_row("Archivos en destino", str(en_destino))

    # mostrar primera tabla
    consola.print(tabla)

    # crear segunda tabla
    tabla_movimientos = Table(title="Movimientos realizados")

    tabla_movimientos.add_column("Numero", justify="right", style="deep_pink4")
    tabla_movimientos.add_column("Origen -> Destino")

    contador = 1

    for movimiento in historial:
        tabla_movimientos.add_row(str(contador), movimiento)
        contador += 1

    # mostrar segunda tabla
    consola.print(tabla_movimientos)


# PROGRAMA PRINCIPAL
# variable del historial
historial = []


mostrar_cabecera(console)

ruta_origen, ruta_destino = peticion_rutas(console)

tamano_total = clasificar_carpeta_recursivo(
    ruta_origen, ruta_destino, historial)

# contar los archivos movidos
movidos = len(historial)

en_origen = contar_archivos_recursivo(ruta_origen)

en_destino = contar_archivos_recursivo(ruta_destino)

mostrar_informe(console, movidos, tamano_total,
                en_origen, en_destino, historial)
