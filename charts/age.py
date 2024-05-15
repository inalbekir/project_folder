# /project_folder/charts/program_age.py
import pandas as pd
import plotly.express as px


def plot_students_by_program_and_age(df, selected_years, selected_programs):
    # Filter by educational year
    df = df[df['Educational Year'].isin(selected_years)]

    # Further filter by selected programs if provided
    if selected_programs:
        df = df[df['Product Name'].isin(selected_programs)]

    # Group by 'Educational Year', 'Age', and 'Product Name'
    summary = df.groupby(['Educational Year', 'Student Age', 'Product Name'])['StudentID'].nunique().reset_index(
        name='Number of Students')

    fig = px.bar(summary, x='Educational Year', y='Number of Students', color='Product Name', barmode='stack',
                 title='Number of Students in Different Types of Programs Depending on Year and Age',
                 facet_col='Student Age', category_orders={"Student Age": sorted(df['Student Age'].unique())})

    return fig
