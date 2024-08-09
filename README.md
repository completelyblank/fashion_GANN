![image](https://github.com/user-attachments/assets/ec53dafa-7dd1-44de-8d66-bd5f352e64e9)

# Fashion GAN

## Overview

Fashion GAN is a project that utilizes TensorFlow to create a Generative Adversarial Network (GAN) for generating new fashion images. The backend is built with Flask, providing a RESTful API for generating and retrieving images. The frontend is interactive, developed using HTML, CSS, and JavaScript, to display and interact with the generated fashion images.

## Features

- **Generative Adversarial Network (GAN)**: Trains a GAN to generate new fashion images based on the Fashion MNIST dataset.
- **Backend**: Flask application serving the GAN model and handling image generation requests.
- **Frontend**: Interactive HTML+CSS+JS interface to display generated images.
- **Dataset**: Uses the Kaggle Fashion MNIST dataset.
- **GPU Acceleration**: Utilizes GPU for faster training and image generation.
- **Model Components**:
  - `Conv2D`, `Dense`, and `LeakyReLU` layers in the GAN architecture.
  - `Adam` optimizer.
  - `Binary Crossentropy` loss function.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/fashion-gan.git
cd fashion-gan
