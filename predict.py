import pickle
import pandas as pd
import numpy as np

# Load model
model = pickle.load(open("pipe.pkl", "rb"))

# Laptop specification
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

# Predict
log_price = model.predict(sample)

# Convert back from log(price)
price = np.exp(log_price)

print("Predicted Price:", round(price[0], 2))