carpeta_nombre = "./Documentos/"
archivo_nombre = "Doc1.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()
    
palabras_lista = texto.split()
print(palabras_lista)