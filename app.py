import streamlit as st
import pickle
import pandas as pd
import numpy as np

# =========================
# Load Model and Dataset
# =========================

model = pickle.load(open("pipe.pkl", "rb"))
df = pd.read_csv("cleaned_laptop.csv")

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

# =========================
# Title
# =========================

st.title("💻 Laptop Price Predictor")
st.write("Enter laptop specifications to estimate its price.")

st.markdown("---")

# =========================
# Input Fields
# =========================

company = st.selectbox(
    "🏢 Company",
    sorted(df["Company"].unique())
)

type_name = st.selectbox(
    "📂 Laptop Type",
    sorted(df["TypeName"].unique())
)

ram = st.selectbox(
    "🧠 RAM (GB)",
    sorted(df["Ram"].unique())
)

primary_storage = st.selectbox(
    "💾 Storage (GB)",
    sorted(df["PrimaryStorage"].unique())
)

cpu_company = st.selectbox(
    "⚙️ Processor Brand",
    sorted(df["CPU_company"].unique())
)

cpu_freq = st.number_input(
    "🚀 CPU Frequency (GHz)",
    min_value=1.0,
    max_value=5.0,
    value=2.5,
    step=0.1
)

inches = st.slider(
    "🖥️ Screen Size (Inches)",
    min_value=10.0,
    max_value=18.0,
    value=15.6,
    step=0.1
)

os = st.selectbox(
    "💿 Operating System",
    sorted(df["OS"].unique())
)

st.markdown("---")

# =========================
# Prediction
# =========================

if st.button("🔍 Predict Price"):

    sample = pd.DataFrame({
        "Company": [company],
        "TypeName": [type_name],
        "Ram": [ram],
        "PrimaryStorage": [primary_storage],
        "CPU_company": [cpu_company],
        "CPU_freq": [cpu_freq],
        "Inches": [inches],
        "OS": [os]
    })

    try:
        # Predict log(price)
        prediction_log = model.predict(sample)

        # Convert back to actual price
        prediction_price = np.exp(prediction_log)

        # Convert Euro to INR
        price_inr = prediction_price[0] * 95

        st.success(
            f"💰 Estimated Laptop Price: ₹{price_inr:,.0f}"
        )

        st.info(
            f"Approximate Price in Euros: €{prediction_price[0]:,.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# =========================
# Footer
# =========================

st.markdown("---")
st.caption("Built with Python, Scikit-Learn and Streamlit")