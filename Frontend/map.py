# import streamlit as st
# from mpl_toolkits.basemap import Basemap
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(8, 8))
# m = Basemap(projection="ortho", lat_0=0, lon_0=0)
# m.bluemarble()

# st.pyplot(fig)

# import streamlit as st
# import geopandas as gpd
# import matplotlib.pyplot as plt

# world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
# world = world[world["name"] != "Antarctica"]

# color_column = "gdp_md_est"
# vmin, vmax = world[color_column].min(), world[color_column].max()

# fig, ax = plt.subplots(figsize=(10, 6))
# world.plot(column=color_column, cmap="Blues", ax=ax)
# ax.axis("off")

# cbar = plt.colorbar(ax.get_children()[2], fraction=0.03, pad=0.04)
# cbar.ax.tick_params(labelsize=8)
# cbar.ax.set_ylabel(color_column, size=8)

# st.pyplot(fig)

import streamlit as st
import pandas as pd
import pydeck as pdk

#Read the data from the online website that provide the country map
df = pd.read_csv("https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson")

#show the chart using the pydeck library 
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["Longitude", "Latitude"],
            get_color=[200, 30, 0, 160],
            get_radius=100000,
        ),
    ],
))
