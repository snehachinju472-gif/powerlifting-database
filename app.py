import streamlit as st
import numpy as np
import pickle
import base64

# -----------------------------
# Background Image
# -----------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# add_bg_from_local("home.jpg")
# -----------------------------
# Load Model (No Scaler)
# -----------------------------
model = pickle.load(open("scaler.sav", "rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏠 Home Price Prediction App")

area = st.number_input("Enter Area (sq.ft)", min_value=100, max_value=10000, step=50)

if st.button("Predict Price"):
    prediction = model.predict([[area]])
    st.success(f"Estimated Price: $ {prediction[0]:,.2f}")
