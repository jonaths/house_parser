# -*- coding: UTF-8 -*-

import urllib2
from tools.scraper import Scraper
import random
import time
import csv


def parse_inner_page(html):
    """
    Parser para paginas interiores
    :param html:
    :return:
    """
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
    """
    Parser para la pagina principal
    :param html:
    :return:
    """
    s2 = Scraper(html)
    return {
        'target_urls': s2.scrape('urls_from_main')
    }


def parse_from_files(files_list, folder='samples/'):
    """
    Hace un parsing a partir de una lista de nombres de archivos
    :param files_list:
    :param folder:
    :return:
    """
    data = []
    for p in files_list:
        print('Processing ' + p)
        f = open(folder + p, 'r')
        html = f.read()
        data.append(parse_inner_page(html))
    return data


def parse_from_urls(urls_list):
    """
    Hace un parsing a partir de una lista de url
    :param urls_list:
    :return:
    """
    data = []
    for p in urls_list:
        print('Processing ' + p)
        response = urllib2.urlopen(p)
        html = response.read()
        data.append(parse_inner_page(html))
        # espera para evitar bloqueos
        timeDelay = random.randrange(1, 5)
        time.sleep(timeDelay)
    return data

# # leer de archivos
# folder = 'samples/'
# to_parse = ['sample2.html', 'sample3.html', 'sample5.html']
# parsed = parse_from_files(to_parse)
# print parsed


print("Iniciando... ")

# definir urls objetivo
base_url = 'https://www.infocasas.com.py'
main_url = base_url+'/venta/casas-y-departamentos-y-terrenos-y-locales-comerciales-y-oficinas-y-tinglado-o-deposito-y-duplex/central'

print("Leyendo pagina principal... ")

# recupera enlaces de propiedades
response = urllib2.urlopen(main_url)
html = response.read()
to_parse_without_base_url = list(set(parse_main_page(html)['target_urls']))
to_parse = [base_url+p for p in to_parse_without_base_url]

print("Salvando lista de enlaces... ")

# guarda lista de enlaces encontrados
with open('output/to_parse.txt', 'w') as f:
    for line in to_parse:
        f.write(line + "\n")

# print("Leyendo enlaces... ")
#
# # leer de sitios web
# parsed = parse_from_urls(to_parse)
#
# print("Guardando csv... ")
#
#
# keys = parsed[0].keys()
# with open('output/info.csv', 'wb') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(parsed)
