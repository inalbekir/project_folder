import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import streamlit as st

# Function to get latitude and longitude with retries
def get_lat_lon(postcode):
    geolocator = Nominatim(user_agent="geoapiExercises")
    for attempt in range(3):  # Retry up to 3 times
        try:
            location = geolocator.geocode(postcode, timeout=10)
            if location:
                return location.latitude, location.longitude
        except GeocoderTimedOut:
            continue
    return None, None

# Function to create heatmap
def plot_student_heatmap(df):
    # Filter the data to ensure only Dutch postcodes are used
    df = df[df['PostCodes'].str.match(r'^[1-9][0-9]{3}\s?[A-Z]{2}$')]

    # Aggregate the data by PostCodes
    postcode_counts = df['PostCodes'].value_counts().reset_index()
    postcode_counts.columns = ['PostCodes', 'Number of Students']

    # Get latitude and longitude for each postcode
    postcode_counts[['latitude', 'longitude']] = postcode_counts['PostCodes'].apply(
        lambda x: pd.Series(get_lat_lon(x))
    )

    # Print debug information
    st.write(postcode_counts.head())

    # Drop rows with missing coordinates
    postcode_counts = postcode_counts.dropna(subset=['latitude', 'longitude'])

    # Ensure there are valid coordinates
    if postcode_counts.empty:
        st.write("No valid coordinates found.")
        return None

    # Create a heatmap using Plotly
    fig = px.density_mapbox(postcode_counts, lat='latitude', lon='longitude', z='Number of Students',
                            radius=10, center=dict(lat=52.3676, lon=4.9041), zoom=7,
                            mapbox_style="open-street-map")

    return fig
