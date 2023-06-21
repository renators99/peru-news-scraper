import argparse
from utils.scrapers.scraping_lib import ProcessLibrary

print("Hola, bienvenidos para ")
parser = argparse.ArgumentParser(description='Args to start the data collection process')
parser.add_argument('--process', type=str, help='Process to run', required=True,
                    choices=['CodigoCPP', 'JurisprudenciaTC', 'JurisprudenciaPJ','JurisprudenciaCIDH'])
parser.add_argument('--step', type=str, help='Process type to run', required=True,
                    choices=['extract', 'transform', 'load', 'all'])
args = parser.parse_args()

#Do the process with all arguments parsed
x = getattr(ProcessLibrary, args.process)
x = x(args.step)
x.run()