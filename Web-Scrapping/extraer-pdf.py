from bz2 import compress
from tkinter import PAGES
import camelot


# el primer argumento es el nombre o ruta del archivo, segundo argumento la pagina donde esta la tabla
tabla = camelot.read_pdf("", pages='')

print(tabla)


# primer argumento nombre del archivo que crearemos, segundo el formato y el tercero indicamos que lo comprima
tabla.export('', f='csv', compress=True)
