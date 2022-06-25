from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys


ruta_ejecutable = os.path.dirname(sys.executable)

fecha_hoy = datetime.now()
#MMDDYYYY
mes_dia_ano = fecha_hoy.strftime("%m%d%y")

website = "https://www.thesun.co.uk/sport/football/"
path = (r"C:\Users\marcos.sandovalr\Downloads\chromedriver_win32\chromedriver.exe")


opciones = Options()
opciones.headless = True

servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio, options=opciones)
driver.get(website)

contenedores = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titulos = []
subtitulos = []
links = []

for contenedor in contenedores:
    titulo = contenedor.find_element(by="xpath", value='./a/h2').text
    subtitulo = contenedor.find_element(by="xpath", value='./a/p').text
    link = contenedor.find_element(by="xpath", value='./a').get_attribute("href")
    titulos.append(titulo)
    subtitulos.append(subtitulo)
    links.append(link)


mi_diccionario = {'titulo':titulos, 'subtitulo':subtitulos, 'link': links}
df_noticias = pd.DataFrame(mi_diccionario)
nombre_archivo = f'noticias-{mes_dia_ano}.csv'
ruta_final = os.path.join(ruta_ejecutable,nombre_archivo)
df_noticias.to_csv(ruta_final)
driver.quit()
