"""
Organizador de carpetas
"""

# importacion de las librerias
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import os

# variable de la consola de rich
console = Console()




# funcion con los paneles, estilos del titulo del programa
def mostrar_cabecera() :
          
    console.print(Panel.fit(f"[deep_pink4] {"Organizador automático de carpetas"}[/deep_pink4]"))

