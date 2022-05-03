print("Procesamiento de lenguaje natural")
print("Ingenieria en computacion")
suma = 7+5 
resultado = suma * 6
print("Resultado =", resultado)
#-------------------------------------
archivo = open("Texto.txt", "r")
print(archivo.read())
archivo.close()

archivo = open("Texton.txt", "w")
cadena1 = "Primer clase de programacion python"
archivo.write(cadena1)
archivo.close()

archivo = open("Texton.txt", "r")
print(archivo.read())
archivo.close()
