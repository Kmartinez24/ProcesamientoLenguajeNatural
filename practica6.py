carpeta_nombre = "./Documentos/"
archivo_nombre = "UNION.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()
simbolos = ["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto = texto.replace(simbolo," "+simbolo+" ")

palabras_lista = texto.split()

palabras_unicas=[]

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)
print(palabras_unicas)
num = len(palabras_unicas)
num2 = len(palabras_lista)
print("Numero de palabras en el documento", num2)
print("Numero de palabras unicas en el documento", num)