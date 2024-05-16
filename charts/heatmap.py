import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
import streamlit as st

# Function to load data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to get latitude and longitude
@st.cache
def get_lat_lon(postcode):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(postcode)
        return location.latitude, location.longitude
    except:
        return None, None

# Function to create heatmap
def plot_student_heatmap(df):
    # Aggregate the data by PostCodes
    postcode_counts = df['PostCodes'].value_counts().reset_index()
    postcode_counts.columns = ['PostCodes', 'Number of Students']

    # Get latitude and longitude for each postcode
    postcode_counts[['latitude', 'longitude']] = postcode_counts['PostCodes'].apply(
        lambda x: pd.Series(get_lat_lon(x))
    )

    # Drop rows with missing coordinates
    postcode_counts = postcode_counts.dropna(subset=['latitude', 'longitude'])

    # Create a heat
