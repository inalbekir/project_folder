import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def plot_student_heatmap(df):
    df_coords = pd.read_csv('project_folder/data/postcode_coordinates.csv')

    # Ensure the correct columns are present
    expected_columns = ['postcode', 'latitude', 'longitude']
    if not all(col in df_coords.columns for col in expected_columns):
        st.error("The 'postcode' column is missing in postcode_coordinates.csv")
        return None

    # Merge coordinates with the main dataframe
    df = df.merge(df_coords, left_on='PostCodes', right_on='postcode', how='left')

    # Debugging: Print the first few rows of the dataframe
    st.write("Filtered DataFrame (first few rows):")
    st.write(df.head())

    # Drop rows with missing coordinates
    df = df.dropna(subset=['latitude', 'longitude'])

    if df.empty:
        st.warning("No data available for the selected filters.")
        return None

    # Create a heatmap
    fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='Number of Students', radius=10,
                            center=dict(lat=52.3676, lon=4.9041), zoom=7,
                            mapbox_style="stamen-terrain")

    return fig
