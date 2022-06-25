from tkinter import PAGES
import camelot


tabla = camelot.read_pdf("", pages='')

print(tabla)

tabla.export('')
