import sqlite3
import matplotlib.pyplot as plt
import streamlit as st 
import altair as alt
import plotly.express as px 
import pandas as pd

APP_TITLE = "Mapping and Sentiment Analysis of Geo-spatial Data regarding usage of :orange[Renewable Energy]"

sqliteconnection = sqlite3.connect('D:\CLG\Loyalist\SEM 1\STEP PRESENTATION\Project - Sentimental Analysis\streamlit\SentimentDB.db')

def formatCountryName(name):
    return str(name).replace("(","").replace(")","").replace(",","").replace("'","")

def getCountries():
    cursor = sqliteconnection.cursor()
    c_query = "select name from Countries"
    cursor.execute(c_query)
    countries = cursor.fetchall()
    country_list = []
    country_list.append("World")
    for country in countries:
        country_list.append(formatCountryName(country))
    return country_list

def getCountryIdfromname(name):
    cursor = sqliteconnection.cursor()
    c_query = "select id from Countries where name = '"+name+"'"
    cursor.execute(c_query)
    try:
        return int(formatCountryName(cursor.fetchall()[0]))
    except:
        return 0
         
def getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral):
    cursor = sqliteconnection.cursor()
    if countryId == 0:
        if all:
            t_query = "select count(*) from Tweets"
            cursor.execute(t_query)
            totalCount = int(formatCountryName(cursor.fetchall()[0]))
            print(totalCount)

            p_query = "select count(*) from Tweets where Polarity = 'Positive'"
            cursor.execute(p_query)
            pCount = int(formatCountryName(cursor.fetchall()[0]))
            print(pCount)

            neg_query = "select count(*) from Tweets where Polarity = 'Negative'"
            cursor.execute(neg_query)
            negCount = int(formatCountryName(cursor.fetchall()[0]))
            print(negCount)

            neu_query = "select count(*) from Tweets where Polarity = 'Neutral'"
            cursor.execute(neu_query)
            neuCount = int(formatCountryName(cursor.fetchall()[0]))
            print(neuCount)

            return pCount,negCount,neuCount
    else:
        if positive:
            p_query = "select count(*) from Tweets where CountryId = "+countryId+" and Polarity = 'Positive'"


def main():
    st.set_page_config(APP_TITLE , layout="wide")
    st.title(APP_TITLE)
    
    col1, col2, col3, col4, col5 = st.columns((2, 1, 1,0.4,0.4))

    with col3:
        selected_option = st.selectbox('Select the Country:', getCountries())
        countryId = getCountryIdfromname(selected_option)
            # Create lists to hold data
        

    with col4:

        all = st.checkbox("All",value=True)
        neutral = st.checkbox("Neutral")

        

        
     
    with col5:
        
        positive = st.checkbox("Positive")
        negative = st.checkbox("Negative")

    co1,co2,co3 = st.columns((2,1,1.8))

    with co3:
        labels = ["Positive","Negative","Neutral"]
        values = getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral)

        # Loop through data and append to lists
        # Plot pie chart using Matplotlib
        fig, ax = plt.subplots(figsize=(2,2))
        plt.rcParams['font.size'] = 7
        ax.pie(values, labels=labels,wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')

        # Show the pie chart in Streamlit
        st.pyplot(fig)

        
        # Create a sample dataframe
        data = pd.DataFrame({
            'Category': ["Positive","Negative","Neutral"],
            'No of Tweet': values,
            'Color': ['#1F77B4', '#FF7F0E', '#2CA02C']
        })

        # Create the bar chart using Altair
        bars = alt.Chart(data).mark_bar().encode(
            x='Category',
            y='No of Tweet',
            color=alt.Color('Color', scale=None),
            tooltip=['Category', 'No of Tweet']
        ).properties(
            width=300,
            height=400
        )

        # Display the chart in Streamlit
        st.altair_chart(bars, use_container_width=True)      



if __name__ == '__main__':
    main()


