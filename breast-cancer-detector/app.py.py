import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.title("🔬 Breast Cancer Detection App")
st.markdown("Enter the input values for 30 features to predict if the tumor is **Benign** or **Malignant**.")

# Feature names (based on breast cancer dataset)
features = [
    "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
    "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension",
    "radius error", "texture error", "perimeter error", "area error", "smoothness error",
    "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error",
    "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
    "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"
]

# Create 30 input fields
input_values = []
for feature in features:
    val = st.number_input(f"Enter {feature}", format="%.5f")
    input_values.append(val)

# Predict button
if st.button("Predict"):
    input_array = np.array(input_values).reshape(1, -1)
    prediction = model.predict(input_array)

    if prediction[0] == 0:
        st.error("🚨 The tumor is **Malignant**")
    else:
        st.success("✅ The tumor is **Benign**")
