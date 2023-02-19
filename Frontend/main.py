import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

#st.title("Mapping and Sentiment Analysis of Geo-spatial Data regarding usage of :red[Renewable Energy]")

APP_TITLE = "Mapping and Sentiment Analysis of Geo-spatial Data regarding usage of :orange[Renewable Energy]"

# st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    st.set_page_config(APP_TITLE , layout="wide")
    st.title(APP_TITLE)

    #LOAD DATA
    df = pd.read_csv('C:\My Files\College Documents\Step Presentation\Code\StreamLit\streamlit/DATA/newcleanenergy.csv')

    #DISPLAY THE DATA

    # st.write(df.shape)
    # st.write(df.head())
    # st.write(df.columns)
    # st.write(df['user location'].unique())

    #folium = library that help to visualize geospatial data
    #location = cordinates of the map        
    m = folium.Map(location=[0,0], zoom_start=2)


    # Define a list of options for the dropdown
    #options = ['Option 1', 'Option 2', 'Option 3']
    options = df['Location'].unique()

    # Divide the screen into two columns using beta_columns
    col1, col2, col3, col4 = st.columns((2, 1, 1, 1))
    #col1, col2 = st.columns([1,1])

    with col1:
        folium_static(m)

    # Place the dropdown widget in the right column
    with col3:
        selected_option = st.selectbox('Select an option:', options)

    with col4:
        all_review = st.checkbox('All review')
        positive = st.checkbox('Positive')
        negative = st.checkbox('Negative')
        neutral = st.checkbox('Neutral')

        if all_review:
            st.write('Great!')
            chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

            st.line_chart(chart_data)


if __name__ == '__main__':
    main()


