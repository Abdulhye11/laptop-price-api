import streamlit as st
import pandas as pd
import joblib


# Load trained pipeline
model = joblib.load("laptop_price_model.pkl")


st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻"
)


st.title("💻 Laptop Price Prediction")
st.write(
    "Enter laptop specifications to estimate the market price in PKR"
)


# User inputs

brand = st.selectbox(
    "Brand",
    [
        "Dell",
        "HP",
        "Lenovo",
        "Apple",
        "Acer",
        "Asus"
    ]
)


model_name = st.text_input(
    "Model",
    "Latitude"
)


processor = st.text_input(
    "Processor",
    "Intel Core i5"
)


processor_family = st.text_input(
    "Processor Family",
    "Core i5"
)


ram = st.number_input(
    "RAM (GB)",
    4,
    64,
    16
)


storage_type = st.selectbox(
    "Storage Type",
    ["SSD", "HDD"]
)


storage = st.number_input(
    "Storage (GB)",
    128,
    2048,
    512
)


screen = st.number_input(
    "Screen Size (Inches)",
    10.0,
    18.0,
    15.6
)


gpu = st.text_input(
    "GPU",
    "Integrated"
)


year = st.number_input(
    "Manufacturing Year",
    2010,
    2026,
    2022
)


condition = st.selectbox(
    "Condition",
    [
        "New",
        "Used",
        "Refurbished"
    ]
)


battery = st.number_input(
    "Battery Health %",
    0,
    100,
    90
)


warranty = st.number_input(
    "Warranty Months",
    0,
    36,
    6
)


city = st.text_input(
    "City",
    "Islamabad"
)


# Feature engineering
laptop_age = 2026 - year


if ram <= 4:
    ram_category = "Low"
elif ram <= 16:
    ram_category = "Medium"
else:
    ram_category = "High"


if storage <= 256:
    storage_category = "Small"
elif storage <= 512:
    storage_category = "Medium"
else:
    storage_category = "Large"


has_warranty = 1 if warranty > 0 else 0


# Prediction

if st.button("Predict Price"):

    input_data = pd.DataFrame({

        "Brand": [brand],
        "Model": [model_name],
        "Processor": [processor],
        "Processor_Family": [processor_family],
        "RAM_GB": [ram],
        "Storage_Type": [storage_type],
        "Storage_GB": [storage],
        "Screen_Size_Inches": [screen],
        "GPU": [gpu],
        "Year": [year],
        "Condition": [condition],
        "Battery_Health_Percent": [battery],
        "Warranty_Months": [warranty],
        "City": [city],
        "Laptop_Age": [laptop_age],
        "RAM_Category": [ram_category],
        "Storage_Category": [storage_category],
        "Has_Warranty": [has_warranty]

    })


    prediction = model.predict(input_data)


    st.success(
        f"Estimated Laptop Price: PKR {prediction[0]:,.0f}"
    )
