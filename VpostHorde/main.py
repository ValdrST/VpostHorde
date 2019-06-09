import pkg_resources
import sys
from .tools import Consola
def main():
    consola = Consola()
    consola.evaluarArgumentos()
    consola.iniciar_consola()