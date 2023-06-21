import argparse
from utils.scrapers.scrapnews_lib import ProcessLibrary

print("Hola, bienvenidos a la base de palabras repetidas en los diarios del Pais")
parser = argparse.ArgumentParser(description='Args to start the data collection process')
parser.add_argument('--process', type=str, help='Process to run', required=True,
                    choices=['Comercio','Republica','Correo','Ojo','Peru21','Andina'])
parser.add_argument('--step', type=str, help='Process type to run', required=True,
                    choices=['extract', 'transform', 'load', 'all'])
args = parser.parse_args()

#Do the process with all arguments parsed
x = getattr(ProcessLibrary, args.process)
x = x(args.step)
x.run()