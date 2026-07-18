import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("laptop_price_model.pkl")

st.title("Laptop Price Prediction")

st.write("Enter laptop details")

brand = st.selectbox(
    "Brand",
    ["Dell", "HP", "Lenovo", "Apple"]
)

ram = st.number_input(
    "RAM (GB)",
    min_value=2,
    max_value=64,
    value=8
)

storage = st.number_input(
    "Storage (GB)",
    min_value=64,
    max_value=2048,
    value=512
)

# Create input dataframe
input_data = pd.DataFrame({
    "Brand": [brand],
    "Model": ["Unknown"],
    "Processor": ["Unknown"],
    "Processor_Family": ["Unknown"],
    "RAM_GB": [ram],
    "Storage_Type": ["SSD"],
    "Storage_GB": [storage],
    "Screen_Size_Inches": [15.6],
    "GPU": ["Integrated"],
    "Year": [2023],
    "Condition": ["Used"],
    "Battery_Health_Percent": [90],
    "Warranty_Months": [6],
    "City": ["Islamabad"],
    "Laptop_Age": [3],
    "RAM_Category": ["Medium"],
    "Storage_Category": ["Medium"],
    "Has_Warranty": [1]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)

    st.success(
        f"Estimated Price: PKR {prediction[0]:,.0f}"
    )
