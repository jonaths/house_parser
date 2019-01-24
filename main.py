from bs4 import BeautifulSoup
import urllib2
from tools.scraper import Scraper
import json

def parse_inner_page(html):
    s1 = Scraper(html)
    return {
        'titulo': s1.scrape('title'),
        'zona': s1.scrape('zone'),
        'precio': s1.scrape('price'),
        'telefono': s1.scrape('phone'),
        'info': s1.scrape('info'),
        'referencia': s1.scrape('reference'),
        'descripcion': s1.scrape('desc')
    }


def parse_main_page(html):
    s2 = Scraper(html)
    return {
        'target_urls': s2.scrape('urls_from_main')
    }


def parse_from_files(files_list, folder='samples/'):
    data = []
    for p in files_list:
        print('Processing ' + p)
        f = open(folder + p, 'r')
        html = f.read()
        data.append(parse_inner_page(html))
    return data


def parse_from_urls(urls_list):
    data = []
    for p in urls_list:
        print('Processing ' + p)
        response = urllib2.urlopen(p)
        html = response.read()
        data.append(parse_inner_page(html))
    return data

# leer de archivos
# folder = 'samples/'
# to_parse = ['sample2.html', 'sample3.html', 'sample5.html']
# parsed = parse_from_files(to_parse)
# print parsed


base_url = 'https://www.infocasas.com.py'
main_url = base_url+'/venta/casas-y-departamentos-y-terrenos-y-locales-comerciales-y-oficinas-y-tinglado-o-deposito-y-duplex/central'


# recupera enlaces de propiedades
response = urllib2.urlopen(main_url)
html = response.read()
to_parse = parse_main_page(html)
to_parse = [base_url+p for p in to_parse['target_urls']]

# guarda lista de enlaces encontrados
with open('output/to_parse.txt', 'w') as f:
    for line in to_parse:
        f.write(line + "\n")

to_parse = to_parse[]

# leer de sitios web
# to_parse = ['https://www.infocasas.com.py/duplex-en-lambare-pegado-al-colegio-sek/185925457?v']
# parsed = parse_from_urls(to_parse)
# print parsed







# print soup.prettify()

# Titulo	Zona	Precio	Anunciante	Telefono	Tipo de propiedad	Cant. dormitorios
# Cantidad de Banos	M2 edificado	Garage	Referencia	Ubicacion Lat	Ubicacion Long

#banner > div > div.dinamicaLeft > div > div.left > p
# //*[@id="banner"]/div/div[1]/div/div[2]/p
# <p class="titulo">Residencia en Lambare</p>