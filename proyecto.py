#Kiyoshi Ali Martinez Renteria
import os

carpeta_nombre = "./Documentos/"

carpeta_salida = "./Documentos/"

archivo_salida = "documento.txt"

archivos_lista = os.listdir(carpeta_nombre)

union = ""
linea_vacia = 0

for archivo_nombre in archivos_lista:
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_lista = archivo.readlines()
    archivo.close()
    
    #Cuantas lineas tiene el texto
    longitud = len(lineas_lista)
    print("El archivo", archivo_nombre, "tiene", longitud, "lineas")
    
    #Cuantas lineas vacias tiene el texto
    for linea in lineas_lista:
        if linea.strip() == "":
            linea_vacia = linea_vacia+1
    print("El archivo", archivo_nombre, "tiene", linea_vacia, "lineas vacias")
    
    #Eliminar los simbolos de puntuacion
    with open(carpeta_nombre+archivo_nombre, "r") as archivo:
        texto = archivo.read()
    archivo.close()
    simbolos = ["(",")",",",".",";",":","\""]
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " ")
        
    #Todas las palabras de manera ordenada
    palabras_lista = texto.split()
    palabras_lista.sort()
    print(palabras_lista)
    
    union += texto + "\n"
    
    #Cuantas palabras contiene cada documento
    print("El archivo", archivo_nombre, "tiene", len(palabras_lista), "palabras")
    
with open(carpeta_salida+archivo_salida, "w") as salida:
    salida.write(union)
    
#Parte 2

with open(carpeta_salida+archivo_salida, "r") as texto:
    
    #Mostrar palabras que tiene el documento
    palabras_lista.sort()
    print(palabras_lista)
        
    #Cuantas palabras tiene  el documento
    print("El archivo", archivo_salida, "tiene", len(palabras_lista), "palabras")
    acumuladorPalabras = 0
    
    #Busqueda de una palabra
    palabra = input("\nEscribe la palabra a buscar: ")
    for palabras in palabras_lista:
        if palabra in palabras:
            acumuladorPalabras += 1
            
    print("La palabra ", palabra, " aparecio ", acumuladorPalabras, " veces")