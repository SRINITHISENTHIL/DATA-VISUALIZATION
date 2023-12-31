# -*- coding: utf-8 -*-
"""BICYCLE DATASET ANALYSIS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AffZLjiyo2gmk_O3R7a9Bdeu8_Mp63Wy
"""

import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Load the GeoDataFrame with pedestrian paths or sidewalks
bicycle_data = gpd.read_file("/content/export (3).geojson")

# Visualize pedestrian paths density using Geopandas
fig, ax = plt.subplots(figsize=(10, 10))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
bicycle_data.plot(ax=ax, alpha=0.7, legend=True, cax=cax)
ax.set_title("Pedestrian Paths Density")

# Display the plot
plt.show()

# Create a Folium map centered around the pedestrian data
map_center = [bicycle_data.geometry.centroid.y.mean(), bicycle_data.geometry.centroid.x.mean()]
mymap = folium.Map(location=map_center, zoom_start=14)

# Add pedestrian paths to the map
folium.GeoJson(bicycle_data).add_to(mymap)

# Display the map in the Jupyter Notebook
display(mymap)