import  tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from scipy.ndimage import center_of_mass
import os

# -------- FUNCIONES DE PROCESADO --------

def centrar_imagen(imagen_array):
    # Obtener centro de masa
    centro_y, centro_x = center_of_mass(imagen_array)

    # Crear nueva imagen centrada
    nueva_imagen = np.zeros((28, 28))
    shift_x = int(14 - centro_x)
    shift_y = int(14 - centro_y)

    for y in range(28):
        for x in range(28):
            nuevo_x = x + shift_x
            nuevo_y = y + shift_y
            if 0 <= nuevo_x < 28 and 0 <= nuevo_y < 28:
                nueva_imagen[nuevo_y, nuevo_x] = imagen_array[y, x]
    return nueva_imagen

def procesar_imagen(ruta):
    imagen = Image.open(ruta).convert("L")
    imagen = ImageOps.invert(imagen)  # invertir si es fondo blanco
    imagen = imagen.resize((28, 28))

    imagen_array = np.array(imagen)

    # Binarizar
    imagen_array = (imagen_array > 100) * 255

    # Normalizar
    imagen_array = imagen_array / 255.0

    # Centrar
    imagen_array = centrar_imagen(imagen_array)

    return imagen_array

# -------- CARGA DEL MODELO --------
modelo = tf.keras.models.load_model("modelo_mnist.keras")

# -------- PREDICCIÓN DE IMAGEN PERSONAL --------
ruta_imagen = "numero.png"

if os.path.exists(ruta_imagen):
    imagen_procesada = procesar_imagen(ruta_imagen)

    # Mostrar imagen final
    plt.imshow(imagen_procesada, cmap='gray')
    plt.title("Imagen procesada para predicción")
    plt.axis('off')
    plt.show()

    # Ajustar forma y predecir
    imagen_input = imagen_procesada.reshape(1, 28, 28)
    prediccion = modelo.predict(imagen_input)
    resultado = np.argmax(prediccion)

    print(f"El modelo cree que es un: {resultado}")
else:
    print(f"No se encontró la imagen: {ruta_imagen}")