# /project_folder/charts/courses.py
import pandas as pd
import plotly.express as px


def plot_students_by_period_and_program(df, selected_periods, selected_programs):
    # Filter DataFrame by selected periods if provided
    if selected_periods:
        df = df[df['Period'].isin(selected_periods)]

    # Further filter by selected programs if provided
    if selected_programs:
        df = df[df['Product Name'].isin(selected_programs)]

    # Group by 'Educational Year', 'Period', and now 'Product Name'
    summary = df.groupby(['Educational Year', 'Period', 'Product Name'])['StudentID'].nunique().reset_index(
        name='Number of Students')

    fig = px.bar(summary, x='Educational Year', y='Number of Students', color='Product Name',
                 title='Number of Students in Different Types of Programs Depending on the Period')
    return fig