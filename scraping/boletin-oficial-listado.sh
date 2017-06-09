python3 scraping-get-links.py | grep "\!DetalleSegunda" | sed "s/.*/https:\/\/www.boletinoficial.gob.ar\/&/" > boletin-oficial-listado.txt
