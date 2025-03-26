from transformers import MarianMTModel, MarianTokenizer

# Oración de ejemplo en español
spanish_sentence = "el aprendizaje automatico es fascinante"

# Cargamos el modelo pre-entrenado para la traducción español-inglés
model_name = "Helsinki-NLP/opus-mt-es-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Tokenizamos la oración en español y la traducimos a inglés
inputs = tokenizer(spanish_sentence, return_tensors="pt", padding=True, truncation=True)
translated_ids = model.generate(**inputs)
translated_sentence = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("Traduccion de la oracion:", translated_sentence)
