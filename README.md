# Reconocimiento de Dígitos MNIST

Este proyecto implementa un reconocedor de dígitos escritos a mano utilizando un modelo entrenado en el conjunto de datos MNIST. El sistema puede procesar imágenes de dígitos, centrarlas adecuadamente y realizar una predicción sobre qué número representan.

## Descripción

Este programa utiliza una red neuronal entrenada con el conjunto de datos MNIST para reconocer dígitos escritos a mano. Características principales:

- Procesamiento de imágenes para adaptarlas al formato MNIST (28x28 píxeles)
- Centrado automático del dígito basado en el centro de masa
- Normalización y binarización de la imagen
- Predicción mediante un modelo pre-entrenado

## Requisitos

- Python 3.x
- TensorFlow
- NumPy
- Matplotlib
- PIL (Pillow)
- SciPy

Puedes instalar las dependencias con:

```bash
pip install tensorflow numpy matplotlib pillow scipy
```

## Estructura del proyecto

```
.
├── modelo_mnist.keras    # Modelo TensorFlow pre-entrenado
├── numero.png            # Imagen de ejemplo para predecir
└── Reconocer_Numeros.py  # Script principal
```

## Uso

1. Coloca una imagen de un dígito escrito a mano con el nombre `numero.png` en el directorio del proyecto.
2. Asegúrate de que el modelo pre-entrenado `modelo_mnist.keras` esté en el directorio.
3. Ejecuta el script:

```bash
python Reconocer_Numeros.py
```

El programa mostrará la imagen procesada y la predicción del dígito.

## Funcionamiento

El script realiza las siguientes operaciones:

1. Carga y procesa la imagen:
   - Convierte a escala de grises
   - Invierte los colores (asume fondo blanco, dígito negro)
   - Redimensiona a 28x28 píxeles
   - Binariza la imagen
   - Normaliza los valores entre 0 y 1
   - Centra el dígito basado en su centro de masa

2. Carga el modelo pre-entrenado con TensorFlow.

3. Realiza la predicción del dígito y muestra el resultado.

## Personalización

Para utilizar otra imagen, simplemente cambia la variable `ruta_imagen` en el código o modifica el archivo para que acepte argumentos de línea de comandos.

## Licencia

[![Licencia](https://img.shields.io/badge/Licencia-GNU%20GPL%20v3-blue.svg)](LICENSE)

## Autor

Rafa San Pablo Gonzalez

[LinkedIn](https://www.linkedin.com/in/rafaspg) · [GitHub](https://github.com/R4F405)
