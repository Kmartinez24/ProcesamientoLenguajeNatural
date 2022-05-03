#Kiyoshi Ali Martinez Renteria
import os

carpeta_nombre = "./Documentos/"

archivos_lista = os.listdir(carpeta_nombre)

for archivo_nombre in archivos_lista:
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_lista = archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivo_nombre, "tiene", longitud, "lineas")
    with open(carpeta_nombre+archivo_nombre, "r") as archivo:
        texto = archivo.read()
    archivo.close()
    
    simbolos = ["(",")",",",".",";",":","\""]
    for simbolo in simbolos:
        texto = texto.replace(simbolo," "+simbolo+" ")
    
    palabras_lista = texto.split()
    palabras_lista.sort()
    for palabra in palabras_lista:
        print(palabra)
    print("\n")