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