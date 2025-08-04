## Main Flask backend file ##


from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import cv2

# Initialize the Flask app
app = Flask(__name__)

# Loading trained CNN model (.keras file)
model = load_model('skin_disease_model.keras')

# Class mapping: class_name → full disease name
class_names = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
disease_labels = {
    'akiec': 'Actinic Keratoses',
    'bcc': 'Basal Cell Carcinoma',
    'bkl': 'Benign Keratosis',
    'df': 'Dermatofibroma',
    'mel': 'Melanoma',
    'nv': 'Melanocytic Nevus',
    'vasc': 'Vascular Lesion'
}

UPLOAD_FOLDER = 'static/uploads'  # Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##----- Function to predict the disease -----##

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(128, 128))   # Load image and resize to model input shape (128x128)
    img_array = image.img_to_array(img) / 255.0           # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)         # Add batch dimension
##----- Predict using the model -----##
    preds = model.predict(img_array)
    pred_class_index = np.argmax(preds)        # Get index of highest probability
    class_key = class_names[pred_class_index]  # Get class name
    class_label = disease_labels[class_key]    # Convert to human-readable label
    confidence = float(np.max(preds))          # Get top probability as confidence score

    return class_label, round(confidence * 100, 2)  # Return readable label and confidence percentage

##----- Landing page -----##
@app.route('/')
def home():
    return render_template('home.html')      # Loads the home page

##----- Upload and prediction page -----##

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    prediction = None   # Initialize variables for template rendering
    confidence = None
    uploaded_image = None

    if request.method == 'POST':          # If the form is submitted via POST
        file = request.files['file']      # Get uploaded file
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            prediction, confidence = predict_disease(filepath)    # Run prediction
            uploaded_image = filepath
# Render result page with prediction data
    return render_template('index.html',
                           prediction=prediction,
                           confidence=confidence,
                           uploaded_image=uploaded_image)

##----- Learn More page -----##
@app.route('/learn')
def learn():
    return render_template('learn.html')


if __name__ == '__main__':
    app.run(debug=True)
