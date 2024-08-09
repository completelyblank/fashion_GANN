from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load the pre-trained model
generator = tf.keras.models.load_model('models/generator_model.h5')

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        # Generate random noise
        random_vector = np.random.normal(0, 1, (1, 128))
        generated_image = generator.predict(random_vector)

        # Rescale the generated image to [0, 1]
        generated_image = 0.5 * generated_image + 0.5

        # Ensure the image has the correct shape and channels
        if generated_image.shape != (1, 28, 28, 1):
            raise ValueError(f"Unexpected image shape: {generated_image.shape}")

        # Convert to PIL Image (grayscale)
        img = Image.fromarray((generated_image[0, :, :, 0] * 255).astype(np.uint8), mode='L')

        # Resize if necessary
        img = img.resize((256, 256), Image.LANCZOS)  # Adjust size as needed

        # Save the image to a BytesIO object
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
