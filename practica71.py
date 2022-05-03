from distutils import archive_util
import nltk

carpeta_nombre = "./Documentos/"
archivo_nombre = "documento2.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)
    
palabras_total = len(tokens)
print("Palabras",palabras_total)

total_conjunto = set(tokens)
palabras_diferentes = len(total_conjunto)
print("Palabras diferentes ", palabras_diferentes)

riqueza_lexica = palabras_diferentes/palabras_total
print("Riqueza lexica : ", riqueza_lexica)
riqueza_lexicap = 100* riqueza_lexica
print("Porcentaje de riqueza lexica: ", round(riqueza_lexicap, 2),"%")

conteo_individual = tokens.count("eth")

print("Numero de veces que se encuentra la palabra 'eth' =", conteo_individual)

palabras_totales = len(tokens)

porcentaje = 100 * conteo_individual/palabras_totales
porcentaje = round(porcentaje, 2)
print(porcentaje,"%")

texto_nltk = nltk.Text(tokens)
texto_nltk.concordance("de")
print("------------------------------------")
texto_nltk.similar("ETH")

