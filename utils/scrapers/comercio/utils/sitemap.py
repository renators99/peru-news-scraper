import os
import sys
import json
import requests

from bs4 import BeautifulSoup

from utils.scrapers.comercio.settings import URL,PATH_SITEMAP

def get_soup(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Hubo un error al realizar la solicitud HTTP: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Hubo un error al parsear el HTML: {e}")
        sys.exit(1)

def get_data(soup):
    try:
        # Buscar la sección 'nav' con id='nav-ds-container'
        nav_section = soup.find('nav', id='nav-ds-container')

        # Encontrar todos los elementos 'li' dentro de este 'nav'
        li_elements = nav_section.find_all('li')

        # Crear una lista para almacenar los datos
        data = []

        # Llenar la lista con los datos de cada elemento 'li'
        for li in li_elements:
            href = li.a['href']
            if not href.startswith(('http', 'https')):
                href=URL+href

            data.append({
                'text': li.a.text,
                'href': href,
            })

        # Excluir los dos primeros elementos y el último
        data = data[2:-1]
        
        return data
    except Exception as e:
        print(f"Hubo un error al procesar los datos del HTML: {e}")
        sys.exit(1)

def save_to_json(data, file_name):
    if not os.path.exists(PATH_SITEMAP):
        os.makedirs(PATH_SITEMAP)
    try:
        # Guardar los datos en un archivo JSON
        with open(PATH_SITEMAP+file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Hubo un error al guardar los datos en un archivo JSON: {e}")
        sys.exit(1)
        
def get_sections():  # sustituir por la URL que quieres scrappear

    soup = get_soup(URL)
    data = get_data(soup)
    save_to_json(data, 'comercio_sections.json')