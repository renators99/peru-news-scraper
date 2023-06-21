#Import classes from utils.scrapers
from utils.scrapers.ojo.ojo import Ojo
from utils.scrapers.correo.correo import Correo
from utils.scrapers.andina.andina import Andina
from utils.scrapers.peru21.peru21 import Peru21
from utils.scrapers.comercio.comercio import Comercio
from utils.scrapers.republica.republica import Republica

class ProcessLibrary():
    """
        Library to consolidate the different modules used in the project
    """
    Ojo = Ojo
    Andina = Andina
    Correo = Correo
    Peru21 = Peru21
    Comercio = Comercio
    Republica = Republica