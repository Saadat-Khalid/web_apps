import streamlit as st
import joblib
import pandas as pd

# from pathlib import Path
# st.text(Path.cwd()) 

# Load the preprocessor and best model
preprocessor = joblib.load('laptop_price_prediction_app/preprocessor.pkl')
best_model = joblib.load('laptop_price_prediction_app/best_model.pkl')

# Load your dataset
df = pd.read_csv('laptop_price_prediction_app/data.csv')

# Drop 'spec_rating' and 'price' columns
X = df.drop(columns=['spec_rating', 'price'])

# Define the unique values for each feature
unique_values = {}
for col in X.columns:
    unique_values[col] = X[col].unique().tolist()

# Define the predict_laptop_price function
def predict_laptop_price(brand, name, cpu, processor, ram, ram_type, storage, storage_type, gpu, display_size, resolution_width, resolution_height, os, warranty):
    input_data = pd.DataFrame({
        'brand': [brand],
        'name': [name],
        'processor': [processor],
        'CPU': [cpu],
        'Ram': [ram],
        'Ram_type': [ram_type],
        'ROM': [storage],
        'ROM_type': [storage_type],
        'GPU': [gpu],
        'display_size': [display_size],
        'resolution_width': [resolution_width],
        'resolution_height': [resolution_height],
        'OS': [os],
        'warranty': [warranty]
    })

    input_data_transformed = preprocessor.transform(input_data)
    price_prediction = best_model.predict(input_data_transformed)[0]

    return price_prediction

# Set up the Streamlit app
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻")
st.title("💻 Laptop Price Predictor")
st.subheader("Enter laptop details to get predicted price")

# Define the input fields
with st.sidebar:
    st.header("Input Features")
    brand = st.selectbox("Select Brand", unique_values['brand'])
    name = st.selectbox("Enter Laptop Name", unique_values['name'])
    processor = st.selectbox("Select Processor", unique_values['processor'])
    cpu = st.selectbox("Select CPU", unique_values['CPU'])
    ram = st.selectbox("Select RAM", unique_values['Ram'])
    ram_type = st.selectbox("Select RAM Type", unique_values['Ram_type'])
    storage = st.selectbox("Select Storage", unique_values['ROM'])
    storage_type = st.selectbox("Select Storage Type", unique_values['ROM_type'])
    gpu = st.selectbox("Select GPU", unique_values['GPU'])
    display_size = st.selectbox("Select Display Size", unique_values['display_size'])
    resolution_width = st.number_input("Enter Resolution Width", min_value=float(min(unique_values['resolution_width'])), step=1.0)
    resolution_height = st.number_input("Enter Resolution Height", min_value=float(min(unique_values['resolution_height'])), step=1.0)
    os = st.selectbox("Select Operating System", unique_values['OS'])
    warranty = st.selectbox("Select Warranty", unique_values['warranty'])

# Predict the laptop price
if st.button("Predict Laptop Price"):
    results = predict_laptop_price(
        brand, name, cpu, processor, ram, ram_type, storage, storage_type, gpu, display_size, resolution_width, resolution_height, os, warranty
    )
    st.write(f"Predicted Laptop Price: ₹{results:.2f}")
    st.write(f"Predicted Laptop Price: ${results*0.012:.2f}")

## About ME:
st.header("About ME:")
st.write("Hi there, I'm Saadat Khalid Awan 👋")
st.write("`Aspiring Data Scientist`")
st.write("I'm a software engineer with a keen interest in data science. I hold a BS degree in Software Engineering and am currently learning about the field of data science.")

st.write("Submission Date: June 08, 2024")

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
