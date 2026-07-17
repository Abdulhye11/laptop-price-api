import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("laptop_price_model.pkl")

st.set_page_config(page_title="Laptop Price Predictor", layout="wide")

st.title("💻 Laptop Price Prediction")
st.write("Enter the laptop details and click Predict.")

brand = st.text_input("Brand")
model_name = st.text_input("Model")
processor = st.text_input("Processor")
processor_family = st.text_input("Processor Family")

ram = st.number_input("RAM (GB)", min_value=1, value=8)

storage_type = st.selectbox(
    "Storage Type",
    ["SSD", "HDD", "NVMe SSD", "eMMC"]
)

storage = st.number_input("Storage (GB)", min_value=64, value=512)

screen = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=20.0,
    value=15.6
)

gpu = st.text_input("GPU")

year = st.number_input(
    "Year",
    min_value=2010,
    max_value=2035,
    value=2022
)

condition = st.selectbox(
    "Condition",
    ["New", "Used", "Refurbished"]
)

battery = st.slider(
    "Battery Health %",
    0,
    100,
    90
)

warranty = st.number_input(
    "Warranty (Months)",
    min_value=0,
    max_value=60,
    value=6
)

city = st.text_input("City")

if st.button("Predict Price"):

    data = pd.DataFrame({
        "Brand":[brand],
        "Model":[model_name],
        "Processor":[processor],
        "Processor_Family":[processor_family],
        "RAM_GB":[ram],
        "Storage_Type":[storage_type],
        "Storage_GB":[storage],
        "Screen_Size_Inches":[screen],
        "GPU":[gpu],
        "Year":[year],
        "Condition":[condition],
        "Battery_Health_Percent":[battery],
        "Warranty_Months":[warranty],
        "City":[city]
    })

    prediction = model.predict(data)

    st.success(f"Estimated Price: PKR {prediction[0]:,.0f}")
