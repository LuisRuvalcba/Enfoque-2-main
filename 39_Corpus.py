import random

# Función para generar texto probabilístico
def generate_text(word_prob, num_words=50, seed_word='the'):
    text = [seed_word]
    for _ in range(num_words):
        next_word = random.choices(list(word_prob.keys()), weights=list(word_prob.values()))[0]
        text.append(next_word)
    return ' '.join(text)

# Generamos texto probabilístico
generated_text = generate_text(word_prob)

# Imprimimos el texto generado
print("Texto generado:")
print(generated_text)
