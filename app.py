import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Define class labels
class_labels = {
    0: 'Adenocarcinoma',
    1: 'Large Cell Carcinoma',
    2: 'Normal Cell',
    3: 'Squamous Cell Carcinoma'
}

# Load the trained model
model = tf.keras.models.load_model('chest_cancer_detector.h5')

# Function to preprocess and make predictions
def predict(uploaded_image):
    # Preprocess the uploaded image
    img = image.load_img(uploaded_image, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # Make a prediction
    prediction = model.predict(img)
    return prediction

# Streamlit app
st.title('Chest Cancer Classification App')
st.write('Upload an image for classification.')

# Upload image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    st.write('')
    st.write('Classifying...')

    # Make a prediction
    prediction = predict(uploaded_image)

    # Get the predicted class label
    predicted_class = np.argmax(prediction)

    # Display the predicted class label
    st.success(f'Predicted Class: {class_labels[predicted_class]}')
