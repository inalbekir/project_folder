import pandas as pd
from geopy.geocoders import Nominatim
import time

def get_lat_lon(postcode):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(postcode)
        return location.latitude, location.longitude
    except:
        return None, None

# Load the main dataset
df_main = pd.read_csv('data/updated_coderminds.csv')

# Extract unique postcodes
postcodes = df_main['PostCodes'].unique()

# Load existing coordinates
df_coords = pd.read_csv('data/postcode_coordinates.csv')

# Filter out postcodes already present in the coordinates file
new_postcodes = set(postcodes) - set(df_coords['postcode'])

# Get coordinates for new postcodes
new_coords = []
for postcode in new_postcodes:
    lat, lon = get_lat_lon(postcode)
    if lat and lon:
        new_coords.append({'postcode': postcode, 'latitude': lat, 'longitude': lon})
    time.sleep(1)  # To prevent being blocked by the geocoding service

# Convert to DataFrame
df_new_coords = pd.DataFrame(new_coords)

# Append new coordinates to existing ones
df_coords = pd.concat([df_coords, df_new_coords])

# Save updated coordinates
df_coords.to_csv('data/postcode_coordinates.csv', index=False)

print("postcode_coordinates.csv has been updated and saved.")
