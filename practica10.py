#A esta altura ya tenemos la lista de tokens en "tokens"
import nltk

carpeta_nombre = "./Documentos/"
archivo_nombre = "documento2.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")

tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)

texto_nltk = nltk.Text(tokens)

distribucion = nltk.FreqDist(texto_nltk)
hapaxes = distribucion.hapaxes()
print("---------------------------------------------------")
print("Hapaxes")
for hapax in hapaxes:
    print(hapax)
print("---------------------------------------------------")
print("Palabras totales: ", palabras_totales)
print("Palabras diferentes: ", palabras_diferentes)
print("---------------------------------------------------")
distribucion.plot(cumulative=True)
distribucion.plot(40, cumulative=True)