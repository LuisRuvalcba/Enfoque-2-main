import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Cargar y preprocesar los datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir el modelo de red neuronal profunda
modelo = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(x_train, y_train, epochs=5)

# Evaluar el modelo
modelo.evaluate(x_test, y_test)
