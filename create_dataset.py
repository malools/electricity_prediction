import json
import requests
import pandas as pd
import numpy as np
import folium

def get_places(api_key, location, radius, place_type):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    results = data.get("results", [])
    return results

API_KEY = ""
radius = 500  # Radius in meters
place_type = "store"

# Define a bounding box for Paris
lat_min, lat_max = 48.815573, 48.902145  
lng_min, lng_max = 2.224199, 2.469921   

# Create a grid of points (centers of the circles)
grid_step = 0.005  # Adjust step for the grid (approx. 500m)
latitudes = np.arange(lat_min, lat_max, grid_step)
longitudes = np.arange(lng_min, lng_max, grid_step)
grid_points = [(lat, lng) for lat in latitudes for lng in longitudes]

data_shop = []
for lat, lng in grid_points:
    location = f"{lat},{lng}"
    places   = get_places(API_KEY, location, radius, place_type)
    for place in places:
        data_shop.append({
            "name"  : place.get("name"),
            "lat"   : place["geometry"]["location"]["lat"],
            "lng"   : place["geometry"]["location"]["lng"],
            "rating": place.get("rating"),
            "types" : place.get("types")
        })

df_rest = pd.DataFrame(data_rest)
df_rest.to_csv("data/paris_restaurants.csv", index=False)

df_shop = pd.DataFrame(data_shop)
df_shop.to_csv("paris_shops.csv", index=False)


