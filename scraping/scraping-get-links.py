#!/usr/bin/env python
# Script que basicamente consigue todos los links de una URL
# Antes que nada hay que instalar python3 y algunas librerias con pip3
# (manejador de paquetes de python)

# Requerimientos:
# Instalar los siguientes paquetes/librerias
# apt-get install python3 python3-pip xvfb
# pip3 install beautifulsoup4 pyvirtualdisplay selenium

# Bajar el chromedriver y dejarlo en /usr/bin con los permisos necesarios
# wget http://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip && mv chromedriver /usr/bin
# chmod 755 /usr/bin/chromedriver

# Importo las librerias necesarias
from bs4 import BeautifulSoup 
from pyvirtualdisplay import Display
from selenium import webdriver

# Le paso los parametros del display que usara el browser
display = Display(visible=0, size=(1024, 768))
display.start()

# Defino una alias para una url
URL = 'https://www.boletinoficial.gob.ar/#!Portada/segunda/all/20170508'
# https://www.boletinoficial.gob.ar/#!DetalleSegunda/A650000/null

# Abro el browser chrome, y me bajo todo el contenido
browser = webdriver.Chrome()
browser.get(URL)
soup = BeautifulSoup(browser.page_source, 'html.parser')

# Imprimo solo los links, todo lo que tenga la referencia href
for link in soup.find_all('a'):
    x = link.get('href')
    print (x)

# Cierro el navegador y el display
browser.close()
display.stop()
