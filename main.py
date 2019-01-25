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
        'titulo': s1.soup.find('title').text.encode("utf-8"),
        'zona': s1.scrape_tags_with_class('p', 'zona-nombre'),
        'precio': s1.scrape_tags_with_class('p', 'precio-final'),
        'telefono': s1.scrape_tags_with_class('span', 'lineInmo'),
        'info': s1.scrape_tags_with_class('div', 'dotInfo'),
        'referencia': s1.find_tag_or_empty('div', 'class', 'referencia-slider'),
        'descripcion': s1.find_tag_and_strip_html('div', 'id', 'descripcion'),
        'anunciante': s1.find_tag_or_empty('p', 'id', 'nombre-inmobiliaria'),
    }


def parse_main_page(html):
    """
    Parser para la pagina principal
    :param html:
    :return:
    """
    s2 = Scraper(html)
    return {
        'target_urls': s2.get_attr_from_tag_with_class('a', 'class', 'holder-link')
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


def main():
    print("python main function")

    # # leer de archivos
    # folder = 'samples/'
    # to_parse = ['sample2.html', 'sample3.html', 'sample5.html', 'sample6.html']
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

    to_parse = to_parse[:3]

    print("Salvando lista de enlaces... ")

    # guarda lista de enlaces encontrados
    with open('output/to_parse.txt', 'w') as f:
        for line in to_parse:
            f.write(line + "\n")

    print("Leyendo enlaces... ")

    # leer de sitios web
    parsed = parse_from_urls(to_parse)

    print("Guardando csv... ")


    keys = parsed[0].keys()
    with open('output/info.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(parsed)


if __name__ == '__main__':
    main()


