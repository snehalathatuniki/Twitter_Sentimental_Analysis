import streamlit as st 
import pandas as pd


APP_TITLE = "Mapping and Sentiment Analysis of Geo-spatial Data regarding usage of :orange[Renewable Energy]"
st.set_page_config(APP_TITLE , layout="wide")
st.title(APP_TITLE)

df = pd.read_csv('C:\My Files\College Documents\Step Presentation\Code\StreamLit\streamlit/DATA/newcleanenergy.csv')

options = df['Location'].unique()

selected_option = st.selectbox('Select an option:', options)
