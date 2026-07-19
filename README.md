# 🏠 California House Price Prediction

An end-to-end Machine Learning project that predicts house prices in California using demographic and housing-related features. This project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment.

---

## 📖 Project Overview

Accurately predicting house prices is an important problem in the real estate industry. This project uses the California Housing Dataset to build a regression model capable of estimating median house values based on various socio-economic and geographic features.

The project focuses on building an interpretable and production-ready machine learning pipeline rather than simply training a model.

---

## 🎯 Problem Statement

Develop a machine learning model capable of predicting the median house price in California districts using housing and demographic information.

The objective is to:

- Analyze housing data
- Perform feature engineering
- Train regression models
- Evaluate model performance
- Deploy the trained model

---

## 📊 Dataset

Dataset: California Housing Dataset

Features include:

- Median Income
- Housing Median Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude
- Ocean Proximity

Target Variable:

- Median House Value

---

## 🚀 Machine Learning Pipeline

### 1. Data Collection

- California Housing Dataset

### 2. Data Cleaning

- Missing value handling
- Data inspection
- Feature selection

### 3. Exploratory Data Analysis

- Distribution analysis
- Correlation analysis
- Feature relationships
- Data visualization

### 4. Feature Engineering

Created additional features such as:

- Rooms per Household
- Bedrooms per Room
- Population per Household

### 5. Data Preprocessing

- One-Hot Encoding
- Feature Scaling (where required)
- Train-Test Split

### 6. Model Training

Regression models were trained and evaluated to determine the best-performing model.

### 7. Model Evaluation

Evaluation metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📈 Model Performance

| Metric | Value |
|---------|--------|
| MAE | ~32,328 |
| RMSE | ~50,356 |
| R² Score | ~0.81 |

---

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit (Deployment)

---




## 📷 Exploratory Data Analysis

The project includes multiple visualizations including:

- Correlation Heatmap
- Feature Distributions
- Scatter Plots
- Pair Plots
- Histograms

These visualizations help understand feature relationships and identify patterns affecting house prices.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move into the project directory

```bash
cd House-Price-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

- Hyperparameter Optimization
- XGBoost Regression
- Random Forest Regression
- Cross Validation
- Model Explainability using SHAP
- Docker Deployment
- CI/CD Integration
- Cloud Deployment (AWS/Azure)

---

## 📚 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Regression
- Model Evaluation
- Machine Learning Pipeline
- Data Visualization
- Model Deployment
- Python Development

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building an end-to-end machine learning pipeline
- Feature engineering and preprocessing
- Training and evaluating regression models
- Interpreting model performance metrics
- Deploying ML applications using Streamlit
- Applying best practices for project organization and documentation

---

## 👨‍💻 Author

**Atharv Singh**

B.Tech Computer Science Engineering



LinkedIn: https://www.linkedin.com/in/atharv-s-324102318/

---

⭐ If you found this project useful, consider giving it a star!
