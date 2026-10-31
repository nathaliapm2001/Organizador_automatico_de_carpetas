# 📂 Organizador Automático de Carpetas

Aplicación desarrollada en **Python** que permite organizar automáticamente los archivos de una carpeta según su extensión, utilizando programación modular y recursividad.

El programa recorre la carpeta de origen y todas sus subcarpetas, clasifica los archivos y los mueve a una carpeta de destino, creando automáticamente las subcarpetas necesarias.

Al finalizar, genera un **informe visual en consola** mediante la librería **Rich**, mostrando los archivos movidos, el espacio ocupado y el historial de movimientos.

---

## 👤 Autor

**Nathalia Piñera Molina**

---

## 🛠️ Tecnologías utilizadas

- **Python 3:** lenguaje utilizado para desarrollar la lógica del programa.
- **Rich:** librería para mostrar paneles, colores y tablas en consola.
- **os:** módulo para gestionar rutas, archivos y directorios.
- **shutil:** módulo para mover archivos entre carpetas.
- **Visual Studio Code:** entorno de desarrollo.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

---

## 🎯 Funcionalidades

1. **Solicitud de rutas:** permite introducir las carpetas de origen y destino mediante teclado.

2. **Validación de rutas:** comprueba que las rutas sean válidas y evita utilizar carpetas iguales o anidadas entre sí.

3. **Clasificación automática:** organiza los archivos según su extensión (`jpg`, `pdf`, `txt`, `csv`, `docx`, etc.).

4. **Creación de carpetas:** genera automáticamente las subcarpetas necesarias para cada extensión.

5. **Recursividad:** recorre todas las subcarpetas del origen, independientemente de su profundidad.

6. **Control de archivos duplicados:** evita sobrescribir archivos utilizando nombres alternativos como `notas_1.txt`, `notas_2.txt`, etc.

7. **Archivos sin extensión:** los clasifica dentro de una carpeta llamada `sin_extension`.

8. **Cálculo del espacio ocupado:** convierte los tamaños de bytes a KB, MB o GB, según corresponda.

9. **Historial de movimientos:** registra la ubicación original y final de cada archivo.

10. **Informe final:** presenta los resultados mediante tablas y colores utilizando Rich.

---

## 📁 Estructura del proyecto

```text
Organizador_automatico_de_carpetas/
│
├── carpeta_prueba/              # Archivos y subcarpetas para la clasificación
│   ├── foto.jpg
│   ├── informe.pdf
│   ├── notas.txt
│   ├── LEEME
│   └── trabajos/
│       ├── documentos.docx
│       └── antiguos/
│           ├── datos.csv
│           └── notas.txt
│
├── pruebas/                     # Carpetas para realizar las pruebas
│   └── origen_vacio/            # Prueba 1: carpeta de origen sin archivos
│
├── organizadorCarpetas.py       # Programa principal
├── tamano_legible.py            # Pruebas de conversión de tamaños
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
└── .gitignore                   # Archivos excluidos de Gi
```
Durante el desarrollo y las ejecuciones de prueba también pueden generarse las siguientes carpetas:

.venv/: entorno virtual de Python.

__pycache__/: caché generada automáticamente por Python.

organizados/: carpeta de destino donde se clasifican los archivos.

pruebas/: carpetas auxiliares utilizadas para los casos de prueba.

---

## 🧪 Ejemplo de funcionamiento

### 📥 Antes de ejecutar el programa

Tenemos una carpeta con archivos de diferentes tipos, subcarpetas anidadas y nombres repetidos.

```text
carpeta_prueba/
│
├── foto.jpg
├── informe.pdf
├── notas.txt
├── LEEME
│
└── trabajos/
    │
    ├── documentos.docx
    │
    └── antiguos/
        ├── datos.csv
        └── notas.txt
```

### 📤 Después de ejecutar el programa

El programa organiza automáticamente los archivos según su extensión.

```text
organizados/
│
├── jpg/
│   └── foto.jpg
│
├── pdf/
│   └── informe.pdf
│
├── txt/
│   ├── notas.txt
│   └── notas_1.txt
│
├── docx/
│   └── documentos.docx
│
├── csv/
│   └── datos.csv
│
└── sin_extension/
    └── LEEME
```

### ✅ Resultado

- Los archivos han quedado clasificados por extensión.
- Se ha evitado sobrescribir archivos con nombres repetidos.
- Se han procesado correctamente las subcarpetas anidadas.
- Los archivos sin extensión se han guardado en su propia categoría.
- Las carpetas originales permanecen, aunque hayan quedado vacías.

---

## 📊 Informe final con Rich

Una vez finalizada la organización, se muestran dos tablas.

### 📋 Tabla de resumen

| Concepto | Resultado de ejemplo |
|---|---:|
| Archivos movidos | 7 |
| Tamaño total movido | 2.35 MB |
| Archivos restantes en origen | 0 |
| Archivos en destino | 7 |

*Los valores son ilustrativos; dependen de los archivos procesados.*

El número de archivos restantes en origen se muestra en **verde** cuando es cero y en **rojo** cuando quedan archivos pendientes.

### 📑 Tabla de movimientos

Muestra un registro numerado de los archivos trasladados, indicando su ruta de origen y su ubicación de destino.

| Nº | Origen | Destino |
|---|---|---|
| 1 | carpeta_prueba/foto.jpg | organizados/jpg/foto.jpg |
| 2 | carpeta_prueba/informe.pdf | organizados/pdf/informe.pdf |
| 3 | carpeta_prueba/notas.txt | organizados/txt/notas.txt |
| 4 | carpeta_prueba/trabajos/antiguos/notas.txt | organizados/txt/notas_1.txt |

---

## 🔢 Pruebas de la función tamano_legible()

También se ha creado el archivo tamano_legible.py para comprobar de forma independiente la conversión de tamaños.

| Bytes introducidos | Resultado |
|---|---:|
| 500 | 500 bytes |
| 1024 | 1.00 KB |
| 2048576 | 1.95 MB |
| 5073741824 | 4.72 GB |

Para ejecutar estas pruebas:

python tamano_legible.py

Este archivo importa la función tamano_legible() del organizador, permitiendo comprobar su funcionamiento sin ejecutar la clasificación de archivos.

## ⚠️ Consideraciones importantes

- El programa **mueve los archivos, no los copia**.
- Se recomienda utilizar carpetas de prueba antes de trabajar con documentos importantes.
- Los archivos existentes en destino no deben sobrescribirse.
- Las carpetas originales no se eliminan después de mover su contenido.
- El entorno virtual `.venv` no se incluye en el repositorio.
- Las rutas de origen y destino deben ser distintas y no estar una dentro de la otra.

