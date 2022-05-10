# Kiyoshi Ali Martinez Renteria

import nltk
from nltk.corpus import treebank

sentence = "./Documentos/documento2.txt"
tokens = nltk.word_tokenize(sentence)
print(tokens)

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
