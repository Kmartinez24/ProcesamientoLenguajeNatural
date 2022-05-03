from cgitb import text
import re
from typing import TextIO

carpeta_nombre = "./Documentos/"
archivo_nombre = "Texto1.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()
    
expresion_regular = re.compile(r"de")
resultados_busqueda = expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))