import sqlite3
import matplotlib.pyplot as plt
import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

APP_TITLE = "Mapping and Sentiment Analysis of Geo-spatial Data regarding usage of :orange[Renewable Energy]"

sqliteConnection = sqlite3.connect('C:\My Files\College Documents\Step Presentation\Code\DB\SentimentDB1.db')

def formatData(name):
    return str(name).replace("(","").replace(")","").replace(",","").replace("'","")


#Function to get the list of countries from the DB
def getCountries():
    cursor = sqliteConnection.cursor()
    c_query = "select name from Countries"
    cursor.execute(c_query)
    countries = cursor.fetchall()
    country_list = ["World"]
    for country in countries:
        country_list.append(formatData(country))
    return country_list

#Function to get the selected country's id from the db.
def getCountryIdfromname(name):
    cursor = sqliteConnection.cursor()
    c_query = "select id from Countries where name = '"+name+"'"
    cursor.execute(c_query)
    try:
        return int(formatData(cursor.fetchall()[0]))
    except:
        return 0
         
def getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral):
    cursor = sqliteConnection.cursor()
    totalCount = 0

    cc= ""
    acc=""
    if countryId != 0:
        cc = " where CountryId = "+str(countryId)
        acc = " and CountryId = "+str(countryId)
    
    t_query = "select count(*) from Tweets"+cc
    cursor.execute(t_query)
    totalCount = int(formatData(cursor.fetchall()[0]))

    if all:

        p_query = "select count(*) from Tweets where Polarity = 'Positive'"+acc
        cursor.execute(p_query)
        pCount = int(formatData(cursor.fetchall()[0]))

        neg_query = "select count(*) from Tweets where Polarity = 'Negative'"+acc
        cursor.execute(neg_query)
        negCount = int(formatData(cursor.fetchall()[0]))

        neu_query = "select count(*) from Tweets where Polarity = 'Neutral'"+acc
        cursor.execute(neu_query)
        neuCount = int(formatData(cursor.fetchall()[0]))

        label = ["Positive","Negative","Neutral"]
        counts = [pCount,negCount,neuCount]
        return [label,counts,totalCount]
    elif positive:
        p_query = "select count(*) from Tweets where Polarity = 'Positive'"+acc
        cursor.execute(p_query)
        pCount = int(formatData(cursor.fetchall()[0]))
        label = ["Positive"]
        counts = [pCount]

        if negative:
            neg_query = "select count(*) from Tweets where Polarity = 'Negative'"+acc
            cursor.execute(neg_query)
            negCount = int(formatData(cursor.fetchall()[0]))
            label.append("Negative")
            counts.append(negCount)
        
        if neutral:
            neu_query = "select count(*) from Tweets where Polarity = 'Neutral'"+acc
            cursor.execute(neu_query)
            neuCount = int(formatData(cursor.fetchall()[0]))
            label.append("Neutral")
            counts.append(neuCount)

        if negative == False | neutral == False:  
            o_query = "select count(*) from Tweets where Polarity is not 'Positive'"+acc
            cursor.execute(o_query)
            oCount = int(formatData(cursor.fetchall()[0]))
            label.append("Other")
            counts.append(oCount)
        
        return [label,counts,totalCount]
    elif negative:
        neg_query = "select count(*) from Tweets where Polarity = 'Negative'"+acc
        cursor.execute(neg_query)
        negCount = int(formatData(cursor.fetchall()[0]))
        label = ["Negative"]
        counts = [negCount]

        if neutral:
            neu_query = "select count(*) from Tweets where Polarity = 'Neutral'"+acc
            cursor.execute(neu_query)
            neuCount = int(formatData(cursor.fetchall()[0]))
            label.append("Neutral")
            counts.append(neuCount)

        else:  
            o_query = "select count(*) from Tweets where Polarity is not 'Negative'"+acc
            cursor.execute(o_query)
            oCount = int(formatData(cursor.fetchall()[0]))
            label.append("Other")
            counts.append(oCount)

        return [label,counts,totalCount]
    else:
        neu_query = "select count(*) from Tweets where Polarity = 'Neutral'"+acc
        cursor.execute(neu_query)
        neuCount = int(formatData(cursor.fetchall()[0]))

        o_query = "select count(*) from Tweets where Polarity is not 'Neutral'"+acc
        cursor.execute(o_query)
        oCount = int(formatData(cursor.fetchall()[0]))

        label = ["Neutral","Other"]
        counts = [neuCount,oCount]
        return [label,counts,totalCount]

def getDataForLineChart(countryId,all,positive,negative,neutral):

    cc=""
    if countryId != 0:
        cc = " where CountryId = "+str(countryId)

    cursor = sqliteConnection.cursor()

    counts = []
    columns = []

    p_query2020 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2020 and Polarity='Positive'"+cc
    p_query2021 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2021 and Polarity='Positive'"+cc
    p_query2022 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2022 and Polarity='Positive'"+cc

    neg_query2020 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2020 and Polarity='Negative'"+cc
    neg_query2021 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2021 and Polarity='Negative'"+cc
    neg_query2022 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2022 and Polarity='Negative'"+cc

    neu_query2020 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2020 and Polarity='Neutral'"+cc
    neu_query2021 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2021 and Polarity='Neutral'"+cc
    neu_query2022 = "select count(*) from Tweets where CAST(strftime('%Y',DateTime) as decimal)=2022 and Polarity='Neutral'"+cc

    if all:
        columns = ["Positive","Negative","Neutral"]
        
        cursor.execute(p_query2020)
        p20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p20Count)
        cursor.execute(p_query2021)
        p21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p21Count)
        cursor.execute(p_query2022)
        p22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p22Count)

        cursor.execute(neg_query2020)
        n20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(n20Count)
        cursor.execute(neg_query2021)
        neg21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neg21Count)
        cursor.execute(neg_query2022)
        neg22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neg22Count)

        cursor.execute(neu_query2020)
        neu20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu20Count)
        cursor.execute(neu_query2021)
        neu21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu21Count)
        cursor.execute(neu_query2022)
        neu22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu22Count)

    if positive:
        columns.append("Positive")
        cursor.execute(p_query2020)
        p20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p20Count)
        cursor.execute(p_query2021)
        p21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p21Count)
        cursor.execute(p_query2022)
        p22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(p22Count)

    if negative:
        columns.append("Negative")
        cursor.execute(neg_query2020)
        neg20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neg20Count)
        cursor.execute(neg_query2021)
        neg21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neg21Count)
        cursor.execute(neg_query2022)
        neg22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neg22Count)

    if neutral:
        columns.append("Neutral")
        cursor.execute(neu_query2020)
        neu20Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu20Count)
        cursor.execute(neu_query2021)
        neu21Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu21Count)
        cursor.execute(neu_query2022)
        neu22Count = int(formatData(cursor.fetchall()[0]))
        counts.append(neu22Count)

    return columns,counts

def main():
    st.set_page_config(APP_TITLE , layout="wide")
    st.title(APP_TITLE)
    
    hide_streamlit_style = """<style> #MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    all = True
    positive = False
    negative = False
    neutral = False

    col1, col2, col3, col4 = st.columns((3, 1,0.4,0.4))

    with col2:
        selected_option = st.selectbox('Select the Country:', getCountries())
        countryId = getCountryIdfromname(selected_option)
        getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral)

    with col3:
        all = st.checkbox("All",value=True)
        if all:
            neutral = st.checkbox("Neutral",disabled=True)
        else:
            neutral = st.checkbox("Neutral")
    
    with col4:
        if all:
            positive = st.checkbox("Positive",disabled=True)
            negative = st.checkbox("Negative",disabled=True)
        else:
            positive = st.checkbox("Positive")
            negative = st.checkbox("Negative")

    co1,co2 = st.columns((3,1.8))

    with co2:
        # labels = ["Positive","Negative","Neutral"]
        # getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral)
        labels,values,totalCount = getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral)

        tot = "<h4 style='text-align: center;'> Total Tweets : "+str(totalCount) +"</h4>"

        st.markdown(tot, unsafe_allow_html=True)

        #Getting data from DB
        # labels,values,totalCount = getTweetDataAccordingtoFilter(countryId,all,positive,negative,neutral)

        # Plot pie chart using Matplotlib
        fig, ax = plt.subplots(figsize=(4,2))
        plt.rcParams['font.size'] = 7
        ax.pie(values, labels=labels,wedgeprops={'edgecolor': 'white', 'linewidth': 2.5}, autopct='%0.1f%%')
        centre_circle = plt.Circle((0,0),0.35,fc='white')
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        # Show the pie chart in Streamlit
        st.pyplot(fig)

        # Create a dataframe
        data = pd.DataFrame({'Sentiment': labels,'Tweet Count': values,'Color': ['#1F77B4', '#FF7F0E', '#2CA02C']})

        # Create the bar chart using Altair
        bars = alt.Chart(data).mark_bar().encode( x='Sentiment',y='Tweet Count',color=alt.Color('Color', scale=None),
                tooltip=['Sentiment', 'Tweet Count']).properties(width=300,height=400)

        # Display the chart in Streamlit
        st.altair_chart(bars, use_container_width=True)


    with co1:
        years = ["2020","2021","2022"]
        columns,counts = getDataForLineChart(countryId,all,positive,negative,neutral)
       
        print(columns)
        print(counts)
        # print(counts[0:3])
        # print(counts[3:6])
        # print(counts[6:9])

        fig = go.Figure()
        for c in columns:
            print(c)
            if c == 'Positive': yy = counts[0:3]
            elif c == 'Negative': yy = counts[3:6]
            else: yy = counts[6:9]
            print(yy)
            fig = fig.add_trace(go.Scatter(x=years, y=yy, name=c))
            

        st.plotly_chart(fig)

if __name__ == '__main__':
    main()
