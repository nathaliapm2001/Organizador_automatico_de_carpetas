from rich.console import Console
from organizadorCarpetas import tamano_legible

# PROGRAMA PRUEBAS TAMANO_LEGIBLE
if __name__ == "__main__":

    console = Console()

    # Pruebas de la función tamano_legible
    console.print(tamano_legible(500))
    console.print(tamano_legible(1024))
    console.print(tamano_legible(2048576))
    console.print(tamano_legible(5073741824))