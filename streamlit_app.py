# app.py
import streamlit as st
import joblib
import numpy as np

# Load model and label encoder
model = joblib.load("pokemon_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Pokémon Type Classifier", layout="centered")

st.title("🔮 Pokémon Type Classifier")
st.markdown("Enter Pokémon stats to predict its **Primary Type**:")

# Input form
with st.form("pokemon_form"):
    col1, col2 = st.columns(2)
    with col1:
        hp = st.number_input("HP", min_value=1, max_value=255, value=50)
        attack = st.number_input("Attack", min_value=1, max_value=255, value=50)
        defense = st.number_input("Defense", min_value=1, max_value=255, value=50)
        speed = st.number_input("Speed", min_value=1, max_value=255, value=50)
    with col2:
        special_attack = st.number_input("Special Attack", min_value=1, max_value=255, value=50)
        special_defense = st.number_input("Special Defense", min_value=1, max_value=255, value=50)
        base_experience = st.number_input("Base Experience", min_value=1, max_value=400, value=100)
        height = st.number_input("Height (dm)", min_value=1, max_value=100, value=10)
        weight = st.number_input("Weight (hg)", min_value=1, max_value=10000, value=100)

    submitted = st.form_submit_button("Predict Type")

if submitted:
    features = np.array([[hp, attack, defense, special_attack, special_defense, speed,
                          base_experience, height, weight]])
    prediction = model.predict(features)
    predicted_type = label_encoder.inverse_transform(prediction)[0]
    st.success(f"The predicted primary Pokémon type is: **{predicted_type.upper()}** 🔥")

