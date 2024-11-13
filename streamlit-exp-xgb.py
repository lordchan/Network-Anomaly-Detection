# Importing required libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
import requests
import pickle
from io import BytesIO

# Loading the model from GitHub
@st.cache_data
def load_model_from_github():
    url = "https://github.com/username/repo_name/path_to_model.pkl"  # Replace with your model's GitHub URL
    response = requests.get(url)
    model = pickle.load(BytesIO(response.content))
    return model

# Load the model
model = load_model_from_github()

# Streamlit UI
st.title("🚀 Fun and Interactive XGBoost Predictor")
st.write("Enter your details below to get predictions using our XGBoost model!")

# Define the input fields
# Adjust these according to the model's features
age = st.slider("Age", 18, 100, 25)
income = st.number_input("Income (in USD)", 0, 100000, 50000)
score = st.slider("Credit Score", 300, 850, 600)
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed", "Student"])

# Convert user input into a DataFrame for the model
user_input = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Credit_Score": [score],
    "Employment_Status": [1 if employment_status == "Employed" else 0]  # Example encoding
})

# Predict button
if st.button("Predict"):
    prediction = model.predict(user_input)[0]  # Assuming binary output (0 or 1)
    if prediction == 1:
        st.success("🎉 Congratulations! The model predicts a positive outcome!")
    else:
        st.error("🔴 Unfortunately, the model predicts a negative outcome.")

# Add some styling
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
    }
    .stTitle {
        font-size: 2.5em;
        color: #FF6347;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
