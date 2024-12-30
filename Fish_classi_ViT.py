import streamlit as st
import requests
from PIL import Image

# Streamlit App
st.title("Fish Species Classification")

# Image uploader
uploaded_file = st.file_uploader("Upload an image of a fish", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Send image to Flask API for prediction
    with st.spinner('Predicting...'):
        try:
            response = requests.post(
                "http://127.0.0.1:5001/predict",  # Flask API URL
                files={'file': uploaded_file.getvalue()}
            )
            data = response.json()

            if 'prediction' in data:
                st.success(f"Prediction: {data['prediction']}")
            else:
                st.error(f"Error: {data['error']}")
        except Exception as e:
            st.error(f"Failed to connect to the prediction server: {e}")
