# /project_folder/charts/age.py
import pandas as pd
import plotly.express as px


def plot_students_by_program_and_age(df, selected_years, selected_programs, age_range):
    # Filter by educational year
    df = df[df['Educational Year'].isin(selected_years)]

    # Further filter by selected programs if provided
    if selected_programs:
        df = df[df['Product Name'].isin(selected_programs)]

    # Further filter by selected age range if provided
    df = df[(df['Student Age'] >= age_range[0]) & (df['Student Age'] <= age_range[1])]

    # Group by 'Educational Year', 'Student Age', and 'Product Name'
    summary = df.groupby(['Educational Year', 'Student Age', 'Product Name'])['StudentID'].nunique().reset_index(
        name='Number of Students')

    # Create a treemap chart
    fig = px.treemap(summary, path=['Educational Year', 'Product Name', 'Student Age'], values='Number of Students',
                     title='Number of Students in Different Programs Depending on Year and Age')

    fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    return fig