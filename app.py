import os
import streamlit as st
import joblib

MODEL_PATH = "laptop_price_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()
