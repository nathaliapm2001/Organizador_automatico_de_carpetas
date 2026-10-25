"""
Organizador de carpetas
"""

# importacion de las librerias
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import os
import sys

# variable de la consola de rich
console = Console()




# Funcion con los paneles, estilos del titulo del programa
def mostrar_cabecera() :
          
    console.print(Panel.fit(f"[deep_pink4] {"Organizador automático de carpetas"}[/deep_pink4]"))

# Funcion con la peticion de las rutas de las carpetas
def peticion_rutas(consola) :

    ruta_origen = Prompt.ask("[cyan]Introduce la carpeta de origen[/cyan]",console=consola)

    ruta_destino = Prompt.ask("[cyan]Introduce la carpeta de destino[/cyan]",console=consola)

    # Comprueba si corresponde a una carpeta existente
    if os.path.isdir(ruta_origen):
        consola.print("La carpeta existe")
    else:
        consola.print(Panel.fit("La carpeta no existe o no es una carpeta", border_style="red"))

    #comprueba si existe algo en esa ruta y comprueba si existe esa carpeta
    if os.path.exists(ruta_destino) and not os.path.isdir(ruta_destino):
        consola.print(Panel.fit("Ruta invalida", border_style="red"))
        sys.exit()

    #llamar funcion de comprobacion de una dentro de otra
    if una_dentro_de_otra(ruta_origen, ruta_destino):
        consola.print(Panel.fit("Origen y destino no pueden ser iguales o estar uno dentro del otro", border_style="red"))

    return ruta_origen, ruta_destino
        
# Funscion obtiene nombre y extension del archivo        
def obtener_extension(nombre_archivo) :

    nombre, extension = os.path.splitext(nombre_archivo)

    if extension == "" : 
        return "sin_extension"

    else :

     #converrtir la extensionn en minuscula
     extension = extension.lower()

     #eliminar el punto de la extension
     extension= extension[1:]

     return extension

#Funcion de conversion de tamaño al mas adecuado
def tamano_legible(tamano_bytes):

    unidades = ["bytes" , "KB", "MB" , "GB"]
    tamano = tamano_bytes
    indice  = 0

    # recorre hasta la unidad mas adecuada
    while tamano >= 1024 and indice < 3 :
        tamano = tamano/1024
        indice +=1

    #devolver tamaño y su unidad
    if indice == 0:
        return f"{tamano} bytes"
    else:
        return f"{tamano:.2f} {unidades[indice]}"

#Funcion comprobar si estan dentro una de otra 
def una_dentro_de_otra(ruta_a, ruta_b):

    #obtiene la ruta absoluta
    ruta_a = os.path.abspath(ruta_a) + os.sep
    ruta_b = os.path.abspath(ruta_b) + os.sep

    #detecta si esta una dentro de otra
    return ruta_a.startswith(ruta_b) or ruta_b.startswith(ruta_a)


