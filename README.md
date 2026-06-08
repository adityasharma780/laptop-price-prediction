# 💻 Laptop Price Prediction using Machine Learning

## Live Demo

🚀 Try the application here:

https://laptop-price-prediction-zhcs33w8esgs96j6zbcrhq.streamlit.app/

---

# 📌 Project Overview

This project predicts the price of a laptop based on a small set of important specifications using Machine Learning.

Instead of requiring users to enter more than 20 technical specifications, the application uses only a few key features that have the greatest impact on laptop pricing. This makes the prediction process faster, simpler, and more user-friendly.

The project follows a complete Machine Learning workflow:

* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Preprocessing
* Model Training
* Model Evaluation
* Model Deployment using Streamlit

The final application allows users to enter laptop specifications through a web interface and receive an estimated laptop price instantly.

---

# 📊 Dataset Information

The dataset contains laptop specifications and their corresponding prices.

### Features Used for Prediction

| Feature        | Description                 |
| -------------- | --------------------------- |
| Company        | Laptop manufacturer         |
| TypeName       | Laptop category             |
| Ram            | RAM size (GB)               |
| PrimaryStorage | Storage capacity (GB)       |
| CPU_company    | Processor manufacturer      |
| CPU_freq       | Processor frequency (GHz)   |
| Inches         | Screen size                 |
| OS             | Operating System            |

### Target Variable

```text
Price_euros
```

To improve model performance and reduce skewness, the target variable was transformed using a logarithmic transformation before training.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle
* Git & GitHub

---

# 🔄 Project Workflow

## 1. Data Cleaning

Performed preprocessing and cleaning on the raw dataset.

Tasks included:

* Handling missing values
* Removing unnecessary columns
* Correcting data types
* Standardizing categorical values

---

## 2. Feature Engineering

Several useful features were extracted from the original dataset, including:

### CPU Features

* CPU_company
* CPU_model
* CPU_freq

### Storage Features

* PrimaryStorage
* SecondaryStorage
* PrimaryStorageType
* SecondaryStorageType

### Display Features

* Screen
* ScreenW
* ScreenH
* Touchscreen
* IPSpanel
* RetinaDisplay

### GPU Features

* GPU_company
* GPU_model

Although many engineered features were created, only the most impactful features were selected for the final deployed model to improve usability.

---

## 3. Data Preprocessing

Categorical features were encoded using:

```python
OneHotEncoder(handle_unknown="ignore")
```

A ColumnTransformer was used to apply transformations efficiently:

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

Using a fixed random state ensures reproducible results.

---

## 5. Machine Learning Model

The model used in this project is:

```python
LinearRegression()
```

A Pipeline was created to combine preprocessing and model training:

```python
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])
```

Benefits of Pipeline:

* Prevents data leakage
* Simplifies prediction workflow
* Automatically applies preprocessing before prediction

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

This improved model stability and prediction accuracy.

---

# 📈 Model Evaluation

### R² Score

```text
0.779
```

Meaning:

Approximately 77.9% of the variation in laptop prices is explained by the model.

### Mean Absolute Error (MAE)

```text
≈ 274 Euros
```

Meaning:

On average, the model's prediction differs from the actual laptop price by approximately €274.

The reduced-feature model was chosen to provide a better user experience while maintaining good predictive performance.

---

# 🌐 Streamlit Deployment

The project is deployed using Streamlit Cloud.

Features:

* Clean and user-friendly interface
* Minimal input requirements
* Real-time price prediction
* Instant prediction results

Users can estimate laptop prices using only six key specifications.

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
├── predict.py
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
* Model Comparison Dashboard
* Advanced Feature Selection
* Improved UI/UX
* Cloud Deployment Enhancements

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

**Aditya Sharma**

Machine Learning Project

Built using Python, Scikit-Learn, and Streamlit.

