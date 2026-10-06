import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the model and scaler
model = joblib.load("naegleria_rf_model.joblib")
scaler = joblib.load("naegleria_scaler.joblib")

# Streamlit UI
st.set_page_config(page_title="Aqua Safe ", layout="centered")
st.title("🦠 Aqua Safe")
st.write("Adjust the sliders and options to dynamically calculate the risk of Naegleria fowleri.")

# Input fields with real-time updates
with st.form("risk_form"):
    water_source = st.selectbox("Water Source Type", ["River", "Pond", "Lake", "Well", "Tap", "Other"])
    contaminant = st.slider("Chlorine content (ppm)", 0.0, 50.0, 5.0, step=0.1)
    turbidity = st.slider("Turbidity (NTU)", 0.0, 100.0, 5.0, step=0.1)
    dissolved_oxygen = st.slider("Dissolved Oxygen (mg/L)", 0.0, 15.0, 7.0, step=0.1)
    nitrate = st.slider("Nitrate Level (mg/L)", 0.0, 50.0, 10.0, step=0.1)
    temperature = st.slider("Temperature (°C)", 0.0, 60.0, 30.0, step=0.1)
    submit = st.form_submit_button("Predict Risk")

if submit:
    # One-hot encode water source (drop_first=True)
    water_source_features = ["Water Source Type_Lake", "Water Source Type_Pond", "Water Source Type_Tap", "Water Source Type_Well", "Water Source Type_Other"]
    water_source_encoded = [1 if water_source in col else 0 for col in water_source_features]

    # Prepare feature vector
    features = np.array([[contaminant, turbidity, dissolved_oxygen, nitrate, temperature] + water_source_encoded])
    scaled_features = scaler.transform(features)

    # Prediction
    prediction_proba = model.predict_proba(scaled_features)[0][1]  # probability of class 1 (high risk)
    prediction = model.predict(scaled_features)[0]
    risk_percentage = round(prediction_proba * 100, 2)

    if prediction == 1:
        st.error(f"⚠️ High Risk of Naegleria fowleri ({risk_percentage}%)")
        st.markdown("### Precautions:")
        st.markdown("- Avoid swimming in warm freshwater bodies like lakes or ponds.")
        st.markdown("- Use nose clips or keep your head above water while swimming.")
        st.markdown("- Ensure water used in neti pots or nasal rinsing is distilled, sterile, or boiled.")
        st.markdown("- Avoid disturbing sediment in shallow, warm freshwater areas.")
        st.markdown("- Educate the community on early symptoms and risks of exposure.")
        
    else:
        st.success(f"✅ Low Risk of Naegleria fowleri ({risk_percentage}%)")
        st.markdown("- Continue monitoring water quality regularly.")
        st.markdown("- Maintain safe recreational practices in freshwater environments.")

# Footer
st.markdown("---")
st.caption("Developed as a machine learning project using Streamlit")