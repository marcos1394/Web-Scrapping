from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


website = "https://www.thesun.co.uk/sport/football/"
path = (r"C:\Users\marcos.sandovalr\Downloads\chromedriver_win32\chromedriver.exe")

servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)
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
df_noticias.to_csv('noticias.csv')

driver.quit()