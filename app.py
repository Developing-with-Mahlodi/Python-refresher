from flask import Flask

# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model, Scaler, and Features
model    = joblib.load('churn_model_2.pkl')
scaler   = joblib.load('churn_scaler.pkl')
features = joblib.load('feature_columns.pkl')

#---------------------------Page Config-----------------------------------------

st.set_page_config(page_title = 'Churn Predictor', page_icon = '%%', layout = 'centered')
st.title('%% Telecom Customern Churn Preductor')
st.markdown('Fill in the customer details below to predict churn risk')
st.divider()

#----------------------------------------Input Form---------------------------------------------

col1, col2, col3 =st.columns(3)
with col1:
    tenure              =st.slider('Tenure (months)',        0, 72, 16)
    monthlycharges      =st.slider('Monthly Charges($)',     18, 119, 65)
    totalCharges        =st.number_input('Total Charges($)',  0.0, 9000, float(tenure * monthlycharges))
    senior              =st.selectbox('Senior Citizen',       ['No', 'Yes'])
    partner             =st.selectbox('Partner',              ['No', 'Yes'])
    dependents          =st.selectbox('Dependents',           ['No', 'Yes'])
    gender              =st.selectbox('Gender',               ['No', 'Yes'])


with col2:
    contract            =st.selectbox('Contract Type',        ['Month-to-month', 'One year', 'Two year'])
    internet            =st.selectbox('Internet Service',     ['DSL', 'Fibre optic', 'No'])
    payment             =st.selectbox('Payment Method',       ['Electronic check', 'Mailed check', 
                                                               'Bank transfer (automatic)', 
                                                               'Credit card (automatic)'])
    paperless           =st.selectbox('Paperless Billing',    ['No', 'Yes'])
    phone               =st.selectbox('Phone Service',        ['No', 'Yes'])
    multiple            =st.selectbox('Multiple Lines',       ['No', 'Yes'])

with col3:
    online_sec          =st.selectbox('Online Security',      ['No', 'Yes'])
    online_bak          =st.selectbox('Online Backup',        ['No', 'Yes'])
    device              =st.selectbox('Device Protection',    ['No', 'Yes'])
    tech                =st.selectbox('Tech Support',         ['No', 'Yes'])
    tv                  =st.selectbox('Streaming TV',         ['No', 'Yes'])
    movies              =st.selectbox('Streaming Movies',     ['No', 'Yes'])
st.divider()