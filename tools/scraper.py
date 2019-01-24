# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, features="html.parser")
        self.scrapers = {
            'title': self.soup.find('title').text.encode("utf-8"),
            'zone': self.scrape_tags_with_class('p', 'zona-nombre'),
            'price': self.scrape_tags_with_class('p', 'precio-final'),
            'phone': self.scrape_tags_with_class('span', 'lineInmo'),
            'info': self.scrape_tags_with_class('div', 'dotInfo'),
            'reference': self.find_tag_or_empty('div', 'referencia-slider'),
            'desc': self.find_tag_and_strip_html('div', 'id', 'descripcion'),
            'urls_from_main': self.get_attr_from_tag_with_class('a', 'class', 'holder-link')
        }
        pass

    def scrape(self, index):
        return self.scrapers[index]

    def get_attr_from_tag_with_class(self, tag, attr_name, class_name, attr_to_find='href'):
        """
        Recupera una lista de todos los attr_to_find que haya segun las restricciones
        :param attr_to_find:
        :param tag:
        :param attr_name:
        :param class_name:
        :return:
        """
        items = self.soup.find_all(tag, attrs={attr_name: class_name})
        items_arr = []
        for i in items:
            if i.has_attr(attr_to_find):
                items_arr.append(i.attrs[attr_to_find])
            else:
                items_arr.append('')
        return items_arr

    def find_tag_and_strip_html(self, tag, attr_name, class_name):
        """
        Recupera un tag y elimina html interior para mostrar texto plano
        :param tag: div, p u otro
        :param attr_name: id, class
        :param class_name: nombre del id o de la clase
        :return:
        """
        return self.soup.find(tag, attrs={attr_name: class_name}).get_text().encode("utf-8") if self.soup.find(tag, attrs={attr_name: class_name}) else ''

    def find_tag_or_empty(self, tag, class_name):
        """
        Encuentra el tag con class_name y si no esta regresa ""
        :param tag:
        :param class_name:
        :return:
        """
        return self.soup.find(tag, attrs={'class': class_name}).text.encode("utf-8") \
                   if self.soup.find(tag, attrs={'class': class_name}) else '',

    def scrape_tags_with_class(self, tag, class_name):
        """
        Encuentra todos los tags con class_name y los devuelve concatenados por un |
        :param tag:
        :param class_name:
        :return:
        """
        items = self.soup.find_all(tag, attrs={'class': class_name})
        items_str = ''
        for p in items:
            items_str += p.text.encode("utf-8") + '|'
        # elimina el ultimo |
        return items_str[:-1]
