import pickle
import pandas as pd
import numpy as np

# Load model
model = pickle.load(open("pipe.pkl", "rb"))

# Laptop specification
sample = pd.DataFrame({
    'Company': ['Dell'],
    'Product': ['Inspiron'],
    'TypeName': ['Notebook'],
    'Inches': [15.6],
    'Ram': [8],
    'OS': ['Windows 10'],
    'Weight': [2.0],
    'Screen': ['Full HD'],
    'ScreenW': [1920],
    'ScreenH': [1080],
    'Touchscreen': ['No'],
    'IPSpanel': ['Yes'],
    'RetinaDisplay': ['No'],
    'CPU_company': ['Intel'],
    'CPU_freq': [2.5],
    'CPU_model': ['Core i5'],
    'PrimaryStorage': [256],
    'SecondaryStorage': [0],
    'PrimaryStorageType': ['SSD'],
    'SecondaryStorageType': ['No'],
    'GPU_company': ['Intel'],
    'GPU_model': ['HD Graphics 620']
})

# Predict
log_price = model.predict(sample)

# Convert back from log(price)
price = np.exp(log_price)

print("Predicted Price:", round(price[0], 2))