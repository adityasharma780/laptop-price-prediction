# 💻 Laptop Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts the price of a laptop based on its specifications such as company, RAM, processor, storage, display characteristics, operating system, and GPU information.

The project follows a complete Machine Learning workflow:

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Preprocessing
* Model Training
* Model Evaluation
* Model Deployment using Streamlit

The final application allows users to enter laptop specifications through a web interface and receive an estimated laptop price.

---

# 📊 Dataset Information

The dataset contains laptop specifications and their corresponding prices.

### Features Used

| Feature              | Description                 |
| -------------------- | --------------------------- |
| Company              | Laptop manufacturer         |
| Product              | Laptop model name           |
| TypeName             | Laptop category             |
| Inches               | Screen size                 |
| Ram                  | RAM size (GB)               |
| OS                   | Operating System            |
| Weight               | Weight in kg                |
| Screen               | Screen quality/type         |
| ScreenW              | Screen width resolution     |
| ScreenH              | Screen height resolution    |
| Touchscreen          | Touchscreen availability    |
| IPSpanel             | IPS display availability    |
| RetinaDisplay        | Retina display availability |
| CPU_company          | Processor manufacturer      |
| CPU_freq             | Processor frequency         |
| CPU_model            | Processor model             |
| PrimaryStorage       | Primary storage capacity    |
| SecondaryStorage     | Secondary storage capacity  |
| PrimaryStorageType   | SSD/HDD/Hybrid etc.         |
| SecondaryStorageType | SSD/HDD/Hybrid etc.         |
| GPU_company          | Graphics card manufacturer  |
| GPU_model            | Graphics card model         |

### Target Variable

```text
Price_euros
```

The target variable was transformed using logarithmic transformation to reduce skewness and improve model performance.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

# 🔄 Project Workflow

## 1. Data Cleaning

Performed cleaning and preprocessing on the raw dataset.

Tasks included:

* Handling missing values
* Removing unnecessary columns
* Correcting data types
* Standardizing categorical values

---

## 2. Feature Engineering

Several useful features were extracted and transformed:

### Screen Features

Created:

* Screen
* ScreenW
* ScreenH
* Touchscreen
* IPSpanel
* RetinaDisplay

### CPU Features

Extracted:

* CPU_company
* CPU_model
* CPU_freq

### Storage Features

Created:

* PrimaryStorage
* SecondaryStorage
* PrimaryStorageType
* SecondaryStorageType

### GPU Features

Extracted:

* GPU_company
* GPU_model

---

## 3. Data Preprocessing

Categorical variables were encoded using:

```python
OneHotEncoder(handle_unknown="ignore")
```

A ColumnTransformer was used to apply encoding only on categorical columns.

```python
preprocessor = ColumnTransformer(
    transformers=[
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)
```

---

## 4. Train-Test Split

The dataset was divided into:

* 80% Training Data
* 20% Testing Data

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Using a fixed random_state ensures reproducible results.

---

## 5. Machine Learning Model

The model used in this project is:

```python
LinearRegression()
```

A Pipeline was created to combine preprocessing and model training.

```python
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])
```

Benefits of Pipeline:

* Prevents data leakage
* Simplifies prediction workflow
* Automatically applies transformations before prediction

---

## 6. Log Transformation

The target variable was highly skewed.

Therefore:

```python
y = np.log(y)
```

was applied before training.

Predictions were converted back using:

```python
np.exp(prediction)
```

This significantly improved model performance.

---

# 📈 Model Evaluation

Evaluation Metrics:

### R² Score

Measures how well the model explains variation in laptop prices.

Result:

```text
0.878
```

Meaning:

Approximately 87.8% of the variation in laptop prices is explained by the model.

### Mean Absolute Error (MAE)

Calculated after converting predictions back to actual prices.

Result:

```text
≈ 194 Euros
```

Meaning:

On average, the model's prediction differs from the actual laptop price by approximately €194.

---

# 🌐 Streamlit Deployment

A Streamlit web application was developed for deployment.

Features:

* User-friendly interface
* Dynamic dropdowns
* Real-time price prediction
* INR price display

Users can select laptop specifications and receive an estimated price instantly.

---

# 📂 Project Structure

```text
laptop-price-prediction/
│
├── app.py
├── pipe.pkl
├── cleaned_laptop.csv
├── requirements.txt
├── README.md
├── main.ipynb
│__predict.py
└── .gitignore
```

---

# 🚀 Running the Project Locally

## Clone Repository

```bash
git clone <repository-url>
```

## Move into Project Directory

```bash
cd laptop-price-prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

Possible enhancements:

* Random Forest Regression
* XGBoost Regression
* Hyperparameter Tuning
* Better UI Design
* Live Currency Conversion
* Cloud Deployment
* Model Comparison Dashboard

---

# 📚 Key Learnings

Through this project, I learned:

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* One-Hot Encoding
* ColumnTransformer
* Pipeline Creation
* Linear Regression
* Model Evaluation
* Streamlit Deployment
* Git and GitHub Workflow

---

# 👨‍💻 Author

Aditya Sharma

Machine Learning Beginner Project

Built using Python, Scikit-Learn, and Streamlit.
