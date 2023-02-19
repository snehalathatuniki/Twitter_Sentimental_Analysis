#st.line_chart(data = data, x=None, y=None, width=0, height=0, use_container_width=True)

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)

# geolocator = Nominatim(user_agent="my_app")
    # countries = []
    # for lat in range(-90, 90):
    #     for lon in range(-180, 180):
    #         location = geolocator.reverse(f"{lat}, {lon}")
    #         country = location.raw['address'].get('country')
    #         if country:
    #             countries.append((lat, lon, country))

    # for country in countries:
    #     folium.Marker(location=[country[0], country[1]], popup=country[2]).add_to(m)


    # map = folium.Map(location=[43.6532, -79.3832], zoom_start=13)
    # folium.Marker(location=[43.6532, -79.3832], popup="Toronto, CA").add_to(map)
    # folium_static(map)

import streamlit as st

# Define a list of options for the dropdown
options = ['Option 1', 'Option 2', 'Option 3']

# Create a container with a right-aligned dropdown widget
container = st.container()
with container:
    st.write('Some content on the left side')
    selected_option = st.selectbox('Select an option:', options, index=0, help='Select an option from the dropdown', key='my_dropdown')
    st.write('You selected:', selected_option)

    # Set the container's style to right-align its contents
    container._css = f"box-sizing:border-box;display:flex;justify-content:flex-end;width:100%;"


# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")