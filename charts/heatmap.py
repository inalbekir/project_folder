# /project_folder/charts/heatmap.py
import pandas as pd
import plotly.express as px

def plot_student_heatmap(df, selected_years):
    # Filter by selected educational years
    df_filtered = df[df['Educational Year'].isin(selected_years)]

    # Group by latitude and longitude to count the number of students
    summary = df_filtered.groupby(['Latitude', 'Longitude']).size().reset_index(name='Number of Students')

    # Create the heatmap
    fig = px.density_mapbox(
        summary,
        lat='Latitude',
        lon='Longitude',
        z='Number of Students',
        radius=10,
        center=dict(lat=52.1326, lon=5.2913),  # Center on the Netherlands
        zoom=7,
        mapbox_style="stamen-terrain",
        title='Heatmap of Student Distribution'
    )

    return fig
