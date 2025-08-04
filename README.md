## Shurida-21047377-DSP-PROJECT

## Human Skin Disease Detection Using Image Classification

![logo](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/logo.png)


------------------------------------------------

### Contents:

- README.md → Full documentation of this project

- SkinAid WebApp/ → All files used for building the Web Application

- SkinAid CNN Model/ → The.ipynb file used for training the model in Google Colab

- resources/ → All images and videos for demonstration (including screenshots and recordings) & presentation/ → PowerPoint/OBS assets

--------------------------------------------------
--------------------------------------------------

### Overview:

This project implements a **deep learning-based system** to assist in detecting human skin diseases through **image classification**. 
Using a **Convolutional Neural Network (CNN) model**, users can upload an image of a skin lesion and receive **real-time predictions** along with **confidence scores**.
The system is designed for general users and healthcare professionals, especially in remote or under-resourced areas.

-------------------------------------------------

##### FILE STRUCTURE OF THE WEB-APP

```
├── app.py             # Flask app
├── model/             
│   └── skin_disease_model.keras    # Trained CNN model
├── static/            
│   └── styles.css     # CSS styling
├── templates/         
│   ├── home.html    # Landing page
│   └── index.html    # Result display page
    └── learn.html    # Extra information about the diseases 

```


-------------------------------------------------

### Features

- **Upload** a skin lesion image via a simple web interface.

- **CNN Model** classifies the image into disease categories (for example- melanoma, benign keratosis).

- **Real-time Prediction** with confidence scores.

- **Privacy first** Uploaded images are not stored.

- **Decision Support Only** The system assists in diagnosis but does not replace professional medical advice.

-------------------------------------------------

### System Architecture

**Frontend:** HTML, CSS (Flask templates)

**Backend:** Flask (Python)

**Model Training:** Colab (Keras/TensorFlow CNN)

**Model Deployment:** Pretrained .h5 model loaded into Flask for prediction.

-------------------------------------------------

### Flask Routes

| Route | Method | Description |
|------- | -------| -------------|
| `/` | GET | Home page (upload form) |
| `/upload` | POST | Handle image upload and prediction |
| `/predict` | POST | Process image, predict, return JSON |


-------------------------------------------------

### Project design

###### 1. USE CASE DIAGRAM

The use case diagram describes the interaction between the system and external actors (the user). It highlights how users upload images, trigger classification, and receive diagnostic feedback.

```
          +-----------+
          |   User    |
          +-----------+
                |
                | Upload Image
                v
        +------------------+
        |  Web Interface   |
        +------------------+
                |
                | Sends image
                v
        +------------------+
        |  CNN Model       |
        +------------------+
                |
                | Returns classification
                v
        +------------------+
        |  Display Results |
        +------------------+
```

###### 2. HIGH LEVEL SYSTEM ARCHITECTURE

This architecture breaks the project into its main subsystems.

```
+-------------------------+        +--------------------------+
|  User Interface (Web)   |<-----> |   Flask API Backend      |
|  - Upload form          |        |  - Route handling        |
|  - Results display      |        |  - Image preprocessing   |
+-------------------------+        |  - Calls CNN model       |
                                   +-----------+--------------+
                                               |
                                               v
                                   +--------------------------+
                                   |     Trained CNN Model    |
                                   |  - Image classification  |
                                   |  - Returns prediction    |
                                   +--------------------------+
```

###### 3. CLASS DIAGRAM (Simplified)

Shows the core components in object-oriented terms.

```
+------------------------+
|   SkinImage            |
+------------------------+
| - file_path            |
| - label (optional)     |
+------------------------+
| + preprocess()         |
| + resize()             |
+------------------------+

+------------------------+
|   ClassifierModel      |
+------------------------+
| - model_path           |
| - model_object         |
+------------------------+
| + load_model()         |
| + predict(image)       |
| + evaluate()           |
+------------------------+

+------------------------+
|   ResultDisplay        |
+------------------------+
| - prediction           |
| - confidence_score     |
+------------------------+
| + format_output()      |
+------------------------+
```

###### 4. FLOW DIAGRAM (SYSTEM WORKFLOW)

```
User Uploads Image
        ↓
Image Preprocessed (Resize, Normalize)
        ↓
Image Passed to CNN Model
        ↓
CNN Predicts Disease & Confidence
        ↓
Result Sent to Flask Backend
        ↓
Displayed on Web Interface
```

###### 5. UI DESIGN (WIREFRAME)

Basic mock layout using Canva.

![Wireframe Flowchart Whiteboard](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/Wireframe_Flowchart_Whiteboard.png)


-------------------------------------------------

### Requirements

- Python 3.x

- Flask

- TensorFlow / Keras

Activating the virtual environment:

```
venv\Scripts\activate    
```

Run the Flask server:

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

### Screenshots

![36](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/36.png)

![28](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/28.png)

![29](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/29.png)



### ***Disclaimer***

This project is for educational and research purposes only. It is not intended to replace professional medical diagnosis.

### Demo of the Web-Application

![SkinAid-Shurida](https://gitlab.uwe.ac.uk/s2-binterashed/shurida-dsp-project/-/raw/main/resources/presentation/SkinAid-Shurida.mp4)


