import folium 
import pandas as pd

paris_map_restaurants = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
paris_restaurants_df  = pd.read_csv('data/paris_restaurants.csv')

for _, row in paris_restaurants_df.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lng"]],
        radius=5,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        popup=f"{row['name']} (Rating: {row['rating']})"
    ).add_to(paris_map_restaurants)

paris_map_shops = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
paris_shops_df  = pd.read_csv('data/paris_shops.csv')

for _, row in paris_shops_df.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lng"]],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        popup=f"{row['name']} (Rating: {row['rating']})"
    ).add_to(paris_map_shops)

paris_map_restaurants.save("maps/paris_restaurants_map.html")
paris_map_shops.save("maps/paris_shops_map.html")
