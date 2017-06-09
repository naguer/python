#!/usr/bin/env python3
# Script que basicamente consigue todos los links de las actas de constitucion s.a
# del boletin oficinal
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
import datetime

WEB = 'https://www.boletinoficial.gob.ar/'
FILE = 'actas-constitucion-sa-' +  datetime.date.today().strftime(r"%Y-%m-%d") + '.txt'

urls_extraidas = []
# urls_extraidas_tmp va es solo un contador para mostrar la cant de urls
 
# <-- Extraccion de links -->

#startdate = input("Ingrese la fecha de inicio (d-m-a ej 30-05-2017): ")   
startdate = "25-04-2017"
#enddate = input("Ingrese la fecha de fin (d-m-a ej 12-06-2017): ")   
enddate = "26-04-2017"

# Usando la libreria datetime, puedo imprimir las fechas en un rango
# y como quiero ej day-month-year
start = datetime.datetime.strptime(startdate, "%d-%m-%Y")
end = datetime.datetime.strptime(enddate, "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# Para mostrar en pantalla la cantidad de dias procesados
diassemana = 0
diastotales = 0
for date in date_generated:
    diastotales = diastotales + 1
    if date.weekday() < 5:
        diassemana = diassemana + 1
print ("Cantidad de dias procesados: " + str(diastotales))
print ("Cantidad de dias menos sabados y domingos: " + str(diassemana))

# Browser
print("Iniciando browser...")
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Chrome()

# Segun el rango de fechas que defini, voy ingresando a cada dia 
# del boletin oficinal en la seccion de Constitucion S.A (id: 1110)
for date in date_generated:
    # Salteo sabado y doming
    if date.weekday() < 5: 
        DAY = (date.strftime("%Y%m%d"))
        URL = (WEB + '#!Portada/segunda/1110/')
        # Agrego a la url por defecto el dia
        URLDAY = (URL + DAY)
               
        urls_extraidas_tmp = []
        # Abro el browser y me bajo el contenido de la pagina
        browser = webdriver.Chrome()
        browser.get(URLDAY)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        
       # Imprimo solo los links, todo lo que tenga la referencia href
        # (sin el href=True, a veces el campo es none y da error)
        for link in soup.findAll('a', href=True):
            x = link.get('href')
            # Si el link tiene el contenido "#!DetalleSegunda"
            # lo escribo en un file
            if '#!DetalleSegunda' in x:
                urls_extraidas.append(x)
                urls_extraidas_tmp.append(x)
                # Remuevo duplicados
            url1 = len(list(set(urls_extraidas_tmp)))
        print("Extrayendo " + str(url1) + " links dia " + date.strftime("%d-%m-%Y ") + "URL: " + URLDAY)
        browser.close()

# Remuevo duplicados
urls = list(set(urls_extraidas))
print ("Actas a descargar unicas: ", len(urls))

# Descarga de actas
actas = []
tot = len(urls)
i = 0
for URL in urls:
    i += 1
    WEBURL = (WEB + URL)
    # Abro el browser y me bajo el contenido de la pagina
    browser = webdriver.Chrome()
    browser.get(WEBURL)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    print("Descargando actas de ", WEBURL, "(", i ," de ", tot, ")")
    
    # Me bajo solo el acta de cada pagina y lo escribo en un file
    for X in soup.findAll('div', {'id': 'print'}):
        # Ignoro los vacios
        if '/' in X.text:
            actas.append(X.text)

print(len(actas), " actas descargadas, guardando en ", FILE)
# Guardo en archivo
with open(FILE, 'w') as f:
  print("--\n".join(actas), file=f)

# Cierro el navegador y el display
browser.close()
display.stop()
