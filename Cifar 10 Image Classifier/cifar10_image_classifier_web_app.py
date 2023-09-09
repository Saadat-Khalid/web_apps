import streamlit as st
import cv2 as cv
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    /* Style the quote container */
    .quote-container {
        background-color: #f4f4f4;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
    }

    /* Style the quote text */
    .quote-text {
        font-size: 24px;
        font-style: italic;
        text-align: center;
    }

    /* Style the quote author */
    .quote-author {
        margin-top: 10px;
        font-size: 18px;
        text-align: right;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load your trained model
model = load_model('cifar10_image_classifier.h5')  # path to your trained model

# Define class names
class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

def classify_image(uploaded_image):
    # Read the uploaded image as bytes
    image_bytes = uploaded_image.read()

    # Convert the bytes to a NumPy array
    image_np = np.asarray(bytearray(image_bytes), dtype=np.uint8)

    # Decode the image as an OpenCV image (BGR format)
    image_cv = cv.imdecode(image_np, cv.IMREAD_COLOR)

    # Resize the image to match the input shape of your model (32x32 pixels)
    resized_image = cv.resize(image_cv, (32, 32))
    resized_image = np.expand_dims(resized_image, axis=0)  # Add batch dimension

    # Normalize the image
    normalized_image = resized_image / 255.0

    # Make predictions
    predictions = model.predict(normalized_image)
    class_index = np.argmax(predictions)

    return class_names[class_index], predictions[0]

# Streamlit app
st.title('Image Classification App')
st.write('Upload an image and let the model classify it.')

uploaded_image = st.file_uploader('Upload an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    class_name, predictions = classify_image(uploaded_image)
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    
    if st.button('Classify'):
        st.header(f'Predicted Class: {class_name}')
        st.write('Class Probabilities:')
        for i, prob in enumerate(predictions):
            st.write(f'{class_names[i]}: {prob:.2f}')

## About ME:
st.header("About ME:")
st.write("Hi there, I'm Saadat Khalid Awan 👋")
st.write("`Aspiring Data Scientist | Problem Solver | Lifelong Learner`")
st.write("I'm a software engineer with a keen interest in data science. I hold a BS degree in Software Engineering and am currently learning about the field of data science.")

st.write("Submission Date: September 9, 2023")

# Social Media Links
st.header("Let's Connect:")
st.markdown(
    "[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/Saadat.Khalid.Awan) "
    "[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/saadii_awan66) "
    "[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/saadatawan) "
    "[![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@@me.saadat) "
    "[![Pinterest](https://img.shields.io/badge/Pinterest-%23E60023.svg?logo=Pinterest&logoColor=white)](https://pinterest.com/its_saadatkhalid) "
    "[![Quora](https://img.shields.io/badge/Quora-%23B92B27.svg?logo=Quora&logoColor=white)](https://quora.com/profile/Saadat-Khalid-Awan) "
    "[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?logo=TikTok&logoColor=white)](https://tiktok.com/@@saadat.awan) "
    "[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/saadat_96) "
    "[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@saadatkhalidawan) "
    "[![Github](https://img.shields.io/badge/Github-%23FF0000.svg?logo=Github&logoColor=Black)](https://github.com/Saadat-Khalid/)"
)
