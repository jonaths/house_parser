# Scraper para bienes raices

Scraper para recuperar datos de un sitio web.

  - Scraper para pagina catalogo
  - Scraper para pagina de contenido
  - Diseño modular y adaptable

### Instalación

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ git clone https://github.com/jonaths/house_parser.git
$ cd house_parser
$ pip install BeautifulSoup4
$ python main.py
```
### Funcionamiento
El programa esta diseñado para recuperar datos de forma estructurada del sitio web    https://www.infocasas.com.py/venta/casas-y-departamentos-y-terrenos-y-locales-comerciales-y-oficinas-y-tinglado-o-deposito-y-duplex/central y de sus paginas consecutivas
  - pagina1
  - pagina2
  - ...

La pagina inicial y la final estan controladas por las variables `start_page` y `end_page`.

### Configuracion

En main.py editar:
  - start_page: el consecutivo de la pagina donde empezara a hacer scraping. Min. 1.
  - end_page: el consecutivo de la pagina donde terminara de hacer scraping. Debe ser mayor que end_page.

### Desarrollo

Es posible actualizar nuevas rutas en la estructura html editando los metodos `parse_main_page` y `parse_inner_page`.
