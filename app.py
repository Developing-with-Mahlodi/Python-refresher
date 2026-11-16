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
    totalcharges        =st.number_input('Total Charges($)',  0.0, 9000.0, float(tenure * monthlycharges))
    senior              =st.selectbox('Senior Citizen',       ['No', 'Yes'])
    partner             =st.selectbox('Partner',              ['No', 'Yes'])
    dependents          =st.selectbox('Dependents',           ['No', 'Yes'])
    gender              =st.selectbox('Gender',               ['No', 'Yes'])


with col2:
    contract            =st.selectbox('Contract Type',        ['Month-to-month', 'One year', 'Two year'])
    internet            =st.selectbox('Internet Service',     ['DSL', 'Fiber optic', 'No'])
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

#--------------------------------------Predict Buttom-----------------------------------------------------------
if st.button('Predict Churn Risk', use_container_width = True):

    # Build Input Dict
    input_dict ={
        'gender'                 : 1 if gender     == 'Male' else 0,
        'SeniorCitizen'          : 1 if senior     == 'Yes'  else 0,
        'Partner'                : 1 if partner    == 'Yes'  else 0,
        'Dependents'             : 1 if dependents == 'Yes'  else 0,
        'tenure'                 : tenure,
        'PhoneService'           : 1 if phone      == 'Yes'  else 0,
        'MultipleLines'          : 1 if multiple   == 'Yes'  else 0,
        'OnlineSecurity'         : 1 if online_sec == 'Yes'  else 0,
        'OnlineBackup'           : 1 if online_bak == 'Yes'  else 0,
        'DeviceProtection'       : 1 if device     == 'Yes'  else 0,
        'TechSupport'            : 1 if tech       == 'Yes'  else 0,
        'StreamingTV'            : 1 if tv         == 'Yes'  else 0,
        'StreamingMovies'        : 1 if movies     == 'Yes'  else 0,
        'PaperlessBilling'       : 1 if paperless  == 'Yes'  else 0,
        'MonthlyCharges'         : monthlycharges,
        'TotalCharges'           : totalcharges,
        'InternetService_DSL'            : 1 if internet  == 'DSL'            else 0,
        'InternetService_Fibre optic'    : 1 if internet  == 'Fiber optic'    else 0,
        'InternetService_No'             : 1 if internet  == 'No'             else 0,
        'Contract_Month-to-month'        : 1 if contract  == 'Month-to-month' else 0,
        'Contract_One year'              : 1 if contract  == 'One year'       else 0,
        'Contract_Two year'              : 1 if contract  == 'Two year'       else 0,
        'PaymentMethod_Bank transfer (automatic)'        : 1 if payment == 'Bank transfer (automatic)' else 0,
        'PaymentMethod_Credit card (automatic)'          : 1 if payment == 'Credit card (automatic)'   else 0,
        'PaymentMethod_Electronic check'                 : 1 if payment == 'Electronic check'          else 0,
        'PaymentMethod_Mailed check'                     : 1 if payment == 'Mailed check'              else 0,
          }