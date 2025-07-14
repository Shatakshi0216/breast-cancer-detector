# Breast Cancer Prediction App 🎗️

A Streamlit web application that predicts whether a tumor is benign or malignant based on input features from the Breast Cancer Wisconsin dataset.

## 🔍 Overview

- Built using Python, Streamlit, and Scikit-learn  
- Takes user input of 30 features from the dataset  
- Predicts tumor type using a trained classification model

## 📁 Project Files

| File                   | Description                                  |
|------------------------|----------------------------------------------|
| `app.py`               | Streamlit frontend code                      |
| `model.pkl`            | Trained machine learning model               |
| `data.csv`             | Dataset used for training                    |
| `Breast_Cancer.ipynb`  | Model training notebook                      |
| `requirements.txt`     | Required Python libraries                    |
| `README.md`            | Project documentation                        |

## 🚀 Run This Project Locally

```bash
git clone https://github.com/your-username/breast-cancer-prediction-app.git
cd breast-cancer-prediction-app
pip install -r requirements.txt
streamlit run app.py
