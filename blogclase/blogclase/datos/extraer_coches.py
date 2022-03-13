'''
Programa que extrae los datos de https://www.eleconomista.es/ecomotor/marcas/
y genera un json con los datos de las películas

Trabajo: 
* Inspeccionar la estructura de la web
* Extraer los datos de las películas con xpath
'''

import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}



def detalle(url_peli):
    url = urljoin ('https://www.eleconomista.es/ecomotor/marcas/', url_peli)
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)
    script = pagina.xpath('//script[@type="application/ld+json"]')[0]
    datos = json.loads(script.text)

def datos_coches(peli):
    ''''
    Función que dado un elemento tr de la web devuelve los datos de la pagina
    '''
    # datos a devolver
    datos = {}

    elementos = peli.xpath(".//td")
    marca = elementos[0]
    modelo_ = elementos[1]

    #marca
    marca = marca.xpath(".//a/@title")[0]
    datos['mar'] = marca

    #modelo
    modelo_ = marca.xpath(".//a/@text")[0]
    datos['mar'] = modelo_
    
    datos.update(detalle(url))

    return datos

if __name__ == '__main__':

    url = 'https://www.imdb.com/chart/top/'
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    peliculas = pagina.xpath("//tr")


    datos = [datos_coches(p) for p in peliculas]
    json.dump(datos, open('datos_coches.json', 'w'))