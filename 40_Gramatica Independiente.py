# Definimos una frase para analizar
sentence = "the cat chased the bird on the roof"

# Creamos un parser probabilístico basado en la gramática
parser = nltk.ViterbiParser(grammar)

# Analizamos la frase y mostramos los árboles de análisis más probables
for tree in parser.parse(sentence.split()):
    print("Arbol de Analisis:")
    print(tree)
    print("Probabilidad:", parser.probability(tree))
