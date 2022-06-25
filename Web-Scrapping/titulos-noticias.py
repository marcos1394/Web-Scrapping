from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = (r"C:\Users\marcos.sandovalr\Downloads\chromedriver_win32\chromedriver.exe")

servicio = Service(executable_path=path)
driver = webdriver.Chrome(service=servicio)
driver.get(website)

