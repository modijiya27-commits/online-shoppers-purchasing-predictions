# 🛒 Online Shoppers Purchase Prediction

An end-to-end Machine Learning project that predicts whether an online visitor is likely to make a purchase based on their browsing behavior.

This project covers the complete ML workflow—from data preprocessing and feature engineering to model training, evaluation, and deployment using Streamlit.

---

## 🌐 Live Demo

🔗 https://online-shoppers-purchasing-predictions-hmnmujywfndmj6kfckhgpd.streamlit.app/

---

## 📌 Project Overview

Online retailers generate large amounts of customer browsing data. Predicting whether a visitor will make a purchase helps businesses optimize marketing campaigns, improve user experience, and increase conversion rates.

In this project, a Random Forest Classifier was trained on the Online Shoppers Purchasing Intention dataset to classify whether a visitor is likely to complete a purchase.

---

## 🎯 Objectives

- Understand customer browsing behavior
- Predict purchase intent using Machine Learning
- Compare multiple classification models
- Perform feature engineering
- Deploy the trained model as an interactive web application

---

## 📊 Dataset

**Dataset:** Online Shoppers Purchasing Intention Dataset

The dataset contains user browsing session information such as:

- Administrative Pages
- Informational Pages
- Product Related Pages
- Bounce Rate
- Exit Rate
- Page Value
- Special Day
- Operating System
- Browser
- Region
- Traffic Source
- Visitor Type
- Month
- Weekend
- Revenue (Target Variable)

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## ⚙ Machine Learning Workflow

### Data Preprocessing

- Missing Value Handling
- One-Hot Encoding
- Feature Selection
- Train-Test Split

### Feature Engineering

- Created meaningful derived features
- Compared model performance before and after feature engineering

### Models Implemented

- Logistic Regression (Baseline Model)
- Random Forest Classifier (Final Model)

### Model Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- Cross Validation

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | ~89.75% |
| Random Forest | ~90.21% |

Random Forest achieved better predictive performance and was selected for deployment.

---

## 🚀 Streamlit Application

The deployed application allows users to:

- Enter customer browsing details
- Predict purchase probability
- View purchase intent
- Review entered input data

---

## 📂 Project Structure

```text
Online_Shoppers_Purchase_Prediction/
│
├── app.py
├── purchase_prediction_model.pkl
├── requirements.txt
├── README.md
├── End_to_End_ML.ipynb
└── online_shoppers_intention.csv
```

---

## ▶ How to Run Locally

### Clone the repository

```bash
git clone https://github.com/yourusername/Online_Shoppers_Purchase_Prediction.git
```

### Navigate to the project

```bash
cd Online_Shoppers_Purchase_Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

## 📷 Application Preview

> Add screenshots of your Streamlit application here.

---

## 💡 Business Insights

- Returning visitors generally have a higher likelihood of making purchases.
- Product-related engagement is one of the strongest indicators of buying intent.
- High bounce and exit rates reduce purchase probability.
- Customer browsing patterns can help businesses optimize marketing campaigns and improve conversion rates.

---

## 📚 Key Learnings

- End-to-End Machine Learning Pipeline
- Feature Engineering
- Classification Model Comparison
- Random Forest Implementation
- Model Evaluation Techniques
- Model Serialization using Joblib
- Streamlit Deployment
- Building Interactive ML Applications

---

## 🔮 Future Improvements

- Hyperparameter Optimization using GridSearchCV
- XGBoost and LightGBM comparison
- SHAP Explainability
- Probability Confidence Visualization
- Docker Deployment
- Cloud Deployment with Streamlit Community Cloud

---

## 👨‍💻 Author

**Jiya Modi**


LinkedIn: https://www.linkedin.com/in/jiya-modi-7046a6368/

---

⭐ If you found this project useful, consider giving the repository a star!





