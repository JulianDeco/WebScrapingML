import os

#Necesario para el scrapping
from bs4 import BeautifulSoup
import requests
import time

#Necesario para ordenar el diccionario
import operator

#Necesario para manejar hoja de calculo
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.dimensions import ColumnDimension



search = input('Introduzca lo que quiera buscar: ')
#URL donde solicitamos el html
url = requests.get(f'https://listado.mercadolibre.com.ar/{search}')


soup = BeautifulSoup(url.content, "html.parser")


resultados_titulos = soup.findAll('h2', {'class':'ui-search-item__title'})

resultados_precios = soup.findAll('div', {'class':'ui-search-price__second-line'})



for i in range(0, len(resultados_titulos)):
    b = resultados_precios[i].text
    a = b.split()
    
    print(a[0], " /// ", resultados_titulos[i].text)

print(len(resultados_precios))
print(len(resultados_titulos))