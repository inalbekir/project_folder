import pandas as pd
from geopy.geocoders import Nominatim

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
unique_postcodes = df_main['PostCodes'].unique()

# Create a DataFrame to store coordinates
df_coords = pd.DataFrame(columns=['postcode', 'latitude', 'longitude'])

# Get coordinates for each postcode and append to df_coords using pd.concat
coordinates = []
for postcode in unique_postcodes:
    lat, lon = get_lat_lon(postcode)
    coordinates.append({'postcode': postcode, 'latitude': lat, 'longitude': lon})

df_coords = pd.concat([df_coords, pd.DataFrame(coordinates)], ignore_index=True)

# Save the coordinates to a CSV file
df_coords.to_csv('data/postcode_coordinates.csv', index=False)
print("postcode_coordinates.csv has been updated.")
