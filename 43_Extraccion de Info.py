import spacy

# Cargamos el modelo en español de Spacy
nlp = spacy.load("es_core_news_sm")

# Ejemplo de texto
text = "Apple es una empresa de tecnología con sede en Cupertino, California. Tim Cook es el CEO de Apple."

# Procesamos el texto para obtener objetos de documento de Spacy
doc = nlp(text)

# Extraemos relaciones entre entidades utilizando dependencias sintácticas
relations = []
for entity in doc.ents:
    if entity.label_ == 'ORG':
        for child in entity.root.children:
            if child.dep_ == 'nsubj' and child.ent_type_ == 'PERSON':
                relation = (child.text, 'es CEO de', entity.text)
                relations.append(relation)

print("Relaciones extraidas:")
for relation in relations:
    print(relation)
