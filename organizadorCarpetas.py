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




# funcion con los paneles, estilos del titulo del programa
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
        consola.print("La carpeta no existe")

    #comprueba si existe algo en esa ruta y comprueba si existe esa carpeta
    if os.path.exists(ruta_destino) and not os.path.isdir(ruta_destino):
        consola.print(Panel.fit("Ruta invalida", border_style="red"))
        sys.exit()
        
