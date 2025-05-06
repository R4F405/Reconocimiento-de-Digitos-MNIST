 # MNIST Digit Recognition ✍️🔢

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-380/)

This project implements a handwritten digit recognizer using a model trained on the MNIST dataset. The system can process images of digits, center them appropriately, and predict which number they represent.

## 💡 Description

This program uses a neural network trained with the MNIST dataset to recognize handwritten digits. Main features:

- Image processing to adapt them to the MNIST format (28x28 pixels)
- Automatic digit centering based on the center of mass
- Image normalization and binarization
- Prediction using a pre-trained model

## ✅ Requirements

- Python 3.8 or higher
- TensorFlow
- NumPy
- Matplotlib
- PIL (Pillow)
- SciPy

You can install the dependencies with:

```bash
pip install tensorflow numpy matplotlib pillow scipy
```

## 📁 Project Structure

```
.
├── modelo_mnist.keras    # Pre-trained TensorFlow model
├── numero.png            # Example image to predict
└── Reconocer_Numeros.py  # Main script
```

## ▶️ Usage

1.  Place an image of a handwritten digit named `numero.png` in the project directory.
2.  Make sure the pre-trained model `modelo_mnist.keras` is in the directory.
3.  Run the script:

```bash
python Reconocer_Numeros.py
```

The program will display the processed image and the digit prediction.

## ⚙️ How it Works

The script performs the following operations:

1.  Loads and processes the image:
    * Converts to grayscale
    * Inverts colors (assumes white background, black digit)
    * Resizes to 28x28 pixels
    * Binarizes the image
    * Normalizes values between 0 and 1
    * Centers the digit based on its center of mass

2.  Loads the pre-trained model with TensorFlow.

3.  Performs digit prediction and displays the result.

## 🎨 Customization

To use another image, simply change the `ruta_imagen` variable in the code or modify the file to accept command-line arguments.

## 📜 License

This project is under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## 👨‍💻 Author

R4F405

[LinkedIn](https://www.linkedin.com/in/rafaspg) · [GitHub](https://github.com/R4F405)
