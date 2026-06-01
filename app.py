import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and dataset
model = pickle.load(open("pipe.pkl", "rb"))
df = pd.read_csv("cleaned_laptop.csv")

st.set_page_config(page_title="Laptop Price Predictor")

st.title("💻 Laptop Price Predictor")

# =========================
# Basic Information
# =========================

company = st.selectbox(
    "Company",
    sorted(df["Company"].unique())
)

product = st.selectbox(
    "Product",
    sorted(df["Product"].unique())
)

type_name = st.selectbox(
    "Type",
    sorted(df["TypeName"].unique())
)

inches = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=20.0,
    step=0.1
)

ram = st.number_input(
    "RAM (GB)",
    min_value=2,
    max_value=64,
    step=2
)

# =========================
# Operating System
# =========================

os = st.selectbox(
    "Operating System",
    sorted(df["OS"].unique())
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.5,
    max_value=5.0,
    step=0.1
)

# =========================
# Display Information
# =========================

screen = st.selectbox(
    "Screen Type",
    sorted(df["Screen"].unique())
)

screen_w = st.number_input(
    "Screen Width",
    min_value=800,
    max_value=5000,
    step=1
)

screen_h = st.number_input(
    "Screen Height",
    min_value=600,
    max_value=3000,
    step=1
)

touchscreen = st.selectbox(
    "Touchscreen",
    ["Yes", "No"]
)

ips_panel = st.selectbox(
    "IPS Panel",
    ["Yes", "No"]
)

retina_display = st.selectbox(
    "Retina Display",
    ["Yes", "No"]
)

# =========================
# CPU Information
# =========================

cpu_company = st.selectbox(
    "CPU Company",
    sorted(df["CPU_company"].unique())
)

cpu_freq = st.number_input(
    "CPU Frequency (GHz)",
    min_value=1.0,
    max_value=5.0,
    step=0.1
)

cpu_model = st.selectbox(
    "CPU Model",
    sorted(df["CPU_model"].unique())
)

# =========================
# Storage Information
# =========================

primary_storage = st.number_input(
    "Primary Storage (GB)",
    min_value=0,
    max_value=5000,
    step=32
)

secondary_storage = st.number_input(
    "Secondary Storage (GB)",
    min_value=0,
    max_value=5000,
    step=32
)

primary_storage_type = st.selectbox(
    "Primary Storage Type",
    sorted(df["PrimaryStorageType"].unique())
)

secondary_storage_type = st.selectbox(
    "Secondary Storage Type",
    sorted(df["SecondaryStorageType"].unique())
)

# =========================
# GPU Information
# =========================

gpu_company = st.selectbox(
    "GPU Company",
    sorted(df["GPU_company"].unique())
)

gpu_model = st.selectbox(
    "GPU Model",
    sorted(df["GPU_model"].unique())
)

# =========================
# Prediction
# =========================

if st.button("Predict Price"):

    sample = pd.DataFrame({
        'Company': [company],
        'Product': [product],
        'TypeName': [type_name],
        'Inches': [inches],
        'Ram': [ram],
        'OS': [os],
        'Weight': [weight],
        'Screen': [screen],
        'ScreenW': [screen_w],
        'ScreenH': [screen_h],
        'Touchscreen': [touchscreen],
        'IPSpanel': [ips_panel],
        'RetinaDisplay': [retina_display],
        'CPU_company': [cpu_company],
        'CPU_freq': [cpu_freq],
        'CPU_model': [cpu_model],
        'PrimaryStorage': [primary_storage],
        'SecondaryStorage': [secondary_storage],
        'PrimaryStorageType': [primary_storage_type],
        'SecondaryStorageType': [secondary_storage_type],
        'GPU_company': [gpu_company],
        'GPU_model': [gpu_model]
    })

    try:
        prediction_log = model.predict(sample)
        prediction_price = np.exp(prediction_log)

        st.success(
            f"Predicted Laptop Price: Rs{prediction_price[0] * 95:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")