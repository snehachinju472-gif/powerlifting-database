import streamlit as st
import pandas as pd
import joblib

# Load
model = joblib.load("mental_health_model.pkl")
feature_columns = joblib.load("train_feature_columns.pkl")

st.title("Mental Health Prediction")

# Inputs
age = st.number_input("Age", 1, 100)
gender = st.selectbox("Gender", [0, 1])
stress = st.slider("Stress Level", 0, 10)

# Create dataframe
input_data = {
    "Age": age,
    "Gender": gender,
    "Stress": stress
}

input_df = pd.DataFrame([input_data])

# Match columns
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")