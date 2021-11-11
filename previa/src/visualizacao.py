import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
from tqdm import tqdm

#df = pd.read_csv('postos_policiais_geocoded.csv', index_col='id')
df = pd.read_csv('dados_crimes.csv', index_col='NUM_BO')

# Create a map object and center it to the avarage coordinates to m
m = folium.Map(location=df[["LATITUDE", "LONGITUDE"]].mean().to_list(), zoom_start=2)# if the points are too close to each other, cluster them, create a cluster overlay with MarkerCluster, add to m
marker_cluster = MarkerCluster().add_to(m)# draw the markers and assign popup and hover texts
# add the markers the the cluster layers so that they are automatically clustered
for i,r in tqdm(df.iterrows(), total=len(df)):
    location = (r["LATITUDE"], r["LONGITUDE"])
    folium.Marker(location=location,
                      popup = r['TIPO'],
                      tooltip=r['TIPO'])\
    .add_to(marker_cluster)

m.save("folium_map_crimes.html")
