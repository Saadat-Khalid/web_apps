import streamlit as st
import joblib
import pandas as pd

# Load the preprocessor and best model
preprocessor = joblib.load('https://github.com/Saadat-Khalid/web_apps/blob/d80e7d776b228f9e2d4a227f6553095214dbf7d9/laptop_price_prediction_app/preprocessor.pkl')
best_model = joblib.load('best_model.pkl')

# # Load the name of the best model
# with open('best_model_name.txt', 'r') as f:
#     best_model_name = f.read().strip()

# Load your dataset
df = pd.read_csv('data.csv')

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
st.title("💻 Laptop Price Predictor")
st.subheader("Enter laptop details to get predicted price")
st.set_page_config(page_title="💻 Laptop Price Predictor")

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

# Define the footer
def footer():
  footer_text = [
      "Made with Streamlit by Saadat Khalid ",
      "Connect with me on:",
      f"[Kaggle](https://www.kaggle.com/saadatkhalid)  [![Kaggle](https://iconail.com/icons/kaggle-flat.png)]",
      f"[LinkedIn](https://www.linkedin.com/in/saadatawan/)  [![LinkedIn](https://cdn-icons-png.flaticon.com/v8/static/svg/media/fi-rr-brands/fi-rr-linkedin.svg)]",
  ]
  st.write('<br/>'.join(footer_text), unsafe_allow_html=True)

# Call the footer function at the end of your app
footer()
