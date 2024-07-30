import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib


model = joblib.load("model.joblib")


# Create a Streamlit app
st.title("Loan Prediction App")

# Create input fields for user data
st.subheader("Enter Your Details:")


col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", [1, 0])
    married = st.selectbox("Married", [1, 0])
    dependents = st.selectbox("Dependents", [1, 0])
    education = st.selectbox("Education", [1, 0])
    self_employed = st.selectbox("Self Employed", [1, 0])

with col2:
    applicant_income = st.number_input("Applicant Income")
    coapplicant_income = st.number_input("Coapplicant Income")
    loan_amount = st.number_input("Loan Amount")
    loan_amount_term = st.number_input("Loan Amount Term")
    credit_history = st.selectbox("Credit History", [1, 0])
    property_area = st.selectbox("Property Area", [1, 2, 3])

# Create a button to submit user data
if st.button("Get Prediction"):
    # Create a new DataFrame with user input
    new_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Get prediction from the loaded model
    predictions = model.predict(new_data)
    if predictions >0.5:
        st.subheader("Prediction:")
        st.write("Yes will take loan ")
    else:
        st.subheader("Prediction:")
        st.write("Yes will take loan ")
   